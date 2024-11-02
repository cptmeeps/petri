import unittest
from src.core.game_setup import GameSetup
from src.core.hex_grid import HexCoord
from src.components.player import Player
from src.components.unit import Unit

class TestGameSetup(unittest.TestCase):
    def test_basic_game_setup(self):
        # Create world with systems
        world = GameSetup.create_game(10, 10)
        
        # Add players
        player1, player2 = GameSetup.add_players(world)
        
        # Add units at specific positions
        p1_pos = HexCoord(1, 1)
        p2_pos = HexCoord(8, 8)
        unit1, unit2 = GameSetup.add_initial_units(world, player1, player2, p1_pos, p2_pos)
        
        # Verify setup
        self.assertEqual(len(world.systems), 4)  # PlayerSystem, MovementSystem, UnitSystem, SpawnSystem
        self.assertEqual(len(world.entities), 4)  # 2 players + 2 units
        self.assertEqual(unit1.get_component(Unit).owner_id, 
                        player1.get_component(Player).id) 