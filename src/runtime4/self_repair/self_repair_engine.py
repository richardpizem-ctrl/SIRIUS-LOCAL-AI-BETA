# File: src/runtime4/self_repair/self_repair_engine.py
"""
Self-Repair Engine
Version: 4.5.0
Component of: Self-Repair Layer (Phase‑5)

Responsible for:
- Monitoring runtime integrity
- Triggering repair actions
- Coordinating recovery protocols
- Dispatching fallback logic
- Logging repair events

Notes:
- Deterministic, offline, isolated
- No dynamic imports, no eval, no reflection
- Fully compatible with Runtime 4.5
"""

from .integrity_scanner import IntegrityScanner
from .recovery_protocol import RecoveryProtocol
from .module_rebuilder import ModuleRebuilder
from .fallback_manager import FallbackManager
from .repair_log import RepairLog


class SelfRepairEngine:
    """
    Main orchestrator for the Self‑Repair Layer.
    Runs continuous integrity checks and triggers deterministic repair actions.
    """

    def __init__(self):
        self.version = "4.5.0"

        self.scanner = IntegrityScanner()
        self.protocol = RecoveryProtocol()
        self.rebuilder = ModuleRebuilder()
        self.fallback = FallbackManager()
        self.log = RepairLog()

    # ---------------------------------------------------------
    # INTEGRITY CHECK
    # ---------------------------------------------------------
    def run_integrity_check(self):
        """Runs a full integrity scan and returns the result."""
        result = self.scanner.scan()
        self.log.record_scan(result)
        return result

    # ---------------------------------------------------------
    # REPAIR PIPELINE
    # ---------------------------------------------------------
    def repair_if_needed(self):
        """
        Executes repair actions if integrity scan detects issues.
        Returns a structured repair report.
        """
        scan = self.run_integrity_check()

        if scan["status"] == "OK":
            return {
                "repaired": False,
                "details": "System stable",
                "version": self.version,
            }

        # Step 1: Apply recovery protocol
        recovery_actions = self.protocol.apply(scan)

        # Step 2: Rebuild modules if required
        rebuild_actions = []
        if scan.get("corrupted_modules"):
            rebuild_actions = self.rebuilder.rebuild(scan["corrupted_modules"])

        # Step 3: Apply fallback logic
        fallback_actions = self.fallback.apply(scan)

        # Step 4: Log everything
        report = {
            "repaired": True,
            "recovery_actions": recovery_actions,
            "rebuild_actions": rebuild_actions,
            "fallback_actions": fallback_actions,
            "version": self.version,
        }

        self.log.record_repair(report)
        return report

    # ---------------------------------------------------------
    # RUNTIME STABILIZATION
    # ---------------------------------------------------------
    def stabilize_runtime(self):
        """Optional: runtime stabilization hook."""
        self.fallback.stabilize()
        self.log.record_event("Runtime stabilized")
