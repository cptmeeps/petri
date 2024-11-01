from typing import Dict, List
from dataclasses import dataclass
import uuid

class Entity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.components: Dict = {}
    
    def add_component(self, component: object) -> None:
        self.components[type(component)] = component
        
    def get_component(self, component_type: type) -> object:
        return self.components.get(component_type)

class System:
    def update(self, entities: List[Entity]) -> None:
        pass

class World:
    def __init__(self):
        self.entities: List[Entity] = []
        self.systems: List[System] = []
        
    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)
        
    def add_system(self, system: System) -> None:
        self.systems.append(system)
        
    def update(self) -> None:
        for system in self.systems:
            system.update(self.entities) 