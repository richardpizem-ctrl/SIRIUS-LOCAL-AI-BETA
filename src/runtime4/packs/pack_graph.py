"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Graph

Responsible for:
- tracking dependencies between packs
- resolving activation order
- detecting cycles
- preparing packs for linking

This is the graph layer of Knowledge Packs 2.0.
"""


class PackGraph4:
    """
    Graph-based dependency manager for Knowledge Packs 2.0.
    """

    def __init__(self):
        # Graph stored as adjacency list:
        # { "pack_name": ["depends_on_A", "depends_on_B"] }
        self.graph = {}

    # ---------------------------------------------------------
    # GRAPH MANAGEMENT
    # ---------------------------------------------------------

    def add_pack(self, name: str):
        """Registers a pack in the graph with safety checks."""

        # Validate name
        if not isinstance(name, str) or not name.strip():
            return {"error": "invalid_pack_name"}

        if name not in self.graph:
            self.graph[name] = []

        return {"status": "pack_added"}

    def add_dependency(self, pack: str, depends_on: str):
        """Declares that `pack` depends on `depends_on` with safety checks."""

        # Validate pack name
        if not isinstance(pack, str) or not pack.strip():
            return {"error": "invalid_pack_name"}

        # Validate dependency name
        if not isinstance(depends_on, str) or not depends_on.strip():
            return {"error": "invalid_dependency_name"}

        # Prevent self-dependency
        if pack == depends_on:
            return {"error": "self_dependency_not_allowed"}

        # Ensure pack exists
        if pack not in self.graph:
            self.graph[pack] = []

        # Ensure dependency exists
        if depends_on not in self.graph:
            self.graph[depends_on] = []

        # Add dependency
        self.graph[pack].append(depends_on)

        return {"status": "dependency_added"}

    def get_dependencies(self, pack: str):
        """Returns all packs that the given pack depends on."""
        if not isinstance(pack, str):
            return []
        return self.graph.get(pack, [])

    # ---------------------------------------------------------
    # ORDER RESOLUTION
    # ---------------------------------------------------------

    def resolve_order(self):
        """
        Performs a topological sort to determine safe activation order.
        Returns a list of packs in correct order.
        Includes cycle detection and safety validation.
        """

        # Detect cycles first
        if self.has_cycles():
            return {"error": "cycle_detected"}

        visited = set()
        order = []

        def visit(node):
            if node in visited:
                return
            visited.add(node)

            deps = self.graph.get(node, [])
            if not isinstance(deps, list):
                raise ValueError("Invalid dependency list type.")

            for dep in deps:
                if not isinstance(dep, str) or not dep.strip():
                    raise ValueError("Invalid dependency name.")
                visit(dep)

            order.append(node)

        # Visit all nodes
        for pack in list(self.graph.keys()):
            visit(pack)

        return order

    # ---------------------------------------------------------
    # CYCLE DETECTION
    # ---------------------------------------------------------

    def has_cycles(self) -> bool:
        """
        Detects circular dependencies between packs.
        Includes safety validation.
        """

        visited = set()
        stack = set()

        def visit(node):
            if not isinstance(node, str) or not node.strip():
                return True  # invalid node = treat as unsafe

            if node in stack:
                return True

            if node in visited:
                return False

            visited.add(node)
            stack.add(node)

            deps = self.graph.get(node, [])
            if not isinstance(deps, list):
                return True  # invalid structure = unsafe

            for dep in deps:
                if visit(dep):
                    return True

            stack.remove(node)
            return False

        return any(visit(p) for p in self.graph)
