# SIRIUS COLNIK-6.x — Terminal Assistant (SUPER-FINAL + TIMECORE)
# This module checks terminal commands for safety and forbidden operations.

from timecore import TimeCore   # <<< TIMECORE
from terminal_assistant.terminal_assistant_rules import TERMINAL_ASSISTANT_RULES
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TOTO JE OPRAVA — SPRÁVNY IMPORT


class TerminalAssistant:
    def __init__(self):
        # TIMECORE — PILIER 0
        self.timecore = TimeCore()
        self.timecore.runtime_start()

        # Pravidlá z TERMINAL_ASSISTANT_RULES
        self.allowed = TERMINAL_ASSISTANT_RULES.get("allowed", [])
        self.risky = TERMINAL_ASSISTANT_RULES.get("risky", [])
        self.forbidden = TERMINAL_ASSISTANT_RULES.get("forbidden", [])
        self.confirmation_required = TERMINAL_ASSISTANT_RULES.get("confirmation_required", [])

    def is_forbidden(self, command: str) -> bool:
        """Check if command contains any forbidden keyword."""
        cmd_lower = command.lower()
        for bad in self.forbidden:
            if bad in cmd_lower:
                return True
        return False

    def is_allowed(self, command: str) -> bool:
        """Check if command is in allowed list."""
        cmd_lower = command.lower()
        for ok in self.allowed:
            if cmd_lower.startswith(ok):
                return True
        return False

    def is_risky(self, command: str) -> bool:
        """Check if command is in risky list."""
        cmd_lower = command.lower()
        for r in self.risky:
            if cmd_lower.startswith(r):
                return True
        return False

    def needs_confirmation(self, command: str) -> bool:
        """Check if command requires confirmation."""
        cmd_lower = command.lower()
        for c in self.confirmation_required:
            if cmd_lower.startswith(c):
                return True
        return False

    # --- HLAVNÁ METÓDA (používaná testami + autonómiou) ---
    def check_command(self, command: str):
        """
        Return ALLOW or FORBID based on rules.
        Teraz s TIMECORE meraním času + kategóriou.
        """

        self.timecore.cycle_start()   # <<< TIMECORE START

        # 1. Zakázané príkazy → FORBID
        if self.is_forbidden(command):
            self.timecore.cycle_end()
            return {
                "status": "FORBID",
                "category": "FORBIDDEN",
                "requires_confirmation": False,
                "command": command,
                "cycle_time": self.timecore.cycle_delta()
            }

        # 2. Povolené príkazy → ALLOW
        if self.is_allowed(command):
            self.timecore.cycle_end()
            return {
                "status": "ALLOW",
                "category": "ALLOWED",
                "requires_confirmation": False,
                "command": command,
                "cycle_time": self.timecore.cycle_delta()
            }

        # 3. Rizikové príkazy → ALLOW, ale s potvrdením
        if self.is_risky(command):
            self.timecore.cycle_end()
            return {
                "status": "ALLOW",
                "category": "RISKY",
                "requires_confirmation": self.needs_confirmation(command),
                "command": command,
                "cycle_time": self.timecore.cycle_delta()
            }

        # 4. Neznáme príkazy → ALLOW, ale označené ako UNKNOWN
        self.timecore.cycle_end()
        return {
            "status": "ALLOW",
            "category": "UNKNOWN",
            "requires_confirmation": True,
            "command": command,
            "cycle_time": self.timecore.cycle_delta()
        }

    # --- Alias pre budúcu kompatibilitu ---
    def validate(self, command: str):
        """Alias for check_command (compatibility layer)."""
        return self.check_command(command)
