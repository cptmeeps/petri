import unittest
from src.core.ecs import World
from src.core.hex_grid import HexCoord
from src.systems.spawn_system import SpawnSystem
from src.factories.unit_factory import create_soldier
from src.components.unit import Unit

class TestSpawnSystem(unittest.TestCase):
    def setUp(self):
        self.world = World()
        self.spawn_system = SpawnSystem()
        
    def test_unit_spawning(self):
        # Create initial unit
        initial_unit = create_soldier(owner_id=1, position=HexCoord(0, 0))
        self.world.add_entity(initial_unit)
        
        # Initial count
        initial_count = len(self.world.entities)
        
        # Update spawn system
        self.spawn_system.update(self.world.entities)
        
        # Should have one more unit
        self.assertEqual(len(self.world.entities), initial_count + 1)
        
        # New unit should have same owner
        new_unit = [e for e in self.world.entities if e != initial_unit][0]
        self.assertEqual(new_unit.get_component(Unit).owner_id, 1)

if __name__ == '__main__':
    unittest.main() 