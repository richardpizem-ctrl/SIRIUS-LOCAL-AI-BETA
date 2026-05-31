# Runtime4 Service Status
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class ServiceStatus:
    """
    SIRIUS LOCAL AI — Service Status (v4.5.0 PRO)

    Responsibilities:
        - Deterministic representation of service state
        - Safe-mode compatible
        - Phase‑5 ready (isolation, no exception leakage)
        - Used by ServiceManager, ServiceRegistry, RuntimeManager45
    """

    def __init__(self, name: str, running: bool, details: dict | None = None, logger=None):
        self.name = name
        self.running = running
        self.details = details or {}
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log(f"[ServiceStatus] Created status for '{self.name}' (running={self.running})")

    # --------------------------------------------------------
    # UPDATE RUNNING STATE
    # --------------------------------------------------------
    def update(self, running: bool, details: dict | None = None):
        """Update service status safely."""
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[ServiceStatus] SAFE MODE → update('{self.name}') blocked")
                return

            self.running = running
            if details is not None:
                self.details = details

            if self.logger:
                self.logger.log(
                    f"[ServiceStatus] Updated '{self.name}' → running={self.running}, details={self.details}"
                )

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[ServiceStatus] update() error: {exc}")

    # --------------------------------------------------------
    # EXPORT STATUS
    # --------------------------------------------------------
    def to_dict(self) -> dict:
        """Return structured service status safely."""
        try:
            status = {
                "name": self.name,
                "running": self.running,
                "details": self.details,
            }

            if self.logger:
                self.logger.log(f"[ServiceStatus] to_dict('{self.name}') → {status}")

            return status

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[ServiceStatus] to_dict() error: {exc}")

            return {
                "name": self.name,
                "running": False,
                "details": {"error": "internal_error"},
            }

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log(f"[ServiceStatus] SAFE MODE enabled for '{self.name}'")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log(f"[ServiceStatus] SAFE MODE disabled for '{self.name}'")
