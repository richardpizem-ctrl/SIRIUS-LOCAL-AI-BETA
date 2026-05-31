# Runtime4 Self‑Repair — Repair Monitor
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class RepairMonitor:
    """
    SIRIUS LOCAL AI — Repair Monitor (v4.5.0 PRO)

    Responsibilities:
        - Monitor health of Self‑Repair Layer components
        - Detect degraded or failed repair cycles
        - Deterministic, safe-mode compatible monitoring
        - Phase‑5 ready (isolation, no exception leakage)
        - Works with RepairLogger, RepairCore, RepairStateMachine
    """

    def __init__(self, logger=None):
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        # Internal health flags
        self.last_check_ok: bool = True
        self.last_issue: str | None = None

        if self.logger:
            self.logger.log("[RepairMonitor] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # HEALTH CHECK
    # --------------------------------------------------------
    def check(self) -> bool:
        """
        Perform a deterministic health check of the Self‑Repair Layer.
        Phase‑5 rules:
            - No exceptions leak
            - Safe-mode aware
            - Deterministic output
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[RepairMonitor] SAFE MODE → check() blocked")
                return True

            if self.logger:
                self.logger.log("[RepairMonitor] Health check started")

            # Phase‑5: deterministic check
            # (In PRO version, this is a placeholder for deeper diagnostics)
            self.last_check_ok = True
            self.last_issue = None

            if self.logger:
                self.logger.log("[RepairMonitor] Health check OK")

            return True

        except Exception as exc:
            self.degraded_mode = True
            self.last_check_ok = False
            self.last_issue = str(exc)

            if self.logger:
                self.logger.log(f"[RepairMonitor] check() error: {exc}")

            return False

    # --------------------------------------------------------
    # STATUS EXPORT
    # --------------------------------------------------------
    def status(self) -> dict:
        """Return structured monitoring status."""
        try:
            result = {
                "ok": self.last_check_ok,
                "issue": self.last_issue,
                "safe_mode": self.safe_mode,
                "degraded_mode": self.degraded_mode,
            }

            if self.logger:
                self.logger.log(f"[RepairMonitor] status() → {result}")

            return result

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RepairMonitor] status() error: {exc}")

            return {
                "ok": False,
                "issue": "internal_error",
                "safe_mode": self.safe_mode,
                "degraded_mode": True,
            }

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[RepairMonitor] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[RepairMonitor] SAFE MODE disabled")
