from abc import ABC, abstractmethod

class Creature(ABC):

    def __init__(self, name: str, element: str, move: str) -> None:
        self.name: str = name.capitalize()
        self.element: str = element.capitalize()
        self.move: str = move.capitalize()

    @abstractmethod
    def attack(self) -> None:
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
    def create_base(self) -> str:
        pass

    @abstractmethod
    def create_evolved(self) -> str:
        pass

class FlameFactory(CreatureFactory):
    def create_base(self) -> str:
        return Flameling("flameling", "fire", "ember")
    
    def create_evolved(self) -> str:
        return Pyrodon("pyrodon", "fire/flying", "flamethrower")
    
class AquaFactory(CreatureFactory):
    def create_base(self) -> str:
        return Aquabub("aquabub", "water", "water gun")
    
    def create_evolved(self) -> str:
        return Torragon("Torragon", "water", "hydro pump")
