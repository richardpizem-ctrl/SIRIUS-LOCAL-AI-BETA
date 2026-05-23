"""
SIRIUS LOCAL AI – Reasoning Context Memory 4.5.0 (PRO)

Deterministic context memory for Reasoning Engine 4.5.

Účel:
- drží krátkodobú reasoning pamäť pre jeden dotaz
- uchováva fakty, packy, pravidlá, symbolické výrazy, intermediate výsledky
- poskytuje bezpečné API pre zápis/čítanie
- 100 % offline, deterministické, bez AI heuristiky
- žiadne dynamické importy, eval, exec
- kompatibilné so Security Family 4.5 a Self‑Repair 4.5
"""

from typing import Dict, Any, List


class ReasoningContextMemory45:
    """
    Krátkodobá reasoning pamäť pre jeden dotaz (PRO).
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        # Hlavné pamäťové sekcie
        self.packs: List[str] = []
        self.facts: List[Dict[str, Any]] = []
        self.rules: List[Dict[str, Any]] = []
        self.symbolic: List[str] = []
        self.intermediate: List[Dict[str, Any]] = []

        # Meta
        self.query: str = ""
        self.subjects: List[str] = []

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            self.clear()
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
    # SET QUERY + SUBJECTS
    # ------------------------------------------------------------------
    def set_query(self, query: str, subjects: List[str]) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Context memory disabled in safe-mode.",
                "version": "4.5",
            }

        if not isinstance(query, str):
            return {"status": "error", "code": "invalid_query_type", "version": "4.5"}

        if not isinstance(subjects, list):
            return {"status": "error", "code": "invalid_subjects_type", "version": "4.5"}

        self.query = query
        self.subjects = subjects
        return {"status": "ok", "version": "4.5"}

    # ------------------------------------------------------------------
    # ADD PACK
    # ------------------------------------------------------------------
    def add_pack(self, pack_name: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "version": "4.5"}

        if not isinstance(pack_name, str):
            return {"status": "error", "code": "invalid_pack_name", "version": "4.5"}

        if pack_name not in self.packs:
            self.packs.append(pack_name)

        return {"status": "ok", "version": "4.5"}

    # ------------------------------------------------------------------
    # ADD FACT
    # ------------------------------------------------------------------
    def add_fact(self, pack: str, key: str, value: Any) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "version": "4.5"}

        if not isinstance(pack, str) or not isinstance(key, str):
            return {"status": "error", "code": "invalid_fact_fields", "version": "4.5"}

        self.facts.append(
            {
                "pack": pack,
                "key": key,
                "value": value,
            }
        )

        return {"status": "ok", "version": "4.5"}

    # ------------------------------------------------------------------
    # ADD RULE
    # ------------------------------------------------------------------
    def add_rule(self, rule: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "version": "4.5"}

        if not isinstance(rule, dict):
            return {"status": "error", "code": "invalid_rule_type", "version": "4.5"}

        self.rules.append(rule)
        return {"status": "ok", "version": "4.5"}

    # ------------------------------------------------------------------
    # ADD SYMBOLIC EXPRESSION
    # ------------------------------------------------------------------
    def add_symbolic(self, expr: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "version": "4.5"}

        if not isinstance(expr, str):
            return {"status": "error", "code": "invalid_symbolic_type", "version": "4.5"}

        self.symbolic.append(expr)
        return {"status": "ok", "version": "4.5"}

    # ------------------------------------------------------------------
    # ADD INTERMEDIATE RESULT
    # ------------------------------------------------------------------
    def add_intermediate(self, label: str, data: Any) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "version": "4.5"}

        if not isinstance(label, str):
            return {
                "status": "error",
                "code": "invalid_intermediate_label",
                "version": "4.5",
            }

        self.intermediate.append(
            {
                "label": label,
                "data": data,
            }
        )

        return {"status": "ok", "version": "4.5"}

    # ------------------------------------------------------------------
    # EXPORT CONTEXT
    # ------------------------------------------------------------------
    def export(self) -> Dict[str, Any]:
        """
        Deterministický export pre:
        - Graph Builder 4.5
        - Chain Executor 4.5
        - Rule Engine 4.5
        - Explainer 4.5
        """

        return {
            "status": "ok",
            "query": self.query,
            "subjects": list(self.subjects),
            "packs": list(self.packs),
            "facts": list(self.facts),
            "rules": list(self.rules),
            "symbolic": list(self.symbolic),
            "intermediate": list(self.intermediate),
            "degraded_mode": self.degraded_mode,
            "version": "4.5",
        }

    # ------------------------------------------------------------------
    # CLEAR MEMORY
    # ------------------------------------------------------------------
    def clear(self) -> Dict[str, Any]:
        try:
            self.packs.clear()
            self.facts.clear()
            self.rules.clear()
            self.symbolic.clear()
            self.intermediate.clear()
            self.query = ""
            self.subjects = []
            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "clear_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "packs": len(self.packs),
            "facts": len(self.facts),
            "rules": len(self.rules),
            "symbolic": len(self.symbolic),
            "intermediate": len(self.intermediate),
            "version": "4.5",
        }
