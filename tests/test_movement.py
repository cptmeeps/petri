from unittest import TestCase
from src.core.hex_grid import HexCoord
from src.components.position import Position, MovementSpeed
from src.systems.movement import MovementSystem
from src.core.ecs import Entity
from src.factories.unit_factory import create_soldier

class TestMovementSystem(TestCase):
    def test_multi_turn_movement(self):
        soldier = create_soldier(1, HexCoord(0, 0))
        movement_system = MovementSystem()
        
        # Set a path that would take multiple turns
        target = HexCoord(6, 0)  # Would take 3 turns with speed 2
        movement_system.set_movement_path(soldier, target)
        
        # Simulate three turns
        for _ in range(3):
            movement_system.update([soldier])
            
        # Check if reached destination
        final_pos = soldier.get_component(Position).coord
        self.assertEqual(final_pos, target)
    
    def test_unit_movement(self):
        # Create a unit at position (0,0)
        soldier = create_soldier(1, HexCoord(0, 0))
        
        # Create movement system
        movement_system = MovementSystem()
        
        # Test movement within range
        target = HexCoord(1, 0)
        success = movement_system.set_movement_path(soldier, target)
        self.assertTrue(success)
        
        # Update to execute movement
        movement_system.update([soldier])
        
        # Check if reached destination
        final_pos = soldier.get_component(Position).coord
        self.assertEqual(final_pos, target)
        
        # Test invalid movement (too far for one turn)
        far_target = HexCoord(4, 0)
        movement_system.set_movement_path(soldier, far_target)
        movement_system.update([soldier])
        
        # Should not reach far target in one turn
        current_pos = soldier.get_component(Position).coord
        self.assertNotEqual(current_pos, far_target) 