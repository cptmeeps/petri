from dataclasses import dataclass
from src.core.ecs import Entity
from src.core.hex_grid import HexCoord

class Command:
    pass

@dataclass
class MoveCommand(Command):
    entity: Entity
    target: HexCoord

@dataclass
class AttackCommand(Command):
    attacker: Entity
    defender: Entity 