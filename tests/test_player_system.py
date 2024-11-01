import unittest
from src.core.ecs import World
from src.systems.player_system import PlayerSystem
from src.components.player import Player
from src.factories.unit_factory import create_soldier
from src.core.hex_grid import HexCoord

class TestPlayerSystem(unittest.TestCase):
    def setUp(self):
        self.world = World()
        self.player_system = PlayerSystem()
        
    def test_player_creation(self):
        player = self.player_system.add_player(self.world, "Test Player", "#FF0000")
        self.assertIsNotNone(player.get_component(Player))
        self.assertEqual(player.get_component(Player).name, "Test Player")
        
    def test_player_units(self):
        player = self.player_system.add_player(self.world, "Test Player", "#FF0000")
        player_id = player.get_component(Player).id
        
        # Create units for the player
        unit1 = create_soldier(player_id, HexCoord(0, 0))
        unit2 = create_soldier(player_id, HexCoord(1, 0))
        self.world.add_entity(unit1)
        self.world.add_entity(unit2)
        
        player_units = self.player_system.get_player_units(self.world.entities, player_id)
        self.assertEqual(len(player_units), 2)
        
    def test_player_turns(self):
        player1 = self.player_system.add_player(self.world, "Player 1", "#FF0000")
        player2 = self.player_system.add_player(self.world, "Player 2", "#0000FF")
        
        current = self.player_system.get_current_player()
        self.assertEqual(current, player1)
        
        self.player_system.next_turn()
        current = self.player_system.get_current_player()
        self.assertEqual(current, player2)

if __name__ == '__main__':
    unittest.main() 