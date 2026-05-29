# runtime5/health_monitor_5.py

import time
from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.system_hooks_5 import SystemHooks5


class HealthMonitor5:
    """
    Advanced health monitor for Runtime 5.x.
    Tracks:
    - runtime stability
    - error frequency
    - degraded mode triggers
    - recovery conditions
    - timestamps
    - Self‑Repair Layer hooks
    """

    error_count = 0
    success_count = 0
    degraded_mode = False
    last_error_time = None

    ERROR_THRESHOLD = 3          # errors before degraded mode
    RECOVERY_THRESHOLD = 5       # successes to exit degraded mode
    ERROR_DECAY_SECONDS = 120    # errors older than 2 min decay

    # --------------------------------------------------------
    # SUCCESS
    # --------------------------------------------------------
    @staticmethod
    def record_success():
        def _exec():
            HealthMonitor5.success_count += 1

            # decay error count over time
            HealthMonitor5._decay_errors()

            if HealthMonitor5.degraded_mode and HealthMonitor5.success_count >= HealthMonitor5.RECOVERY_THRESHOLD:
                HealthMonitor5.degraded_mode = False
                log5("[HealthMonitor5] EXITING DEGRADED MODE")
                SystemHooks5.on_recovery()

            log5("[HealthMonitor5] OK: Runtime cycle completed.")

        return ErrorHandler5.safe_execute(_exec)

    # --------------------------------------------------------
    # ERROR
    # --------------------------------------------------------
    @staticmethod
    def record_error(message: str):
        def _exec():
            HealthMonitor5.error_count += 1
            HealthMonitor5.last_error_time = time.time()
            HealthMonitor5.success_count = 0  # reset success streak

            log5(f"[HealthMonitor5] ERROR #{HealthMonitor5.error_count}: {message}")

            if HealthMonitor5.error_count >= HealthMonitor5.ERROR_THRESHOLD:
                if not HealthMonitor5.degraded_mode:
                    HealthMonitor5.degraded_mode = True
                    log5("[HealthMonitor5] ENTERING DEGRADED MODE")
                    SystemHooks5.on_degraded()

        return ErrorHandler5.safe_execute(_exec)

    # --------------------------------------------------------
    # DECAY OLD ERRORS
    # --------------------------------------------------------
    @staticmethod
    def _decay_errors():
        if HealthMonitor5.last_error_time is None:
            return

        if time.time() - HealthMonitor5.last_error_time > HealthMonitor5.ERROR_DECAY_SECONDS:
            HealthMonitor5.error_count = max(0, HealthMonitor5.error_count - 1)
            HealthMonitor5.last_error_time = time.time()

    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------
    @staticmethod
    def is_degraded():
        return HealthMonitor5.degraded_mode

    @staticmethod
    def snapshot():
        """
        Returns a structured health snapshot for diagnostics.
        """
        return {
            "errors": HealthMonitor5.error_count,
            "successes": HealthMonitor5.success_count,
            "degraded": HealthMonitor5.degraded_mode,
            "last_error_time": HealthMonitor5.last_error_time,
        }

    # --------------------------------------------------------
    # MANUAL RESET
    # --------------------------------------------------------
    @staticmethod
    def reset():
        HealthMonitor5.error_count = 0
        HealthMonitor5.success_count = 0
        HealthMonitor5.degraded_mode = False
        HealthMonitor5.last_error_time = None
        log5("[HealthMonitor5] RESET")
