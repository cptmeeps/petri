import time
from src.core.game_setup import GameSetup
from src.systems.player_system import PlayerSystem
from src.components.player import Player

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
    
    try:
        while True:
            current_time = time.time()
            
            if current_time - last_turn_time >= TURN_DURATION:
                turn_counter += 1
                current_player = next(s for s in world.systems 
                                    if isinstance(s, PlayerSystem)).get_current_player()
                player_name = current_player.get_component(Player).name
                
                # Log turn start
                world.logger.log_turn(turn_counter, player_name)
                print(f"\nTurn {turn_counter} - {player_name}'s turn")
                
                # Execute all systems in their proper phases
                world.update()
                
                # Move to next player
                next(s for s in world.systems 
                     if isinstance(s, PlayerSystem)).next_turn()
                last_turn_time = current_time
            
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        world.logger.log_game_end("User terminated the game")
        print("\nGame terminated by user")

if __name__ == "__main__":
    main() 