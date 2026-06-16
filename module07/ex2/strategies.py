from ex0.creatures import Creature
from abc import ABC, abstractmethod

class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> None:
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature):
        return True
    
    def act(self, creature: Creature):
        print(creature.attack())

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        try:
            creature.transform()
            creature.revert()
            return True
        except Exception:
            return False
        
    def act(self, creature: Creature):
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise ValueError("Battle error, aborting tournament: Invalid Crea"
                             f"ture '{creature}' for this aggressive strategy"
                             )
            
class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        try:
            creature.heal()
            return True
        except Exception:
            return False
        
    def act(self, creature: Creature):
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise ValueError("Battle error, aborting tournament: Invalid Crea"
                             f"ture '{creature}' for this defensive strategy")