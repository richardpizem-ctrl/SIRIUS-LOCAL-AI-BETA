"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Package Initializer

Tento modul poskytuje jednotné API pre celú vrstvu samoopravy:
- Repair Core (hlavná orchestrácia)
- Repair Sandbox (izolácia)
- Repair State Machine (stavový automat)
- Repair Planner (výber opravnej stratégie)
- Repair Context Memory (kontext pre celý cyklus)
- Repair Logs (špecializované logovanie)

Používa sa v:
- Runtime Integrity Engine 1.0
- Workflow Engine 5.1
- System Agent 5.1
- HealthMonitor5
"""

from .repair_core import RepairCore, ErrorState, RepairResult, RepairStage, RepairOutcome
from .repair_sandbox import RepairSandbox
from .repair_state_machine import RepairStateMachine, RepairState, RepairExit
from .repair_planner import RepairPlanner, RepairPlan
from .repair_context import RepairContext, RepairContextMemory
from .repair_logs import RepairLogger

__all__ = [
    # Core
    "RepairCore",
    "ErrorState",
    "RepairResult",
    "RepairStage",
    "RepairOutcome",

    # Sandbox
    "RepairSandbox",

    # State Machine
    "RepairStateMachine",
    "RepairState",
    "RepairExit",

    # Planner
    "RepairPlanner",
    "RepairPlan",

    # Context
    "RepairContext",
    "RepairContextMemory",

    # Logs
    "RepairLogger",
]
