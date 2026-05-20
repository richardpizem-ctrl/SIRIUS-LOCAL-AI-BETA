import logging

from modules.fs_module import FSModule
from modules.editor_module import EditorModule
from modules.workflow_module import WorkflowModule

log = logging.getLogger(__name__)


class CommandRouter:
    """
    CommandRouter 4.4
    --------------------
    Routes parsed commands to the correct module and method.

    New in 4.4:
        - Deterministic routing contract
        - Stable error model for Runtime4.4
        - Strict module/method validation
        - Self‑Repair Layer 4.4 compatible output
        - Guaranteed structured response
        - No side-effects outside module execution
    """

    def __init__(self):
        self.name = "router"

        # Registered modules (deterministic order)
        self.modules = {
            "fs": FSModule(),
            "editor": EditorModule(),
            "workflow": WorkflowModule(),
        }

    # --------------------------------------------------------
    # MAIN ROUTE FUNCTION
    # --------------------------------------------------------
    def route(self, parsed: dict):
        """
        Executes a parsed command.
        Deterministic, safe, and audit‑friendly.
        """

        # -----------------------------
        # VALIDATE PARSED OBJECT
        # -----------------------------
        if not isinstance(parsed, dict):
            log.error("ROUTER: Invalid parsed command object.")
            return {
                "status": "error",
                "message": "Invalid parsed command."
            }

        module_name = parsed.get("module")
        method_name = parsed.get("method")
        args = parsed.get("args", [])

        # -----------------------------
        # VALIDATE MODULE
        # -----------------------------
        module = self.modules.get(module_name)
        if module is None:
            log.error("ROUTER: Unknown module '%s'", module_name)
            return {
                "status": "error",
                "message": f"Unknown module '{module_name}'."
            }

        # -----------------------------
        # VALIDATE METHOD
        # -----------------------------
        method = getattr(module, method_name, None)
        if not callable(method):
            log.error("ROUTER: Unknown method '%s' in module '%s'", method_name, module_name)
            return {
                "status": "error",
                "message": f"Unknown method '{method_name}' in module '{module_name}'."
            }

        # -----------------------------
        # EXECUTE METHOD
        # -----------------------------
        try:
            result = method(*args)
            log.info("ROUTER: Executed %s.%s(%s)", module_name, method_name, args)

            return {
                "status": "success",
                "module": module_name,
                "method": method_name,
                "args": args,
                "result": result
            }

        except Exception as exc:
            log.exception("ROUTER: Error executing %s.%s: %s", module_name, method_name, exc)
            return {
                "status": "error",
                "message": f"Execution failed for {module_name}.{method_name}.",
                "exception": str(exc)
            }
