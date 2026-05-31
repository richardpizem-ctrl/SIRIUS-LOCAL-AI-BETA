"""
SIRIUS Runtime 5.1.0
System Agent 5.1

Účel:
- prijíma udalosti z RuntimeCore (workflow, health, repair)
- vyhodnocuje ich pomocou ThreatModel 1.0
- aplikuje IsolationRules 1.0
- zapisuje výsledky do SecurityAudit 1.0
- poskytuje bezpečnostnú vrstvu pre celý Runtime5
"""

from typing import Dict, Any, List


class SystemAgent5:
    """
    SystemAgent5 – bezpečnostný agent novej generácie.

    Očakávané závislosti (dependency injection):
        threat_model     – ThreatModel 1.0 (API: evaluate(event) -> dict)
        isolation_rules  – IsolationRules 1.0 (API: apply(event) -> dict)
        security_audit   – SecurityAudit 1.0 (API: record(entry: dict) -> None)
        logger           – Logging5 / RuntimeLogger
    """

    def __init__(self, threat_model, isolation_rules, security_audit, logger):
        self.threat_model = threat_model
        self.isolation_rules = isolation_rules
        self.security_audit = security_audit
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def process_events(self, events: List[Dict[str, Any]]) -> None:
        """
        Spracuje zoznam udalostí z RuntimeCore.

        Každá udalosť má tvar:
        {
            "type": "workflow" | "health" | "repair",
            "data": {...},
            "triggered": bool (len pre repair)
        }
        """
        self.logger.info(
            "SystemAgent5: processing events",
            extra={"count": len(events)},
        )

        for event in events:
            self._process_single_event(event)

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------

    def _process_single_event(self, event: Dict[str, Any]) -> None:
        event_type = event.get("type", "unknown")

        self.logger.info(
            "SystemAgent5: evaluating event",
            extra={"type": event_type},
        )

        # 1) Threat Model – vyhodnotenie rizika
        threat = self._safe_threat_eval(event)

        # 2) Isolation Rules – aplikácia bezpečnostných pravidiel
        isolation = self._safe_isolation(event, threat)

        # 3) Security Audit – uloženie výsledku
        self._safe_audit(
            {
                "event": event,
                "threat": threat,
                "isolation": isolation,
            }
        )

    # ---------------------------------------------------------
    # SAFE WRAPPERS
    # ---------------------------------------------------------

    def _safe_threat_eval(self, event: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return self.threat_model.evaluate(event) or {}
        except Exception as e:
            self.logger.exception(
                "SystemAgent5: threat_model.evaluate() failed",
                extra={"error": str(e)},
            )
            return {"error": "threat_eval_failed", "details": str(e)}

    def _safe_isolation(self, event: Dict[str, Any], threat: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return self.isolation_rules.apply(event, threat) or {}
        except Exception as e:
            self.logger.exception(
                "SystemAgent5: isolation_rules.apply() failed",
                extra={"error": str(e)},
            )
            return {"error": "isolation_failed", "details": str(e)}

    def _safe_audit(self, entry: Dict[str, Any]) -> None:
        try:
            self.security_audit.record(entry)
        except Exception as e:
            self.logger.exception(
                "SystemAgent5: security_audit.record() failed",
                extra={"error": str(e)},
            )
