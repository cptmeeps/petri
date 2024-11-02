import unittest
from src.core.game_setup import GameSetup
from src.core.hex_grid import HexCoord
from src.components.player import Player
from src.systems.unit_system import UnitSystem

class BaseGameTest(unittest.TestCase):
    def setUp(self):
        # Create base game setup with smaller map for tests
        self.world = GameSetup.create_game(10, 10)
        self.player1, self.player2 = GameSetup.add_players(self.world)
        self.p1_id = self.player1.get_component(Player).id
        self.p2_id = self.player2.get_component(Player).id
        self.unit_system = next(s for s in self.world.systems 
                              if isinstance(s, UnitSystem))