import time
from src.core.ecs import World, Entity
from src.components.position import Position, MovementSpeed
from src.components.unit import Unit, Combat
from src.systems.movement import MovementSystem
from src.systems.unit_system import UnitSystem
from src.core.hex_grid import HexCoord
from src.systems.spawn_system import SpawnSystem
from src.factories.unit_factory import create_soldier
from src.components.player import Player
from src.systems.player_system import PlayerSystem

def main():
    world = World()
    
    # Initialize systems
    player_system = PlayerSystem()
    world.add_system(player_system)
    world.add_system(MovementSystem())
    world.add_system(UnitSystem())
    world.add_system(SpawnSystem())
    
    # Add players
    player1 = player_system.add_player(world, "Player 1", "#FF0000")
    player2 = player_system.add_player(world, "Player 2", "#0000FF")
    
    # Create initial units for each player
    p1_soldier = create_soldier(player1.get_component(Player).id, HexCoord(0, 0))
    p2_soldier = create_soldier(player2.get_component(Player).id, HexCoord(5, 5))
    world.add_entity(p1_soldier)
    world.add_entity(p2_soldier)
    
    TURN_DURATION = 1.0
    last_turn_time = time.time()
    turn_counter = 0
    
    try:
        while True:
            current_time = time.time()
            
            if current_time - last_turn_time >= TURN_DURATION:
                turn_counter += 1
                current_player = player_system.get_current_player()
                print(f"\nTurn {turn_counter} - {current_player.get_component(Player).name}'s turn")
                
                # Update all systems
                world.update()
                
                # Move to next player
                player_system.next_turn()
                
                last_turn_time = current_time
            
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("\nGame terminated by user")

if __name__ == "__main__":
    main() 