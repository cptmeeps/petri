from tests.test_base import BaseGameTest
from src.core.hex_grid import HexCoord
from src.factories.unit_factory import create_soldier
from src.components.unit import Combat
from src.components.combat import CombatRange

class TestCombat(BaseGameTest):
    def test_basic_combat(self):
        # Create two adjacent units
        attacker = create_soldier(self.p1_id, HexCoord(0, 0))
        defender = create_soldier(self.p2_id, HexCoord(1, 0))
        self.world.add_entity(attacker)
        self.world.add_entity(defender)
        
        # Test attack
        success, damage = self.unit_system.attack(attacker, defender)
        self.assertTrue(success)
        self.assertEqual(damage, 5)  # 10 attack - 5 defense = 5 damage
        
        # Verify defender health
        defender_health = defender.get_component(Combat).health
        self.assertEqual(defender_health, 95)  # 100 - 5 = 95
        
    def test_combat_range(self):
        # Create units at different ranges
        attacker = create_soldier(self.p1_id, HexCoord(0, 0))
        adjacent = create_soldier(self.p2_id, HexCoord(1, 0))
        far_unit = create_soldier(self.p2_id, HexCoord(2, 0))
        
        # Set attacker range
        attacker.get_component(CombatRange).max_range = 2
        
        # Test range checks
        self.assertTrue(self.unit_system.can_attack(attacker, adjacent))
        self.assertTrue(self.unit_system.can_attack(attacker, far_unit))
        
        # Get attackable units
        attackable = self.unit_system.get_attackable_units(
            attacker, 
            [attacker, adjacent, far_unit]
        )
        self.assertEqual(len(attackable), 2) 