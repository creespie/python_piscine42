from alchemy.elements import create_fire
from .. import potions
from .. import elements


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{elements.create_air()}'"
            f" and '{potions.strength_potion()}' mixed with '{create_fire()}'"
            )
