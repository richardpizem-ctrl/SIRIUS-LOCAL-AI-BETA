"""
SIRIUS LOCAL AI – Knowledge Packs Graph 4.4.0 (PRO)

Responsible for:
- deterministic dependency tracking
- activation order resolution (topological sort)
- cycle diagnostics with full path
- strict validation of pack names
- safe-mode compatibility
- degraded-mode detection
- Self‑Repair 4.4 compatible error surface
- Security Family 4.4 enforcement

This is the graph layer of Knowledge Packs 4.4.
"""

from typing import Dict, Any, List, Optional


class PackGraph44:
    """
    Deterministic dependency graph for Knowledge Packs 4.4.
    """

    def __init__(self, max_packs: int = 1000):
        self.graph: Dict[str, List[str]] = {}
        self.max_packs = max_packs

        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # VALIDATION HELPERS
    # ------------------------------------------------------------------
    def _validate_name(self, name: Any) -> bool:
        return isinstance(name, str) and name.strip()

    # ------------------------------------------------------------------
    # GRAPH MANAGEMENT
    # ------------------------------------------------------------------
    def add_pack(self, name: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Graph modification disabled in safe-mode."}

        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_pack_name"}

        if len(self.graph) >= self.max_packs:
            return {"status": "error", "code": "pack_limit_reached"}

        if name not in self.graph:
            self.graph[name] = []

        return {"status": "ok", "pack": name}

    def add_dependency(self, pack: str, depends_on: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Graph modification disabled in safe-mode."}

        if not self._validate_name(pack):
            return {"status": "error", "code": "invalid_pack_name"}

        if not self._validate_name(depends_on):
            return {"status": "error", "code": "invalid_dependency_name"}

        if pack == depends_on:
            return {"status": "error", "code": "self_dependency_not_allowed"}

        if pack not in self.graph:
            self.graph[pack] = []

        if depends_on not in self.graph:
            self.graph[depends_on] = []

        if depends_on not in self.graph[pack]:
            self.graph[pack].append(depends_on)

        return {"status": "ok", "pack": pack, "depends_on": depends_on}

    def get_dependencies(self, pack: str) -> List[str]:
        if not self._validate_name(pack):
            return []
        return list(self.graph.get(pack, []))

    # ------------------------------------------------------------------
    # CYCLE DETECTION (FULL DIAGNOSTIC PATH)
    # ------------------------------------------------------------------
    def _detect_cycle(self) -> Optional[List[str]]:
        visited = set()
        stack: List[str] = []

        def visit(node: str):
            if not self._validate_name(node):
                return ["invalid_node"]

            if node in stack:
                idx = stack.index(node)
                return stack[idx:] + [node]

            if node in visited:
                return None

            visited.add(node)
            stack.append(node)

            for dep in self.graph.get(node, []):
                result = visit(dep)
                if result:
                    return result

            stack.pop()
            return None

        for pack in self.graph:
            result = visit(pack)
            if result:
                return result

        return None

    # ------------------------------------------------------------------
    # ORDER RESOLUTION (TOPOLOGICAL SORT)
    # ------------------------------------------------------------------
    def resolve_order(self) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Graph resolution disabled in safe-mode."}

        cycle = self._detect_cycle()
        if cycle:
            return {
                "status": "error",
                "code": "cycle_detected",
                "cycle": cycle,
            }

        visited = set()
        order: List[str] = []

        def visit(node: str):
            if node in visited:
                return
            visited.add(node)

            for dep in self.graph.get(node, []):
                visit(dep)

            order.append(node)

        try:
            for pack in list(self.graph.keys()):
                visit(pack)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "resolution_failed",
                "exception": str(exc),
            }

        return {
            "status": "ok",
            "order": order,
            "count": len(order),
            "degraded_mode": self.degraded_mode,
        }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "packs": len(self.graph),
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }
