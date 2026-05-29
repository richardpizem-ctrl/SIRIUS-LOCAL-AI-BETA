# runtime5/error_handler_5.py

from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class ErrorHandler5:
    """
    Centralized error handling for Runtime 5.x.
    Ensures:
    - no hard crashes
    - unified fallback structure
    - diagnostics
    - degraded mode awareness
    - Self‑Repair Layer compatibility
    """

    @staticmethod
    def safe_execute(fn, *args, fallback=None, context=None, **kwargs):
        """
        Executes a function safely.
        On error:
        - logs
        - records diagnostics
        - triggers system hooks
        - returns unified fallback structure
        """
        try:
            return fn(*args, **kwargs)

        except Exception as exc:
            name = fn.__name__ if hasattr(fn, "__name__") else "unknown_fn"

            log5(f"[ErrorHandler5] ERROR in {name}: {exc}")
            HealthMonitor5.record_error(str(exc))
            SystemHooks5.on_error(str(exc))

            # Unified fallback structure
            fallback_payload = fallback or {
                "error": True,
                "message": "Runtime5 encountered an internal error.",
                "details": str(exc),
                "context": context,
                "degraded": HealthMonitor5.is_degraded()
            }

            return fallback_payload
