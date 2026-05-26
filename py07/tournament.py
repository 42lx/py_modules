from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = [(factory.create_base(), strat) for factory, strat in opponents]
    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            a, sa = fighters[i]
            b, sb = fighters[j]
            print("* Battle *")
            print(a.describe())
            print("vs.")
            print(b.describe())
            print("now fight!")
            sa.act(a)
            sb.act(b)


def run_tournament(opponents: list[Opponent]) -> None:
    try:
        battle(opponents)
    except InvalidStrategyError as exc:
        print(f"Battle error, aborting tournament: {exc}")


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament(
        [(FlameFactory(), normal), (HealingCreatureFactory(), defensive)]
    )

    print("")
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    run_tournament(
        [(FlameFactory(), aggressive), (HealingCreatureFactory(), defensive)]
    )

    print("")
    print("Tournament 2 (multiple)")
    print(
        "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
    )
    run_tournament([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])


if __name__ == "__main__":
    main()
