import ast
import logging

log = logging.getLogger(__name__)


class CommandParser:
    """
    CommandParser 4.5
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

    Updated in 4.5:
        - Deterministic AST contract (unchanged)
        - Strict node whitelist (Self‑Repair 4.5)
        - Stable error model for Runtime4.5
        - Guaranteed safe argument extraction
        - No execution, no evaluation, no side‑effects
        - Metadata version bumped to 4.5
    """

    def __init__(self):
        self.name = "parser"

    # --------------------------------------------------------
    # INTERNAL: SAFE NODE CHECK
    # --------------------------------------------------------
    @staticmethod
    def _is_safe_node(node) -> bool:
        """
        Only allow:
        - ast.Expression
        - ast.Call
        - ast.Attribute
        - ast.Name
        - ast.Constant
        """
        safe_types = (
            ast.Expression,
            ast.Call,
            ast.Attribute,
            ast.Name,
            ast.Constant,
        )
        return isinstance(node, safe_types)

    # --------------------------------------------------------
    # MAIN PARSE FUNCTION
    # --------------------------------------------------------
    def parse(self, command: str) -> dict | None:
        """
        Parses a command string into module, method, and args.
        Deterministic, safe, and audit‑friendly.
        """

        if not isinstance(command, str) or not command.strip():
            log.error("PARSER: Empty or invalid command.")
            return None

        try:
            # Convert string into AST
            tree = ast.parse(command.strip(), mode="eval")

            # Validate root node
            if not self._is_safe_node(tree):
                log.error("PARSER: Unsafe root node.")
                return None

            # Must be a function call
            if not isinstance(tree.body, ast.Call):
                log.error("PARSER: Not a valid call expression.")
                return None

            call = tree.body

            # Validate call node
            if not self._is_safe_node(call):
                log.error("PARSER: Unsafe call node.")
                return None

            # Extract module.method
            if not isinstance(call.func, ast.Attribute):
                log.error("PARSER: Invalid function format.")
                return None

            if not isinstance(call.func.value, ast.Name):
                log.error("PARSER: Invalid module name.")
                return None

            module = call.func.value.id
            method = call.func.attr

            # Extract arguments (only constants allowed)
            args = []
            for arg in call.args:
                if not isinstance(arg, ast.Constant):
                    log.error("PARSER: Unsupported argument type: %s", type(arg).__name__)
                    return None
                args.append(arg.value)

            parsed = {
                "module": module,
                "method": method,
                "args": args,
                "parser_version": "4.5"
            }

            log.info("PARSER: Parsed command → %s", parsed)
            return parsed

        except Exception as exc:
            log.exception("PARSER: Failed to parse command '%s': %s", command, exc)
            return None
