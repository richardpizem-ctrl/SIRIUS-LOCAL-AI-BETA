"""
SIRIUS LOCAL AI – Multi‑Subject Reasoning Router 4.4.0 (PRO)

Deterministic router pre Reasoning Engine 4.4.

Účel:
- rozhoduje, ktorý reasoning modul sa má použiť
- rozdeľuje dotaz podľa tém
- vyberá relevantné Knowledge Packy
- spúšťa správny reasoning mód (symbolic / rules / chain)
- 100 % offline, deterministické, bez AI heuristiky
- kompatibilné so Security Family 4.4 a Self‑Repair 4.4
"""

from typing import Dict, Any, List, Optional


class ReasoningMultiSubjectRouter44:
    """
    Deterministic multi‑subject router (PRO).
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
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            modules = [
                self.registry,
                self.query_engine,
                self.context_builder,
                self.chain_executor,
                self.rule_engine,
                self.symbolic_solver,
            ]

            for m in modules:
                if m and hasattr(m, "initialize"):
                    res = m.initialize()
                    if isinstance(res, dict) and res.get("status") == "error":
                        self.degraded_mode = True
                        return {
                            "status": "error",
                            "code": "module_init_failed",
                            "details": res,
                        }

            self.initialized = True
            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "init_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SUBJECT DETECTION (deterministic)
    # ------------------------------------------------------------------
    def detect_subjects(self, text: str) -> List[str]:
        """
        Deterministická detekcia tém podľa kľúčových slov.
        Žiadne AI, žiadne heuristiky.
        """

        if not isinstance(text, str):
            return ["general"]

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
    # ROUTING LOGIC (PRO)
    # ------------------------------------------------------------------
    def route(self, query: str) -> Dict[str, Any]:
        """
        Hlavná routing funkcia.
        Rozhoduje, ktorý reasoning mód sa použije.
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Router disabled in safe-mode."}

        if not isinstance(query, str):
            return {"status": "error", "code": "invalid_query_type"}

        try:
            # 1. Detekcia tém
            subjects = self.detect_subjects(query)

            # 2. Zostavenie kontextu
            if not self.context_builder:
                return {"status": "error", "code": "no_context_builder"}

            ctx = self.context_builder.build_context(subjects)
            if ctx.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "context_build_failed",
                    "details": ctx,
                }

            # 3. Symbolic reasoning (math)
            if "math" in subjects and self.symbolic_solver:
                symbolic = self.symbolic_solver.simplify(query)
                return {
                    "status": "ok",
                    "type": "symbolic",
                    "result": symbolic,
                    "subjects": subjects,
                }

            # 4. Rule‑based reasoning (history, science)
            if ("history" in subjects or "science" in subjects) and self.rule_engine:
                rules = self.rule_engine.apply_rules(query, ctx)
                return {
                    "status": "ok",
                    "type": "rules",
                    "result": rules,
                    "subjects": subjects,
                }

            # 5. Default → chain executor
            if not self.chain_executor:
                return {"status": "error", "code": "no_chain_executor"}

            chain = self.chain_executor.execute(query, ctx)
            return {
                "status": "ok",
                "type": "chain",
                "result": chain,
                "subjects": subjects,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "routing_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }
