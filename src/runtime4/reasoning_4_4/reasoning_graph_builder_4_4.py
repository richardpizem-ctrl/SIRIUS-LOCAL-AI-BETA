"""
SIRIUS LOCAL AI – Reasoning Graph Builder 4.4.0 (PRO)

Deterministic graph builder for Reasoning Engine 4.4.

Účel:
- vytvára reasoning grafy z kontextu
- uzly = fakty, packy, pravidlá, symbolické výrazy, intermediate kroky
- hrany = závislosti, referencie, odvodenia
- 100 % offline, deterministické, bez AI heuristiky
- kompatibilné so Security Family 4.4 a Self‑Repair 4.4
"""

from typing import Dict, Any, List


class ReasoningGraphBuilder44:
    """
    Deterministic reasoning graph builder (PRO).
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
    # BUILD GRAPH
    # ------------------------------------------------------------------
    def build_graph(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Vytvorí reasoning graf pre dotaz.
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Graph builder disabled in safe-mode."}

        if not isinstance(query, str):
            return {"status": "error", "code": "invalid_query_type"}

        if not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type"}

        try:
            nodes: List[Dict[str, Any]] = []
            edges: List[Dict[str, Any]] = []

            # ----------------------------------------------------------
            # 1. Query node
            # ----------------------------------------------------------
            nodes.append({
                "id": "query",
                "type": "query",
                "value": query,
            })

            # ----------------------------------------------------------
            # 2. Subject nodes
            # ----------------------------------------------------------
            for s in context.get("subjects", []):
                nodes.append({
                    "id": f"subject:{s}",
                    "type": "subject",
                    "value": s,
                })
                edges.append({
                    "from": "query",
                    "to": f"subject:{s}",
                    "type": "subject_relation",
                })

            # ----------------------------------------------------------
            # 3. Pack nodes
            # ----------------------------------------------------------
            for p in context.get("packs", []):
                nodes.append({
                    "id": f"pack:{p}",
                    "type": "pack",
                    "value": p,
                })
                edges.append({
                    "from": "query",
                    "to": f"pack:{p}",
                    "type": "pack_usage",
                })

            # ----------------------------------------------------------
            # 4. Fact nodes
            # ----------------------------------------------------------
            for fact in context.get("facts", []):
                fid = f"fact:{fact['pack']}:{fact['key']}"
                nodes.append({
                    "id": fid,
                    "type": "fact",
                    "pack": fact["pack"],
                    "key": fact["key"],
                    "value": fact["value"],
                })
                edges.append({
                    "from": f"pack:{fact['pack']}",
                    "to": fid,
                    "type": "fact_belongs_to_pack",
                })

            # ----------------------------------------------------------
            # 5. Rule nodes
            # ----------------------------------------------------------
            for rule in context.get("rules", []):
                rid = f"rule:{rule.get('id', 'unknown')}"
                nodes.append({
                    "id": rid,
                    "type": "rule",
                    "rule": rule,
                })

                # Rule dependencies
                for cond in rule.get("if", []):
                    fkey = f"fact:{cond['pack']}:{cond['key']}"
                    edges.append({
                        "from": fkey,
                        "to": rid,
                        "type": "rule_condition",
                    })

            # ----------------------------------------------------------
            # 6. Symbolic nodes
            # ----------------------------------------------------------
            for expr in context.get("symbolic", []):
                sid = f"symbolic:{expr}"
                nodes.append({
                    "id": sid,
                    "type": "symbolic",
                    "expr": expr,
                })
                edges.append({
                    "from": "query",
                    "to": sid,
                    "type": "symbolic_relation",
                })

            # ----------------------------------------------------------
            # 7. Intermediate nodes
            # ----------------------------------------------------------
            for idx, step in enumerate(context.get("intermediate", [])):
                iid = f"intermediate:{idx}"
                nodes.append({
                    "id": iid,
                    "type": "intermediate",
                    "label": step.get("label"),
                    "data": step.get("data"),
                })
                edges.append({
                    "from": "query",
                    "to": iid,
                    "type": "intermediate_step",
                })

            return {
                "status": "ok",
                "graph": {
                    "nodes": nodes,
                    "edges": edges,
                },
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "graph_build_failed", "exception": str(exc)}

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
