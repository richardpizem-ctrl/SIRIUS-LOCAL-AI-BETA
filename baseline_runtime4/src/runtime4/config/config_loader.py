# Runtime4 Configuration Loader
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations

import json
import os


class ConfigLoader:
    """
    SIRIUS LOCAL AI — Configuration Loader (v4.5.0 PRO)

    Responsibilities:
        - Deterministic, safe-mode compatible config loading
        - JSON-based configuration parsing
        - Phase‑5 validation hooks
        - Isolated error handling (no exceptions leak)
        - RuntimeManager45-compatible logging
    """

    def __init__(self, logger):
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        self.logger.log("[ConfigLoader] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------------
    def load(self, path: str) -> dict:
        """
        Load configuration file safely.
        Phase‑5 rules:
            - Deterministic behavior
            - No exceptions leak
            - Safe-mode aware
        """
        if self.safe_mode:
            self.logger.log(f"[ConfigLoader] SAFE MODE → skipping load for: {path}")
            return {}

        self.logger.log(f"[ConfigLoader] Loading config: {path}")

        if not os.path.exists(path):
            self.logger.log(f"[ConfigLoader] File not found: {path}")
            return {}

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                self.logger.log("[ConfigLoader] Invalid config format (must be dict)")
                return {}

            # Phase‑5 validation hook
            if not self._validate(data):
                self.logger.log("[ConfigLoader] Validation failed")
                return {}

            self.logger.log("[ConfigLoader] Config loaded successfully")
            return data

        except Exception as exc:
            self.degraded_mode = True
            self.logger.log(f"[ConfigLoader] Error loading config: {exc}")
            return {}

    # --------------------------------------------------------
    # VALIDATION (Phase‑5)
    # --------------------------------------------------------
    def _validate(self, data: dict) -> bool:
        """
        Phase‑5 baseline validation.
        Can be extended by plugins or runtime modules.
        """
        # Example rule: config must contain "version"
        if "version" not in data:
            self.logger.log("[ConfigLoader] Missing required field: version")
            return False

        return True

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.logger.log("[ConfigLoader] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.logger.log("[ConfigLoader] SAFE MODE disabled")
