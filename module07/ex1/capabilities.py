from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex0.creatures import CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"

    def heal(self, target: str = "itself"):
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"

    def heal(self, target: str = "itself") -> str:
        return f"{self.name} heals {target} for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling("sproutling", "Grass", "Vine Whip")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy", "Petal Dance")


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str, move: str) -> None:
        Creature.__init__(self, name, creature_type, move)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, creature_type: str, move: str) -> None:
        Creature.__init__(self, name, creature_type, move)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} attacks normally."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "normal", "unknown")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "normal/Dragon", "unknown")
