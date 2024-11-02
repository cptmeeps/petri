from typing import Optional, Tuple
from .ecs import World, Entity
from ..systems.player_system import PlayerSystem
from ..systems.movement import MovementSystem
from ..systems.unit_system import UnitSystem
from ..systems.spawn_system import SpawnSystem
from .game_phases import GamePhase
from .hex_grid import HexCoord
from ..factories.unit_factory import create_soldier

class GameSetup:
    @staticmethod
    def create_game(map_width: int = 20, map_height: int = 20) -> World:
        world = World(map_width, map_height)
        
        # Initialize systems with phases
        player_system = PlayerSystem(world)
        world.add_system(player_system)
        world.add_system(MovementSystem(world), GamePhase.MOVEMENT)
        world.add_system(UnitSystem(world), GamePhase.COMBAT)
        world.add_system(SpawnSystem(world), GamePhase.SPAWN)
        
        return world
    
    @staticmethod
    def add_players(world: World, 
                    player1_name: str = "Player 1", 
                    player2_name: str = "Player 2",
                    player1_color: str = "#FF0000",
                    player2_color: str = "#0000FF") -> Tuple[Entity, Entity]:
        # Get the player system using the new method
        player_system = world.get_system(PlayerSystem)
        if player_system is None:
            raise Exception("PlayerSystem not found in world systems.")
        
        player1 = player_system.add_player(world, player1_name, player1_color)
        player2 = player_system.add_player(world, player2_name, player2_color)
        
        return player1, player2
    
    @staticmethod
    def add_initial_units(world: World, 
                          player1: Entity, 
                          player2: Entity,
                          p1_pos: Optional[HexCoord] = None,
                          p2_pos: Optional[HexCoord] = None) -> Tuple[Entity, Entity]:
        p1_pos = p1_pos or HexCoord(0, 0)
        p2_pos = p2_pos or HexCoord(5, 5)
        
        from ..components.player import Player
        p1_soldier = create_soldier(player1.get_component(Player).id, p1_pos)
        p2_soldier = create_soldier(player2.get_component(Player).id, p2_pos)
        
        world.add_entity(p1_soldier)
        world.add_entity(p2_soldier)
        
        return p1_soldier, p2_soldier 