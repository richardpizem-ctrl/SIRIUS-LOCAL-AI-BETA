# Runtime4 IO Status
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class IOStatus:
    """
    SIRIUS LOCAL AI — IO Status (v4.5.0 PRO)

    Responsibilities:
        - Track last sent and last received IO data
        - Deterministic, safe-mode compatible state tracking
        - Phase‑5 ready (isolated, no exception leakage)
        - Used by IOManager and RuntimeManager45
    """

    def __init__(self, last_sent: str | None = None, last_received: str | None = None, logger=None):
        self.last_sent = last_sent
        self.last_received = last_received
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[IOStatus] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # UPDATE SENT
    # --------------------------------------------------------
    def update_sent(self, data: str) -> None:
        """Record last sent data safely."""
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[IOStatus] SAFE MODE → blocked update_sent('{data}')")
                return

            self.last_sent = data

            if self.logger:
                self.logger.log(f"[IOStatus] last_sent updated → {data}")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[IOStatus] update_sent() error: {exc}")

    # --------------------------------------------------------
    # UPDATE RECEIVED
    # --------------------------------------------------------
    def update_received(self, data: str) -> None:
        """Record last received data safely."""
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[IOStatus] SAFE MODE → blocked update_received('{data}')")
                return

            self.last_received = data

            if self.logger:
                self.logger.log(f"[IOStatus] last_received updated → {data}")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[IOStatus] update_received() error: {exc}")

    # --------------------------------------------------------
    # EXPORT STATUS
    # --------------------------------------------------------
    def to_dict(self) -> dict:
        """Return IO status safely."""
        try:
            status = {
                "last_sent": self.last_sent,
                "last_received": self.last_received,
            }

            if self.logger:
                self.logger.log(f"[IOStatus] to_dict() → {status}")

            return status

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[IOStatus] to_dict() error: {exc}")
            return {
                "last_sent": None,
                "last_received": None,
            }

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[IOStatus] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[IOStatus] SAFE MODE disabled")
