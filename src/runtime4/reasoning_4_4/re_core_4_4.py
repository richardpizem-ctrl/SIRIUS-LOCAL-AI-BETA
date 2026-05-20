"""
SIRIUS LOCAL AI – Reasoning Core 4.4.0 (PRO)

Hlavné deterministické jadro Reasoning Engine 4.4.

Účel:
- centralizované rozhranie pre reasoning dotazy
- orchestrácia:
    - Multi‑Subject Router 4.4
    - Context Builder 4.4
    - Context Memory 4.4
    - Chain Executor 4.4
    - Rule Engine 4.4
    - Symbolic Solver 4.4
    - (voliteľne) Graph Builder 4.4

Vlastnosti:
- 100 % offline, deterministické
- žiadne AI heuristiky
- žiadne dynamické importy, eval, exec
- kompatibilné so Security Family 4.4 a Self‑Repair 4.4
"""

from typing import Dict, Any, Optional


class ReasoningCore44:
    """
    Deterministic PRO jadro Reasoning Engine 4.4.
    """

    def __init__(
        self,
        registry=None,
        query_engine=None,
        context_builder=None,
        context_memory=None,
        multi_subject_router=None,
        graph_builder=None,
        chain_executor=None,
        rule_engine=None,
        symbolic_solver=None,
    ):
        # Základné komponenty
        self.registry = registry
        self.query_engine = query_engine
        self.context_builder = context_builder
        self.context_memory = context_memory
        self.multi_subject_router = multi_subject_router
        self.graph_builder = graph_builder
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
                self.context_memory,
                self.multi_subject_router,
                self.graph_builder,
                self.chain_executor,
                self.rule_engine,
                self.symbolic_solver,
            ]

            for module in modules:
                if module and hasattr(module, "initialize"):
                    res = module.initialize()
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
    # MAIN ENTRYPOINT – REASON
    # ------------------------------------------------------------------
    def reason(self, query: str) -> Dict[str, Any]:
        """
        Deterministická reasoning pipeline:

        1. validácia vstupu
        2. detekcia tém (router)
        3. zostavenie kontextu (Context Builder 4.4)
        4. vykonanie reasoning chainu (Chain Executor 4.4)
        5. voliteľne: reasoning graf
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Reasoning disabled in safe-mode."}

        if not isinstance(query, str) or not query.strip():
            return {"status": "error", "code": "invalid_query"}

        # 1. Inicializácia
        if not self.initialized:
            init = self.initialize()
            if init.get("status") != "ok" and init.get("status") != "already_initialized":
                return init

        try:
            # 2. Detekcia tém
            subjects = (
                self.multi_subject_router.detect_subjects(query)
                if self.multi_subject_router
                else ["general"]
            )

            # 3. Zostavenie kontextu
            if not self.context_builder:
                return {"status": "error", "code": "no_context_builder"}

            context_export = self.context_builder.build_context(subjects)
            if context_export.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "context_build_failed",
                    "details": context_export,
                }

            # 4. Reasoning chain
            if not self.chain_executor:
                return {"status": "error", "code": "no_chain_executor"}

            chain_result = self.chain_executor.execute(query, context_export)

            # 5. Reasoning graf (voliteľné)
            graph_result: Optional[Dict[str, Any]] = None
            if self.graph_builder:
                graph_result = self.graph_builder.build_graph(query, context_export)

            return {
                "status": "ok",
                "query": query,
                "subjects": subjects,
                "context": context_export,
                "chain": chain_result,
                "graph": graph_result,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "reasoning_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "has_registry": self.registry is not None,
            "has_query_engine": self.query_engine is not None,
            "has_context_builder": self.context_builder is not None,
            "has_context_memory": self.context_memory is not None,
            "has_router": self.multi_subject_router is not None,
            "has_graph_builder": self.graph_builder is not None,
            "has_chain_executor": self.chain_executor is not None,
            "has_rule_engine": self.rule_engine is not None,
            "has_symbolic_solver": self.symbolic_solver is not None,
        }
