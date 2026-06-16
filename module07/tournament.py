import ex0
import ex1
import ex2

print("Tournament 0 (basic)")
print("[ (Flameling+Normal), (Healing+Defensive) ]")
print("*** Tournament ***")
print("2 opponents involved")
print("* Battle *")
flameling = ex0.FlameFactory().create_base()
pyrodon = ex0.FlameFactory().create_evolved()
aquabub = ex0.AquaFactory().create_base()
torragon = ex0.AquaFactory().create_evolved()
shiftling = ex1.TransformCreatureFactory().create_base()
Morphagon = ex1.TransformCreatureFactory().create_base()
sproutling = ex1.HealingCreatureFactory().create_base()
bloomelle = ex1.HealingCreatureFactory().create_evolved()
print(flameling.describe())
print("vs.")
print(sproutling.describe())
print("now fight!")
ex2.NormalStrategy().act(flameling)
ex2.DefensiveStrategy().act(sproutling)
print("Tournament 1 (error)")
print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
*** Tournament ***
2 opponents involved
* Battle *
Flameling is a Fire type Creature
vs.
Sproutling is a Grass type Creature
now fight!
Battle error, aborting tournament: Invalid Creature 'Flameling' for this aggressive strategy
Tournament 2 (multiple)
[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]
*** Tournament ***
3 opponents involved
* Battle *
Aquabub is a Water type Creature
vs.
Sproutling is a Grass type Creature
now fight!
Aquabub uses Water Gun!
Sproutling uses Vine Whip!
Sproutling heals itself for a small amount
* Battle *
Aquabub is a Water type Creature
vs.
Shiftling is a Normal type Creature
now fight!
Aquabub uses Water Gun!
Shiftling shifts into a sharper form!
Shiftling performs a boosted strike!
Shiftling returns to normal.
* Battle *
Sproutling is a Grass type Creature
vs.
Shiftling is a Normal type Creature
now fight!
Sproutling uses Vine Whip!
Sproutling heals itself for a small amount
Shiftling shifts into a sharper form!
Shiftling performs a boosted strike!
Shiftling returns to normal.