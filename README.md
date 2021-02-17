# Mod Overview
This game rebalances drop rates & gambling rates to be SSF viable & fun.
Rebalancing decisions for drop rates is based on https://github.com/andreasruden/d2-dropsimulator .

The core goal is for a person who plays a moderate amount, which was defined as 150 hours,
will have a good chance of collecting the items he needs for his build. And for someone who
plays a very high amount, which was defined as 800 hours, to have a finished collection
with very high probability. Where finished collection means having found all uniques, set
items and runes, at least once.

The mod is balanced around playing without MF gear and/or goldfind gear at /players 1.
By having a weapon swap for more mf, or wearing MF-intended gear you will likely worsen
the experience, as the game has already been sped up a lot. I have considered wether
I ought to disable or nerf MF and GF, but this poses problems (e.g. it'd not be much
fun finding some items, like tal'rasha's armor). As such it has been unchanged, but
it's my recommendation to use combat-focused pieces, instead of aiming for specific MF.

# DifficultyLevels.txt
Gambling Probabilities Changed:
  Unique: 0.05% -> 7.5% (roll always happens)
  Set: 0.1% -> 12.5% (roll happens only if unique fails)
  Rare: 10% -> 35% (roll happens only if unique and set fails)
  Exceptional: 0.9% -> 25% (roll always happens)
  Elite: 0.33% -> 12.5% (roll only happens if exceptional succeeds => chance of elite: 0.0027% -> 3.125%)
      E[X=#Gambles for 1 Normal Unique] ~= 13
      E[X=#Gambles for 1 Exceptional Unique] ~= 50
      E[X=#Gambles for 1 Elite Unique] ~= 430
Meaning: Gambling for uniques and sets is quite profitable if you have gold.

# ItemRatio.txt
Drop rates have been returned in accordance with the core goals stated above.
All changes have been guided by the d2 drop simulator & probabilities calculator.
Another defining change is that exceptional/elite items no longer have a smaller ratio.
That means their ratio of appearance now only differs in their base items being rarer.

**NOTE:** When making these ratios we have to keep in mind that only 22% of item bases
exist as set items, whereas 70% of item bases have a unique variant. As such a
lower ratio for sets (when compared to uniques) does not automatically translate
to more dropped set items.
  
# TreasureClassEx.txt:
- Made higher Runes a lot more common (chane to downgrade is much smaller).
- Trippled gold drop from special sources (bosses, uniques). Doubled gold from other already increased sources.
- Made chests drop more loot and less chance for junk.
- Made the "good" TCs less likely to drop bad gems in hell & nightmare. I.e., more likely to drop runes or good jewelry.
- Countess now always drops 3 runes.
- Rebalanced drop rates of runes r01-r24 (El-Ist) to be farmable at Countess at more linear rates.

# UniqueItems.txt
- Weighting of unique rings have been rebalanced.
  From:
  Nagelring (15), Manald (15), Dwarf Star (10), Raven Frost (10),
  Carrion Wind (3), Natures Peace (3), Jordan (1), Bulkathos (1), Wisp (1)
  To:
  Nagelring (8), Manald (8), Dwarf Star (6), Raven Frost (6),
  Carrion Wind (4), Natures Peace (4), Jordan (2), Bulkathos (2), Wisp (2)

- Weighting of amulets have changed a bit:
  Nokozan (20) -> (10), Mahim (10) -> (7) Seraph (3) -> (5), Metalgrid (2) -> (5)

- The Following uniques have had their weighting decreased additionaly:
    Venomsward, Bladebone, Bloodrise, Rusthandle, Griswold's Edge, Soul Harvest,
    Bloodthief, Hawkmail, The Chieftain, Soulflay, Twitchthroe, Shadowfang,	Duskdeep,
    Sparking Mail, Steelclash, Deathspade, Gleamscythe, Steelgoad, Crushflange, Mindrend,
    The Generals Tan Do Li Ga, Goreshovel, Hellplague, Lance of Yaggai, Razortine,
    Stormeye, Bonesob, Kinemils Awl, The Battlebranch, Nagelring, Manald Heal,
    Coil of Glory, Darkglow, Stormguild, Krintizs Skewer, Frostburn, Tearhaunch, Woestave

- The Following uniques have been made less rare (sorted by order of rarity):
  - Tyrael's Might (1:1 templars, uar 87)
  - Griffon's Eye (ci3, 84)
  - Deaths's Web (7gw, 74)
  - Earthshifter (7gm, 77)
  - The Cranium Basher (7gm, 85)
  - Windforce (6lw, 80)
  - Mang Song's Lesson (6ws, 86)
  - Stormspire (7wc, 78)
  - Ghostflame (7bl, 70)

# MagicPrefix.txt and MagicSuffix.txt:
Modifiers now spawn with equal weight regardless of tier, to make it more likely to find good rare items when playing solo.

# Experience.Txt:
Experience gain no longer drops off starting at level 70.
Total experience needed for each level has been modified in the following way:
   1-30: 50% -> 100% increased leveling speed
  31-50: 55% ->  80% increased leveling speed
  51-70: 60% ->  65% increased leveling speed
  71+:   65% ->  50% increased leveling speed
