from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    counter = 0

    def counting() -> int:
        nonlocal counter
        counter += 1
        return counter

    return counting


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def adding(more: int) -> int:
        nonlocal power
        power += more
        return power

    return adding


def enchantment_factory(enchantment_type: str) -> Callable:
    enchant = enchantment_type

    def enchanted(item: str) -> str:
        return f"{enchant} {item}"

    return enchanted


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: Any, value: Any) -> None:
        storage[key] = value

    def recall(key: Any) -> Any:
        if key in storage.keys():
            return storage[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
