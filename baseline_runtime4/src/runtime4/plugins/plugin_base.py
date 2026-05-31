# Runtime4 Plugin Base
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class PluginBase:
    """
    SIRIUS LOCAL AI — Plugin Base (v4.5.0 PRO)

    Responsibilities:
        - Deterministic plugin lifecycle (initialize/shutdown)
        - Safe-mode compatible plugin execution
        - Phase‑5 ready (isolated, no exception leakage)
        - Base class for all Runtime 4.5 plugins
    """

    def __init__(self, name: str, logger=None):
        self.name = name
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.initialized: bool = False

        if self.logger:
            self.logger.log(f"[PluginBase] Plugin '{self.name}' created (v4.5.0 PRO)")

    # --------------------------------------------------------
    # INITIALIZE (Phase‑5 safe)
    # --------------------------------------------------------
    def initialize(self) -> bool:
        """
        Deterministic, safe-mode compatible initialization.
        Plugins override this method.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[PluginBase] SAFE MODE → init blocked for '{self.name}'")
                return False

            if self.logger:
                self.logger.log(f"[PluginBase] Initializing plugin: {self.name}")

            self.initialized = True
            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[PluginBase] Initialization error in '{self.name}': {exc}")
            return False

    # --------------------------------------------------------
    # SHUTDOWN (Phase‑5 safe)
    # --------------------------------------------------------
    def shutdown(self) -> bool:
        """
        Deterministic, safe-mode compatible shutdown.
        Plugins override this method.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[PluginBase] SAFE MODE → shutdown blocked for '{self.name}'")
                return False

            if self.logger:
                self.logger.log(f"[PluginBase] Shutting down plugin: {self.name}")

            self.initialized = False
            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[PluginBase] Shutdown error in '{self.name}': {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log(f"[PluginBase] SAFE MODE enabled for '{self.name}'")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log(f"[PluginBase] SAFE MODE disabled for '{self.name}'")
