#!/usr/bin/env python3
from abc import ABC, abstractmethod

'''----BattleStrategy abstract class----'''
class BattleStrategy(ABC):
    @abstractmethod
    def act():
        pass
    
    @abstractmethod
    def is_valid() -> bool:
        pass
    
'''Three concrete classes (BattleStrategy)'''

#---Only use attack method
class NormalStrategy(BattleStrategy):
    def act():
        pass
    
    def is_valid() -> bool:
        pass

#---Creature with transform capabilities
class AggressiveStrategy(BattleStrategy):
    pass

#---Creature with healing capabilities
class DefensiveStrategy(BattleStrategy):
    pass

