#!/usr/bin/env python3
"""
PotatoCraft multiplayer client.

Keep this file next to potatocraft.py (your unchanged single-player game) and run:

    python potatocraft_mp.py --server https://YOUR-SERVER/api.php --room friends --name Tom

It asks for anything you leave out (a password is always asked: it protects your name and your
saved inventory on the server).  Requires:  pip install pygame     (nothing else - plain standard library)

What is shared between everybody in a room:
  * the world: same seed, and every block anybody places or breaks (all three dimensions)
  * the other players: position, direction, held item, health, name tag
  * chat: press T and type, Enter sends  (commands start with /  - try /help, /players, /tp name)
  * the time of day
  * your own progress: inventory, armor, ender chest, XP, health, position are saved on the server
    (F6 while paused, every 2 minutes, and on quit) and restored when you rejoin with the same name

What stays local to each player (see README): mobs, dropped items, chest / furnace contents,
redstone machines are simulated by each client from the shared blocks.
"""
import argparse
import getpass
import hashlib
import http.client
import json
import math
import os
import queue
import sys
import threading
import time
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.getcwd()):
    if os.path.exists(os.path.join(p, "potatocraft.py")):
        sys.path.insert(0, p)
        break
try:
    import potatocraft as pc
except ImportError as ex:
    if ex.name == "pygame":
        sys.exit("pygame is missing:  pip install pygame")
    sys.exit("potatocraft.py must be in the same folder as potatocraft_mp.py (%s)" % ex)
import pygame

SYNC_INTERVAL = 0.30          # seconds between server round trips
MAX_BLOCKS_PER_SYNC = 400
CHEAT_CMDS = ("give", "setblock", "fill", "tick")
CONFIG_FILE = os.path.join(HERE, "potatocraft_mp_config.json")


# --------------------------------------------------------------------------- #
#  Hook World.set so every block change made by this player is recorded
# --------------------------------------------------------------------------- #
_orig_set = pc.World.set
pc.World.mp = None


def _hooked_set(self, x, y, v):
    mp = self.mp
    if mp is not None and 0 <= x < pc.WW and 0 <= y < pc.WH and self.cols[x][y] != v:
        _orig_set(self, x, y, v)
        mp.on_local_set(self.dim, x, y, int(v))
    else:
        _orig_set(self, x, y, v)


pc.World.set = _hooked_set


# --------------------------------------------------------------------------- #
#  Saving a player to JSON (never pickle: data comes from a server)
# --------------------------------------------------------------------------- #
def enc(o):
    if isinstance(o, pc.Dur):
        return {"__dur": int(o), "ench": dict(o.ench) if o.ench else None}
    if o is None or isinstance(o, (bool, str)):
        return o
    if isinstance(o, int):
        return int(o)
    if isinstance(o, float):
        return float(o)
    if isinstance(o, list):
        return [enc(v) for v in o]
    if isinstance(o, tuple):
        return {"__t": [enc(v) for v in o]}
    if isinstance(o, dict):
        return {"__d": [[enc(k), enc(v)] for k, v in o.items()]}
    return None


def dec(o):
    if isinstance(o, list):
        return [dec(v) for v in o]
    if isinstance(o, dict):
        if "__dur" in o:
            d = pc.Dur(int(o["__dur"]))
            if isinstance(o.get("ench"), dict):
                d.ench = {str(k): int(v) for k, v in o["ench"].items()}
            return d
        if "__t" in o:
            return tuple(dec(v) for v in o["__t"])
        if "__d" in o:
            return {dec(k) if not isinstance(dec(k), list) else tuple(dec(k)): dec(v) for k, v in o["__d"]}
    return o


