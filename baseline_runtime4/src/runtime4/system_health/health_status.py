# Runtime4 System Health — Health Status
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class HealthStatus:
    """
    SIRIUS LOCAL AI — Health Status (v4.5.0 PRO)

    Responsibilities:
        - Deterministic representation of system health
        - Safe-mode compatible
        - Phase‑5 ready (isolation, no exception leakage)
        - Used by HealthMonitor, HealthRules, SystemHealth, RuntimeManager45
    """

    def __init__(self, ok: bool, details: dict | None = None, logger=None):
        self.ok = bool(ok)
        self.details = details or {}
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log(f"[HealthStatus] Created (ok={self.ok}, details={self.details})")

    # --------------------------------------------------------
    # UPDATE STATUS
    # --------------------------------------------------------
    def update(self, ok: bool, details: dict | None = None):
        """Update health status safely."""
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[HealthStatus] SAFE MODE → update() blocked")
                return

            self.ok = bool(ok)
            if details is not None:
                self.details = details

            if self.logger:
                self.logger.log(
                    f"[HealthStatus] Updated → ok={self.ok}, details={self.details}"
                )

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[HealthStatus] update() error: {exc}")

    # --------------------------------------------------------
    # EXPORT SUMMARY
    # --------------------------------------------------------
    def summarize(self) -> dict:
        """Return structured health summary safely."""
        try:
            summary = {
                "ok": self.ok,
                "details": self.details,
                "safe_mode": self.safe_mode,
                "degraded_mode": self.degraded_mode,
            }

            if self.logger:
                self.logger.log(f"[HealthStatus] summarize() → {summary}")

            return summary

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[HealthStatus] summarize() error: {exc}")

            return {
                "ok": False,
                "details": {"error": "internal_error"},
                "safe_mode": self.safe_mode,
                "degraded_mode": True,
            }

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[HealthStatus] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[HealthStatus] SAFE MODE disabled")
