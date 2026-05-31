# Runtime4 Runtime Context
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class RuntimeContext:
    """
    SIRIUS LOCAL AI — Runtime Context (v4.5.0 PRO)

    Responsibilities:
        - Store runtime configuration and dynamic context values
        - Provide deterministic, safe-mode compatible access
        - Phase‑5 ready (context integrity, isolation)
        - Isolated error handling (no exceptions leak)
        - RuntimeManager45-compatible logging
    """

    def __init__(self, config: dict | None = None, logger=None):
        self.config: dict = config or {}
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[RuntimeContext] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # GET VALUE (Phase‑5 safe)
    # --------------------------------------------------------
    def get(self, key: str, default=None):
        """
        Deterministic, safe-mode compatible context lookup.
        No exceptions leak.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[RuntimeContext] SAFE MODE → blocked get('{key}')")
                return default

            value = self.config.get(key, default)

            if self.logger:
                self.logger.log(f"[RuntimeContext] get('{key}') → {value}")

            return value

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeContext] Error in get(): {exc}")
            return default

    # --------------------------------------------------------
    # SET VALUE (Phase‑5 safe)
    # --------------------------------------------------------
    def set(self, key: str, value):
        """
        Deterministic, safe-mode compatible setter.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[RuntimeContext] SAFE MODE → blocked set('{key}')")
                return False

            self.config[key] = value

            if self.logger:
                self.logger.log(f"[RuntimeContext] set('{key}') = {value}")

            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeContext] Error in set(): {exc}")
            return False

    # --------------------------------------------------------
    # MERGE CONFIG (Phase‑5)
    # --------------------------------------------------------
    def merge(self, data: dict):
        """
        Merge new values into context safely.
        """
        if not isinstance(data, dict):
            if self.logger:
                self.logger.log("[RuntimeContext] merge() ignored: invalid type")
            return False

        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[RuntimeContext] SAFE MODE → merge blocked")
                return False

            self.config.update(data)

            if self.logger:
                self.logger.log(f"[RuntimeContext] merge() applied: {data}")

            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeContext] merge() error: {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[RuntimeContext] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[RuntimeContext] SAFE MODE disabled")
