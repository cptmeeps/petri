from enum import Enum, auto

class GamePhase(Enum):
    MOVEMENT = auto()
    COMBAT = auto()
    SPAWN = auto() 