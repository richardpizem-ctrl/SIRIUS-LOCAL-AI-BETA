# reasoning_4_4/reasoning_multi_subject_router_4_4.py
"""
SIRIUS LOCAL AI – Multi‑Subject Reasoning Router 4.4.0

Deterministic router, ktorý rozhoduje:
- ktorý reasoning modul sa má použiť
- ktoré Knowledge Packy sú relevantné
- ako sa má rozdeliť dotaz podľa tém
- ako sa má vykonať multi‑subject reasoning pipeline

Router 4.4 je 100 % offline, deterministický, bez AI heuristiky.
Používa iba:
- KP Registry 4.4
- KP Query Engine 4.4
- Reasoning Context Builder 4.4
- Reasoning Chain Executor 4.4
- Reasoning Rule Engine 4.4
- Reasoning Symbolic Solver 4.4 (ak treba)
"""

from typing import Dict, Any, List, Optional


class ReasoningMultiSubjectRouter44:
    """
    Hlavný router pre Reasoning Engine 4.4.
    Rozdeľuje dotazy podľa tém a smeruje ich do správnych reasoning modulov.
    """

    def __init__(
        self,
        registry=None,
        query_engine=None,
        context_builder=None,
        chain_executor=None,
        rule_engine=None,
        symbolic_solver=None,
    ):
        self.registry = registry
        self.query_engine = query_engine
        self.context_builder = context_builder
        self.chain_executor = chain_executor
        self.rule_engine = rule_engine
        self.symbolic_solver = symbolic_solver

        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.registry:
                self.registry.initialize()
            if self.query_engine:
                self.query_engine.initialize()
            if self.context_builder:
                self.context_builder.initialize()
            if self.chain_executor:
                self.chain_executor.initialize()
            if self.rule_engine:
                self.rule_engine.initialize()
            if self.symbolic_solver:
                self.symbolic_solver.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SUBJECT DETECTION (deterministic)
    # ------------------------------------------------------------------
    def detect_subjects(self, text: str) -> List[str]:
        """
        Jednoduchá deterministická detekcia tém podľa kľúčových slov.
        Žiadne AI, žiadne heuristiky.
        """

        text_l = text.lower()
        subjects = []

        if any(w in text_l for w in ["math", "calculate", "solve", "equation"]):
            subjects.append("math")

        if any(w in text_l for w in ["history", "year", "war", "king"]):
            subjects.append("history")

        if any(w in text_l for w in ["language", "grammar", "word", "translate"]):
            subjects.append("language")

        if any(w in text_l for w in ["science", "physics", "chemistry", "biology"]):
            subjects.append("science")

        if any(w in text_l for w in ["geography", "country", "capital", "continent"]):
            subjects.append("geography")

        if not subjects:
            subjects.append("general")

        return subjects

    # ------------------------------------------------------------------
    # ROUTING LOGIC
    # ------------------------------------------------------------------
    def route(self, query: str) -> Dict[str, Any]:
        """
        Hlavná routing funkcia.
        """

        try:
            subjects = self.detect_subjects(query)

            # 1. Vyber relevantné packy
            ctx = self.context_builder.build_context(subjects)

            # 2. Ak je matematika → symbolic solver
            if "math" in subjects and self.symbolic_solver:
                symbolic = self.symbolic_solver.simplify(query)
                return {
                    "status": "ok",
                    "type": "symbolic",
                    "result": symbolic,
                    "subjects": subjects,
                }

            # 3. Ak sú pravidlá → rule engine
            if "history" in subjects or "science" in subjects:
                rules = self.rule_engine.apply_rules(query, ctx)
                return {
                    "status": "ok",
                    "type": "rules",
                    "result": rules,
                    "subjects": subjects,
                }

            # 4. Default → chain executor
            chain = self.chain_executor.execute(query, ctx)
            return {
                "status": "ok",
                "type": "chain",
                "result": chain,
                "subjects": subjects,
            }

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
