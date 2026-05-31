# Runtime4 System Health — Health Monitor
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class HealthMonitor:
    """
    SIRIUS LOCAL AI — Health Monitor (v4.5.0 PRO)

    Responsibilities:
        - Perform deterministic system health checks
        - Integrate with HealthRules and HealthStatus
        - Safe-mode compatible
        - Phase‑5 ready (isolation, no exception leakage)
        - Used by RuntimeManager45 and SystemHealth Layer
    """

    def __init__(self, logger=None, rules=None):
        self.logger = logger
        self.rules = rules  # Optional HealthRules module

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.last_check_ok: bool = True
        self.last_issue: str | None = None

        if self.logger:
            self.logger.log("[HealthMonitor] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # MAIN HEALTH CHECK
    # --------------------------------------------------------
    def check(self) -> bool:
        """
        Perform a deterministic health check.
        Phase‑5 rules:
            - No exceptions leak
            - Safe-mode aware
            - Deterministic output
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[HealthMonitor] SAFE MODE → check() blocked")
                return True

            if self.logger:
                self.logger.log("[HealthMonitor] Health check started")

            # If HealthRules is provided, use it
            if self.rules and hasattr(self.rules, "evaluate"):
                result = self.rules.evaluate()
                self.last_check_ok = bool(result.get("ok", True))
                self.last_issue = result.get("issue", None)

            else:
                # Default deterministic behavior
                self.last_check_ok = True
                self.last_issue = None

            if self.last_check_ok:
                if self.logger:
                    self.logger.log("[HealthMonitor] System health OK")
            else:
                if self.logger:
                    self.logger.log(f"[HealthMonitor] System health issue: {self.last_issue}")

            return self.last_check_ok

        except Exception as exc:
            self.degraded_mode = True
            self.last_check_ok = False
            self.last_issue = str(exc)

            if self.logger:
                self.logger.log(f"[HealthMonitor] check() error: {exc}")

            return False

    # --------------------------------------------------------
    # EXPORT STATUS
    # --------------------------------------------------------
    def status(self) -> dict:
        """Return structured health status safely."""
        try:
            result = {
                "ok": self.last_check_ok,
                "issue": self.last_issue,
                "safe_mode": self.safe_mode,
                "degraded_mode": self.degraded_mode,
            }

            if self.logger:
                self.logger.log(f"[HealthMonitor] status() → {result}")

            return result

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[HealthMonitor] status() error: {exc}")

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
            self.logger.log("[HealthMonitor] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[HealthMonitor] SAFE MODE disabled")