def clean_stack(s, depth=0):
    """Return a safe stack or None - the server data must never crash the game."""
    if not isinstance(s, list) or len(s) < 2 or depth > 2:
        return None
    item, n = s[0], s[1]
    if not isinstance(item, int) or isinstance(item, bool) or item not in pc.ITEMS or item in pc.NO_ITEM:
        return None
    if not isinstance(n, int) or n < 1 or n > 64:
        return None
    extra = s[2] if len(s) > 2 else None
    if isinstance(extra, list):                                  # shulker box contents
        extra = [clean_stack(x, depth + 1) for x in extra[:27]]
        extra += [None] * (27 - len(extra))
    elif isinstance(extra, dict):                                # written book
        pages = extra.get("pages")
        extra = {"pages": [str(x)[:pc.BOOK_PAGE_CHARS] for x in pages[:pc.BOOK_MAX_PAGES]]} if isinstance(pages, list) else None
    elif not isinstance(extra, int) or isinstance(extra, bool):
        extra = None
    return [item, n, extra]


def clean_list(lst, size):
    if not isinstance(lst, list):
        return [None] * size
    out = [clean_stack(x) for x in lst[:size]]
    return out + [None] * (size - len(out))


# --------------------------------------------------------------------------- #
#  HTTP client (keep-alive, runs in a background thread)
# --------------------------------------------------------------------------- #
class NetError(Exception):
    def __init__(self, msg, status=0):
        super().__init__(msg)
        self.status = status


class Net:
    def __init__(self, server, room, name, password):
        server = server.strip()
        if "://" not in server:
            server = "https://" + server
        u = urllib.parse.urlparse(server)
        path = u.path or "/"
        if not path.endswith(".php"):
            path = path.rstrip("/") + "/api.php"
        self.https = u.scheme == "https"
        self.host, self.port, self.path = u.hostname, u.port, path
        self.room, self.name, self.password = room, name, password
        self.token, self.cursor = "", ""
        self.conn = None
        self.conn_lock = threading.Lock()
        self.stop = threading.Event()
        self.fails = 0
        self.last_ms = 0

    def call(self, action, payload=None, timeout=10):
        body = dict(payload or {})
        body.update(room=self.room, name=self.name)
        if self.token:
            body["token"] = self.token
        raw = json.dumps(body, separators=(",", ":")).encode()
        with self.conn_lock:
            for attempt in (0, 1):
                try:
                    if self.conn is None:
                        cls = http.client.HTTPSConnection if self.https else http.client.HTTPConnection
                        self.conn = cls(self.host, self.port, timeout=timeout)
                    t0 = time.time()
                    self.conn.request("POST", "%s?action=%s" % (self.path, action), raw,
                                      {"Content-Type": "application/json", "Accept": "application/json",
                                       "User-Agent": "Mozilla/5.0 (compatible; PotatoCraft/1.0)"})
                    r = self.conn.getresponse()
                    data = r.read()
                    self.last_ms = int((time.time() - t0) * 1000)
                    break
                except (OSError, http.client.HTTPException) as ex:
                    try:
                        self.conn.close()
                    except Exception:                                  # noqa
                        pass
                    self.conn = None
                    if attempt:
                        raise NetError("connection failed: %s" % ex)
        try:
            j = json.loads(data.decode("utf-8", "replace"))
        except ValueError:
            snippet = " ".join(data.decode("utf-8", "replace").split())[:120]
            raise NetError("the server sent something that is not JSON (HTTP %d): %s" % (r.status, snippet), r.status)
        if not isinstance(j, dict) or not j.get("ok"):
            raise NetError((j or {}).get("error", "HTTP %d" % r.status) if isinstance(j, dict) else "bad reply", r.status)
        return j

    def join(self, create_code=""):
        j = self.call("join", dict(pw=self.password, create_code=create_code))
        self.token, self.cursor = j["token"], j.get("cursor", "")
        return j

    def start(self, game):
        self.game = game
        threading.Thread(target=self._loop, daemon=True).start()

    def _loop(self):
        g = self.game
        while not self.stop.is_set():
            t0 = time.time()
            payload, undo = g.net_payload()
            more = False
            try:
                payload["cursor"] = self.cursor
                j = self.call("sync", payload)
                self.fails = 0
                self.cursor = j.get("cursor", self.cursor)
                g.inbox.put(j)
                more = bool(j.get("more"))
                if j.get("resync"):
                    s = self.call("snapshot")
                    self.cursor = s.get("cursor", self.cursor)
                    g.inbox.put(dict(snapshot=s.get("blocks", {})))
            except NetError as ex:
                g.net_requeue(undo)
                self.fails += 1
                g.net_error = str(ex)
                if ex.status in (401, 404):
                    g.net_fatal = str(ex)
                    return
            backlog = g.net_backlog()
            wait = 0.03 if (more or backlog) and not self.fails else max(0.0, SYNC_INTERVAL - (time.time() - t0))
            if self.fails:
                wait = min(5.0, 0.5 * self.fails)
            self.stop.wait(wait)


