# Runtime4 Runtime Core
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class RuntimeCore:
    """
    SIRIUS LOCAL AI — Runtime Core (v4.5.0 PRO)

    Responsibilities:
        - Initialize runtime subsystems (context, state, events, errors)
        - Provide deterministic, safe-mode compatible lifecycle
        - Phase‑5 ready (self-repair hooks, isolation, integrity)
        - Central logging point for RuntimeManager45
        - No external side effects (sandboxed)
    """

    def __init__(self, context, state, events, errors, logger):
        self.context = context
        self.state = state
        self.events = events
        self.errors = errors
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        self.logger.log("[RuntimeCore] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # INITIALIZATION (Phase‑5 safe)
    # --------------------------------------------------------
    def initialize(self) -> bool:
        """
        Initialize runtime subsystems.
        Deterministic, safe-mode compatible, no exceptions leak.
        """
        if self.safe_mode:
            self.logger.log("[RuntimeCore] SAFE MODE → initialization skipped")
            return False

        try:
            self.logger.log("[RuntimeCore] Initialization started")

            # Phase‑5: context integrity check
            if hasattr(self.context, "merge"):
                self.context.merge({"runtime_initialized": True})

            # Phase‑5: state bootstrap
            if hasattr(self.state, "set"):
                self.state.set("initialized", True)

            # Phase‑5: event log
            if hasattr(self.events, "push"):
                self.events.push("runtime_initialized")

            self.logger.log("[RuntimeCore] Initialization OK")
            return True

        except Exception as exc:
            self.degraded_mode = True
            self.logger.log(f"[RuntimeCore] Initialization error: {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.logger.log("[RuntimeCore] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.logger.log("[RuntimeCore] SAFE MODE disabled")
