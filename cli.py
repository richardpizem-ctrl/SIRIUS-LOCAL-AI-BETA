import sys
from runtime.runtime_manager import RuntimeManager


class SiriusCLI:
    """
    Simple CLI interface for SIRIUS-LOCAL-AI
    - supports NL commands
    - supports AI tasks
    - serves as terminal input for the runtime
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()

    # --------------------------------------------------------
    # MAIN ENTRY
    # --------------------------------------------------------
    def run(self, argv):
        if len(argv) < 2:
            self._print_help()
            return

        command = argv[1].lower()

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
        # HELP
        # ----------------------------------------------------
        if command == "help":
            self._print_help()
            return

        print(f"Unknown command: {command}")
        self._print_help()

    # --------------------------------------------------------
    # HELPERS
    # --------------------------------------------------------

    def _parse_args(self, items):
        """
        Convert key=value arguments into a dict.
        """
        args = {}
        for item in items:
            if "=" in item:
                key, value = item.split("=", 1)
                args[key] = value
        return args

    def _print_result(self, result):
        """
        Unified output formatting.
        """
        print("--------------------------------------------------")
        for k, v in result.items():
            print(f"{k}: {v}")
        print("--------------------------------------------------")

    def _print_help(self):
        print("""
SIRIUS CLI – available commands:

  sirius nl "<natural sentence>"
      - processes natural language through the NL Router
      - e.g. sirius nl "move vs code to the right"

  sirius task <goal> key=value key=value
      - direct call to the autonomous runtime agent
      - e.g. sirius task move_file source=a.txt target=data/

  sirius context
      - returns system context

  sirius help
      - shows this help
""")


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------

if __name__ == "__main__":
    cli = SiriusCLI()
    cli.run(sys.argv)
