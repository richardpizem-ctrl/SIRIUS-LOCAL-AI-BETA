# Runtime4 Service Manager
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class ServiceManager:
    """
    SIRIUS LOCAL AI — Service Manager (v4.5.0 PRO)

    Responsibilities:
        - Start/stop services deterministically
        - Safe-mode compatible service control
        - Phase‑5 ready (isolation, no exception leakage)
        - Works with RuntimeManager45 and PluginManager
    """

    def __init__(self, registry: dict, logger=None):
        self.registry = registry or {}
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[ServiceManager] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # START SERVICE
    # --------------------------------------------------------
    def start(self, name: str) -> bool:
        """
        Start a service safely.
        Deterministic, safe-mode compatible, no exception leakage.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[ServiceManager] SAFE MODE → start('{name}') blocked")
                return False

            if name not in self.registry:
                if self.logger:
                    self.logger.log(f"[ServiceManager] ERROR: Unknown service '{name}'")
                return False

            service = self.registry[name]

            if hasattr(service, "start"):
                ok = service.start()
            else:
                ok = False

            if ok:
                if self.logger:
                    self.logger.log(f"[ServiceManager] Service started: {name}")
                return True

            if self.logger:
                self.logger.log(f"[ServiceManager] Service FAILED to start: {name}")
            return False

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[ServiceManager] start() error: {exc}")
            return False

    # --------------------------------------------------------
    # STOP SERVICE
    # --------------------------------------------------------
    def stop(self, name: str) -> bool:
        """
        Stop a service safely.
        Deterministic, safe-mode compatible, no exception leakage.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[ServiceManager] SAFE MODE → stop('{name}') blocked")
                return False

            if name not in self.registry:
                if self.logger:
                    self.logger.log(f"[ServiceManager] ERROR: Unknown service '{name}'")
                return False

            service = self.registry[name]

            if hasattr(service, "stop"):
                ok = service.stop()
            else:
                ok = False

            if ok:
                if self.logger:
                    self.logger.log(f"[ServiceManager] Service stopped: {name}")
                return True

            if self.logger:
                self.logger.log(f"[ServiceManager] Service FAILED to stop: {name}")
            return False

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[ServiceManager] stop() error: {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[ServiceManager] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[ServiceManager] SAFE MODE disabled")
