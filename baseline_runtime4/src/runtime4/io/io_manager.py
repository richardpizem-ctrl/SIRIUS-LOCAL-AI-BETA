# Runtime4 IO Manager
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class IOManager:
    """
    SIRIUS LOCAL AI — IO Manager (v4.5.0 PRO)

    Responsibilities:
        - High-level IO wrapper around IOChannel
        - Deterministic, safe-mode compatible IO operations
        - Phase‑5 ready (sandboxed, isolated, no exception leakage)
        - Central IO abstraction for RuntimeManager45
    """

    def __init__(self, channel, logger=None):
        self.channel = channel
        self.logger = logger
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[IOManager] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # WRITE (Phase‑5 safe)
    # --------------------------------------------------------
    def write(self, data: str) -> bool:
        """
        Deterministic, safe-mode compatible write operation.
        Delegates to IOChannel.send().
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[IOManager] SAFE MODE → blocked write('{data}')")
                return False

            if self.logger:
                self.logger.log(f"[IOManager] write(): {data}")

            return self.channel.send(data)

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[IOManager] write() error: {exc}")
            return False

    # --------------------------------------------------------
    # READ (Phase‑5 safe)
    # --------------------------------------------------------
    def read(self) -> str | None:
        """
        Deterministic, safe-mode compatible read operation.
        Delegates to IOChannel.receive().
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[IOManager] SAFE MODE → blocked read()")
                return None

            if self.logger:
                self.logger.log("[IOManager] read() called")

            return self.channel.receive()

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[IOManager] read() error: {exc}")
            return None

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[IOManager] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[IOManager] SAFE MODE disabled")
