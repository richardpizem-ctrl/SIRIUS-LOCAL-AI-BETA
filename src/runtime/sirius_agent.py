import logging
from typing import Dict, Any
from runtime.runtime_manager import RuntimeManager

log = logging.getLogger(__name__)


class Sirius:
    """
    SIRIUS 4.5
    ---------------------------
    Unified entrypoint for the entire SIRIUS LOCAL AI runtime.

    Updated in 4.5:
        - Deterministic initialization pipeline
        - Stable structured initialization result
        - Safe‑mode + degraded‑mode propagation
        - RuntimeManager 4.5 integration
        - NL Router 4.5 integration
        - AI Task handler 4.5 integration
        - Context provider 4.5
        - Engine lifecycle control 4.5
        - Self‑Repair Layer 4.5 compatible
        - Metadata version bumped to 4.5
    """

    def __init__(self, safe_mode: bool = False):
        # Create runtime manager
        self.rm = RuntimeManager()

        # Enable safe-mode if requested
        if safe_mode:
            self.rm.safe_mode = True
            log.warning("SIRIUS 4.5 started in SAFE MODE.")

        # Full initialization pipeline (plugins, modules, NL, workflows, AI loop)
        init_result = self.rm.initialize()

        # Store initialization result for diagnostics
        self.init_result = init_result

        # Log final status
        status = init_result.get("status")

        if status == "success":
            log.info("SIRIUS 4.5 initialized successfully.")
        elif status == "degraded":
            log.warning("SIRIUS 4.5 initialized in DEGRADED MODE.")
        elif status == "safe_mode":
            log.warning("SIRIUS 4.5 running in SAFE MODE.")
        else:
            log.error("SIRIUS 4.5 initialization encountered errors.")

    # --------------------------------------------------------
    # DIRECT AI TASKS
    # --------------------------------------------------------
    def task(self, goal: str, args: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Execute an AI task through the RuntimeManager 4.5.
        Deterministic structured return.
        """
        result = self.rm.handle_ai_task(goal, args or {})
        if isinstance(result, dict) and "sirius_version" not in result:
            result["sirius_version"] = "4.5"
        return result

    # --------------------------------------------------------
    # NATURAL LANGUAGE PROCESSING
    # --------------------------------------------------------
    def process(self, text: str) -> Dict[str, Any]:
        """
        Process natural language input through NL Router 4.5.
        """
        result = self.rm.handle_nl(text)
        if isinstance(result, dict) and "sirius_version" not in result:
            result["sirius_version"] = "4.5"
        return result

    # --------------------------------------------------------
    # SYSTEM CONTEXT
    # --------------------------------------------------------
    def context(self) -> Dict[str, Any]:
        """
        Return system context (ContextManager 4.5).
        """
        ctx = self.rm.get_ai_context()
        if isinstance(ctx, dict) and "sirius_version" not in ctx:
            ctx["sirius_version"] = "4.5"
        return ctx

    # --------------------------------------------------------
    # RUNTIME ENGINE CONTROL
    # --------------------------------------------------------
    def start(self) -> Dict[str, Any]:
        """
        Start the runtime engine (RuntimeEngine 4.5).
        """
        result = self.rm.start()
        if isinstance(result, dict) and "sirius_version" not in result:
            result["sirius_version"] = "4.5"
        return result

    def stop(self) -> Dict[str, Any]:
        """
        Stop the runtime engine safely.
        """
        result = self.rm.stop()
        if isinstance(result, dict) and "sirius_version" not in result:
            result["sirius_version"] = "4.5"
        return result


# Global instance (not auto‑initialized)
sirius = None
