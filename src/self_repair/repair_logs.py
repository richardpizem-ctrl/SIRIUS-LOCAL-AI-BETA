"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair Logs 1.0

Účel:
- špecializované logovanie pre Self‑Repair Layer
- jednotný formát logov
- audit trail pre každý opravný cyklus
- bezpečné logovanie bez citlivých údajov
"""

import time
from typing import Dict, Any


class RepairLogger:
    """
    RepairLogger je tenká vrstva nad Logging5,
    ktorá zabezpečuje jednotný formát logov pre opravy.
    """

    def __init__(self, base_logger):
        """
        base_logger – Logging5 instance
        """
        self.base = base_logger

    # ---------------------------------------------------------
    # INTERNAL FORMATTER
    # ---------------------------------------------------------

    def _format(self, level: str, message: str, extra: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Vytvorí jednotnú štruktúru logu.
        """
        return {
            "timestamp": time.time(),
            "level": level,
            "component": "SelfRepair",
            "message": message,
            "extra": extra or {}
        }

    # ---------------------------------------------------------
    # PUBLIC LOGGING API
    # ---------------------------------------------------------

    def info(self, message: str, extra: Dict[str, Any] = None) -> None:
        self.base.log(self._format("INFO", message, extra))

    def warning(self, message: str, extra: Dict[str, Any] = None) -> None:
        self.base.log(self._format("WARNING", message, extra))

    def error(self, message: str, extra: Dict[str, Any] = None) -> None:
        self.base.log(self._format("ERROR", message, extra))

    def exception(self, message: str, extra: Dict[str, Any] = None) -> None:
        """
        Loguje výnimku s tracebackom.
        """
        formatted = self._format("EXCEPTION", message, extra)
        self.base.log_exception(formatted)

    # ---------------------------------------------------------
    # SPECIALIZED SELF‑REPAIR EVENTS
    # ---------------------------------------------------------

    def event_start(self, module: str, error_code: str) -> None:
        self.info(
            "Repair cycle started",
            extra={"module": module, "error_code": error_code}
        )

    def event_stage(self, stage: str, module: str) -> None:
        self.info(
            f"Stage: {stage}",
            extra={"module": module}
        )

    def event_success(self, module: str) -> None:
        self.info(
            "Repair completed successfully",
            extra={"module": module}
        )

    def event_degraded(self, module: str, reason: str) -> None:
        self.warning(
            "Repair ended in degraded mode",
            extra={"module": module, "reason": reason}
        )

    def event_failure(self, module: str, reason: str) -> None:
        self.error(
            "Repair failed",
            extra={"module": module, "reason": reason}
        )
