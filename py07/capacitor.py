from typing import Any

from ex0 import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def show_healer(creature: Any) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def show_transformer(creature: Any) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print("base:")
    show_healer(factory.create_base())
    print("evolved:")
    show_healer(factory.create_evolved())


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print("base:")
    show_transformer(factory.create_base())
    print("evolved:")
    show_transformer(factory.create_evolved())


def main() -> None:
    try:
        test_healing(HealingCreatureFactory())
        test_transform(TransformCreatureFactory())
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
