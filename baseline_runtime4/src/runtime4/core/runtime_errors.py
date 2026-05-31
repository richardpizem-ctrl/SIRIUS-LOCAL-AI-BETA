# Runtime4 Runtime Errors
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class RuntimeErrors:
    """
    SIRIUS LOCAL AI — Runtime Errors (v4.5.0 PRO)

    Responsibilities:
        - Collect runtime errors deterministically
        - Provide safe-mode compatible error recording
        - Phase‑5 ready (isolated, no exception leakage)
        - Centralized error storage for RuntimeManager45
        - Compatible with Self‑Repair Layer 4.5
    """

    def __init__(self, logger=None):
        self.errors: list[str] = []
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[RuntimeErrors] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # ADD ERROR (Phase‑5 safe)
    # --------------------------------------------------------
    def add(self, message: str) -> None:
        """
        Add an error message safely.
        Deterministic, safe-mode compatible, no exceptions leak.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[RuntimeErrors] SAFE MODE → blocked add('{message}')")
                return

            self.errors.append(message)

            if self.logger:
                self.logger.log(f"[RuntimeErrors] Added error: {message}")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeErrors] Error in add(): {exc}")

    # --------------------------------------------------------
    # GET ALL ERRORS
    # --------------------------------------------------------
    def get_all(self) -> list[str]:
        """
        Return all stored errors safely.
        """
        try:
            if self.logger:
                self.logger.log("[RuntimeErrors] get_all() called")
            return list(self.errors)

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeErrors] get_all() error: {exc}")
            return []

    # --------------------------------------------------------
    # CLEAR ERRORS
    # --------------------------------------------------------
    def clear(self) -> None:
        """
        Clear all stored errors.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[RuntimeErrors] SAFE MODE → clear() blocked")
                return

            self.errors.clear()

            if self.logger:
                self.logger.log("[RuntimeErrors] Cleared all errors")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeErrors] clear() error: {exc}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[RuntimeErrors] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[RuntimeErrors] SAFE MODE disabled")
