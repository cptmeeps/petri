import unittest
from src.core.ecs import World, Entity
from src.components.unit import Unit, Combat
from src.components.position import Position, MovementSpeed
from src.systems.unit_system import UnitSystem
from src.core.hex_grid import HexCoord
from src.systems.movement import MovementSystem

class TestUnit(unittest.TestCase):
    def setUp(self):
        self.world = World()
        self.unit_system = UnitSystem()
        
    def create_test_soldier(self, owner_id: int, position: HexCoord) -> Entity:
        entity = Entity()
        entity.add_component(Position(position))
        entity.add_component(Unit(owner_id))
        entity.add_component(Combat())
        return entity
        
    def test_unit_creation(self):
        soldier = self.create_test_soldier(1, HexCoord(0, 0))
        
        # Test components exist
        self.assertIsNotNone(soldier.get_component(Unit))
        self.assertIsNotNone(soldier.get_component(Combat))
        self.assertIsNotNone(soldier.get_component(Position))
        
        # Test component values
        unit = soldier.get_component(Unit)
        combat = soldier.get_component(Combat)
        position = soldier.get_component(Position)
        
        self.assertEqual(unit.owner_id, 1)
        self.assertEqual(combat.health, 100)
        self.assertEqual(position.coord, HexCoord(0, 0))
        
    def test_combat(self):
        attacker = self.create_test_soldier(1, HexCoord(0, 0))
        defender = self.create_test_soldier(2, HexCoord(1, 0))
        
        initial_health = defender.get_component(Combat).health
        self.unit_system.attack(attacker, defender)
        final_health = defender.get_component(Combat).health
        
        # Test that damage was dealt
        self.assertLess(final_health, initial_health)
        
    def test_unit_death(self):
        soldier = self.create_test_soldier(1, HexCoord(0, 0))
        self.world.add_entity(soldier)
        
        # Set health to 0
        soldier.get_component(Combat).health = 0
        
        # Update should remove dead units
        self.unit_system.update(self.world.entities)
        
        self.assertEqual(len(self.world.entities), 0)
        
    def test_get_unit_at_position(self):
        soldier = self.create_test_soldier(1, HexCoord(0, 0))
        self.world.add_entity(soldier)
        
        # Test finding unit at position
        found_unit = self.unit_system.get_unit_at_position(
            self.world.entities, 
            HexCoord(0, 0)
        )
        self.assertEqual(found_unit, soldier)
        
        # Test position with no unit
        empty_pos = self.unit_system.get_unit_at_position(
            self.world.entities, 
            HexCoord(1, 1)
        )
        self.assertIsNone(empty_pos)

if __name__ == '__main__':
    unittest.main() 