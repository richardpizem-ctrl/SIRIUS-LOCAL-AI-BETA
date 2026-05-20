# reasoning_4_4/reasoning_context_memory_4_4.py
"""
SIRIUS LOCAL AI – Reasoning Context Memory 4.4.0

Deterministic context memory for Reasoning Engine 4.4.

Účel:
- drží krátkodobú reasoning pamäť pre jeden dotaz
- uchováva fakty, packy, pravidlá, symbolické výrazy, intermediate výsledky
- poskytuje bezpečné API pre zápis/čítanie
- 100 % offline, deterministické, bez AI heuristiky
- žiadne dynamické importy, eval, exec

Používa sa v:
- Context Builder 4.4
- Chain Executor 4.4
- Rule Engine 4.4
- Graph Builder 4.4
- Multi‑Subject Router 4.4
"""

from typing import Dict, Any, List


class ReasoningContextMemory44:
    """
    Krátkodobá reasoning pamäť pre jeden dotaz.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

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
            return {"status": "already_initialized"}

        try:
            self.clear()
            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SET QUERY + SUBJECTS
    # ------------------------------------------------------------------
    def set_query(self, query: str, subjects: List[str]) -> None:
        self.query = query
        self.subjects = subjects

    # ------------------------------------------------------------------
    # ADD PACK
    # ------------------------------------------------------------------
    def add_pack(self, pack_name: str) -> None:
        if pack_name not in self.packs:
            self.packs.append(pack_name)

    # ------------------------------------------------------------------
    # ADD FACT
    # ------------------------------------------------------------------
    def add_fact(self, pack: str, key: str, value: Any) -> None:
        self.facts.append({
            "pack": pack,
            "key": key,
            "value": value,
        })

    # ------------------------------------------------------------------
    # ADD RULE
    # ------------------------------------------------------------------
    def add_rule(self, rule: Dict[str, Any]) -> None:
        self.rules.append(rule)

    # ------------------------------------------------------------------
    # ADD SYMBOLIC EXPRESSION
    # ------------------------------------------------------------------
    def add_symbolic(self, expr: str) -> None:
        self.symbolic.append(expr)

    # ------------------------------------------------------------------
    # ADD INTERMEDIATE RESULT
    # ------------------------------------------------------------------
    def add_intermediate(self, label: str, data: Any) -> None:
        self.intermediate.append({
            "label": label,
            "data": data,
        })

    # ------------------------------------------------------------------
    # EXPORT CONTEXT (for graph builder, chain executor, etc.)
    # ------------------------------------------------------------------
    def export(self) -> Dict[str, Any]:
        return {
            "query": self.query,
            "subjects": self.subjects,
            "packs": list(self.packs),
            "facts": list(self.facts),
            "rules": list(self.rules),
            "symbolic": list(self.symbolic),
            "intermediate": list(self.intermediate),
        }

    # ------------------------------------------------------------------
    # CLEAR MEMORY
    # ------------------------------------------------------------------
    def clear(self) -> None:
        self.packs.clear()
        self.facts.clear()
        self.rules.clear()
        self.symbolic.clear()
        self.intermediate.clear()
        self.query = ""
        self.subjects = []

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "packs": len(self.packs),
            "facts": len(self.facts),
            "rules": len(self.rules),
            "symbolic": len(self.symbolic),
            "intermediate": len(self.intermediate),
        }
