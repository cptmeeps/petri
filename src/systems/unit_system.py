from typing import List, Optional, Tuple
from ..core.ecs import System, Entity
from ..components.unit import Unit, Combat
from ..components.combat import CombatRange
from ..components.position import Position
from ..core.hex_grid import HexCoord, HexGrid

class UnitSystem(System):
    def can_attack(self, attacker: Entity, defender: Entity) -> bool:
        """Check if attacker can attack defender based on range and components"""
        attacker_pos = attacker.get_component(Position)
        defender_pos = defender.get_component(Position)
        combat_range = attacker.get_component(CombatRange)
        
        if not (attacker_pos and defender_pos and combat_range):
            return False
            
        distance = HexGrid.distance(attacker_pos.coord, defender_pos.coord)
        return combat_range.min_range <= distance <= combat_range.max_range

    def get_attackable_units(self, attacker: Entity, entities: List[Entity]) -> List[Entity]:
        """Get all units that can be attacked by the attacker"""
        attackable = []
        attacker_unit = attacker.get_component(Unit)
        
        if not attacker_unit:
            return []
            
        for target in entities:
            target_unit = target.get_component(Unit)
            if (target_unit and 
                target_unit.owner_id != attacker_unit.owner_id and
                self.can_attack(attacker, target)):
                attackable.append(target)
                
        return attackable

    def attack(self, attacker: Entity, defender: Entity) -> Tuple[bool, int]:
        """Perform attack and return (success, damage_dealt)"""
        if not self.can_attack(attacker, defender):
            return False, 0
            
        attacker_combat = attacker.get_component(Combat)
        defender_combat = defender.get_component(Combat)
        
        if not (attacker_combat and defender_combat):
            return False, 0

        damage = max(1, attacker_combat.attack - defender_combat.defense)
        defender_combat.health -= damage
        return True, damage

    def update(self, entities: List[Entity]) -> None:
        # Remove dead units
        for entity in entities[:]:
            combat = entity.get_component(Combat)
            if combat and combat.health <= 0:
                entities.remove(entity)

    def get_units_at_position(self, entities: List[Entity], coord: HexCoord) -> List[Entity]:
        """Get all units at a specific position"""
        return [
            entity for entity in entities
            if entity.get_component(Position) and 
            entity.get_component(Position).coord == coord
        ]
