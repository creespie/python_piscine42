from . import elements


def healing_potion() -> str:
    return (f"Healing potion brewed with '{elements.create_earth()}' and "
            f"'{elements.create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed with '{elements.create_fire()}' and "
            f"'{elements.create_water()}'")