# --------------------------------------------------------------------------- #
#  The multiplayer game
# --------------------------------------------------------------------------- #
class MPGame(pc.Game):
    CMD_NAMES = pc.Game.CMD_NAMES + ("kick", "players", "tp")
    CMD_USAGE = dict(pc.Game.CMD_USAGE,
                     kick="/kick <player> [reason]   - remove a player from the server (admins only)",
                     players="/players   - who is online",
                     tp="/tp <player>   - teleport to a player in the same dimension",
                     help="/help [command]   (type text without a / to chat)")

    def __init__(self, net, info):
        self.net, self.mp_seed = net, info["seed"]
        self.name = net.name
        self.cheats = bool(info.get("cheats"))
        self.admin = bool(info.get("admin"))
        self._fatal_at = None
        self.lock = threading.Lock()
        self.out_blocks, self.out_chat = {}, []
        self.inbox = queue.Queue()
        self.others = {}
        self.block_state = {}                      # dim -> {(x, y): id}  every shared change we know of
        self.net_error, self.net_fatal = "", None
        self._mach = False
        self.out_puts, self.new_containers = [], set()
        self._open_chest = None            # (key, contents list) while a shared chest is open
        self.chest_pending = set()         # chests whose save is still being retried
        self.srv_time = info.get("time", 0)
        super().__init__(new=True, menu=False)
        pygame.display.set_caption("PotatoCraft - %s @ %s" % (net.name, net.room))
        self.world.mp = self
        self.apply_snapshot(info.get("blocks", {}))
        if info.get("data"):
            self.restore_player(info["data"])
        self.sync_time(self.srv_time)
        self.autosave_t = 0.0
        self.chat_add("Joined room '%s' as %s. %d online. Press T to chat." % (net.room, net.name, info.get("online", 1)),
                      (255, 230, 120))
        if not self.cheats:
            self.chat_add("Cheats (creative, /give, /setblock...) are off on this server.", (180, 180, 190))
        net.start(self)

    # ----- world seed -------------------------------------------------------
    def new_game(self, seed=None):
        super().new_game(seed if seed is not None else self.mp_seed)

    # ----- outgoing ---------------------------------------------------------
    def on_local_set(self, dim, x, y, v):
        if v in (pc.CHEST, pc.SHULKER_BOX):
            with self.lock:
                self.new_containers.add((dim, x, y))
        if self._mach:                       # redstone machines run on every client by themselves
            return
        with self.lock:
            self.out_blocks[(dim, x, y)] = v

    def update_machines(self, dt):
        self._mach = True
        try:
            return super().update_machines(dt)
        finally:
            self._mach = False

    def send_chat(self, text):
        with self.lock:
            self.out_chat.append(text[:200])
        self.chat_add("<%s> %s" % (self.name, text), (255, 255, 255))

    def net_payload(self):
        with self.lock:
            keys = list(self.out_blocks.keys())[:MAX_BLOCKS_PER_SYNC]
            blocks = [(k, self.out_blocks.pop(k)) for k in keys]
            chats = self.out_chat[:3]
            del self.out_chat[:3]
            puts = self.out_puts[:5]
            del self.out_puts[:5]
        p = self.p
        s = self.held()
        me = dict(x=p.x, y=p.y, vx=p.vx, f=p.face, d=self.dim, hp=p.hp, sw=min(1.0, p.swing),
                  h=int(s[0]) if s else 0)
        ev = [{"t": "b", "d": d, "x": x, "y": y, "b": v} for (d, x, y), v in blocks]
        ev += [{"t": "c", "m": m} for m in chats]
        ev += puts
        payload = dict(me=me, ev=ev)
        oc = self._open_chest
        if oc and self.ui == "chest":
            payload["oc"] = list(oc[0])                       # keeps our lock on the open chest alive
        return payload, (blocks, chats, puts)

    def net_requeue(self, undo):
        blocks, chats, puts = undo
        with self.lock:
            for k, v in blocks:
                self.out_blocks.setdefault(k, v)          # a newer value for the same cell wins
            self.out_chat[:0] = chats
            self.out_puts[:0] = puts

    def net_backlog(self):
        with self.lock:
            return bool(self.out_blocks) or bool(self.out_chat) or bool(self.out_puts)

    # ----- incoming ---------------------------------------------------------
    def sync_time(self, ms):
        if not self.tick_frozen:
            self.time = ms / 1000.0 + 0.15 * pc.DAY_LEN

    def apply_block(self, d, x, y, v):
        if not (0 <= d <= 2 and 0 <= x < pc.WW and 0 <= y < pc.WH and 0 <= v < 256):
            return
        self.block_state.setdefault(d, {})[(x, y)] = v
        with self.lock:
            if (d, x, y) in self.out_blocks:             # my newer change is still on its way
                return
        w = self.worlds.get(d)
        if w is not None:
            _orig_set(w, x, y, v)

    def apply_snapshot(self, blocks):
        for d, cells in (blocks or {}).items():
            try:
                di = int(d)
            except ValueError:
                continue
            for key, v in (cells or {}).items():
                try:
                    xs, ys = key.split("_")
                    self.apply_block(di, int(xs), int(ys), int(v))
                except (ValueError, AttributeError):
                    continue

    def net_pump(self):
        if self.net_fatal:
            self.say("Disconnected: %s" % self.net_fatal, 8)
            if self._fatal_at is None:
                self._fatal_at = pygame.time.get_ticks()
            elif self.net_fatal.startswith("You were kicked") and pygame.time.get_ticks() - self._fatal_at > 5000:
                self.quit()
        while True:
            try:
                j = self.inbox.get_nowait()
            except queue.Empty:
                break
            if "snapshot" in j:
                self.apply_snapshot(j["snapshot"])
                continue
            for e in j.get("events", []):
                t, n = e.get("t"), str(e.get("n", "?"))[:16]
                if t == "b":
                    if all(isinstance(e.get(k), int) for k in ("d", "x", "y", "b")):
                        self.apply_block(e["d"], e["x"], e["y"], e["b"])
                elif t == "c" and n != self.name:
                    self.chat_add("<%s> %s" % (n, str(e.get("m", ""))[:200]))
                elif t == "j" and n != self.name:
                    self.chat_add("%s joined the game" % n, (255, 230, 120))
                elif t == "k":
                    self.chat_add("%s was kicked by %s (%s)" % (n, str(e.get("by", "?"))[:16], str(e.get("m", ""))[:100]),
                                  (255, 160, 120))
                elif t == "l" and n != self.name:
                    self.chat_add("%s left the game" % n, (255, 230, 120))
            seen = j.get("players", {})
            for n in list(self.others):
                if n not in seen:
                    del self.others[n]
            for n, d in seen.items():
                try:
                    o = self.others.setdefault(n, dict(dx=float(d["x"]), dy=float(d["y"]), walk=0.0))
                    o.update(x=float(d["x"]), y=float(d["y"]), vx=float(d["vx"]), f=int(d["f"]), d=int(d["d"]),
                             hp=float(d["hp"]), sw=float(d["sw"]), h=int(d["h"]))
                except (KeyError, TypeError, ValueError):
                    continue
            if "time" in j:
                self.sync_time(j["time"])

    # ----- game hooks -------------------------------------------------------
    def publish_new_containers(self):
        with self.lock:
            todo, self.new_containers = self.new_containers, set()
        for d, x, y in todo:
            w = self.worlds.get(d)
            if w is None or w.get(x, y) not in (pc.CHEST, pc.SHULKER_BOX):
                continue
            cont = self.chests.get((x, y)) if d == self.dim else None
            c = json.dumps(enc(cont if cont is not None else [None] * 27), separators=(",", ":"))
            with self.lock:
                self.out_puts.append(dict(t="p", d=d, x=x, y=y, c=c))

    def update(self, dt):
        self.net_pump()
        if self.new_containers:
            self.publish_new_containers()
        super().update(dt)
        k = 1 - math.exp(-14 * dt)
        for o in self.others.values():
            if abs(o["x"] - o["dx"]) > 8 or abs(o["y"] - o["dy"]) > 8:
                o["dx"], o["dy"] = o["x"], o["y"]
            o["dx"] += (o["x"] - o["dx"]) * k
            o["dy"] += (o["y"] - o["dy"]) * k
            o["walk"] += abs(o["vx"]) * dt

    def switch_dim(self, dim):
        fresh = dim not in self.worlds
        super().switch_dim(dim)
        self.world.mp = self
        if fresh:
            for (x, y), v in self.block_state.get(dim, {}).items():
                _orig_set(self.world, x, y, v)

    def toggle_creative(self):
        if not self.cheats and not self.creative:
            self.say("Creative mode is disabled on this server.")
            return
        super().toggle_creative()

    def open_menu(self):
        self.say("There is no world menu in multiplayer (X quits).")

    def run_command(self, text):
        t = text.strip()
        if not t:
            return False
        if not t.startswith("/"):
            self.send_chat(t)
            return True
        parts = t[1:].split()
        if parts and parts[0].lower() in CHEAT_CMDS and not self.cheats:
            self.chat_add(t, (190, 190, 195))
            self.chat_add("Cheat commands are disabled on this server.", (255, 130, 120))
            return False
        return super().run_command(t)

    # ----- shared chests and shulker boxes ----------------------------------
    CONTAINERS = (pc.CHEST, pc.SHULKER_BOX)

    def right_click(self):
        _, _, bx, by = self.mouse_world()
        if self.in_reach(bx, by) and self.world.get(bx, by) in self.CONTAINERS:
            self.open_shared_chest(bx, by)
            return
        super().right_click()

    def open_shared_chest(self, bx, by):
        key = (self.dim, bx, by)
        if key in self.chest_pending:
            self.say("Still saving that chest, try again in a moment.")
            return
        try:
            r = self.net.call("chest_open", dict(d=self.dim, x=bx, y=by), timeout=6)
        except NetError as ex:
            self.say(str(ex), 3)
            return
        c = r.get("c")
        if c:
            try:
                self.chests[(bx, by)] = clean_list(dec(json.loads(c)), 27)
            except ValueError:
                pass
        cont = self.chests.setdefault((bx, by), [None] * 27)
        self.cur_chest = cont
        self.chest_name = "Shulker Box" if self.world.get(bx, by) == pc.SHULKER_BOX else "Chest"
        self._open_chest = (key, cont)
        self.ui = "chest"

    def close_ui(self):
        oc = self._open_chest if self.ui == "chest" else None
        super().close_ui()
        if oc:
            self._open_chest = None
            self.save_shared_chest(*oc)

    def save_shared_chest(self, key, cont):
        c = json.dumps(enc(cont), separators=(",", ":"))
        d, x, y = key
        try:
            self.net.call("chest_close", dict(d=d, x=x, y=y, c=c), timeout=6)
            return
        except NetError as ex:
            if ex.status == 409:
                self.say(str(ex), 6)
                return
        self.chest_pending.add(key)                       # network trouble: keep retrying in the background
        self.say("Could not reach the server - the chest will be saved when it is back.", 5)

        def retry():
            for _ in range(40):
                time.sleep(3)
                try:
                    self.net.call("chest_close", dict(d=d, x=x, y=y, c=c), timeout=8)
                    break
                except NetError as ex:
                    if ex.status == 409:
                        break
            self.chest_pending.discard(key)
        threading.Thread(target=retry, daemon=True).start()

    def break_block(self, bx, by, can):
        b = self.world.get(bx, by)
        if b in self.CONTAINERS:
            try:
                r = self.net.call("chest_take", dict(d=self.dim, x=bx, y=by), timeout=6)
            except NetError as ex:
                self.say(str(ex), 3)
                self.mining, self.mine_prog = None, 0.0
                self.no_mine = True
                return
            if r.get("c"):
                try:
                    self.chests[(bx, by)] = clean_list(dec(json.loads(r["c"])), 27)
                except ValueError:
                    pass
        super().break_block(bx, by, can)

    def blast_block(self, bx, by, b):
        if b in self.CONTAINERS:                          # shared chests survive explosions (no item loss or duplication)
            return
        super().blast_block(bx, by, b)

    def cmd_players(self, args):
        names = [self.name + " (you)"] + sorted(self.others)
        return "%d online: %s" % (len(names), ", ".join(names))

    def cmd_kick(self, args):
        if not self.admin:
            raise ValueError("Only server admins can kick (see 'admins' in the server config).")
        if not args:
            raise ValueError("Usage: /kick <player> [reason]")
        target, reason = args[0], " ".join(args[1:])

        def work():
            try:
                self.net.call("kick", dict(target=target, reason=reason))
            except NetError as ex:
                self.chat_add("Kick failed: %s" % ex, (255, 130, 120))
        threading.Thread(target=work, daemon=True).start()
        return "Kicking %s..." % target

    def cmd_tp(self, args):
        if not args:
            raise ValueError("Usage: /tp <player>")
        for n, o in self.others.items():
            if n.lower() == args[0].lower():
                if o["d"] != self.dim:
                    raise ValueError("%s is in another dimension." % n)
                self.p.x, self.p.y, self.p.vx, self.p.vy = o["x"], o["y"] - 0.1, 0.0, 0.0
                return "Teleported to %s." % n
        raise ValueError("No player called '%s' here. /players lists them." % args[0])

    # ----- saving: to the server instead of a file --------------------------
    def encode_player(self):
        p = self.p
        return json.dumps(enc(dict(inv=self.inv, armor=self.armor, ender=self.ender, xp=self.xp, food=self.food,
                                   hp=p.hp, sel=self.sel, px=p.x, py=p.y, dim=self.dim, spawn=self.spawn,
                                   waypoints=self.waypoints)), separators=(",", ":"))

    def restore_player(self, blob):
        try:
            d = dec(json.loads(blob))
            self.inv = clean_list(d.get("inv"), 36)
            self.armor = clean_list(d.get("armor"), 4)
            self.ender = clean_list(d.get("ender"), 27)
            self.xp = max(0, int(d.get("xp", 0)))
            self.food = max(0.0, min(20.0, float(d.get("food", 20))))
            self.p.hp = max(1.0, min(20.0, float(d.get("hp", 20))))
            self.sel = max(0, min(8, int(d.get("sel", 0))))
            sp = d.get("spawn")
            if isinstance(sp, tuple) and len(sp) == 2:
                self.spawn = (float(sp[0]), float(sp[1]))
            wps = d.get("waypoints")
            if isinstance(wps, list):
                self.waypoints = [dict(x=int(w["x"]), y=int(w["y"]), dim=int(w["dim"])) for w in wps[:self.MAX_WAYPOINTS]
                                  if isinstance(w, dict) and all(k in w for k in ("x", "y", "dim"))]
            dim = int(d.get("dim", 0))
            if dim in (1, 2):
                self.switch_dim(dim)
            x, y = float(d.get("px", self.p.x)), float(d.get("py", self.p.y))
            if 0 <= x < pc.WW and 0 <= y < pc.WH and self.spot_ok(self.world, x, y):
                self.p.x, self.p.y = x, y
            elif self.dim != 0:
                self.switch_dim(0)
            self.purge_bad_items()
            self.say("Welcome back, %s! Your progress was restored." % self.name, 5)
        except Exception as ex:                                       # noqa
            self.say("Could not restore your saved progress (%s)." % ex, 6)

    def save(self):
        data = self.encode_player()
        threading.Thread(target=self._save_bg, args=(data,), daemon=True).start()
        self.say("Progress saved to the server.")

    def _save_bg(self, data):
        try:
            self.net.call("save", dict(data=data))
        except NetError as ex:
            self.net_error = "save failed: %s" % ex

    def quit(self):
        if self._open_chest and self.ui == "chest":
            try:
                key, cont = self._open_chest
                self.net.call("chest_close", dict(d=key[0], x=key[1], y=key[2],
                                                  c=json.dumps(enc(cont), separators=(",", ":"))), timeout=6)
            except Exception:                                         # noqa
                pass
        try:
            self.net.stop.set()
            self.net.call("save", dict(data=self.encode_player()), timeout=6)
            self.net.call("leave", timeout=4)
        except Exception:                                             # noqa
            pass
        pygame.quit()
        sys.exit(0)

    # ----- drawing ----------------------------------------------------------
    @staticmethod
    def name_color(n):
        h = int(hashlib.md5(n.encode()).hexdigest()[:6], 16)
        return (70 + (h & 0xFF) % 150, 70 + ((h >> 8) & 0xFF) % 150, 70 + ((h >> 16) & 0xFF) % 150)

    def draw_entities(self):
        super().draw_entities()
        scr, cx, cy = self.screen, self.camx, self.camy
        t = pygame.time.get_ticks() / 1000.0
        for n, o in self.others.items():
            if o["d"] != self.dim:
                continue
            sx, sy = int(o["dx"] * pc.TILE - cx), int(o["dy"] * pc.TILE - cy)
            if sx < -60 or sx > pc.SW + 60 or sy < -80 or sy > pc.SH + 40:
                continue
            w_, h_ = int(0.6 * pc.TILE), int(1.8 * pc.TILE)
            shirt = self.name_color(n)
            moving = abs(o["vx"]) > 0.3
            leg = math.sin(o["walk"] * 3) * 5 if moving else 0
            top_legs = sy + int(h_ * 0.62)
            pygame.draw.rect(scr, (50, 50, 150), (sx + 1, top_legs, w_ // 2 - 1, h_ - int(h_ * 0.62) - leg * 0.3))
            pygame.draw.rect(scr, (50, 50, 150), (sx + w_ // 2, top_legs, w_ // 2 - 1, h_ - int(h_ * 0.62) + leg * 0.3))
            pygame.draw.rect(scr, shirt, (sx, sy + w_, w_, top_legs - sy - w_))
            pygame.draw.rect(scr, (205, 160, 120), (sx, sy, w_, w_))
            pygame.draw.rect(scr, (60, 40, 30), (sx, sy, w_, 6))
            f = o["f"]
            ex = sx + (w_ - 7 if f > 0 else 2)
            pygame.draw.rect(scr, (255, 255, 255), (ex, sy + 9, 5, 4))
            pygame.draw.rect(scr, (60, 60, 200), (ex + (2 if f > 0 else 0), sy + 9, 3, 4))
            sw_ = math.sin(t * 22) * 8 if o["sw"] > 0 else 0
            ax = sx + (w_ - 3 if f > 0 else -5)
            pygame.draw.rect(scr, (205, 160, 120), (ax, sy + w_ + 2 + sw_ * 0.5, 8, 14))
            if o["h"] in pc.ICON_S:
                ic = pc.ICON_S[o["h"]]
                ix = ax + (6 if f > 0 else -14) + sw_ * f * 0.5
                scr.blit(ic if f > 0 else pygame.transform.flip(ic, True, False), (ix, sy + w_ + 8 + sw_))
            tag = self.small.render(n, True, (255, 255, 255))
            bg = pygame.Surface((tag.get_width() + 8, tag.get_height() + 2), pygame.SRCALPHA)
            bg.fill((0, 0, 0, 130))
            scr.blit(bg, (sx + w_ // 2 - bg.get_width() // 2, sy - 24))
            scr.blit(tag, (sx + w_ // 2 - tag.get_width() // 2, sy - 23))
            pygame.draw.rect(scr, (180, 30, 30), (sx - 2, sy - 7, w_ + 4, 3))
            pygame.draw.rect(scr, (60, 220, 60), (sx - 2, sy - 7, int((w_ + 4) * max(0.0, min(20.0, o["hp"])) / 20), 3))

    def draw_hud(self):
        super().draw_hud()
        lines = [(self.name + " (you)", (255, 255, 255))]
        lines += [(n + ("" if o["d"] == self.dim else " (other dim)"), self.name_color(n)) for n, o in sorted(self.others.items())]
        y = 8
        for text, col in lines[:12]:
            surf = self.small.render(text, True, col)
            self.screen.blit(surf, (pc.SW - surf.get_width() - 10, y))
            y += 15
        if self.net.fails:
            self.txt("Connection problem - retrying...  %s" % self.net_error[:60], (pc.SW // 2, 8), (255, 120, 100), center=True)
        elif self.debug:
            self.txt("ping %d ms" % self.net.last_ms, (pc.SW - 70, y + 4), (200, 200, 200))



# --------------------------------------------------------------------------- #
def main():
    global SYNC_INTERVAL
    cfg = {}
    try:
        with open(CONFIG_FILE) as f:
            cfg = json.load(f)
    except (OSError, ValueError):
        pass
    ap = argparse.ArgumentParser(description="PotatoCraft multiplayer client")
    ap.add_argument("--server", help="URL of api.php, e.g. https://potato.example.com/api.php")
    ap.add_argument("--room", help="room (world) name - everyone using the same name plays together")
    ap.add_argument("--name", help="your player name (2-16 letters, digits, _)")
    ap.add_argument("--password", help="your player password (asked if left out)")
    ap.add_argument("--interval", type=float, default=SYNC_INTERVAL,
                    help="seconds between server updates (default %.2f; raise to 0.6-1.0 on a weak connection or a host that rate-limits)" % SYNC_INTERVAL)
    ap.add_argument("--create-code", default="", help="only if the server owner set a create code")
    a = ap.parse_args()
    SYNC_INTERVAL = max(0.15, min(5.0, a.interval))

    server = a.server or cfg.get("server") or input("Server URL (api.php): ").strip()
    room = a.room or cfg.get("room") or input("Room name [world]: ").strip() or "world"
    name = a.name or cfg.get("name") or input("Player name: ").strip()
    password = a.password or os.environ.get("POTATO_PASSWORD") or getpass.getpass("Password (new name = choose one): ")
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(dict(server=server, room=room, name=name), f)
    except OSError:
        pass

    net = Net(server, room, name, password)
    print("Joining %s ..." % room)
    try:
        info = net.join(a.create_code)
    except NetError as ex:
        sys.exit("Could not join: %s" % ex)
    print("Joined. %d player(s) online. Generating the world..." % info.get("online", 1))
    MPGame(net, info).run()


if __name__ == "__main__":
    main()
