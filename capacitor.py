
#  base:
# Sproutling is a Grass type Creature
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount
#  evolved:
# Bloomelle is a Grass/Fairy type Creature
# Bloomelle uses Petal Dance!
# Bloomelle heals itself and others for a large amount
#
# Testing Creature with transform capability
#  base:
# Shiftling is a Normal type Creature
# Shiftling attacks normally.
# Shiftling shifts into a sharper form!
# Shiftling performs a boosted strike!
# Shiftling returns to normal.
#  evolved:
# Morphagon is a Normal/Dragon type Creature
# Morphagon attacks normally.
# Morphagon morphs into a dragonic battle form!
# Morphagon unleashes a devastating morph strike!
# Morphagon stabilizes its form.

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import Creature


def test_healing(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def test_transform(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def main() -> None:
    heal_fac = HealingCreatureFactory()
    tran_fac = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    print(" base:")
    test_healing(heal_fac.create_base())
    print(" evolved:")
    test_healing(heal_fac.create_evolved())
    print()
    print("Testing Creature with transform capability")
    print(" base:")
    test_transform(tran_fac.create_base())
    print(" evolved:")
    test_transform(tran_fac.create_evolved())


if __name__ == "__main__":
    main()
