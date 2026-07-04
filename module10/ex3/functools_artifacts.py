from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError("Invalid operation type")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    elements = ["fire", "earth", "air"]
    return {
        element: partial(base_enchantment, power=50, element=element)
        for element in elements
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


# --- Funzione di esempio per testare partial_enchanter ---

def enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment ({power}) on {target}"


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(enchant)
    print(enchanters["fire"](target="Sword"))
    print(enchanters["earth"](target="Shield"))
    print(enchanters["air"](target="Bow"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()