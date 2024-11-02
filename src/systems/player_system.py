from typing import List, Optional, Dict
from ..core.ecs import System, Entity
from ..components.player import Player
from ..components.unit import Unit

class PlayerSystem(System):
    def __init__(self, world):
        self.world = world
        self.players = []
        self.current_player_index = 0

    def add_player(self, world, name: str, color: str) -> Entity:
        player_id = len(self.players) + 1
        player_entity = Entity()
        player_entity.add_component(Player(id=player_id, name=name, color=color))
        self.players.append(player_entity)
        world.add_entity(player_entity)
        return player_entity

    def get_player_units(self, entities: List[Entity], player_id: int) -> List[Entity]:
        return [
            entity for entity in entities
            if entity.get_component(Unit) and entity.get_component(Unit).owner_id == player_id
        ]

    def next_turn(self) -> None:
        if not self.players:
            return
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_current_player(self) -> Optional[Entity]:
        if not self.players:
            return None
        return self.players[self.current_player_index]

    def update(self, entities: List[Entity]) -> None:
        # Check win conditions or player elimination
        for player in self.players[:]:
            player_units = self.get_player_units(entities, player.get_component(Player).id)
            if not player_units:
                player.get_component(Player).is_active = False 