"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair Context 1.0

Účel:
- zozbierať všetky relevantné signály pre Self‑Repair Layer
- vytvoriť jednotný, deterministický repair context (dict)
- slúžiť ako context_provider pre MultiStageRepair / RepairCore
"""

from typing import Dict, Any


class RepairContext:
    """
    RepairContext – zber a normalizácia signálov pre Self‑Repair.

    Očakávané vstupné zdroje (dependency injection):
        integrity_source  – poskytuje výsledky Integrity / KG validatora
        workflow_source   – poskytuje informácie o zlyhaniach workflow
        os_state_source   – poskytuje informácie o OS / prostredí
        kg_state_source   – poskytuje informácie o stave KG

    Každý zdroj by mal mať jednoduché API typu:
        .get_state() -> dict
    alebo
        .get_last_result() -> dict
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

    def build_context(self) -> Dict[str, Any]:
        """
        Vytvorí repair context pre plánovanie a orchestráciu opráv.

        Výstupny formát:
        {
            "integrity": {...},
            "workflow": {...},
            "os": {...},
            "kg": {...},
        }
        """
        self.logger.info("RepairContext: building repair context")

        integrity_ctx = self._safe_get_integrity()
        workflow_ctx = self._safe_get_workflow()
        os_ctx = self._safe_get_os_state()
        kg_ctx = self._safe_get_kg_state()

        context: Dict[str, Any] = {
            "integrity": integrity_ctx,
            "workflow": workflow_ctx,
            "os": os_ctx,
            "kg": kg_ctx,
        }

        self.logger.info(
            "RepairContext: context built",
            extra={
                "integrity_keys": list(integrity_ctx.keys()),
                "workflow_keys": list(workflow_ctx.keys()),
                "os_keys": list(os_ctx.keys()),
                "kg_keys": list(kg_ctx.keys()),
            },
        )

        return context

    # ---------------------------------------------------------
    # INTERNAL HELPERS – SAFE WRAPPERS
    # ---------------------------------------------------------

    def _safe_get_integrity(self) -> Dict[str, Any]:
        try:
            result = self.integrity_source.get_state()
            return result or {}
        except Exception as e:
            self.logger.exception(
                "RepairContext: failed to get integrity state",
                extra={"error": str(e)},
            )
            return {"error": "integrity_unavailable", "details": str(e)}

    def _safe_get_workflow(self) -> Dict[str, Any]:
        try:
            result = self.workflow_source.get_last_result()
            return result or {}
        except Exception as e:
            self.logger.exception(
                "RepairContext: failed to get workflow state",
                extra={"error": str(e)},
            )
            return {"error": "workflow_unavailable", "details": str(e)}

    def _safe_get_os_state(self) -> Dict[str, Any]:
        try:
            result = self.os_state_source.get_state()
            return result or {}
        except Exception as e:
            self.logger.exception(
                "RepairContext: failed to get OS state",
                extra={"error": str(e)},
            )
            return {"error": "os_state_unavailable", "details": str(e)}

    def _safe_get_kg_state(self) -> Dict[str, Any]:
        try:
            result = self.kg_state_source.get_state()
            return result or {}
        except Exception as e:
            self.logger.exception(
                "RepairContext: failed to get KG state",
                extra={"error": str(e)},
            )
            return {"error": "kg_state_unavailable", "details": str(e)}
