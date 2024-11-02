from typing import List, Optional
from ..core.ecs import System, Entity, World
from ..core.hex_grid import HexGrid, HexCoord
from ..components.position import Position, MovementSpeed, MovementPath
from src.commands import MoveCommand

class MovementSystem(System):
    def __init__(self, world: Optional['World'] = None):
        super().__init__(world)
    
    def update(self, entities: List[Entity]) -> None:
        # Process MoveCommands
        commands_to_process = [cmd for cmd in self.world.command_queue if isinstance(cmd, MoveCommand)]
        for command in commands_to_process:
            self.process_move_command(command)
            self.world.command_queue.remove(command)

        # Existing movement logic
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

    def process_move_command(self, command: MoveCommand) -> None:
        entity = command.entity
        target = command.target

        if not self.world.game_map.in_bounds(target):
            return

        pos = entity.get_component(Position)
        if not pos:
            return

        path = HexGrid.line(pos.coord, target)

        path_component = entity.get_component(MovementPath)
        if path_component:
            path_component.path = path
            path_component.current_index = 0
        else:
            entity.add_component(MovementPath(path=path, current_index=0))