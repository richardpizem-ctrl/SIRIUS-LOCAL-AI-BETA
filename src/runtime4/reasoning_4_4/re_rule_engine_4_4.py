"""
SIRIUS LOCAL AI – Reasoning Rule Engine 4.5.0 (PRO)

Deterministic rule engine pre Reasoning Engine 4.5.

Účel:
- aplikácia jednoduchých IF–THEN pravidiel nad faktami
- žiadne AI, žiadne heuristiky
- 100 % offline, deterministické
- pravidlá sú čisté JSON/dict štruktúry
- kompatibilné so Security Family 4.5 a Self‑Repair 4.5

Pravidlo má formát:
{
    "id": "rule_001",
    "if": [
        {"pack": "history_pack", "key": "napoleon", "equals": "emperor"}
    ],
    "then": {
        "conclusion": "napoleon_is_emperor",
        "value": True
    }
}
"""

from typing import Dict, Any, List, Tuple


class ReasoningRuleEngine45:
    """
    Deterministic rule engine (PRO).
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        # Registered rules (pure JSON/dict)
        self.registered_rules: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            self.initialized = True
            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # RULE VALIDATION
    # ------------------------------------------------------------------
    def _validate_rule(self, rule: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(rule, dict):
            return {"status": "error", "code": "invalid_rule_type", "version": "4.5"}

        if "id" not in rule or not isinstance(rule["id"], str):
            return {"status": "error", "code": "invalid_rule_id", "version": "4.5"}

        if "if" not in rule or not isinstance(rule["if"], list):
            return {"status": "error", "code": "invalid_rule_if", "version": "4.5"}

        if "then" not in rule or not isinstance(rule["then"], dict):
            return {"status": "error", "code": "invalid_rule_then", "version": "4.5"}

        for cond in rule["if"]:
            if not isinstance(cond, dict):
                return {"status": "error", "code": "invalid_condition_type", "version": "4.5"}

            if "pack" not in cond or "key" not in cond or "equals" not in cond:
                return {"status": "error", "code": "invalid_condition_fields", "version": "4.5"}

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # REGISTER RULE
    # ------------------------------------------------------------------
    def register_rule(self, rule: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registruje deterministické pravidlo.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Rule registration disabled in safe-mode.",
                "version": "4.5",
            }

        valid = self._validate_rule(rule)
        if valid.get("status") != "ok":
            return valid

        self.registered_rules.append(rule)
        return {"status": "ok", "rule_id": rule["id"], "version": "4.5"}

    # ------------------------------------------------------------------
    # EXTRACT RULES (from context)
    # ------------------------------------------------------------------
    def extract_rules(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        V tejto verzii vracia len ručne registrované pravidlá.
        """
        return list(self.registered_rules)

    # ------------------------------------------------------------------
    # APPLY RULES
    # ------------------------------------------------------------------
    def apply_rules(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Aplikuje všetky pravidlá nad faktami v kontexte.
        Deterministické, bez AI heuristiky.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Rule engine disabled in safe-mode.",
                "version": "4.5",
            }

        if not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type", "version": "4.5"}

        try:
            facts = context.get("facts", [])
            fact_map: Dict[Tuple[str, str], Any] = {}

            # Build fact map
            for f in facts:
                if isinstance(f, dict) and "pack" in f and "key" in f and "value" in f:
                    fact_map[(f["pack"], f["key"])] = f["value"]

            conclusions = []
            applied_rules = 0

            for rule in self.registered_rules:
                if self._rule_matches(rule, fact_map):
                    applied_rules += 1
                    conclusions.append(rule["then"])

            return {
                "status": "ok",
                "type": "rules",
                "rules_applied": applied_rules,
                "conclusions": conclusions,
                "version": "4.5",
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "apply_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # RULE MATCHING
    # ------------------------------------------------------------------
    def _rule_matches(self, rule: Dict[str, Any], fact_map: Dict[Any, Any]) -> bool:
        """
        Overí, či všetky IF podmienky pravidla sú splnené.
        """

        for cond in rule.get("if", []):
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
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "registered_rules": len(self.registered_rules),
            "version": "4.5",
        }
