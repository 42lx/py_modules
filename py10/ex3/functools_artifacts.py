import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if not spells:
        return 0
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    elements = ["fire", "ice", "lightning"]
    return {
        e: functools.partial(base_enchantment, power=50, element=e)
        for e in elements
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell: object) -> str:
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()} enchantment of {power} power on {target}"


def main() -> None:
    spell_powers = [50, 49, 33, 46, 22, 14]
    fibonacci_tests = [8, 18, 11]

    print(f"Spell powers: {spell_powers}")
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")
    print(f"Empty add: {spell_reducer([], 'add')}")
    try:
        spell_reducer(spell_powers, 'divide')
    except ValueError as e:
        print(f"Error caught: {e}")
    print()

    print("Testing partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"](target="Sword"))
    print(enchanters["ice"](target="Shield"))
    print(enchanters["lightning"](target="Staff"))
    print()

    print("Testing memoized fibonacci...")
    for n in (0, 1, 10, 15):
        print(f"Fib({n}): {memoized_fibonacci(n)}")
        print(f"  Cache info: {memoized_fibonacci.cache_info()}")
    for n in fibonacci_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
        print(f"  Cache info: {memoized_fibonacci.cache_info()}")
    print()

    print("Testing spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast(["heal", "shield", "fireball"]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
