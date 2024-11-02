from typing import List, Optional
from ..core.ecs import System, Entity
from ..components.position import Position
from ..components.unit import Unit, Combat
from ..core.hex_grid import HexCoord
from ..factories.unit_factory import create_soldier

class SpawnSystem(System):
    def __init__(self, world: Optional['World'] = None):
        super().__init__(world)  # Call parent class's __init__

    def update(self, entities: List[Entity]) -> None:
        # Reset just_spawned flag for existing units
        for entity in entities:
            unit = entity.get_component(Unit)
            if unit and unit.just_spawned:
                unit.just_spawned = False

        # Check each entity for spawning
        for entity in entities:
            pos = entity.get_component(Position)
            unit = entity.get_component(Unit)
            
            # Skip if unit was just spawned
            if pos and unit and not unit.just_spawned:
                # Only spawn if the current unit's position is in bounds
                if not self.world.game_map.in_bounds(pos.coord):
                    continue
                    
                # Create a new unit at the same position
                new_unit = create_soldier(unit.owner_id, pos.coord)
                print(f"Creating new unit for owner {unit.owner_id} at {pos.coord}")
                self.world.add_entity(new_unit)
                print(f"New unit components: {new_unit.components}")