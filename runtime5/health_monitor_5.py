# runtime5/health_monitor_5.py

from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5


class HealthMonitor5:
    """
    Lightweight health monitor for Runtime 5.x.
    Tracks:
    - runtime stability
    - error frequency
    - degraded mode triggers
    - future Self-Repair Layer hooks
    """

    error_count = 0
    degraded_mode = False

    @staticmethod
    def record_success():
        return ErrorHandler5.safe_execute(
            lambda: log5("[HealthMonitor5] OK: Runtime cycle completed.")
        )

    @staticmethod
    def record_error(message: str):
        def _exec():
            HealthMonitor5.error_count += 1
            log5(f"[HealthMonitor5] ERROR #{HealthMonitor5.error_count}: {message}")

            if HealthMonitor5.error_count >= 3:
                HealthMonitor5.degraded_mode = True
                log5("[HealthMonitor5] ENTERING DEGRADED MODE")

        return ErrorHandler5.safe_execute(_exec)

    @staticmethod
    def is_degraded():
        return HealthMonitor5.degraded_mode
