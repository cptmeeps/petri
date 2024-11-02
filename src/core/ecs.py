from typing import Dict, List, Optional
from dataclasses import dataclass
import uuid
from src.core.game_phases import GamePhase
from src.core.game_map import GameMap
from src.utils.logger import GameLogger

class Entity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.components: Dict = {}
    
    def add_component(self, component: object) -> None:
        self.components[type(component)] = component
        
    def get_component(self, component_type: type) -> object:
        return self.components.get(component_type)

class System:
    def __init__(self, world: Optional['World'] = None):
        self.world = world

    def update(self, entities: List[Entity]) -> None:
        pass

class World:
    def __init__(self, map_width: int = 20, map_height: int = 20):
        self.entities: List[Entity] = []
        self.systems: List[System] = []
        self.game_map = GameMap(map_width, map_height)
        self.phase_systems: Dict[GamePhase, List[System]] = {
            GamePhase.MOVEMENT: [],
            GamePhase.COMBAT: [],
            GamePhase.SPAWN: []
        }
        # Define the order of phases
        self.phase_order = [
            GamePhase.MOVEMENT,
            GamePhase.COMBAT,
            GamePhase.SPAWN
        ]
        self.logger = GameLogger()
        
    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)
        
    def add_system(self, system: System, phase: GamePhase = None) -> None:
        self.systems.append(system)
        if phase:
            self.phase_systems[phase].append(system)
        
    def update_phase(self, phase: GamePhase) -> None:
        self.logger.log_phase(phase.name)
        for system in self.phase_systems[phase]:
            system.update(self.entities)

    def update(self) -> None:
        # Execute all phases in order
        for phase in self.phase_order:
            self.update_phase(phase)