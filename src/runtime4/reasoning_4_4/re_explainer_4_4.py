# reasoning_4_4/re_explainer_4_4.py
"""
SIRIUS LOCAL AI – Reasoning Explainer 4.4.0

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
"""

from typing import Dict, Any, List, Optional


class ReasoningExplainer44:
    """
    Deterministic explainer pre Reasoning Engine 4.4.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

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
    # BUILD EXPLANATION
    # ------------------------------------------------------------------
    def explain(
        self,
        core_result: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Vytvorí vysvetlenie z výsledku ReasoningCore44.reason().
        Očakáva štruktúru:
        {
            "status": "ok",
            "query": ...,
            "subjects": [...],
            "routing": {...},
            "context": {...},
            "graph": {...} alebo None
        }
        """

        try:
            if core_result.get("status") != "ok":
                return {
                    "status": "error",
                    "reason": "core_not_ok",
                    "core_status": core_result.get("status"),
                }

            query = core_result.get("query", "")
            subjects = core_result.get("subjects", [])
            routing = core_result.get("routing", {})
            context = core_result.get("context", {})
            graph = core_result.get("graph")

            explanation: Dict[str, Any] = {
                "status": "ok",
                "query": query,
                "subjects": subjects,
                "steps": [],
            }

            # 1. Základný kontext
            explanation["steps"].append(self._step_query_context(query, subjects, context))

            # 2. Routing rozhodnutie
            explanation["steps"].append(self._step_routing(routing))

            # 3. Chain trace (ak existuje)
            chain_trace = self._extract_chain_trace(routing)
            if chain_trace is not None:
                explanation["steps"].append(chain_trace)

            # 4. Pravidlá (ak existujú)
            rules_step = self._extract_rules_step(routing)
            if rules_step is not None:
                explanation["steps"].append(rules_step)

            # 5. Symbolic (ak existuje)
            symbolic_step = self._extract_symbolic_step(routing)
            if symbolic_step is not None:
                explanation["steps"].append(symbolic_step)

            # 6. Graf (ak existuje)
            if graph is not None and graph.get("status", "ok") == "ok":
                explanation["steps"].append(self._step_graph(graph))

            return explanation

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

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

    def _step_routing(self, routing: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "type": "routing",
            "routing_type": routing.get("type"),
            "routing_status": routing.get("status"),
            "routing_subjects": routing.get("subjects"),
        }

    def _extract_chain_trace(self, routing: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if routing.get("type") != "chain":
            return None

        state = routing.get("result", {}).get("state", {})
        return {
            "type": "chain_trace",
            "chain": routing.get("result", {}).get("chain"),
            "intermediate": state.get("intermediate", []),
        }

    def _extract_rules_step(self, routing: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if routing.get("type") != "rules":
            return None

        result = routing.get("result", {})
        return {
            "type": "rules",
            "status": result.get("status"),
            "rules_applied": result.get("rules_applied"),
            "conclusions": result.get("conclusions"),
        }

    def _extract_symbolic_step(self, routing: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if routing.get("type") != "symbolic":
            return None

        result = routing.get("result", {})
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
            "degraded_mode": self.degraded_mode,
        }
