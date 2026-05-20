"""
SIRIUS LOCAL AI – Reasoning Explainer 4.4.0 (PRO)

Účel:
- vytvára vysvetliteľný reasoning trace
- skladá dokopy:
    - query
    - subjects
    - použité packy a fakty
    - aplikované pravidlá
    - chain kroky a intermediate stavy
    - reasoning graf (ak je k dispozícii)
- 100 % offline, deterministické, bez AI heuristiky
- kompatibilné so Security Family 4.4 a Self‑Repair 4.4
"""

from typing import Dict, Any, List, Optional


class ReasoningExplainer44:
    """
    Deterministic explainer pre Reasoning Engine 4.4 (PRO).
    """

    def __init__(self):
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
            self.initialized = True
            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "init_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # PUBLIC API – EXPLAIN
    # ------------------------------------------------------------------
    def explain(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Vytvorí vysvetlenie z výsledku ReasoningCore44.reason().

        Očakáva štruktúru:
        {
            "status": "ok",
            "query": ...,
            "subjects": [...],
            "context": {...},
            "chain": {...},
            "graph": {...} alebo None
        }
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Explainer disabled in safe-mode."}

        if not isinstance(core_result, dict):
            return {"status": "error", "code": "invalid_core_result_type"}

        if core_result.get("status") != "ok":
            return {
                "status": "error",
                "code": "core_not_ok",
                "core_status": core_result.get("status"),
            }

        try:
            query = core_result.get("query", "")
            subjects = core_result.get("subjects", [])
            context = core_result.get("context", {})
            chain = core_result.get("chain", {})
            graph = core_result.get("graph")

            explanation: Dict[str, Any] = {
                "status": "ok",
                "query": query,
                "subjects": subjects,
                "steps": [],
                "degraded_mode": self.degraded_mode,
            }

            # 1. Základný kontext
            explanation["steps"].append(
                self._step_query_context(query, subjects, context)
            )

            # 2. Chain trace (ak existuje)
            chain_step = self._extract_chain_trace(chain)
            if chain_step is not None:
                explanation["steps"].append(chain_step)

            # 3. Pravidlá (ak existujú)
            rules_step = self._extract_rules_step(chain)
            if rules_step is not None:
                explanation["steps"].append(rules_step)

            # 4. Symbolic (ak existuje)
            symbolic_step = self._extract_symbolic_step(chain)
            if symbolic_step is not None:
                explanation["steps"].append(symbolic_step)

            # 5. Reasoning graf (ak existuje)
            if graph is not None and isinstance(graph, dict):
                if graph.get("status") == "ok":
                    explanation["steps"].append(self._step_graph(graph))

            return explanation

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "explain_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STEP BUILDERS
    # ------------------------------------------------------------------
    def _step_query_context(
        self,
        query: str,
        subjects: List[str],
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        return {
            "type": "query_context",
            "query": query,
            "subjects": subjects,
            "packs_used": context.get("packs", []),
            "facts_count": len(context.get("facts", [])),
            "rules_count": len(context.get("rules", [])),
            "symbolic_count": len(context.get("symbolic", [])),
        }

    def _extract_chain_trace(self, chain: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if chain.get("status") != "ok":
            return None

        state = chain.get("state", {})
        return {
            "type": "chain_trace",
            "chain": chain.get("chain"),
            "intermediate": state.get("intermediate", []),
        }

    def _extract_rules_step(self, chain: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        result = chain.get("result", {})
        if result.get("type") != "rules":
            return None

        return {
            "type": "rules",
            "status": result.get("status"),
            "rules_applied": result.get("rules_applied"),
            "conclusions": result.get("conclusions"),
        }

    def _extract_symbolic_step(self, chain: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        result = chain.get("result", {})
        if result.get("type") != "symbolic":
            return None

        return {
            "type": "symbolic",
            "status": result.get("status"),
            "ast": result.get("ast"),
            "value": result.get("value"),
        }

    def _step_graph(self, graph_result: Dict[str, Any]) -> Dict[str, Any]:
        graph = graph_result.get("graph", {})
        return {
            "type": "graph",
            "nodes_count": len(graph.get("nodes", [])),
            "edges_count": len(graph.get("edges", [])),
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
        }
