# Runtime4 Self‑Repair — Repair Logger
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations
import time


class RepairLogger:
    """
    SIRIUS LOCAL AI — Repair Logger (v4.5.0 PRO)

    Responsibilities:
        - Deterministic logging for Self‑Repair Layer
        - Safe-mode compatible, isolated, no exception leakage
        - Phase‑5 ready (structured logs, audit trail)
        - Works with RepairCore, RepairPlanner, RepairStateMachine, RepairSandbox
    """

    def __init__(self, logger=None):
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.entries: list[dict] = []

        if self.logger:
            self.logger.log("[RepairLogger] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # INTERNAL FORMATTER
    # --------------------------------------------------------
    def _format(self, level: str, message: str, extra: dict | None = None) -> dict:
        """Create deterministic structured log entry."""
        return {
            "timestamp": time.time(),
            "level": level,
            "component": "SelfRepair",
            "message": message,
            "extra": extra or {},
        }

    # --------------------------------------------------------
    # PUBLIC LOGGING API
    # --------------------------------------------------------
    def log(self, message: str, extra: dict | None = None) -> None:
        """Generic info log."""
        try:
            if self.safe_mode:
                return

            entry = self._format("INFO", message, extra)
            self.entries.append(entry)

            if self.logger:
                self.logger.log(f"[RepairLogger] {message}")

        except Exception as exc:
            self._fail(exc)

    def warn(self, message: str, extra: dict | None = None) -> None:
        """Warning log."""
        try:
            if self.safe_mode:
                return

            entry = self._format("WARNING", message, extra)
            self.entries.append(entry)

            if self.logger:
                self.logger.log(f"[RepairLogger] WARNING: {message}")

        except Exception as exc:
            self._fail(exc)

    def error(self, message: str, extra: dict | None = None) -> None:
        """Error log."""
        try:
            if self.safe_mode:
                return

            entry = self._format("ERROR", message, extra)
            self.entries.append(entry)

            if self.logger:
                self.logger.log(f"[RepairLogger] ERROR: {message}")

        except Exception as exc:
            self._fail(exc)

    # --------------------------------------------------------
    # SPECIALIZED SELF‑REPAIR EVENTS
    # --------------------------------------------------------
    def event_start(self, module: str, error_code: str) -> None:
        self.log("Repair cycle started", extra={"module": module, "error_code": error_code})

    def event_stage(self, stage: str, module: str) -> None:
        self.log(f"Stage: {stage}", extra={"module": module})

    def event_success(self, module: str) -> None:
        self.log("Repair completed successfully", extra={"module": module})

    def event_degraded(self, module: str, reason: str) -> None:
        self.warn("Repair ended in degraded mode", extra={"module": module, "reason": reason})

    def event_failure(self, module: str, reason: str) -> None:
        self.error("Repair failed", extra={"module": module, "reason": reason})

    # --------------------------------------------------------
    # EXPORT LOGS
    # --------------------------------------------------------
    def export(self) -> list[dict]:
        """Return all structured logs safely."""
        try:
            return list(self.entries)
        except Exception as exc:
            self._fail(exc)
            return []

    # --------------------------------------------------------
    # INTERNAL FAILURE HANDLER
    # --------------------------------------------------------
    def _fail(self, exc: Exception):
        """Mark logger as degraded and record internal failure."""
        self.degraded_mode = True
        if self.logger:
            self.logger.log(f"[RepairLogger] INTERNAL ERROR: {exc}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[RepairLogger] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[RepairLogger] SAFE MODE disabled")
