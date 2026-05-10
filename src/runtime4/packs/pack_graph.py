# pack_graph.py
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
        """Registers a pack in the graph."""
        if name not in self.graph:
            self.graph[name] = []

    def add_dependency(self, pack: str, depends_on: str):
        """Declares that `pack` depends on `depends_on`."""
        if pack not in self.graph:
            self.graph[pack] = []
        self.graph[pack].append(depends_on)

    def get_dependencies(self, pack: str):
        """Returns all packs that the given pack depends on."""
        return self.graph.get(pack, [])

    # ---------------------------------------------------------
    # ORDER RESOLUTION
    # ---------------------------------------------------------

    def resolve_order(self):
        """
        Performs a topological sort to determine safe activation order.
        Returns a list of packs in correct order.
        """
        visited = set()
        order = []

        def visit(node):
            if node in visited:
                return
            visited.add(node)
            for dep in self.graph.get(node, []):
                visit(dep)
            order.append(node)

        for pack in self.graph:
            visit(pack)

        return order

    # ---------------------------------------------------------
    # CYCLE DETECTION
    # ---------------------------------------------------------

    def has_cycles(self) -> bool:
        """
        Detects circular dependencies between packs.
        """
        visited = set()
        stack = set()

        def visit(node):
            if node in stack:
                return True
            if node in visited:
                return False

            visited.add(node)
            stack.add(node)

            for dep in self.graph.get(node, []):
                if visit(dep):
                    return True

            stack.remove(node)
            return False

        return any(visit(p) for p in self.graph)
