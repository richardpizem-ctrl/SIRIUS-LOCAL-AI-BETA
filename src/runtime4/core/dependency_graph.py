# dependency_graph.py
"""
SIRIUS LOCAL AI – Runtime 4.0 Dependency Graph

The Dependency Graph manages:
- module dependencies
- task execution order
- parallelization rules
- blocking constraints
- safe‑mode restrictions
- schoolwork priority overrides

This component ensures deterministic and safe execution flow.
"""


class DependencyGraph4:
    """
    Graph-based dependency manager for Runtime 4.0.
    Tracks relationships between modules and tasks.
    """

    def __init__(self):
        # Graph stored as adjacency list:
        # { "module": ["depends_on_A", "depends_on_B"] }
        self.graph = {}

    # ---------------------------------------------------------
    # GRAPH MANAGEMENT
    # ---------------------------------------------------------

    def add_module(self, name: str):
        """Registers a module in the dependency graph."""
        if name not in self.graph:
            self.graph[name] = []

    def add_dependency(self, module: str, depends_on: str):
        """
        Declares that `module` depends on `depends_on`.
        """
        if module not in self.graph:
            self.graph[module] = []
        self.graph[module].append(depends_on)

    def get_dependencies(self, module: str):
        """Returns all modules that the given module depends on."""
        return self.graph.get(module, [])

    # ---------------------------------------------------------
    # EXECUTION ORDER
    # ---------------------------------------------------------

    def resolve_order(self):
        """
        Performs a topological sort to determine safe execution order.
        Returns a list of modules in correct order.
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

        for module in self.graph:
            visit(module)

        return order

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    def has_cycles(self) -> bool:
        """
        Detects circular dependencies.
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

        return any(visit(m) for m in self.graph)
