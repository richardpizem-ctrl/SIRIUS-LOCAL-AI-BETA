# Runtime4 System Health — Health Rules
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class HealthRules:
    """
    SIRIUS LOCAL AI — Health Rules (v4.5.0 PRO)

    Responsibilities:
        - Deterministic evaluation of system metrics
        - Safe-mode compatible
        - Phase‑5 ready (isolation, no exception leakage)
        - Used by HealthMonitor and SystemHealth Layer

    Expected metrics structure:
        {
            "cpu": float (0.0–1.0),
            "memory": float (0.0–1.0),
            "disk": float (0.0–1.0),
            "services": {
                "service_name": True/False
            }
        }
    """

    def __init__(self, logger=None):
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[HealthRules] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # MAIN EVALUATION
    # --------------------------------------------------------
    def evaluate(self, metrics: dict | None = None) -> dict:
        """
        Evaluate system health deterministically.
        Returns:
            {
                "ok": bool,
                "issue": str | None
            }
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[HealthRules] SAFE MODE → evaluate() blocked")
                return {"ok": True, "issue": None}

            if self.logger:
                self.logger.log("[HealthRules] Evaluating system metrics")

            if not isinstance(metrics, dict):
                return self._fail("invalid_metrics")

            # --------------------------------------------------------
            # RULE 1 — CPU usage
            # --------------------------------------------------------
            cpu = metrics.get("cpu")
            if isinstance(cpu, (int, float)) and cpu > 0.95:
                return self._fail("cpu_overload")

            # --------------------------------------------------------
            # RULE 2 — Memory usage
            # --------------------------------------------------------
            memory = metrics.get("memory")
            if isinstance(memory, (int, float)) and memory > 0.95:
                return self._fail("memory_overload")

            # --------------------------------------------------------
            # RULE 3 — Disk usage
            # --------------------------------------------------------
            disk = metrics.get("disk")
            if isinstance(disk, (int, float)) and disk > 0.98:
                return self._fail("disk_full")

            # --------------------------------------------------------
            # RULE 4 — Service failures
            # --------------------------------------------------------
            services = metrics.get("services", {})
            if isinstance(services, dict):
                for name, running in services.items():
                    if running is False:
                        return self._fail(f"service_down:{name}")

            # --------------------------------------------------------
            # ALL OK
            # --------------------------------------------------------
            if self.logger:
                self.logger.log("[HealthRules] System health OK")

            return {"ok": True, "issue": None}

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[HealthRules] evaluate() error: {exc}")
            return {"ok": False, "issue": "internal_error"}

    # --------------------------------------------------------
    # INTERNAL FAILURE HANDLER
    # --------------------------------------------------------
    def _fail(self, issue: str) -> dict:
        if self.logger:
            self.logger.log(f"[HealthRules] Issue detected → {issue}")
        return {"ok": False, "issue": issue}

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[HealthRules] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[HealthRules] SAFE MODE disabled")
