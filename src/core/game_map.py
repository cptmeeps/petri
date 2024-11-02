from enum import Enum, auto
from typing import Dict, Optional
from .map_layer import MapLayer
from .hex_grid import HexCoord

class LayerType(Enum):
    TERRAIN = auto()
    UNITS = auto()
    RESOURCES = auto()
    EFFECTS = auto()

class GameMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.layers: Dict[LayerType, MapLayer] = {
            LayerType.TERRAIN: MapLayer(width, height, default_value="plain"),
            LayerType.UNITS: MapLayer(width, height),
            LayerType.RESOURCES: MapLayer(width, height),
            LayerType.EFFECTS: MapLayer(width, height)
        }
    
    def in_bounds(self, coord: HexCoord) -> bool:
        return self.layers[LayerType.TERRAIN].in_bounds(coord)
    
    def get_layer(self, layer_type: LayerType) -> MapLayer:
        return self.layers[layer_type] 