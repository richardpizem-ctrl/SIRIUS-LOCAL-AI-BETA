# runtime5_test.py
# SIRIUS LOCAL AI – Runtime 5.1 Test Harness
# Deterministic, offline-only, Self‑Repair Layer 1.0 ready

from __future__ import annotations

from runtime5.runtime_core import RuntimeCore
from runtime5.runtime_config import RuntimeConfig
from runtime5.health_monitor import HealthMonitor
from runtime5.workflow_engine5 import WorkflowEngine5
from runtime5.system_agent5 import SystemAgent5
from runtime5.repair_entrypoint import RepairEntrypoint

# ------------------------------------------------------------
# Dummy providers for isolated testing (no OS access required)
# ------------------------------------------------------------

class DummyLogger:
    def info(self, msg, extra=None): print("[INFO]", msg, extra or "")
    def warning(self, msg, extra=None): print("[WARN]", msg, extra or "")
    def error(self, msg, extra=None): print("[ERROR]", msg, extra or "")
    def exception(self, msg, extra=None): print("[EXC]", msg, extra or "")

class DummyIntegritySource:
    def get_state(self): return {"ok": True}

class DummyWorkflowSource:
    def get_pending(self):
        return [
            {"name": "test_step_1"},
            {"name": "test_step_2"},
        ]
    def get_last_result(self):
        return {"status": "OK"}

class DummyWorkflowExecutor:
    def execute(self, task):
        return {"executed": task["name"]}

class DummyOSStateSource:
    def get_state(self): return {"status": "OK"}

class DummyKGStateSource:
    def get_state(self): return {"status": "OK"}

class DummyThreatModel:
    def evaluate(self, event): return {"risk": "none"}

class DummyIsolationRules:
    def apply(self, event, threat): return {"isolation": "none"}

class DummySecurityAudit:
    def record(self, entry): print("[AUDIT]", entry)

class DummyRepairCore:
    def __init__(self, logger): self.logger = logger
    def run_repair_cycle(self):
        return type("RepairResult", (), {
            "ok": True,
            "stages": ["check", "validate", "complete"],
            "details": {"final_state": "OK"}
        })()

# ------------------------------------------------------------
# RUNTIME 5.1 TEST
# ------------------------------------------------------------

if __name__ == "__main__":
    logger = DummyLogger()
    config = RuntimeConfig()

    health_monitor = HealthMonitor(
        DummyIntegritySource(),
        DummyWorkflowSource(),
        DummyOSStateSource(),
        DummyKGStateSource(),
        logger,
    )

    workflow_engine = WorkflowEngine5(
        DummyWorkflowSource(),
        DummyWorkflowExecutor(),
        logger,
    )

    system_agent = SystemAgent5(
        DummyThreatModel(),
        DummyIsolationRules(),
        DummySecurityAudit(),
        logger,
    )

    repair_core = DummyRepairCore(logger)
    repair_entry = RepairEntrypoint(repair_core, logger)

    runtime = RuntimeCore(
        workflow_engine,
        repair_core,
        system_agent,
        health_monitor,
        logger,
        config,
    )

    print("\n=== RUNNING RUNTIME 5.1 CYCLE ===")
    result = runtime.run_cycle()

    print("\n=== WORKFLOW OUTPUT ===")
    print(result.details["workflow"])

    print("\n=== HEALTH OUTPUT ===")
    print(result.details["health"])

    print("\n=== REPAIR OUTPUT ===")
    print(result.details["repair"])

    print("\n=== FINAL STATUS ===")
    print("OK:", result.ok)
