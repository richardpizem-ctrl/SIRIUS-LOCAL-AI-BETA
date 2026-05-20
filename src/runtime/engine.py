import logging
import time

from modules.fs_module import FSModule
from modules.editor_module import EditorModule
from modules.workflow_module import WorkflowModule
from modules.command_parser import CommandParser
from modules.command_router import CommandRouter

log = logging.getLogger(__name__)


class RuntimeEngine:
    """
    RuntimeEngine 4.4
    -----------------
    - Manages module lifecycle
    - Dependency-aware startup
    - Safe shutdown (reverse order)
    - Telemetry and health checks
    - Error isolation
    - Command parsing + routing
    - Deterministic Runtime4.4 behavior
    - Self‑Repair Layer 4.4 compatible
    - Stable structured return values
    """

    def __init__(self):
        self.modules = {}
        self.order = []          # startup order
        self.started = []        # modules that actually started
        self.start_time = None
        self.stop_time = None

        # PC Automation Runtime
        self.parser = CommandParser()
        self.router = CommandRouter()

    # --------------------------------------------------------
    # MODULE REGISTRATION
    # --------------------------------------------------------
    def register_module(self, name: str, module, after: list[str] = None):
        if not isinstance(name, str) or not name:
            raise ValueError("Module name must be a non-empty string.")

        if name in self.modules:
            log.warning("Module '%s' is being overwritten.", name)

        self.modules[name] = {
            "instance": module,
            "after": after or []
        }

        log.info("Module registered: %s", name)

        return {
            "status": "success",
            "module": name
        }

    # --------------------------------------------------------
    # RESOLVE STARTUP ORDER
    # --------------------------------------------------------
    def _resolve_order(self):
        resolved = []
        unresolved = set(self.modules.keys())

        while unresolved:
            progress = False

            for name in list(unresolved):
                deps = self.modules[name]["after"]

                if all(d in resolved for d in deps):
                    resolved.append(name)
                    unresolved.remove(name)
                    progress = True

            if not progress:
                raise RuntimeError("Circular or unresolved module dependencies.")

        self.order = resolved
        log.info("Startup order resolved: %s", self.order)

    # --------------------------------------------------------
    # START ENGINE
    # --------------------------------------------------------
    def start(self):
        log.info("RuntimeEngine starting...")
        self.start_time = time.time()

        # Register PC Automation modules
        self.register_module("fs", FSModule())
        self.register_module("editor", EditorModule())
        self.register_module("workflow", WorkflowModule())

        # Resolve dependency order
        try:
            self._resolve_order()
        except Exception as exc:
            log.exception("Failed to resolve startup order: %s", exc)
            return {
                "status": "error",
                "message": "Failed to resolve startup order.",
                "exception": str(exc)
            }

        for name in self.order:
            module = self.modules[name]["instance"]

            try:
                if hasattr(module, "start"):
                    module.start()

                self.started.append(name)
                log.info("Module started: %s", name)

            except Exception as exc:
                log.exception("Failed to start module '%s': %s", name, exc)

        duration = time.time() - self.start_time
        log.info("RuntimeEngine started in %.2f seconds.", duration)

        return {
            "status": "success",
            "started_modules": self.started,
            "duration": duration
        }

    # --------------------------------------------------------
    # EXECUTE COMMAND
    # --------------------------------------------------------
    def execute(self, command: str):
        """
        Full pipeline:
        1. Parse command
        2. Route to module
        3. Execute method
        """

        log.info("ENGINE: Executing command: %s", command)

        parsed = self.parser.parse(command)
        if not parsed:
            log.error("ENGINE: Parsing failed.")
            return {
                "status": "error",
                "message": "Parsing failed."
            }

        result = self.router.route(parsed)
        return result

    # --------------------------------------------------------
    # STOP ENGINE
    # --------------------------------------------------------
    def stop(self):
        log.info("RuntimeEngine stopping...")
        self.stop_time = time.time()

        # Stop in reverse order
        for name in reversed(self.started):
            module = self.modules[name]["instance"]

            try:
                if hasattr(module, "stop"):
                    module.stop()

                log.info("Module stopped: %s", name)

            except Exception as exc:
                log.exception("Failed to stop module '%s': %s", name, exc)

        duration = time.time() - self.stop_time
        log.info("RuntimeEngine stopped in %.2f seconds.", duration)

        return {
            "status": "success",
            "stopped_modules": list(reversed(self.started)),
            "duration": duration
        }
