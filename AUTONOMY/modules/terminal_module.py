# SIRIUS COLNIK-6.x — Autonomy Terminal Module (SUPER-FINAL)
# Tento modul integruje TerminalAssistant do autonómie.
# Autonómia nikdy nevykonáva príkazy — iba vytvára TERMINAL_TASK návrhy.

from timecore import TimeCore
from terminal_assistant.terminal_assistant import TerminalAssistant


class TerminalModule:
    def __init__(self):
        # TIMECORE – PILIER 0
        self.timecore = TimeCore()
        self.timecore.runtime_start()

        # Terminal Assistant (validácia príkazov)
        self.ta = TerminalAssistant()

    # ============================================================
    # HLAVNÁ METÓDA — AUTONÓMIA VOLÁ TÚTO FUNKCIU
    # ============================================================
    def generate_terminal_proposal(self, command: str):
        """
        Vytvorí návrh TERMINAL_TASK na základe validácie príkazu.
        Autonómia nikdy príkaz nevykoná — iba navrhne.
        """

        self.timecore.cycle_start()

        # Validácia príkazu cez TerminalAssistant
        result = self.ta.check_command(command)

        status = result["status"]
        category = result["category"]
        requires_confirmation = result["requires_confirmation"]
        cycle_time = result["cycle_time"]

        # ============================================================
        # ZAKÁZANÉ PRÍKAZY → návrh typu FORBID
        # ============================================================
        if status == "FORBID":
            proposal = {
                "proposal_id": f"terminal-forbid-{command}",
                "module": "terminal_assistant",
                "type": "TERMINAL_TASK",
                "action": "FORBID_COMMAND",
                "target": command,
                "payload": {
                    "command": command,
                    "category": category,
                    "reason": "Forbidden terminal command",
                    "requires_confirmation": False
                },
                "priority": "CRITICAL",
                "cycle_time": cycle_time
            }

            self.timecore.cycle_end()
            return proposal

        # ============================================================
        # POVOLENÉ / RIZIKOVÉ / UNKNOWN → návrh RUN_COMMAND
        # ============================================================
        proposal = {
            "proposal_id": f"terminal-run-{command}",
            "module": "terminal_assistant",
            "type": "TERMINAL_TASK",
            "action": "RUN_COMMAND",
            "target": command,
            "payload": {
                "command": command,
                "category": category,
                "requires_confirmation": requires_confirmation
            },
            "priority": "HIGH" if category in ["RISKY", "UNKNOWN"] else "NORMAL",
            "cycle_time": cycle_time
        }

        self.timecore.cycle_end()
        return proposal

    # ============================================================
    # Alias pre autonómiu — kompatibilita
    # ============================================================
    def handle(self, command: str):
        """Kompatibilná metóda pre autonómiu."""
        return self.generate_terminal_proposal(command)
