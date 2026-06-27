from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    heal_fac = HealingCreatureFactory()
    heal_base = heal_fac.create_base()
    heal_evolved = heal_fac.create_evolved()
    tran_fac = TransformCreatureFactory()
    tran_base = tran_fac.create_base()
    tran_evolved = tran_fac.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    print(heal_base.describe())
    print(heal_base.attack())
    print(heal_base.heal())
    print(" evolved:")
    print(heal_evolved.describe())
    print(heal_evolved.attack())
    print(heal_evolved.heal())
    print()
    print("Testing Creature with transform capability")
    print(" base:")
    print(tran_base.describe())
    print(tran_base.attack())
    print(tran_base.transform())
    print(tran_base.attack())
    print(tran_base.revert())
    print(" evolved:")
    print(tran_evolved.describe())
    print(tran_evolved.attack())
    print(tran_evolved.transform())
    print(tran_evolved.attack())
    print(tran_evolved.revert())


if __name__ == "__main__":
    main()
