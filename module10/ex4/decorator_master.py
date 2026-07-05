from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, spell_name: str, power: int) -> str:
            if power >= min_power:
                return func(self, spell_name, power)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)  # se funziona, esce subito
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            return name.replace(" ", "").isalpha()
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# --- Spell di esempio per testare i decoratori ---


@spell_timer
def fireball(target: str, power: int) -> str:
    time.sleep(0.1)  # simula un piccolo "costo" di esecuzione
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell(target: str, power: int) -> str:
    raise ValueError("The spell backfired!")  # fallisce sempre, di proposito


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball('Dragon', 50)}")

    print("\nTesting retrying spell...")
    print(unstable_spell("Dragon", 50))

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Jordan"))
    print(MageGuild.validate_mage_name("Al"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
