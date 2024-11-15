import time
from src.core.game_setup import GameSetup
from src.systems.player_system import PlayerSystem
from src.components.player import Player
from src.commands import MoveCommand

def main():
    # Create game world with systems
    world = GameSetup.create_game()
    
    # Add players
    player1, player2 = GameSetup.add_players(world)
    
    # Add initial units
    GameSetup.add_initial_units(world, player1, player2)
    
    TURN_DURATION = 1.0
    last_turn_time = time.time()
    turn_counter = 0
    
    # Get the player system using the new method
    player_system = world.get_system(PlayerSystem)
    if player_system is None:
        raise Exception("PlayerSystem not found in world systems.")
    
    try:
        while True:
            current_time = time.time()
            
            if current_time - last_turn_time >= TURN_DURATION:
                turn_counter += 1
                current_player = player_system.get_current_player()
                player_name = current_player.get_component(Player).name
                
                # Log turn start
                world.logger.log_turn(turn_counter, player_name)
                print(f"\nTurn {turn_counter} - {player_name}'s turn")
                
                # Example: Enqueue a move command
                entity_to_move = ...  # Determine which entity to move
                target_position = ...  # Determine target position
                move_command = MoveCommand(entity=entity_to_move, target=target_position)
                world.enqueue_command(move_command)
                
                # Execute all systems in their proper phases
                world.update()
                
                # Move to next player
                player_system.next_turn()
                last_turn_time = current_time
            
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        world.logger.log_game_end("User terminated the game")
        print("\nGame terminated by user")

if __name__ == "__main__":
    main() 