# Runtime4 Module Rebuilder
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations
import os
import shutil


class ModuleRebuilder:
    """
    SIRIUS LOCAL AI — Module Rebuilder (v4.5.0 PRO)

    Responsibilities:
        - Restore modules from baseline_store into target_paths
        - Deterministic, safe-mode compatible rebuild operations
        - Phase‑5 ready (self-repair hooks, isolation)
        - No exception leakage
        - Works with Self‑Repair Layer and RuntimeManager45
    """

    def __init__(self, baseline_store: dict, target_paths: dict, logger=None):
        self.baseline_store = baseline_store or {}
        self.target_paths = target_paths or {}
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.last_rebuild_ok: bool = True

        if self.logger:
            self.logger.log("[ModuleRebuilder] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # REBUILD MODULES
    # --------------------------------------------------------
    def rebuild(self) -> bool:
        """
        Restore modules from baseline_store into target_paths.
        Phase‑5 rules:
            - Deterministic
            - No exceptions leak
            - Safe-mode aware
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[ModuleRebuilder] SAFE MODE → rebuild() blocked")
                return False

            if self.logger:
                self.logger.log("[ModuleRebuilder] Rebuild started")

            self.last_rebuild_ok = True

            # Validate structure
            if not isinstance(self.baseline_store, dict):
                self._fail("Invalid baseline_store format")
                return False

            if not isinstance(self.target_paths, dict):
                self._fail("Invalid target_paths format")
                return False

            # Perform rebuild
            for module_name, baseline_content in self.baseline_store.items():
                if module_name not in self.target_paths:
                    self._fail(f"Missing target path for module: {module_name}")
                    continue

                target_path = self.target_paths[module_name]

                # Ensure directory exists
                os.makedirs(os.path.dirname(target_path), exist_ok=True)

                # Write baseline content
                try:
                    with open(target_path, "w", encoding="utf-8") as f:
                        f.write(baseline_content)

                    if self.logger:
                        self.logger.log(f"[ModuleRebuilder] Restored module: {module_name}")

                except Exception as exc:
                    self._fail(f"Failed to restore {module_name}: {exc}")

            if self.last_rebuild_ok:
                if self.logger:
                    self.logger.log("[ModuleRebuilder] Rebuild OK")
            else:
                if self.logger:
                    self.logger.log("[ModuleRebuilder] Rebuild completed with errors")

            return self.last_rebuild_ok

        except Exception as exc:
            self.degraded_mode = True
            self.last_rebuild_ok = False
            if self.logger:
                self.logger.log(f"[ModuleRebuilder] rebuild() error: {exc}")
            return False

    # --------------------------------------------------------
    # INTERNAL FAILURE HANDLER
    # --------------------------------------------------------
    def _fail(self, message: str):
        """Mark rebuild as failed and log the issue."""
        self.last_rebuild_ok = False
        if self.logger:
            self.logger.log(f"[ModuleRebuilder] ERROR: {message}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[ModuleRebuilder] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[ModuleRebuilder] SAFE MODE disabled")
