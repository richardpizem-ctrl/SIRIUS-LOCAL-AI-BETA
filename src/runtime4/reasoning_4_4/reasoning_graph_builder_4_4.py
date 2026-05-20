# reasoning_4_4/reasoning_graph_builder_4_4.py
"""
SIRIUS LOCAL AI – Reasoning Graph Builder 4.4.0

Deterministic graph builder for Reasoning Engine 4.4.

Účel:
- vytvára reasoning grafy z kontextu
- uzly = fakty, packy, pravidlá, symbolické výrazy
- hrany = závislosti, referencie, odvodenia
- 100 % offline, deterministické, bez AI heuristiky
- žiadne dynamické importy, eval, exec

Používa:
- KP Registry 4.4
- KP Query Engine 4.4
- Context Builder 4.4
- Rule Engine 4.4
- Symbolic Solver 4.4 (ak treba)
"""

from typing import Dict, Any, List


class ReasoningGraphBuilder44:
    """
    Vytvára reasoning graf pre dotaz.
    """

    def __init__(
        self,
        registry=None,
        query_engine=None,
        rule_engine=None,
        symbolic_solver=None,
    ):
        self.registry = registry
        self.query_engine = query_engine
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
    # BUILD GRAPH
    # ------------------------------------------------------------------
    def build_graph(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Vytvorí reasoning graf:
        - uzly: fakty, packy, pravidlá, symbolické výrazy
        - hrany: závislosti medzi nimi
        """

        try:
            graph = {
                "nodes": [],
                "edges": [],
                "query": query,
            }

            # 1. Pack nodes
            for pack_name in context.get("packs", []):
                graph["nodes"].append({
                    "id": f"pack:{pack_name}",
                    "type": "pack",
                    "name": pack_name,
                })

            # 2. Fact nodes
            for fact in context.get("facts", []):
                graph["nodes"].append({
                    "id": f"fact:{fact['key']}",
                    "type": "fact",
                    "key": fact["key"],
                    "value": fact["value"],
                    "pack": fact["pack"],
                })
                graph["edges"].append({
                    "from": f"pack:{fact['pack']}",
                    "to": f"fact:{fact['key']}",
                    "type": "contains",
                })

            # 3. Rule nodes
            if self.rule_engine:
                rules = self.rule_engine.extract_rules(context)
                for r in rules:
                    rid = f"rule:{r['id']}"
                    graph["nodes"].append({
                        "id": rid,
                        "type": "rule",
                        "rule": r,
                    })
                    # Link rule to facts it uses
                    for dep in r.get("depends_on", []):
                        graph["edges"].append({
                            "from": f"fact:{dep}",
                            "to": rid,
                            "type": "rule_depends",
                        })

            # 4. Symbolic nodes (if math)
            if self.symbolic_solver and context.get("symbolic"):
                parsed = self.symbolic_solver.parse(context["symbolic"])
                if parsed.get("status") == "ok":
                    graph["nodes"].append({
                        "id": "symbolic:expr",
                        "type": "symbolic",
                        "ast": repr(parsed["ast"]),
                    })

            return {"status": "ok", "graph": graph}

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
