from ex0 import CreatureFactory, FlameFactory, AquaFactory


def single(factory: CreatureFactory):
    print("Testing factory")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory):
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    single(flame_factory)
    print()
    aqua_factory = AquaFactory()
    single(aqua_factory)
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
