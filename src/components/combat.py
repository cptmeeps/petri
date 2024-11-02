from dataclasses import dataclass

@dataclass
class CombatRange:
    min_range: int = 1  # Minimum attack range in hexes
    max_range: int = 1  # Maximum attack range in hexes 