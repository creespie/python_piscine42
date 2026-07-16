from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, element: str, move: str) -> None:
        self.name: str = name.capitalize()
        self.element: str = element.capitalize()
        self.move: str = move.capitalize()

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.element} element Creature"


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"


class Aquabub(Creature):
    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"


class Torragon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling("flameling", "fire", "ember")

    def create_evolved(self) -> Pyrodon:
        return Pyrodon("pyrodon", "fire/flying", "flamethrower")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub("aquabub", "water", "water gun")

    def create_evolved(self) -> Torragon:
        return Torragon("Torragon", "water", "hydro pump")
