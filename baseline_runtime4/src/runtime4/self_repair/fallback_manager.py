# Runtime4 Fallback Manager
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class FallbackManager:
    """
    SIRIUS LOCAL AI — Fallback Manager (v4.5.0 PRO)

    Responsibilities:
        - Activate fallback mode when critical components fail
        - Deterministic, safe-mode compatible behavior
        - Phase‑5 ready (self-repair hooks, isolation)
        - No exception leakage
        - Works with RuntimeManager45 and Self‑Repair Layer
    """

    def __init__(self, logger=None):
        self.logger = logger
        self.active: bool = False
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[FallbackManager] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # ACTIVATE FALLBACK MODE
    # --------------------------------------------------------
    def activate(self) -> None:
        """
        Activate fallback mode safely.
        Phase‑5 rules:
            - Deterministic
            - No exceptions leak
            - Safe-mode aware
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[FallbackManager] SAFE MODE → activate() blocked")
                return

            self.active = True

            if self.logger:
                self.logger.log("[FallbackManager] Fallback mode ACTIVATED")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[FallbackManager] activate() error: {exc}")

    # --------------------------------------------------------
    # DEACTIVATE FALLBACK MODE
    # --------------------------------------------------------
    def deactivate(self) -> None:
        """
        Disable fallback mode safely.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[FallbackManager] SAFE MODE → deactivate() blocked")
                return

            self.active = False

            if self.logger:
                self.logger.log("[FallbackManager] Fallback mode DEACTIVATED")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[FallbackManager] deactivate() error: {exc}")

    # --------------------------------------------------------
    # STATUS CHECK
    # --------------------------------------------------------
    def is_active(self) -> bool:
        """Return True if fallback mode is active."""
        try:
            return self.active
        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[FallbackManager] is_active() error: {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[FallbackManager] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[FallbackManager] SAFE MODE disabled")
