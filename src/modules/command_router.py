import logging

from modules.fs_module import FSModule
from modules.editor_module import EditorModule
from modules.workflow_module import WorkflowModule

log = logging.getLogger(__name__)


class CommandRouter:
    """
    CommandRouter 3.5.0
    --------------------
    Takes parsed commands and routes them to the correct module.

    Input example:
        {
            "module": "fs",
            "method": "move",
            "args": ["src/a.py", "modules/a.py"]
        }
    """

    def __init__(self):
        self.name = "router"

        # Registered modules
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
        """

        if not parsed:
            log.error("ROUTER: No parsed command provided.")
            return None

        module_name = parsed.get("module")
        method_name = parsed.get("method")
        args = parsed.get("args", [])

        # Validate module
        module = self.modules.get(module_name)
        if not module:
            log.error("ROUTER: Unknown module '%s'", module_name)
            return None

        # Validate method
        method = getattr(module, method_name, None)
        if not callable(method):
            log.error("ROUTER: Unknown method '%s' in module '%s'", method_name, module_name)
            return None

        try:
            result = method(*args)
            log.info("ROUTER: Executed %s.%s(%s)", module_name, method_name, args)
            return result
        except Exception as exc:
            log.exception("ROUTER: Error executing %s.%s: %s", module_name, method_name, exc)
            return None
