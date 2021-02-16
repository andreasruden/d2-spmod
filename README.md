# Mod Overview
This game rebalances drop rates & gambling rates to be SSF viable & fun.
Rebalancing decisions for drop rates is based on https://github.com/andreasruden/d2-dropsimulator .

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
Drop Rates:
  Unique: 140
  UniqueDivisor: 1
  UniqueMin: 3200
  Rare: 40
  RareDivisor: 2
  RareMin: 1600
  Set: 70
  SetDivisor: 3
  SetMin: 2400
Meaning:
  At 0 mf: There will drop roughly 3 times the uniques, rares and set items.
  
# TreasureClassEx.txt:
- Made higher Runes a lot more common (chane to downgrade is much smaller).
- Trippled gold drop from special sources (bosses, uniques). Doubled gold from other already increased sources.
- Made chests drop more loot and less chance for junk.
- Made the "good" TCs less likely to drop bad gems in hell & nightmare. I.e., more likely to drop runes or good jewelry.
- Countess now always drops 3 runes.
- Rebalanced drop rates of runes r01-r24 (El-Ist) to be farmable at Countess at more linear rates.

# MagicPrefix.txt and MagicSuffix.txt:
Modifiers now spawn with equal weight regardless of tier, to make it more likely to find good rare items when playing solo.

# Experience.Txt:
Experience gain no longer drops off starting at level 70.
Total experience needed for each level has been modified in the following way:
   1-30: 50% -> 100% increased leveling speed
  31-50: 55% ->  80% increased leveling speed
  51-70: 60% ->  65% increased leveling speed
  71+:   65% ->  50% increased leveling speed
