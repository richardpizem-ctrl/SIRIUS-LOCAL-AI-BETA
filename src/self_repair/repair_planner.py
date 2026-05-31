"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair Planner 1.0

Účel:
- rozhodnúť, aký typ opravy použiť podľa ErrorState
- vybrať správny repair handler (KG, workflow, runtime, dependency…)
- pripraviť RepairPlan pre RepairCore
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class RepairPlan:
    """
    Výstup plánovača:
    - handler: funkcia alebo objekt, ktorý vykoná opravu
    - context: doplnkové informácie pre opravu
    """
    handler: Any
    context: Dict[str, Any]


class RepairPlanner:
    """
    RepairPlanner analyzuje ErrorState a rozhoduje:
    - čo sa pokazilo
    - aký typ opravy je potrebný
    - ktorý opravný modul použiť
    """

    def __init__(self, handlers: Dict[str, Any], logger):
        """
        handlers – dict:
            {
                "kg": KGRepairHandler,
                "workflow": WorkflowRepairHandler,
                "runtime": RuntimeRepairHandler,
                "dependencies": DependencyRepairHandler,
                ...
            }

        logger – Logging5 / RepairLogs
        """
        self.handlers = handlers
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def plan(self, error_state) -> Optional[RepairPlan]:
        """
        Hlavná funkcia:
        Vstup: ErrorState
        Výstup: RepairPlan alebo None
        """
        module = error_state.module
        error_code = error_state.error_code

        self.logger.info(
            "RepairPlanner: analyzing error",
            extra={"module": module, "error_code": error_code}
        )

        # 1) KG ERRORS
        if error_code.startswith("KG_") or "knowledge" in module.lower():
            return self._plan_kg_repair(error_state)

        # 2) WORKFLOW ERRORS
        if "workflow" in module.lower():
            return self._plan_workflow_repair(error_state)

        # 3) DEPENDENCY ERRORS
        if error_code in {"MISSING_DEPENDENCY", "BROKEN_IMPORT", "INVALID_GRAPH"}:
            return self._plan_dependency_repair(error_state)

        # 4) RUNTIME ERRORS
        if "runtime" in module.lower():
            return self._plan_runtime_repair(error_state)

        # 5) DEFAULT FALLBACK
        return self._plan_generic_repair(error_state)

    # ---------------------------------------------------------
    # INTERNAL PLANNERS
    # ---------------------------------------------------------

    def _plan_kg_repair(self, error_state):
        handler = self.handlers.get("kg")
        if not handler:
            return None

        self.logger.info("RepairPlanner: selected KG repair handler")

        return RepairPlan(
            handler=handler,
            context={
                "entity": error_state.context.get("entity"),
                "relation": error_state.context.get("relation"),
                "severity": error_state.severity,
            }
        )

    def _plan_workflow_repair(self, error_state):
        handler = self.handlers.get("workflow")
        if not handler:
            return None

        self.logger.info("RepairPlanner: selected Workflow repair handler")

        return RepairPlan(
            handler=handler,
            context={
                "workflow_id": error_state.context.get("workflow_id"),
                "step": error_state.context.get("step"),
                "severity": error_state.severity,
            }
        )

    def _plan_dependency_repair(self, error_state):
        handler = self.handlers.get("dependencies")
        if not handler:
            return None

        self.logger.info("RepairPlanner: selected Dependency repair handler")

        return RepairPlan(
            handler=handler,
            context={
                "missing": error_state.context.get("missing"),
                "module": error_state.module,
                "severity": error_state.severity,
            }
        )

    def _plan_runtime_repair(self, error_state):
        handler = self.handlers.get("runtime")
        if not handler:
            return None

        self.logger.info("RepairPlanner: selected Runtime repair handler")

        return RepairPlan(
            handler=handler,
            context={
                "module": error_state.module,
                "error_code": error_state.error_code,
                "severity": error_state.severity,
            }
        )

    def _plan_generic_repair(self, error_state):
        handler = self.handlers.get("generic")
        if not handler:
            self.logger.warning("RepairPlanner: no handler for generic repair")
            return None

        self.logger.info("RepairPlanner: selected Generic repair handler")

        return RepairPlan(
            handler=handler,
            context={
                "module": error_state.module,
                "error_code": error_state.error_code,
                "severity": error_state.severity,
            }
        )
