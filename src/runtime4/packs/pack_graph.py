"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Graph (Runtime 4.3)

Responsible for:
- tracking dependencies between packs
- resolving activation order
- detecting cycles with diagnostics
- preparing packs for linking
- enforcing Security Family 4.4 rules
- supporting Self‑Repair 4.4 diagnostics

This is the graph layer of Knowledge Packs 2.0 (Runtime 4.3).
"""


class PackGraph4:
    """
    Graph-based dependency manager for Knowledge Packs 2.0.
    Provides:
    - strict validation
    - structured error surface
    - deterministic topological sorting
    - cycle diagnostics
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, max_packs: int = 500):
        self.graph = {}
        self.max_packs = max_packs
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_name(self, name):
        return isinstance(name, str) and name.strip()

    # ---------------------------------------------------------
    # GRAPH MANAGEMENT
    # ---------------------------------------------------------

    def add_pack(self, name: str):
        """Registers a pack in the graph with safety checks."""

        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_pack_name"}

        if len(self.graph) >= self.max_packs:
            return {"status": "error", "code": "pack_limit_reached"}

        if name not in self.graph:
            self.graph[name] = []

        return {"status": "success", "pack": name}

    def add_dependency(self, pack: str, depends_on: str):
        """Declares that `pack` depends on `depends_on` with safety checks."""

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

        return {"status": "success", "pack": pack, "depends_on": depends_on}

    def get_dependencies(self, pack: str):
        if not self._validate_name(pack):
            return []
        return self.graph.get(pack, [])

    # ---------------------------------------------------------
    # ORDER RESOLUTION (TOPOLOGICAL SORT)
    # ---------------------------------------------------------

    def resolve_order(self):
        """
        Performs a topological sort to determine safe activation order.
        Returns structured result with diagnostics.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "PackGraph resolution disabled in safe-mode."
            }

        cycle = self._detect_cycle_path()
        if cycle:
            return {
                "status": "error",
                "code": "cycle_detected",
                "cycle": cycle
            }

        visited = set()
        order = []

        def visit(node):
            if node in visited:
                return
            visited.add(node)

            deps = self.graph.get(node, [])
            for dep in deps:
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
                "exception": str(exc)
            }

        return {
            "status": "success",
            "order": order,
            "count": len(order),
            "degraded_mode": self.degraded_mode
        }

    # ---------------------------------------------------------
    # CYCLE DETECTION WITH DIAGNOSTICS
    # ---------------------------------------------------------

    def _detect_cycle_path(self):
        visited = set()
        stack = []

        def visit(node):
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
