from ..core.ecs import Entity
from ..components.position import Position, MovementSpeed
from ..components.unit import Unit, Combat
from ..core.hex_grid import HexCoord

def create_soldier(owner_id: int, position: HexCoord) -> Entity:
    entity = Entity()
    entity.add_component(Position(position))
    entity.add_component(MovementSpeed(2))  # Can move 2 hexes per turn
    entity.add_component(Unit(owner_id))
    entity.add_component(Combat())
    return entity 