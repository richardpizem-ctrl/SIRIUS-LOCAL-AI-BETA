# Runtime4 Service Registry
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class ServiceRegistry:
    """
    SIRIUS LOCAL AI — Service Registry (v4.5.0 PRO)

    Responsibilities:
        - Deterministic registration and lookup of services
        - Safe-mode compatible
        - Phase‑5 ready (isolation, no exception leakage)
        - Works with ServiceManager and RuntimeManager45
    """

    def __init__(self, logger=None):
        self.logger = logger
        self.services: dict[str, object] = {}

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[ServiceRegistry] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # REGISTER SERVICE
    # --------------------------------------------------------
    def register(self, name: str, service) -> None:
        """
        Register a service safely.
        Deterministic, safe-mode compatible, no exception leakage.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[ServiceRegistry] SAFE MODE → register('{name}') blocked")
                return

            if not name or service is None:
                if self.logger:
                    self.logger.log(f"[ServiceRegistry] ERROR: Invalid registration for '{name}'")
                return

            self.services[name] = service

            if self.logger:
                self.logger.log(f"[ServiceRegistry] Registered service: {name}")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[ServiceRegistry] register() error: {exc}")

    # --------------------------------------------------------
    # GET SERVICE
    # --------------------------------------------------------
    def get(self, name: str):
        """
        Retrieve a service safely.
        Returns None if not found or on error.
        """
        try:
            if self.logger:
                self.logger.log(f"[ServiceRegistry] get('{name}') called")

            return self.services.get(name, None)

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[ServiceRegistry] get() error: {exc}")
            return None

    # --------------------------------------------------------
    # LIST SERVICES
    # --------------------------------------------------------
    def list(self) -> list[str]:
        """
        Return list of registered service names.
        """
        try:
            names = list(self.services.keys())

            if self.logger:
                self.logger.log(f"[ServiceRegistry] list() → {names}")

            return names

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[ServiceRegistry] list() error: {exc}")
            return []

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[ServiceRegistry] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[ServiceRegistry] SAFE MODE disabled")
