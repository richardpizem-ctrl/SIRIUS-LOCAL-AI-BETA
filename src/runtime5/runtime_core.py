"""
SIRIUS Runtime 5.1.0
Runtime Core 5.1 – hlavný orchestrátor

Účel:
- koordinovať beh Workflow Engine 5.1, Self‑Repair Layer 1.0, System Agent 5.1 a Health Monitor 5.1
- poskytovať jednotné API pre spúšťanie runtime cyklov
- zabezpečiť deterministický, auditovateľný priebeh
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class RuntimeCycleResult:
    ok: bool
    repair_triggered: bool
    repair_ok: Optional[bool]
    details: Dict[str, Any]


class RuntimeCore:
    """
    RuntimeCore 5.1 – mozog Runtime5.

    Očakávané závislosti (dependency injection):
        workflow_engine   – WorkflowEngine5 (API: run_pending() -> dict)
        repair_core       – RepairCore (API: run_repair_cycle() -> RepairCycleResult)
        system_agent      – SystemAgent5 (API: process_events(events: list[dict]) -> None)
        health_monitor    – HealthMonitor5 (API: check() -> dict)
        logger            – Logging5 / RuntimeLogger
        config            – RuntimeConfig (dict-like, voliteľné)
    """

    def __init__(
        self,
        workflow_engine,
        repair_core,
        system_agent,
        health_monitor,
        logger,
        config: Optional[Dict[str, Any]] = None,
    ):
        self.workflow_engine = workflow_engine
        self.repair_core = repair_core
        self.system_agent = system_agent
        self.health_monitor = health_monitor
        self.logger = logger
        self.config = config or {}

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def run_cycle(self) -> RuntimeCycleResult:
        """
        Spustí jeden runtime cyklus:

        1) spustí workflow engine (run_pending)
        2) spustí health check
        3) podľa výsledku health checku rozhodne, či spustiť Self‑Repair
        4) odošle udalosti System Agentovi
        """
        self.logger.info("RuntimeCore: starting runtime cycle")

        # 1) Workflow Engine – spracovanie čakajúcich úloh
        wf_result = self._safe_run_workflow()

        # 2) Health Monitor – kontrola stavu
        health = self._safe_health_check()

        repair_triggered = False
        repair_ok: Optional[bool] = None
        repair_details: Dict[str, Any] = {}

        # 3) Rozhodnutie: spustiť Self‑Repair?
        if self._should_trigger_repair(health):
            repair_triggered = True
            rc = self._safe_run_repair()
            repair_ok = rc.ok
            repair_details = {
                "final_state": rc.details.get("final_state"),
                "stages": rc.stages,
            }

        # 4) System Agent – spracovanie udalostí
        self._safe_system_agent(
            events=[
                {"type": "workflow", "data": wf_result},
                {"type": "health", "data": health},
                {"type": "repair", "data": repair_details, "triggered": repair_triggered},
            ]
        )

        final_ok = (health.get("status") in ("OK", "DEGRADED")) and (repair_ok is not False)

        self.logger.info(
            "RuntimeCore: runtime cycle finished",
            extra={
                "ok": final_ok,
                "repair_triggered": repair_triggered,
                "repair_ok": repair_ok,
                "health_status": health.get("status"),
            },
        )

        return RuntimeCycleResult(
            ok=final_ok,
            repair_triggered=repair_triggered,
            repair_ok=repair_ok,
            details={
                "workflow": wf_result,
                "health": health,
                "repair": repair_details,
            },
        )

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------

    def _safe_run_workflow(self) -> Dict[str, Any]:
        try:
            self.logger.info("RuntimeCore: running workflow_engine.run_pending()")
            result = self.workflow_engine.run_pending()
            return result or {}
        except Exception as e:
            self.logger.exception(
                "RuntimeCore: workflow_engine.run_pending() failed",
                extra={"error": str(e)},
            )
            return {"error": "workflow_failed", "details": str(e)}

    def _safe_health_check(self) -> Dict[str, Any]:
        try:
            self.logger.info("RuntimeCore: running health_monitor.check()")
            result = self.health_monitor.check()
            return result or {}
        except Exception as e:
            self.logger.exception(
                "RuntimeCore: health_monitor.check() failed",
                extra={"error": str(e)},
            )
            return {"status": "UNKNOWN", "error": "health_check_failed", "details": str(e)}

    def _safe_run_repair(self):
        try:
            self.logger.info("RuntimeCore: triggering Self‑Repair cycle")
            return self.repair_core.run_repair_cycle()
        except Exception as e:
            self.logger.exception(
                "RuntimeCore: repair_core.run_repair_cycle() failed",
                extra={"error": str(e)},
            )
            # fallback prázdny výsledok
            from self_repair.orchestration.repair_core import RepairCycleResult  # type: ignore

            return RepairCycleResult(
                ok=False,
                stages=[],
                details={"error": "repair_core_failed", "details": str(e)},
            )

    def _safe_system_agent(self, events: list[Dict[str, Any]]) -> None:
        try:
            self.logger.info(
                "RuntimeCore: sending events to SystemAgent5",
                extra={"events_count": len(events)},
            )
            self.system_agent.process_events(events)
        except Exception as e:
            self.logger.exception(
                "RuntimeCore: system_agent.process_events() failed",
                extra={"error": str(e)},
            )

    def _should_trigger_repair(self, health: Dict[str, Any]) -> bool:
        """
        Jednoduchá politika:
        - ak status == "ERROR" → spustiť Self‑Repair
        - ak status == "DEGRADED" → spustiť Self‑Repair, ak to povoľuje config
        """
        status = health.get("status")
        if status == "ERROR":
            return True
        if status == "DEGRADED":
            return self.config.get("repair_on_degraded", True)
        return False
