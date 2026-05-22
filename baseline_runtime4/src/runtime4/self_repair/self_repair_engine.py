# File: src/runtime4/self_repair/self_repair_engine.py
# Version: 4.5.0
# Runtime Self‑Repair Engine (active implementation)

from typing import Protocol


class IntegrityScanner(Protocol):
    def scan(self) -> bool:
        ...


class RecoveryProtocol(Protocol):
    def execute(self) -> bool:
        ...


class ModuleRebuilder(Protocol):
    def rebuild(self) -> bool:
        ...


class FallbackManager(Protocol):
    def activate(self) -> None:
        ...


class RepairLogger(Protocol):
    def log(self, message: str) -> None:
        ...


class SelfRepairEngine:
    """
    Orchestrates the full self‑repair cycle:
    1. Integrity scan
    2. Recovery protocol
    3. Module rebuild
    4. Fallback activation (degraded mode) if all else fails
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

    def run_cycle(self) -> bool:
        """
        Executes a single self‑repair cycle.
        Returns True if system is stable after the cycle, False if degraded mode is active.
        """
        self.logger.log("[SelfRepair] Starting integrity scan.")
        integrity_ok = self.scanner.scan()

        if integrity_ok:
            self.logger.log("[SelfRepair] Integrity OK — no action required.")
            return True

        self.logger.log("[SelfRepair] Integrity check FAILED — starting recovery protocol.")
        recovered = self.recovery.execute()

        if recovered:
            self.logger.log("[SelfRepair] Recovery protocol succeeded.")
            return True

        self.logger.log("[SelfRepair] Recovery FAILED — attempting module rebuild.")
        rebuilt = self.rebuilder.rebuild()

        if rebuilt:
            self.logger.log("[SelfRepair] Module rebuild succeeded.")
            return True

        self.logger.log(
            "[SelfRepair] Rebuild FAILED — activating fallback mode (degraded but safe operation)."
        )
        self.fallback.activate()
        return False

