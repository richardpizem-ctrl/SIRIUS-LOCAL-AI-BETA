# SIRIUS COLNIK-6.x — Terminal Assistant (FINAL + TIMECORE)
# This module checks terminal commands for safety and forbidden operations.

from timecore import TimeCore   # <<< TIMECORE

class TerminalAssistant:
    def __init__(self):
        # TIMECORE — PILIER 0
        self.timecore = TimeCore()
        self.timecore.runtime_start()

        # Základná sada zakázaných príkazov (PRE-FINAL)
        self.forbidden = [
            "format",
            "del /f /s /q",
            "rm -rf",
            "shutdown",
            "mkfs",
            "diskpart",
            "erase",
            "poweroff"
        ]

    def is_forbidden(self, command: str) -> bool:
        """Check if command contains any forbidden keyword."""
        cmd_lower = command.lower()
        for bad in self.forbidden:
            if bad in cmd_lower:
                return True
        return False

    # --- HLAVNÁ METÓDA (používaná testami) ---
    def check_command(self, command: str):
        """
        Return ALLOW or FORBID based on forbidden command list.
        Teraz s TIMECORE meraním času.
        """

        self.timecore.cycle_start()   # <<< TIMECORE START

        if self.is_forbidden(command):
            self.timecore.cycle_end()
            return {
                "status": "FORBID",
                "command": command,
                "cycle_time": self.timecore.cycle_delta()
            }

        self.timecore.cycle_end()
        return {
            "status": "ALLOW",
            "command": command,
            "cycle_time": self.timecore.cycle_delta()
        }

    # --- Alias pre budúcu kompatibilitu ---
    def validate(self, command: str):
        """Alias for check_command (compatibility layer)."""
        return self.check_command(command)
