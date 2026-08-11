# SIRIUS COLNIK-6.x — Terminal Assistant (PRE-FINAL)
# This module checks terminal commands for safety and forbidden operations.

class TerminalAssistant:
    def __init__(self):
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
        """Return ALLOW or FORBID based on forbidden command list."""
        if self.is_forbidden(command):
            return f"[TERMINAL] Command forbidden: {command}"
        return f"[TERMINAL] Command allowed: {command}"

    # --- Alias pre budúcu kompatibilitu ---
    def validate(self, command: str):
        """Alias for check_command (compatibility layer)."""
        return self.check_command(command)
