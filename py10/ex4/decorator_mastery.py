import time
import functools
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power')
            if power is None:
                power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return (
                f"Spell casting failed after {max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(c.isalpha() or c == ' ' for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    raise RuntimeError("magic surge")


def make_eventual_spell() -> Callable:
    attempts = 0

    @retry_spell(max_attempts=3)
    def eventual_spell() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise RuntimeError("not yet...")
        return "Waaaaaaagh spelled !"

    return eventual_spell


@power_validator(min_power=20)
def meteor(power: int) -> str:
    return f"Meteor strikes for {power} damage!"


def main() -> None:
    test_powers = [29, 14, 7, 12]
    spell_names = ['heal', 'tornado', 'freeze', 'tsunami']
    mage_names = ['Nova', 'Riley', 'Sage', 'Kai', 'Casey', 'Luna']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")
    print()

    print("Testing retrying spell...")
    print(unstable_spell())
    print(make_eventual_spell()())
    print()

    print("Testing standalone power validator...")
    for p in test_powers:
        print(f"power={p}: {meteor(p)}")
    print()

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("Jo"))
    guild = MageGuild()
    for name, p in zip(spell_names, test_powers):
        print(guild.cast_spell(name, p))
    print()

    print("Invalid name checks:")
    for n in invalid_names:
        print(f"  {n!r}: {MageGuild.validate_mage_name(n)}")

    print("Mage name checks:")
    for n in mage_names:
        print(f"  {n!r}: {MageGuild.validate_mage_name(n)}")


if __name__ == "__main__":
    main()
