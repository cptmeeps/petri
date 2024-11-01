from typing import List
from ..core.ecs import System, Entity
from ..components.position import Position
from ..components.unit import Unit, Combat
from ..core.hex_grid import HexCoord
from ..utils.unit_factory import create_soldier

class SpawnSystem(System):
    def update(self, entities: List[Entity]) -> None:
        # Keep track of positions where we've already spawned units this turn
        spawned_positions = set()
        new_units = []

        # Check each entity for spawning
        for entity in entities:
            pos = entity.get_component(Position)
            unit = entity.get_component(Unit)
            
            if pos and unit and pos.coord not in spawned_positions:
                # Create a new unit at an adjacent hex
                neighbors = self.find_empty_neighbor(entities, pos.coord)
                if neighbors:
                    # Create new unit with same owner
                    new_unit = create_soldier(unit.owner_id, neighbors)
                    new_units.append(new_unit)
                    spawned_positions.add(neighbors)

        # Add all new units to the entity list
        entities.extend(new_units)

    def find_empty_neighbor(self, entities: List[Entity], coord: HexCoord) -> HexCoord:
        from ..core.hex_grid import HexGrid
        
        # Get all neighboring positions
        neighbors = HexGrid.get_neighbors(coord)
        
        # Find positions that are already occupied
        occupied_positions = set()
        for entity in entities:
            pos = entity.get_component(Position)
            if pos:
                occupied_positions.add(pos.coord)
        
        # Filter out occupied positions
        available_positions = [pos for pos in neighbors if pos not in occupied_positions]
        
        # Return first available position or None if none available
        return available_positions[0] if available_positions else None 