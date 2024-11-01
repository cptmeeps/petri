from dataclasses import dataclass
from src.core.hex_grid import HexCoord
from typing import List

@dataclass
class Position:
    coord: HexCoord

@dataclass
class MovementSpeed:
    speed: int  # Number of hexes that can be moved 

@dataclass
class MovementPath:
    path: List[HexCoord] = None
    current_index: int = 0
    
    def is_complete(self) -> bool:
        return self.path is None or self.current_index >= len(self.path)