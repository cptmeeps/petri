from typing import List, Optional
from ..core.ecs import System, Entity
from ..core.hex_grid import HexGrid, HexCoord
from ..components.position import Position, MovementSpeed, MovementPath

class MovementSystem(System):
    def set_movement_path(self, entity: Entity, target: HexCoord) -> bool:
        pos = entity.get_component(Position)
        if not pos:
            return False
            
        # Calculate path using HexGrid.line
        path = HexGrid.line(pos.coord, target)
        
        # Add or update movement path component
        path_component = entity.get_component(MovementPath)
        if path_component:
            path_component.path = path
            path_component.current_index = 0
        else:
            entity.add_component(MovementPath(path=path, current_index=0))
        return True
    
    def update(self, entities: List[Entity]) -> None:
        for entity in entities:
            pos = entity.get_component(Position)
            speed = entity.get_component(MovementSpeed)
            path = entity.get_component(MovementPath)
            
            if not (pos and speed and path and not path.is_complete()):
                continue
                
            # Calculate how many steps we can take this turn
            remaining_moves = speed.speed
            while remaining_moves > 0 and not path.is_complete():
                # Check if we're at the last position
                if path.current_index >= len(path.path) - 1:
                    break
                    
                next_pos = path.path[path.current_index + 1]
                
                # Check if we can move to the next position
                distance = HexGrid.distance(pos.coord, next_pos)
                if distance <= remaining_moves:
                    pos.coord = next_pos
                    path.current_index += 1
                    remaining_moves -= distance
                else:
                    break