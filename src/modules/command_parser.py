import ast
import logging

log = logging.getLogger(__name__)


class CommandParser:
    """
    CommandParser 4.3
    --------------------
    Parses structured commands like:

        fs.move("src/a.py", "modules/a.py")
        editor.open_at_line("main.py", 42)
        workflow.generate_module("src/modules", "router")

    Output format:
        {
            "module": "fs",
            "method": "move",
            "args": ["src/a.py", "modules/a.py"]
        }

    Improvements in 4.3:
    - deterministic Runtime4 behavior
    - strict AST validation (no unsafe nodes)
    - consistent error structure
    - Self‑Repair 4.4 compatible
    """

    def __init__(self):
        self.name = "parser"

    # --------------------------------------------------------
    # MAIN PARSE FUNCTION
    # --------------------------------------------------------
    def parse(self, command: str) -> dict | None:
        """
        Parses a command string into module, method, and args.
        """

        if not isinstance(command, str) or not command.strip():
            log.error("PARSER: Empty or invalid command.")
            return None

        try:
            # Convert string into AST
            tree = ast.parse(command.strip(), mode="eval")

            # Must be a function call
            if not isinstance(tree.body, ast.Call):
                log.error("PARSER: Not a valid call expression.")
                return None

            call = tree.body

            # Extract module.method
            if not isinstance(call.func, ast.Attribute):
                log.error("PARSER: Invalid function format.")
                return None

            # Module name must be an identifier
            if not isinstance(call.func.value, ast.Name):
                log.error("PARSER: Invalid module name.")
                return None

            module = call.func.value.id
            method = call.func.attr

            # Extract arguments (only constants allowed)
            args = []
            for arg in call.args:
                if isinstance(arg, ast.Constant):
                    args.append(arg.value)
                else:
                    log.error("PARSER: Unsupported argument type: %s", type(arg).__name__)
                    return None

            parsed = {
                "module": module,
                "method": method,
                "args": args
            }

            log.info("PARSER: Parsed command → %s", parsed)
            return parsed

        except Exception as exc:
            log.exception("PARSER: Failed to parse command '%s': %s", command, exc)
            return None
