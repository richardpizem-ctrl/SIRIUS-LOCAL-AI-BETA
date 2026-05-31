"""
SIRIUS Runtime 5.1.0
Health Monitor 5.1

Účel:
- zhromažďovať zdravotné signály z Integrity, Workflow, OS a KG
- vyhodnocovať celkový stav systému
- poskytovať RuntimeCore informáciu, či treba spustiť Self‑Repair
"""

from typing import Dict, Any


class HealthMonitor:
    """
    HealthMonitor 5.1 – centrálna diagnostická jednotka Runtime5.

    Očakávané zdroje (dependency injection):
        integrity_source  – poskytuje výsledky Integrity Engine 3.x
        workflow_source   – poskytuje stav workflow
        os_state_source   – poskytuje OS / systémové signály
        kg_state_source   – poskytuje stav Knowledge Graphu
        logger            – Logging5 / RuntimeLogger
    """

    def __init__(
        self,
        integrity_source,
        workflow_source,
        os_state_source,
        kg_state_source,
        logger,
    ):
        self.integrity_source = integrity_source
        self.workflow_source = workflow_source
        self.os_state_source = os_state_source
        self.kg_state_source = kg_state_source
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def check(self) -> Dict[str, Any]:
        """
        Vráti zdravotný stav systému v tvare:

        {
            "status": "OK" | "DEGRADED" | "ERROR" | "UNKNOWN",
            "integrity": {...},
            "workflow": {...},
            "os": {...},
            "kg": {...}
        }
        """
        self.logger.info("HealthMonitor: running health check")

        integrity = self._safe_integrity()
        workflow = self._safe_workflow()
        os_state = self._safe_os()
        kg_state = self._safe_kg()

        status = self._evaluate_status(
            integrity=integrity,
            workflow=workflow,
            os_state=os_state,
            kg_state=kg_state,
        )

        result = {
            "status": status,
            "integrity": integrity,
            "workflow": workflow,
            "os": os_state,
            "kg": kg_state,
        }

        self.logger.info(
            "HealthMonitor: health check completed",
            extra={"status": status},
        )

        return result

    # ---------------------------------------------------------
    # INTERNAL HELPERS – SAFE WRAPPERS
    # ---------------------------------------------------------

    def _safe_integrity(self) -> Dict[str, Any]:
        try:
            return self.integrity_source.get_state() or {}
        except Exception as e:
            self.logger.exception("HealthMonitor: integrity_source failed", extra={"error": str(e)})
            return {"error": "integrity_unavailable", "details": str(e)}

    def _safe_workflow(self) -> Dict[str, Any]:
        try:
            return self.workflow_source.get_last_result() or {}
        except Exception as e:
            self.logger.exception("HealthMonitor: workflow_source failed", extra={"error": str(e)})
            return {"error": "workflow_unavailable", "details": str(e)}

    def _safe_os(self) -> Dict[str, Any]:
        try:
            return self.os_state_source.get_state() or {}
        except Exception as e:
            self.logger.exception("HealthMonitor: os_state_source failed", extra={"error": str(e)})
            return {"error": "os_state_unavailable", "details": str(e)}

    def _safe_kg(self) -> Dict[str, Any]:
        try:
            return self.kg_state_source.get_state() or {}
        except Exception as e:
            self.logger.exception("HealthMonitor: kg_state_source failed", extra={"error": str(e)})
            return {"error": "kg_state_unavailable", "details": str(e)}

    # ---------------------------------------------------------
    # STATUS EVALUATION
    # ---------------------------------------------------------

    def _evaluate_status(
        self,
        integrity: Dict[str, Any],
        workflow: Dict[str, Any],
        os_state: Dict[str, Any],
        kg_state: Dict[str, Any],
    ) -> str:
        """
        Politika hodnotenia:

        ERROR:
            - integrity.ok == False
            - workflow.error
            - os_state.error
            - kg_state.error

        DEGRADED:
            - integrity má issues, ale nie kritické
            - workflow má drobné chyby
            - OS má varovania
            - KG má menšie nekonzistencie

        OK:
            - všetko v norme

        UNKNOWN:
            - ak niektorý zdroj zlyhá
        """

        # UNKNOWN – ak niektorý zdroj je nedostupný
        if "error" in integrity or "error" in workflow or "error" in os_state or "error" in kg_state:
            return "UNKNOWN"

        # ERROR – kritické chyby
        if integrity.get("ok") is False:
            return "ERROR"
        if workflow.get("status") == "ERROR":
            return "ERROR"
        if os_state.get("status") == "ERROR":
            return "ERROR"
        if kg_state.get("status") == "ERROR":
            return "ERROR"

        # DEGRADED – menšie problémy
        if integrity.get("issues"):
            return "DEGRADED"
        if workflow.get("status") == "DEGRADED":
            return "DEGRADED"
        if os_state.get("status") == "DEGRADED":
            return "DEGRADED"
        if kg_state.get("status") == "DEGRADED":
            return "DEGRADED"

        # OK – všetko v poriadku
        return "OK"
