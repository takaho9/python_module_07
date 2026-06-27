from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, \
                NormalStrategy, \
                AggressiveStrategy, \
                DefensiveStrategy, \
                StrategyError


def battle(
    a: tuple[CreatureFactory, BattleStrategy],
    b: tuple[CreatureFactory, BattleStrategy]
):
    print("* Battle *")
    factory_a, strategy_a = a
    factory_b, strategy_b = b
    base_a = factory_a.create_base()
    base_b = factory_b.create_base()
    print(base_a.describe())
    print(" vs.")
    print(base_b.describe())
    print(" now fight!")
    strategy_a.act(base_a)
    strategy_b.act(base_b)


def single(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    len_opponents = len(opponents)
    print(f"{len_opponents} opponents involved")
    for i in range(len_opponents):
        for j in range(i+1, len_opponents):
            battle(opponents[i], opponents[j])


def main() -> None:
    print("Tournament 0 (basic)")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    try:
        single(opponents)
    except StrategyError as e:
        print(f"Battle error, aborting tournament: {e}")

    print("Tournament 1 (error)")
    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    try:
        single(opponents)
    except StrategyError as e:
        print(f"Battle error, aborting tournament: {e}")

    print("Tournament 2 (multiple)")
    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    try:
        single(opponents)
    except StrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    main()
