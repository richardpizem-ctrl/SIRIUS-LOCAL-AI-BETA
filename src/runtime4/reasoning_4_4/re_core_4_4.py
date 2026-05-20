# reasoning_4_4/re_core_4_4.py
"""
SIRIUS LOCAL AI – Reasoning Core 4.4.0

Hlavné jadro Reasoning Engine 4.4.

Účel:
- centralizované rozhranie pre reasoning dotazy
- orchestrácia:
    - Multi‑Subject Router 4.4
    - Context Memory 4.4
    - Graph Builder 4.4
    - Chain Executor 4.4
    - Rule Engine 4.4
    - Symbolic Solver 4.4
- 100 % offline, deterministické, bez AI heuristiky
- žiadne dynamické importy, eval, exec
"""

from typing import Dict, Any, Optional


class ReasoningCore44:
    """
    Hlavné jadro Reasoning Engine 4.4.
    """

    def __init__(
        self,
        registry=None,
        query_engine=None,
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
        self.context_memory = context_memory
        self.multi_subject_router = multi_subject_router
        self.graph_builder = graph_builder
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
            if self.context_memory:
                self.context_memory.initialize()
            if self.multi_subject_router:
                self.multi_subject_router.initialize()
            if self.graph_builder:
                self.graph_builder.initialize()
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
    # MAIN ENTRYPOINT – REASON
    # ------------------------------------------------------------------
    def reason(self, query: str) -> Dict[str, Any]:
        """
        Hlavný vstupný bod pre reasoning dotazy.
        Pipeline (deterministicky):

        1. detekcia tém (router)
        2. inicializácia context memory
        3. naplnenie context memory (packs, fakty, atď.)
        4. routing na konkrétny reasoning mód
        5. voliteľne: build reasoning graf
        """

        if not self.initialized:
            init = self.initialize()
            if init.get("status") != "initialized" and init.get("status") != "already_initialized":
                return init

        try:
            # 1. Detekcia tém
            subjects = self.multi_subject_router.detect_subjects(query) if self.multi_subject_router else ["general"]

            # 2. Context memory
            if self.context_memory:
                self.context_memory.clear()
                self.context_memory.set_query(query, subjects)

            # 3. Naplnenie kontextu z registry/query engine (ak chceš, rozšíriš neskôr)
            context_export = self.context_memory.export() if self.context_memory else {
                "query": query,
                "subjects": subjects,
                "packs": [],
                "facts": [],
                "rules": [],
                "symbolic": [],
                "intermediate": [],
            }

            # 4. Routing – nech router rozhodne, čo ďalej
            routed = self.multi_subject_router.route(query) if self.multi_subject_router else {
                "status": "ok",
                "type": "none",
                "result": None,
                "subjects": subjects,
            }

            # 5. Reasoning graf (voliteľný, ale užitočný)
            graph_result: Optional[Dict[str, Any]] = None
            if self.graph_builder:
                graph_result = self.graph_builder.build_graph(query, context_export)

            return {
                "status": "ok",
                "query": query,
                "subjects": subjects,
                "routing": routed,
                "context": context_export,
                "graph": graph_result,
            }

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # LOW-LEVEL ACCESSORS (ak chceš používať moduly priamo)
    # ------------------------------------------------------------------
    def get_registry(self):
        return self.registry

    def get_query_engine(self):
        return self.query_engine

    def get_context_memory(self):
        return self.context_memory

    def get_router(self):
        return self.multi_subject_router

    def get_graph_builder(self):
        return self.graph_builder

    def get_chain_executor(self):
        return self.chain_executor

    def get_rule_engine(self):
        return self.rule_engine

    def get_symbolic_solver(self):
        return self.symbolic_solver

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "has_registry": self.registry is not None,
            "has_query_engine": self.query_engine is not None,
            "has_context_memory": self.context_memory is not None,
            "has_router": self.multi_subject_router is not None,
            "has_graph_builder": self.graph_builder is not None,
            "has_chain_executor": self.chain_executor is not None,
            "has_rule_engine": self.rule_engine is not None,
            "has_symbolic_solver": self.symbolic_solver is not None,
        }
