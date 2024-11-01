import time
from src.core.ecs import World, Entity
from src.components.position import Position, MovementSpeed
from src.components.unit import Unit, Combat
from src.systems.movement import MovementSystem
from src.systems.unit_system import UnitSystem
from src.core.hex_grid import HexCoord
from src.systems.spawn_system import SpawnSystem
from src.factories.unit_factory import create_soldier

def main():
    world = World()
    movement_system = MovementSystem()
    
    # Create a soldier
    soldier = create_soldier(owner_id=1, position=HexCoord(0, 0))
    world.add_entity(soldier)
    
    # Set a long-distance movement path
    target = HexCoord(10, -5)  # Far away destination
    movement_system.set_movement_path(soldier, target)
    
    # Add systems
    world.add_system(MovementSystem())
    world.add_system(UnitSystem())
    world.add_system(SpawnSystem())
    
    TURN_DURATION = 1.0  # 1 second per turn
    last_turn_time = time.time()
    turn_counter = 0
    
    try:
        while True:
            current_time = time.time()
            
            # Check if it's time for the next turn
            if current_time - last_turn_time >= TURN_DURATION:
                turn_counter += 1
                print(f"Turn {turn_counter}")
                
                # Update all systems
                world.update()
                
                # Reset the timer
                last_turn_time = current_time
            
            # Small sleep to prevent CPU hogging
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("\nGame terminated by user")

if __name__ == "__main__":
    main() 