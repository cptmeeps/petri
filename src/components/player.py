from dataclasses import dataclass
from typing import Optional

@dataclass
class Player:
    id: int
    name: str
    color: str  # Could be used for visual representation
    is_active: bool = True 