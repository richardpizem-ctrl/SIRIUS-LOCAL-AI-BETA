# cli_4_5.py
# SIRIUS LOCAL AI – Command Line Interface (v4.5.0 PRO)
# Deterministic, safe-mode compatible CLI front-end (Phase‑5 ready)

from __future__ import annotations

import sys
from runtime.runtime_manager_4_5 import RuntimeManager45


class SiriusCLI45:
    """
    SIRIUS LOCAL AI — Command Line Interface (v4.5.0 PRO)

    Features:
        - Natural language commands
        - Direct AI task execution
        - System context inspection
        - Safe-mode + degraded-mode support
        - Deterministic, offline-only behavior
        - Phase‑5 ready
    """

    def __init__(self):
        self.rm = RuntimeManager45()
        self.safe_mode = False
        self.degraded_mode = False

        try:
            self.rm.initialize()
            self.rm.logger.info("CLI initialized (v4.5.0 PRO)")
        except Exception as exc:
            self.degraded_mode = True
            print(f"[CLI] Initialization failed: {exc}")

    # --------------------------------------------------------
    # MAIN ENTRY (4.5.0 PRO)
    # --------------------------------------------------------
    def run(self, argv):
        if len(argv) < 2:
            self._print_help()
            return

        command = argv[1].lower()

        if self.safe_mode:
            print("SIRIUS CLI is in SAFE MODE. Only 'context' and 'help' are available.")
            if command not in {"context", "help"}:
                return

        try:
            # ----------------------------------------------------
            # NATURAL LANGUAGE
            # sirius nl "move vs code to the right"
            # ----------------------------------------------------
            if command == "nl":
                text = " ".join(argv[2:])
                result = self.rm.handle_nl(text)
                self._print_result(result)
                return

            # ----------------------------------------------------
            # DIRECT AI TASKS
            # sirius task snap_right app="vs code"
            # ----------------------------------------------------
            if command == "task":
                if len(argv) < 3:
                    print("Missing task name.")
                    return

                goal = argv[2]
                args = self._parse_args(argv[3:])
                result = self.rm.handle_ai_task(goal, args)
                self._print_result(result)
                return

            # ----------------------------------------------------
            # SYSTEM CONTEXT
            # sirius context
            # ----------------------------------------------------
            if command == "context":
                result = self.rm.get_ai_context()
                self._print_result(result)
                return

            # ----------------------------------------------------
            # SAFE MODE
            # sirius safemode on/off
            # ----------------------------------------------------
            if command == "safemode":
                if len(argv) < 3:
                    print("Usage: sirius safemode on|off")
                    return

                mode = argv[2].lower()
                if mode == "on":
                    self.safe_mode = True
                    print("SAFE MODE enabled.")
                elif mode == "off":
                    self.safe_mode = False
                    print("SAFE MODE disabled.")
                else:
                    print("Usage: sirius safemode on|off")
                return

            # ----------------------------------------------------
            # HELP
            # ----------------------------------------------------
            if command == "help":
                self._print_help()
                return

            print(f"Unknown command: {command}")
            self._print_help()

        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"CLI error: {e}")
            print("An internal error occurred. Check logs for details.")

    # --------------------------------------------------------
    # HELPERS (4.5.0 PRO)
    # --------------------------------------------------------
    def _parse_args(self, items):
        """Convert key=value arguments into a dict."""
        args = {}
        for item in items:
            if "=" in item:
                key, value = item.split("=", 1)
                args[key] = value
        return args

    def _print_result(self, result):
        """Unified output formatting."""
        print("--------------------------------------------------")
        if isinstance(result, dict):
            for k, v in result.items():
                print(f"{k}: {v}")
        else:
            print(result)
        print("--------------------------------------------------")

    def _print_help(self):
        print("""
SIRIUS CLI – available commands (v4.5.0 PRO):

  sirius nl "<natural sentence>"
      - processes natural language through the NL Router 4.5
      - e.g. sirius nl "move vs code to the right"

  sirius task <goal> key=value key=value
      - direct call to the autonomous runtime agent
      - e.g. sirius task move_file source=a.txt target=data/

  sirius context
      - returns system context

  sirius safemode on|off
      - enables or disables SAFE MODE

  sirius help
      - shows this help
""")

# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    cli = SiriusCLI45()
    cli.run(sys.argv)
