# Runtime4 Plugin Manager
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class PluginManager:
    """
    SIRIUS LOCAL AI — Plugin Manager (v4.5.0 PRO)

    Responsibilities:
        - Register and manage plugin lifecycle
        - Deterministic, safe-mode compatible initialization/shutdown
        - Phase‑5 ready (isolated, no exception leakage)
        - Works with PluginBase and PluginLoader45
    """

    def __init__(self, logger=None):
        self.logger = logger
        self.plugins: dict[str, object] = {}
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[PluginManager] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # REGISTER PLUGIN
    # --------------------------------------------------------
    def register(self, plugin) -> None:
        """
        Register a plugin safely.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[PluginManager] SAFE MODE → blocked register('{plugin.name}')")
                return

            self.plugins[plugin.name] = plugin

            if self.logger:
                self.logger.log(f"[PluginManager] Registered plugin: {plugin.name}")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[PluginManager] register() error: {exc}")

    # --------------------------------------------------------
    # INITIALIZE ALL PLUGINS
    # --------------------------------------------------------
    def initialize_all(self) -> bool:
        """
        Initialize all registered plugins safely.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[PluginManager] SAFE MODE → initialize_all() blocked")
                return False

            if self.logger:
                self.logger.log("[PluginManager] Initializing all plugins")

            for name, plugin in self.plugins.items():
                ok = plugin.initialize()
                if not ok:
                    if self.logger:
                        self.logger.log(f"[PluginManager] Plugin init failed: {name}")
                    self.degraded_mode = True

            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[PluginManager] initialize_all() error: {exc}")
            return False

    # --------------------------------------------------------
    # SHUTDOWN ALL PLUGINS
    # --------------------------------------------------------
    def shutdown_all(self) -> bool:
        """
        Shutdown all registered plugins safely.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[PluginManager] SAFE MODE → shutdown_all() blocked")
                return False

            if self.logger:
                self.logger.log("[PluginManager] Shutting down all plugins")

            for name, plugin in self.plugins.items():
                ok = plugin.shutdown()
                if not ok:
                    if self.logger:
                        self.logger.log(f"[PluginManager] Plugin shutdown failed: {name}")
                    self.degraded_mode = True

            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[PluginManager] shutdown_all() error: {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[PluginManager] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[PluginManager] SAFE MODE disabled")
