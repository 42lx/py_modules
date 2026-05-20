"""ex0 test driver — exercises factories and a base-vs-base fight."""
from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(a: CreatureFactory, b: CreatureFactory) -> None:
    print("Testing battle")
    fighter_a = a.create_base()
    fighter_b = b.create_base()
    print(fighter_a.describe())
    print("vs.")
    print(fighter_b.describe())
    print("fight!")
    print(fighter_a.attack())
    print(fighter_b.attack())


def main() -> None:
    try:
        flame = FlameFactory()
        aqua = AquaFactory()
        test_factory(flame)
        test_factory(aqua)
        test_battle(flame, aqua)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
