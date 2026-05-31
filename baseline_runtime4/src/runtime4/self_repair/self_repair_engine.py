# Runtime4 Self‑Repair Engine
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations
from typing import Protocol


class IntegrityScanner(Protocol):
    def scan(self) -> bool: ...


class RecoveryProtocol(Protocol):
    def execute(self) -> bool: ...


class ModuleRebuilder(Protocol):
    def rebuild(self) -> bool: ...


class FallbackManager(Protocol):
    def activate(self) -> None: ...


class RepairLogger(Protocol):
    def log(self, message: str) -> None: ...
    def warn(self, message: str) -> None: ...
    def error(self, message: str) -> None: ...


class SelfRepairEngine:
    """
    SIRIUS LOCAL AI — Self‑Repair Engine (v4.5.0 PRO)

    Responsibilities:
        - Orchestrate the full self‑repair cycle
        - Deterministic, safe-mode compatible execution
        - Phase‑5 ready (isolation, no exception leakage)
        - Works with IntegrityScanner, RecoveryProtocol, ModuleRebuilder, FallbackManager
    """

    def __init__(
        self,
        scanner: IntegrityScanner,
        recovery: RecoveryProtocol,
        rebuilder: ModuleRebuilder,
        fallback: FallbackManager,
        logger: RepairLogger,
    ) -> None:

        self.scanner = scanner
        self.recovery = recovery
        self.rebuilder = rebuilder
        self.fallback = fallback
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.last_cycle_ok: bool = True

        self.logger.log("[SelfRepairEngine] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # MAIN REPAIR CYCLE
    # --------------------------------------------------------
    def run_cycle(self) -> bool:
        """
        Executes a single self‑repair cycle.
        Returns True if system is stable after the cycle,
        False if degraded mode is active.
        """
        try:
            if self.safe_mode:
                self.logger.warn("[SelfRepairEngine] SAFE MODE → run_cycle() blocked")
                return True

            self.logger.log("[SelfRepair] Starting integrity scan.")
            integrity_ok = self.scanner.scan()

            if integrity_ok:
                self.logger.log("[SelfRepair] Integrity OK — no action required.")
                self.last_cycle_ok = True
                return True

            # --------------------------------------------------------
            # RECOVERY PROTOCOL
            # --------------------------------------------------------
            self.logger.warn("[SelfRepair] Integrity FAILED — starting recovery protocol.")
            recovered = self.recovery.execute()

            if recovered:
                self.logger.log("[SelfRepair] Recovery protocol succeeded.")
                self.last_cycle_ok = True
                return True

            # --------------------------------------------------------
            # MODULE REBUILD
            # --------------------------------------------------------
            self.logger.warn("[SelfRepair] Recovery FAILED — attempting module rebuild.")
            rebuilt = self.rebuilder.rebuild()

            if rebuilt:
                self.logger.log("[SelfRepair] Module rebuild succeeded.")
                self.last_cycle_ok = True
                return True

            # --------------------------------------------------------
            # FALLBACK MODE
            # --------------------------------------------------------
            self.logger.error(
                "[SelfRepair] Rebuild FAILED — activating fallback mode (degraded but safe)."
            )
            self.fallback.activate()

            self.last_cycle_ok = False
            self.degraded_mode = True
            return False

        except Exception as exc:
            self.logger.error(f"[SelfRepairEngine] run_cycle() internal error: {exc}")
            self.degraded_mode = True
            self.last_cycle_ok = False
            self.fallback.activate()
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.logger.warn("[SelfRepairEngine] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.logger.log("[SelfRepairEngine] SAFE MODE disabled")
