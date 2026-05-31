# runtime5_cli.py
# SIRIUS LOCAL AI – Runtime 5.1 Command Line Interface
# Deterministic, safe-mode compatible, Self‑Repair Layer 1.0 ready

from __future__ import annotations

import sys

from runtime5.runtime_core import RuntimeCore
from runtime5.runtime_config import RuntimeConfig
from runtime5.health_monitor import HealthMonitor
from runtime5.workflow_engine5 import WorkflowEngine5
from runtime5.system_agent5 import SystemAgent5
from runtime5.repair_entrypoint import RepairEntrypoint

# Your real implementations must be injected here:
# These are placeholders for your actual system providers.
from runtime5_test import (
    DummyIntegritySource,
    DummyWorkflowSource,
    DummyOSStateSource,
    DummyKGStateSource,
    DummyWorkflowExecutor,
    DummyThreatModel,
    DummyIsolationRules,
    DummySecurityAudit,
    DummyRepairCore,
    DummyLogger,
)


class Runtime5CLI:
    """
    SIRIUS LOCAL AI — Command Line Interface (Runtime 5.1)

    Features:
        - Natural language input (delegated to Workflow Engine)
        - Direct AI task execution (delegated to RuntimeCore)
        - Health monitoring
        - Self‑Repair triggering
        - Safe-mode + degraded-mode support
        - Deterministic, offline-only behavior
    """

    def __init__(self):
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        # ----------------------------------------------------
        # Dependency Injection (Runtime 5.1)
        # ----------------------------------------------------
        self.logger = DummyLogger()
        self.config = RuntimeConfig()

        self.health_monitor = HealthMonitor(
            DummyIntegritySource(),
            DummyWorkflowSource(),
            DummyOSStateSource(),
            DummyKGStateSource(),
            self.logger,
        )

        self.workflow_engine = WorkflowEngine5(
            DummyWorkflowSource(),
            DummyWorkflowExecutor(),
            self.logger,
        )

        self.system_agent = SystemAgent5(
            DummyThreatModel(),
            DummyIsolationRules(),
            DummySecurityAudit(),
            self.logger,
        )

        self.repair_core = DummyRepairCore(self.logger)
        self.repair_entry = RepairEntrypoint(self.repair_core, self.logger)

        self.runtime = RuntimeCore(
            self.workflow_engine,
            self.repair_core,
            self.system_agent,
            self.health_monitor,
            self.logger,
            self.config,
        )

        self.logger.info("Runtime5 CLI initialized (v5.1.0)")

    # --------------------------------------------------------
    # MAIN ENTRY
    # --------------------------------------------------------
    def run(self, argv):
        if len(argv) < 2:
            self._print_help()
            return

        command = argv[1].lower()

        if self.safe_mode:
            print("Runtime5 CLI is in SAFE MODE. Only 'health' and 'help' are available.")
            if command not in {"health", "help"}:
                return

        try:
            # ----------------------------------------------------
            # RUN RUNTIME CYCLE
            # ----------------------------------------------------
            if command == "cycle":
                result = self.runtime.run_cycle()
                self._print_result(result.details)
                return

            # ----------------------------------------------------
            # HEALTH CHECK
            # ----------------------------------------------------
            if command == "health":
                result = self.health_monitor.check()
                self._print_result(result)
                return

            # ----------------------------------------------------
            # SELF‑REPAIR
            # ----------------------------------------------------
            if command == "repair":
                result = self.repair_entry.run()
                self._print_result(result)
                return

            # ----------------------------------------------------
            # SAFE MODE
            # ----------------------------------------------------
            if command == "safemode":
                if len(argv) < 3:
                    print("Usage: runtime5 safemode on|off")
                    return

                mode = argv[2].lower()
                if mode == "on":
                    self.safe_mode = True
                    print("SAFE MODE enabled.")
                elif mode == "off":
                    self.safe_mode = False
                    print("SAFE MODE disabled.")
                else:
                    print("Usage: runtime5 safemode on|off")
                return

            # ----------------------------------------------------
            # HELP
            # ----------------------------------------------------
            if command == "help":
                self._print_help()
                return

            print(f"Unknown command: {command}")
            self._print_help()

        except Exception as e:
            self.degraded_mode = True
            self.logger.error(f"Runtime5 CLI error: {e}")
            print("An internal error occurred. Check logs for details.")

    # --------------------------------------------------------
    # HELPERS
    # --------------------------------------------------------
    def _print_result(self, result):
        print("--------------------------------------------------")
        if isinstance(result, dict):
            for k, v in result.items():
                print(f"{k}: {v}")
        else:
            print(result)
        print("--------------------------------------------------")

    def _print_help(self):
        print("""
Runtime5 CLI – available commands (v5.1.0):

  runtime5 cycle
      - runs one full Runtime5 cycle (workflow → health → repair → agent)

  runtime5 health
      - runs HealthMonitor 5.1

  runtime5 repair
      - triggers Self‑Repair Layer 1.0

  runtime5 safemode on|off
      - enables or disables SAFE MODE

  runtime5 help
      - shows this help
""")


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    cli = Runtime5CLI()
    cli.run(sys.argv)
