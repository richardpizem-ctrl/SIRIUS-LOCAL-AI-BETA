# Runtime4 Configuration Validator
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class ConfigValidator:
    """
    SIRIUS LOCAL AI — Configuration Validator (v4.5.0 PRO)

    Responsibilities:
        - Deterministic, safe-mode compatible config validation
        - Phase‑5 rule enforcement
        - Isolated error handling (no exceptions leak)
        - RuntimeManager45-compatible logging
    """

    def __init__(self, logger):
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        self.logger.log("[ConfigValidator] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------------
    def validate(self, config: dict) -> bool:
        """
        Validate configuration dictionary.
        Phase‑5 rules:
            - Deterministic behavior
            - No exceptions leak
            - Safe-mode aware
        """
        if self.safe_mode:
            self.logger.log("[ConfigValidator] SAFE MODE → skipping validation")
            return True

        self.logger.log("[ConfigValidator] Validation started")

        try:
            # Basic structure check
            if not isinstance(config, dict):
                self.logger.log("[ConfigValidator] Invalid config type (must be dict)")
                return False

            # Required field: version
            if "version" not in config:
                self.logger.log("[ConfigValidator] Missing required field: version")
                return False

            # Optional Phase‑5 integrity field
            if "integrity" in config:
                if not isinstance(config["integrity"], str):
                    self.logger.log("[ConfigValidator] Invalid integrity field")
                    return False

            # Optional metadata
            if "metadata" in config and not isinstance(config["metadata"], dict):
                self.logger.log("[ConfigValidator] Invalid metadata field")
                return False

            self.logger.log("[ConfigValidator] Validation OK")
            return True

        except Exception as exc:
            self.degraded_mode = True
            self.logger.log(f"[ConfigValidator] Validation error: {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.logger.log("[ConfigValidator] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.logger.log("[ConfigValidator] SAFE MODE disabled")
