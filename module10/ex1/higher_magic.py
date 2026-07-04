from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiplied(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return multiplied


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condit(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return condit


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"


def has_enough_power(target: str, power: int) -> bool:
    return power >= 20


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(has_enough_power, fireball)
    print(f"Power 30: {safe_fireball('Dragon', 30)}")
    print(f"Power 5: {safe_fireball('Dragon', 5)}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, shield])
    for line in combo("Dragon", 25):
        print(line)


if __name__ == "__main__":
    main()
