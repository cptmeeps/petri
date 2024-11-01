from dataclasses import dataclass

@dataclass
class Unit:
    owner_id: int  # Player ID who owns this unit

@dataclass
class Combat:
    health: int = 100
    max_health: int = 100
    attack: int = 10
    defense: int = 5 