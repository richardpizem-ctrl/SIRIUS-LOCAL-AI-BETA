# Runtime4 IO Channel
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class IOChannel:
    """
    SIRIUS LOCAL AI — IO Channel (v4.5.0 PRO)

    Responsibilities:
        - Deterministic, safe-mode compatible IO operations
        - Sandboxed send/receive interface
        - Phase‑5 ready (isolated, no exception leakage)
        - Central IO abstraction for RuntimeManager45
    """

    def __init__(self, logger=None):
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[IOChannel] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # SEND (Phase‑5 safe)
    # --------------------------------------------------------
    def send(self, data: str) -> bool:
        """
        Deterministic, safe-mode compatible send operation.
        No real IO is performed — sandboxed.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[IOChannel] SAFE MODE → blocked send('{data}')")
                return False

            if self.logger:
                self.logger.log(f"[IOChannel] send(): {data}")

            # Phase‑5: sandboxed — no external IO
            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[IOChannel] send() error: {exc}")
            return False

    # --------------------------------------------------------
    # RECEIVE (Phase‑5 safe)
    # --------------------------------------------------------
    def receive(self) -> str | None:
        """
        Deterministic, safe-mode compatible receive operation.
        Always returns None — sandboxed.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[IOChannel] SAFE MODE → blocked receive()")
                return None

            if self.logger:
                self.logger.log("[IOChannel] receive() called")

            # Phase‑5: sandboxed — no external IO
            return None

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[IOChannel] receive() error: {exc}")
            return None

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[IOChannel] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[IOChannel] SAFE MODE disabled")
