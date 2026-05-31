# Runtime4 Runtime State
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class RuntimeState:
    """
    SIRIUS LOCAL AI — Runtime State (v4.5.0 PRO)

    Responsibilities:
        - Store runtime state values deterministically
        - Provide safe-mode compatible state access
        - Phase‑5 ready (isolated, no exception leakage)
        - Central state container for RuntimeManager45
    """

    def __init__(self, logger=None):
        self.state: dict[str, object] = {}
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[RuntimeState] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # SET VALUE (Phase‑5 safe)
    # --------------------------------------------------------
    def set(self, key: str, value) -> bool:
        """
        Deterministic, safe-mode compatible setter.
        No exceptions leak.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[RuntimeState] SAFE MODE → blocked set('{key}')")
                return False

            self.state[key] = value

            if self.logger:
                self.logger.log(f"[RuntimeState] set('{key}') = {value}")

            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeState] Error in set(): {exc}")
            return False

    # --------------------------------------------------------
    # GET VALUE (Phase‑5 safe)
    # --------------------------------------------------------
    def get(self, key: str, default=None):
        """
        Deterministic, safe-mode compatible getter.
        """
        try:
            value = self.state.get(key, default)

            if self.logger:
                self.logger.log(f"[RuntimeState] get('{key}') → {value}")

            return value

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeState] Error in get(): {exc}")
            return default

    # --------------------------------------------------------
    # CLEAR STATE
    # --------------------------------------------------------
    def clear(self) -> None:
        """
        Clear all stored state values.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[RuntimeState] SAFE MODE → clear() blocked")
                return

            self.state.clear()

            if self.logger:
                self.logger.log("[RuntimeState] Cleared all state")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeState] clear() error: {exc}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[RuntimeState] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[RuntimeState] SAFE MODE disabled")
