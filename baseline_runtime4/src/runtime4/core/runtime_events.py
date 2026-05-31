# Runtime4 Runtime Events
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class RuntimeEvents:
    """
    SIRIUS LOCAL AI — Runtime Events (v4.5.0 PRO)

    Responsibilities:
        - Deterministic event emission
        - Safe-mode compatible event logging
        - Phase‑5 ready (isolated, no exception leakage)
        - Central event bus for RuntimeManager45
        - Compatible with Self‑Repair Layer 4.5
    """

    def __init__(self, logger=None):
        self.logger = logger
        self.events: list[dict] = []
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[RuntimeEvents] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # EMIT EVENT (Phase‑5 safe)
    # --------------------------------------------------------
    def emit(self, event_name: str, payload: dict | None = None) -> None:
        """
        Emit an event safely.
        Deterministic, safe-mode compatible, no exceptions leak.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[RuntimeEvents] SAFE MODE → blocked emit('{event_name}')")
                return

            event = {
                "name": event_name,
                "payload": payload or {},
            }

            self.events.append(event)

            if self.logger:
                self.logger.log(f"[RuntimeEvents] Event emitted: {event_name}")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeEvents] emit() error: {exc}")

    # --------------------------------------------------------
    # PUSH EVENT (alias)
    # --------------------------------------------------------
    def push(self, event_name: str, payload: dict | None = None) -> None:
        """Alias for emit(), for compatibility with older modules."""
        self.emit(event_name, payload)

    # --------------------------------------------------------
    # GET ALL EVENTS
    # --------------------------------------------------------
    def get_all(self) -> list[dict]:
        """
        Return all stored events safely.
        """
        try:
            if self.logger:
                self.logger.log("[RuntimeEvents] get_all() called")
            return list(self.events)

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeEvents] get_all() error: {exc}")
            return []

    # --------------------------------------------------------
    # CLEAR EVENTS
    # --------------------------------------------------------
    def clear(self) -> None:
        """
        Clear all stored events.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[RuntimeEvents] SAFE MODE → clear() blocked")
                return

            self.events.clear()

            if self.logger:
                self.logger.log("[RuntimeEvents] Cleared all events")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[RuntimeEvents] clear() error: {exc}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[RuntimeEvents] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[RuntimeEvents] SAFE MODE disabled")
