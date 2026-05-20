# reasoning_4_4/re_rule_engine_4_4.py
"""
SIRIUS LOCAL AI – Reasoning Rule Engine 4.4.0

Deterministic rule engine pre Reasoning Engine 4.4.

Účel:
- aplikácia jednoduchých IF–THEN pravidiel nad faktami
- žiadne AI, žiadne heuristiky
- 100 % offline, deterministické
- pravidlá sú čisté JSON/dict štruktúry

Pravidlo má formát:
{
    "id": "rule_001",
    "if": [
        {"pack": "history_pack", "key": "napoleon", "equals": "emperor"}
    ],
    "then": {
        "conclusion": "napoleon_is_emperor",
        "value": True
    },
    "depends_on": ["napoleon"]
}
"""

from typing import Dict, Any, List


class ReasoningRuleEngine44:
    """
    Deterministic rule engine.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

        # Tu môžeš neskôr pridať dynamické pravidlá
        self.registered_rules: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # REGISTER RULE
    # ------------------------------------------------------------------
    def register_rule(self, rule: Dict[str, Any]) -> None:
        self.registered_rules.append(rule)

    # ------------------------------------------------------------------
    # EXTRACT RULES (from context)
    # ------------------------------------------------------------------
    def extract_rules(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        V tejto verzii vracia len ručne registrované pravidlá.
        Neskôr môžeš pridať pack-based rules.
        """
        return list(self.registered_rules)

    # ------------------------------------------------------------------
    # APPLY RULES
    # ------------------------------------------------------------------
    def apply_rules(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Aplikuje všetky pravidlá nad faktami v kontexte.
        """

        try:
            facts = context.get("facts", [])
            fact_map = {(f["pack"], f["key"]): f["value"] for f in facts}

            conclusions = []

            for rule in self.registered_rules:
                if self._rule_matches(rule, fact_map):
                    conclusions.append(rule["then"])

            return {
                "status": "ok",
                "conclusions": conclusions,
                "rules_applied": len(conclusions),
            }

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # RULE MATCHING
    # ------------------------------------------------------------------
    def _rule_matches(self, rule: Dict[str, Any], fact_map: Dict[Any, Any]) -> bool:
        """
        Overí, či všetky IF podmienky pravidla sú splnené.
        """

        conditions = rule.get("if", [])
        for cond in conditions:
            pack = cond.get("pack")
            key = cond.get("key")
            expected = cond.get("equals")

            if (pack, key) not in fact_map:
                return False

            if fact_map[(pack, key)] != expected:
                return False

        return True

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "registered_rules": len(self.registered_rules),
        }
