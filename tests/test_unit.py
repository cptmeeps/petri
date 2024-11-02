from tests.test_base import BaseGameTest
from src.systems.unit_system import UnitSystem
from src.components.unit import Combat
from src.components.position import Position
from src.core.hex_grid import HexCoord
from src.factories.unit_factory import create_soldier

class TestUnit(BaseGameTest):
    def setUp(self):
        super().setUp()
        self.unit_system = next(s for s in self.world.systems 
                              if isinstance(s, UnitSystem))
    
    def test_unit_death(self):
        soldier = create_soldier(self.p1_id, HexCoord(0, 0))
        self.world.add_entity(soldier)
        
        # Set health to 0
        soldier.get_component(Combat).health = 0
        
        # Update should remove dead units
        self.unit_system.update(self.world.entities)
        
        self.assertEqual(len([e for e in self.world.entities 
                            if e.get_component(Combat)]), 0)
        
    def test_get_units_at_position(self):
        soldier = create_soldier(self.p1_id, HexCoord(0, 0))
        self.world.add_entity(soldier)
        
        # Test finding units at position
        found_units = self.unit_system.get_units_at_position(
            self.world.entities, 
            HexCoord(0, 0)
        )
        self.assertEqual(len(found_units), 1)
        self.assertEqual(found_units[0], soldier)
        
        # Test position with no units
        empty_pos = self.unit_system.get_units_at_position(
            self.world.entities, 
            HexCoord(1, 1)
        )
        self.assertEqual(len(empty_pos), 0)