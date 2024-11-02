import os
from datetime import datetime
from typing import Optional

class GameLogger:
    def __init__(self, log_directory: str = "logs"):
        # Create logs directory if it doesn't exist
        self.log_directory = log_directory
        os.makedirs(log_directory, exist_ok=True)
        
        # Create log file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(log_directory, f"game_log_{timestamp}.txt")
        self._initialize_log_file()
        
    def _initialize_log_file(self):
        with open(self.log_file, 'w') as f:
            f.write(f"Game Log - Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-" * 50 + "\n\n")
    
    def log_turn(self, turn_number: int, player_name: str):
        self._write_log(f"\nTurn {turn_number} - {player_name}'s turn")
        
    def log_phase(self, phase_name: str):
        self._write_log(f"\n  Phase: {phase_name}")
        
    def log_action(self, action: str, details: Optional[str] = None):
        message = f"    • {action}"
        if details:
            message += f": {details}"
        self._write_log(message)
        
    def log_game_end(self, reason: str):
        self._write_log(f"\nGame Ended - {reason}")
        
    def _write_log(self, message: str):
        with open(self.log_file, 'a') as f:
            f.write(f"{message}\n") 