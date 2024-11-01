from dataclasses import dataclass
from typing import List, Tuple, Set
import math

@dataclass(frozen=True)
class HexCoord:
    q: int  # x-axis
    r: int  # y-axis
    
    def __add__(self, other: 'HexCoord') -> 'HexCoord':
        return HexCoord(self.q + other.q, self.r + other.r)
    
    def __sub__(self, other: 'HexCoord') -> 'HexCoord':
        return HexCoord(self.q - other.q, self.r - other.r)

class HexGrid:
    # Directions in axial coordinates (q, r)
    DIRECTIONS = [
        HexCoord(1, 0),   # East
        HexCoord(1, -1),  # Northeast
        HexCoord(0, -1),  # Northwest
        HexCoord(-1, 0),  # West
        HexCoord(-1, 1),  # Southwest
        HexCoord(0, 1),   # Southeast
    ]
    
    @staticmethod
    def distance(a: HexCoord, b: HexCoord) -> int:
        """Calculate the distance between two hex coordinates."""
        vec = b - a
        # In axial coordinates, distance is (abs(q) + abs(r) + abs(-q-r)) / 2
        return (abs(vec.q) + abs(vec.r) + abs(-vec.q - vec.r)) // 2
    
    @staticmethod
    def get_neighbor(coord: HexCoord, direction: int) -> HexCoord:
        """Get the neighboring hex in a given direction (0-5)."""
        return coord + HexGrid.DIRECTIONS[direction]
    
    @staticmethod
    def get_neighbors(coord: HexCoord) -> List[HexCoord]:
        """Get all neighboring hexes."""
        return [coord + direction for direction in HexGrid.DIRECTIONS]
    
    @staticmethod
    def get_range(center: HexCoord, radius: int) -> Set[HexCoord]:
        """Get all hexes within a given range."""
        results = set()
        for q in range(-radius, radius + 1):
            r1 = max(-radius, -q - radius)
            r2 = min(radius, -q + radius)
            for r in range(r1, r2 + 1):
                results.add(HexCoord(q + center.q, r + center.r))
        return results
    
    @staticmethod
    def line(start: HexCoord, end: HexCoord) -> List[HexCoord]:
        """Get all hexes in a line from start to end."""
        N = HexGrid.distance(start, end)
        if N == 0:
            return [start]
        
        results = []
        for i in range(N + 1):
            t = 1.0 * i / N
            q = round(start.q * (1-t) + end.q * t)
            r = round(start.r * (1-t) + end.r * t)
            results.append(HexCoord(q, r))
        return results 