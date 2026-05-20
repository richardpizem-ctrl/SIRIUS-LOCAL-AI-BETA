import logging
import time
from typing import Dict, Any, Callable

log = logging.getLogger(__name__)


class SiriusAgent:
    """
    SiriusAgent 4.4
    ----------------
    - Unified AI task registry
    - Security Family enforcement (identity, risk, capabilities)
    - Workflow integration
    - Plugin task support
    - Telemetry and error isolation
    - Deterministic structured returns
    - Self‑Repair Layer 4.4 compatible (safe-mode, degraded-mode)
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.tasks: Dict[str, Callable] = {}
        self.task_meta: Dict[str, Dict[str, Any]] = {}
        self.degraded_mode = False

    # --------------------------------------------------------
    # REGISTER TASK
    # --------------------------------------------------------
    def register_task(self, name: str, fn: Callable, meta: Dict[str, Any] = None):
        """
        Register an AI task.

        meta = {
            "description": "...",
            "risk_level": 0.2,
            "required_identity": "OWNER",
            "capabilities": ["fs.read", "net.http"],
            "params": {...}
        }
        """
        name = name.lower().strip()
        self.tasks[name] = fn
        self.task_meta[name] = meta or {}

        log.info("AI task registered: %s", name)

        return {
            "status": "success",
            "task": name
        }

    # --------------------------------------------------------
    # RUN TASK
    # --------------------------------------------------------
    def run_task(self, name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        name = name.lower().strip()

        if name not in self.tasks:
            return {
                "status": "error",
                "task": name,
                "message": f"Unknown AI task: {name}"
            }

        meta = self.task_meta.get(name, {})

        # ----------------------------------------------------
        # SECURITY FAMILY: IDENTITY CHECK
        # ----------------------------------------------------
        required_identity = meta.get("required_identity")
        if required_identity:
            identity = getattr(self.rm.security, "identity", None)
            if identity != required_identity:
                return {
                    "status": "error",
                    "task": name,
                    "message": f"Task '{name}' requires identity '{required_identity}'."
                }

        # ----------------------------------------------------
        # SECURITY FAMILY: RISK CHECK
        # ----------------------------------------------------
        risk = meta.get("risk_level", 0)
        max_risk = getattr(self.rm.security, "max_task_risk", 1.0)

        if risk > max_risk:
            return {
                "status": "error",
                "task": name,
                "message": f"Task '{name}' blocked due to high risk."
            }

        # ----------------------------------------------------
        # SECURITY FAMILY: CAPABILITY CHECK
        # ----------------------------------------------------
        required_caps = meta.get("capabilities", [])
        granted_caps = getattr(self.rm.security, "capabilities", [])

        missing = [cap for cap in required_caps if cap not in granted_caps]

        if missing:
            return {
                "status": "error",
                "task": name,
                "message": f"Missing required capabilities: {missing}"
            }

        # ----------------------------------------------------
        # EXECUTION
        # ----------------------------------------------------
        fn = self.tasks[name]
        start = time.time()

        try:
            result = fn(args, self.rm)

            return {
                "status": "ok",
                "task": name,
                "duration": round(time.time() - start, 4),
                "result": result
            }

        except Exception as exc:
            self.degraded_mode = True
            log.exception("AI task error (%s): %s", name, exc)
            return {
                "status": "error",
                "task": name,
                "message": str(exc)
            }
