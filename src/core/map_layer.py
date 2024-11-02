from typing import Dict, Optional, Any, List
from .hex_grid import HexCoord

class MapLayer:
    def __init__(self, width: int, height: int, default_value: Any = None):
        self.width = width
        self.height = height
        self.data: Dict[HexCoord, List[Any]] = {}
        self.default_value = default_value
        
    def in_bounds(self, coord: HexCoord) -> bool:
        return (0 <= coord.q < self.width and 
                0 <= coord.r < self.height)
        
    def get(self, coord: HexCoord) -> List[Any]:
        if not self.in_bounds(coord):
            return []
        return self.data.get(coord, [])
        
    def add(self, coord: HexCoord, value: Any) -> bool:
        if not self.in_bounds(coord):
            return False
        if coord not in self.data:
            self.data[coord] = []
        self.data[coord].append(value)
        return True
        
    def remove(self, coord: HexCoord, value: Any) -> bool:
        if not self.in_bounds(coord) or coord not in self.data:
            return False
        if value in self.data[coord]:
            self.data[coord].remove(value)
            if not self.data[coord]:  # Clean up empty lists
                del self.data[coord]
            return True
        return False 