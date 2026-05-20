"""ex1 test driver — heal + transform capability families."""
from ex0 import Creature, CreatureFactory
from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def show_healer(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())


def show_transformer(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
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
