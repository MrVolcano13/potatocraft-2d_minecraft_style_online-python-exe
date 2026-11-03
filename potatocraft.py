#!/usr/bin/env python3
"""
PotatoCraft - a 2D side-view Minecraft-style survival game with potato graphics.

Requires:  pip install pygame
Run:       python potatocraft.py          (continues your saved world if one exists)
           python potatocraft.py --new    (start a fresh world)

CONTROLS
  A / D (or arrows)  walk            Shift      sprint
  W / Space          jump            1-9/wheel  select hotbar slot
  Left mouse (hold)  mine / attack   Right mouse place block / open table, furnace, chest
  E                  inventory       Q          drop one held item
  Esc                close UI / pause (while paused: F5 creative, F6 save, M world menu, X save & quit)
  F5                 creative mode   F6         save          F3   debug info
  F11                fullscreen on/off
  F2 (in the F3 menu) saves your X/Y at the bottom of the menu; click [x] to remove one,
                        or [TP] to teleport there (works across dimensions)

COMMANDS (T or / opens the command line; Enter runs, Esc cancels, Tab completes, Up/Down repeat)
  /setblock x y block [keep]       put one block (block = a name like stone, oak_planks, piston_left,
                                   air; a part of a name works when it is unique)
  /fill x1 y1 x2 y2 block [replace [old] | hollow | outline | keep]   fill a box, up to 32768 cells
  /give item [count]               put items in your inventory (any item from the creative menu; a
                                   unique part of the name works; up to 2304)
  /tick freeze | unfreeze | step [n] | query   freeze the world (mobs, drops, machines, time of
                                   day, TNT, water bobber...; you can still move and build) and run
                                   n ticks at a time (20 ticks = 1 second). A step freezes first.
  x and y are cells (y grows downward). ~ is your own cell, ~3 and ~-3 are offsets from it.
  /help lists them.

CREATIVE MODE (F5 toggles)
  Unlimited blocks, no damage or drowning, instant mining (no drops), tools never wear
  out. Double-tap Space to fly: Space up, S down, S on the ground to land. Open the
  inventory (E) for the item list (scroll it with the mouse wheel or drag its bar): click = full stack, right-click = 1, click the list
  while holding an item to delete it.

BUILDING
  Ladder (7 sticks, 3 ladders): place beside a wall, hold W/Space to climb, S to go down.
  Bucket (3 iron ingots in a V): right-click lava to scoop it up, right-click an empty
  space to pour it out. A lava bucket also fuels a furnace for 100 items (and you get
  the empty bucket back).
  Water pools: swim with W/Space (up) and S (down). You can hold your breath for about
  10 seconds. Scoop water with a bucket (pool middles refill themselves). Pour water onto
  lava to make obsidian, a quick way to a portal.
  Storage blocks: 9 iron ingots, diamonds or netherite ingots make a block; put one block
  in the grid to get 9 back.
  Ender Chest (8 obsidian around a diamond): every ender chest opens the SAME 27 slots,
  in any dimension, so you can stash items in one and take them out of another. Mining
  one keeps the items safe; they stay in your ender inventory.
  Shulker Box (2 diamonds around a chest, vertical): a 27-slot box that keeps everything
  inside when you mine it and carry it. Right-click to open. No shulker inside shulker.
  Potion of Protection (netherite scrap, diamond, iron ingot, top to bottom): right-click
  to drink; no damage of any kind for 2 minutes.
  Potion of Regeneration (coal, diamond, coal, top to bottom): right-click to drink; fully
  restores your health.
  Wooden Door (6 planks, 3 doors): place on solid ground (2 blocks tall), right-click to
  open or close. Closed doors stop zombies.

ENDER PEARL (2x2: diamond and ancient debris on the diagonals, works in the inventory)
  Right-click to throw it toward the cursor. You teleport to where it lands and take
  2.5 hearts of damage (creative and the protection potion ignore it).
  A pearl that hits water floats on the surface (even a single water block) and does NOT
  teleport you; walk (or swim) up to it to pick it back up. A floating pearl stays where it
  is, also when you change dimension or save and quit (a "stasis chamber"), and it presses
  wooden pressure plates in its cell or the one under it. Remove the water under it (bucket)
  and it falls and lands: you teleport to it, even from another dimension (a stasis chamber
  keeps running while you are away: plates, pistons, torches and doors in that dimension work
  as long as a floating pearl or your bobber is there).

THE END
  Craft an Eye of Ender (ender pearl over coal), build a closed obsidian frame in the
  Overworld (at least 2 wide x 3 tall) and right-click it with the eye. Stand in the dark
  portal for ~3 s. The End is a flat island over the void with two obsidian pillars; an
  end crystal tops each one and heals the Ender Dragon. Hit a crystal to blow it up (it
  also hurts the dragon, and you if you stand close). The dragon circles high up and dives
  at you; strike it as it swoops. When it dies an exit portal and the Dragon Egg appear.
  Falling into the void kills you. Dying sends you back to the Overworld.
  To fight the dragon again: craft 4 End Crystals (obsidian over eye of ender over diamond),
  place them (right-click) on obsidian, bedrock or end stone within a few blocks of the exit
  portal. After ~6 seconds the dragon is reborn with fresh pillar crystals and the exit
  portal closes until it dies again. The Dragon Egg only appears for the first kill.

BOW AND ARROWS
  Bow: sticks and planks (.SP / S.P / .SP, planks stand in for string). Arrows: coal over a
  stick makes 4. Hold the RIGHT mouse button with the bow in your hand to draw it (the bar
  above your head fills in 1 s), release to shoot toward the cursor. A full draw is fast
  and hits for 9; a quick tap (under 0.2 s) cancels. Arrows arc, stick in blocks and hit
  mobs, cows, end crystals and the Ender Dragon. Creative mode has endless arrows.

ELYTRA AND FIREWORKS
  Elytra goes in the chestplate slot: right-click to wear
  it. It drops once from the Ender Dragon, or craft it: diamonds on the sides, a netherite
  ingot on top and an eye of ender in the middle (D N D / D E D / D . D). While falling,
  press Space once in mid-air to spread the wings: W/Up pitch up (slows you), S/Down dives
  (speeds you up), A/D turn. Landing too hard or crashing into a wall hurts; water and
  ladders end the flight. It wears 1 durability per second.
  Firework Rocket (coal over planks makes 3): right-click to launch a rocket that bursts in
  colours. While gliding it gives a strong boost instead.

BOOKS
  Paper: 3 planks in a row make 3. Book: paper, paper, leather (top to bottom); cows drop
  leather. Right-click a Book to open it and just type: up to 250 pages of 600 characters.
  < > or PageUp/PageDown turn pages, + Page / - Page add or remove one, Copy book duplicates
  it (needs one empty Book in your inventory; creative: free). Books keep their text when
  carried, dropped or saved. Chests, shulker boxes and ender chests can hold any number of books.

PRESSURE PLATES, PISTONS, FISHING
  Wooden plate: 2 planks side by side (anything standing on it, even dropped items). Stone
  plate: 2 stone (players and mobs only). Place on solid ground; it powers what touches it:
  the blocks on its left, right and above it, and the sides of the block it rests on. Powered
  pistons extend, TNT ignites, doors open, and they undo it when you step off.
  Piston: planks x3 / cobble, iron, cobble / cobble, coal, cobble. It faces away from you when
  placed (aim left, right, up or down). It pushes up to 12 blocks (not bedrock, obsidian,
  chests, furnaces, doors, other pistons) and shoves mobs and you; stepping off retracts it.
  Trapdoor: 2x3 planks make 2. Right-click toggles it: closed it is a solid floor, open you
  fall (and walk) through. Powered ones (plate, torch) open by themselves and close when the
  power goes. Pistons can push them; an open one is crushed into its item.
  Redstone dust: 1 coal makes 2. It lies on top of solid blocks and links up with dust beside
  it (and up or down a block step) into a wire: a plate or a lit torch touching one end powers
  the whole wire (15 blocks of reach), and the powered wire runs pistons, doors, trapdoors and TNT
  at its sides and under it, and switches off a torch hanging on the block under it. A block sitting
  on a lit torch also powers what touches it. Mine dust by hand; it pops off if its ground goes.
  Slime block: 9 slime balls (4 coal in a 2x2 square make 1 ball here; a block turns back into 9 balls).
  Falling onto it does no damage and bounces you back up. Whatever touches a slime block is
  stuck to it: a piston that pushes or pulls it drags the blocks around it along (12 at most;
  careful, ground under it counts). Sticky piston: slime ball over a piston. On the way back
  it pulls the block in front of it (and any slime-stuck blocks) with it.
  Observer: 6 cobble over 2 redstone dust and an iron ingot (iron stands in for quartz). It
  faces you when placed. Whenever the block in front of its face changes (mined, placed, a door
  or trapdoor toggles, a piston moves it) it sends a short pulse out of its back (red dot): that
  powers a piston, dust, door or TNT behind it. Pistons can push observers; observers within
  ~56 blocks of you are active.
  Farming: a hoe (2 planks/cobble/iron/diamond over 2 sticks, like a pickaxe's top row) right-clicks
  grass or dirt into farmland if the cell above is open. Mining grass sometimes drops Wheat Seeds
  (12%); right-click seeds onto farmland to plant. Crops grow in 4 stages while you are near:
  about a minute on wet farmland (water within 4 blocks, same row or the one above) and twice as
  slow when dry. Mine a ripe crop for Wheat and seeds; 3 wheat in a row bake Bread (restores 5).
  Farmland under a solid block turns back into dirt; crops need soil under them.
  Saplings: leaves sometimes drop one (8%). Right-click it onto grass or dirt; after about a
  minute near you it grows into an oak (4-6 logs and leaves) if there is room above. It pops off
  if its ground goes.
  Trees: when you break a log (or blow one up), leaves around it that are more than 4 steps from
  any log fall away over a few seconds (a few drop sticks or saplings). Break every log and the
  whole crown comes down; leaves you built far from any broken log stay.
  Lever: a stick over cobblestone. Place it on a block or a wall and right-click to flip it
  (works even with a block in hand). While ON it powers what touches it and the block it is on,
  like a pressed plate; a torch on that block goes dark. Redstone dust next to it carries it on.
  Buttons: 1 stone makes a stone button, 1 plank a wooden one. Place like a lever (on a block or
  wall) and right-click: it pops in and powers what touches it and its block for 1 s (stone) or
  1.5 s (wood), then pops out. Dust next to it carries the pulse; an observer sees it press.
  Redstone torch: redstone dust over a stick. It sits on a block (or a wall) and powers the blocks
  around it (not the one it hangs on): pistons extend, doors open, TNT ignites next to it.
  It is a NOT gate: when the block it hangs on is powered, it goes dark and lets go. A block
  is powered when it is the one under a pressed plate, so a torch on the side of that block
  switches off while you stand on the plate. Torches within ~56 blocks of you are active.
  Remote control: plates, pistons, torches and doors near a floating pearl, near your bobber,
  or near an extended piston keep running while you are in another dimension, and for 8 seconds
  after you reel the bobber in from over there. So you can park the bobber on a plate in the
  Overworld, go to the Nether, pull the rod (or press R) and the circuit reacts (the plate lets
  go, the torch lights, the piston pushes).
  Fishing rod: sticks and string (..S / .ST / S.T). String comes from leaves (and fishing).
  Press R to reel the bobber in with any item in hand. Right-click to throw the bobber to the cursor (up to 14 blocks, water not needed); it is a
  real entity that falls, lands on the ground and floats on water. Right-click again to reel
  it in from anywhere (any distance, any dimension). If it floats on water, hold the rod nearby
  and wait for the dip (a fish is biting!), then reel in raw cod or salmon (smelt them) and
  sometimes string, leather or XP bottles.
  The bobber stays where it lies when you walk away, switch items, change dimension or save
  and quit (one at a time). Any pressure plate it rests on or floats over is pressed (wooden
  and stone). Plates may be placed under water.

ENCHANTING
  Bottle o' Enchanting: iron ingot, diamond, coal (top to bottom) make 2; right-click one to
  gain 3-11 XP (Mending gear soaks it up first). Loot chests often hold 2-6 of them.
  Grindstone (stick, stone, stick over planks, gap, planks): right-click it, put an enchanted
  item in the slot and press Remove enchantments. The item keeps its durability and you get
  5 XP back per enchantment level removed (none in creative).
  Enchanting Table: obsidian, obsidian, obsidian (bottom row), diamond, obsidian, diamond
  (middle row), a Book in the top middle. Earn XP by killing mobs (zombie 5, cow 2, dragon
  500) and mining ores (coal 2, iron 3, diamond 10, ancient debris 20); the bar over the
  hotbar shows your level. Right-click the table, put a tool, weapon, armor piece or bow in
  the slot and pick one of three offers (costs 2, 4 or 6 levels for enchant level I, II, III;
  the effect is random but fixed per item). Efficiency (faster mining), Sharpness (more
  damage), Protection (armor), Power (bow), Unbreaking (wears out slower), Mending (XP you
  earn repairs the held item and worn armor first: 1 xp = 2 durability). Enchant again to
  add more or raise a level. Enchanted items glow purple and keep it when dropped or stored.
  Creative mode enchants for free. Dying loses your XP.

LOOT CHESTS
  Every world hides 6 small stone rooms deep underground, each with a chest full of good
  stuff: iron, diamonds, ender pearls, potions of regeneration and protection, food. Dig
  for them! Only one netherite ingot exists in all six (and only some worlds have it).

HUNGER AND COWS
  The drumsticks under the hearts are your hunger. They drain slowly, faster while you walk
  and sprint. You only regenerate health while at least 7 drumsticks are full; at zero you
  starve (health drops to 1 heart but never kills you). Creative mode has no hunger.
  Cows roam the grass in the Overworld. Hit one for Raw Beef (1-3), smelt it in a furnace
  into Steak, and right-click food to eat it (Raw Beef 3, Steak 8).

THE NETHER (netherrack + ancient debris only)
  Mine obsidian (deep underground near lava, needs a DIAMOND pickaxe), then build a
  frame of 10 obsidian around a 2 wide x 3 tall opening (corners not needed).
  Craft Flint and Steel (iron ingot over coal) and right-click inside the frame.
  Stand in the purple portal ~3 s to travel. Lava burns and destroys dropped items!
  In the Nether, mine Ancient Debris with a DIAMOND pickaxe (rare, deep down), smelt it
  in a furnace into Netherite Scrap, craft a Netherite Ingot at a crafting table
  (4 scrap + 4 iron ingots), then put the ingot over a Diamond tool to upgrade it.

INVENTORY: left click = pick up / put down / swap, right click = split stack or
place one, shift+click = quick-move.  Items left in the crafting grid return to
your inventory when you close the window.
"""
import math
import os
import pickle
import random
import sys

import pygame

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #
SW, SH = 1100, 680
TILE = 32
WW, WH = 360, 120          # world size in blocks
SURF = 42                  # average surface height
REACH = 5.5
GRAVITY = 32.0
SMASH_MIN_FALL = 3.0      # an axe hit while falling further than this many blocks does extra damage
DAY_LEN = 300.0            # seconds per day/night cycle
SAVE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "potatocraft_save.pkl")        # the old single save
WORLD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "potatocraft_worlds")     # one file per world

# --------------------------------------------------------------------------- #
# Item / block registry
# --------------------------------------------------------------------------- #
ITEMS = {}


def reg(name, **kw):
    i = len(ITEMS) + 1
    ITEMS[i] = dict(name=name, **kw)
    return i


AIR = 0
GRASS = reg("Grass Block", block=1, hard=0.6, tool="shovel")
DIRT = reg("Dirt", block=1, hard=0.5, tool="shovel")
STONE = reg("Stone", block=1, hard=1.5, tool="pickaxe", tier=1)
COBBLE = reg("Cobblestone", block=1, hard=2.0, tool="pickaxe", tier=1)
LOG = reg("Oak Log", block=1, hard=2.0, tool="axe")
LEAVES = reg("Leaves", block=1, hard=0.2, tool=None)
PLANKS = reg("Oak Planks", block=1, hard=2.0, tool="axe")
COAL_ORE = reg("Coal Ore", block=1, hard=3.0, tool="pickaxe", tier=1)
IRON_ORE = reg("Iron Ore", block=1, hard=3.0, tool="pickaxe", tier=2)
DIAMOND_ORE = reg("Diamond Ore", block=1, hard=3.0, tool="pickaxe", tier=3)
BEDROCK = reg("Bedrock", block=1, hard=-1)
TABLE = reg("Crafting Table", block=1, hard=2.5, tool="axe")
FURNACE = reg("Furnace", block=1, hard=3.5, tool="pickaxe", tier=1)
CHEST = reg("Chest", block=1, hard=2.5, tool="axe")
STICK = reg("Stick")
COAL = reg("Coal")
IRON_INGOT = reg("Iron Ingot")
DIAMOND = reg("Diamond")

ITEMS[GRASS]["drop"] = DIRT
ITEMS[STONE]["drop"] = COBBLE
ITEMS[COAL_ORE]["drop"] = COAL
ITEMS[DIAMOND_ORE]["drop"] = DIAMOND

# (name, tier, durability, material item)
TIERS = [("Wooden", 1, 59, PLANKS), ("Stone", 2, 131, COBBLE),
         ("Iron", 3, 250, IRON_INGOT), ("Diamond", 4, 1561, DIAMOND)]
TIER_SPEED = [1, 2, 4, 6, 8, 10]
TOOL_KINDS = ("pickaxe", "axe", "shovel", "sword")
TOOLS = {}
for _n, _t, _d, _m in TIERS:
    for _k in TOOL_KINDS:
        TOOLS[(_n, _k)] = reg("%s %s" % (_n, _k.title()), tool=_k, tier=_t, dur=_d)

# --- The Nether (registered last so older saves keep valid item ids) ------- #
NETHERRACK = reg("Netherrack", block=1, hard=0.4, tool="pickaxe")
OBSIDIAN = reg("Obsidian", block=1, hard=50.0, tool="pickaxe", tier=4)
ANCIENT_DEBRIS = reg("Ancient Debris", block=1, hard=30.0, tool="pickaxe", tier=4)
LAVA = reg("Lava", hard=-1)
PORTAL = reg("Nether Portal", hard=-1)
NETHERITE_SCRAP = reg("Netherite Scrap")
NETHERITE_INGOT = reg("Netherite Ingot")
FLINT_STEEL = reg("Flint and Steel", tool="lighter", tier=0, dur=32)
TOOLS[("Netherite", "pickaxe")] = reg("Netherite Pickaxe", tool="pickaxe", tier=5, dur=2031, speed=10)
LADDER = reg("Ladder", block=1, hard=0.4, tool="axe")
DOOR_ITEM = reg("Wooden Door")
DOOR_CB = reg("Door", hard=3.0, tool="axe", drop=DOOR_ITEM)      # closed, bottom half
DOOR_CT = reg("Door", hard=3.0, tool="axe", drop=DOOR_ITEM)      # closed, top half
DOOR_OB = reg("Open Door", hard=3.0, tool="axe", drop=DOOR_ITEM)  # open, bottom half
DOOR_OT = reg("Open Door", hard=3.0, tool="axe", drop=DOOR_ITEM)  # open, top half
for _k in ("axe", "shovel", "sword"):      # registered after the doors so older saves keep their ids
    TOOLS[("Netherite", _k)] = reg("Netherite %s" % _k.title(), tool=_k, tier=5, dur=2031, speed=10)
BUCKET = reg("Bucket", stack=16)                  # registered after the netherite tools: ids stay stable
LAVA_BUCKET = reg("Lava Bucket", stack=1)
WATER = reg("Water", hard=-1)                    # appended: ids of older items never move
IRON_BLOCK = reg("Iron Block", block=1, hard=5.0, tool="pickaxe", tier=2)
DIAMOND_BLOCK = reg("Diamond Block", block=1, hard=5.0, tool="pickaxe", tier=3)
NETHERITE_BLOCK = reg("Netherite Block", block=1, hard=50.0, tool="pickaxe", tier=4)
WATER_BUCKET = reg("Water Bucket", stack=1)
SHULKER_BOX = reg("Shulker Box", block=1, hard=2.0, tool="pickaxe", stack=1)
PROTECTION_POTION = reg("Potion of Protection", stack=16)
REGEN_POTION = reg("Potion of Regeneration", stack=16)
ENDER_CHEST = reg("Ender Chest", block=1, hard=10.0, tool="pickaxe", tier=1)
TNT = reg("TNT", block=1, hard=0.0)
# --- Armor (appended last: older saves keep their ids) --------------------- #
ARMOR_SLOTS = ("helmet", "chestplate", "leggings", "boots")
ARMOR_DEFENSE = {"Iron": (2, 6, 5, 2), "Diamond": (3, 8, 6, 3), "Netherite": (3, 8, 6, 3)}
ARMOR_DUR = {"Iron": (165, 240, 225, 195), "Diamond": (363, 528, 495, 429), "Netherite": (407, 592, 555, 481)}
ARMORS = {}
for _n in ("Iron", "Diamond", "Netherite"):
    for _i, _sl in enumerate(ARMOR_SLOTS):
        ARMORS[(_n, _sl)] = reg("%s %s" % (_n, _sl.title()), armor=_sl, tier=_n, defense=ARMOR_DEFENSE[_n][_i],
                                dur=ARMOR_DUR[_n][_i], stack=1)
# --- Hunger and cows (appended last: older saves keep their ids) ---------- #
RAW_BEEF = reg("Raw Beef", food=3)
STEAK = reg("Steak", food=8)
ENDER_PEARL = reg("Ender Pearl", stack=16)
# --- The End (appended last: older saves keep their ids) ------------------- #
EYE_OF_ENDER = reg("Eye of Ender", stack=16)
END_PORTAL = reg("End Portal", hard=-1)
END_STONE = reg("End Stone", block=1, hard=3.0, tool="pickaxe", tier=1)
DRAGON_EGG = reg("Dragon Egg", block=1, hard=4.0)
END_CRYSTAL = reg("End Crystal", stack=16)
BOW = reg("Bow", tool="bow", tier=0, dur=385)
ARROW = reg("Arrow")
# --- Elytra and fireworks (appended last: older saves keep their ids) ------ #
ELYTRA = reg("Elytra", armor="chestplate", tier="Elytra", defense=0, dur=432, stack=1, glider=True)
FIREWORK = reg("Firework Rocket", stack=64)
# --- Books (appended last: older saves keep their ids) ---------------------- #
PAPER = reg("Paper", stack=64)
LEATHER = reg("Leather")
BOOK = reg("Book", stack=1)                  # s[2] holds {"pages": [str, ...]} once written in
BOOK_MAX_PAGES = 250
BOOK_PAGE_CHARS = 600                        # characters per page
# --- Enchanting (appended last: older saves keep their ids) ------------------ #
ENCHANT_TABLE = reg("Enchanting Table", block=1, hard=5.0, tool="pickaxe", tier=2)
GRINDSTONE = reg("Grindstone", block=1, hard=3.0, tool="pickaxe", tier=1)
GRIND_XP = 5                                 # XP refunded per enchantment level removed
XP_BOTTLE = reg("Bottle o' Enchanting", stack=16)    # right-click: 3-11 XP
# --- Fishing, pressure plates and pistons (appended last: older saves keep their ids) ---- #
STRING = reg("String", stack=64)
FISHING_ROD = reg("Fishing Rod", tool="rod", tier=0, dur=64)
RAW_COD = reg("Raw Cod", food=2)
COOKED_COD = reg("Cooked Cod", food=5)
RAW_SALMON = reg("Raw Salmon", food=2)
COOKED_SALMON = reg("Cooked Salmon", food=6)
WOOD_PLATE = reg("Wooden Pressure Plate", block=1, hard=0.5, tool="axe")
STONE_PLATE = reg("Stone Pressure Plate", block=1, hard=0.8, tool="pickaxe", tier=1)
PISTON = reg("Piston", block=1, hard=1.5, tool="pickaxe")
PISTON_DIRS = "LRUD"                                  # facing left / right / up / down
DIRV = ((-1, 0), (1, 0), (0, -1), (0, 1))
PISTON_ANGLE = (180, 0, 90, 270)
PISTON_BASE = tuple(reg("Piston (%s)" % n, block=1, hard=1.5, tool="pickaxe", drop=PISTON) for n in PISTON_DIRS)
PISTON_EXT = tuple(reg("Piston base (%s)" % n, block=1, hard=1.5, tool="pickaxe", drop=PISTON) for n in PISTON_DIRS)
PISTON_HEAD = tuple(reg("Piston head (%s)" % n, block=1, hard=1.5, tool="pickaxe", drop=PISTON) for n in PISTON_DIRS)
PLATES = (WOOD_PLATE, STONE_PLATE)
SOFT_PUSH = PLATES + (LADDER,)                        # a pushed block breaks these (they drop as items)
FREE_PUSH = (AIR, WATER, LAVA) + SOFT_PUSH            # a piston may push into these
IMMOVABLE = (BEDROCK, OBSIDIAN, PORTAL, END_PORTAL, CHEST, SHULKER_BOX, FURNACE, ENDER_CHEST, DRAGON_EGG,
             DOOR_CB, DOOR_CT, DOOR_OB, DOOR_OT) + PISTON_EXT + PISTON_HEAD
PISTON_LIMIT = 12
TICK_DT, TICK_BATCH, TICK_STEP_MAX, FILL_LIMIT = 0.05, 40, 100000, 32768     # command console limits
GIVE_MAX = 2304                                                              # 36 inventory slots of 64
REDSTONE_TORCH = reg("Redstone Torch", block=1, hard=0.1)
TRAPDOOR = reg("Trapdoor", block=1, hard=1.5, tool="axe")                              # the closed block is the item itself
TRAPDOOR_OPEN = reg("Trapdoor (open)", block=1, hard=1.5, tool="axe", drop=TRAPDOOR)
REDSTONE_DUST = reg("Redstone Dust", block=1, hard=0.05)
OBSERVER = reg("Observer", block=1, hard=1.5, tool="pickaxe")
OBSERVER_BLK = tuple(reg("Observer (%s)" % n, block=1, hard=1.5, tool="pickaxe", drop=OBSERVER) for n in PISTON_DIRS)
STICKY = reg("Sticky Piston", block=1, hard=1.5, tool="pickaxe")
STICKY_BASE = tuple(reg("Sticky piston (%s)" % n, block=1, hard=1.5, tool="pickaxe", drop=STICKY) for n in PISTON_DIRS)
STICKY_EXT = tuple(reg("Sticky piston base (%s)" % n, block=1, hard=1.5, tool="pickaxe", drop=STICKY) for n in PISTON_DIRS)
STICKY_HEAD = tuple(reg("Sticky piston head (%s)" % n, block=1, hard=1.5, tool="pickaxe", drop=STICKY) for n in PISTON_DIRS)
SLIME_BALL = reg("Slime Ball")
SLIME_BLOCK = reg("Slime Block", block=1, hard=0.4, tool=None)
LEVER = reg("Lever", block=1, hard=0.1)                                                  # off; also the item
LEVER_ON = reg("Lever (on)", block=1, hard=0.1, drop=LEVER)
BUTTON_STONE = reg("Stone Button", block=1, hard=0.1)                                    # the item, and the unpressed block
BUTTON_STONE_ON = reg("Stone Button (pressed)", block=1, hard=0.1, drop=BUTTON_STONE)
BUTTON_WOOD = reg("Wooden Button", block=1, hard=0.1)
BUTTON_WOOD_ON = reg("Wooden Button (pressed)", block=1, hard=0.1, drop=BUTTON_WOOD)
BUTTONS = (BUTTON_STONE, BUTTON_WOOD)
BUTTON_ON = {BUTTON_STONE: BUTTON_STONE_ON, BUTTON_WOOD: BUTTON_WOOD_ON}
BUTTON_OFF = {v: k for k, v in BUTTON_ON.items()}
BUTTON_TIME = {BUTTON_STONE: 1.0, BUTTON_WOOD: 1.5}                                      # seconds a press lasts
POWER_ON = (LEVER_ON, BUTTON_STONE_ON, BUTTON_WOOD_ON)                                   # blocks that power their surroundings
# --- Farming (appended last) ------------------------------------------------ #
for _n, _t, _d, _m in TIERS:
    TOOLS[(_n, "hoe")] = reg("%s Hoe" % _n, tool="hoe", tier=_t, dur=_d)
TOOLS[("Netherite", "hoe")] = reg("Netherite Hoe", tool="hoe", tier=5, dur=2031, speed=10)
SEEDS = reg("Wheat Seeds")
WHEAT = reg("Wheat")
BREAD = reg("Bread", food=5)
FARMLAND = reg("Farmland", block=1, hard=0.6, tool="shovel", drop=DIRT)               # dry: crops grow slowly
FARMLAND_WET = reg("Farmland (wet)", block=1, hard=0.6, tool="shovel", drop=DIRT)     # water within 4 blocks
FARMLANDS = (FARMLAND, FARMLAND_WET)
CROPS = tuple(reg("Wheat (stage %d)" % i, block=1, hard=0.05, drop=SEEDS) for i in range(1, 5))   # stage 4 is ripe
SAPLING = reg("Sapling", block=1, hard=0.05)                                           # grows into an oak tree
PLANTS = CROPS + (SAPLING,)
IMMOVABLE = IMMOVABLE + STICKY_EXT + STICKY_HEAD
PIST_BASE_OF = dict([(b, (i, False)) for i, b in enumerate(PISTON_BASE)] + [(b, (i, True)) for i, b in enumerate(STICKY_BASE)])


def piston_ids(sticky):
    """(base, extended base, head) id tuples for a normal or a sticky piston."""
    return (STICKY_BASE, STICKY_EXT, STICKY_HEAD) if sticky else (PISTON_BASE, PISTON_EXT, PISTON_HEAD)


OBS_PULSE = 0.2                                                  # seconds an observer's signal lasts
TEX_OBS_ON = {}
SOFT_PUSH = SOFT_PUSH + (TRAPDOOR_OPEN, REDSTONE_DUST, LEVER, LEVER_ON) + tuple(BUTTON_ON) + tuple(BUTTON_OFF) + PLANTS
FREE_PUSH = FREE_PUSH + (TRAPDOOR_OPEN, REDSTONE_DUST, LEVER, LEVER_ON) + tuple(BUTTON_ON) + tuple(BUTTON_OFF) + PLANTS
ENCH = {"efficiency": ("Efficiency", 3), "sharpness": ("Sharpness", 3), "protection": ("Protection", 3),
        "power": ("Power", 3), "unbreaking": ("Unbreaking", 3), "mending": ("Mending", 1)}
ROMAN = ("", "I", "II", "III")
END_CX, END_SURF, END_HALF = WW // 2, 60, 80          # island centre column, surface row, half width
END_PILLARS = ((END_CX - 32, 17), (END_CX + 32, 23))   # (centre column, height above the surface)
END_SPAWN_X = END_CX - 68
DOOR_TOGGLE = {DOOR_CB: DOOR_OB, DOOR_OB: DOOR_CB, DOOR_CT: DOOR_OT, DOOR_OT: DOOR_CT}
NONSOLID = (AIR, LAVA, PORTAL, LADDER, DOOR_OB, DOOR_OT, WATER, END_PORTAL, REDSTONE_TORCH, TRAPDOOR_OPEN, REDSTONE_DUST, LEVER, LEVER_ON) + tuple(BUTTON_ON) + tuple(BUTTON_OFF) + PLANTS + PLATES
ALPHA_BLOCKS = (LADDER, DOOR_OB, DOOR_OT, REDSTONE_TORCH, TRAPDOOR_OPEN, REDSTONE_DUST, LEVER, LEVER_ON) + tuple(BUTTON_ON) + tuple(BUTTON_OFF) + PLANTS + PLATES + PISTON_HEAD + STICKY_HEAD
CREATIVE_ITEMS = [i for i in ITEMS if i not in (LAVA, PORTAL, END_PORTAL, WATER, DOOR_CB, DOOR_CT, DOOR_OB, DOOR_OT)
                  + PISTON_BASE + PISTON_EXT + PISTON_HEAD + (TRAPDOOR_OPEN, LEVER_ON, FARMLAND_WET) + tuple(BUTTON_OFF) + CROPS + OBSERVER_BLK + STICKY_BASE + STICKY_EXT + STICKY_HEAD]
SOLID = [b not in NONSOLID for b in range(256)]


def targetable(b):
    """Blocks the cursor can highlight and mine (solid ones plus ladders and open doors)."""
    return SOLID[b] or b in ALPHA_BLOCKS

# Recipes ------------------------------------------------------------------- #
RECIPES = []


def recipe(rows, key, out, n=1):
    key = dict(key)
    key["."] = 0
    RECIPES.append(([[key[c] for c in row] for row in rows], out, n))


recipe(["L"], {"L": LOG}, PLANKS, 4)
recipe(["P", "P"], {"P": PLANKS}, STICK, 4)
recipe(["PP", "PP"], {"P": PLANKS}, TABLE)
recipe(["CCC", "C.C", "CCC"], {"C": COBBLE}, FURNACE)
recipe(["PPP", "P.P", "PPP"], {"P": PLANKS}, CHEST)
_SHAPES = {"pickaxe": ["MMM", ".S.", ".S."], "axe": ["MM", "MS", ".S"],
           "shovel": ["M", "S", "S"], "sword": ["M", "M", "S"]}
for _n, _t, _d, _m in TIERS:
    for _k in TOOL_KINDS:
        recipe(_SHAPES[_k], {"M": _m, "S": STICK}, TOOLS[(_n, _k)])

recipe(["SSI", "SSI", "II."], {"S": NETHERITE_SCRAP, "I": IRON_INGOT}, NETHERITE_INGOT)
for _n, _t, _d, _m in TIERS:
    recipe(["MM", ".S", ".S"], {"M": _m, "S": STICK}, TOOLS[(_n, "hoe")])
recipe(["N", "P"], {"N": NETHERITE_INGOT, "P": TOOLS[("Diamond", "hoe")]}, TOOLS[("Netherite", "hoe")])
recipe(["WWW"], {"W": WHEAT}, BREAD)
for _k in TOOL_KINDS:      # smithing: netherite ingot above a diamond tool
    recipe(["N", "P"], {"N": NETHERITE_INGOT, "P": TOOLS[("Diamond", _k)]}, TOOLS[("Netherite", _k)])
recipe(["I", "C"], {"I": IRON_INGOT, "C": COAL}, FLINT_STEEL)
recipe(["S.S", "SSS", "S.S"], {"S": STICK}, LADDER, 3)
recipe(["I.I", ".I."], {"I": IRON_INGOT}, BUCKET)
recipe(["D", "C", "D"], {"D": DIAMOND, "C": CHEST}, SHULKER_BOX)
recipe(["S", "D", "I"], {"S": NETHERITE_SCRAP, "D": DIAMOND, "I": IRON_INGOT}, PROTECTION_POTION)
recipe(["C", "D", "C"], {"C": COAL, "D": DIAMOND}, REGEN_POTION)
recipe(["..S", ".ST", "S.T"], {"S": STICK, "T": STRING}, FISHING_ROD)
recipe(["CC", "CC"], {"C": COAL}, SLIME_BALL)                       # coal stands in for slime
recipe(["SSS", "SSS", "SSS"], {"S": SLIME_BALL}, SLIME_BLOCK)
recipe(["B"], {"B": SLIME_BLOCK}, SLIME_BALL, 9)
recipe(["S", "P"], {"S": SLIME_BALL, "P": PISTON}, STICKY)
recipe(["CCC", "DDI"], {"C": COBBLE, "D": REDSTONE_DUST, "I": IRON_INGOT}, OBSERVER)      # iron stands in for quartz
recipe(["C"], {"C": COAL}, REDSTONE_DUST, 2)                       # coal stands in for redstone
recipe(["S", "C"], {"S": STICK, "C": COBBLE}, LEVER)
recipe(["S"], {"S": STONE}, BUTTON_STONE)
recipe(["P"], {"P": PLANKS}, BUTTON_WOOD)
recipe(["D", "S"], {"D": REDSTONE_DUST, "S": STICK}, REDSTONE_TORCH)
recipe(["PPP", "PPP"], {"P": PLANKS}, TRAPDOOR, 2)
recipe(["PP"], {"P": PLANKS}, WOOD_PLATE)
recipe(["SS"], {"S": STONE}, STONE_PLATE)
recipe(["PPP", "CIC", "CKC"], {"P": PLANKS, "C": COBBLE, "I": IRON_INGOT, "K": COAL}, PISTON)   # coal stands in for redstone
recipe(["I", "D", "C"], {"I": IRON_INGOT, "D": DIAMOND, "C": COAL}, XP_BOTTLE, 2)
recipe(["OOO", "ODO", "OOO"], {"O": OBSIDIAN, "D": DIAMOND}, ENDER_CHEST)
recipe(["DA", "AD"], {"D": DIAMOND, "A": ANCIENT_DEBRIS}, ENDER_PEARL)
recipe([".SP", "S.P", ".SP"], {"S": STICK, "P": PLANKS}, BOW)        # planks stand in for string
recipe(["DND", "DED", "D.D"], {"D": DIAMOND, "N": NETHERITE_INGOT, "E": EYE_OF_ENDER}, ELYTRA)
recipe(["C", "P"], {"C": COAL, "P": PLANKS}, FIREWORK, 3)         # coal = gunpowder, planks = paper
recipe(["C", "S"], {"C": COAL, "S": STICK}, ARROW, 4)         # coal stands in for the flint head
recipe(["O", "E", "D"], {"O": OBSIDIAN, "E": EYE_OF_ENDER, "D": DIAMOND}, END_CRYSTAL)
recipe(["PPP"], {"P": PLANKS}, PAPER, 3)                        # planks stand in for sugar cane
recipe(["P", "P", "L"], {"P": PAPER, "L": LEATHER}, BOOK)       # leather comes from cows
recipe(["P", "C"], {"P": ENDER_PEARL, "C": COAL}, EYE_OF_ENDER)     # coal stands in for blaze powder   # 2x2, fits the inventory grid
recipe(["S#S", "P.P"], {"S": STICK, "#": STONE, "P": PLANKS}, GRINDSTONE)
recipe([".B.", "DOD", "OOO"], {"B": BOOK, "D": DIAMOND, "O": OBSIDIAN}, ENCHANT_TABLE)
recipe(["C#C", "#C#", "C#C"], {"C": COAL, "#": COBBLE}, TNT)   # coal stands in for gunpowder
_ASHAPES = {"helmet": ["MMM", "M.M"], "chestplate": ["M.M", "MMM", "MMM"],
            "leggings": ["MMM", "M.M", "M.M"], "boots": ["M.M", "M.M"]}
for _sl in ARMOR_SLOTS:
    recipe(_ASHAPES[_sl], {"M": IRON_INGOT}, ARMORS[("Iron", _sl)])
    recipe(_ASHAPES[_sl], {"M": DIAMOND}, ARMORS[("Diamond", _sl)])
    recipe(["N", "P"], {"N": NETHERITE_INGOT, "P": ARMORS[("Diamond", _sl)]}, ARMORS[("Netherite", _sl)])   # smithing
POTIONS = (PROTECTION_POTION, REGEN_POTION, XP_BOTTLE)
PROTECTION_TIME = 120.0
for _blk, _it in ((IRON_BLOCK, IRON_INGOT), (DIAMOND_BLOCK, DIAMOND), (NETHERITE_BLOCK, NETHERITE_INGOT)):
    recipe(["III", "III", "III"], {"I": _it}, _blk)
    recipe(["B"], {"B": _blk}, _it, 9)
recipe(["PP", "PP", "PP"], {"P": PLANKS}, DOOR_ITEM, 3)

SMELT = {RAW_BEEF: STEAK, IRON_ORE: IRON_INGOT, ANCIENT_DEBRIS: NETHERITE_SCRAP, COBBLE: STONE, LOG: COAL}       # log -> "charcoal"
SMELT[RAW_COD] = COOKED_COD
SMELT[RAW_SALMON] = COOKED_SALMON
FUEL = {COAL: 80.0, LOG: 15.0, PLANKS: 15.0, STICK: 5.0, LAVA_BUCKET: 1000.0}
SMELT_TIME = 10.0


def trim(g):
    rows = [i for i, r in enumerate(g) if any(r)]
    if not rows:
        return []
    cols = [j for j in range(len(g[0])) if any(r[j] for r in g)]
    return [r[min(cols):max(cols) + 1] for r in g[min(rows):max(rows) + 1]]


def match_recipe(grid):
    t = trim(grid)
    if not t:
        return None
    for pat, out, n in RECIPES:
        if t == pat or t == [r[::-1] for r in pat]:
            return out, n
    return None


def maxstack(i):
    if "stack" in ITEMS[i]:
        return ITEMS[i]["stack"]
    return 1 if "tool" in ITEMS[i] and "dur" in ITEMS[i] else 64


def new_stack(i, n=1):
    return [i, n, ITEMS[i].get("dur")]


def can_fit(cont, rng, i, n):
    mx, free = maxstack(i), 0
    for k in rng:
        s = cont[k]
        if s is None:
            free += mx
        elif s[0] == i and mx > 1:
            free += mx - s[1]
    return free >= n


class Dur(int):
    """A durability value that can carry enchantments in `.ench` ({key: level}); it behaves like an int
    and travels with the stack through drops, chests, shulker boxes and saves."""
    ench = None


def ench_of(st):
    d = st[2] if st and len(st) > 2 else None
    return (getattr(d, "ench", None) or {}) if isinstance(d, int) else {}


def dur_sub(st, n):
    old = st[2]
    new = Dur(old - n)
    e = getattr(old, "ench", None)
    if e:
        new.ench = e
    st[2] = new


def ench_options(item):
    """Enchantment keys that can go on an item (empty list if it can't be enchanted)."""
    it = ITEMS[item]
    if "dur" not in it:
        return []
    out = []
    t = it.get("tool")
    if "armor" in it and not it.get("glider"):
        out.append("protection")
    if t in ("pickaxe", "axe", "shovel", "hoe"):
        out.append("efficiency")
    if t in ("sword", "axe"):
        out.append("sharpness")
    if t == "bow":
        out.append("power")
    out.append("unbreaking")
    out.append("mending")
    return out


def ench_label(k, v):
    return ENCH[k][0] if ENCH[k][1] == 1 else "%s %s" % (ENCH[k][0], ROMAN[v])


def stack_name(s):
    n = ITEMS[s[0]]["name"]
    e = ench_of(s)
    if e:
        n += " (" + ", ".join(ench_label(k, v) for k, v in e.items() if k in ENCH) + ")"
    return n


def put_into(cont, rng, s):
    """Move stack s (mutated) into container slots rng. True if all moved."""
    mx = maxstack(s[0])
    if mx > 1:
        for k in rng:
            t = cont[k]
            if t and t[0] == s[0] and t[1] < mx:
                m = min(mx - t[1], s[1])
                t[1] += m
                s[1] -= m
                if s[1] <= 0:
                    return True
    for k in rng:
        if cont[k] is None:
            cont[k] = list(s)
            s[1] = 0
            return True
    return False


def break_time(bid, held):
    b = ITEMS[bid]
    if b["hard"] < 0:
        return None, False
    tool = ITEMS[held[0]] if held else None
    ttype = tool.get("tool") if tool else None
    tier = tool.get("tier", 0) if tool else 0
    need = b.get("tier", 0)
    right = ttype is not None and ttype == b.get("tool")
    can = need == 0 or (right and tier >= need)
    speed = (tool.get("speed", TIER_SPEED[tier]) if tool else 1) if right else 1
    if right:
        speed *= 1 + 0.5 * ench_of(held).get("efficiency", 0) ** 2
    return max(0.05, b["hard"] * (1.5 if can else 5.0) / speed), can


def drops_for(bid, rnd):
    if bid == LEAVES:
        r = rnd.random()
        return [STICK] if r < 0.2 else ([STRING] if r < 0.32 else ([SAPLING] if r < 0.40 else []))
    if bid == GRASS:
        return [DIRT, SEEDS] if rnd.random() < 0.12 else [DIRT]       # grass sometimes hides seeds
    if bid == CROPS[-1]:
        return [WHEAT] + [SEEDS] * rnd.randint(1, 3)                  # ripe: wheat and seeds
    return [ITEMS[bid].get("drop", bid)]


# --------------------------------------------------------------------------- #
# Textures (procedural 16x16 "potato" pixel art, scaled up)
# --------------------------------------------------------------------------- #
TEX, ICON, ICON_S, CRACKS = {}, {}, {}, []
TEX_FURNACE_ON = None
TEX_TNT_FLASH = None
TEX_PLATE_ON = {}
TEX_LEVER = {}
TEX_BUTTON = {}
TEX_TORCH_OFF = None
BG_TILE = None
BG_NETHER = None
BG_END = None
ANIM = {}


def cl(v):
    return max(0, min(255, int(v)))


def mk(base, var, seed):
    s = pygame.Surface((16, 16))
    r = random.Random(seed)
    for y in range(16):
        for x in range(16):
            d = r.randint(-var, var)
            s.set_at((x, y), (cl(base[0] + d), cl(base[1] + d), cl(base[2] + d)))
    return s


def ore_tex(color, seed, base=(125, 125, 125)):
    s = mk(base, 12, 1)
    r = random.Random(seed)
    for _ in range(5):
        x, y = r.randint(1, 13), r.randint(1, 13)
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)):
            if r.random() < 0.85:
                s.set_at((x + dx, y + dy), color)
    return s


def tool_icon(kind, col):
    s = pygame.Surface((16, 16), pygame.SRCALPHA)
    wood = (120, 85, 40)
    d = pygame.draw
    if kind == "stick":
        d.line(s, wood, (3, 13), (12, 4), 2)
    elif kind == "pickaxe":
        d.line(s, wood, (2, 14), (10, 6), 2)
        d.line(s, col, (5, 2), (14, 11), 2)
    elif kind == "axe":
        d.line(s, wood, (3, 14), (11, 6), 2)
        d.polygon(s, col, [(8, 2), (14, 4), (14, 9), (10, 8)])
    elif kind == "shovel":
        d.line(s, wood, (3, 14), (10, 7), 2)
        d.circle(s, col, (12, 4), 3)
    elif kind == "hoe":
        d.line(s, wood, (3, 14), (11, 5), 2)
        d.line(s, col, (7, 3), (13, 3), 2)
        d.line(s, col, (7, 3), (7, 6), 2)
    elif kind == "sword":
        d.line(s, col, (5, 11), (13, 3), 3)
        d.line(s, wood, (3, 9), (7, 13), 2)
        d.line(s, wood, (2, 14), (4, 12), 2)
    elif kind == "pearl":
        d.circle(s, (20, 110, 100), (8, 8), 6)
        d.circle(s, (40, 175, 150), (8, 8), 5)
        d.circle(s, (90, 225, 195), (7, 7), 3)
        d.circle(s, (225, 255, 245), (6, 6), 1)
    elif kind == "bow":
        d.arc(s, (150, 105, 50), (-2, 1, 14, 14), -1.4, 1.4, 3)
        d.line(s, (235, 235, 235), (8, 2), (8, 14), 1)
        d.line(s, (235, 235, 235), (8, 8), (3, 8), 1)
    elif kind == "elytra":
        for sgn in (1, -1):
            cxx = 8
            pts = [(cxx, 2), (cxx + sgn * 7, 4), (cxx + sgn * 7, 13), (cxx + sgn * 1, 14)]
            d.polygon(s, (175, 165, 200), pts)
            d.polygon(s, (110, 100, 140), pts, 1)
            d.line(s, (215, 205, 235), (cxx + sgn * 2, 5), (cxx + sgn * 5, 11), 1)
    elif kind == "firework":
        d.line(s, (140, 100, 55), (8, 8), (8, 15), 1)
        d.rect(s, (200, 50, 50), (6, 4, 4, 7))
        d.rect(s, (240, 240, 240), (6, 7, 4, 1))
        d.polygon(s, (255, 190, 60), [(8, 0), (10, 4), (6, 4)])
    elif kind == "arrow":
        d.line(s, (150, 105, 50), (3, 13), (12, 4), 2)
        d.polygon(s, (170, 170, 175), [(14, 2), (9, 4), (12, 7)])
        d.line(s, (235, 235, 235), (2, 11), (5, 14), 1)
        d.line(s, (235, 235, 235), (3, 10), (6, 13), 1)
    elif kind == "rod":
        d.line(s, wood, (2, 14), (12, 3), 2)
        d.line(s, (235, 235, 235), (12, 3), (14, 12), 1)
        d.circle(s, (225, 40, 40), (14, 12), 2)
    elif kind == "string":
        d.line(s, (240, 240, 240), (2, 12), (13, 4), 1)
        d.line(s, (225, 225, 225), (3, 5), (12, 13), 1)
        d.line(s, (240, 240, 240), (2, 8), (14, 9), 1)
    elif kind == "fish":
        c = col or (200, 170, 110)
        d.polygon(s, c, [(2, 8), (7, 4), (12, 6), (12, 10), (7, 12)])
        d.polygon(s, tuple(max(0, v - 40) for v in c), [(11, 8), (15, 5), (15, 11)])
        d.rect(s, (20, 20, 20), (4, 7, 2, 2))
    elif kind == "paper":
        d.rect(s, (238, 232, 212), (3, 2, 10, 12))
        d.rect(s, (175, 168, 148), (3, 2, 10, 12), 1)
        for yy in (5, 8, 11):
            d.line(s, (190, 183, 163), (5, yy), (11, yy))
    elif kind == "leather":
        d.polygon(s, (150, 92, 52), [(3, 4), (7, 2), (10, 4), (14, 5), (13, 11), (9, 14), (4, 12), (2, 8)])
        d.polygon(s, (105, 62, 34), [(3, 4), (7, 2), (10, 4), (14, 5), (13, 11), (9, 14), (4, 12), (2, 8)], 1)
        d.line(s, (185, 125, 80), (5, 6), (10, 7))
    elif kind == "book":
        d.rect(s, (110, 40, 40), (2, 2, 12, 13))
        d.rect(s, (70, 22, 22), (2, 2, 12, 13), 1)
        d.rect(s, (235, 225, 190), (4, 3, 9, 11))
        d.line(s, (150, 140, 110), (5, 6), (11, 6))
        d.line(s, (150, 140, 110), (5, 9), (11, 9))
        d.rect(s, (70, 22, 22), (2, 2, 3, 13))
    elif kind == "crystal":
        d.polygon(s, (110, 40, 130), [(8, 0), (14, 8), (8, 16), (2, 8)])
        d.polygon(s, (235, 100, 225), [(8, 1), (13, 8), (8, 15), (3, 8)])
        d.polygon(s, (255, 235, 255), [(8, 4), (10, 8), (8, 12), (6, 8)])
    elif kind == "eye":
        d.circle(s, (15, 70, 60), (8, 8), 7)
        d.circle(s, (45, 190, 150), (8, 8), 6)
        d.circle(s, (15, 30, 30), (8, 8), 3)
        d.circle(s, (225, 255, 245), (6, 6), 1)
    elif kind in ("beef", "steak"):
        raw = kind == "beef"
        c, edge, fat = ((205, 70, 80), (140, 40, 55), (245, 205, 205)) if raw else ((130, 78, 44), (80, 44, 24), (190, 140, 90))
        d.polygon(s, c, [(2, 7), (5, 3), (11, 3), (14, 6), (13, 12), (8, 14), (3, 12)])
        d.polygon(s, edge, [(2, 7), (5, 3), (11, 3), (14, 6), (13, 12), (8, 14), (3, 12)], 1)
        d.line(s, fat, (5, 5), (10, 5), 1)
        d.line(s, fat, (4, 9), (9, 11), 1)
        if not raw:
            d.line(s, (60, 32, 18), (6, 7), (11, 9), 1)
            d.line(s, (60, 32, 18), (5, 11), (9, 8), 1)
        else:
            d.circle(s, fat, (10, 9), 2)
    elif kind in ARMOR_SLOTS:
        c = col
        dk = tuple(int(v * 0.6) for v in c)
        lt = tuple(min(255, int(v * 1.25) + 10) for v in c)
        if kind == "helmet":
            d.rect(s, c, (3, 3, 10, 9))
            d.rect(s, (0, 0, 0, 0), (5, 8, 6, 4))
            d.rect(s, dk, (3, 3, 10, 9), 1)
            d.line(s, lt, (4, 4), (11, 4))
        elif kind == "chestplate":
            d.rect(s, c, (3, 3, 10, 12))
            d.rect(s, c, (1, 3, 3, 6))
            d.rect(s, c, (12, 3, 3, 6))
            d.polygon(s, (0, 0, 0, 0), [(6, 3), (10, 3), (8, 6)])
            d.rect(s, dk, (3, 3, 10, 12), 1)
            d.line(s, lt, (4, 7), (4, 13))
        elif kind == "leggings":
            d.rect(s, c, (3, 2, 10, 5))
            d.rect(s, c, (3, 7, 4, 7))
            d.rect(s, c, (9, 7, 4, 7))
            d.rect(s, dk, (3, 2, 10, 5), 1)
            d.rect(s, dk, (3, 7, 4, 7), 1)
            d.rect(s, dk, (9, 7, 4, 7), 1)
        else:
            d.rect(s, c, (2, 7, 5, 6))
            d.rect(s, c, (9, 7, 5, 6))
            d.rect(s, c, (1, 11, 6, 3))
            d.rect(s, c, (9, 11, 6, 3))
            d.rect(s, dk, (2, 7, 5, 7), 1)
            d.rect(s, dk, (9, 7, 5, 7), 1)
    elif kind == "coal":
        d.polygon(s, (35, 35, 35), [(4, 6), (8, 3), (12, 5), (12, 10), (7, 12), (4, 10)])
        s.set_at((7, 5), (90, 90, 90))
    elif kind == "ingot":
        c = col or (225, 225, 225)
        d.polygon(s, c, [(2, 10), (5, 5), (14, 5), (11, 10)])
        d.line(s, tuple(int(v * 0.7) for v in c), (2, 10), (11, 10))
    elif kind == "scrap":
        d.polygon(s, (110, 78, 66), [(3, 8), (7, 4), (13, 6), (12, 11), (6, 12)])
        d.line(s, (150, 112, 90), (5, 7), (11, 7))
        d.line(s, (70, 48, 42), (6, 11), (11, 10))
    elif kind == "door":
        d.rect(s, (110, 76, 38), (4, 1, 8, 14))
        d.rect(s, (168, 124, 70), (5, 2, 6, 12))
        d.rect(s, (130, 92, 48), (6, 3, 4, 4), 1)
        d.rect(s, (130, 92, 48), (6, 8, 4, 5), 1)
        d.rect(s, (225, 225, 225), (9, 8, 1, 2))
    elif kind == "bucket":
        d.line(s, (150, 150, 158), (4, 4), (11, 4), 1)
        d.polygon(s, (190, 190, 198), [(3, 5), (13, 5), (11, 14), (5, 14)])
        d.polygon(s, (150, 150, 158), [(3, 5), (5, 5), (7, 14), (5, 14)])
        if col:
            d.rect(s, col, (4, 5, 8, 3))
            d.line(s, (255, 230, 120), (6, 6), (9, 6))
        else:
            d.rect(s, (90, 90, 98), (4, 5, 8, 2))
    elif kind == "potion":
        c = col or (200, 200, 220)
        d.rect(s, (200, 215, 235), (6, 1, 4, 3))                       # cork / neck
        d.rect(s, (225, 235, 250), (6, 3, 4, 3))
        d.polygon(s, (205, 220, 240), [(6, 5), (10, 5), (14, 10), (13, 14), (3, 14), (2, 10)])
        d.polygon(s, c, [(4, 9), (12, 9), (13, 10), (12, 13), (4, 13), (3, 10)])
        d.line(s, (255, 255, 255), (5, 10), (5, 12))
    elif kind == "lighter":
        d.polygon(s, (95, 95, 100), [(2, 7), (6, 3), (10, 5), (9, 10), (4, 11)])
        d.line(s, (150, 150, 155), (4, 6), (7, 4))
        d.line(s, (215, 215, 225), (8, 13), (14, 5), 2)
        d.line(s, (215, 215, 225), (14, 5), (14, 10), 2)
    elif kind == "diamond":
        d.polygon(s, (90, 235, 235), [(8, 2), (13, 6), (8, 14), (3, 6)])
        d.line(s, (200, 255, 255), (8, 3), (5, 6))
    return s


def build_assets():
    global TEX_FURNACE_ON, BG_TILE, BG_NETHER, TEX_TNT_FLASH, BG_END, TEX_TORCH_OFF
    t = {}
    t[STONE] = mk((125, 125, 125), 12, 1)
    t[DIRT] = mk((134, 96, 67), 14, 2)
    g = t[DIRT].copy()
    r = random.Random(3)
    for x in range(16):
        for y in range(r.randint(2, 4)):
            v = r.randint(-12, 12)
            g.set_at((x, y), (cl(70 + v), cl(160 + v), cl(50 + v)))
    t[GRASS] = g
    fm_ = mk((98, 64, 36), 9, 41)
    fw_ = mk((64, 42, 26), 7, 42)
    for yy_ in (3, 8, 13):
        pygame.draw.line(fm_, (70, 44, 24), (0, yy_), (15, yy_))
        pygame.draw.line(fw_, (40, 26, 16), (0, yy_), (15, yy_))
    t[FARMLAND], t[FARMLAND_WET] = fm_, fw_
    c = mk((120, 120, 120), 10, 4)
    r = random.Random(5)
    for _ in range(14):
        col = (90, 90, 90) if r.random() < 0.5 else (150, 150, 150)
        pygame.draw.rect(c, col, (r.randint(0, 13), r.randint(0, 13), r.randint(2, 4), r.randint(2, 4)), 1)
    t[COBBLE] = c
    lg = mk((110, 85, 50), 8, 6)
    for x in range(16):
        if x % 4 == 0 or x % 7 == 3:
            for y in range(16):
                p = lg.get_at((x, y))
                lg.set_at((x, y), (cl(p[0] - 28), cl(p[1] - 24), cl(p[2] - 18)))
    t[LOG] = lg
    lv = mk((48, 130, 40), 22, 7)
    r = random.Random(8)
    for x in range(16):
        for y in range(16):
            if r.random() < 0.22:
                lv.set_at((x, y), (25, 90, 25))
    t[LEAVES] = lv
    sl_ = mk((110, 196, 80), 9, 777)
    pygame.draw.rect(sl_, (66, 146, 48), (0, 0, 16, 16), 1)
    pygame.draw.rect(sl_, (150, 226, 122), (4, 4, 8, 8))
    pygame.draw.rect(sl_, (66, 146, 48), (4, 4, 8, 8), 1)
    t[SLIME_BLOCK] = sl_
    pl = mk((172, 132, 78), 6, 9)
    for y in range(3, 16, 4):
        for x in range(16):
            p = pl.get_at((x, y))
            pl.set_at((x, y), (cl(p[0] - 40), cl(p[1] - 40), cl(p[2] - 30)))
    t[PLANKS] = pl
    t[COAL_ORE] = ore_tex((25, 25, 25), 10)
    t[IRON_ORE] = ore_tex((215, 165, 125), 11)
    t[DIAMOND_ORE] = ore_tex((80, 230, 230), 12)
    t[BEDROCK] = mk((50, 50, 50), 30, 13)
    tb = t[PLANKS].copy()
    pygame.draw.rect(tb, (115, 75, 35), (0, 0, 16, 4))
    pygame.draw.rect(tb, (150, 150, 150), (3, 7, 4, 2))
    pygame.draw.rect(tb, (190, 60, 50), (10, 7, 3, 5))
    pygame.draw.rect(tb, (80, 50, 20), (0, 0, 16, 16), 1)
    t[TABLE] = tb
    fu = mk((110, 110, 110), 10, 14)
    pygame.draw.rect(fu, (60, 60, 60), (0, 0, 16, 16), 1)
    pygame.draw.rect(fu, (15, 15, 15), (4, 5, 8, 7))
    fon = fu.copy()
    pygame.draw.rect(fon, (255, 150, 30), (5, 8, 6, 3))
    pygame.draw.rect(fon, (255, 230, 80), (7, 7, 2, 2))
    t[FURNACE] = fu
    ch = mk((160, 110, 50), 8, 15)
    pygame.draw.rect(ch, (90, 55, 20), (0, 0, 16, 16), 1)
    pygame.draw.line(ch, (90, 55, 20), (0, 5), (15, 5))
    pygame.draw.rect(ch, (205, 205, 205), (7, 6, 2, 3))
    t[CHEST] = ch
    t[NETHERRACK] = mk((112, 48, 50), 16, 20)
    rr_ = random.Random(21)
    for _ in range(26):
        t[NETHERRACK].set_at((rr_.randint(0, 15), rr_.randint(0, 15)),
                             (150, 70, 66) if rr_.random() < 0.5 else (78, 30, 34))
    ob = mk((24, 12, 40), 8, 22)
    for _ in range(18):
        ob.set_at((rr_.randint(0, 15), rr_.randint(0, 15)), (70, 40, 110))
    pygame.draw.rect(ob, (12, 6, 22), (0, 0, 16, 16), 1)
    t[OBSIDIAN] = ob
    ad = mk((96, 62, 52), 10, 26)
    for y in (3, 7, 11, 14):
        for x in range(16):
            if rr_.random() < 0.7:
                ad.set_at((x, y), (136, 98, 74))
    for _ in range(20):
        ad.set_at((rr_.randint(0, 15), rr_.randint(0, 15)), (58, 36, 32))
    pygame.draw.rect(ad, (70, 45, 40), (0, 0, 16, 16), 1)
    t[ANCIENT_DEBRIS] = ad
    ib = mk((218, 218, 224), 6, 50)
    pygame.draw.rect(ib, (165, 165, 175), (0, 0, 16, 16), 1)
    pygame.draw.rect(ib, (188, 188, 198), (3, 3, 10, 10), 1)
    t[IRON_BLOCK] = ib
    db = mk((70, 200, 200), 10, 51)
    pygame.draw.rect(db, (38, 148, 160), (0, 0, 16, 16), 1)
    pygame.draw.polygon(db, (150, 245, 245), [(8, 3), (13, 8), (8, 13), (3, 8)], 1)
    for px_, py_ in ((8, 7), (6, 6), (10, 9)):
        db.set_at((px_, py_), (235, 255, 255))
    t[DIAMOND_BLOCK] = db
    nb = mk((62, 54, 60), 6, 52)
    pygame.draw.rect(nb, (36, 30, 36), (0, 0, 16, 16), 1)
    pygame.draw.line(nb, (40, 34, 40), (8, 1), (8, 14))
    pygame.draw.line(nb, (40, 34, 40), (1, 8), (14, 8))
    pygame.draw.rect(nb, (98, 84, 94), (2, 2, 5, 5), 1)
    pygame.draw.rect(nb, (98, 84, 94), (9, 9, 5, 5), 1)
    t[NETHERITE_BLOCK] = nb
    sh = mk((152, 100, 172), 7, 60)
    pygame.draw.rect(sh, (118, 70, 140), (0, 0, 16, 6))
    pygame.draw.rect(sh, (84, 46, 104), (0, 0, 16, 16), 1)
    pygame.draw.line(sh, (84, 46, 104), (0, 6), (15, 6))
    pygame.draw.rect(sh, (232, 205, 248), (6, 5, 4, 3))
    pygame.draw.rect(sh, (84, 46, 104), (6, 5, 4, 3), 1)
    t[SHULKER_BOX] = sh
    ec = mk((26, 34, 40), 5, 70)
    pygame.draw.rect(ec, (12, 16, 22), (0, 0, 16, 16), 1)
    pygame.draw.rect(ec, (40, 58, 64), (1, 1, 14, 5))
    pygame.draw.line(ec, (12, 16, 22), (0, 6), (15, 6))
    pygame.draw.rect(ec, (62, 225, 190), (6, 5, 4, 3))
    pygame.draw.rect(ec, (12, 16, 22), (6, 5, 4, 3), 1)
    pygame.draw.circle(ec, (62, 225, 190), (8, 11), 2, 1)
    t[ENDER_CHEST] = ec
    et = mk((34, 22, 52), 5, 90)
    pygame.draw.rect(et, (176, 34, 46), (0, 0, 16, 5))
    pygame.draw.rect(et, (20, 12, 30), (0, 0, 16, 16), 1)
    for ex_, ey_ in ((3, 9), (12, 9), (7, 12), (8, 2)):
        pygame.draw.rect(et, (90, 235, 235), (ex_, ey_, 2, 2))
    t[ENCHANT_TABLE] = et
    gs = mk((120, 92, 58), 6, 95)
    pygame.draw.rect(gs, (30, 22, 14), (0, 0, 16, 16), 1)
    pygame.draw.circle(gs, (150, 150, 156), (8, 7), 5)
    pygame.draw.circle(gs, (92, 92, 98), (8, 7), 5, 1)
    pygame.draw.circle(gs, (60, 60, 66), (8, 7), 1)
    pygame.draw.rect(gs, (70, 50, 30), (1, 13, 3, 3))
    pygame.draw.rect(gs, (70, 50, 30), (12, 13, 3, 3))
    t[GRINDSTONE] = gs
    tn = mk((200, 42, 36), 10, 80)
    for yy in (0, 1, 14, 15):
        pygame.draw.line(tn, (150, 28, 26), (0, yy), (15, yy))
    pygame.draw.rect(tn, (236, 232, 222), (0, 5, 16, 6))
    pygame.draw.rect(tn, (150, 28, 26), (0, 5, 16, 6), 1)
    for lx, ly, lw, lh in ((2, 6, 3, 1), (3, 7, 1, 3), (6, 6, 1, 4), (9, 6, 1, 4), (7, 7, 1, 1), (8, 8, 1, 1),
                           (11, 6, 3, 1), (11, 7, 1, 3), (11, 9, 3, 1), (13, 7, 1, 2)):
        pygame.draw.rect(tn, (40, 30, 30), (lx, ly, lw, lh))
    t[TNT] = tn
    TEX_TNT_FLASH = None                  # filled in once TEX has been scaled
    a_ = 2 * math.pi / 16

    def lava_frame(i):
        sf = pygame.Surface((16, 16))
        for y in range(16):
            for x in range(16):
                v = (math.sin(a_ * (x + 4 * i)) + math.sin(a_ * 2 * y - a_ * 4 * i + x * a_)) / 4 + 0.5
                sf.set_at((x, y), lerpc((190, 50, 10), (255, 200, 60), max(0.0, min(1.0, v))))
        return sf

    def portal_frame(i):
        sf = pygame.Surface((16, 16), pygame.SRCALPHA)
        for y in range(16):
            for x in range(16):
                v = (math.sin(a_ * (x + y) + i * math.pi / 2) + math.sin(a_ * (x - 2 * y) - i * math.pi / 2)) / 4 + 0.5
                sf.set_at((x, y), (int(90 + 90 * v), int(20 + 40 * v), int(160 + 70 * v), int(120 + 90 * v)))
        return sf

    def end_portal_frame(i):
        sf = pygame.Surface((16, 16))
        sf.fill((8, 10, 20))
        rr_ = random.Random(40 + i)
        for _ in range(20):
            sf.set_at((rr_.randint(0, 15), rr_.randint(0, 15)), rr_.choice(((60, 200, 170), (130, 90, 220), (40, 120, 110))))
        return sf

    t[LAVA] = lava_frame(0)
    t[PORTAL] = portal_frame(0)
    t[END_PORTAL] = end_portal_frame(0)
    t[END_STONE] = mk((222, 222, 158), 9, 90)
    egg = pygame.Surface((16, 16))
    egg.fill((12, 8, 22))
    pygame.draw.ellipse(egg, (22, 8, 38), (3, 1, 10, 14))
    pygame.draw.ellipse(egg, (70, 20, 110), (4, 2, 8, 12))
    pygame.draw.ellipse(egg, (140, 60, 190), (5, 3, 3, 5))
    t[DRAGON_EGG] = egg
    for k, v in t.items():
        TEX[k] = pygame.transform.scale(v.convert(), (TILE, TILE))
    TEX_FURNACE_ON = pygame.transform.scale(fon.convert(), (TILE, TILE))
    TEX_TNT_FLASH = TEX[TNT].copy()
    TEX_TNT_FLASH.fill((120, 120, 120), special_flags=pygame.BLEND_RGB_ADD)
    BG_TILE = pygame.transform.scale(mk((38, 30, 26), 6, 16).convert(), (TILE, TILE))
    BG_NETHER = pygame.transform.scale(mk((46, 16, 20), 5, 24).convert(), (TILE, TILE))
    wood, dark = (166, 122, 68), (92, 62, 30)
    ta = {}
    lad = pygame.Surface((16, 16), pygame.SRCALPHA)
    for rx in (2, 12):
        pygame.draw.rect(lad, (140, 100, 52), (rx, 0, 2, 16))
        pygame.draw.rect(lad, dark, (rx, 0, 1, 16))
    for ry in (2, 6, 10, 14):
        pygame.draw.rect(lad, wood, (4, ry, 8, 2))
        pygame.draw.rect(lad, dark, (4, ry + 1, 8, 1))
    ta[LADDER] = lad

    def plate_surf(col, edge, h):
        sf = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.rect(sf, col, (1, 16 - h, 14, h))
        pygame.draw.rect(sf, edge, (1, 16 - h, 14, h), 1)
        return sf
    for pid, col_, edge_ in ((WOOD_PLATE, (176, 134, 76), (100, 70, 34)), (STONE_PLATE, (138, 138, 144), (78, 78, 84))):
        ta[pid] = plate_surf(col_, edge_, 4)
        TEX_PLATE_ON[pid] = pygame.transform.scale(plate_surf(col_, edge_, 2), (TILE, TILE)).convert_alpha()

    def torch_surf(on):
        sf = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.rect(sf, (112, 80, 42), (7, 6, 2, 9))
        pygame.draw.rect(sf, (80, 56, 28), (7, 6, 1, 9))
        pygame.draw.rect(sf, (255, 62, 42) if on else (96, 34, 30), (6, 2, 4, 5))
        if on:
            pygame.draw.rect(sf, (255, 190, 170), (7, 3, 2, 2))
        return sf
    ta[REDSTONE_TORCH] = torch_surf(True)
    td_ = pygame.Surface((16, 16), pygame.SRCALPHA)
    pygame.draw.rect(td_, (160, 118, 66), (0, 0, 16, 16))
    for ty_ in (5, 10):
        pygame.draw.line(td_, (120, 84, 42), (1, ty_), (14, ty_))
    pygame.draw.rect(td_, (96, 66, 32), (0, 0, 16, 16), 2)
    pygame.draw.rect(td_, (60, 60, 66), (1, 2, 3, 2))
    pygame.draw.rect(td_, (60, 60, 66), (1, 12, 3, 2))
    pygame.draw.rect(td_, (225, 225, 225), (11, 7, 2, 2))
    ta[TRAPDOOR] = td_
    to_ = pygame.Surface((16, 16), pygame.SRCALPHA)
    pygame.draw.rect(to_, (150, 108, 58), (0, 0, 4, 16))
    pygame.draw.rect(to_, (96, 66, 32), (0, 0, 4, 16), 1)
    pygame.draw.rect(to_, (60, 60, 66), (0, 2, 2, 2))
    pygame.draw.rect(to_, (60, 60, 66), (0, 12, 2, 2))
    ta[TRAPDOOR_OPEN] = to_
    def lever_surf(on, orient):                             # orient: floor, or the side its block is on
        sf = pygame.Surface((16, 16), pygame.SRCALPHA)
        base, edge, stick = (122, 122, 128), (70, 70, 76), (150, 108, 56)
        knob = (232, 70, 58) if on else (205, 160, 92)
        if orient == "floor":
            pygame.draw.rect(sf, base, (3, 12, 10, 4))
            pygame.draw.rect(sf, edge, (3, 12, 10, 4), 1)
            tip = (12, 3) if on else (4, 3)
            pygame.draw.line(sf, stick, (8, 13), tip, 2)
            pygame.draw.rect(sf, knob, (tip[0] - 1, tip[1] - 1, 3, 3))
        else:
            pygame.draw.rect(sf, base, (0, 3, 4, 10))
            pygame.draw.rect(sf, edge, (0, 3, 4, 10), 1)
            tip = (12, 3) if on else (12, 12)
            pygame.draw.line(sf, stick, (3, 8), tip, 2)
            pygame.draw.rect(sf, knob, (tip[0] - 1, tip[1] - 1, 3, 3))
            if orient == "right":
                sf = pygame.transform.flip(sf, True, False)
        return sf
    for on_ in (False, True):
        for or_ in ("floor", "left", "right"):
            TEX_LEVER[(on_, or_)] = pygame.transform.scale(lever_surf(on_, or_), (TILE, TILE)).convert_alpha()
    def button_surf(kind, on, orient):
        sf = pygame.Surface((16, 16), pygame.SRCALPHA)
        col, edge = ((138, 138, 144), (78, 78, 84)) if kind == 0 else ((176, 134, 76), (100, 70, 34))
        h = 2 if on else 3
        if orient == "floor":
            pygame.draw.rect(sf, col, (4, 16 - h, 8, h))
            pygame.draw.rect(sf, edge, (4, 16 - h, 8, h), 1)
        else:
            pygame.draw.rect(sf, col, (0, 5, h, 6))
            pygame.draw.rect(sf, edge, (0, 5, h, 6), 1)
            if orient == "right":
                sf = pygame.transform.flip(sf, True, False)
        return sf
    for kind_, bid_ in ((0, BUTTON_STONE), (1, BUTTON_WOOD)):
        for on_ in (False, True):
            for or_ in ("floor", "left", "right"):
                TEX_BUTTON[(kind_, on_, or_)] = pygame.transform.scale(button_surf(kind_, on_, or_), (TILE, TILE)).convert_alpha()
        ta[bid_] = button_surf(kind_, False, "floor")
        ta[BUTTON_ON[bid_]] = button_surf(kind_, True, "floor")
    for st_, cid_ in enumerate(CROPS):
        sf_ = pygame.Surface((16, 16), pygame.SRCALPHA)
        hh_ = (3, 6, 10, 13)[st_]
        ripe_ = st_ == 3
        stem_ = (212, 172, 60) if ripe_ else ((84, 168, 58) if st_ < 2 else (140, 188, 60))
        for xx_ in (2, 5, 8, 11, 14):
            top_ = 16 - hh_ + ((xx_ * 7) % 3)
            pygame.draw.line(sf_, stem_, (xx_, 15), (xx_, top_), 1)
            if ripe_:
                pygame.draw.rect(sf_, (240, 204, 84), (xx_ - 1, top_ - 1, 3, 3))
        ta[cid_] = sf_
    sp_ = pygame.Surface((16, 16), pygame.SRCALPHA)
    pygame.draw.rect(sp_, (112, 80, 42), (7, 9, 2, 7))
    for (qx_, qy_, qw_, qh_, qc_) in ((4, 4, 8, 5, (62, 140, 46)), (2, 6, 5, 4, (74, 158, 52)), (9, 6, 5, 4, (74, 158, 52)), (6, 2, 4, 3, (96, 184, 66))):
        pygame.draw.rect(sp_, qc_, (qx_, qy_, qw_, qh_))
    ta[SAPLING] = sp_
    ta[LEVER] = lever_surf(False, "floor")
    ta[LEVER_ON] = lever_surf(True, "floor")
    dust_ = pygame.Surface((16, 16), pygame.SRCALPHA)
    pygame.draw.rect(dust_, (150, 24, 24), (1, 11, 14, 3))
    pygame.draw.rect(dust_, (150, 24, 24), (6, 5, 3, 9))
    pygame.draw.rect(dust_, (236, 70, 60), (6, 11, 3, 1))
    pygame.draw.rect(dust_, (236, 70, 60), (3, 12, 1, 1))
    pygame.draw.rect(dust_, (236, 70, 60), (12, 12, 1, 1))
    ta[REDSTONE_DUST] = dust_
    def obs_surf(on):                                       # drawn facing right (face on the right), then rotated
        sf = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.rect(sf, (118, 118, 124), (0, 0, 16, 16))
        pygame.draw.rect(sf, (70, 70, 76), (0, 0, 16, 16), 1)
        pygame.draw.rect(sf, (92, 92, 98), (12, 1, 3, 14))
        for ey_ in (4, 10):
            pygame.draw.rect(sf, (30, 30, 34), (10, ey_, 4, 3))
            pygame.draw.rect(sf, (236, 236, 236), (11, ey_ + 1, 2, 1))
        pygame.draw.rect(sf, (255, 70, 56) if on else (96, 28, 26), (1, 6, 4, 4))
        pygame.draw.rect(sf, (60, 60, 66), (1, 6, 4, 4), 1)
        return sf
    ta[OBSERVER] = obs_surf(False)
    for di_ in range(4):
        ta[OBSERVER_BLK[di_]] = pygame.transform.rotate(obs_surf(False), PISTON_ANGLE[di_])
        TEX_OBS_ON[OBSERVER_BLK[di_]] = pygame.transform.scale(
            pygame.transform.rotate(obs_surf(True), PISTON_ANGLE[di_]), (TILE, TILE)).convert_alpha()
    TEX_TORCH_OFF = pygame.transform.scale(torch_surf(False), (TILE, TILE)).convert_alpha()

    def piston_surf(kind, sticky=False):                    # drawn facing right, then rotated
        sf = pygame.Surface((16, 16), pygame.SRCALPHA)
        wood_, wood_d = ((110, 196, 80), (58, 124, 40)) if sticky else ((176, 134, 76), (100, 70, 34))
        if kind == "head":
            pygame.draw.rect(sf, (120, 92, 50), (0, 6, 12, 4))
            pygame.draw.rect(sf, wood_, (12, 0, 4, 16))
            pygame.draw.rect(sf, wood_d, (12, 0, 4, 16), 1)
            return sf
        pygame.draw.rect(sf, (112, 112, 118), (0, 0, 12, 16))
        pygame.draw.rect(sf, (78, 78, 84), (0, 0, 12, 16), 1)
        for ry_ in (4, 11):
            pygame.draw.rect(sf, (150, 150, 156), (3, ry_, 6, 1))
        if kind == "ext":
            pygame.draw.rect(sf, (48, 40, 32), (12, 0, 4, 16))
        else:
            pygame.draw.rect(sf, wood_, (12, 0, 4, 16))
            pygame.draw.rect(sf, wood_d, (12, 0, 4, 16), 1)
        return sf
    ta[PISTON] = piston_surf("base")
    for di_ in range(4):
        ta[PISTON_BASE[di_]] = pygame.transform.rotate(piston_surf("base"), PISTON_ANGLE[di_])
        ta[PISTON_EXT[di_]] = pygame.transform.rotate(piston_surf("ext"), PISTON_ANGLE[di_])
        ta[PISTON_HEAD[di_]] = pygame.transform.rotate(piston_surf("head"), PISTON_ANGLE[di_])
        ta[STICKY_BASE[di_]] = pygame.transform.rotate(piston_surf("base", True), PISTON_ANGLE[di_])
        ta[STICKY_EXT[di_]] = pygame.transform.rotate(piston_surf("ext"), PISTON_ANGLE[di_])
        ta[STICKY_HEAD[di_]] = pygame.transform.rotate(piston_surf("head", True), PISTON_ANGLE[di_])
    ta[STICKY] = piston_surf("base", True)
    for bid, top in ((DOOR_CB, False), (DOOR_CT, True)):
        d_ = mk((160, 118, 66), 6, 40 + int(top))
        pygame.draw.rect(d_, dark, (0, 0, 16, 16), 1)
        pygame.draw.rect(d_, (130, 92, 48), (3, 2, 10, 5 if top else 12), 1)
        if top:
            pygame.draw.rect(d_, (170, 215, 235), (4, 3, 8, 3))
        else:
            pygame.draw.rect(d_, (130, 92, 48), (3, 9, 10, 5), 1)
            pygame.draw.rect(d_, (225, 225, 225), (11, 3, 2, 2))
        TEX[bid] = pygame.transform.scale(d_.convert(), (TILE, TILE))
    for bid, top in ((DOOR_OB, False), (DOOR_OT, True)):
        o_ = pygame.Surface((16, 16), pygame.SRCALPHA)
        pygame.draw.rect(o_, (150, 108, 58), (0, 0, 3, 16))
        pygame.draw.rect(o_, dark, (0, 0, 3, 16), 1)
        pygame.draw.rect(o_, (225, 225, 225), (1, 7, 1, 2))
        ta[bid] = o_
    for k, v in ta.items():
        TEX[k] = pygame.transform.scale(v, (TILE, TILE)).convert_alpha()
    ANIM[LAVA] = [pygame.transform.scale(lava_frame(i).convert(), (TILE, TILE)) for i in range(4)]
    def water_frame(i):
        sf = pygame.Surface((16, 16), pygame.SRCALPHA)
        for y in range(16):
            for x in range(16):
                v = (math.sin(a_ * (x + 4 * i)) + math.sin(a_ * 2 * y + a_ * 4 * i + x * a_)) / 4 + 0.5
                sf.set_at((x, y), (int(35 + 40 * v), int(95 + 60 * v), int(205 + 40 * v), int(150 + 30 * v)))
        return sf

    ANIM[WATER] = [pygame.transform.scale(water_frame(i), (TILE, TILE)).convert_alpha() for i in range(4)]
    ANIM[PORTAL] = [pygame.transform.scale(portal_frame(i), (TILE, TILE)).convert_alpha() for i in range(4)]
    ANIM[END_PORTAL] = [pygame.transform.scale(end_portal_frame(i), (TILE, TILE)).convert() for i in range(4)]
    BG_END = pygame.transform.scale(mk((14, 10, 28), 4, 33).convert(), (TILE, TILE))

    mats = {"Wooden": (150, 110, 60), "Stone": (135, 135, 135),
            "Iron": (225, 225, 225), "Diamond": (80, 230, 230), "Netherite": (70, 60, 66)}
    icons = {STICK: tool_icon("stick", None), COAL: tool_icon("coal", None),
             IRON_INGOT: tool_icon("ingot", None), DIAMOND: tool_icon("diamond", None),
             NETHERITE_SCRAP: tool_icon("scrap", None),
             NETHERITE_INGOT: tool_icon("ingot", (80, 68, 74)), FLINT_STEEL: tool_icon("lighter", None),
             XP_BOTTLE: tool_icon("potion", (120, 235, 60)), PROTECTION_POTION: tool_icon("potion", (70, 150, 255)), REGEN_POTION: tool_icon("potion", (255, 70, 110)),
             DOOR_ITEM: tool_icon("door", None),
             BUCKET: tool_icon("bucket", None), LAVA_BUCKET: tool_icon("bucket", (255, 140, 30)),
             WATER_BUCKET: tool_icon("bucket", (60, 120, 230)),
             RAW_BEEF: tool_icon("beef", None), STEAK: tool_icon("steak", None),
             ENDER_PEARL: tool_icon("pearl", None), EYE_OF_ENDER: tool_icon("eye", None), END_CRYSTAL: tool_icon("crystal", None),
             BOW: tool_icon("bow", None), ARROW: tool_icon("arrow", None),
             ELYTRA: tool_icon("elytra", None), FIREWORK: tool_icon("firework", None),
             PAPER: tool_icon("paper", None), LEATHER: tool_icon("leather", None), BOOK: tool_icon("book", None),
             STRING: tool_icon("string", None), FISHING_ROD: tool_icon("rod", None),
             RAW_COD: tool_icon("fish", (200, 170, 120)), COOKED_COD: tool_icon("fish", (150, 98, 52)),
             RAW_SALMON: tool_icon("fish", (225, 105, 85)), COOKED_SALMON: tool_icon("fish", (190, 120, 92))}
    sb_ = pygame.Surface((16, 16), pygame.SRCALPHA)
    pygame.draw.circle(sb_, (66, 146, 48), (8, 8), 6)
    pygame.draw.circle(sb_, (118, 208, 88), (8, 8), 5)
    pygame.draw.rect(sb_, (180, 238, 150), (6, 5, 2, 2))
    icons[SLIME_BALL] = sb_
    sd_ = pygame.Surface((16, 16), pygame.SRCALPHA)
    for (qx_, qy_) in ((4, 5), (9, 4), (6, 9), (11, 9), (8, 12), (3, 12)):
        pygame.draw.rect(sd_, (86, 140, 54), (qx_, qy_, 2, 2))
        pygame.draw.rect(sd_, (150, 196, 96), (qx_, qy_, 1, 1))
    icons[SEEDS] = sd_
    wh_ = pygame.Surface((16, 16), pygame.SRCALPHA)
    for xx_ in (4, 7, 10):
        pygame.draw.line(wh_, (206, 168, 62), (xx_, 14), (xx_ + 1, 4), 2)
        pygame.draw.rect(wh_, (240, 204, 84), (xx_ - 1, 2, 4, 5))
    pygame.draw.line(wh_, (120, 90, 40), (3, 12), (12, 12), 2)
    icons[WHEAT] = wh_
    br_ = pygame.Surface((16, 16), pygame.SRCALPHA)
    pygame.draw.ellipse(br_, (150, 96, 44), (1, 5, 14, 8))
    pygame.draw.ellipse(br_, (204, 146, 76), (2, 5, 12, 6))
    for xx_ in (5, 8, 11):
        pygame.draw.line(br_, (150, 96, 44), (xx_, 6), (xx_ - 1, 9), 1)
    icons[BREAD] = br_
    for (n, k), tid in TOOLS.items():
        icons[tid] = tool_icon(k, mats[n])
    for (n, sl), tid in ARMORS.items():
        icons[tid] = tool_icon(sl, mats[n])
    for k, v in icons.items():
        ICON[k] = pygame.transform.scale(v, (TILE, TILE))
    for k in TEX:
        ICON[k] = TEX[k]
    for k, v in ICON.items():
        ICON_S[k] = pygame.transform.scale(v, (18, 18))

    r = random.Random(7)
    surf = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
    for _ in range(10):
        x, y = r.randint(4, TILE - 4), r.randint(4, TILE - 4)
        for _ in range(2):
            x2 = max(0, min(TILE, x + r.randint(-9, 9)))
            y2 = max(0, min(TILE, y + r.randint(-9, 9)))
            pygame.draw.line(surf, (20, 20, 20, 220), (x, y), (x2, y2), 2)
            x, y = x2, y2
        CRACKS.append(surf.copy())


def make_heart(cols_filled):
    pat = [".XX.XX.", "XXXXXXX", "XXXXXXX", ".XXXXX.", "..XXX..", "...X..."]
    s = pygame.Surface((21, 18), pygame.SRCALPHA)
    for y, row in enumerate(pat):
        for x, ch in enumerate(row):
            if ch == "X":
                col = (225, 35, 35) if x < cols_filled else (70, 25, 25)
                if x < cols_filled and y == 1 and x in (1, 2):
                    col = (255, 150, 150)
                pygame.draw.rect(s, col, (x * 3, y * 3, 3, 3))
    return s


# --------------------------------------------------------------------------- #
# World
# --------------------------------------------------------------------------- #
class World:
    def __init__(self, seed=None, dim=0):
        self.seed = seed if seed is not None else random.randrange(1 << 30)
        self.dim = dim
        self.cols = [bytearray(WH) for _ in range(WW)]
        self.height = [0] * WW
        if dim == 0:
            self.generate()
        elif dim == 1:
            self.generate_nether()
        else:
            self.generate_end()

    def get(self, x, y):
        if x < 0 or x >= WW or y >= WH:
            return BEDROCK
        if y < 0:
            return AIR
        return self.cols[x][y]

    def set(self, x, y, v):
        if 0 <= x < WW and 0 <= y < WH:
            self.cols[x][y] = v

    def surface_y(self, x):
        col = self.cols[max(0, min(WW - 1, x))]
        for y in range(WH):
            if col[y]:
                return y
        return WH

    def vein(self, r, bid, x, y, size, base=STONE):
        for _ in range(size):
            if self.get(x, y) == base:
                self.set(x, y, bid)
            x += r.randint(-1, 1)
            y += r.randint(-1, 1)

    def carve(self, cx, cy, rad, deep_only=True):
        ri = int(math.ceil(rad))
        for dx in range(-ri, ri + 1):
            for dy in range(-ri, ri + 1):
                if dx * dx + dy * dy <= rad * rad:
                    x, y = int(cx) + dx, int(cy) + dy
                    if 1 <= x < WW - 1 and y < WH - 3 and self.get(x, y) not in (AIR, BEDROCK):
                        if not deep_only or y > self.height[x] + 6:
                            self.set(x, y, AIR)

    def generate(self):
        r = random.Random(self.seed)
        p = [r.random() * 6.28 for _ in range(4)]
        for x in range(WW):
            h = SURF + 7 * math.sin(x * 0.022 + p[0]) + 4 * math.sin(x * 0.07 + p[1]) \
                + 2 * math.sin(x * 0.17 + p[2])
            self.height[x] = int(h)
        for x in range(WW):
            h, col = self.height[x], self.cols[x]
            dirt = 3 + r.randint(0, 2)
            for y in range(h, WH):
                col[y] = GRASS if y == h else (DIRT if y < h + dirt else STONE)
            col[WH - 1] = BEDROCK
            if r.random() < 0.6:
                col[WH - 2] = BEDROCK
            if r.random() < 0.25:
                col[WH - 3] = BEDROCK
        for _ in range(WW * WH // 130):
            self.vein(r, COAL_ORE, r.randint(0, WW - 1), r.randint(SURF + 5, WH - 4), r.randint(6, 12))
        for _ in range(WW * WH // 300):
            self.vein(r, IRON_ORE, r.randint(0, WW - 1), r.randint(SURF + 14, WH - 4), r.randint(4, 8))
        for _ in range(WW // 4):                     # diamonds: more and bigger veins, starting a bit higher up
            self.vein(r, DIAMOND_ORE, r.randint(0, WW - 1), r.randint(WH - 45, WH - 5), r.randint(3, 6))
        # caves
        for _ in range(WW // 5):
            x, y = r.randint(5, WW - 5), r.randint(SURF + 12, WH - 8)
            ang = r.random() * 6.28
            for _ in range(r.randint(60, 200)):
                ang += r.uniform(-0.5, 0.5)
                x += math.cos(ang) * 1.2
                y += math.sin(ang) * 0.8
                self.carve(x, y, r.uniform(1.0, 2.2))
        # cave entrances from the surface
        for _ in range(WW // 40):
            x = r.randint(10, WW - 10)
            y = float(self.height[int(x)])
            ang = math.pi / 2 + r.uniform(-0.5, 0.5)
            for _ in range(r.randint(25, 50)):
                ang += r.uniform(-0.35, 0.35)
                ang = max(0.4, min(math.pi - 0.4, ang))
                x += math.cos(ang) * 1.1
                y += math.sin(ang) * 1.1
                self.carve(x, y, 1.3, deep_only=False)
        # lava lakes at the bottom of caves, obsidian veins near them
        for x in range(WW):
            for y in range(WH - 14, WH - 3):
                if self.cols[x][y] == AIR:
                    self.cols[x][y] = LAVA
        for _ in range(WW // 9):
            self.vein(r, OBSIDIAN, r.randint(0, WW - 1), r.randint(WH - 30, WH - 5), r.randint(3, 6))
        # water pools: shallow ponds in the grass
        ponds = []
        for _ in range(WW // 22):
            cx, hw = r.randint(8, WW - 9), r.randint(3, 6)
            if abs(cx - WW // 2) < 12 or any(abs(cx - c) < hw + h2 + 4 for c, h2 in ponds):
                continue
            span = range(cx - hw, cx + hw + 1)
            wl = max(self.height[cx - hw - 1], self.height[cx + hw + 1])
            if abs(self.height[cx - hw - 1] - self.height[cx + hw + 1]) > 3 \
                    or wl - min(self.height[x] for x in span) > 3 \
                    or max(self.height[x] for x in span) - wl > 4:
                continue
            ponds.append((cx, hw))
            dmax = r.randint(2, 4)
            for x in span:
                g = self.height[x]
                depth = max(1, round(dmax * math.sqrt(max(0.0, 1 - ((x - cx) / (hw + 0.5)) ** 2))))
                for y in range(min(g, wl) - 8, wl):
                    self.cols[x][y] = AIR
                bottom = max(g, wl) + depth
                for y in range(wl, bottom):
                    self.cols[x][y] = WATER
                if self.cols[x][bottom] == AIR:
                    self.cols[x][bottom] = DIRT
            for bx in (cx - hw - 1, cx + hw + 1):          # seal the banks (cave mouths etc.)
                for y in range(wl, wl + dmax + 1):
                    if self.cols[bx][y] == AIR:
                        self.cols[bx][y] = DIRT
        # trees
        x = 3
        while True:
            x += r.randint(4, 9)
            if x >= WW - 4:
                break
            if abs(x - WW // 2) < 3:
                continue
            h = self.height[x]
            if self.get(x, h) != GRASS:
                continue
            tall = r.randint(4, 6)
            top = h - tall
            for i in range(1, tall + 1):
                self.set(x, h - i, LOG)
            for dy, hw in ((-2, 1), (-1, 2), (0, 2), (1, 2)):
                for dx in range(-hw, hw + 1):
                    if self.get(x + dx, top + dy) == AIR:
                        self.set(x + dx, top + dy, LEAVES)

    def generate_nether(self):
        """Pure netherrack: a dark cavern, a thick solid floor, ancient debris deep down."""
        r = random.Random(self.seed + 1)
        p = [r.random() * 6.28 for _ in range(5)]
        ceil = []
        for x in range(WW):
            c = int(15 + 5 * math.sin(x * 0.031 + p[0]) + 3 * math.sin(x * 0.09 + p[1]) + r.randint(0, 1))
            f = int(46 + 6 * math.sin(x * 0.027 + p[2]) + 3 * math.sin(x * 0.083 + p[3])
                    + 2 * math.sin(x * 0.19 + p[4]))
            ceil.append(c)
            self.height[x] = f                       # floor row (top of the netherrack)
            col = self.cols[x]
            for y in range(WH):
                col[y] = NETHERRACK if (y <= c or y >= f) else AIR
            for y in range(3 + (1 if r.random() < 0.5 else 0)):
                col[y] = BEDROCK
            col[WH - 1] = BEDROCK
            if r.random() < 0.6:
                col[WH - 2] = BEDROCK
            if r.random() < 0.3:
                col[WH - 3] = BEDROCK
        # tunnels under the floor
        for _ in range(WW // 8):
            x, y = r.randint(5, WW - 5), r.randint(60, WH - 8)
            ang = r.random() * 6.28
            for _ in range(r.randint(40, 120)):
                ang += r.uniform(-0.5, 0.5)
                x += math.cos(ang) * 1.2
                y += math.sin(ang) * 0.8
                self.carve(x, y, r.uniform(1.0, 2.0), deep_only=False)
        # floating netherrack islands
        for _ in range(WW // 9):
            cx, cy = r.randint(6, WW - 6), r.randint(24, 34)
            rw, rh = r.randint(3, 8), r.randint(1, 3)
            for dx in range(-rw, rw + 1):
                for dy in range(-rh, rh + 1):
                    if (dx / rw) ** 2 + (dy / rh) ** 2 <= 1 and self.get(cx + dx, cy + dy) == AIR:
                        self.set(cx + dx, cy + dy, NETHERRACK)
        # stalactites and stalagmites
        for x in range(3, WW - 3):
            if r.random() < 0.18:
                for i in range(1, r.randint(2, 8)):
                    if self.get(x, ceil[x] + i) == AIR:
                        self.set(x, ceil[x] + i, NETHERRACK)
            if r.random() < 0.12:
                for i in range(1, r.randint(2, 7)):
                    self.set(x, self.height[x] - i, NETHERRACK)
        # lava lakes: flat-topped basins sunk into the floor
        used, lava_cells = [], []
        for _ in range(WW // 22):
            half = r.randint(5, 11)
            cx = r.randint(half + 6, WW - half - 6)
            a, b = cx - half, cx + half
            if any(a - 4 < ub and b + 4 > ua for ua, ub in used):
                continue
            used.append((a, b))
            L = max(self.height[x] for x in range(a - 2, b + 3))       # surface: the lowest floor row in the span
            dmax = r.randint(2, 4)
            orig = {}
            for x in range(a, b + 1):
                dep = int(round(dmax * math.sqrt(max(0.0, 1 - ((x - cx) / half) ** 2)) + r.uniform(-0.3, 0.3)))
                if dep < 1:
                    continue
                orig[x] = self.height[x]
                y = orig[x] - 1
                while y > 0 and self.get(x, y) == NETHERRACK:        # stalagmites above the lake
                    self.set(x, y, AIR)
                    y -= 1
                for y in range(orig[x], L):
                    self.set(x, y, AIR)
                for y in range(L, L + dep):
                    self.set(x, y, LAVA)
                self.height[x] = L
                lava_cells += [(x, y) for y in range(L, L + dep)]
        for x, y in lava_cells:                      # seal the basins: tunnels or caves must never drain a lake
            for dx, dy in ((-1, 0), (1, 0), (0, 1)):
                if self.get(x + dx, y + dy) == AIR:
                    self.set(x + dx, y + dy, NETHERRACK)
        # rare ancient debris, 1-3 blocks per vein, deeper is a little more common
        for _ in range(WW * WH // 600):
            y = r.randint(58, WH - 5)
            if r.random() < 0.5:
                y = r.randint(WH - 30, WH - 5)
            self.vein(r, ANCIENT_DEBRIS, r.randint(0, WW - 1), y, r.randint(1, 3), base=NETHERRACK)

    def generate_end(self):
        """A flat floating island of end stone in the void, two obsidian pillars, an obsidian landing pad."""
        for x in range(WW):
            self.height[x] = END_SURF
        for x in range(END_CX - END_HALF, END_CX + END_HALF + 1):
            t = (x - END_CX) / END_HALF
            depth = int(round(7 * math.sqrt(max(0.0, 1 - t * t))))
            for y in range(END_SURF, END_SURF + depth + 1):
                self.cols[x][y] = END_STONE
        for px, h in END_PILLARS:
            for dx in (-1, 0, 1):
                for y in range(END_SURF - h, END_SURF):
                    self.cols[px + dx][y] = OBSIDIAN
        for x in range(END_SPAWN_X - 2, END_SPAWN_X + 3):
            self.cols[x][END_SURF] = OBSIDIAN


# --------------------------------------------------------------------------- #
# Entities
# --------------------------------------------------------------------------- #
class Entity:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.vx = self.vy = 0.0
        self.on_ground = False
        self.air_peak = None


def mob_fall(g, e):
    """Fall damage for mobs, same rule as the player: 3 free blocks, then 1 HP per block."""
    w = g.world
    if touching(w, e, WATER) or touching(w, e, LAVA) or touching(w, e, LADDER):
        e.air_peak = None
    elif e.on_ground:
        if e.air_peak is not None:
            d = e.y - e.air_peak - 3
            if d >= 1 and w.get(math.floor(e.x + e.w / 2), math.floor(e.y + e.h + 0.05)) != SLIME_BLOCK:
                e.hp -= int(d)
                e.flash = 0.25
        e.air_peak = None
    else:
        e.air_peak = e.y if e.air_peak is None else min(e.air_peak, e.y)


def collide(world, e, axis):
    hit = False
    x0, x1 = math.floor(e.x), math.floor(e.x + e.w - 1e-4)
    y0, y1 = math.floor(e.y), math.floor(e.y + e.h - 1e-4)
    for tx in range(x0, x1 + 1):
        for ty in range(y0, y1 + 1):
            if SOLID[world.get(tx, ty)]:
                if axis == 0:
                    if e.vx > 0:
                        e.x = tx - e.w - 1e-4
                    elif e.vx < 0:
                        e.x = tx + 1 + 1e-4
                    e.vx = 0.0
                else:
                    if e.vy > 0:
                        e.y = ty - e.h - 1e-4
                        e.on_ground = True
                    elif e.vy < 0:
                        e.y = ty + 1 + 1e-4
                    e.vy = 0.0
                hit = True
    return hit


def physics(world, e, dt):
    e.x += e.vx * dt
    e.x = max(0.0, min(WW - e.w, e.x))
    collide(world, e, 0)
    e.on_ground = False
    e.y += e.vy * dt
    collide(world, e, 1)


def overlap(a, b, pad=0.0):
    return (a.x < b.x + b.w + pad and a.x + a.w > b.x - pad and
            a.y < b.y + b.h + pad and a.y + a.h > b.y - pad)


def touching(world, e, bid):
    for tx in range(math.floor(e.x), math.floor(e.x + e.w - 1e-4) + 1):
        for ty in range(math.floor(e.y), math.floor(e.y + e.h - 1e-4) + 1):
            if world.get(tx, ty) == bid:
                return True
    return False


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 0.6, 1.8)
        self.hp = 20
        self.face = 1
        self.walk = 0.0
        self.invuln = 0.0
        self.air_peak = None
        self.regen = 0.0
        self.swing = 0.0
        self.air, self.drown_t = 10.0, 0.0
        self.flying = False
        self.gliding, self.glide_v, self.glide_pitch, self.boost_t = False, 0.0, -0.2, 0.0
        self._gin = (0.0, 0.0)

    def step(self, g, mv, sprint, jump, dt, down=False):
        speed = 5.6 if sprint else 4.3
        acc = 16 if self.on_ground else 7
        self.vx += (mv * speed - self.vx) * min(1.0, acc * dt)
        if mv:
            self.face = 1 if mv > 0 else -1
        if self.gliding and (self.flying or not g.has_elytra() or touching(g.world, self, LAVA)
                             or touching(g.world, self, WATER) or touching(g.world, self, LADDER)):
            self.gliding = False
        if self.flying:
            self.vx += (mv * speed * 1.8 - self.vx) * min(1.0, 8 * dt)
            self.vy = -9.0 if jump else (9.0 if down else 0.0)
            self.air_peak = None
            if self.on_ground and down:
                self.flying = False
        elif self.gliding:                                   # elytra: W/Up pitch up (slows), S/Down dives (speeds up)
            if jump:
                self.glide_pitch = min(0.9, self.glide_pitch + 1.3 * dt)
            elif down:
                self.glide_pitch = max(-1.2, self.glide_pitch - 1.3 * dt)
            else:
                self.glide_pitch += (-0.17 - self.glide_pitch) * min(1.0, 0.9 * dt)
            th = self.glide_pitch
            v = self.glide_v + (14.0 * -math.sin(th) - 0.12 * self.glide_v) * dt
            if self.boost_t > 0:                             # firework rocket thrust
                self.boost_t -= dt
                v += 24.0 * dt
            self.glide_v = max(1.0, min(34.0, v))
            self.vx = self.face * self.glide_v * math.cos(th)
            self.vy = -self.glide_v * math.sin(th) + max(0.0, 8.0 - self.glide_v)
            self._gin = (self.vx, self.vy)
            self.air_peak = None
        elif touching(g.world, self, LAVA):
            self.vx *= max(0.0, 1 - 5 * dt)
            self.vy = -8.0 if jump else min(self.vy + GRAVITY * 0.2 * dt, 2.5)
            self.air_peak = None
            g.hurt(3)
        elif touching(g.world, self, LADDER):
            self.vy = -3.4 if jump else (3.4 if down else 0.0)
            self.air_peak = None
        elif touching(g.world, self, WATER):
            self.vx *= max(0.0, 1 - 6 * dt)
            self.vy = -7.5 if jump else (4.0 if down else min(self.vy + GRAVITY * 0.12 * dt, 1.8))
            self.air_peak = None
        else:
            if jump and self.on_ground:
                self.vy = -9.2
            self.vy = min(self.vy + GRAVITY * dt, 25.0)
        physics(g.world, self, dt)
        if self.gliding:
            self.air_peak = None
            ivx, ivy = self._gin
            wall = ivx != 0 and self.vx == 0.0
            ceil_ = ivy < 0 and self.vy == 0.0
            if self.on_ground or wall or ceil_:               # landing / crash
                v = self.glide_v
                self.gliding = False
                dmg = (ivy - 12) * 0.6 if (self.on_ground and ivy > 12) else ((v - 10) * 0.8 if (wall or ceil_) and v > 10 else 0)
                if dmg >= 1:
                    g.hurt(int(dmg), force=True, armor=False)
        self.walk += abs(self.vx) * dt * 2.0
        if self.on_ground:
            if self.air_peak is not None:
                d = self.y - self.air_peak - 3
                if g.world.get(math.floor(self.x + self.w / 2), math.floor(self.y + self.h + 0.05)) == SLIME_BLOCK:
                    fall = self.y - self.air_peak              # slime: no damage, you bounce back up
                    v = math.sqrt(2 * GRAVITY * max(0.0, fall)) * 0.8
                    if v >= 4.0:
                        self.vy = -min(v, 17.0)
                        self.on_ground = False
                elif d >= 1:
                    g.hurt(int(d), force=True, armor=False)
                self.air_peak = None
        else:
            self.air_peak = self.y if self.air_peak is None else min(self.air_peak, self.y)
        if g.world.get(math.floor(self.x + self.w / 2), math.floor(self.y + 0.25)) == WATER:
            self.air = max(0.0, self.air - dt)
            if self.air <= 0:
                self.drown_t += dt
                if self.drown_t >= 1.0:
                    self.drown_t = 0.0
                    g.hurt(2, force=True, armor=False)
        else:
            self.air, self.drown_t = min(10.0, self.air + 4 * dt), 0.0


class Zombie(Entity):
    def __init__(self, x, y, kind="zombie"):
        super().__init__(x, y, 0.6, 1.8)
        self.kind = kind
        self.angry = kind == "zombie"
        self.wander, self.wdir = 0.0, 0
        self.hp = 20.0
        self.cd = 0.0
        self.flash = 0.0
        self.face = 1

    def update(self, g, dt):
        p = g.p
        dx = (p.x + p.w / 2) - (self.x + self.w / 2)
        target = 0.0
        if self.angry:
            if 0.35 < abs(dx) < 30:
                target = math.copysign(3.0 if self.kind == "pigman" else 2.0, dx)
            self.face = 1 if dx > 0 else -1
        else:
            self.wander -= dt
            if self.wander <= 0:
                self.wdir, self.wander = random.choice((-1, 0, 1)), random.uniform(1.5, 4.0)
            target = self.wdir * 1.0
            if self.wdir:
                self.face = self.wdir
        self.vx += (target - self.vx) * min(1.0, dt * 8)
        self.vy = min(self.vy + GRAVITY * dt, 25.0)
        physics(g.world, self, dt)
        mob_fall(g, self)
        if self.on_ground and target and abs(self.vx) < 0.01:
            self.vy = -9.0                       # blocked: hop over
        self.cd = max(0.0, self.cd - dt)
        self.flash = max(0.0, self.flash - dt)
        if self.angry and self.cd <= 0 and overlap(self, p, 0.15):
            px0 = p.x
            g.hurt(5 if self.kind == "pigman" else 3)
            self.cd = 1.0
            if p.x == px0:                       # (if that hit killed us we were already moved to spawn)
                p.vx = 6.0 if dx < 0 else -6.0
                p.vy = -5.0
        if self.kind == "zombie" and g.dim == 0 and g.light > 0.6 \
                and g.world.surface_y(int(self.x + self.w / 2)) >= self.y:
            self.hp -= 4 * dt                    # burns in sunlight
        if touching(g.world, self, LAVA):
            self.hp -= 10 * dt


class Cow(Entity):
    kind = "cow"

    def __init__(self, x, y):
        super().__init__(x, y, 1.3, 1.0)
        self.hp = 10.0
        self.wander, self.wdir = random.uniform(0, 3), 0
        self.flash = 0.0
        self.face = random.choice((-1, 1))
        self.panic = 0.0
        self.hurt_t = 0.0

    def update(self, g, dt):
        p = g.p
        self.panic = max(0.0, self.panic - dt)
        if self.panic > 0:                                   # run away from whoever hit us
            dx = (self.x + self.w / 2) - (p.x + p.w / 2)
            target = math.copysign(3.6, dx)
            self.face = 1 if dx > 0 else -1
        else:
            self.wander -= dt
            if self.wander <= 0:
                self.wdir, self.wander = random.choice((-1, 0, 0, 1)), random.uniform(1.5, 5.0)
            target = self.wdir * 0.9
            if self.wdir:
                self.face = self.wdir
        self.vx += (target - self.vx) * min(1.0, dt * 8)
        self.vy = min(self.vy + GRAVITY * dt, 25.0)
        physics(g.world, self, dt)
        mob_fall(g, self)
        if self.on_ground and target and abs(self.vx) < 0.01:
            self.vy = -8.6                                   # blocked: hop over
        self.flash = max(0.0, self.flash - dt)
        if touching(g.world, self, LAVA):
            self.hp -= 10 * dt


class Drop(Entity):
    def __init__(self, x, y, item, n, dur, vx=0.0, vy=-4.0, delay=0.0):
        super().__init__(x, y, 0.28, 0.28)
        self.item, self.n, self.dur = item, n, dur
        self.vx, self.vy = vx, vy
        self.age = -delay


def new_furnace():
    return dict(s=[None, None, None], burn=0.0, burnmax=1.0, prog=0.0)


class Crystal(Entity):
    kind = "crystal"

    def __init__(self, x, y):
        super().__init__(x, y, 0.8, 0.8)
        self.hp = 1.0
        self.flash = 0.0
        self.placed = False                     # True for crystals the player put down


class Dragon(Entity):
    """A minimalist Ender Dragon: circles high above the island, periodically dives at you."""
    kind = "dragon"
    MAXHP = 100.0

    def __init__(self, x, y):
        super().__init__(x, y, 4.5, 1.8)
        self.hp = self.MAXHP
        self.flash = 0.0
        self.face = 1
        self.state, self.state_t, self.ang = "circle", 0.0, 0.0
        self.target = (x, y)
        self.cd = 0.0

    def steer(self, tx, ty, speed, dt):
        cx_, cy_ = self.x + self.w / 2, self.y + self.h / 2
        dx, dy = tx - cx_, ty - cy_
        d = math.hypot(dx, dy)
        if d > 0.01:
            step = min(d, speed * dt)
            self.x += dx / d * step
            self.y += dy / d * step
        if abs(dx) > 0.6:
            self.face = 1 if dx > 0 else -1
        return d

    def update(self, g, dt):
        p = g.p
        self.flash = max(0.0, self.flash - dt)
        self.cd = max(0.0, self.cd - dt)
        self.state_t += dt
        if g.crystals:                                   # end crystals keep healing it
            self.hp = min(self.MAXHP, self.hp + 1.5 * len(g.crystals) * dt)
        if self.state == "circle":
            self.ang += dt * 0.45
            self.steer(END_CX + math.cos(self.ang) * 48, 36 + math.sin(self.ang * 2) * 5, 11.0, dt)
            if self.state_t > 7.0 and not p.flying:
                self.state, self.state_t = "dive", 0.0
        else:
            if self.state_t < 1.2:                       # keeps aiming for the first moments of the dive
                self.target = (p.x + p.w / 2, p.y + p.h / 2)
            d = self.steer(self.target[0], self.target[1], 16.0, dt)
            if d < 1.5 or self.state_t > 2.6:
                self.state, self.state_t = "circle", 0.0
        if self.cd <= 0 and overlap(self, p, 0.0):
            px0 = p.x
            g.hurt(5)
            self.cd = 1.2
            if p.x == px0:                               # (die() would already have moved us)
                p.vx = 8.0 * self.face
                p.vy = -6.0


class Arrow:
    bonus = 0

    def __init__(self, x, y, vx, vy, power):
        self.x, self.y, self.vx, self.vy, self.power = x, y, vx, vy, power
        self.age, self.stuck = 0.0, False


def book_pages(st):
    """The (sanitised) page list of a Book stack; a bad or oversized value is repaired, never trusted."""
    d = st[2] if isinstance(st[2], dict) else None
    pages = d.get("pages") if d else None
    if not isinstance(pages, list) or not pages:
        pages = [""]
    pages = [p[:BOOK_PAGE_CHARS] if isinstance(p, str) else "" for p in pages[:BOOK_MAX_PAGES]]
    st[2] = {"pages": pages}
    return pages


def wrap_text(font, text, width):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split(" "):
            trial = word if not cur else cur + " " + word
            if font.size(trial)[0] <= width:
                cur = trial
                continue
            if cur:
                lines.append(cur)
            cur = ""
            while font.size(word)[0] > width:               # a single word wider than the box
                k = 1
                while k < len(word) and font.size(word[:k + 1])[0] <= width:
                    k += 1
                lines.append(word[:k])
                word = word[k:]
            cur = word
        lines.append(cur)
    return lines


class Pearl:
    PEARL_PICKUP_DELAY = 0.6                     # a floating pearl can be collected after this long
    PEARL_FLOAT_MAX = 1e12                       # a floating pearl stays (stasis) until picked up or released

    def __init__(self, x, y, vx, vy):
        self.x, self.y, self.vx, self.vy, self.age = x, y, vx, vy, 0.0
        self.float_t, self.surf = None, 0.0      # float_t is None until the pearl touches water


class PrimedTnt(Entity):
    def __init__(self, x, y, fuse=4.0):
        super().__init__(x + 0.01, y + 0.01, 0.98, 0.98)
        self.fuse = fuse


UNBLASTABLE = (BEDROCK, OBSIDIAN, ENDER_CHEST, ANCIENT_DEBRIS, NETHERITE_BLOCK, WATER, LAVA, PORTAL,
               END_PORTAL, DRAGON_EGG)
NO_ITEM = (PORTAL, END_PORTAL, WATER, LAVA)       # world-only blocks: they never turn into items


def update_furnace(f, dt):
    src, fuel, out = f["s"]
    rec = SMELT.get(src[0]) if src else None
    can = rec is not None and (out is None or (out[0] == rec and out[1] < 64))
    if f["burn"] <= 0 and can and fuel and fuel[0] in FUEL:
        f["burn"] = f["burnmax"] = FUEL[fuel[0]]
        if fuel[0] == LAVA_BUCKET:
            f["s"][1] = new_stack(BUCKET)          # the bucket comes back empty
        else:
            fuel[1] -= 1
            if fuel[1] <= 0:
                f["s"][1] = None
    if f["burn"] > 0:
        f["burn"] = max(0.0, f["burn"] - dt)
        if can:
            f["prog"] += dt
            if f["prog"] >= SMELT_TIME:
                f["prog"] = 0.0
                src[1] -= 1
                if src[1] <= 0:
                    f["s"][0] = None
                if f["s"][2] is None:
                    f["s"][2] = new_stack(rec, 1)
                else:
                    f["s"][2][1] += 1
        else:
            f["prog"] = max(0.0, f["prog"] - dt * 2)
    else:
        f["prog"] = max(0.0, f["prog"] - dt * 2)


# --------------------------------------------------------------------------- #
# Game
# --------------------------------------------------------------------------- #
def lerpc(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


class Game:
    SLOT = 44

    def __init__(self, new=False, menu=False):
        self.use_menu, self.menu, self.save_path, self.world_name = menu, None, None, "World"
        self.cmd, self.chat, self.cmd_hist, self.tab_state = None, [], [], None
        pygame.init()
        pygame.display.set_caption("PotatoCraft")
        self.fullscreen = False
        self.screen = pygame.display.set_mode((SW, SH), pygame.SCALED)     # SCALED: the 1100x680 picture stretches to any screen
        self.clock = pygame.time.Clock()
        build_assets()
        self.font = pygame.font.Font(None, 22)
        self.small = pygame.font.Font(None, 18)
        self.big = pygame.font.Font(None, 44)
        self.hearts = {k: pygame.transform.smoothscale(make_heart(c), (17, 15))      # a bit smaller so they clear the hunger bar
                       for k, c in ((2, 7), (1, 4), (0, 0))}
        rr = random.Random(1)
        self.stars = [(rr.randint(0, SW), rr.randint(0, SH // 2)) for _ in range(70)]
        self.clouds = [[rr.randint(0, SW), rr.randint(30, 180), rr.randint(80, 190)] for _ in range(6)]
        self.new_game()
        if not new and not menu and os.path.exists(SAVE):
            self.load()

    # ----- state ----------------------------------------------------------- #
    def new_game(self, seed=None):
        self.world = World(seed)
        self.worlds, self.dim, self.dstate = {0: self.world}, 0, {}
        sx = WW // 2
        self.p = Player(sx + 0.2, self.world.height[sx] - 2.0)
        self.spawn = (self.p.x, self.p.y)
        self.inv = [None] * 36
        self.sel = 0
        self.cursor = None
        self.craft = [None] * 9
        self.ui = None
        self.cur_furnace = None
        self.cur_chest = None
        self.chest_name = "Chest"
        self.clear_t = 0.0
        self.waypoints = []
        self.ender = [None] * 27                 # shared by every Ender Chest, in every dimension
        self.protect_t = 0.0
        self.furnaces, self.chests = {}, {}
        self.drops, self.zombies = [], []
        self.tnts, self.booms = [], []
        self.armor = [None] * 4                  # helmet, chestplate, leggings, boots
        self.food, self.starve_t, self.cow_t = 20.0, 0.0, 3.5
        self.cows = []
        self.crystals, self.bosses = [], []
        self.end_state = dict(dragon_dead=False)
        self.revive_t = None
        self.pearls, self.pearl_cd = [], 0.0
        self.arrows, self.bow_t, self.bow_on = [], 0.0, False
        self.bk_stack, self.bk_page = None, 0
        self.rockets, self.sparks, self.fw_cd, self.glide_wear = [], [], 0.0, 0.0
        self.book_open, self.book_page, self.icon22 = True, 0, {}
        self.portal_t, self.portal_lock = 0.0, False
        self.creative, self.last_space = False, -1000
        self.xp, self.ench_slot, self.grind_slot = 0, [None], [None]
        self.bobber, self.active_plates = None, set()
        self.ext_pistons, self.plate_doors = {}, set()
        self.torch_list, self.torch_on, self.torch_scan_t = [], set(), 0.0
        self.plate_traps = set()
        self.dust_lvs, self.dust_live, self.dust_cache, self.dust_t = {}, {}, {}, {}
        self.lever_lists, self.buttons_on = {}, {}
        self.farm_t = 0.0
        self.leaf_hot = []                      # [x, y, seconds left]: where a log was just removed
        self.piston_cells = set()
        self.pal_scroll, self.pal_drag = 0, False
        self.observers, self.obs_pulse = {}, {}
        self.remote, self.pending_pearl, self.scan_center = False, None, None
        self.remote_hot = {}                    # dim -> [x, y, seconds left]: keep its machines running after a remote change
        self.lights, self.glow_cache = [], {}
        self.time = 0.15 * DAY_LEN
        self.mining, self.mine_prog = None, 0.0
        self.no_mine = False
        self.attack_cd = 0.0
        self.spawn_t = 0.0
        self.paused = False
        self.cmd, self.tick_frozen, self.tick_steps, self.tick_done = None, False, 0, 0
        self.debug = False
        self.light = 1.0
        self.rnd = random.Random()
        self.msg, self.msg_t = "", 0.0
        self.name_t = 0.0
        self.autosave_t = 0.0
        self.place_loot_chests()
        self.say("Punch trees (hold left click) to get logs. Press E for crafting.", 6)

    LOOT_CHESTS = 6

    def place_loot_chests(self):
        """6 hidden loot rooms deep underground, the same for a given world seed.
        Each has a chest with iron, diamonds and often pearls / potions; at most ONE netherite
        ingot exists in all six (and only about half of all worlds have it)."""
        w = self.world
        rng = random.Random(w.seed * 7919 + 13)
        seg = WW // self.LOOT_CHESTS
        netherite_in = rng.randrange(self.LOOT_CHESTS) if rng.random() < 0.5 else -1
        self.loot_spots = []
        for i in range(self.LOOT_CHESTS):
            x0 = i * seg + rng.randint(6, seg - 12)
            y0 = rng.randint(w.height[x0] + 16, WH - 14)
            for xx in range(x0 - 1, x0 + 6):               # a 5x3 room with a stone shell
                for yy in range(y0 - 1, y0 + 4):
                    if x0 <= xx <= x0 + 4 and y0 <= yy <= y0 + 2:
                        w.set(xx, yy, AIR)
                    elif w.get(xx, yy) in (AIR, LAVA, WATER):
                        w.set(xx, yy, STONE)
            loot = [(IRON_INGOT, rng.randint(6, 20)), (DIAMOND, rng.randint(2, 6))]
            for item, chance, lo, hi in ((ENDER_PEARL, 0.75, 1, 3), (REGEN_POTION, 0.55, 1, 2),
                                         (PROTECTION_POTION, 0.5, 1, 1), (STEAK, 0.6, 3, 8), (COAL, 0.5, 5, 16)):
                if rng.random() < chance:
                    loot.append((item, rng.randint(lo, hi)))
            if i == netherite_in:
                loot.append((NETHERITE_INGOT, 1))
            slots = [None] * 27
            for k, (item, n) in zip(rng.sample(range(27), len(loot)), loot):
                slots[k] = new_stack(item, n)
            xr = random.Random(w.seed * 104729 + 31 * i + 7)     # own stream: older loot layouts stay unchanged
            if xr.random() < 0.7:
                free = [k for k in range(27) if slots[k] is None]
                slots[xr.choice(free)] = new_stack(XP_BOTTLE, xr.randint(2, 6))
            pos = (x0 + 2, y0 + 2)
            w.set(pos[0], pos[1], CHEST)
            self.chests[pos] = slots
            self.loot_spots.append(pos)

    def save(self):
        try:
            self.stash()
            dims = {d: dict(cols=[bytes(c) for c in w.cols], height=w.height,
                            furnaces=self.dstate[d]["furnaces"], chests=self.dstate[d]["chests"],
                            pearls=[x for x in self.dstate[d].get("pearls", []) if x.float_t is not None])
                    for d, w in self.worlds.items()}
            data = dict(seed=self.worlds[0].seed, dims=dims, dim=self.dim, inv=self.inv,
                        px=self.p.x, py=self.p.y, hp=self.p.hp,
                        time=self.time, sel=self.sel, spawn=self.spawn, creative=self.creative,
                        waypoints=self.waypoints, protect_t=self.protect_t, xp=self.xp, ext_pistons=self.ext_pistons,
                        bobber=self.bobber,
                        ender=self.ender, armor=self.armor, food=self.food, end_state=self.end_state,
                        name=self.world_name)
            path = self.save_path or SAVE
            if os.path.dirname(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                pickle.dump(data, f)
            self.say("Game saved.")
        except Exception as ex:                       # noqa
            self.say("Save failed: %s" % ex)

    def load(self, path=None):
        """Load a world file (the current one by default). True when it worked."""
        try:
            path = path or self.save_path or SAVE
            with open(path, "rb") as f:
                d = pickle.load(f)
            dims = d.get("dims") or {0: dict(cols=d["cols"], height=d["height"],
                                             furnaces=d["furnaces"], chests=d["chests"])}
            self.worlds, self.dstate = {}, {}
            for k, v in dims.items():
                w = World.__new__(World)
                w.seed, w.dim = d["seed"], k
                w.cols = [bytearray(c) for c in v["cols"]]
                w.height = v["height"]
                self.worlds[k] = w
                pl = v.get("pearls", [])
                pl = [x for x in pl if isinstance(x, Pearl)] if isinstance(pl, list) else []
                self.dstate[k] = dict(furnaces=v["furnaces"], chests=v["chests"], drops=[], zombies=[], tnts=[], cows=[], crystals=[], bosses=[], pearls=pl)
            self.dim = d.get("dim", 0)
            self.world = self.worlds[self.dim]
            for k in self.DIM_KEYS:
                setattr(self, k, self.dstate[self.dim][k])
            self.inv, self.sel = d["inv"], d["sel"]
            self.p.x, self.p.y, self.p.hp = d["px"], d["py"], d["hp"]
            self.time, self.spawn = d["time"], d["spawn"]
            self.creative = d.get("creative", False)
            self.waypoints = d.get("waypoints", [])
            self.protect_t = d.get("protect_t", 0.0)
            bo = d.get("bobber")
            self.bobber = bo if isinstance(bo, dict) and all(k in bo for k in ("x", "y", "vx", "vy", "mode", "surf", "t", "bite", "window", "dim")) else None
            ep = d.get("ext_pistons", {})
            self.ext_pistons = ep if isinstance(ep, dict) else {}
            self.observers, self.obs_pulse = {}, {}
            xp = d.get("xp", 0)
            self.xp = int(xp) if isinstance(xp, (int, float)) else 0
            es = d.get("end_state")
            self.end_state = es if isinstance(es, dict) else dict(dragon_dead=False)
            if self.end_state.get("dragon_dead"):
                self.end_state.setdefault("egg_spawned", True)
            fd = d.get("food", 20.0)
            self.food = float(fd) if isinstance(fd, (int, float)) else 20.0
            arm = d.get("armor")
            self.armor = arm if isinstance(arm, list) and len(arm) == 4 else [None] * 4
            ender = d.get("ender")
            self.ender = ender if isinstance(ender, list) and len(ender) == 27 else [None] * 27
            self.save_path = path if path != SAVE else None
            nm = d.get("name")
            self.world_name = nm if isinstance(nm, str) and nm.strip() else ("Old World" if path == SAVE else "World")
            self.say("World loaded.")
            self.purge_bad_items()
            return True
        except Exception as ex:                       # noqa
            self.say("Could not load save (%s), new world." % ex)
            return False

    # ----- command line ------------------------------------------------------ #
    CMD_USAGE = {
        "setblock": "/setblock <x> <y> <block> [replace|keep]   - put one block. x y are cells; ~ means your cell, ~3 / ~-3 are offsets",
        "fill": "/fill <x1> <y1> <x2> <y2> <block> [replace [old] | hollow | outline | keep]   - fill a box (up to %d cells)" % FILL_LIMIT,
        "give": "/give <item> [count]   - put items in your inventory (count 1-%d, default 1). Same names as the creative menu" % GIVE_MAX,
        "tick": "/tick freeze | unfreeze | step [n] | query   - stop the world's clock, run n ticks (20 per second) at a time",
        "help": "/help [command]",
    }
    CMD_NAMES = ("fill", "give", "help", "setblock", "tick")

    def chat_add(self, text, col=(255, 255, 255)):
        self.chat.append((text, col, pygame.time.get_ticks() + 8000))
        del self.chat[:-60]

    def open_cmd(self, text=""):
        self.cmd = dict(text=text, hist=None)
        self.tab_state = None

    def close_cmd(self):
        self.cmd = None

    def cmd_key(self, key, uni=""):
        c = self.cmd
        if key == pygame.K_ESCAPE:
            self.close_cmd()
        elif key == pygame.K_RETURN:
            text = c["text"].strip()
            self.close_cmd()
            if text:
                if not self.cmd_hist or self.cmd_hist[-1] != text:
                    self.cmd_hist.append(text)
                del self.cmd_hist[:-50]
                self.run_command(text)
        elif key == pygame.K_BACKSPACE:
            c["text"] = c["text"][:-1]
            self.tab_state = None
        elif key == pygame.K_UP and self.cmd_hist:
            c["hist"] = len(self.cmd_hist) - 1 if c["hist"] is None else max(0, c["hist"] - 1)
            c["text"] = self.cmd_hist[c["hist"]]
        elif key == pygame.K_DOWN and c["hist"] is not None:
            c["hist"] += 1
            if c["hist"] >= len(self.cmd_hist):
                c["hist"], c["text"] = None, ""
            else:
                c["text"] = self.cmd_hist[c["hist"]]
        elif key == pygame.K_TAB:
            self.cmd_complete()
        elif uni and len(uni) == 1 and ord(uni) >= 32 and len(c["text"]) < 200:
            c["text"] += uni
            self.tab_state = None

    def cmd_complete(self):
        c = self.cmd
        text = c["text"]
        head, sp, last = text.rpartition(" ")
        if not sp:
            cands = [n for n in self.CMD_NAMES if n.startswith(last.lstrip("/").lower())]
            pre = "/" if last.startswith("/") else ""
            word = last.lstrip("/")
        else:
            word = last.lower()
            pre = ""
            if last[:1] in "~-0123456789":
                return
            toks = head.split()
            cmd, idx = toks[0].lstrip("/").lower(), len(toks) - 1          # idx: which argument is being typed
            blocks = self.block_table()
            if cmd == "tick" and idx == 0:
                pool = ("freeze", "unfreeze", "step", "query")
            elif cmd == "help" and idx == 0:
                pool = self.CMD_NAMES
            elif cmd == "give":
                pool = self.item_table() if idx == 0 else ()
            elif cmd == "setblock":
                pool = blocks if idx == 2 else (("replace", "keep") if idx == 3 else ())
            elif cmd == "fill":
                pool = blocks if idx == 4 else (("replace", "hollow", "outline", "keep") if idx == 5
                                                else (blocks if idx == 6 and toks[5].lower() == "replace" else ()))
            else:
                pool = ()
            cands = sorted(n for n in pool if n.startswith(word))
        if not cands:
            return
        common = cands[0]
        for n in cands[1:]:
            while not n.startswith(common):
                common = common[:-1]
        c["text"] = (head + sp if sp else "") + pre + common + (" " if len(cands) == 1 else "")
        if len(cands) > 1 and common == word:
            self.chat_add("  ".join(cands[:14]) + (" ..." if len(cands) > 14 else ""), (170, 200, 255))

    @staticmethod
    def norm_name(name):
        out, prev = [], False
        for ch in name.lower():
            if ch.isalnum():
                out.append(ch)
                prev = False
            elif not prev and out:
                out.append("_")
                prev = True
        return "".join(out).strip("_")

    def block_table(self):
        """{typed name: block id}: every placeable block (pistons and observers as <name>_left/right/up/down)."""
        tab = getattr(self, "_block_table", None)
        if tab is not None:
            return tab
        skip = set(PISTON_BASE + PISTON_EXT + PISTON_HEAD + STICKY_BASE + STICKY_EXT + STICKY_HEAD + OBSERVER_BLK
                   + (DOOR_CB, DOOR_CT, DOOR_OB, DOOR_OT))
        tab = {"air": AIR}
        for i, it in ITEMS.items():
            if i in skip or not it.get("block"):
                continue
            tab.setdefault(self.norm_name(it["name"]), i)
        for base, blks in ((PISTON, PISTON_BASE), (STICKY, STICKY_BASE), (OBSERVER, OBSERVER_BLK)):
            nm = self.norm_name(ITEMS[base]["name"])
            tab[nm] = blks[1]                                    # facing right unless you say otherwise
            for d, dn in enumerate(("left", "right", "up", "down")):
                tab[nm + "_" + dn] = blks[d]
        self._block_table = tab
        return tab

    def resolve_block(self, word):
        tab = self.block_table()
        key = self.norm_name(word)
        if key.startswith("potatocraft_"):
            key = key[12:]
        if key in tab:
            return tab[key]
        hits = sorted(n for n in tab if n.startswith(key)) or sorted(n for n in tab if key and key in n)
        if len(hits) == 1:
            return tab[hits[0]]
        if hits:
            raise ValueError("Ambiguous block '%s': %s" % (word, ", ".join(hits[:8]) + (" ..." if len(hits) > 8 else "")))
        for i, it in ITEMS.items():
            if self.norm_name(it["name"]) == key:
                raise ValueError("%s is an item, not a block." % it["name"])
        raise ValueError("Unknown block '%s'." % word)

    def item_table(self):
        """{typed name: item id}: everything in the creative menu."""
        tab = getattr(self, "_item_table", None)
        if tab is None:
            tab = {}
            for i in CREATIVE_ITEMS:
                tab.setdefault(self.norm_name(ITEMS[i]["name"]), i)
            self._item_table = tab
        return tab

    def resolve_item(self, word):
        tab = self.item_table()
        key = self.norm_name(word)
        if key.startswith("potatocraft_"):
            key = key[12:]
        if key in tab:
            return tab[key]
        if key.isdigit() and int(key) in tab.values():
            return int(key)
        hits = sorted(n for n in tab if n.startswith(key)) or sorted(n for n in tab if key and key in n)
        if len(hits) == 1:
            return tab[hits[0]]
        if hits:
            raise ValueError("Ambiguous item '%s': %s" % (word, ", ".join(hits[:8]) + (" ..." if len(hits) > 8 else "")))
        raise ValueError("Unknown item '%s'." % word)

    def cmd_give(self, args):
        if args and args[0].lower() in ("@s", "@p", "me"):
            args = args[1:]
        if not 1 <= len(args) <= 2:
            raise ValueError("Usage: " + self.CMD_USAGE["give"])
        i = self.resolve_item(args[0])
        try:
            n = int(args[1]) if len(args) == 2 else 1
        except ValueError:
            raise ValueError("'%s' is not a whole number." % args[1])
        if not 1 <= n <= GIVE_MAX:
            raise ValueError("The count must be between 1 and %d." % GIVE_MAX)
        mx, rest, given = maxstack(i), n, 0
        while rest > 0:                                      # one stack at a time
            chunk = min(mx, rest)
            left = self.give(i, chunk, ITEMS[i].get("dur"))
            given += chunk - left
            rest -= chunk
            if left:
                break
        name = ITEMS[i]["name"]
        if given <= 0:
            raise ValueError("Your inventory is full.")
        if given < n:
            return "Gave %d x %s (inventory full: %d did not fit)." % (given, name, n - given)
        return "Gave %d x %s." % (n, name)

    def cmd_coord(self, tok, axis):
        p = self.p
        base = int(math.floor(p.x + p.w / 2)) if axis == 0 else int(math.floor(p.y + p.h - 0.01))
        try:
            if tok.startswith("~"):
                return base + (int(tok[1:]) if tok[1:] else 0)
            return int(tok)
        except ValueError:
            raise ValueError("'%s' is not a whole number (use ~ for your own cell, ~2 / ~-2 for offsets)." % tok)

    def cmd_clear_cell(self, x, y):
        """A block is being replaced by a command: drop the per-block state of what stood there."""
        old = self.world.get(x, y)
        if old in (CHEST, SHULKER_BOX):
            self.chests.pop((x, y), None)
        elif old == FURNACE:
            self.furnaces.pop((x, y), None)
        elif old in PISTON_EXT or old in STICKY_EXT:
            self.ext_pistons.pop((self.dim, x, y), None)
        return old

    def cmd_put(self, x, y, b):
        self.cmd_clear_cell(x, y)
        self.world.set(x, y, b)
        if b == CHEST:
            self.chests[(x, y)] = [None] * 27
        elif b == SHULKER_BOX:
            self.chests[(x, y)] = [None] * 27
        elif b == FURNACE:
            self.furnaces[(x, y)] = new_furnace()

    def run_command(self, text):
        """Run one command line. Prints the result into the chat log; True when it worked."""
        parts = text.strip().lstrip("/").split()
        if not parts:
            return False
        name, args = parts[0].lower(), parts[1:]
        self.chat_add("/" + " ".join(parts), (190, 190, 195))
        try:
            fn = getattr(self, "cmd_" + name, None) if name in self.CMD_NAMES else None
            if fn is None:
                raise ValueError("Unknown command '%s'. Try /help." % name)
            msg = fn(args)
            self.chat_add(msg, (150, 230, 150))
            return True
        except ValueError as ex:
            self.chat_add(str(ex), (255, 130, 120))
            return False

    def cmd_help(self, args):
        if args:
            u = self.CMD_USAGE.get(args[0].lower().lstrip("/"))
            if not u:
                raise ValueError("No such command: %s" % args[0])
            return u
        for n in self.CMD_NAMES:
            self.chat_add(self.CMD_USAGE[n], (170, 200, 255))
        return "Press T or / to type a command. Tab completes, Up/Down repeat. Y grows downward (~-1 is the cell above you)."

    def cmd_setblock(self, args):
        if len(args) < 3 or len(args) > 4:
            raise ValueError("Usage: " + self.CMD_USAGE["setblock"])
        x, y = self.cmd_coord(args[0], 0), self.cmd_coord(args[1], 1)
        b = self.resolve_block(args[2])
        mode = (args[3].lower() if len(args) == 4 else "replace")
        if mode not in ("replace", "keep"):
            raise ValueError("Mode must be replace or keep.")
        if not (0 <= x < WW and 0 <= y < WH):
            raise ValueError("That cell is outside the world (x 0-%d, y 0-%d)." % (WW - 1, WH - 1))
        if mode == "keep" and self.world.get(x, y) != AIR:
            raise ValueError("The cell (%d, %d) is not empty." % (x, y))
        self.cmd_put(x, y, b)
        self.torch_scan_t = 0.0
        return "Placed %s at (%d, %d)." % (ITEMS[b]["name"] if b else "air", x, y)

    def cmd_fill(self, args):
        if len(args) < 5:
            raise ValueError("Usage: " + self.CMD_USAGE["fill"])
        x1, y1 = self.cmd_coord(args[0], 0), self.cmd_coord(args[1], 1)
        x2, y2 = self.cmd_coord(args[2], 0), self.cmd_coord(args[3], 1)
        b = self.resolve_block(args[4])
        mode, flt = "replace", None
        if len(args) >= 6:
            mode = args[5].lower()
            if mode not in ("replace", "hollow", "outline", "keep"):
                raise ValueError("Mode must be replace, hollow, outline or keep.")
            if mode == "replace" and len(args) >= 7:
                raw = self.resolve_block(args[6])
                base = {PISTON_BASE[1]: PISTON, STICKY_BASE[1]: STICKY, OBSERVER_BLK[1]: OBSERVER}.get(raw, raw)
                if any(raw == blks[d] for blks in (PISTON_BASE, STICKY_BASE, OBSERVER_BLK) for d in (0, 2, 3)):
                    flt = {raw}
                else:
                    flt = {i for i in ITEMS if i == base or ITEMS[i].get("drop") == base} | {raw}
                if raw == AIR:
                    flt = {AIR}
            if len(args) > (7 if mode == "replace" else 6):
                raise ValueError("Too many arguments. " + self.CMD_USAGE["fill"])
        x1, x2, y1, y2 = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
        if x1 < 0 or x2 >= WW or y1 < 0 or y2 >= WH:
            raise ValueError("The box leaves the world (x 0-%d, y 0-%d)." % (WW - 1, WH - 1))
        vol = (x2 - x1 + 1) * (y2 - y1 + 1)
        if vol > FILL_LIMIT:
            raise ValueError("That box is %d cells; the limit is %d." % (vol, FILL_LIMIT))
        w, n = self.world, 0
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                edge = x in (x1, x2) or y in (y1, y2)
                cur = w.get(x, y)
                put = b
                if mode == "hollow" and not edge:
                    put = AIR
                elif mode == "outline" and not edge:
                    continue
                elif mode == "keep" and cur != AIR:
                    continue
                elif flt is not None and cur not in flt:
                    continue
                if cur == put and put not in (CHEST, SHULKER_BOX, FURNACE):
                    continue
                self.cmd_put(x, y, put)
                n += 1
        if not n:
            raise ValueError("Nothing changed.")
        self.torch_scan_t = 0.0
        return "Filled %d cell%s." % (n, "" if n == 1 else "s")

    def cmd_tick(self, args):
        sub = args[0].lower() if args else "query"
        if sub == "freeze":
            self.tick_frozen = True
            return "The world is frozen. You can still move and build. /tick step [n] runs ticks, /tick unfreeze resumes."
        if sub in ("unfreeze", "resume"):
            self.tick_frozen, self.tick_steps, self.tick_done = False, 0, 0
            return "The world is running again."
        if sub == "step":
            try:
                n = int(args[1]) if len(args) > 1 else 1
            except ValueError:
                raise ValueError("Usage: /tick step [number of ticks]")
            if not 1 <= n <= TICK_STEP_MAX:
                raise ValueError("Steps must be between 1 and %d." % TICK_STEP_MAX)
            self.tick_frozen = True
            self.tick_steps += n
            return "Stepping %d tick%s (%.2f s of game time)..." % (n, "" if n == 1 else "s", n * TICK_DT)
        if sub == "query":
            return ("The world is frozen" + (" (%d ticks still to run)." % self.tick_steps if self.tick_steps else ".")
                    if self.tick_frozen else "The world is running (20 ticks per second).")
        raise ValueError("Usage: " + self.CMD_USAGE["tick"])

    def draw_console(self):
        scr, now = self.screen, pygame.time.get_ticks()
        open_ = self.cmd is not None
        lines = self.chat[-12:] if open_ else [c for c in self.chat[-6:] if c[2] > now]
        base = SH - 44 if open_ else SH - 66
        for i, (text, col, _) in enumerate(reversed(lines)):
            self.txt(text[:150], (12, base - 18 * (i + 1)), col, self.small)
        if open_:
            bar = pygame.Surface((SW - 20, 26), pygame.SRCALPHA)
            bar.fill((0, 0, 0, 190))
            scr.blit(bar, (10, SH - 38))
            caret = "_" if int(now / 400) % 2 == 0 else " "
            self.txt("> " + self.cmd["text"] + caret, (18, SH - 32))
        if self.tick_frozen:
            self.txt("TICKS FROZEN" + ("  (%d to go)" % self.tick_steps if self.tick_steps else ""), (SW // 2, 22), (140, 220, 255), self.font, True)

    # ----- world menu ------------------------------------------------------- #
    MENU_ROW = 68
    MENU_ROWS = 5

    @staticmethod
    def parse_seed(text):
        """Empty: random. A number: that number. Any other text: a number made from it."""
        text = (text or "").strip()
        if not text:
            return None
        try:
            return abs(int(text)) % (1 << 30)
        except ValueError:
            import zlib
            return zlib.crc32(text.encode("utf-8")) % (1 << 30)

    def world_files(self):
        out = [SAVE] if os.path.exists(SAVE) else []
        try:
            out += [os.path.join(WORLD_DIR, f) for f in os.listdir(WORLD_DIR) if f.endswith(".pkl")]
        except OSError:
            pass
        return out

    def world_info(self, path):
        info = dict(path=path, name="Old World" if path == SAVE else os.path.basename(path)[:-4],
                    creative=False, dim=0, ok=False, mtime=0.0)
        try:
            info["mtime"] = os.path.getmtime(path)
            with open(path, "rb") as f:
                d = pickle.load(f)
            nm = d.get("name")
            if isinstance(nm, str) and nm.strip():
                info["name"] = nm
            info.update(creative=bool(d.get("creative", False)), dim=d.get("dim", 0), ok=True)
        except Exception:                             # noqa
            pass
        return info

    def refresh_worlds(self):
        infos = sorted((self.world_info(p) for p in self.world_files()), key=lambda i: -i["mtime"])
        m = self.menu
        m["worlds"] = infos
        m["sel"] = max(0, min(len(infos) - 1, m["sel"])) if infos else -1
        m["scroll"] = max(0, min(max(0, len(infos) - self.MENU_ROWS), m["scroll"]))

    def open_menu(self):
        self.paused, self.ui = False, None
        self.menu = dict(screen="list", worlds=[], sel=0, scroll=0, name="", seed="", creative=False,
                         field=0, msg="", drag=False)
        self.refresh_worlds()

    def create_world(self, name, seed_text="", creative=False):
        """Start a brand new world, save it right away under its own file."""
        import time as _tm
        name = (name or "").strip() or "New World"
        self.new_game(self.parse_seed(seed_text))
        self.world_name = name
        slug = "".join(c if c.isalnum() else "_" for c in name)[:24].strip("_") or "world"
        os.makedirs(WORLD_DIR, exist_ok=True)
        path = os.path.join(WORLD_DIR, "%s_%d.pkl" % (slug, int(_tm.time())))
        n = 1
        while os.path.exists(path):
            n += 1
            path = os.path.join(WORLD_DIR, "%s_%d_%d.pkl" % (slug, int(_tm.time()), n))
        self.save_path = path
        if creative:
            self.toggle_creative()
        self.menu = None
        self.save()
        self.say('World "%s" created.' % name, 3)

    def open_world(self, path):
        self.new_game()
        if self.load(path):
            self.menu = None
            return True
        return False

    def delete_world(self, path):
        try:
            os.remove(path)
            return True
        except OSError:
            return False

    def menu_rects(self):
        x0 = SW // 2 - 320
        R = pygame.Rect
        m = self.menu
        if m["screen"] == "new":
            return dict(name=R(x0 + 120, 190, 400, 40), seed=R(x0 + 120, 262, 400, 40), mode=R(x0 + 120, 330, 400, 40),
                        create=R(x0 + 120, 410, 400, 46), back=R(x0 + 120, 466, 400, 36))
        r = dict(panel=R(x0, 120, 640, self.MENU_ROW * self.MENU_ROWS), play=R(x0, 480, 640, 44),
                 new=R(x0, 534, 312, 40), delete=R(x0 + 328, 534, 312, 40), quit=R(x0, 584, 640, 34),
                 track=R(x0 + 648, 120, 12, self.MENU_ROW * self.MENU_ROWS))
        if m["screen"] == "confirm":
            r.update(yes=R(SW // 2 - 150, 360, 140, 44), no=R(SW // 2 + 10, 360, 140, 44))
        return r

    def menu_row_rect(self, i):
        p = self.menu_rects()["panel"]
        return pygame.Rect(p.x, p.y + (i - self.menu["scroll"]) * self.MENU_ROW, p.w, self.MENU_ROW)

    def menu_thumb(self):
        tr, m = self.menu_rects()["track"], self.menu
        mx = max(0, len(m["worlds"]) - self.MENU_ROWS)
        th = max(30, int(tr.h * self.MENU_ROWS / float(max(self.MENU_ROWS, len(m["worlds"])))))
        ty = tr.y + (int((tr.h - th) * m["scroll"] / float(mx)) if mx else 0)
        return pygame.Rect(tr.x, ty, tr.w, th)

    def menu_scroll_by(self, rows):
        m = self.menu
        m["scroll"] = max(0, min(max(0, len(m["worlds"]) - self.MENU_ROWS), m["scroll"] + rows))

    def menu_select(self, i):
        m = self.menu
        m["sel"] = i
        if i < m["scroll"]:
            m["scroll"] = i
        elif i >= m["scroll"] + self.MENU_ROWS:
            m["scroll"] = i - self.MENU_ROWS + 1

    def menu_play(self):
        m = self.menu
        if 0 <= m["sel"] < len(m["worlds"]):
            info = m["worlds"][m["sel"]]
            if not self.open_world(info["path"]):
                self.open_menu()
                self.menu["msg"] = 'Could not open "%s" (the file is damaged).' % info["name"]

    def menu_click(self, pos, button=1):
        m, r = self.menu, self.menu_rects()
        if button != 1:
            return
        if m["screen"] == "new":
            if r["name"].collidepoint(pos):
                m["field"] = 0
            elif r["seed"].collidepoint(pos):
                m["field"] = 1
            elif r["mode"].collidepoint(pos):
                m["creative"] = not m["creative"]
            elif r["create"].collidepoint(pos):
                self.create_world(m["name"], m["seed"], m["creative"])
            elif r["back"].collidepoint(pos):
                m["screen"] = "list"
            return
        if m["screen"] == "confirm":
            if r["yes"].collidepoint(pos):
                info = m["worlds"][m["sel"]]
                ok = self.delete_world(info["path"])
                m["screen"] = "list"
                self.refresh_worlds()
                m["msg"] = ('Deleted "%s".' if ok else 'Could not delete "%s".') % info["name"]
            elif r["no"].collidepoint(pos):
                m["screen"] = "list"
            return
        m["msg"] = ""
        if len(m["worlds"]) > self.MENU_ROWS and r["track"].inflate(10, 0).collidepoint(pos):
            th = self.menu_thumb()
            m["drag"] = True
            mx = len(m["worlds"]) - self.MENU_ROWS
            frac = (pos[1] - r["track"].y - th.h / 2.0) / float(max(1, r["track"].h - th.h))
            m["scroll"] = max(0, min(mx, int(round(frac * mx))))
            return
        if r["panel"].collidepoint(pos):
            i = m["scroll"] + (pos[1] - r["panel"].y) // self.MENU_ROW
            if 0 <= i < len(m["worlds"]):
                if i == m["sel"] and m.get("click_i") == i and m.get("click_t", -9999) + 450 > pygame.time.get_ticks():
                    self.menu_play()                      # a double click plays
                    return
                m["sel"], m["click_i"], m["click_t"] = i, i, pygame.time.get_ticks()
        elif r["play"].collidepoint(pos):
            self.menu_play()
        elif r["new"].collidepoint(pos):
            m.update(screen="new", name="", seed="", creative=False, field=0)
        elif r["delete"].collidepoint(pos):
            if 0 <= m["sel"] < len(m["worlds"]):
                m["screen"] = "confirm"
        elif r["quit"].collidepoint(pos):
            pygame.quit()
            sys.exit(0)

    def menu_drag(self, pos):
        m = self.menu
        if m and m.get("drag") and m["screen"] == "list":
            r = self.menu_rects()
            th = self.menu_thumb()
            mx = max(0, len(m["worlds"]) - self.MENU_ROWS)
            frac = (pos[1] - r["track"].y - th.h / 2.0) / float(max(1, r["track"].h - th.h))
            m["scroll"] = max(0, min(mx, int(round(frac * mx))))

    def menu_key(self, key, uni=""):
        m = self.menu
        if m["screen"] == "new":
            if key == pygame.K_ESCAPE:
                m["screen"] = "list"
            elif key == pygame.K_RETURN:
                self.create_world(m["name"], m["seed"], m["creative"])
            elif key == pygame.K_TAB:
                m["field"] = 1 - m["field"]
            elif key == pygame.K_BACKSPACE:
                k = "name" if m["field"] == 0 else "seed"
                m[k] = m[k][:-1]
            elif uni and len(uni) == 1 and ord(uni) >= 32:
                k, cap = ("name", 24) if m["field"] == 0 else ("seed", 18)
                if len(m[k]) < cap:
                    m[k] += uni
            return
        if m["screen"] == "confirm":
            if key == pygame.K_y or key == pygame.K_RETURN:
                self.menu_click(self.menu_rects()["yes"].center)
            elif key == pygame.K_n or key == pygame.K_ESCAPE:
                m["screen"] = "list"
            return
        if key == pygame.K_UP and m["worlds"]:
            self.menu_select(max(0, m["sel"] - 1))
        elif key == pygame.K_DOWN and m["worlds"]:
            self.menu_select(min(len(m["worlds"]) - 1, m["sel"] + 1))
        elif key == pygame.K_RETURN:
            if m["worlds"]:
                self.menu_play()
            else:
                m.update(screen="new", name="", seed="", creative=False, field=0)
        elif key == pygame.K_n:
            m.update(screen="new", name="", seed="", creative=False, field=0)
        elif key == pygame.K_DELETE and 0 <= m["sel"] < len(m["worlds"]):
            m["screen"] = "confirm"

    def menu_button(self, rect, label, enabled=True, hot=False, big=False):
        scr = self.screen
        pygame.draw.rect(scr, (90, 150, 80) if (hot and enabled) else ((70, 70, 78) if enabled else (50, 50, 54)), rect)
        pygame.draw.rect(scr, (230, 230, 235) if enabled else (110, 110, 115), rect, 2)
        self.txt(label, rect.center, (255, 255, 255) if enabled else (140, 140, 145), self.big if big else self.font, True)

    def draw_menu(self):
        import time as _tm
        scr, m, r = self.screen, self.menu, self.menu_rects()
        mpos = pygame.mouse.get_pos()
        scr.fill((38, 30, 24))
        for ty in range(0, SH, TILE):
            for tx in range(0, SW, TILE):
                scr.blit(TEX[DIRT], (tx, ty))
        dim = pygame.Surface((SW, SH), pygame.SRCALPHA)
        dim.fill((0, 0, 0, 165))
        scr.blit(dim, (0, 0))
        self.txt("PotatoCraft", (SW // 2, 62), (255, 220, 120), self.big, True)
        self.txt("Select World" if m["screen"] != "new" else "Create New World", (SW // 2, 98), (210, 210, 215), self.font, True)
        if m["screen"] == "new":
            x0 = SW // 2 - 320
            for key, label in (("name", "World name"), ("seed", "Seed (optional)")):
                rc = r[key]
                self.txt(label, (rc.x, rc.y - 20), (210, 210, 215), self.small)
                pygame.draw.rect(scr, (20, 20, 24), rc)
                act = m["field"] == (0 if key == "name" else 1)
                pygame.draw.rect(scr, (255, 255, 255) if act else (120, 120, 126), rc, 2)
                caret = "|" if act and int(pygame.time.get_ticks() / 400) % 2 == 0 else ""
                if m[key]:
                    self.txt(m[key] + caret, (rc.x + 10, rc.y + 12))
                else:
                    self.txt(caret + ("New World" if key == "name" else "random"), (rc.x + 10, rc.y + 12), (110, 110, 116))
            self.menu_button(r["mode"], "Game mode: " + ("Creative" if m["creative"] else "Survival"), True, r["mode"].collidepoint(mpos))
            self.menu_button(r["create"], "Create World", True, r["create"].collidepoint(mpos), True)
            self.menu_button(r["back"], "Back", True, r["back"].collidepoint(mpos))
            self.txt("Tab: next field    Enter: create    Esc: back    (a word or number as seed always gives the same world)",
                     (SW // 2, 540), (170, 170, 176), self.small, True)
        else:
            p = r["panel"]
            pygame.draw.rect(scr, (16, 16, 20), p)
            if not m["worlds"]:
                self.txt("No worlds yet. Click Create New World!", p.center, (200, 200, 205), self.font, True)
            old = scr.get_clip() if hasattr(scr, "get_clip") else None
            scr.set_clip(p)
            for i in range(m["scroll"], min(len(m["worlds"]), m["scroll"] + self.MENU_ROWS)):
                inf, rr = m["worlds"][i], self.menu_row_rect(i)
                if i == m["sel"]:
                    pygame.draw.rect(scr, (60, 70, 100), rr)
                    pygame.draw.rect(scr, (255, 255, 255), rr, 2)
                elif rr.collidepoint(mpos):
                    pygame.draw.rect(scr, (36, 36, 44), rr)
                self.txt(inf["name"], (rr.x + 14, rr.y + 10), (255, 255, 255) if inf["ok"] else (230, 120, 110), self.font)
                if inf["ok"]:
                    when = _tm.strftime("%Y-%m-%d %H:%M", _tm.localtime(inf["mtime"]))
                    sub = "%s  -  %s  -  last played %s" % ("Creative" if inf["creative"] else "Survival",
                                                            {0: "Overworld", 1: "Nether", 2: "The End"}.get(inf["dim"], "Overworld"), when)
                else:
                    sub = "Damaged file - can't be opened (you can delete it)"
                self.txt(sub, (rr.x + 14, rr.y + 38), (170, 170, 176), self.small)
            scr.set_clip(old)
            pygame.draw.rect(scr, (120, 120, 126), p, 2)
            if len(m["worlds"]) > self.MENU_ROWS:
                pygame.draw.rect(scr, (30, 30, 36), r["track"])
                pygame.draw.rect(scr, (200, 200, 205) if m.get("drag") else (140, 140, 146), self.menu_thumb())
            has = 0 <= m["sel"] < len(m["worlds"])
            self.menu_button(r["play"], "Play Selected World", has, has and r["play"].collidepoint(mpos), True)
            self.menu_button(r["new"], "Create New World", True, r["new"].collidepoint(mpos))
            self.menu_button(r["delete"], "Delete World", has, has and r["delete"].collidepoint(mpos))
            self.menu_button(r["quit"], "Quit", True, r["quit"].collidepoint(mpos))
            if m["msg"]:
                self.txt(m["msg"], (SW // 2, 640), (255, 200, 120), self.font, True)
            if m["screen"] == "confirm":
                ov = pygame.Surface((SW, SH), pygame.SRCALPHA)
                ov.fill((0, 0, 0, 170))
                scr.blit(ov, (0, 0))
                nm = m["worlds"][m["sel"]]["name"]
                self.txt('Delete "%s" forever?' % nm, (SW // 2, 300), (255, 255, 255), self.big, True)
                self.txt("This cannot be undone.", (SW // 2, 336), (230, 150, 140), self.font, True)
                self.menu_button(r["yes"], "Yes, delete", True, r["yes"].collidepoint(mpos))
                self.menu_button(r["no"], "No", True, r["no"].collidepoint(mpos))
            else:
                self.txt("Up/Down: choose    Enter: play    N: new    Del: delete    double-click plays",
                         (SW // 2, 656), (140, 140, 146), self.small, True)
        pygame.display.flip()

    def menu_frame(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif self.menu is None:
                break                                       # a click just started a world: leave the rest for the game
            elif e.type == pygame.KEYDOWN:
                self.menu_key(e.key, getattr(e, "unicode", ""))
            elif e.type == pygame.MOUSEWHEEL and self.menu["screen"] == "list":
                self.menu_scroll_by(-e.y)
            elif e.type == pygame.MOUSEMOTION:
                self.menu_drag(e.pos)
            elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                self.menu["drag"] = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                self.menu_click(e.pos, e.button)
        if self.menu is not None:
            self.clock.tick(60)
            self.draw_menu()

    def purge_bad_items(self):
        """Old saves may hold 'items' that are really world blocks (e.g. the End Portal block picked up
        after TNT blew up a portal). Remove them from every container."""
        conts = [self.inv, self.ender] + [c for st in self.dstate.values() for c in st["chests"].values()]
        n = 0
        for cont in conts:
            for i, st in enumerate(cont):
                if st and st[0] in NO_ITEM:
                    cont[i] = None
                    n += 1
        if n:
            self.say("Removed %d invalid item stack(s) from your save." % n, 5)

    DIM_KEYS = ("furnaces", "chests", "drops", "zombies", "tnts", "cows", "crystals", "bosses", "pearls")

    def stash(self):
        self.dstate[self.dim] = {k: getattr(self, k) for k in self.DIM_KEYS}

    def switch_dim(self, dim):
        self.pearls[:] = [x for x in self.pearls if x.float_t is not None]     # floating pearls stay behind
        self.torch_list, self.torch_on, self.torch_scan_t, self.active_plates = [], set(), 0.0, set()
        self.stash()
        self.arrows.clear()
        self.dim = dim
        if dim not in self.worlds:
            self.worlds[dim] = World(self.worlds[0].seed, dim)
        self.world = self.worlds[dim]
        st = self.dstate.get(dim) or dict(furnaces={}, chests={}, drops=[], zombies=[], tnts=[], cows=[], crystals=[], bosses=[], pearls=[])
        for k in self.DIM_KEYS:
            setattr(self, k, st[k])
        self.mining, self.mine_prog = None, 0.0

    # ----- portals --------------------------------------------------------- #
    def find_frame(self, bx, by):
        """Air cells of a closed obsidian rectangle (>=2x3) next to the clicked block, else None."""
        w = self.world
        nb = ((1, 0), (-1, 0), (0, 1), (0, -1))
        b = w.get(bx, by)
        if b == AIR:
            starts = [(bx, by)]
        elif b == OBSIDIAN:
            starts = [(bx + dx, by + dy) for dx, dy in nb if w.get(bx + dx, by + dy) == AIR]
        else:
            return None
        for st in starts:
            cells, todo, ok = {st}, [st], True
            while todo and ok:
                x, y = todo.pop()
                for dx, dy in nb:
                    n = (x + dx, y + dy)
                    if n in cells:
                        continue
                    nbk = w.get(*n)
                    if nbk == AIR:
                        cells.add(n)
                        todo.append(n)
                        if len(cells) > 64:
                            ok = False
                            break
                    elif nbk != OBSIDIAN:
                        ok = False
                        break
            if not ok:
                continue
            xs, ys = [c[0] for c in cells], [c[1] for c in cells]
            fw, fh = max(xs) - min(xs) + 1, max(ys) - min(ys) + 1
            if len(cells) == fw * fh and 2 <= fw <= 8 and 3 <= fh <= 8:
                return cells
        return None

    def light_portal(self, bx, by, block=PORTAL):
        cells = self.find_frame(bx, by)
        if not cells:
            return False
        for x, y in cells:
            self.world.set(x, y, block)
        return True

    def unlight(self, bx, by):
        w = self.world
        todo = [(bx + dx, by + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
        while todo:
            x, y = todo.pop()
            if w.get(x, y) in (PORTAL, END_PORTAL):
                w.set(x, y, AIR)
                todo += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def find_portal(self, tx):
        w, pb = self.world, bytes([PORTAL])
        for d in range(31):
            for x in {tx - d, tx + d}:
                if 0 <= x < WW:
                    y = w.cols[x].find(pb)
                    if y >= 0:
                        while w.get(x, y + 1) == PORTAL:
                            y += 1
                        return x + 0.2, y - 0.8 - 0.001
        return None

    def build_portal(self, tx):
        w = self.world
        tx = max(4, min(WW - 8, tx))
        if self.dim == 1:
            order = sorted(range(4, WW - 8), key=lambda x: abs(x - tx))
            def dry(x):             # keep the arrival platform away from lava lakes
                h = w.height[x]
                return not any(w.get(xx, yy) == LAVA for xx in range(x - 5, x + 8) for yy in range(h - 1, h + 2))
            tx = next((x for x in order if w.height[x] <= 74 and dry(x)), tx)
        h = w.height[tx]
        base = NETHERRACK if self.dim == 1 else DIRT
        for x in range(tx - 2, tx + 4):
            for y in range(h - 6, h):
                w.set(x, y, AIR)
            for y in range(h, h + 8):
                if w.get(x, y) in NONSOLID:
                    w.set(x, y, base)
                else:
                    break
        for y in range(h - 3, h):
            w.set(tx - 1, y, OBSIDIAN)
            w.set(tx + 2, y, OBSIDIAN)
        for x in (tx, tx + 1):
            w.set(x, h - 4, OBSIDIAN)
            w.set(x, h, OBSIDIAN)
            for y in range(h - 3, h):
                w.set(x, y, PORTAL)
        return tx + 0.2, h - 1 - 0.8 - 0.001

    def end_spawn(self):
        return END_SPAWN_X + 0.2, END_SURF - 1.8 - 0.01

    def use_portal(self, kind=PORTAL):
        p = self.p
        self.close_ui()
        if kind == END_PORTAL:
            dst = 2 if self.dim == 0 else 0
            self.switch_dim(dst)
            if dst == 2:
                p.x, p.y = self.end_spawn()
                self.enter_end()
            else:
                p.x, p.y = self.spawn
            p.vx = p.vy = 0.0
            p.air_peak = None
            self.portal_t, self.portal_lock = 0.0, True
            self.say("You arrive in the End. Destroy the crystals, slay the dragon!" if dst == 2 else "Back in the Overworld.", 5)
            return
        dst = 1 if self.dim == 0 else 0
        tx = int(p.x)
        self.switch_dim(dst)
        p.x, p.y = self.find_portal(tx) or self.build_portal(tx)
        p.vx = p.vy = 0.0
        p.air_peak = None
        self.portal_t, self.portal_lock = 0.0, True
        self.say("Welcome to the Nether. Watch out for lava!" if dst else "Back in the Overworld.", 4)

    def say(self, text, t=3.0):
        self.msg, self.msg_t = text, t

    def held(self):
        return self.inv[self.sel]

    def give(self, i, n, dur=None):
        s = [i, n, dur]
        put_into(self.inv, range(36), s)
        return s[1]

    # ----- The End --------------------------------------------------------- #
    def spawn_dragon(self):
        keep = [c for c in self.crystals if c.placed]
        self.crystals = keep + [Crystal(px - 0.4, END_SURF - h - 0.8 - 0.05) for px, h in END_PILLARS]
        self.bosses = [Dragon(END_CX - 2, 34)]

    def enter_end(self):
        if self.end_state.get("dragon_dead") or self.bosses:
            return
        self.spawn_dragon()

    def ritual_crystals(self):
        cx0, cy0 = END_CX + 0.5, END_SURF - 2.0
        return [c for c in self.crystals if c.placed and abs(c.x + 0.4 - cx0) < 9 and abs(c.y + 0.4 - cy0) < 9]

    def revive_dragon(self):
        for c in self.ritual_crystals():
            self.crystals.remove(c)
            self.booms.append([c.x + 0.4, c.y + 0.4, 0.2])
        for x in range(END_CX - 1, END_CX + 2):             # the exit portal closes
            for y in range(END_SURF - 3, END_SURF):
                if self.world.get(x, y) == END_PORTAL:
                    self.world.set(x, y, AIR)
        self.end_state["dragon_dead"] = False
        self.revive_t = None
        self.spawn_dragon()
        self.say("The Ender Dragon has been reborn! The exit is sealed until it falls.", 6)

    def crystal_blast(self, c):
        cx, cy = c.x + c.w / 2, c.y + c.h / 2
        self.booms.append([cx, cy, 0.0])
        for b in self.bosses:
            if math.hypot(b.x + b.w / 2 - cx, b.y + b.h / 2 - cy) < 14:
                b.hp -= 15
                b.flash = 0.4
        p = self.p
        d = math.hypot(p.x + p.w / 2 - cx, p.y + p.h / 2 - cy)
        if d < 6:
            self.hurt((1 - d / 6) * 12, force=True)

    def dragon_dead(self):
        self.end_state["dragon_dead"] = True
        w = self.world
        for x in (END_CX - 2, END_CX + 2):                 # bedrock fountain with the exit portal and the egg
            for y in range(END_SURF - 3, END_SURF):
                w.set(x, y, BEDROCK)
        for x in range(END_CX - 2, END_CX + 3):
            w.set(x, END_SURF - 4, BEDROCK)
        for x in range(END_CX - 1, END_CX + 2):
            for y in range(END_SURF - 3, END_SURF):
                w.set(x, y, END_PORTAL)
        if not self.end_state.get("egg_spawned"):            # the egg only appears for the first kill
            self.end_state["egg_spawned"] = True
            w.set(END_CX, END_SURF - 5, DRAGON_EGG)
            self.spawn_drop(END_CX + 1.6, END_SURF - 6.0, ELYTRA, 1, ITEMS[ELYTRA]["dur"], vx=0.0, vy=0.0)
            self.say("The Ender Dragon is dead! Take the Dragon Egg, then step into the portal.", 8)
        else:
            self.say("The Ender Dragon is dead again! Step into the portal to leave.", 6)

    def update_end(self, dt):
        for c in self.crystals[:]:
            if c not in self.crystals:
                continue
            c.flash = max(0.0, c.flash - dt)
            if c.hp <= 0:
                self.crystals.remove(c)
                self.crystal_blast(c)
        for b in self.bosses[:]:
            if b not in self.bosses:
                continue
            b.update(self, dt)
            if b not in self.bosses:
                continue
            if b.hp <= 0:
                self.bosses.remove(b)
                self.gain_xp(500)
                self.booms.append([b.x + b.w / 2, b.y + b.h / 2, 0.0])
                self.dragon_dead()
        if self.dim == 2 and self.end_state.get("dragon_dead") and not self.bosses:
            if len(self.ritual_crystals()) >= 4:
                if self.revive_t is None:
                    self.revive_t = 6.0
                    self.say("The portal rumbles... the crystals are summoning the dragon!", 5)
                self.revive_t -= dt
                if self.revive_t <= 0:
                    self.revive_dragon()
            elif self.revive_t is not None:
                self.revive_t = None
                self.say("The ritual was interrupted.")
        else:
            self.revive_t = None
        p = self.p
        if self.dim == 2 and p.y > END_SURF + 35:           # the void
            if self.creative or self.protect_t > 0:
                p.x, p.y = self.end_spawn()
                p.vx = p.vy = 0.0
                p.air_peak = None
                self.say("Saved from the void!")
            else:
                self.say("You fell into the void.", 4)
                self.die()

    # ----- TNT ------------------------------------------------------------- #
    def ignite_tnt(self, bx, by, fuse=4.0, hop=True):
        if self.world.get(bx, by) != TNT:
            return
        self.world.set(bx, by, AIR)
        t = PrimedTnt(bx, by, fuse)
        if hop:
            t.vy = -5.0
        else:
            t.vx, t.vy = self.rnd.uniform(-2, 2), self.rnd.uniform(-4, -1)
        self.tnts.append(t)

    def leaf_alert(self, bx, by):
        """A log is gone: for a while, leaves around it that lost their trunk fall."""
        for h in self.leaf_hot:
            if abs(h[0] - bx) <= 3 and abs(h[1] - by) <= 3:
                h[2] = 25.0
                return
        self.leaf_hot.append([bx, by, 25.0])
        del self.leaf_hot[:-40]

    def blast_block(self, bx, by, b):
        w = self.world
        w.set(bx, by, AIR)
        if b == LOG:
            self.leaf_alert(bx, by)
        if b in DOOR_TOGGLE:
            for py in (by - 1, by + 1):
                if w.get(bx, py) in DOOR_TOGGLE:
                    w.set(bx, py, AIR)
        cx, cy = bx + 0.35, by + 0.35
        if b == FURNACE and (bx, by) in self.furnaces:
            for s in self.furnaces.pop((bx, by))["s"]:
                if s:
                    self.spawn_drop(cx, cy, *s)
        elif b == CHEST and (bx, by) in self.chests:
            for s in self.chests.pop((bx, by)):
                if s:
                    self.spawn_drop(cx, cy, *s)
        elif b == SHULKER_BOX:
            contents = self.chests.pop((bx, by), None) or [None] * 27
            self.spawn_drop(cx, cy, SHULKER_BOX, 1, contents)
        elif b not in DOOR_TOGGLE and self.rnd.random() < 0.35:
            for it in drops_for(b, self.rnd):
                self.spawn_drop(cx, cy, it, 1, ITEMS[it].get("dur"))

    def explode(self, cx, cy, r=4.2):
        w = self.world
        p = self.p
        self.booms.append([cx, cy, 0.0])
        if w.get(int(cx), int(cy)) != WATER:          # no block damage under water
            for bx in range(int(cx - r) - 1, int(cx + r) + 2):
                for by in range(int(cy - r) - 1, int(cy + r) + 2):
                    if bx < 0 or bx >= WW or by < 0 or by >= WH:
                        continue
                    if math.hypot(bx + 0.5 - cx, by + 0.5 - cy) > r * self.rnd.uniform(0.8, 1.2):
                        continue
                    b = w.get(bx, by)
                    if b == AIR or b in UNBLASTABLE:
                        continue
                    if b == TNT:
                        self.ignite_tnt(bx, by, self.rnd.uniform(0.4, 1.2), hop=False)
                    else:
                        self.blast_block(bx, by, b)
        R = 7.5

        def push(e, d, dx, dy, k):
            e.vx += dx / d * k
            e.vy += dy / d * k - 2.0
        for z in self.zombies[:] + self.cows[:] + self.crystals[:] + self.bosses[:]:
            dx, dy = z.x + z.w / 2 - cx, z.y + z.h / 2 - cy
            d = max(0.3, math.hypot(dx, dy))
            if d < R:
                z.hp -= (1 - d / R) * 22
                z.flash = 0.3
                push(z, d, dx, dy, 12 * (1 - d / R))
        for e in self.drops + self.tnts:
            dx, dy = e.x - cx, e.y - cy
            d = max(0.3, math.hypot(dx, dy))
            if d < R:
                push(e, d, dx, dy, 10 * (1 - d / R))
        dx, dy = p.x + p.w / 2 - cx, p.y + p.h / 2 - cy
        d = max(0.3, math.hypot(dx, dy))
        if d < R:
            if not self.creative:
                push(p, d, dx, dy, 12 * (1 - d / R))
            self.hurt((1 - d / R) * 22, force=True)    # last: may kill us (die() resets everything)

    def update_tnts(self, dt):
        for t in self.tnts[:]:
            if t not in self.tnts:                      # a chain reaction / die() changed the list
                continue
            t.vy = min(t.vy + GRAVITY * dt, 25.0)
            if t.on_ground:
                t.vx *= 0.8
            physics(self.world, t, dt)
            t.fuse -= dt
            if t.fuse <= 0:
                self.tnts.remove(t)
                self.explode(t.x + t.w / 2, t.y + t.h / 2)
        for b in self.booms[:]:
            b[2] += dt
            if b[2] > 0.5:
                self.booms.remove(b)

    # ----- books ----------------------------------------------------------- #
    def bk_open(self):
        st = self.held()
        book_pages(st)
        self.bk_stack, self.bk_page, self.ui = st, 0, "book"

    def bk_close(self):
        self.bk_stack = None
        self.close_ui()

    def bk_rects(self):
        pr = pygame.Rect(SW // 2 - 270, SH // 2 - 250, 540, 500)
        text = pygame.Rect(pr.x + 20, pr.y + 46, pr.w - 40, 360)
        by = pr.bottom - 74
        names = ("prev", "next", "add", "del", "copy", "close")
        widths = (40, 40, 84, 84, 128, 70)
        x, btns = pr.x + 20, {}
        for n, w in zip(names, widths):
            btns[n] = pygame.Rect(x, by, w, 30)
            x += w + 8
        return pr, text, btns

    def bk_click(self, pos):
        st = self.bk_stack
        if not st:
            self.close_ui()
            return
        pages = book_pages(st)
        _, _, b = self.bk_rects()
        if b["prev"].collidepoint(pos):
            self.bk_page = max(0, self.bk_page - 1)
        elif b["next"].collidepoint(pos):
            self.bk_page = min(len(pages) - 1, self.bk_page + 1)
        elif b["add"].collidepoint(pos):
            if len(pages) >= BOOK_MAX_PAGES:
                self.say("A book can have at most %d pages." % BOOK_MAX_PAGES)
            else:
                pages.insert(self.bk_page + 1, "")
                self.bk_page += 1
        elif b["del"].collidepoint(pos):
            if len(pages) > 1:
                del pages[self.bk_page]
                self.bk_page = min(self.bk_page, len(pages) - 1)
            else:
                pages[0] = ""
        elif b["copy"].collidepoint(pos):
            self.bk_copy()
        elif b["close"].collidepoint(pos):
            self.bk_close()

    def bk_copy(self):
        """Duplicate the open book. Costs one empty Book from the inventory (creative: free)."""
        st = self.bk_stack
        pages = book_pages(st)
        if not any(pages):
            self.say("Write something first - there is nothing to copy.")
            return
        blank = None
        if not self.creative:
            for i, o in enumerate(self.inv):
                if o and o[0] == BOOK and o is not st and not any(book_pages(o)):
                    blank = i
                    break
            if blank is None:
                self.say("You need an empty Book in your inventory to make a copy.")
                return
        copy = [BOOK, 1, {"pages": list(pages)}]
        if blank is not None:
            self.inv[blank] = None
        self.give_or_drop(copy)
        self.say("Copied the book (%d pages)." % len(pages))

    def bk_key(self, key, ch):
        st = self.bk_stack
        if not st:
            self.close_ui()
            return
        pages = book_pages(st)
        self.bk_page = max(0, min(self.bk_page, len(pages) - 1))
        if key == pygame.K_ESCAPE:
            self.bk_close()
        elif key == pygame.K_BACKSPACE:
            pages[self.bk_page] = pages[self.bk_page][:-1]
        elif key == pygame.K_PAGEUP:
            self.bk_page = max(0, self.bk_page - 1)
        elif key == pygame.K_PAGEDOWN:
            self.bk_page = min(len(pages) - 1, self.bk_page + 1)
        elif key == pygame.K_RETURN:
            ch = "\n"
        if ch and (ch == "\n" or (ch.isprintable() and ch != "")) and len(pages[self.bk_page]) < BOOK_PAGE_CHARS:
            pages[self.bk_page] += ch

    def bk_draw(self):
        scr = self.screen
        dim = pygame.Surface((SW, SH), pygame.SRCALPHA)
        dim.fill((0, 0, 0, 140))
        scr.blit(dim, (0, 0))
        pr, text, btns = self.bk_rects()
        st = self.bk_stack
        pages = book_pages(st) if st else [""]
        self.bk_page = max(0, min(self.bk_page, len(pages) - 1))
        pygame.draw.rect(scr, (120, 55, 50), pr)
        pygame.draw.rect(scr, (60, 25, 25), pr, 4)
        self.txt("Book  -  page %d / %d" % (self.bk_page + 1, len(pages)), (pr.x + 20, pr.y + 12), (255, 235, 200))
        pygame.draw.rect(scr, (238, 228, 192), text)
        pygame.draw.rect(scr, (150, 130, 90), text, 2)
        page = pages[self.bk_page]
        cursor = "|" if int(pygame.time.get_ticks() / 450) % 2 == 0 else ""
        lines = wrap_text(self.small, page + cursor, text.w - 16)
        for i, ln in enumerate(lines[:19]):
            self.txt(ln, (text.x + 8, text.y + 6 + i * 18), (45, 32, 20), self.small)
        self.txt("%d / %d characters on this page   (type to write, PageUp/PageDown or < > to turn pages)"
                 % (len(page), BOOK_PAGE_CHARS), (pr.x + 20, text.bottom + 6), (255, 235, 200), self.small)
        labels = {"prev": "<", "next": ">", "add": "+ Page", "del": "- Page", "copy": "Copy book", "close": "Close"}
        mpos = self.mouse_pos()
        for n, r in btns.items():
            hot = r.collidepoint(mpos)
            pygame.draw.rect(scr, (170, 120, 90) if hot else (135, 90, 65), r)
            pygame.draw.rect(scr, (255, 235, 200), r, 2)
            self.txt(labels[n], r.center, (255, 245, 225), self.small, center=True)

    def spawn_drop(self, x, y, i, n, dur=None, vx=None, vy=-4.0, delay=0.0):
        if i in NO_ITEM:
            return
        if vx is None:
            vx = self.rnd.uniform(-2, 2)
        self.drops.append(Drop(x, y, i, n, dur, vx, vy, delay))

    def give_or_drop(self, s):
        t = list(s)
        put_into(self.inv, range(36), t)
        if t[1] > 0:
            self.spawn_drop(self.p.x + 0.3, self.p.y + 0.5, t[0], t[1], t[2],
                            vx=self.p.face * 4, delay=1.0)

    def armor_points(self):
        return sum(ITEMS[s[0]]["defense"] for s in self.armor if s)

    def prot_levels(self):
        return sum(ench_of(st).get("protection", 0) for st in self.armor if st)

    def dur_hit(self, st, n=1):
        """Wear a stack down by n (Unbreaking can save points). True once it is used up."""
        u = ench_of(st).get("unbreaking", 0)
        if u:
            n = sum(1 for _ in range(n) if self.rnd.random() >= u / (u + 1.0))
        if n:
            dur_sub(st, n)
        return st[2] <= 0

    def wear_armor(self, raw):
        n = max(1, int(raw / 4))
        for i, st in enumerate(self.armor):
            if st:
                if self.dur_hit(st, n):
                    self.armor[i] = None
                    self.say("Your %s broke!" % ITEMS[st[0]]["name"])

    def take_arrow(self):
        if self.creative:
            return True
        for i, st in enumerate(self.inv):
            if st and st[0] == ARROW:
                st[1] -= 1
                if st[1] <= 0:
                    self.inv[i] = None
                return True
        return False

    def shoot_arrow(self, power):
        if not self.take_arrow():
            self.say("You need arrows (coal over a stick makes 4).")
            return
        p = self.p
        ox, oy = p.x + p.w / 2, p.y + 0.6
        wx, wy, _, _ = self.mouse_world()
        dx, dy = wx - ox, wy - oy
        d = math.hypot(dx, dy)
        if d < 0.01:
            dx, dy, d = p.face, 0.0, 1.0
        speed = 10 + 26 * power
        arw = Arrow(ox, oy, dx / d * speed, dy / d * speed, power)
        arw.bonus = ench_of(self.held()).get("power", 0)
        self.arrows.append(arw)
        self.wear(1)
        p.swing = 0.25

    def arrow_hit(self, e, a):
        e.hp -= (3 + 6 * a.power) * (1 + 0.25 * a.bonus)
        e.flash = 0.25
        if e.kind == "cow":
            e.panic = 4.0
        elif e.kind == "pigman":
            for o in self.zombies:
                if o.kind == "pigman" and abs(o.x - e.x) < 20:
                    o.angry = True
        if e.kind not in ("dragon", "crystal"):
            e.vx += 3.0 if a.vx > 0 else -3.0
            e.vy -= 2.0

    def update_arrows(self, dt):
        p = self.p
        bow = self.held() and self.held()[0] == BOW
        if self.ui is None and bow and not self.paused and self.mouse_buttons()[2]:
            self.bow_on = True
            self.bow_t = min(1.0, self.bow_t + dt)
        elif self.bow_on:
            if self.ui is None and bow and self.bow_t >= 0.2:
                self.shoot_arrow(self.bow_t)
            self.bow_on, self.bow_t = False, 0.0
        for a in self.arrows[:]:
            if a not in self.arrows:
                continue
            a.age += dt
            if a.stuck:
                if a.age > 8:
                    self.arrows.remove(a)
                continue
            n = max(1, int(math.ceil(dt / 0.012)))
            sd = dt / n
            for _ in range(n):
                a.vy += GRAVITY * 0.5 * sd
                nx, ny = a.x + a.vx * sd, a.y + a.vy * sd
                hit = next((e for e in self.zombies + self.cows + self.crystals + self.bosses
                            if e.x <= nx <= e.x + e.w and e.y <= ny <= e.y + e.h), None)
                if hit is not None:
                    self.arrows.remove(a)
                    self.arrow_hit(hit, a)
                    break
                if SOLID[self.world.get(math.floor(nx), math.floor(ny))]:
                    a.stuck, a.age = True, 0.0
                    break
                a.x, a.y = nx, ny
            else:
                if a.age > 12 or not -2 < a.x < WW + 2 or a.y > WH + 5:
                    self.arrows.remove(a)

    FW_COLORS = [(255, 80, 80), (255, 200, 60), (80, 200, 255), (120, 255, 120), (220, 120, 255), (255, 255, 255)]

    def has_elytra(self):
        st = self.armor[1]
        return bool(st and ITEMS[st[0]].get("glider"))

    def try_glide(self):
        p = self.p
        if (p.gliding or p.flying or p.on_ground or not self.has_elytra() or p.vy <= 0 or self.ui
                or touching(self.world, p, WATER) or touching(self.world, p, LAVA) or touching(self.world, p, LADDER)):
            return
        p.gliding = True
        p.glide_v = max(8.0, min(14.0, math.hypot(p.vx, p.vy)))
        p.glide_pitch, p.boost_t = -0.3, 0.0
        self.glide_wear = 0.0
        self.say("Gliding! W/Up pitch up, S/Down dive, A/D turn. Fireworks give a boost.", 4)

    def spawn_burst(self, x, y, col=None, n=40):
        cols = [col or self.rnd.choice(self.FW_COLORS), self.rnd.choice(self.FW_COLORS)]
        for _ in range(n):
            a, sp = self.rnd.uniform(0, 6.283), self.rnd.uniform(2.5, 9.0)
            life = self.rnd.uniform(0.8, 1.4)
            self.sparks.append([x, y, math.cos(a) * sp, math.sin(a) * sp, life, life, self.rnd.choice(cols)])
        del self.sparks[:-900]

    def use_firework(self):
        if self.fw_cd > 0:
            return
        p = self.p
        self.fw_cd = 0.35
        self.consume_held()
        p.swing = 0.25
        if p.gliding:                                        # boost: thrust for a moment, bang when it burns out
            p.boost_t = 1.4
            p.glide_v = min(34.0, p.glide_v + 6.0)
            self.rockets.append(dict(follow=True, t=1.4, x=0.0, y=0.0, vx=0.0, vy=0.0))
        else:                                                # a rocket straight up
            self.rockets.append(dict(follow=False, t=self.rnd.uniform(0.9, 1.4), x=p.x + p.w / 2, y=p.y + 0.2,
                                     vx=self.rnd.uniform(-1.0, 1.0), vy=-14.0))

    def update_fireworks(self, dt):
        p = self.p
        self.fw_cd = max(0.0, self.fw_cd - dt)
        if p.gliding:
            self.glide_wear += dt
            if self.glide_wear >= 1.0:
                self.glide_wear = 0.0
                st = self.armor[1]
                if st:
                    if self.dur_hit(st, 1):
                        self.armor[1] = None
                        p.gliding = False
                        self.say("Your Elytra broke!")
        for r in self.rockets[:]:
            if r["follow"]:
                r["x"], r["y"] = p.x + p.w / 2, p.y + p.h / 2
                bx_, by_ = r["x"] - p.face * 0.3, r["y"] + 0.5
            else:
                r["x"] += r["vx"] * dt
                r["y"] += r["vy"] * dt
                bx_, by_ = r["x"], r["y"] + 0.3
            for _ in range(2):
                self.sparks.append([bx_, by_, self.rnd.uniform(-1, 1), self.rnd.uniform(0.5, 2.5), 0.45, 0.45,
                                    self.rnd.choice(((255, 190, 60), (255, 120, 40), (255, 240, 180)))])
            r["t"] -= dt
            if r["t"] <= 0:
                self.rockets.remove(r)
                self.spawn_burst(r["x"], r["y"])
        for sp in self.sparks[:]:
            sp[0] += sp[2] * dt
            sp[1] += sp[3] * dt
            sp[3] += 7.0 * dt
            sp[2] *= 0.985
            sp[4] -= dt
            if sp[4] <= 0:
                self.sparks.remove(sp)
        del self.sparks[:-900]

    def throw_pearl(self):
        if self.pearl_cd > 0:
            return
        p = self.p
        ox, oy = p.x + p.w / 2, p.y + 0.6
        wx, wy, _, _ = self.mouse_world()
        dx, dy = wx - ox, wy - oy
        d = math.hypot(dx, dy)
        if d < 0.01:
            dx, dy, d = p.face, 0.0, 1.0
        self.pearls.append(Pearl(ox, oy, dx / d * 22, dy / d * 22))
        self.consume_held()
        self.pearl_cd = 0.6
        p.swing = 0.25

    @staticmethod
    def box_free(w, x, y, bw, bh):
        if x < 0 or x + bw > WW or y < 0:
            return False
        for tx in range(math.floor(x), math.floor(x + bw - 1e-4) + 1):
            for ty in range(math.floor(y), math.floor(y + bh - 1e-4) + 1):
                if SOLID[w.get(tx, ty)]:
                    return False
        return True

    def pearl_land(self, cx, cy):
        p, w = self.p, self.world
        for yy in (cy - p.h, cy - p.h / 2, cy - p.h + 0.5, cy - p.h - 0.5):
            for dx in (0.0, -0.4, 0.4, -0.8, 0.8):
                x, y = cx - p.w / 2 + dx, yy
                if self.box_free(w, x, y, p.w, p.h):
                    p.x, p.y = x, y
                    p.vx = p.vy = 0.0
                    p.air_peak = None
                    self.hurt(5, force=True, armor=False)       # like the real thing: 2.5 hearts
                    return True
        self.say("The pearl shattered: no room to land.")
        return False

    # ----- pressure plates, pistons, fishing -------------------------------- #
    def plates_pressed(self):
        w, act = self.world, set()
        ents = ([] if self.remote else [(self.p, True)]) + [(e, True) for e in self.zombies + self.cows] \
            + [(d, False) for d in self.drops]
        for e, stone_ok in ents:
            yc = math.floor(e.y + e.h - 1e-3)
            if e.y + e.h <= yc + 0.7:                       # feet must be low in the plate's cell
                continue
            for x in range(math.floor(e.x), math.floor(e.x + e.w - 1e-4) + 1):
                b = w.get(x, yc)
                if b == WOOD_PLATE or (b == STONE_PLATE and stone_ok):
                    act.add((x, yc))
        floaters = [(pr.x, pr.y, False) for pr in self.pearls if pr.float_t is not None]
        b = self.bobber
        if b and b.get("dim") == self.dim:
            floaters.append((b["x"], b["y"], True))             # the bobber presses stone plates too
        for fx, fy, stone_ok in floaters:
            for cy in (math.floor(fy), math.floor(fy) + 1):
                pb = w.get(math.floor(fx), cy)
                if pb == WOOD_PLATE or (stone_ok and pb == STONE_PLATE):
                    act.add((math.floor(fx), cy))
        return act

    @staticmethod
    def powered_cells(active):
        """Cells a pressed plate powers: its three free sides and the sides of the block it sits on."""
        P = set()
        for x, y in active:
            P.update(((x - 1, y), (x + 1, y), (x, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x, y + 2)))
        return P

    def scan_torches(self):
        """Redstone torches near the player and what each is attached to (below first, then a side wall)."""
        w = self.world
        cx_, cy_ = self.scan_center or (self.p.x, self.p.y)
        out, lout = [], []
        x0, x1 = max(0, int(cx_) - 56), min(WW, int(cx_) + 57)
        y0, y1 = max(0, int(cy_) - 40), min(WH, int(cy_) + 41)
        for x in range(x0, x1):
            col = w.cols[x]
            y = col.find(REDSTONE_TORCH, y0, y1)
            while y != -1:
                if SOLID[w.get(x, y + 1)]:
                    out.append((x, y, x, y + 1))
                elif SOLID[w.get(x - 1, y)]:
                    out.append((x, y, x - 1, y))
                elif SOLID[w.get(x + 1, y)]:
                    out.append((x, y, x + 1, y))
                else:                                      # nothing to hang on: it pops off
                    w.set(x, y, AIR)
                    self.spawn_drop(x + 0.35, y + 0.35, REDSTONE_TORCH, 1)
                y = col.find(REDSTONE_TORCH, y + 1, y1)
            for lb in (LEVER, LEVER_ON) + BUTTONS + tuple(BUTTON_OFF):
                y = col.find(lb, y0, y1)
                while y != -1:
                    if SOLID[w.get(x, y + 1)]:
                        lout.append((x, y, x, y + 1))
                    elif SOLID[w.get(x - 1, y)]:
                        lout.append((x, y, x - 1, y))
                    elif SOLID[w.get(x + 1, y)]:
                        lout.append((x, y, x + 1, y))
                    else:                                  # nothing to hold it: it pops off
                        w.set(x, y, AIR)
                        self.spawn_drop(x + 0.35, y + 0.35, ITEMS[lb].get("drop", lb), 1)
                    if lb in BUTTON_OFF and (self.dim, x, y) not in self.buttons_on:      # a pressed button from a save: let it pop up
                        self.buttons_on[(self.dim, x, y)] = 0.5
                    y = col.find(lb, y + 1, y1)
            for od_, ob_ in enumerate(OBSERVER_BLK):
                y = col.find(ob_, y0, y1)
                while y != -1:
                    key = (self.dim, x, y)
                    if self.observers.get(key, (None,))[0] != od_:
                        self.observers[key] = [od_, w.get(x + DIRV[od_][0], y + DIRV[od_][1])]
                    y = col.find(ob_, y + 1, y1)
            y = col.find(REDSTONE_DUST, y0, y1)
            while y != -1:
                if not SOLID[w.get(x, y + 1)]:             # the ground under the dust is gone
                    w.set(x, y, AIR)
                    self.spawn_drop(x + 0.35, y + 0.35, REDSTONE_DUST, 1)
                y = col.find(REDSTONE_DUST, y + 1, y1)
        self.torch_list = out
        self.lever_lists[self.dim] = lout

    def observer_step(self, dt, P):
        """An observer pulses out of its back whenever the block in front of its face changes."""
        w, dim = self.world, self.dim
        for key in [k for k in self.observers if k[0] == dim]:
            _, x, y = key
            b = w.get(x, y)
            if b not in OBSERVER_BLK:
                del self.observers[key]
                self.obs_pulse.pop(key, None)
                continue
            d = OBSERVER_BLK.index(b)
            dx, dy = DIRV[d]
            fb = w.get(x + dx, y + dy)
            rec = self.observers[key]
            if rec[0] != d:
                rec[0], rec[1] = d, fb
            elif rec[1] != fb:
                rec[1] = fb
                self.obs_pulse[key] = OBS_PULSE
            t = self.obs_pulse.get(key)
            if t is None:
                continue
            t -= dt
            if t <= 0:
                del self.obs_pulse[key]
                continue
            self.obs_pulse[key] = t
            back = (x - dx, y - dy)
            P.add(back)
            if SOLID[w.get(back[0], back[1])]:             # a block it points into passes the signal on
                P.update(c for c in ((back[0] - 1, back[1]), (back[0] + 1, back[1]), (back[0], back[1] - 1),
                                     (back[0], back[1] + 1)) if c != (x, y))

    def dust_links(self, x, y):
        """Dust cells wired to the dust at (x, y): beside it, and one step up or down a block."""
        w, out = self.world, []
        for dx in (-1, 1):
            nx = x + dx
            if w.get(nx, y) == REDSTONE_DUST:
                out.append((nx, y))
            if w.get(nx, y - 1) == REDSTONE_DUST and not SOLID[w.get(x, y - 1)]:
                out.append((nx, y - 1))
            if w.get(nx, y + 1) == REDSTONE_DUST and not SOLID[w.get(nx, y)]:
                out.append((nx, y + 1))
        return out

    def dust_flood(self, P):
        """Signal strength of every powered dust cell: 15 where a source touches it, one less per step."""
        w = self.world
        lv = {c: 15 for c in P if w.get(c[0], c[1]) == REDSTONE_DUST}
        frontier = list(lv)
        while frontier:
            nxt = []
            for x, y in frontier:
                l = lv[(x, y)] - 1
                if l <= 0:
                    continue
                for c in self.dust_links(x, y):
                    if lv.get(c, 0) < l:
                        lv[c] = l
                        nxt.append(c)
            frontier = nxt
        return lv

    def update_machines(self, dt):
        w = self.world
        self.active_plates = act = self.plates_pressed()
        P = self.powered_cells(act)
        self.torch_scan_t -= dt
        if self.torch_scan_t <= 0:
            self.torch_scan_t = 0.1
            self.scan_torches()
        pblock = {(x, y + 1) for x, y in act}              # the block under a pressed plate is powered
        dim = self.dim
        self.dust_t[dim] = self.dust_t.get(dim, 0.0) - dt  # dust feeds back into torches one 0.1 s tick late
        if self.dust_t[dim] <= 0:
            self.dust_t[dim] = 0.1
            self.dust_cache[dim] = self.dust_live.get(dim, set())
        pblock |= self.dust_cache.get(dim, set())
        for key in [k for k in self.buttons_on if k[0] == dim]:                # pressed buttons pop back up
            _, bx_, by_ = key
            bb = w.get(bx_, by_)
            if bb not in BUTTON_OFF:
                del self.buttons_on[key]
                continue
            self.buttons_on[key] -= dt
            if self.buttons_on[key] <= 0:
                del self.buttons_on[key]
                w.set(bx_, by_, BUTTON_OFF[bb])
        levers = [(lx, ly, ax, ay) for lx, ly, ax, ay in self.lever_lists.get(dim, ()) if w.get(lx, ly) in POWER_ON]
        pblock.update((ax, ay) for _, _, ax, ay in levers)  # the block a lever hangs on is powered while it is on
        self.torch_on = set()
        for tx, ty, ax, ay in self.torch_list:             # a torch is ON unless its block is powered (NOT gate)
            if w.get(tx, ty) != REDSTONE_TORCH or (ax, ay) in pblock:
                continue
            self.torch_on.add((tx, ty))
            P.update(c for c in ((tx - 1, ty), (tx + 1, ty), (tx, ty - 1), (tx, ty + 1)) if c != (ax, ay))
            if SOLID[w.get(tx, ty - 1)]:                   # a block sitting on a lit torch powers what touches it
                P.update(((tx - 1, ty - 1), (tx + 1, ty - 1), (tx, ty - 2)))
        for lx, ly, ax, ay in levers:                      # an ON lever powers its sides and what touches its block
            P.update(c for c in ((lx - 1, ly), (lx + 1, ly), (lx, ly - 1), (lx, ly + 1)) if c != (ax, ay))
            P.update(c for c in ((ax - 1, ay), (ax + 1, ay), (ax, ay - 1), (ax, ay + 1)) if c != (lx, ly))
        self.observer_step(dt, P)
        lv = self.dust_flood(P)
        self.dust_lvs[dim] = lv
        live = set()
        for (dx_, dy_) in lv:                              # powered dust powers its sides and the block under it
            P.update(((dx_ - 1, dy_), (dx_ + 1, dy_), (dx_, dy_ + 1)))
            live.add((dx_, dy_ + 1))
        self.dust_live[dim] = live
        for key in [k for k in self.ext_pistons if k[0] == self.dim]:        # extended pistons
            _, x, y = key
            d = self.ext_pistons[key]
            sticky, d = d >= 4, d % 4
            pb_, pe_, ph_ = piston_ids(sticky)
            hx, hy = x + DIRV[d][0], y + DIRV[d][1]
            if w.get(x, y) != pe_[d]:                                         # base was mined or blown up
                del self.ext_pistons[key]
                if w.get(hx, hy) == ph_[d]:
                    w.set(hx, hy, AIR)
            elif w.get(hx, hy) != ph_[d]:                                     # head was mined: base resets
                w.set(x, y, pb_[d])
                del self.ext_pistons[key]
            elif (x, y) not in P:
                self.piston_retract(x, y, d, sticky)
        for (x, y) in sorted(P):
            b = w.get(x, y)
            if b in PIST_BASE_OF:
                self.piston_extend(x, y, *PIST_BASE_OF[b])
            elif b == TNT:
                self.ignite_tnt(x, y)
            elif b == TRAPDOOR:                                               # powered trapdoors open
                self.toggle_trapdoor(x, y)
                self.plate_traps.add((self.dim, x, y))
            elif b in (DOOR_CB, DOOR_CT):                                     # closed door: pressure opens it
                bottom = y if b == DOOR_CB else y + 1
                self.toggle_door(x, y)
                self.plate_doors.add((self.dim, x, bottom))
        for key in [k for k in self.plate_traps if k[0] == self.dim]:        # trapdoors we opened close again
            _, x, y = key
            if w.get(x, y) != TRAPDOOR_OPEN:
                self.plate_traps.discard(key)
            elif (x, y) not in P and self.toggle_trapdoor(x, y, silent=True):
                self.plate_traps.discard(key)
        for key in [k for k in self.plate_doors if k[0] == self.dim]:        # doors we opened close again
            _, x, by_ = key
            b = w.get(x, by_)
            if b not in DOOR_TOGGLE:
                self.plate_doors.discard(key)
                continue
            if (x, by_) in P or (x, by_ - 1) in P:
                continue
            if b == DOOR_OB:
                box = Entity(x, by_ - 1, 1, 2)
                if (not self.remote and overlap(box, self.p)) or any(overlap(box, z) for z in self.zombies + self.cows):
                    continue
                self.toggle_door(x, by_)
            self.plate_doors.discard(key)

    def piston_group(self, start, dx, dy, pushing):
        """Blocks that move together: the pushed chain, plus everything stuck to a slime block.
        Returns {cell: block}, or None when something immovable is in the way (or it is over the limit)."""
        w = self.world
        group, work = {}, list(start)
        while work:
            c = work.pop()
            if c in group:
                continue
            if not (0 <= c[0] < WW and 0 <= c[1] < WH):
                return None
            b = w.get(c[0], c[1])
            if b in IMMOVABLE:
                return None
            group[c] = b
            if len(group) > PISTON_LIMIT:
                return None
            if pushing:                                    # whatever is in front of a moving block gets pushed too
                f = (c[0] + dx, c[1] + dy)
                if not (0 <= f[0] < WW and 0 <= f[1] < WH):
                    return None
                if w.get(f[0], f[1]) not in FREE_PUSH and f not in group:
                    work.append(f)
            if b == SLIME_BLOCK:                           # sticky: the 4 neighbours come along
                for ox, oy in DIRV:
                    n = (c[0] + ox, c[1] + oy)
                    nb = w.get(n[0], n[1])
                    if n not in group and nb not in FREE_PUSH and n not in self.piston_cells:
                        work.append(n)
        return group

    def piston_move(self, group, dx, dy):
        """Move every block of the group one cell along (dx, dy); soft blocks in the way drop as items."""
        w = self.world
        for c in group:
            w.set(c[0], c[1], AIR)
        for c, b in group.items():
            n = (c[0] + dx, c[1] + dy)
            if n not in group:
                old = w.get(n[0], n[1])
                if old in SOFT_PUSH:
                    self.spawn_drop(n[0] + 0.35, n[1] + 0.35, ITEMS[old].get("drop", old), 1)
        for c, b in group.items():
            w.set(c[0] + dx, c[1] + dy, b)

    def piston_extend(self, x, y, d, sticky=False):
        w = self.world
        dx, dy = DIRV[d]
        hx, hy = x + dx, y + dy
        if not (0 <= hx < WW and 0 <= hy < WH):
            return False
        pb_, pe_, ph_ = piston_ids(sticky)
        self.piston_cells = {(x, y)}                       # the piston itself never gets dragged along
        group = {}
        if w.get(hx, hy) not in FREE_PUSH:
            group = self.piston_group([(hx, hy)], dx, dy, True)
            if group is None:
                return False
        elif w.get(hx, hy) in SOFT_PUSH:
            self.spawn_drop(hx + 0.35, hy + 0.35, ITEMS[w.get(hx, hy)].get("drop", w.get(hx, hy)), 1)
        line = all(c == (hx + dx * i, hy + dy * i) for i, c in enumerate(sorted(group, key=lambda c: (c[0] - hx) * dx + (c[1] - hy) * dy)))
        self.piston_move(group, dx, dy)
        w.set(hx, hy, ph_[d])
        w.set(x, y, pe_[d])
        self.ext_pistons[(self.dim, x, y)] = d + (4 if sticky else 0)
        if line and SLIME_BLOCK not in group.values():
            self.shove_entities(hx, hy, len(group), dx, dy)
        else:
            self.shove_group(hx, hy, group, dx, dy)
        return True

    def piston_retract(self, x, y, d, sticky=False):
        w = self.world
        pb_, pe_, ph_ = piston_ids(sticky)
        hx, hy = x + DIRV[d][0], y + DIRV[d][1]
        if w.get(hx, hy) == ph_[d]:
            w.set(hx, hy, AIR)
        if w.get(x, y) == pe_[d]:
            w.set(x, y, pb_[d])
        self.ext_pistons.pop((self.dim, x, y), None)
        if sticky:                                         # a sticky piston drags the block (and slime stuff) back with it
            dx, dy = DIRV[d]
            f = (hx + dx, hy + dy)
            if w.get(hx, hy) == AIR and w.get(f[0], f[1]) not in FREE_PUSH and w.get(f[0], f[1]) not in IMMOVABLE:
                self.piston_cells = {(x, y), (hx, hy)}
                group = self.piston_group([f], dx, dy, False)
                if group is not None:
                    free = all((c[0] - dx, c[1] - dy) in group or w.get(c[0] - dx, c[1] - dy) in FREE_PUSH for c in group)
                    if free:
                        self.piston_move(group, -dx, -dy)

    def shove_group(self, hx, hy, group, dx, dy):
        """Entities inside the head or any moved block are thrown clear along the push direction."""
        cells = {(c[0] + dx, c[1] + dy) for c in group} | {(hx, hy)}
        for e in ([] if self.remote else [self.p]) + self.zombies + self.cows + self.drops:
            def hit():
                return any(e.x < cx + 1 and e.x + e.w > cx and e.y < cy + 1 and e.y + e.h > cy for cx, cy in cells)
            if not hit():
                continue
            ox, oy = e.x, e.y
            for _ in range(16):
                if not hit():
                    break
                e.x += dx
                e.y += dy
            if dx:
                e.vx, e.vy = dx * 6.0, -3.0
            else:
                e.vy = 9.0 if dy > 0 else -10.0
            if e is self.p or hasattr(e, "hp"):
                if hit() or not self.box_free(self.world, e.x, e.y, e.w, e.h):
                    e.x, e.y = ox, oy

    def shove_entities(self, hx, hy, n, dx, dy):
        """Anything now overlapping the head or the pushed blocks is thrown clear of them."""
        fx, fy = hx + dx * n, hy + dy * n                  # far end of the pushed line
        for e in ([] if self.remote else [self.p]) + self.zombies + self.cows + self.drops:
            hit = any(e.x < hx + dx * i + 1 and e.x + e.w > hx + dx * i and e.y < hy + dy * i + 1
                      and e.y + e.h > hy + dy * i for i in range(n + 1))
            if not hit:
                continue
            ox, oy = e.x, e.y
            if dx:
                e.x = fx + 1.02 if dx > 0 else fx - e.w - 0.02
                e.vx, e.vy = dx * 6.0, -3.0
            else:
                e.y = fy + 1.02 if dy > 0 else fy - e.h - 0.02
                e.vy = 9.0 if dy > 0 else -10.0
            if e is self.p or hasattr(e, "hp"):
                if not self.box_free(self.world, e.x, e.y, e.w, e.h):
                    e.x, e.y = ox, oy

    def place_piston(self, bx, by, b, observer=False, sticky=False):
        w = self.world
        if b not in (AIR, LAVA, WATER):
            return
        box = Entity(bx, by, 1, 1)
        if overlap(box, self.p) or any(overlap(box, z) for z in self.zombies + self.cows):
            return
        if not any(SOLID[w.get(bx + dx, by + dy)] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            return
        dx = bx + 0.5 - (self.p.x + 0.3)
        dy = by + 0.5 - (self.p.y + 0.9)
        d = (1 if dx > 0 else 0) if abs(dx) >= abs(dy) else (3 if dy > 0 else 2)     # faces away from you
        if observer:                                       # the face looks at you, the signal leaves the back
            d ^= 1
            w.set(bx, by, OBSERVER_BLK[d])
            self.observers[(self.dim, bx, by)] = [d, w.get(bx + DIRV[d][0], by + DIRV[d][1])]
        else:
            w.set(bx, by, (STICKY_BASE if sticky else PISTON_BASE)[d])
        self.p.swing = 0.2
        self.consume_held()

    def use_rod(self):
        """Right-click: cast the bobber anywhere (it is a real entity), or reel it back in."""
        p = self.p
        if self.bobber:
            self.reel_in()
            return
        ox, oy = p.x + p.w / 2, p.y + 0.6
        wx, wy, _, _ = self.mouse_world()
        dx, dy = wx - ox, wy - oy
        d = math.hypot(dx, dy)
        if d < 0.01:
            dx, dy, d = float(p.face), 0.0, 1.0
        if d > 14.0:                                       # throw at most 14 blocks
            dx, dy, d = dx * 14.0 / d, dy * 14.0 / d, 14.0
        T = max(0.25, min(1.2, d / 12.0))                  # flight time: lands on the cursor if nothing is in the way
        g = GRAVITY * 0.6
        vx, vy = dx / T, dy / T - 0.5 * g * T
        if abs(dx) > 0.3:                                  # refine: make it come down on the spot you aimed at
            for _ in range(6):
                moved = self.bobber_landing(ox, oy, vx, vy) - ox
                if abs(moved) < 0.05 or abs(moved - dx) < 0.1:
                    break
                vx *= max(0.3, min(2.0, dx / moved))
        self.bobber = dict(x=ox, y=oy, vx=vx, vy=vy, mode="air", surf=0.0,
                           t=0.0, bite=0.0, window=0.0, dim=self.dim)
        p.swing = 0.3
        self.say("Cast! Right-click again to reel it in.", 3)

    def bobber_landing(self, x, y, vx, vy):
        """x where a thrown bobber first meets water or a solid block (dry run of its flight)."""
        w, g = self.world, GRAVITY * 0.6
        for _ in range(300):
            vy += g * 0.02
            nx, ny = x + vx * 0.02, y + vy * 0.02
            c = w.get(math.floor(nx), math.floor(ny))
            if c == WATER:
                return nx
            if SOLID[c]:
                return x
            x, y = nx, ny
        return x

    def update_fishing(self, dt):
        b = self.bobber
        if not b or b.get("dim") != self.dim:             # it stays put in its own dimension
            return
        w, p = self.world, self.p
        n = max(1, int(math.ceil(dt / 0.015)))
        sd = dt / n
        for _ in range(n):
            if b["mode"] == "water":
                sc = b["surf"]
                if w.get(math.floor(b["x"]), math.floor(sc)) != WATER:     # its water is gone: it falls
                    b["mode"], b["vy"] = "air", 0.0
                    continue
                b["vx"] *= max(0.0, 1.0 - 4.0 * sd)
                b["x"] += b["vx"] * sd
                b["y"] = sc + 0.15
            elif b["mode"] == "rest":
                if not SOLID[w.get(math.floor(b["x"]), math.floor(b["y"] + 0.2))]:    # the ground went away
                    b["mode"], b["vy"] = "air", 0.0
            else:
                b["vy"] += GRAVITY * 0.6 * sd
                nx, ny = b["x"] + b["vx"] * sd, b["y"] + b["vy"] * sd
                cell = w.get(math.floor(nx), math.floor(ny))
                if cell == WATER:
                    sc = math.floor(ny)
                    while w.get(math.floor(nx), sc - 1) == WATER:
                        sc -= 1
                    b.update(mode="water", surf=float(sc), x=nx, y=sc + 0.15, vx=b["vx"] * 0.2, vy=0.0,
                             t=0.0, bite=self.rnd.uniform(3.0, 8.0), window=0.0)
                elif SOLID[cell]:
                    if SOLID[w.get(math.floor(nx), math.floor(b["y"]))]:      # a wall: slide down it
                        nx, b["vx"] = b["x"], 0.0
                    if SOLID[w.get(math.floor(nx), math.floor(ny))]:           # floor or ceiling
                        if b["vy"] > 0:
                            b.update(mode="rest", y=math.floor(ny) - 0.12, vx=0.0, vy=0.0)
                        else:
                            b["vy"] = 0.0
                        ny = b["y"]
                    b["x"], b["y"] = nx, ny
                else:
                    b["x"], b["y"] = nx, ny
                if b["y"] > WH + 5 or not -2 < b["x"] < WW + 2:
                    self.bobber = None
                    return
        if b["mode"] != "water" or self.remote:
            return
        s = self.held()
        if not (s and s[0] == FISHING_ROD) or math.hypot(b["x"] - (p.x + 0.3), b["y"] - (p.y + 0.9)) > 16:
            return                                        # no bites unless you hold the rod nearby; the bobber just stays
        b["t"] += dt
        if b["window"] > 0:
            b["window"] -= dt
            if b["window"] <= 0:                          # too slow: it got away
                b["bite"] = b["t"] + self.rnd.uniform(3.0, 8.0)
        elif b["t"] >= b["bite"]:
            b["window"] = 1.2
            self.say("A fish is biting! Reel it in!", 2)

    def reel_in(self):
        b, p = self.bobber, self.p
        self.bobber = None
        p.swing = 0.3
        if b.get("dim") != self.dim:
            self.remote_hot[b["dim"]] = [b["x"], b["y"], 8.0]      # its plate lets go: the machines there react
            self.say("You reel in the bobber from the other dimension.")
            return
        if b["mode"] != "water" or b["window"] <= 0:
            self.say("You reel the bobber in." if b["mode"] != "water" else "Nothing yet... you reel the line in.")
            return
        r = self.rnd.random()
        item, n = ((RAW_COD, 1) if r < 0.50 else (RAW_SALMON, 1) if r < 0.75 else (STRING, 1) if r < 0.83
                   else (STICK, 2) if r < 0.88 else (LEATHER, 1) if r < 0.93 else (XP_BOTTLE, 1) if r < 0.97 else (RAW_COD, 2))
        self.spawn_drop(b["x"], b["y"] - 0.1, item, n, None, vx=(p.x + 0.3 - b["x"]) * 1.3, vy=-7.0)
        self.gain_xp(self.rnd.randint(1, 3))
        self.wear(1)
        self.say("You caught %s!" % ITEMS[item]["name"])

    def run_in_dim(self, dim, fn):
        """Run fn with another dimension's entities and world swapped in (the player is left out of it)."""
        keep = {k: getattr(self, k) for k in self.DIM_KEYS}
        keep.update(world=self.world, dim=self.dim, torch_list=self.torch_list, torch_on=self.torch_on,
                    torch_scan_t=self.torch_scan_t, active_plates=self.active_plates)
        st = self.dstate[dim]
        for k in self.DIM_KEYS:
            setattr(self, k, st[k])
        self.world, self.dim = self.worlds[dim], dim
        self.torch_list, self.torch_on, self.torch_scan_t, self.active_plates = [], set(), 0.0, set()
        fl = [(x.x, x.y) for x in self.pearls if x.float_t is not None]
        if self.bobber and self.bobber.get("dim") == dim:
            fl.append((self.bobber["x"], self.bobber["y"]))
        hot = self.remote_hot.get(dim)
        ext = [(k[1], k[2]) for k in self.ext_pistons if k[0] == dim]
        self.scan_center = fl[0] if fl else ((hot[0], hot[1]) if hot else (ext[0] if ext else None))
        self.remote = True
        try:
            fn()
        finally:
            for k in self.DIM_KEYS:
                st[k] = getattr(self, k)
                setattr(self, k, keep[k])
            self.world, self.dim = keep["world"], keep["dim"]
            self.torch_list, self.torch_on = keep["torch_list"], keep["torch_on"]
            self.torch_scan_t, self.active_plates = keep["torch_scan_t"], keep["active_plates"]
            self.remote, self.scan_center = False, None

    def update_remote(self, dt):
        """Floating pearls and the bobber keep working in other dimensions (plates, pistons, torches...)."""
        for d in sorted(self.dstate):
            if d == self.dim or d not in self.worlds:
                continue
            hot = self.remote_hot.get(d)
            if hot:
                hot[2] -= dt
                if hot[2] <= 0:
                    del self.remote_hot[d]
            if not (self.dstate[d].get("pearls")                  # floating or falling pearls (a released one must land)
                    or (self.bobber and self.bobber.get("dim") == d)
                    or any(k[0] == d for k in self.ext_pistons)    # extended pistons must retract when released
                    or any(k[0] == d for k in self.obs_pulse)      # an observer pulse must finish
                    or any(k[0] == d for k in self.buttons_on)     # a pressed button must pop back up
                    or d in self.remote_hot):                      # something just changed over there (bobber reeled in...)
                continue
            self.run_in_dim(d, lambda: (self.update_machines(dt), self.update_pearls(dt), self.update_fishing(dt)))
            if self.pending_pearl:
                break
        if self.pending_pearl:                                  # a pearl came down in another dimension
            d, x, y = self.pending_pearl
            self.pending_pearl = None
            p = self.p
            old = (self.dim, p.x, p.y)
            self.switch_dim(d)
            if self.pearl_land(x, y):
                self.say("Your ender pearl pulls you through the dimensions!", 4)
            else:
                self.switch_dim(old[0])
                p.x, p.y = old[1], old[2]

    def update_pearls(self, dt):
        self.pearl_cd = max(0.0, self.pearl_cd - dt)
        for pr in self.pearls[:]:
            if pr not in self.pearls:
                continue
            n = max(1, int(math.ceil(dt / 0.015)))
            sd = dt / n
            for _ in range(n):
                if pr.float_t is not None:               # floating on water (works for a single block too)
                    if self.world.get(math.floor(pr.x), math.floor(pr.surf)) != WATER:
                        pr.float_t = None                # the water vanished: it falls and lands (stasis release)
                        continue
                    pr.float_t += sd
                    pr.age = 0.0
                    pr.vx *= max(0.0, 1.0 - 4.0 * sd)
                    pr.x += pr.vx * sd
                    pr.y = pr.surf + 0.12 + 0.04 * math.sin(pr.float_t * 9)
                    if pr.float_t > pr.PEARL_FLOAT_MAX:
                        self.pearls.remove(pr)
                        break
                    if (not self.remote and pr.float_t > pr.PEARL_PICKUP_DELAY
                            and math.hypot(pr.x - (self.p.x + 0.3), pr.y - (self.p.y + 0.9)) < 1.3):
                        self.pearls.remove(pr)                # no teleport: just pick it back up
                        self.give_or_drop([ENDER_PEARL, 1, None])
                        self.say("You picked the floating ender pearl back up.")
                        break
                    continue
                pr.vy += GRAVITY * 0.6 * sd
                nx, ny = pr.x + pr.vx * sd, pr.y + pr.vy * sd
                if self.world.get(math.floor(nx), math.floor(ny)) == WATER:
                    sc = math.floor(ny)
                    while self.world.get(math.floor(nx), sc - 1) == WATER:      # rise to the top of the water column
                        sc -= 1
                    pr.x, pr.surf = nx, float(sc)
                    pr.y, pr.vy, pr.float_t = pr.surf + 0.12, 0.0, 0.0
                    continue
                if SOLID[self.world.get(math.floor(nx), math.floor(ny))]:
                    self.pearls.remove(pr)
                    if self.remote:                          # landed in another dimension: pull the owner through
                        self.pending_pearl = (self.dim, pr.x, pr.y)
                    else:
                        self.pearl_land(pr.x, pr.y)
                    break
                pr.x, pr.y = nx, ny
            else:
                pr.age += dt
                if pr.age > 10 or not -2 < pr.x < WW + 2 or pr.y > WH + 5:
                    self.pearls.remove(pr)

    def eat(self):
        st = self.held()
        if self.food >= 20 and not self.creative:
            self.say("You're not hungry.")
            return
        self.food = min(20.0, self.food + ITEMS[st[0]]["food"])
        self.consume_held()
        self.p.swing = 0.3
        self.say("Yum! Hunger: %d/20" % int(self.food))

    def equip_held(self):
        st = self.held()
        slot = ARMOR_SLOTS.index(ITEMS[st[0]]["armor"])
        old = self.armor[slot]
        self.armor[slot] = st
        self.inv[self.sel] = old
        self.p.swing = 0.2
        self.say("Equipped %s." % ITEMS[st[0]]["name"])

    def hurt(self, dmg, force=False, armor=True):
        if self.creative or self.protect_t > 0:        # creative mode / Potion of Protection
            return
        p = self.p
        if p.invuln > 0 and not force:
            return
        pts = (self.armor_points() + self.prot_levels()) if armor else 0
        if pts:                                        # each armor point absorbs 4% (max 80%)
            raw = dmg
            dmg = raw * (1 - min(0.8, pts * 0.04))
            self.wear_armor(raw)
        p.hp -= dmg
        p.invuln = 0.6
        if p.hp <= 0:
            self.die()

    def die(self):
        p = self.p
        for i, s in enumerate(self.inv):
            if s:
                self.spawn_drop(p.x + 0.3, p.y + 0.5, s[0], s[1], s[2])
                self.inv[i] = None
        for i, s in enumerate(self.armor):
            if s:
                self.spawn_drop(p.x + 0.3, p.y + 0.5, s[0], s[1], s[2])
                self.armor[i] = None
        self.food, self.starve_t = 20.0, 0.0
        self.p.gliding = False
        self.pearls[:] = [x for x in self.pearls if x.float_t is not None]
        self.arrows.clear()
        self.close_ui()
        if self.dim != 0:
            self.switch_dim(0)
        p.x, p.y = self.spawn
        p.vx = p.vy = 0.0
        p.hp = 20
        p.air_peak = None
        self.zombies.clear()
        self.protect_t = 0.0
        self.xp = 0
        self.say("You died! Your items were dropped where you fell.", 5)

    # ----- input ----------------------------------------------------------- #
    def toggle_fullscreen(self):
        try:
            pygame.display.toggle_fullscreen()
            self.fullscreen = not self.fullscreen
        except Exception:                              # older pygame / driver: rebuild the window instead
            self.fullscreen = not self.fullscreen
            flags = pygame.SCALED | (pygame.FULLSCREEN if self.fullscreen else 0)
            self.screen = pygame.display.set_mode((SW, SH), flags)
        self.say("Fullscreen on (F11 to leave)" if self.fullscreen else "Fullscreen off")

    def on_key(self, k):
        if k == pygame.K_F11:                          # works everywhere: in game, menus and while paused
            self.toggle_fullscreen()
            return
        if self.paused:
            if k == pygame.K_ESCAPE:
                self.paused = False
            elif k == pygame.K_F5:
                self.toggle_creative()
            elif k == pygame.K_F6:
                self.save()
            elif k == pygame.K_x:
                self.quit()
            elif k == pygame.K_m:
                self.save()
                self.open_menu()
            return
        if k in (pygame.K_t, pygame.K_SLASH) and not self.ui:        # the command line
            self.open_cmd("/" if k == pygame.K_SLASH else "")
            return
        if k == pygame.K_SPACE and not self.ui:
            now = pygame.time.get_ticks()
            if self.creative and now - self.last_space < 300:
                self.p.flying = not self.p.flying
            else:
                self.try_glide()                  # a press in mid-air while falling opens the elytra
            self.last_space = now
        if k == pygame.K_ESCAPE:
            if self.ui:
                self.close_ui()
            else:
                self.paused = True
        elif k == pygame.K_e:
            if self.ui:
                self.close_ui()
            else:
                self.ui = "inv"
        elif pygame.K_1 <= k <= pygame.K_9:
            self.select(k - pygame.K_1)
        elif k == pygame.K_r and not self.ui and self.bobber:      # reel the bobber in with any item in hand
            self.reel_in()
        elif k == pygame.K_q and not self.ui:
            s = self.held()
            if s:
                self.spawn_drop(self.p.x + 0.3, self.p.y + 0.3, s[0], 1, s[2],
                                vx=self.p.face * 5, delay=1.0)
                s[1] -= 1
                if s[1] <= 0:
                    self.inv[self.sel] = None
        elif k == pygame.K_F5:
            self.toggle_creative()
        elif k == pygame.K_F6:
            self.save()
        elif k == pygame.K_F2:
            self.add_waypoint()
        elif k == pygame.K_F3:
            self.debug = not self.debug

    DIM_NAMES = {0: "Overworld", 1: "Nether", 2: "End"}
    MAX_WAYPOINTS = 14

    def add_waypoint(self):
        if not self.debug:
            self.say("Open the F3 menu first, then press F2 to save your coordinates.")
            return
        if len(self.waypoints) >= self.MAX_WAYPOINTS:
            self.say("The coordinate list is full - remove one with its [x] button.")
            return
        p = self.p
        self.waypoints.append(dict(x=int(math.floor(p.x + p.w / 2)), y=int(math.floor(p.y + p.h / 2)), dim=self.dim))
        self.say("Saved coordinates #%d." % len(self.waypoints))

    def waypoint_rows(self):
        """(index, text, remove-button rect) for each saved coordinate, laid out under the F3 lines.
        The teleport button sits right of the remove button (see tp_rect)."""
        y0 = 8 + 18 * 4 + 28            # just under the "Saved coordinates" heading
        rows = []
        for i, wp in enumerate(self.waypoints):
            text = "#%d  X %d  Y %d  %s" % (i + 1, wp["x"], wp["y"], self.DIM_NAMES.get(wp["dim"], "?"))
            rows.append((i, text, pygame.Rect(8 + 214, y0 + i * 20, 22, 17)))
        return rows

    @staticmethod
    def tp_rect(btn):
        return pygame.Rect(btn.right + 4, btn.y, 30, btn.h)

    def spot_ok(self, w, x, y):
        p = self.p
        if not self.box_free(w, x, y, p.w, p.h):
            return False
        for tx in range(math.floor(x), math.floor(x + p.w - 1e-4) + 1):
            for ty in range(math.floor(y), math.floor(y + p.h - 1e-4) + 1):
                if w.get(tx, ty) == LAVA:
                    return False
        return True

    def teleport_to_waypoint(self, i):
        wp = self.waypoints[i]
        p = self.p
        if wp["dim"] != self.dim:
            self.close_ui()
            self.switch_dim(wp["dim"])
            if wp["dim"] == 2:
                self.enter_end()
        w = self.world
        cx, base = wp["x"] + 0.5 - p.w / 2, wp["y"] - 0.4
        for up in range(0, 60):                              # if the spot is now blocked, go up to the first free one
            for dx in (0.0, -1.0, 1.0, -2.0, 2.0):
                if self.spot_ok(w, cx + dx, base - up * 0.5):
                    p.x, p.y = cx + dx, base - up * 0.5
                    p.vx = p.vy = 0.0
                    p.air_peak = None
                    p.flying = False
                    self.mining, self.mine_prog = None, 0.0
                    self.portal_t, self.portal_lock = 0.0, True
                    self.say("Teleported to #%d (%s)." % (i + 1, self.DIM_NAMES.get(wp["dim"], "?")))
                    return True
        self.say("Could not find a free spot at #%d." % (i + 1))
        return False

    def click_waypoint(self, pos):
        for i, _, btn in self.waypoint_rows():
            if self.tp_rect(btn).collidepoint(pos):
                self.no_mine = True
                self.teleport_to_waypoint(i)
                return True
            if btn.collidepoint(pos):
                del self.waypoints[i]
                self.no_mine = True                  # don't start mining with the same click
                return True
        return False

    def toggle_creative(self):
        self.creative = not self.creative
        self.p.flying = False
        if self.creative:
            self.p.hp, self.p.air = 20, 10.0
            self.say("Creative mode ON: double-tap Space to fly, E for the item list.", 5)
        else:
            self.say("Creative mode OFF.")

    PAL_COLS, PAL_VIS = 7, 12

    def pal_rows(self):
        return -(-len(CREATIVE_ITEMS) // self.PAL_COLS)

    def pal_vis(self):
        return min(self.pal_rows(), self.PAL_VIS)

    def pal_max_scroll(self):
        return max(0, self.pal_rows() - self.pal_vis())

    def palette_panel(self):
        h = 28 + self.pal_vis() * 44 + 56            # title, visible item rows, clear button
        return pygame.Rect(766, (SH - h) // 2, 330, h)

    def palette_rects(self):
        pp = self.palette_panel()
        self.pal_scroll = max(0, min(self.pal_max_scroll(), self.pal_scroll))
        a = self.pal_scroll * self.PAL_COLS
        return [(it, pygame.Rect(pp.x + 6 + (n % self.PAL_COLS) * 44, pp.y + 28 + (n // self.PAL_COLS) * 44, 40, 40))
                for n, it in enumerate(CREATIVE_ITEMS[a:a + self.pal_vis() * self.PAL_COLS])]

    def pal_track(self):
        pp = self.palette_panel()
        return pygame.Rect(pp.x + 6 + self.PAL_COLS * 44 + 2, pp.y + 28, 14, self.pal_vis() * 44 - 4)

    def pal_thumb(self):
        tr = self.pal_track()
        rows, vis = self.pal_rows(), self.pal_vis()
        th = max(28, int(tr.h * vis / float(rows)))
        mx = self.pal_max_scroll()
        ty = tr.y + (int((tr.h - th) * self.pal_scroll / float(mx)) if mx else 0)
        return pygame.Rect(tr.x, ty, tr.w, th)

    def pal_scroll_by(self, rows):
        self.pal_scroll = max(0, min(self.pal_max_scroll(), self.pal_scroll + rows))

    def pal_set_from_y(self, y):
        tr, th = self.pal_track(), self.pal_thumb().h
        frac = (y - tr.y - th / 2.0) / float(max(1, tr.h - th))
        self.pal_scroll = max(0, min(self.pal_max_scroll(), int(round(frac * self.pal_max_scroll()))))

    def clear_button(self):
        pp = self.palette_panel()
        return pygame.Rect(pp.x + 12, pp.bottom - 46, pp.w - 24, 34)

    def clear_inventory(self):
        self.inv = [None] * 36
        self.craft = [None] * len(self.craft)
        self.cursor = None
        self.clear_t = 0.0
        self.say("Inventory cleared.")

    def select(self, i):
        self.sel = i % 9
        self.name_t = 1.5

    def mouse_pos(self):
        return pygame.mouse.get_pos()

    def mouse_buttons(self):
        return pygame.mouse.get_pressed()

    def mouse_world(self):
        mx, my = self.mouse_pos()
        wx, wy = (mx + self.camx) / TILE, (my + self.camy) / TILE
        return wx, wy, int(math.floor(wx)), int(math.floor(wy))

    def in_reach(self, bx, by):
        return math.hypot(bx + 0.5 - (self.p.x + 0.3), by + 0.5 - (self.p.y + 0.9)) <= REACH

    def on_click(self, pos, button):
        if self.paused or button not in (1, 3) or self.cmd is not None:
            return
        if self.debug and not self.ui and button == 1 and self.click_waypoint(pos):
            return
        if self.ui:
            self.ui_click(pos, button)
        elif button == 1:
            self.try_attack()
        else:
            s = self.held()
            if self.bobber and s and s[0] == FISHING_ROD:       # reel in, even when aiming at a chest, door, table...
                self.reel_in()
                return
            _, _, bx, by = self.mouse_world()
            uses_block = (self.world.get(bx, by) in (TABLE, ENCHANT_TABLE, GRINDSTONE, FURNACE, CHEST, SHULKER_BOX, ENDER_CHEST) or self.world.get(bx, by) in DOOR_TOGGLE
                          or self.world.get(bx, by) in (TRAPDOOR, TRAPDOOR_OPEN, LEVER, LEVER_ON) + BUTTONS + tuple(BUTTON_OFF)) \
                and self.in_reach(bx, by)
            if s and s[0] in POTIONS and not uses_block:
                self.drink(s[0])
            elif s and "armor" in ITEMS[s[0]] and not uses_block:
                self.equip_held()
            elif s and "food" in ITEMS[s[0]] and not uses_block:
                self.eat()
            elif s and s[0] == BOOK and not uses_block:
                self.bk_open()
            elif s and s[0] == ENDER_PEARL and not uses_block:
                self.throw_pearl()
            elif s and s[0] == FIREWORK and not uses_block:
                self.use_firework()
            elif s and s[0] == FISHING_ROD and not uses_block:
                self.use_rod()
            else:
                self.right_click()

    def try_attack(self):
        if self.attack_cd > 0:
            return
        wx, wy, _, _ = self.mouse_world()
        for z in self.zombies + self.cows + self.crystals + self.bosses:
            if z.x <= wx <= z.x + z.w and z.y <= wy <= z.y + z.h:
                if math.hypot(z.x + z.w / 2 - (self.p.x + 0.3), z.y + z.h / 2 - (self.p.y + 0.9)) > 3.8 + z.w / 2 * (z.kind == "dragon"):
                    continue
                s = self.held()
                dmg = 1.0
                if s and "dur" in ITEMS[s[0]] and isinstance(ITEMS[s[0]].get("tier"), int) and "tool" in ITEMS[s[0]]:
                    t = ITEMS[s[0]]
                    dmg = {"sword": 3 + t["tier"], "axe": 2 + t["tier"]}.get(t["tool"], 1 + t["tier"] // 2)
                    p = self.p
                    if t["tool"] == "axe" and not p.on_ground and p.vy > 0 and p.air_peak is not None \
                            and not p.flying and p.y - p.air_peak > SMASH_MIN_FALL:
                        fall = p.y - p.air_peak
                        extra = min(30.0, 4.0 + 2.0 * (fall - SMASH_MIN_FALL))
                        dmg += extra
                        p.air_peak = p.y                 # the smash cushions the landing
                        self.say("Smash attack! +%d damage (%d block fall)" % (extra, fall))
                    if t["tool"] in ("sword", "axe"):
                        dmg += ench_of(s).get("sharpness", 0)
                    self.wear(1)
                z.hp -= dmg
                z.flash = 0.25
                if z.kind == "cow":
                    z.panic = 4.0
                if z.kind == "pigman":
                    for o in self.zombies:
                        if o.kind == "pigman" and abs(o.x - z.x) < 20:
                            o.angry = True
                if z.kind not in ("dragon", "crystal"):
                    z.vx = 7.0 if wx > self.p.x else -7.0
                    z.vy = -4.5
                self.attack_cd = 0.45
                self.no_mine = True
                self.p.swing = 0.25
                return

    def wear(self, n=1):
        if self.creative:
            return
        s = self.held()
        if s and "dur" in ITEMS[s[0]]:
            if self.dur_hit(s, n):
                self.inv[self.sel] = None
                self.say("Your %s broke!" % ITEMS[s[0]]["name"])

    def right_click(self):
        _, _, bx, by = self.mouse_world()
        if not self.in_reach(bx, by):
            return
        b = self.world.get(bx, by)
        if b == TABLE:
            self.ui = "table"
            return
        if b == ENCHANT_TABLE:
            self.ui = "enchant"
            return
        if b == GRINDSTONE:
            self.ui = "grind"
            return
        if b == FURNACE:
            self.cur_furnace = self.furnaces.setdefault((bx, by), new_furnace())
            self.ui = "furnace"
            return
        if b == ENDER_CHEST:
            self.cur_chest, self.chest_name = self.ender, "Ender Chest"
            self.ui = "chest"
            return
        if b in (CHEST, SHULKER_BOX):
            self.cur_chest = self.chests.setdefault((bx, by), [None] * 27)
            self.chest_name = "Shulker Box" if b == SHULKER_BOX else "Chest"
            self.ui = "chest"
            return
        if b in DOOR_TOGGLE:
            self.toggle_door(bx, by)
            return
        if b in (TRAPDOOR, TRAPDOOR_OPEN):
            self.toggle_trapdoor(bx, by)
            return
        if b in (LEVER, LEVER_ON):
            self.world.set(bx, by, LEVER if b == LEVER_ON else LEVER_ON)
            self.p.swing = 0.2
            return
        if b in BUTTONS or b in BUTTON_OFF:
            off = BUTTON_OFF.get(b, b)
            self.world.set(bx, by, BUTTON_ON[off])
            self.buttons_on[(self.dim, bx, by)] = BUTTON_TIME[off]
            self.p.swing = 0.2
            return
        s = self.held()
        if s and ITEMS[s[0]].get("tool") == "hoe" and b in (GRASS, DIRT):      # till the soil
            if self.world.get(bx, by - 1) != AIR:
                self.say("Tilled soil needs open air above it.")
                return
            self.world.set(bx, by, FARMLAND_WET if self.hydrated(bx, by) else FARMLAND)
            self.p.swing = 0.2
            self.wear(1)
            return
        if s and s[0] == SAPLING:
            ty = by - 1 if b in (GRASS, DIRT) else (by if b == AIR and self.world.get(bx, by + 1) in (GRASS, DIRT) else None)
            if ty is not None and self.world.get(bx, ty) == AIR and self.world.get(bx, ty + 1) in (GRASS, DIRT):
                self.world.set(bx, ty, SAPLING)
                self.p.swing = 0.2
                self.consume_held()
            else:
                self.say("Saplings are planted on grass or dirt.")
            return
        if s and s[0] == SEEDS:
            ty = by - 1 if b in FARMLANDS else (by if b == AIR and self.world.get(bx, by + 1) in FARMLANDS else None)
            if ty is not None and self.world.get(bx, ty) == AIR and self.world.get(bx, ty + 1) in FARMLANDS:
                self.world.set(bx, ty, CROPS[0])
                self.p.swing = 0.2
                self.consume_held()
            else:
                self.say("Seeds are planted on tilled soil (use a hoe on grass or dirt).")
            return
        if s and s[0] == FLINT_STEEL and b == TNT:
            self.ignite_tnt(bx, by)
            self.wear(1)
            self.p.swing = 0.2
            return
        if s and s[0] == DOOR_ITEM:
            self.place_door(bx, by)
            return
        if s and s[0] == LADDER:
            w = self.world
            if b == AIR and (any(SOLID[w.get(bx + dx, by)] for dx in (-1, 1))
                             or w.get(bx, by - 1) == LADDER or w.get(bx, by + 1) == LADDER):
                w.set(bx, by, LADDER)
                self.p.swing = 0.2
                self.consume_held()
            else:
                self.say("Ladders need a wall beside them (or another ladder).")
            return
        if s and s[0] in (BUCKET, LAVA_BUCKET, WATER_BUCKET):
            self.use_bucket(bx, by, b)
            return
        if s and s[0] == END_CRYSTAL:
            if self.dim != 2:
                self.say("End crystals only work in the End.")
            elif (b in (OBSIDIAN, BEDROCK, END_STONE) and self.world.get(bx, by - 1) == AIR
                  and not any(abs(c.x - (bx + 0.1)) < 0.9 and abs(c.y - (by - 0.8)) < 0.9 for c in self.crystals)):
                c = Crystal(bx + 0.1, by - 0.8)
                c.placed = True
                self.crystals.append(c)
                self.consume_held()
                self.p.swing = 0.2
            else:
                self.say("Place it on obsidian, bedrock or end stone with free space above.")
            return
        if s and s[0] == EYE_OF_ENDER:
            if self.dim != 0:
                self.say("The eye only works in the Overworld.")
            elif self.light_portal(bx, by, END_PORTAL):
                self.consume_held()
                self.say("The End portal opens! Stand in it for a few seconds.", 4)
            else:
                self.say("Needs a closed obsidian frame, at least 2 wide x 3 tall.")
            return
        if s and s[0] == FLINT_STEEL:
            if self.light_portal(bx, by):
                self.wear(1)
                self.say("The portal flickers to life!")
            else:
                self.say("Needs a closed obsidian frame, at least 2 wide x 3 tall.")
            return
        if s and s[0] in PLATES:
            if b in (AIR, WATER) and SOLID[self.world.get(bx, by + 1)]:
                self.world.set(bx, by, s[0])
                self.p.swing = 0.2
                self.consume_held()
            else:
                self.say("Pressure plates go on solid ground.")
            return
        if s and s[0] == PISTON:
            self.place_piston(bx, by, b)
            return
        if s and s[0] == STICKY:
            self.place_piston(bx, by, b, sticky=True)
            return
        if s and s[0] == OBSERVER:
            self.place_piston(bx, by, b, observer=True)
            return
        if s and s[0] == REDSTONE_DUST:
            if b == AIR and SOLID[self.world.get(bx, by + 1)]:
                self.world.set(bx, by, REDSTONE_DUST)
                self.p.swing = 0.2
                self.consume_held()
            else:
                self.say("Redstone dust lies on top of a solid block.")
            return
        if s and s[0] in (LEVER, BUTTON_STONE, BUTTON_WOOD):
            w_ = self.world
            if b == AIR and any(SOLID[w_.get(bx + dx, by + dy)] for dx, dy in ((0, 1), (-1, 0), (1, 0))):
                w_.set(bx, by, s[0])
                self.torch_scan_t = 0.0
                self.p.swing = 0.2
                self.consume_held()
            else:
                self.say("A %s needs a solid block under it or beside it." % ("lever" if s[0] == LEVER else "button"))
            return
        if s and s[0] == REDSTONE_TORCH:
            w_ = self.world
            if b == AIR and any(SOLID[w_.get(bx + dx, by + dy)] for dx, dy in ((0, 1), (-1, 0), (1, 0))):
                w_.set(bx, by, REDSTONE_TORCH)
                self.torch_scan_t = 0.0
                self.p.swing = 0.2
                self.consume_held()
            else:
                self.say("A torch needs a solid block under it or beside it.")
            return
        if b not in (AIR, LAVA, WATER) or not s or not ITEMS[s[0]].get("block"):
            return
        box = Entity(bx, by, 1, 1)
        if overlap(box, self.p) or any(overlap(box, z) for z in self.zombies):
            return
        if b != WATER and not any(SOLID[self.world.get(bx + dx, by + dy)] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            return
        self.world.set(bx, by, s[0])
        if s[0] == SHULKER_BOX:               # the carried contents move into the placed box
            carried = s[2] if isinstance(s[2], list) else [None] * 27
            self.chests[(bx, by)] = [list(x) if x else None for x in carried]
        self.p.swing = 0.2
        if not self.creative:
            s[1] -= 1
            if s[1] <= 0:
                self.inv[self.sel] = None

    def swap_bucket(self, item):
        s = self.held()
        if s[1] > 1:
            s[1] -= 1
            self.give_or_drop(new_stack(item))
        else:
            self.inv[self.sel] = new_stack(item)

    def use_bucket(self, bx, by, b):
        w, held = self.world, self.held()[0]
        if held == BUCKET:
            if b == LAVA:
                w.set(bx, by, AIR)
                self.swap_bucket(LAVA_BUCKET)
            elif b == WATER:
                if not (w.get(bx - 1, by) == WATER and w.get(bx + 1, by) == WATER):  # pool middles refill
                    w.set(bx, by, AIR)
                self.swap_bucket(WATER_BUCKET)
            else:
                self.say("Right-click lava or water to fill the bucket.")
                return
        elif b == LAVA and held == WATER_BUCKET:
            w.set(bx, by, OBSIDIAN)
            self.swap_bucket(BUCKET)
            self.say("The water turned the lava into obsidian!")
        elif b == WATER and held == LAVA_BUCKET:
            w.set(bx, by, COBBLE)
            self.swap_bucket(BUCKET)
            self.say("The lava hardened into cobblestone.")
        elif b == AIR:
            if held == LAVA_BUCKET and overlap(Entity(bx, by, 1, 1), self.p):
                self.say("You can't pour lava on yourself!")
                return
            w.set(bx, by, LAVA if held == LAVA_BUCKET else WATER)
            self.swap_bucket(BUCKET)
        else:
            self.say("Pour it onto an empty space.")
            return
        self.p.swing = 0.2

    def drink(self, potion):
        if potion == XP_BOTTLE:
            n = self.rnd.randint(3, 11)
            self.gain_xp(n)
            self.say("Experience bottle: creative mode has no XP." if self.creative else "+%d XP" % n)
        elif potion == REGEN_POTION:
            if self.p.hp >= 20:
                self.say("You're already at full health.")
                return
            self.p.hp = 20
            self.p.regen = 0.0
            self.say("You feel completely healed!")
        else:
            self.protect_t = PROTECTION_TIME
            self.say("Protected from all damage for 2 minutes!", 4)
        self.p.swing = 0.3
        self.consume_held()

    def consume_held(self):
        if self.creative:
            return
        s = self.held()
        s[1] -= 1
        if s[1] <= 0:
            self.inv[self.sel] = None

    def place_door(self, bx, by):
        w = self.world
        if SOLID[w.get(bx, by)]:                  # clicked the ground: put the door on top of it
            by -= 1
        if w.get(bx, by) != AIR or w.get(bx, by - 1) != AIR or not SOLID[w.get(bx, by + 1)]:
            self.say("Doors need 2 free blocks on top of solid ground.")
            return
        box = Entity(bx, by - 1, 1, 2)
        if overlap(box, self.p) or any(overlap(box, z) for z in self.zombies):
            return
        w.set(bx, by, DOOR_CB)
        w.set(bx, by - 1, DOOR_CT)
        self.p.swing = 0.2
        self.consume_held()

    def toggle_trapdoor(self, bx, by, silent=False):
        """Open (walk through, fall through) or close (solid) a trapdoor. False if something blocks closing."""
        w = self.world
        b = w.get(bx, by)
        if b == TRAPDOOR_OPEN:
            box = Entity(bx, by, 1, 1)
            if (not self.remote and overlap(box, self.p)) or any(overlap(box, z) for z in self.zombies + self.cows):
                if not silent:
                    self.say("Something is in the way.")
                return False
            w.set(bx, by, TRAPDOOR)
        elif b == TRAPDOOR:
            w.set(bx, by, TRAPDOOR_OPEN)
        return True

    def toggle_door(self, bx, by):
        w = self.world
        b = w.get(bx, by)
        py = by - 1 if b in (DOOR_CB, DOOR_OB) else by + 1
        if b in (DOOR_OB, DOOR_OT):               # closing: nothing may stand in the doorway
            box = Entity(bx, min(by, py), 1, 2)
            if (not self.remote and overlap(box, self.p)) or any(overlap(box, z) for z in self.zombies):
                self.say("Something is in the way.")
                return
        w.set(bx, by, DOOR_TOGGLE[b])
        if w.get(bx, py) in DOOR_TOGGLE:
            w.set(bx, py, DOOR_TOGGLE[w.get(bx, py)])

    def break_block(self, bx, by, can):
        w = self.world
        b = w.get(bx, by)
        w.set(bx, by, AIR)
        if b == LOG:
            self.leaf_alert(bx, by)
        if w.get(bx, by - 1) in PLATES:               # a pressure plate pops off when its support goes
            pl = w.get(bx, by - 1)
            w.set(bx, by - 1, AIR)
            self.spawn_drop(bx + 0.35, by - 0.65, pl, 1)
        if b in DOOR_TOGGLE:                      # a door is two blocks: remove its other half too
            py = by - 1 if b in (DOOR_CB, DOOR_OB) else by + 1
            if w.get(bx, py) in DOOR_TOGGLE:
                w.set(bx, py, AIR)
        if b == OBSIDIAN:
            self.unlight(bx, by)
        cx, cy = bx + 0.35, by + 0.35
        if b == FURNACE and (bx, by) in self.furnaces:
            for s in self.furnaces.pop((bx, by))["s"]:
                if s:
                    self.spawn_drop(cx, cy, *s)
        if b == CHEST and (bx, by) in self.chests:
            for s in self.chests.pop((bx, by)):
                if s:
                    self.spawn_drop(cx, cy, *s)
        if b == SHULKER_BOX:                  # mined: it keeps its contents inside the item
            contents = self.chests.pop((bx, by), None) or [None] * 27
            if can:
                self.spawn_drop(cx, cy, SHULKER_BOX, 1, contents)
            can = False
        if can:
            self.gain_xp({COAL_ORE: 2, IRON_ORE: 3, DIAMOND_ORE: 10, ANCIENT_DEBRIS: 20}.get(b, 0))
            for it in drops_for(b, self.rnd):
                self.spawn_drop(cx, cy, it, 1, ITEMS[it].get("dur"))
        self.wear(1)
        self.mining, self.mine_prog = None, 0.0

    # ----- inventory / crafting UI ---------------------------------------- #
    def panel_rect(self):
        pw, ph = 9 * self.SLOT + 24, 368
        return pygame.Rect((SW - pw) // 2, (SH - ph) // 2, pw, ph)

    def ui_layout(self):
        S = self.SLOT
        pr = self.panel_rect()
        px, py, ix = pr.x, pr.y, pr.x + 12
        R = lambda x, y: pygame.Rect(x, y, 40, 40)
        out = []
        iy = py + 176
        for r in range(3):
            for c in range(9):
                out.append(("s", self.inv, 9 + r * 9 + c, R(ix + c * S, iy + r * S)))
        for c in range(9):
            out.append(("s", self.inv, c, R(ix + c * S, iy + 3 * S + 8)))
        if self.ui == "inv":
            for r in range(2):
                for c in range(2):
                    out.append(("s", self.craft, r * 2 + c, R(ix + 3 * S + c * S, py + 36 + r * S)))
            out.append(("out", None, 0, R(ix + 6 * S + 10, py + 58)))
            for i in range(4):                 # armor: helmet / chestplate over leggings / boots
                out.append(("s", self.armor, i, R(ix + (i % 2) * S, py + 36 + (i // 2) * S)))
        elif self.ui == "table":
            for r in range(3):
                for c in range(3):
                    out.append(("s", self.craft, r * 3 + c, R(ix + 2 * S + c * S, py + 24 + r * S)))
            out.append(("out", None, 0, R(ix + 6 * S + 10, py + 24 + S)))
        elif self.ui == "enchant":
            out.append(("s", self.ench_slot, 0, R(ix + S, py + 56)))
        elif self.ui == "grind":
            out.append(("s", self.grind_slot, 0, R(ix + S, py + 56)))
        elif self.ui == "furnace":
            f = self.cur_furnace["s"]
            out.append(("s", f, 0, R(ix + 3 * S, py + 30)))
            out.append(("s", f, 1, R(ix + 3 * S, py + 30 + 2 * S)))
            out.append(("take", f, 2, R(ix + 6 * S, py + 30 + S)))
        elif self.ui == "chest":
            for r in range(3):
                for c in range(9):
                    out.append(("s", self.cur_chest, r * 9 + c, R(ix + c * S, py + 24 + r * S)))
        return out

    def craft_result(self):
        n = 2 if self.ui == "inv" else 3
        g = [[(self.craft[r * n + c][0] if self.craft[r * n + c] else 0) for c in range(n)] for r in range(n)]
        return match_recipe(g)

    def consume_craft(self):
        for i, s in enumerate(self.craft):
            if s:
                s[1] -= 1
                if s[1] <= 0:
                    self.craft[i] = None

    def click_output(self, shift):
        for _ in range(64 if shift else 1):
            res = self.craft_result()
            if not res:
                return
            out, n = res
            if shift:
                if not can_fit(self.inv, range(36), out, n):
                    return
                put_into(self.inv, range(36), new_stack(out, n))
            else:
                c = self.cursor
                if c is None:
                    self.cursor = new_stack(out, n)
                elif c[0] == out and maxstack(out) > 1 and c[1] + n <= 64:
                    c[1] += n
                else:
                    return
            self.consume_craft()

    def quick_move(self, cont, idx):
        s = cont[idx]
        if not s:
            return
        if cont is self.inv:
            if self.ui == "chest":
                if self.chest_name == "Shulker Box" and s[0] == SHULKER_BOX:
                    self.say("A shulker box can't go inside a shulker box.")
                    return
                put_into(self.cur_chest, range(27), s)
            elif self.ui == "enchant":
                if ench_options(s[0]) and self.ench_slot[0] is None:
                    put_into(self.ench_slot, [0], s)
            elif self.ui == "grind":
                if ench_options(s[0]) and self.grind_slot[0] is None:
                    put_into(self.grind_slot, [0], s)
            elif self.ui == "furnace":
                f = self.cur_furnace["s"]
                if s[0] in SMELT:
                    put_into(f, [0], s)
                elif s[0] in FUEL:
                    put_into(f, [1], s)
            elif self.ui == "inv" and "armor" in ITEMS[s[0]]:
                sl = ARMOR_SLOTS.index(ITEMS[s[0]]["armor"])
                if self.armor[sl] is None:
                    self.armor[sl], cont[idx] = s, None
                    return
            if s[1] > 0:
                put_into(self.inv, range(9, 36) if idx < 9 else range(9), s)
        else:
            put_into(self.inv, range(36), s)
        if s[1] <= 0:
            cont[idx] = None

    def click_slot(self, cont, idx, button, shift, take_only=False):
        s, c = cont[idx], self.cursor
        if cont is self.grind_slot and c and not shift and not ench_options(c[0]):
            self.say("The grindstone only takes tools, weapons, bows and armor.")
            return
        if cont is self.ench_slot and c and not shift and not ench_options(c[0]):
            self.say("Only tools, weapons, bows and armor can be enchanted.")
            return
        if cont is self.armor and c and not shift and not take_only \
                and ITEMS[c[0]].get("armor") != ARMOR_SLOTS[idx]:
            self.say("That doesn't go in the %s slot." % ARMOR_SLOTS[idx])
            return
        if (cont is self.cur_chest and self.ui == "chest" and self.chest_name == "Shulker Box"
                and c and c[0] == SHULKER_BOX and not shift):
            self.say("A shulker box can't go inside a shulker box.")
            return
        if shift:
            self.quick_move(cont, idx)
            return
        if take_only:
            if s and (c is None):
                self.cursor, cont[idx] = s, None
            elif s and c and c[0] == s[0] and maxstack(c[0]) > 1:
                m = min(s[1], 64 - c[1])
                c[1] += m
                s[1] -= m
                if s[1] <= 0:
                    cont[idx] = None
            return
        if button == 1:
            if c is None:
                if s:
                    self.cursor, cont[idx] = s, None
            elif s is None:
                cont[idx], self.cursor = c, None
            elif s[0] == c[0] and maxstack(c[0]) > 1:
                m = min(c[1], 64 - s[1])
                s[1] += m
                c[1] -= m
                if c[1] <= 0:
                    self.cursor = None
            else:
                cont[idx], self.cursor = c, s
        else:
            if c is None:
                if s:
                    half = (s[1] + 1) // 2
                    self.cursor = [s[0], half, s[2]]
                    s[1] -= half
                    if s[1] <= 0:
                        cont[idx] = None
            elif s is None:
                cont[idx] = [c[0], 1, c[2]]
                c[1] -= 1
                if c[1] <= 0:
                    self.cursor = None
            elif s[0] == c[0] and maxstack(c[0]) > 1 and s[1] < 64:
                s[1] += 1
                c[1] -= 1
                if c[1] <= 0:
                    self.cursor = None
            else:
                cont[idx], self.cursor = c, s

    def ui_click(self, pos, button):
        if self.ui == "book":
            self.bk_click(pos)
            return
        shift = bool(pygame.key.get_mods() & pygame.KMOD_SHIFT)
        if self.creative and self.palette_panel().collidepoint(pos):
            if self.pal_max_scroll() and self.pal_track().inflate(10, 0).collidepoint(pos):
                self.pal_drag = True                 # grab the bar (a click on the track jumps there)
                self.pal_set_from_y(pos[1])
                return
            if self.clear_button().collidepoint(pos):
                if self.clear_t > 0:                 # second click within 3 s confirms
                    self.clear_inventory()
                else:
                    self.clear_t = 3.0
                    self.say("Click the button again to clear your whole inventory.")
                return
            for it, rect in self.palette_rects():
                if rect.collidepoint(pos):
                    n = maxstack(it) if button == 1 else 1
                    c = self.cursor
                    if c and c[0] == it and maxstack(it) > 1:
                        c[1] = min(maxstack(it), c[1] + n)
                    else:
                        self.cursor = new_stack(it, n)
                    return
            self.cursor = None                       # clicking the list's background deletes the held item
            return
        if self.book_ui_click(pos):
            return
        if self.ui == "enchant":
            for i, r in enumerate(self.ench_buttons()):
                if r.collidepoint(pos):
                    self.enchant_apply(i)
                    return
        if self.ui == "grind" and self.ench_buttons()[1].collidepoint(pos):
            self.grind_apply()
            return
        if self.creative and self.ui == "chest":
            bb, sb = self.stress_buttons()
            if bb.collidepoint(pos) or (sb.collidepoint(pos) and self.chest_name != "Shulker Box"):
                self.stress_fill(sb.collidepoint(pos))
                return
        for kind, cont, idx, rect in self.ui_layout():
            if rect.collidepoint(pos):
                if kind == "out":
                    self.click_output(shift)
                else:
                    self.click_slot(cont, idx, button, shift, take_only=(kind == "take"))
                return
        if self.cursor and not self.panel_rect().collidepoint(pos):
            c = self.cursor
            n = c[1] if button == 1 else 1
            self.spawn_drop(self.p.x + 0.3, self.p.y + 0.3, c[0], n, c[2],
                            vx=self.p.face * 5, delay=1.0)
            c[1] -= n
            if c[1] <= 0:
                self.cursor = None

    # ----- recipe book ----------------------------------------------------- #
    BOOK_ROWS = 7

    # ----- experience and enchanting --------------------------------------- #
    @staticmethod
    def xp_for_level(l):
        return 10 * l + 5 * l * (l - 1) // 2

    def xp_level(self):
        l = 0
        while self.xp >= self.xp_for_level(l + 1):
            l += 1
        return l

    def gain_xp(self, n):
        if not n or self.creative:
            return
        held = self.held()
        gear = [st for st in self.armor if st] + ([held] if held else [])
        while n > 0:                                  # Mending: XP repairs gear first (1 xp = 2 durability)
            worn = [st for st in gear if ench_of(st).get("mending") and st[2] < ITEMS[st[0]]["dur"]]
            if not worn:
                break
            st = self.rnd.choice(worn)
            fix = min(2, ITEMS[st[0]]["dur"] - st[2])
            dur_sub(st, -fix)
            n -= 1
        self.xp += n

    def spend_levels(self, k):
        l = self.xp_level()
        into = self.xp - self.xp_for_level(l)
        nl = max(0, l - k)
        self.xp = self.xp_for_level(nl) + min(into, 10 + 5 * nl - 1)

    def ench_buttons(self):
        pr = self.panel_rect()
        return [pygame.Rect(pr.x + 12 + 3 * self.SLOT, pr.y + 30 + i * 44, pr.w - 24 - 3 * self.SLOT, 40) for i in range(3)]

    def ench_offer(self, st, i):
        """(key, level, cost in levels) offered by button i for this stack, or None."""
        if not st or not ench_options(st[0]):
            return None
        import zlib
        cur, lvl = ench_of(st), i + 1
        cands = [k for k in ench_options(st[0]) if cur.get(k, 0) < min(lvl, ENCH[k][1])]
        if not cands:
            return None
        rnd = random.Random(zlib.crc32(repr((self.worlds[0].seed, st[0], sorted(cur.items()), i)).encode()))
        key = rnd.choice(cands)
        return key, min(lvl, ENCH[key][1]), 2 * lvl

    def grind_xp(self, st):
        return GRIND_XP * sum(ench_of(st).values()) if st else 0

    def grind_apply(self):
        """Grindstone: strip every enchantment from the item (durability stays) and refund some XP."""
        st = self.grind_slot[0]
        if not st:
            self.say("Put an enchanted item on the grindstone first.")
            return
        if not ench_of(st):
            self.say("That item has no enchantments.")
            return
        back = self.grind_xp(st)
        st[2] = Dur(st[2])                      # a fresh Dur carries no enchantments
        if not self.creative:
            self.xp += back
        self.say("Enchantments removed%s." % ("" if self.creative else " (+%d XP)" % back), 4)

    def enchant_apply(self, i):
        st = self.ench_slot[0]
        o = self.ench_offer(st, i)
        if not st:
            self.say("Put a tool, weapon or armor piece in the slot first.")
            return
        if not o:
            self.say("Nothing more of that strength can be added.")
            return
        key, lvl, cost = o
        if not self.creative and self.xp_level() < cost:
            self.say("You need %d levels (you have %d)." % (cost, self.xp_level()))
            return
        if not self.creative:
            self.spend_levels(cost)
        old = st[2]
        new = Dur(old)
        new.ench = dict(ench_of(st))
        new.ench[key] = lvl
        st[2] = new
        self.say("Enchanted: %s" % stack_name(st), 4)

    def stress_buttons(self):
        """Creative-only chest buttons for break-testing: (books button, shulkers button)."""
        pr = self.panel_rect()
        return (pygame.Rect(pr.right - 236, pr.y + 4, 112, 22), pygame.Rect(pr.right - 118, pr.y + 4, 106, 22))

    @staticmethod
    def full_book():
        return [BOOK, 1, {"pages": [("%03d " % i) * (BOOK_PAGE_CHARS // 4) for i in range(BOOK_MAX_PAGES)]}]

    def stress_fill(self, shulkers):
        """Fill the open chest with max-size books (or shulker boxes packed with them)."""
        cont = self.cur_chest
        for i in range(len(cont)):
            if shulkers:
                cont[i] = [SHULKER_BOX, 1, [self.full_book() for _ in range(27)]]
            else:
                cont[i] = self.full_book()
        self.say("Stress test: chest filled with %d full books." % (len(cont) * (27 if shulkers else 1)), 4)

    def book_button(self):
        pr = self.panel_rect()
        return pygame.Rect(pr.right - 98, pr.y + 4, 86, 22)

    def book_panel(self):
        pr = self.panel_rect()
        return pygame.Rect(pr.x - 312, pr.y, 300, pr.h)

    def book_entries(self):
        if self.ui == "furnace":
            out = [("smelt", i, o) for i, o in SMELT.items()]
            return out + [("fuel", i, None) for i in FUEL]
        lim = 2 if self.ui == "inv" else 3
        have = self.item_counts()
        ents = []
        for pat, o, n in RECIPES:
            if len(pat) > lim or len(pat[0]) > lim:
                continue
            ents.append(("craft", pat, (o, n)))
        ents.sort(key=lambda e: not self.can_make(e[1], have))      # craftable ones first (stable)
        return ents

    def item_counts(self):
        cnt = {}
        for st in self.inv:
            if st:
                cnt[st[0]] = cnt.get(st[0], 0) + st[1]
        for st in self.craft:
            if st:
                cnt[st[0]] = cnt.get(st[0], 0) + st[1]
        return cnt

    @staticmethod
    def pat_need(pat):
        need = {}
        for row in pat:
            for c in row:
                if c:
                    need[c] = need.get(c, 0) + 1
        return need

    def can_make(self, pat, have):
        return all(have.get(i, 0) >= n for i, n in self.pat_need(pat).items())

    def book_rows(self):
        bp = self.book_panel()
        ents = self.book_entries()
        pages = max(1, -(-len(ents) // self.BOOK_ROWS))
        self.book_page = max(0, min(self.book_page, pages - 1))
        a = self.book_page * self.BOOK_ROWS
        return [(pygame.Rect(bp.x + 6, bp.y + 30 + k * 44, bp.w - 12, 42), e)
                for k, e in enumerate(ents[a:a + self.BOOK_ROWS])], pages

    def book_pager(self):
        bp = self.book_panel()
        return pygame.Rect(bp.x + 8, bp.bottom - 30, 40, 24), pygame.Rect(bp.right - 48, bp.bottom - 30, 40, 24)

    def return_grid(self):
        for i, st in enumerate(self.craft):
            if st:
                self.give_or_drop(st)
                self.craft[i] = None

    def take_one(self, item):
        for st in self.inv:
            if st and st[0] == item and st[1] > 0:
                got = [item, 1, st[2]]
                st[1] -= 1
                if st[1] <= 0:
                    self.inv[self.inv.index(st)] = None
                return got
        return None

    def book_click(self, e):
        kind, a, b = e
        if kind == "craft":
            self.return_grid()
            if not self.can_make(a, self.item_counts()):
                self.say("You are missing ingredients for that recipe.")
                return
            n = 2 if self.ui == "inv" else 3
            for r, row in enumerate(a):
                for c, item in enumerate(row):
                    if item:
                        self.craft[r * n + c] = self.take_one(item)
            return
        f = self.cur_furnace["s"]
        if kind == "smelt":
            slot, item = 0, a
        else:
            slot, item = 1, a
        cur = f[slot]
        if cur and cur[0] != item:
            self.say("Empty that furnace slot first.")
            return
        have = sum(st[1] for st in self.inv if st and st[0] == item)
        if have <= 0:
            self.say("You don't have any %s." % ITEMS[item]["name"])
            return
        want = maxstack(item) if kind == "smelt" else min(8, maxstack(item))
        moved = 0
        while moved < want and (not cur or cur[1] < maxstack(item)):
            got = self.take_one(item)
            if not got:
                break
            if cur:
                cur[1] += 1
            else:
                f[slot] = cur = got
            moved += 1

    def book_ui_click(self, pos):
        """Handle a click on the recipe-book button/panel. True if it was consumed."""
        if self.ui not in ("inv", "table", "furnace"):
            return False
        if self.book_button().collidepoint(pos):
            self.book_open = not self.book_open
            return True
        if not (self.book_open and self.book_panel().collidepoint(pos)):
            return False
        rows, pages = self.book_rows()
        for r, e in rows:
            if r.collidepoint(pos):
                self.book_click(e)
                return True
        prev, nxt = self.book_pager()
        if prev.collidepoint(pos):
            self.book_page = (self.book_page - 1) % pages
        elif nxt.collidepoint(pos):
            self.book_page = (self.book_page + 1) % pages
        return True

    def small_icon(self, it):
        im = self.icon22.get(it)
        if im is None:
            im = self.icon22[it] = pygame.transform.scale(ICON[it], (22, 22))
        return im

    def draw_book(self, mpos):
        """Draws the button and (if open) the recipe book; returns a tooltip or None."""
        scr, tip = self.screen, None
        bb = self.book_button()
        pygame.draw.rect(scr, (120, 80, 150) if self.book_open else (90, 90, 90), bb)
        pygame.draw.rect(scr, (255, 255, 255), bb, 2)
        self.txt("Recipes", bb.center, (255, 255, 255), self.small, center=True)
        if not self.book_open:
            return tip
        bp = self.book_panel()
        pygame.draw.rect(scr, (198, 198, 198), bp)
        pygame.draw.rect(scr, (255, 255, 255), bp, 3)
        pygame.draw.rect(scr, (60, 60, 60), bp.inflate(6, 6), 3)
        self.txt("Furnace recipes" if self.ui == "furnace" else "Recipe book", (bp.x + 12, bp.y + 7), (50, 50, 50))
        rows, pages = self.book_rows()
        have = self.item_counts()
        for r, (kind, a, b) in rows:
            if kind == "craft":
                ok = self.can_make(a, have)
            else:
                ok = any(st and st[0] == a for st in self.inv)
            pygame.draw.rect(scr, (110, 190, 110) if ok else (150, 150, 150), r)
            pygame.draw.rect(scr, (55, 55, 55), r, 2)
            if kind == "craft":
                slot = pygame.Rect(r.x + 1, r.y + 1, 40, 40)
                self.draw_stack([b[0], b[1], None], slot)
                x = r.x + 48
                for it, n in self.pat_need(a).items():
                    scr.blit(self.small_icon(it), (x, r.y + 10))
                    if n > 1:
                        self.txt("x%d" % n, (x + 22, r.y + 22), (255, 255, 255), self.small)
                    x += 38
                if r.collidepoint(mpos):
                    tip = ITEMS[b[0]]["name"]
            elif kind == "smelt":
                self.draw_stack([a, 1, None], pygame.Rect(r.x + 1, r.y + 1, 40, 40))
                pygame.draw.polygon(scr, (60, 60, 60), [(r.x + 60, r.centery - 7), (r.x + 76, r.centery), (r.x + 60, r.centery + 7)])
                self.draw_stack([b, 1, None], pygame.Rect(r.x + 90, r.y + 1, 40, 40))
                if r.collidepoint(mpos):
                    tip = "%s -> %s" % (ITEMS[a]["name"], ITEMS[b]["name"])
            else:
                self.draw_stack([a, 1, None], pygame.Rect(r.x + 1, r.y + 1, 40, 40))
                self.txt("Fuel: smelts %g items" % (FUEL[a] / SMELT_TIME), (r.x + 50, r.centery - 6), (40, 40, 40), self.small)
                if r.collidepoint(mpos):
                    tip = ITEMS[a]["name"]
        prev, nxt = self.book_pager()
        for rc, lab in ((prev, "<"), (nxt, ">")):
            pygame.draw.rect(scr, (139, 139, 139), rc)
            pygame.draw.rect(scr, (55, 55, 55), rc, 2)
            self.txt(lab, rc.center, (255, 255, 255), center=True)
        self.txt("%d / %d" % (self.book_page + 1, pages), (bp.centerx, bp.bottom - 18), (50, 50, 50), center=True)
        return tip

    def close_ui(self):
        for i, s in enumerate(self.craft):
            if s:
                self.give_or_drop(s)
                self.craft[i] = None
        if self.ench_slot[0]:
            self.give_or_drop(self.ench_slot[0])
            self.ench_slot[0] = None
        if self.grind_slot[0]:
            self.give_or_drop(self.grind_slot[0])
            self.grind_slot[0] = None
        if self.cursor:
            self.give_or_drop(self.cursor)
            self.cursor = None
        self.ui = None
        self.book_page = 0

    # ----- update ---------------------------------------------------------- #
    def update(self, dt):
        if self.paused:
            return
        p, w = self.p, self.world
        if not self.tick_frozen:
            self.time += dt
        phase = (self.time / DAY_LEN) % 1.0
        self.light = max(0.0, min(1.0, 0.5 + 1.0 * math.sin(2 * math.pi * phase)))
        keys = pygame.key.get_pressed()
        mouse = self.mouse_buttons()
        if self.pal_drag:
            if self.ui and self.creative and mouse[0]:
                self.pal_set_from_y(self.mouse_pos()[1])
            else:
                self.pal_drag = False
        free = self.ui is None and self.cmd is None
        mv = (int(keys[pygame.K_d] or keys[pygame.K_RIGHT]) - int(keys[pygame.K_a] or keys[pygame.K_LEFT])) if free else 0
        jump = free and (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP])
        down = free and (keys[pygame.K_s] or keys[pygame.K_DOWN])
        shift = bool(keys[pygame.K_LSHIFT])
        p.step(self, mv, free and shift, jump, dt, down)
        w = self.world                      # die() may just have sent us back to the Overworld
        pkind = PORTAL if touching(w, p, PORTAL) else (END_PORTAL if touching(w, p, END_PORTAL) else None)
        if pkind:
            if not self.portal_lock:
                self.portal_t += dt
                if self.portal_t >= 3.0:
                    self.use_portal(pkind)
                    w = self.world
        else:
            self.portal_t = max(0.0, self.portal_t - 2 * dt)
            self.portal_lock = False
        p.invuln = max(0.0, p.invuln - dt)
        p.swing = max(0.0, p.swing - dt)
        self.attack_cd = max(0.0, self.attack_cd - dt)
        if not self.creative:                               # hunger: drains faster when moving / sprinting
            moving = abs(p.vx) > 0.5
            sprinting = bool(free and shift) and moving
            self.food = max(0.0, self.food - dt * (0.011 + (0.02 if moving else 0) + (0.04 if sprinting else 0)))
            if self.food <= 0:
                self.starve_t += dt
                if self.starve_t >= 4.0:
                    self.starve_t = 0.0
                    if p.hp > 1:                            # starvation hurts but never kills
                        self.hurt(1, force=True, armor=False)
                        self.say("You are starving! Eat something.")
            else:
                self.starve_t = 0.0
        if p.hp < 20 and (self.food >= 14 or self.creative):
            p.regen += dt
            if p.regen >= 4:
                p.regen, p.hp = 0.0, p.hp + 1
                self.food = max(0.0, self.food - 0.4)
        # camera
        self.camx = int(p.x * TILE + p.w * TILE / 2 - SW / 2)
        self.camy = int(p.y * TILE + p.h * TILE / 2 - SH / 2)
        self.camx = max(0, min(WW * TILE - SW, self.camx))
        self.camy = max(0, min(WH * TILE - SH, self.camy))
        # mining
        if not mouse[0]:
            self.no_mine = False
        if free and mouse[0] and not self.no_mine:
            _, _, bx, by = self.mouse_world()
            b = w.get(bx, by)
            if (targetable(b) and (b != BEDROCK or (self.creative and 0 <= bx < WW and 0 <= by < WH))
                    and self.in_reach(bx, by)):
                if self.mining != (bx, by):
                    self.mining, self.mine_prog = (bx, by), 0.0
                t, can = break_time(b, self.held())
                if self.creative:
                    t, can = 0.05, False
                self.mine_prog += dt
                p.swing = max(p.swing, 0.1)
                if self.mine_prog >= t:
                    self.break_block(bx, by, can)
            else:
                self.mining, self.mine_prog = None, 0.0
        else:
            self.mining, self.mine_prog = None, 0.0
        if self.tick_frozen:                                # the world stands still; /tick step N runs ticks
            n = min(self.tick_steps, TICK_BATCH)
            for _ in range(n):
                self.time += TICK_DT
                self.update_world(TICK_DT)
            if n:
                self.tick_steps -= n
                self.tick_done += n
                if self.tick_steps <= 0:
                    self.chat_add("Stepped %d tick%s." % (self.tick_done, "" if self.tick_done == 1 else "s"), (150, 230, 150))
                    self.tick_done = 0
        else:
            self.update_world(dt)
        # timers
        self.msg_t = max(0.0, self.msg_t - dt)
        self.clear_t = max(0.0, self.clear_t - dt)
        self.protect_t = max(0.0, self.protect_t - dt)
        self.name_t = max(0.0, self.name_t - dt)
        self.autosave_t += dt
        if self.autosave_t > 120:
            self.autosave_t = 0.0
            self.save()

    def grow_tree(self, x, y):
        """A sapling at (x, y) becomes an oak (same shape as the world's trees) if there is room."""
        w = self.world
        room = 0
        while room < 6 and w.get(x, y - room) in (AIR, SAPLING, LEAVES):
            room += 1
        if room < 4:
            return False
        tall = min(self.rnd.randint(4, 6), room)
        h = y + 1                                       # the ground cell
        top = h - tall
        for i in range(1, tall + 1):
            w.set(x, h - i, LOG)
        for dy, hw in ((-2, 1), (-1, 2), (0, 2), (1, 2)):
            for dx in range(-hw, hw + 1):
                if w.get(x + dx, top + dy) == AIR:
                    w.set(x + dx, top + dy, LEAVES)
        return True

    def update_leaves(self):
        """Leaves more than 4 steps (through leaves) from any log fall, a few per second."""
        w, rnd = self.world, self.rnd
        for h in self.leaf_hot[:]:
            h[2] -= 1.0
            if h[2] <= 0:
                self.leaf_hot.remove(h)
                continue
            x0, x1 = max(0, h[0] - 12), min(WW, h[0] + 13)
            y0, y1 = max(0, h[1] - 14), min(WH, h[1] + 15)
            logs, leaves = [], set()
            for x in range(x0, x1):
                col = w.cols[x]
                y = col.find(LOG, y0, y1)
                while y != -1:
                    logs.append((x, y))
                    y = col.find(LOG, y + 1, y1)
                y = col.find(LEAVES, y0, y1)
                while y != -1:
                    leaves.add((x, y))
                    y = col.find(LEAVES, y + 1, y1)
            if not leaves:
                continue
            dist = {c: 0 for c in logs}
            frontier = logs
            for d in range(1, 5):
                nxt = []
                for x, y in frontier:
                    for c in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        if c in leaves and c not in dist:
                            dist[c] = d
                            nxt.append(c)
                frontier = nxt
            for c in leaves:
                if c in dist or abs(c[0] - h[0]) > 8 or abs(c[1] - h[1]) > 11:
                    continue
                if rnd.random() < 0.4:                         # they fall one after another, not all at once
                    w.set(c[0], c[1], AIR)
                    if not self.creative:
                        r = rnd.random()
                        if r < 0.06:
                            self.spawn_drop(c[0] + 0.35, c[1] + 0.35, SAPLING, 1)
                        elif r < 0.16:
                            self.spawn_drop(c[0] + 0.35, c[1] + 0.35, STICK, 1)

    def hydrated(self, x, y):
        """Water within 4 blocks beside the farmland, in its row or the row above."""
        w = self.world
        return any(w.get(xx, yy) == WATER for xx in range(x - 4, x + 5) for yy in (y, y - 1))

    def update_farms(self, dt):
        """Once a second near you: farmland gets wet or dry, crops grow, and crops without soil pop off."""
        self.farm_t += dt
        if self.farm_t < 1.0:
            return
        self.farm_t = 0.0
        self.update_leaves()
        w, rnd = self.world, self.rnd
        x0, x1 = max(0, int(self.p.x) - 56), min(WW, int(self.p.x) + 57)
        y0, y1 = max(0, int(self.p.y) - 40), min(WH, int(self.p.y) + 41)
        for x in range(x0, x1):
            col = w.cols[x]
            for fid in FARMLANDS:
                y = col.find(fid, y0, y1)
                while y != -1:
                    above = w.get(x, y - 1)
                    if SOLID[above]:                       # something heavy on top: it packs back into dirt
                        w.set(x, y, DIRT)
                    else:
                        wet = self.hydrated(x, y)
                        nid = FARMLAND_WET if wet else FARMLAND
                        if fid != nid:
                            w.set(x, y, nid)
                        if above in CROPS[:-1] and rnd.random() < (0.05 if wet else 0.025):
                            w.set(x, y - 1, CROPS[CROPS.index(above) + 1])
                    y = col.find(fid, y + 1, y1)
            y = col.find(SAPLING, y0, y1)
            while y != -1:
                if w.get(x, y + 1) not in (GRASS, DIRT):               # no ground under it
                    w.set(x, y, AIR)
                    self.spawn_drop(x + 0.35, y + 0.35, SAPLING, 1)
                elif rnd.random() < 1.0 / 60:
                    self.grow_tree(x, y)
                y = col.find(SAPLING, y + 1, y1)
            for cid in CROPS:
                y = col.find(cid, y0, y1)
                while y != -1:
                    if w.get(x, y + 1) not in FARMLANDS:   # no soil under it
                        w.set(x, y, AIR)
                        self.spawn_drop(x + 0.35, y + 0.35, SEEDS, 1)
                    y = col.find(cid, y + 1, y1)

    def update_world(self, dt):
        """Everything that /tick freeze stops: drops, furnaces, mobs, TNT, machines, fishing, arrows."""
        p, w = self.p, self.world
        # drops
        for d in self.drops[:]:
            d.age += dt
            d.vy = min(d.vy + GRAVITY * dt, 25.0)
            if d.on_ground:
                d.vx *= 0.85
            dist = math.hypot(d.x + 0.14 - (p.x + 0.3), d.y + 0.14 - (p.y + 0.9))
            if d.age > 0.4 and dist < 3.0 and dist > 0.01:
                d.vx = (p.x + 0.3 - d.x - 0.14) / dist * 8
                d.vy = (p.y + 0.9 - d.y - 0.14) / dist * 8
            physics(w, d, dt)
            if touching(w, d, LAVA):
                self.drops.remove(d)
                continue
            if d.age > 0.4 and dist < 1.0:
                rem = self.give(d.item, d.n, d.dur)
                if rem <= 0:
                    self.drops.remove(d)
                    continue
                d.n = rem
            if d.age > 300:
                self.drops.remove(d)
        # furnaces
        for f in self.furnaces.values():
            update_furnace(f, dt)
        # zombies
        self.spawn_t += dt
        if self.spawn_t >= 3.0:
            self.spawn_t = 0.0
            if self.dim == 0 and self.light < 0.35 and len(self.zombies) < 5:
                zx = int(p.x + self.rnd.choice((-1, 1)) * self.rnd.randint(14, 26))
                if 2 < zx < WW - 2:
                    zy = w.surface_y(zx) - 2
                    if w.get(zx, zy) == AIR and w.get(zx, zy - 1) == AIR:
                        self.zombies.append(Zombie(zx, zy))
        self.cow_t += dt
        if self.cow_t >= 4.0:
            self.cow_t = 0.0
            for _ in range(8 if self.dim == 0 and len(self.cows) < 6 else 0):       # a few tries to find open grass
                cx = int(p.x + self.rnd.choice((-1, 1)) * self.rnd.randint(10, 28))
                if not 2 < cx < WW - 3:
                    continue
                sy = w.surface_y(cx)
                if (w.get(cx, sy) == GRASS and SOLID[w.get(cx + 1, sy)]
                        and all(w.get(cx + i, sy - j) == AIR for i in (0, 1) for j in (1, 2))
                        and not any(abs(c.x - cx) < 6 for c in self.cows)):
                    self.cows.append(Cow(cx, sy - 1.0 - 0.01))
                    break
        for c in self.cows[:]:
            if c not in self.cows:
                continue
            c.update(self, dt)
            if c.hp <= 0:
                self.cows.remove(c)
                self.gain_xp(2)
                self.spawn_drop(c.x + 0.5, c.y + 0.3, RAW_BEEF, self.rnd.randint(1, 3))
                if self.rnd.random() < 0.6:
                    self.spawn_drop(c.x + 0.5, c.y + 0.3, LEATHER, self.rnd.randint(1, 2))
            elif abs(c.x - p.x) > 80:
                self.cows.remove(c)
        for z in self.zombies[:]:
            if z not in self.zombies:            # die() cleared the list while we were looping
                continue
            z.update(self, dt)
            if z not in self.zombies:            # ...this very zombie killed the player
                continue
            if z.hp <= 0:
                self.zombies.remove(z)
                self.gain_xp(5)
            elif abs(z.x - p.x) > 60:
                self.zombies.remove(z)
        self.update_tnts(dt)
        self.update_end(dt)
        self.update_pearls(dt)
        self.update_machines(dt)
        self.update_fishing(dt)
        self.update_remote(dt)
        self.update_fireworks(dt)
        self.update_arrows(dt)
        self.update_farms(dt)

    # ----- drawing --------------------------------------------------------- #
    def txt(self, s, pos, col=(255, 255, 255), font=None, center=False):
        font = font or self.font
        sh = font.render(s, True, (20, 20, 20))
        im = font.render(s, True, col)
        r = im.get_rect()
        if center:
            r.center = pos
        else:
            r.topleft = pos
        self.screen.blit(sh, (r.x + 1, r.y + 1))
        self.screen.blit(im, r)

    def draw_sky(self):
        if self.dim == 2:
            self.screen.fill((9, 5, 20))
            for x, y in self.stars:
                pygame.draw.rect(self.screen, (170, 150, 220), (x, y, 2, 2))
            return
        if self.dim == 1:
            self.screen.fill((38, 10, 12))
            return
        phase = (self.time / DAY_LEN) % 1.0
        sky = lerpc((8, 10, 32), (125, 185, 255), self.light)
        self.screen.fill(sky)
        if self.light < 0.6:
            a = 1 - self.light / 0.6
            for x, y in self.stars:
                v = int(255 * a)
                pygame.draw.rect(self.screen, (v, v, v), (x, y, 2, 2))
        ang = 2 * math.pi * phase
        for off, col, size in ((0, (255, 235, 120), 44), (math.pi, (225, 225, 235), 36)):
            s = math.sin(ang + off)
            if s > -0.08:
                x = SW / 2 - math.cos(ang + off) * SW * 0.45
                y = SH * 0.62 - s * SH * 0.55
                pygame.draw.rect(self.screen, col, (x - size / 2, y - size / 2, size, size))
        cc = lerpc((70, 70, 90), (250, 250, 250), self.light)
        for c in self.clouds:
            c[0] = (c[0] + 0.08) % (SW + 300)
            x = c[0] - 150
            pygame.draw.rect(self.screen, cc, (x, c[1], c[2], 22))
            pygame.draw.rect(self.screen, cc, (x + 20, c[1] - 14, c[2] - 50, 16))

    def draw_dust(self, x, y, pos):
        l = self.dust_lvs.get(self.dim, {}).get((x, y), 0)
        col = (int(90 + 10 * l), 14 + 3 * l, 14 + 3 * l) if l else (104, 16, 16)
        t, px, py = max(2, TILE // 6), pos[0], pos[1]
        links = self.dust_links(x, y)
        left = any(c[0] < x for c in links)
        right = any(c[0] > x for c in links)
        y0 = py + TILE - t
        if not (left or right):                            # a lone dot with four stubs
            q = TILE // 4
            pygame.draw.rect(self.screen, col, (px + q, y0, TILE - 2 * q, t))
            pygame.draw.rect(self.screen, col, (px + TILE // 2 - t // 2, y0 - t, t, t))
        else:
            xa = px if left else px + TILE // 2 - t // 2
            xb = px + TILE if right else px + TILE // 2 + (t + 1) // 2
            pygame.draw.rect(self.screen, col, (xa, y0, xb - xa, t))
        for cx_, cy_ in links:                             # climbing a wall: a bar up the block's side
            if cy_ < y:
                bx_ = px + TILE - t if cx_ > x else px
                pygame.draw.rect(self.screen, col, (bx_, py, t, TILE))
        if l:
            self.lights.append((x, y, 2))

    def draw_world(self):
        w, scr = self.world, self.screen
        cx, cy = self.camx, self.camy
        x0, x1 = max(0, cx // TILE), min(WW, (cx + SW) // TILE + 1)
        y0, y1 = max(0, cy // TILE), min(WH, (cy + SH) // TILE + 1)
        nether = self.dim in (1, 2)
        bgt = BG_END if self.dim == 2 else (BG_NETHER if nether else BG_TILE)
        frame = int(pygame.time.get_ticks() / 250) % 4
        self.lights = []
        for x in range(x0, x1):
            col, hx = w.cols[x], w.height[x]
            for y in range(y0, y1):
                b = col[y]
                pos = (x * TILE - cx, y * TILE - cy)
                if b:
                    if b == FURNACE:
                        f = self.furnaces.get((x, y))
                        lit = bool(f and f["burn"] > 0)
                        scr.blit(TEX_FURNACE_ON if lit else TEX[b], pos)
                        if lit:
                            self.lights.append((x, y, 4))
                    elif b in (LEVER, LEVER_ON):
                        if nether or y > hx:
                            scr.blit(bgt, pos)
                        ori = "floor" if SOLID[w.get(x, y + 1)] else ("left" if SOLID[w.get(x - 1, y)] else
                                                                      ("right" if SOLID[w.get(x + 1, y)] else "floor"))
                        scr.blit(TEX_LEVER[(b == LEVER_ON, ori)], pos)
                    elif b in BUTTON_ON or b in BUTTON_OFF:
                        if nether or y > hx:
                            scr.blit(bgt, pos)
                        ori = "floor" if SOLID[w.get(x, y + 1)] else ("left" if SOLID[w.get(x - 1, y)] else
                                                                      ("right" if SOLID[w.get(x + 1, y)] else "floor"))
                        scr.blit(TEX_BUTTON[(0 if b in (BUTTON_STONE, BUTTON_STONE_ON) else 1, b in BUTTON_OFF, ori)], pos)
                    elif b == REDSTONE_TORCH:
                        if nether or y > hx:
                            scr.blit(bgt, pos)
                        lit_ = (x, y) in self.torch_on
                        scr.blit(TEX[b] if lit_ else TEX_TORCH_OFF, pos)
                        if lit_:
                            self.lights.append((x, y, 4))
                    elif b == REDSTONE_DUST:
                        if nether or y > hx:
                            scr.blit(bgt, pos)
                        self.draw_dust(x, y, pos)
                    elif b in TEX_OBS_ON:
                        pulsing = (self.dim, x, y) in self.obs_pulse
                        scr.blit(TEX_OBS_ON[b] if pulsing else TEX[b], pos)
                        if pulsing:
                            self.lights.append((x, y, 3))
                    elif b in ALPHA_BLOCKS:
                        if nether or y > hx:
                            scr.blit(bgt, pos)
                        scr.blit(TEX_PLATE_ON[b] if (b in TEX_PLATE_ON and (x, y) in self.active_plates) else TEX[b], pos)
                    elif b in ANIM:
                        if (b == PORTAL and nether) or (b == WATER and (nether or y > hx)):
                            scr.blit(bgt, pos)
                        scr.blit(ANIM[b][frame], pos)
                        if b in (PORTAL, END_PORTAL):
                            self.lights.append((x, y, 6))
                        elif b == LAVA and x % 2 == 0 and w.get(x, y - 1) == AIR:
                            self.lights.append((x, y, 5))
                    else:
                        scr.blit(TEX[b], pos)
                elif nether or y > hx:
                    scr.blit(bgt, pos)
        # target highlight / crack overlay
        if self.ui is None and not self.paused:
            _, _, bx, by = self.mouse_world()
            if targetable(w.get(bx, by)) and self.in_reach(bx, by):
                r = pygame.Rect(bx * TILE - cx, by * TILE - cy, TILE, TILE)
                pygame.draw.rect(scr, (255, 255, 255), r, 2)
            if self.mining:
                t, _ = break_time(w.get(*self.mining), self.held())
                if t:
                    frac = min(0.999, self.mine_prog / t)
                    scr.blit(CRACKS[int(frac * len(CRACKS))],
                             (self.mining[0] * TILE - cx, self.mining[1] * TILE - cy))

    def draw_entities(self):
        scr, cx, cy = self.screen, self.camx, self.camy
        t = pygame.time.get_ticks() / 1000.0
        for d in self.drops:
            ic = ICON_S[d.item]
            bob = math.sin(t * 3 + d.x) * 2
            scr.blit(ic, (d.x * TILE - cx - 2, d.y * TILE - cy - 8 + bob))
        for tn in self.tnts:
            flash = int(tn.fuse * 6) % 2 == 0
            scr.blit(TEX_TNT_FLASH if flash else TEX[TNT], (int(tn.x * TILE - cx), int(tn.y * TILE - cy)))
        for z in self.zombies:
            sx, sy = int(z.x * TILE - cx), int(z.y * TILE - cy)
            w_, h_ = int(z.w * TILE), int(z.h * TILE)
            if z.kind == "pigman":
                skin, shirt, pants = (225, 150, 140), (150, 85, 80), (95, 55, 50)
            else:
                skin, shirt, pants = (50, 140, 60), (45, 110, 130), (40, 50, 130)
            body = (230, 90, 90) if z.flash > 0 else skin
            pygame.draw.rect(scr, pants, (sx + 1, sy + int(h_ * 0.62), w_ // 2 - 1, int(h_ * 0.38)))
            pygame.draw.rect(scr, pants, (sx + w_ // 2, sy + int(h_ * 0.62), w_ // 2 - 1, int(h_ * 0.38)))
            pygame.draw.rect(scr, shirt if not z.flash else body, (sx, sy + w_, w_, int(h_ * 0.62) - w_))
            pygame.draw.rect(scr, body, (sx, sy, w_, w_))
            pygame.draw.rect(scr, body, (sx + (w_ if z.face > 0 else -12), sy + w_ + 2, 12, 7))
            ex = sx + (w_ - 7 if z.face > 0 else 2)
            pygame.draw.rect(scr, (10, 10, 10) if z.kind == "zombie" or not z.angry else (230, 30, 30), (ex, sy + 6, 5, 4))
            hpw = int(w_ * max(0, z.hp) / 20)
            pygame.draw.rect(scr, (180, 30, 30), (sx, sy - 7, w_, 3))
            pygame.draw.rect(scr, (60, 220, 60), (sx, sy - 7, hpw, 3))
        for c in self.crystals:
            ccx, ccy = int((c.x + c.w / 2) * TILE - cx), int((c.y + c.h / 2) * TILE - cy)
            for b in self.bosses:                           # healing beam
                if b.hp < b.MAXHP:
                    pygame.draw.line(scr, (235, 110, 225), (ccx, ccy),
                                     (int((b.x + b.w / 2) * TILE - cx), int((b.y + b.h / 2) * TILE - cy)), 2)
            if self.revive_t is not None and c.placed:
                pygame.draw.line(scr, (235, 110, 225), (ccx, ccy), (int((END_CX + 0.5) * TILE - cx), int((END_SURF - 2.0) * TILE - cy)), 3)
            r_ = 15
            rw = max(3, int(r_ * abs(math.cos(t * 2))))
            col_ = (255, 190, 190) if c.flash > 0 else (235, 100, 225)
            pygame.draw.circle(scr, (110, 40, 130), (ccx, ccy), 20, 2)
            pygame.draw.polygon(scr, col_, [(ccx, ccy - r_), (ccx + rw, ccy), (ccx, ccy + r_), (ccx - rw, ccy)])
            pygame.draw.polygon(scr, (255, 235, 255), [(ccx, ccy - r_ // 2), (ccx + rw // 2, ccy), (ccx, ccy + r_ // 2), (ccx - rw // 2, ccy)])
        for dr in self.bosses:
            sx, sy = int(dr.x * TILE - cx), int(dr.y * TILE - cy)
            bw, bh = int(dr.w * TILE), int(dr.h * TILE)
            f = dr.face
            fxx = (lambda x, w: sx + x) if f > 0 else (lambda x, w: sx + bw - x - w)
            body = (120, 40, 50) if dr.flash > 0 else (26, 20, 36)
            wing = (150, 60, 70) if dr.flash > 0 else (48, 38, 66)
            flap = math.sin(t * 6)
            tipy = sy + int(bh * 0.2) - int(70 * (0.3 + 0.7 * flap))
            sh_x = int(bw * 0.42)
            for off in (0, 26):                              # two wings, near one a bit shifted
                pygame.draw.polygon(scr, wing if off == 0 else tuple(int(v * 0.8) for v in wing),
                                    [(fxx(sh_x, 0) + 0, sy + int(bh * 0.35)), (fxx(sh_x - 70 + off, 0), tipy + off // 2),
                                     (fxx(sh_x - 18 + off, 0), tipy + 22 + off // 2), (fxx(sh_x + 22, 0), sy + int(bh * 0.5))])
            pygame.draw.rect(scr, body, (fxx(int(bw * 0.2), int(bw * 0.58)), sy + int(bh * 0.35), int(bw * 0.58), int(bh * 0.45)))
            pygame.draw.rect(scr, body, (fxx(0, int(bw * 0.24)), sy + int(bh * 0.5), int(bw * 0.24), int(bh * 0.2)))   # tail
            pygame.draw.rect(scr, body, (fxx(int(bw * 0.74), int(bw * 0.26)), sy + int(bh * 0.2), int(bw * 0.26), int(bh * 0.45)))  # head
            pygame.draw.rect(scr, (210, 70, 240), (fxx(int(bw * 0.9), 6), sy + int(bh * 0.3), 6, 5))
            pygame.draw.rect(scr, (60, 40, 80), (fxx(int(bw * 0.86), 5), sy + int(bh * 0.18) - 5, 5, 6))
        for a in self.arrows:
            ang = math.atan2(a.vy, a.vx)
            ax_, ay_ = a.x * TILE - cx, a.y * TILE - cy
            ex_, ey_ = math.cos(ang) * 11, math.sin(ang) * 11
            pygame.draw.line(scr, (150, 105, 50), (ax_ - ex_, ay_ - ey_), (ax_, ay_), 3)
            pygame.draw.line(scr, (235, 235, 235), (ax_ - ex_, ay_ - ey_), (ax_ - ex_ * 0.7, ay_ - ey_ * 0.7), 3)
            pygame.draw.circle(scr, (175, 175, 180), (int(ax_ + ex_ * 0.2), int(ay_ + ey_ * 0.2)), 3)
        for r_ in self.rockets:
            if not r_["follow"]:
                rx, ry = int(r_["x"] * TILE - cx), int(r_["y"] * TILE - cy)
                pygame.draw.rect(scr, (200, 50, 50), (rx - 2, ry - 6, 5, 11))
                pygame.draw.rect(scr, (240, 240, 240), (rx - 2, ry - 1, 5, 2))
        for sp in self.sparks:
            k_ = max(0.0, sp[4] / sp[5])
            col_ = tuple(int(v * (0.35 + 0.65 * k_)) for v in sp[6])
            pygame.draw.rect(scr, col_, (int(sp[0] * TILE - cx) - 1, int(sp[1] * TILE - cy) - 1, 3 if k_ > 0.4 else 2, 3 if k_ > 0.4 else 2))
        if self.bobber and self.bobber.get("dim") == self.dim:
            bb_ = self.bobber
            ox_ = int(bb_["x"] * TILE - cx)
            oy_ = int(bb_["y"] * TILE - cy + (5 if bb_["window"] > 0 else 0))
            hand_ = (int((self.p.x + 0.3 + self.p.face * 0.5) * TILE - cx), int((self.p.y + 0.6) * TILE - cy))
            held_ = self.held()
            if held_ and held_[0] == FISHING_ROD and math.hypot(bb_["x"] - (self.p.x + 0.3), bb_["y"] - (self.p.y + 0.9)) <= 16:
                pygame.draw.line(scr, (235, 235, 235), hand_, (ox_, oy_), 1)
            pygame.draw.circle(scr, (225, 40, 40), (ox_, oy_), 5)
            pygame.draw.circle(scr, (250, 250, 250), (ox_, oy_ - 2), 3)
        for pr in self.pearls:
            px_, py_ = int(pr.x * TILE - cx), int(pr.y * TILE - cy)
            pygame.draw.circle(scr, (20, 110, 100), (px_, py_), 6)
            pygame.draw.circle(scr, (60, 200, 170), (px_, py_), 5)
            pygame.draw.circle(scr, (225, 255, 245), (px_ - 2, py_ - 2), 2)
        for c in self.cows:
            sx, sy = int(c.x * TILE - cx), int(c.y * TILE - cy)
            bw, bh = int(c.w * TILE), int(c.h * TILE)
            fx = (lambda x, w: x) if c.face > 0 else (lambda x, w: bw - x - w)
            hide, patch = ((92, 62, 40), (235, 230, 220)) if not c.flash else ((230, 100, 100), (255, 190, 190))
            leg = math.sin(pygame.time.get_ticks() / 1000.0 * 9) * 2 if abs(c.vx) > 0.4 else 0
            for lx in (3, 10, int(bw * 0.8) - 14, int(bw * 0.8) - 7):
                pygame.draw.rect(scr, (60, 40, 28), (sx + fx(lx, 5), sy + int(bh * 0.62) + (leg if lx % 2 else -leg) * 0.5, 5, bh - int(bh * 0.62)))
            pygame.draw.rect(scr, hide, (sx + fx(0, int(bw * 0.8)), sy + int(bh * 0.1), int(bw * 0.8), int(bh * 0.55)))
            pygame.draw.rect(scr, patch, (sx + fx(8, 12), sy + int(bh * 0.18), 12, 9))
            pygame.draw.rect(scr, patch, (sx + fx(int(bw * 0.8) - 24, 10), sy + int(bh * 0.4), 10, 8))
            hx, hw, hh = int(bw * 0.62), int(bw * 0.38), int(bh * 0.5)
            pygame.draw.rect(scr, hide, (sx + fx(hx, hw), sy, hw, hh))
            pygame.draw.rect(scr, (235, 175, 165), (sx + fx(hx + hw - 9, 9), sy + hh - 10, 9, 10))
            pygame.draw.rect(scr, (240, 240, 230), (sx + fx(hx + 1, 4), sy - 3, 4, 4))
            pygame.draw.rect(scr, (240, 240, 230), (sx + fx(hx + hw - 5, 4), sy - 3, 4, 4))
            pygame.draw.rect(scr, (15, 15, 15), (sx + fx(hx + hw - 14, 3), sy + 6, 3, 3))
            if c.hp < 10:
                pygame.draw.rect(scr, (180, 30, 30), (sx, sy - 8, bw, 3))
                pygame.draw.rect(scr, (60, 220, 60), (sx, sy - 8, int(bw * max(0, c.hp) / 10), 3))
        # player
        p = self.p
        sx, sy = int(p.x * TILE - cx), int(p.y * TILE - cy)
        w_, h_ = int(p.w * TILE), int(p.h * TILE)
        if self.protect_t > 0 and (self.protect_t > 10 or int(t * 6) % 2):
            pulse = 2 + int(abs(math.sin(t * 4)) * 3)
            pygame.draw.rect(scr, (120, 190, 255), (sx - pulse, sy - pulse, w_ + 2 * pulse, h_ + 2 * pulse), 2)
        if p.invuln > 0 and int(t * 20) % 2:
            return
        leg = math.sin(p.walk * 3) * 5 if abs(p.vx) > 0.3 and p.on_ground else 0
        top_legs = sy + int(h_ * 0.62)
        pygame.draw.rect(scr, (50, 50, 150), (sx + 1, top_legs, w_ // 2 - 1, h_ - int(h_ * 0.62) - leg * 0.3))
        pygame.draw.rect(scr, (50, 50, 150), (sx + w_ // 2, top_legs, w_ // 2 - 1, h_ - int(h_ * 0.62) + leg * 0.3))
        pygame.draw.rect(scr, (0, 165, 165), (sx, sy + w_, w_, top_legs - sy - w_))
        pygame.draw.rect(scr, (205, 160, 120), (sx, sy, w_, w_))
        pygame.draw.rect(scr, (80, 50, 25), (sx, sy, w_, 6))
        ex = sx + (w_ - 7 if p.face > 0 else 2)
        pygame.draw.rect(scr, (255, 255, 255), (ex, sy + 9, 5, 4))
        pygame.draw.rect(scr, (60, 60, 200), (ex + (2 if p.face > 0 else 0), sy + 9, 3, 4))
        ACOL = {"Iron": (215, 215, 222), "Diamond": (80, 225, 225), "Netherite": (78, 68, 74)}
        hm, ch, lg, bt = self.armor
        dk = lambda c: tuple(int(v * 0.6) for v in c)
        if lg:
            c = ACOL[ITEMS[lg[0]]["tier"]]
            pygame.draw.rect(scr, c, (sx + 1, top_legs, w_ // 2 - 1, (h_ - int(h_ * 0.62)) * 0.6 - leg * 0.3))
            pygame.draw.rect(scr, c, (sx + w_ // 2, top_legs, w_ // 2 - 1, (h_ - int(h_ * 0.62)) * 0.6 + leg * 0.3))
        if bt:
            c = ACOL[ITEMS[bt[0]]["tier"]]
            for bx0, off in ((sx + 1, -leg * 0.3), (sx + w_ // 2, leg * 0.3)):
                pygame.draw.rect(scr, dk(c), (bx0, sy + h_ - 8 + off, w_ // 2 - 1, 8 - off))
        if ch and ITEMS[ch[0]].get("glider"):                     # elytra: folded on the back, spread when gliding
            cxp, shy, f = sx + w_ // 2, sy + w_ + 4, p.face
            if p.gliding:
                wings = [[(cxp, shy), (cxp - f * 30, shy - 22), (cxp - f * 46, shy + 2), (cxp - f * 36, shy + 28)],
                         [(cxp, shy + 2), (cxp - f * 20, shy - 10), (cxp - f * 34, shy + 8), (cxp - f * 24, shy + 30)]]
            else:
                wings = [[(cxp, shy), (cxp - f * 10, shy + 3), (cxp - f * 8, shy + 22), (cxp, shy + 16)]]
            for k_, pts in enumerate(wings):
                pygame.draw.polygon(scr, (175, 165, 200) if k_ == 0 else (140, 130, 168), pts)
                pygame.draw.polygon(scr, (95, 85, 125), pts, 2)
        elif ch:
            c = ACOL[ITEMS[ch[0]]["tier"]]
            pygame.draw.rect(scr, c, (sx, sy + w_, w_, top_legs - sy - w_))
            pygame.draw.rect(scr, dk(c), (sx, sy + w_, w_, top_legs - sy - w_), 2)
        if hm:
            c = ACOL[ITEMS[hm[0]]["tier"]]
            pygame.draw.rect(scr, c, (sx - 1, sy - 2, w_ + 2, 9))
            pygame.draw.rect(scr, dk(c), (sx - 1, sy - 2, w_ + 2, 9), 2)
            pygame.draw.rect(scr, c, (sx - 1 if p.face > 0 else sx + w_ - 4, sy + 7, 5, 8))
        if self.bow_on:                                     # draw-strength bar
            pygame.draw.rect(scr, (20, 20, 20), (sx - 6, sy - 14, 28, 6))
            pygame.draw.rect(scr, (255, 220, 90) if self.bow_t >= 1.0 else (210, 210, 210), (sx - 5, sy - 13, int(26 * self.bow_t), 4))
        # arm + held item
        sw_ = math.sin(t * 22) * 8 if p.swing > 0 else 0
        ax = sx + (w_ - 3 if p.face > 0 else -5)
        pygame.draw.rect(scr, (205, 160, 120), (ax, sy + w_ + 2 + sw_ * 0.5, 8, 14))
        s = self.held()
        if s:
            ic = ICON_S[s[0]]
            ix = ax + (6 if p.face > 0 else -14) + sw_ * p.face * 0.5
            scr.blit(ic if p.face > 0 else pygame.transform.flip(ic, True, False), (ix, sy + w_ + 8 + sw_))

    def draw_hud(self):
        scr = self.screen
        S = self.SLOT
        x0, y0 = (SW - 9 * S) // 2, SH - S - 10
        bar = pygame.Surface((9 * S, S), pygame.SRCALPHA)
        bar.fill((20, 20, 20, 150))
        scr.blit(bar, (x0, y0))
        for i in range(9):
            r = pygame.Rect(x0 + i * S + 2, y0 + 2, 40, 40)
            pygame.draw.rect(scr, (255, 255, 255) if i == self.sel else (90, 90, 90), r, 3 if i == self.sel else 1)
            self.draw_stack(self.inv[i], r)
        if not self.creative:                      # experience bar over the hotbar
            lv = self.xp_level()
            frac = (self.xp - self.xp_for_level(lv)) / float(10 + 5 * lv)
            pygame.draw.rect(scr, (30, 30, 30), (x0, y0 - 5, 9 * S, 4))
            pygame.draw.rect(scr, (110, 230, 70), (x0, y0 - 5, int(9 * S * frac), 4))
            if lv > 0:
                self.txt(str(lv), (x0 + 9 * S // 2, y0 - 62), (120, 255, 90), center=True)
        hp = self.p.hp
        for i in range(10):
            v = 2 if hp >= (i + 1) * 2 else (1 if hp > i * 2 else 0)
            scr.blit(self.hearts[v], (x0 + i * 18, y0 - 22))
        if not self.creative:                      # hunger: 10 drumsticks, right-aligned
            for i in range(10):
                hx_ = x0 + 9 * S - 20 - i * 20
                hy_ = y0 - 24
                full, half = self.food >= (i + 1) * 2, self.food > i * 2
                meat = (205, 120, 60) if full else ((150, 95, 55) if half else (65, 48, 40))
                pygame.draw.circle(scr, meat, (hx_ + 7, hy_ + 7), 7)
                pygame.draw.circle(scr, (40, 25, 20), (hx_ + 7, hy_ + 7), 7, 1)
                pygame.draw.line(scr, (235, 225, 205) if half else (110, 100, 90), (hx_ + 11, hy_ + 11), (hx_ + 17, hy_ + 17), 3)
                if full:
                    pygame.draw.circle(scr, (240, 170, 110), (hx_ + 5, hy_ + 5), 2)
        pts = self.armor_points()
        for i in range(pts // 2 + pts % 2):          # same size and spacing as the hearts (17x15, 18 apart)
            ax_, ay_ = x0 + i * 18, y0 - 42
            full = pts >= (i + 1) * 2
            shield = [(ax_, ay_), (ax_ + 16, ay_), (ax_ + 16, ay_ + 7), (ax_ + 8, ay_ + 14), (ax_, ay_ + 7)]
            pygame.draw.polygon(scr, (200, 205, 215) if full else (140, 145, 155), shield)
            pygame.draw.polygon(scr, (60, 62, 70), shield, 2)
        if self.p.air < 9.95 and not self.creative:
            for i in range(int(math.ceil(self.p.air))):
                bx_ = x0 + 9 * S - 8 - i * 18
                pygame.draw.circle(scr, (170, 210, 255), (bx_, y0 - 44), 6)
                pygame.draw.circle(scr, (235, 245, 255), (bx_ - 2, y0 - 46), 2)
        for dr in self.bosses:
            bx0, bwid = SW // 2 - 190, 380
            self.txt("Ender Dragon", (SW // 2, 14), (235, 200, 250), center=True)
            pygame.draw.rect(scr, (30, 15, 40), (bx0, 28, bwid, 12))
            pygame.draw.rect(scr, (190, 60, 220), (bx0, 28, int(bwid * max(0.0, dr.hp) / dr.MAXHP), 12))
            pygame.draw.rect(scr, (255, 255, 255), (bx0, 28, bwid, 12), 2)
        if self.p.gliding:
            self.txt("Gliding  %d m/s" % int(self.p.glide_v), (SW // 2, 56), (210, 200, 245), center=True)
        if self.name_t > 0 and self.held():
            self.txt(stack_name(self.held()), (SW // 2, y0 - 38), center=True)
        if self.creative:
            self.txt("CREATIVE" + ("  (flying)" if self.p.flying else ""), (SW - 190, 10), (255, 220, 120))
        if self.protect_t > 0:
            m, sec = divmod(int(math.ceil(self.protect_t)), 60)
            self.txt("Protection  %d:%02d" % (m, sec), (SW - 190, 34), (140, 200, 255))
        if self.msg_t > 0:
            self.txt(self.msg, (SW // 2, 50), (255, 255, 160), center=True)
        if self.debug:
            p = self.p
            lines = ["FPS %d" % self.clock.get_fps(), "XY %.1f %.1f" % (p.x, p.y),
                     "Day phase %.2f light %.2f" % ((self.time / DAY_LEN) % 1, self.light),
                     "Dim %d  mobs %d  drops %d  seed %d" % (self.dim, len(self.zombies), len(self.drops), self.world.seed)]
            for i, l in enumerate(lines):
                self.txt(l, (8, 8 + 18 * i), font=self.small)
            self.txt("Saved coordinates (F2 adds):" if self.waypoints else "F2 saves your coordinates here",
                     (8, 8 + 18 * len(lines) + 8), (255, 230, 140), font=self.small)
            mpos = self.mouse_pos()
            for i, text, btn in self.waypoint_rows():
                self.txt(text, (8, btn.y + 2), font=self.small)
                hot = btn.collidepoint(mpos)
                pygame.draw.rect(self.screen, (215, 70, 70) if hot else (150, 55, 55), btn)
                pygame.draw.rect(self.screen, (255, 255, 255), btn, 1)
                self.txt("x", btn.center, font=self.small, center=True)
                tp = self.tp_rect(btn)
                pygame.draw.rect(self.screen, (70, 175, 90) if tp.collidepoint(mpos) else (50, 130, 70), tp)
                pygame.draw.rect(self.screen, (255, 255, 255), tp, 1)
                self.txt("TP", tp.center, font=self.small, center=True)

    def draw_stack(self, s, r):
        if not s:
            return
        self.screen.blit(ICON[s[0]], (r.x + 4, r.y + 4))
        if ench_of(s):
            gl = getattr(self, "_glint", None)
            if gl is None:
                gl = self._glint = pygame.Surface((32, 32), pygame.SRCALPHA)
                gl.fill((170, 90, 255, 80))
            self.screen.blit(gl, (r.x + 4, r.y + 4))
            pygame.draw.rect(self.screen, (190, 120, 255), (r.x + 3, r.y + 3, 34, 34), 1)
        if s[1] > 1:
            self.txt(str(s[1]), (r.right - 4 - self.small.size(str(s[1]))[0], r.bottom - 15), font=self.small)
        if s[2] is not None and "dur" in ITEMS[s[0]]:
            frac = s[2] / ITEMS[s[0]]["dur"]
            pygame.draw.rect(self.screen, (20, 20, 20), (r.x + 4, r.bottom - 7, 32, 4))
            pygame.draw.rect(self.screen, lerpc((220, 40, 40), (60, 220, 60), frac),
                             (r.x + 4, r.bottom - 7, int(32 * frac), 4))

    def draw_ui(self):
        if self.ui == "book":
            self.bk_draw()
            return
        scr = self.screen
        dim = pygame.Surface((SW, SH), pygame.SRCALPHA)
        dim.fill((0, 0, 0, 120))
        scr.blit(dim, (0, 0))
        pr = self.panel_rect()
        pygame.draw.rect(scr, (198, 198, 198), pr)
        pygame.draw.rect(scr, (255, 255, 255), pr, 3)
        pygame.draw.rect(scr, (60, 60, 60), pr.inflate(6, 6), 3)
        title = {"inv": "Crafting (2x2)", "table": "Crafting Table", "furnace": "Furnace", "chest": "Chest",
                 "enchant": "Enchanting Table", "grind": "Grindstone"}[self.ui]
        if self.ui == "chest":
            title = self.chest_name
        self.txt(title, (pr.x + 12, pr.y + 6), (50, 50, 50))
        if self.ui == "grind":
            st = self.grind_slot[0]
            r = self.ench_buttons()[1]
            ok = bool(st and ench_of(st))
            pygame.draw.rect(scr, (110, 110, 118) if ok else (125, 125, 125), r)
            pygame.draw.rect(scr, (45, 45, 52), r, 2)
            lab = ("Remove enchantments%s" % ("" if self.creative else "  (+%d XP)" % self.grind_xp(st))) if ok \
                else ("Put an item in the slot" if not st else "Nothing to remove")
            self.txt(lab, r.center, (255, 255, 255) if ok else (210, 210, 210), center=True)
        if self.ui == "enchant":
            st = self.ench_slot[0]
            self.txt("Level: %s" % ("free (creative)" if self.creative else self.xp_level()),
                     (pr.x + 12, pr.y + 106), (50, 90, 40), self.small)
            for i, r in enumerate(self.ench_buttons()):
                o = self.ench_offer(st, i)
                ok = bool(o) and (self.creative or self.xp_level() >= o[2])
                pygame.draw.rect(scr, (110, 70, 160) if ok else (125, 125, 125), r)
                pygame.draw.rect(scr, (45, 25, 70), r, 2)
                if o:
                    lab = "%s  -  %s" % (ench_label(o[0], o[1]), "free" if self.creative else "%d levels" % o[2])
                else:
                    lab = "Put an item in the slot" if not st else "Nothing to add"
                self.txt(lab, r.center, (255, 255, 255) if ok else (210, 210, 210), center=True)
        if self.creative and self.ui == "chest":
            bb, sb = self.stress_buttons()
            for r, label, ok in ((bb, "Fill: 27 books", True), (sb, "Fill: 729 books", self.chest_name != "Shulker Box")):
                pygame.draw.rect(scr, (150, 72, 72) if ok else (130, 130, 130), r)
                pygame.draw.rect(scr, (75, 30, 30), r, 2)
                self.txt(label, r.center, (255, 255, 255), center=True)
        self.txt("Inventory", (pr.x + 12, pr.y + 158), (50, 50, 50))
        mpos = self.mouse_pos()
        tip = None
        res = self.craft_result() if self.ui in ("inv", "table") else None
        layout = self.ui_layout()
        for kind, cont, idx, r in layout:
            pygame.draw.rect(scr, (139, 139, 139), r)
            pygame.draw.rect(scr, (55, 55, 55), r, 2)
            if kind == "out":
                if res:
                    self.draw_stack([res[0], res[1], None], r)
                    if r.collidepoint(mpos):
                        tip = ITEMS[res[0]]["name"]
            else:
                s = cont[idx]
                self.draw_stack(s, r)
                if cont is self.armor and not s:
                    self.txt("HCLB"[idx], r.center, (110, 110, 110), center=True)
                if s and r.collidepoint(mpos):
                    tip = stack_name(s)
                    if s[0] == SHULKER_BOX and isinstance(s[2], list):
                        tip += " (%d stacks inside)" % sum(1 for x in s[2] if x)
                    if s[0] == BOOK and isinstance(s[2], dict):
                        tip += " (%d pages)" % len(s[2].get("pages", []))
        if self.ui == "inv":
            self.txt("Armor: %d" % self.armor_points(), (pr.x + 12, pr.y + 36 + 2 * self.SLOT), (50, 50, 50), self.small)
        if self.ui == "furnace":
            f = self.cur_furnace
            base = pr.x + 12 + 3 * self.SLOT
            fy = pr.y + 30 + self.SLOT
            pygame.draw.rect(scr, (80, 80, 80), (base + 6, fy + 2, 28, 36))
            if f["burn"] > 0:
                h = int(36 * f["burn"] / max(1e-6, f["burnmax"]))
                pygame.draw.rect(scr, (255, 150, 30), (base + 6, fy + 2 + 36 - h, 28, h))
            pygame.draw.rect(scr, (80, 80, 80), (base + 52, fy + 14, 90, 12))
            pygame.draw.rect(scr, (240, 240, 240), (base + 52, fy + 14, int(90 * f["prog"] / SMELT_TIME), 12))
            self.txt("fuel", (base + 40, pr.y + 30 + 2 * self.SLOT + 12), (50, 50, 50), self.small)
        if self.ui in ("inv", "table"):
            ox = [r for k, c, i, r in layout if k == "out"][0]
            pygame.draw.polygon(scr, (90, 90, 90), [(ox.x - 28, ox.centery - 8), (ox.x - 12, ox.centery),
                                                    (ox.x - 28, ox.centery + 8)])
        if self.ui in ("inv", "table", "furnace"):
            tip = self.draw_book(mpos) or tip
        if self.creative:
            pp = self.palette_panel()
            pygame.draw.rect(scr, (198, 198, 198), pp)
            pygame.draw.rect(scr, (255, 255, 255), pp, 3)
            pygame.draw.rect(scr, (60, 60, 60), pp.inflate(6, 6), 3)
            self.txt("Creative items", (pp.x + 12, pp.y + 6), (50, 50, 50))
            if self.pal_max_scroll():
                tk, th = self.pal_track(), self.pal_thumb()
                pygame.draw.rect(scr, (120, 120, 120), tk)
                pygame.draw.rect(scr, (55, 55, 55), tk, 2)
                hot_ = self.pal_drag or th.collidepoint(mpos)
                pygame.draw.rect(scr, (235, 235, 235) if hot_ else (190, 190, 190), th)
                pygame.draw.rect(scr, (60, 60, 60), th, 2)
                self.txt("%d-%d / %d" % (self.pal_scroll + 1, self.pal_scroll + self.pal_vis(), self.pal_rows()),
                         (pp.right - 92, pp.y + 8), (70, 70, 70), font=self.small)
            for it, r in self.palette_rects():
                pygame.draw.rect(scr, (139, 139, 139), r)
                pygame.draw.rect(scr, (55, 55, 55), r, 2)
                self.draw_stack([it, 1, None], r)
                if r.collidepoint(mpos):
                    tip = ITEMS[it]["name"]
            cb = self.clear_button()
            armed = self.clear_t > 0
            pygame.draw.rect(scr, (205, 60, 60) if armed else (150, 72, 72), cb)
            pygame.draw.rect(scr, (255, 255, 255) if armed else (75, 30, 30), cb, 2)
            self.txt("Click again to confirm!" if armed else "Clear inventory", cb.center, (255, 255, 255), center=True)
        if self.cursor:
            r = pygame.Rect(mpos[0] - 20, mpos[1] - 20, 40, 40)
            self.draw_stack(self.cursor, r)
        elif tip:
            self.txt(tip, (mpos[0] + 14, mpos[1] - 22), (255, 255, 255))

    def glow(self, r):
        g = self.glow_cache.get(r)
        if g is None:
            size = r * TILE // 2
            g = pygame.Surface((size, size), pygame.SRCALPHA)
            c = size / 2
            for yy in range(size):
                for xx in range(size):
                    d = min(1.0, math.hypot(xx - c, yy - c) / c)
                    g.set_at((xx, yy), (255, 255, 255, int(255 * d ** 1.4)))
            self.glow_cache[r] = g
        return g

    def draw_nether_light(self):
        qs = 4
        dark = pygame.Surface((SW // qs + 1, SH // qs + 1), pygame.SRCALPHA)
        dark.fill((22, 0, 6, 195))
        for x, y, r in self.lights[:120] + [(None, None, 4)]:
            g = self.glow(r)
            if x is None:
                cx, cy = int(self.p.x * TILE + 0.3 * TILE - self.camx), int(self.p.y * TILE + 0.9 * TILE - self.camy)
            else:
                cx, cy = x * TILE - self.camx + TILE // 2, y * TILE - self.camy + TILE // 2
            dark.blit(g, (cx // qs - g.get_width() // 2, cy // qs - g.get_height() // 2),
                      special_flags=pygame.BLEND_RGBA_MIN)
        self.screen.blit(pygame.transform.smoothscale(dark, (dark.get_width() * qs, dark.get_height() * qs)), (0, 0))

    def draw(self):
        self.draw_sky()
        self.draw_world()
        self.draw_entities()
        for bx_, by_, age in self.booms:
            k = age / 0.5
            rad = int((1.5 + 3.5 * min(1.0, k * 2)) * TILE * (1 - 0.3 * k))
            sx_, sy_ = int(bx_ * TILE - self.camx), int(by_ * TILE - self.camy)
            pygame.draw.circle(self.screen, (255, 200, 60), (sx_, sy_), rad, max(2, int(10 * (1 - k))))
            pygame.draw.circle(self.screen, (255, 120, 30), (sx_, sy_), int(rad * 0.6), max(2, int(8 * (1 - k))))
            if k < 0.4:
                pygame.draw.circle(self.screen, (255, 245, 200), (sx_, sy_), int(rad * 0.35))
        # night + depth darkness
        depth = max(0.0, self.p.y - self.world.height[int(self.p.x)] - 10)
        a = int((1 - self.light) * 140 + min(80, depth * 1.6))
        if self.dim == 1:
            self.draw_nether_light()
        elif a > 0 and self.dim == 0:
            ov = pygame.Surface((SW, SH), pygame.SRCALPHA)
            ov.fill((0, 0, 25, min(190, a)))
            self.screen.blit(ov, (0, 0))
        if self.portal_t > 0:
            ov = pygame.Surface((SW, SH), pygame.SRCALPHA)
            ov.fill((120, 40, 190, int(min(1.0, self.portal_t / 3.0) * 170)))
            self.screen.blit(ov, (0, 0))
        self.draw_hud()
        self.draw_console()
        if self.ui:
            self.draw_ui()
        if self.paused:
            dim = pygame.Surface((SW, SH), pygame.SRCALPHA)
            dim.fill((0, 0, 0, 150))
            self.screen.blit(dim, (0, 0))
            self.txt("PAUSED", (SW // 2, SH // 2 - 50), font=self.big, center=True)
            self.txt("Esc: resume    F5: creative mode    F6: save    M: save & world menu    X: save & quit", (SW // 2, SH // 2 + 5), center=True)
        pygame.display.flip()

    # ----- main loop ------------------------------------------------------- #
    def quit(self):
        self.save()
        pygame.quit()
        sys.exit(0)

    def run(self):
        self.camx = self.camy = 0
        if self.use_menu:
            self.open_menu()
            self.use_menu = False
        while True:
            if self.menu is not None:
                self.menu_frame()
                continue
            dt = min(self.clock.tick(60) / 1000.0, 0.04)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.quit()
                elif e.type == pygame.KEYDOWN:
                    if self.cmd is not None and e.key != pygame.K_F11:
                        self.cmd_key(e.key, getattr(e, "unicode", ""))
                    elif self.ui == "book" and e.key != pygame.K_F11:
                        self.bk_key(e.key, getattr(e, "unicode", ""))
                    else:
                        self.on_key(e.key)
                elif e.type == pygame.MOUSEWHEEL and self.ui and self.creative and not self.paused:
                    if self.palette_panel().collidepoint(self.mouse_pos()):
                        self.pal_scroll_by(-e.y)
                elif e.type == pygame.MOUSEWHEEL and not self.ui and not self.paused and self.cmd is None:
                    self.select(self.sel - e.y)
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    self.on_click(e.pos, e.button)
            self.update(dt)
            self.draw()


if __name__ == "__main__":
    Game(new="--new" in sys.argv, menu="--new" not in sys.argv).run()
