from tests.test_base import BaseGameTest
from src.systems.movement import MovementSystem
from src.components.position import Position
from src.core.hex_grid import HexCoord
from src.factories.unit_factory import create_soldier

class TestMovementSystem(BaseGameTest):
    def setUp(self):
        super().setUp()
        self.movement_system = next(s for s in self.world.systems 
                                  if isinstance(s, MovementSystem))
    
    def test_multi_turn_movement(self):
        soldier = create_soldier(self.p1_id, HexCoord(0, 0))
        self.world.add_entity(soldier)
        
        # Set a path that would take multiple turns
        target = HexCoord(6, 0)  # Would take 3 turns with speed 2
        self.movement_system.set_movement_path(soldier, target)
        
        # Simulate three turns
        for _ in range(3):
            self.movement_system.update([soldier])
            
        # Check if reached destination
        final_pos = soldier.get_component(Position).coord
        self.assertEqual(final_pos, target)
    
    def test_unit_movement(self):
        soldier = create_soldier(self.p1_id, HexCoord(0, 0))
        self.world.add_entity(soldier)
        
        # Test movement within range
        target = HexCoord(1, 0)
        success = self.movement_system.set_movement_path(soldier, target)
        self.assertTrue(success)
        
        # Update to execute movement
        self.movement_system.update([soldier])
        
        # Check if reached destination
        final_pos = soldier.get_component(Position).coord
        self.assertEqual(final_pos, target)