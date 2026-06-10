from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def guarded(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return guarded


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [s(target, power) for s in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shields {target} with {power} armor"


def main() -> None:
    test_values = [9, 11, 15]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    target = test_targets[0]

    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    a, b = combo(target, 30)
    print(f"Combined spell result: {a}, {b}")
    print()

    print("Testing power amplifier...")
    base_power = test_values[0]
    amplified = power_amplifier(fireball, 3)
    print(f"Original: {base_power}, Amplified: {base_power * 3}")
    print(amplified(target, base_power))
    print()

    print("Testing conditional caster...")
    powerful_only = conditional_caster(
        lambda t, p: p >= 20, fireball
    )
    print(powerful_only(target, 25))
    print(powerful_only(target, 5))
    print()

    print("Testing spell sequence...")
    seq = spell_sequence([fireball, heal, shield])
    for result in seq(target, test_values[2]):
        print(f"  {result}")


if __name__ == "__main__":
    main()
