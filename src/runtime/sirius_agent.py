from typing import Dict, Any
import logging
from runtime.runtime_manager import RuntimeManager

log = logging.getLogger(__name__)


class Sirius:
    """
    SIRIUS 4.3+
    Unified entrypoint for the entire SIRIUS LOCAL AI runtime.
    - Initializes RuntimeManager 4.3+
    - Structured initialization result (success/degraded/safe-mode)
    - Provides NL, AI task, and context interfaces
    - Controls runtime engine lifecycle
    - Self‑Repair 4.4 ready
    """

    def __init__(self, safe_mode: bool = False):
        # Create runtime manager
        self.rm = RuntimeManager()

        # Enable safe-mode if requested
        if safe_mode:
            self.rm.safe_mode = True
            log.warning("SIRIUS started in SAFE MODE.")

        # Full initialization pipeline (plugins, modules, NL, workflows, AI loop)
        init_result = self.rm.initialize()

        # Store initialization result for diagnostics
        self.init_result = init_result

        # Log final status
        status = init_result.get("status")
        if status == "success":
            log.info("SIRIUS 4.3 initialized successfully.")
        elif status == "degraded":
            log.warning("SIRIUS 4.3 initialized in DEGRADED MODE.")
        elif status == "safe_mode":
            log.warning("SIRIUS 4.3 running in SAFE MODE.")
        else:
            log.error("SIRIUS 4.3 initialization encountered errors.")

    # --------------------------------------------------------
    # DIRECT AI TASKS
    # --------------------------------------------------------
    def task(self, goal: str, args: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Execute an AI task through the RuntimeManager.
        """
        return self.rm.handle_ai_task(goal, args or {})

    # --------------------------------------------------------
    # NATURAL LANGUAGE PROCESSING
    # --------------------------------------------------------
    def process(self, text: str) -> Dict[str, Any]:
        """
        Process natural language input through NL Router 4.3.
        """
        return self.rm.handle_nl(text)

    # --------------------------------------------------------
    # SYSTEM CONTEXT
    # --------------------------------------------------------
    def context(self) -> Dict[str, Any]:
        """
        Return system context (ContextManager 4.3).
        """
        return self.rm.get_ai_context()

    # --------------------------------------------------------
    # RUNTIME ENGINE CONTROL
    # --------------------------------------------------------
    def start(self):
        """
        Start the runtime engine (RuntimeEngine 4.3).
        """
        self.rm.start()

    def stop(self):
        """
        Stop the runtime engine safely.
        """
        self.rm.stop()


# Global instance (not auto‑initialized)
sirius = None
