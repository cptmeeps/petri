from tests.test_base import BaseGameTest
from src.systems.spawn_system import SpawnSystem
from src.components.unit import Unit
from src.core.hex_grid import HexCoord, HexGrid
from src.factories.unit_factory import create_soldier
from src.components.position import Position

class TestSpawnSystem(BaseGameTest):
    def setUp(self):
        super().setUp()
        self.spawn_system = next(s for s in self.world.systems 
                               if isinstance(s, SpawnSystem))
        
    def test_unit_spawning(self):
        # Create initial unit in the center of the map
        initial_unit = create_soldier(self.p1_id, HexCoord(5, 5))  # Center of 10x10 map
        self.world.add_entity(initial_unit)
        
        # Initial count
        initial_count = len(self.world.entities)
        
        # Update spawn system
        self.spawn_system.update(self.world.entities)
        
        # Should have one more unit
        self.assertEqual(len(self.world.entities), initial_count + 1)
        
        # New unit should have same owner
        new_units = [e for e in self.world.entities 
                     if e != initial_unit and e.get_component(Unit)]
        self.assertEqual(len(new_units), 1, "Expected exactly one new unit")
        new_unit = new_units[0]
        self.assertEqual(new_unit.get_component(Unit).owner_id, self.p1_id)
        
        # Verify new unit is in the same position as the parent unit
        new_pos = new_unit.get_component(Position).coord
        initial_pos = initial_unit.get_component(Position).coord
        self.assertTrue(self.world.game_map.in_bounds(new_pos))
        self.assertEqual(new_pos, initial_pos)
        
    def test_unit_spawning_at_map_edge(self):
        # Create initial unit at map edge
        initial_unit = create_soldier(self.p1_id, HexCoord(0, 0))
        self.world.add_entity(initial_unit)
        
        # Initial count
        initial_count = len(self.world.entities)
        
        # Update spawn system
        self.spawn_system.update(self.world.entities)
        
        # Should have one more unit
        self.assertEqual(len(self.world.entities), initial_count + 1)
        
        # New unit should be at the same position
        new_units = [e for e in self.world.entities 
                    if e != initial_unit and e.get_component(Unit)]
        self.assertEqual(len(new_units), 1, "Expected exactly one new unit")
        new_unit = new_units[0]
        new_pos = new_unit.get_component(Position).coord
        self.assertEqual(new_pos, HexCoord(0, 0))