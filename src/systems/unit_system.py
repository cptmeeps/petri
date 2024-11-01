from typing import List, Optional
from ..core.ecs import System, Entity
from ..components.unit import Unit, Combat
from ..components.position import Position
from ..core.hex_grid import HexCoord

class UnitSystem(System):
    def get_unit_at_position(self, entities: List[Entity], coord: HexCoord) -> Optional[Entity]:
        for entity in entities:
            pos = entity.get_component(Position)
            unit = entity.get_component(Unit)
            if pos and unit and pos.coord == coord:
                return entity
        return None

    def attack(self, attacker: Entity, defender: Entity) -> bool:
        attacker_combat = attacker.get_component(Combat)
        defender_combat = defender.get_component(Combat)
        
        if not (attacker_combat and defender_combat):
            return False

        damage = max(1, attacker_combat.attack - defender_combat.defense)
        defender_combat.health -= damage
        return True

    def update(self, entities: List[Entity]) -> None:
        # Remove dead units
        for entity in entities[:]:
            combat = entity.get_component(Combat)
            if combat and combat.health <= 0:
                entities.remove(entity) 