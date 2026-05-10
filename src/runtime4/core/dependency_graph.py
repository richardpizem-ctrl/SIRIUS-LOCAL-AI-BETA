"""
SIRIUS LOCAL AI – Runtime 4.0 Dependency Graph

Responsible for:
- module dependencies
- task execution order
- parallelization rules
- blocking constraints
- safe‑mode restrictions
- schoolwork priority overrides

This component ensures deterministic and safe execution flow.
"""

from typing import Any, Dict, List


class DependencyGraph4:
    """
    Graph-based dependency manager for Runtime 4.0.
    Tracks relationships between modules and tasks.
    """

    def __init__(self, max_modules: int = 300):
        # Graph stored as adjacency list:
        # { "module": ["depends_on_A", "depends_on_B"] }
        self.graph: Dict[str, List[str]] = {}
        self.max_modules = max_modules

    # ---------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_name(self, name: Any) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_dependency(self, dep: Any) -> bool:
        return isinstance(dep, str) and dep.strip()

    def _validate_graph_integrity(self) -> bool:
        if not isinstance(self.graph, dict):
            return False
        for key, deps in self.graph.items():
            if not self._validate_name(key):
                return False
            if not isinstance(deps, list):
                return False
            for d in deps:
                if not self._validate_dependency(d):
                    return False
        return True

    # ---------------------------------------------------------
    # GRAPH MANAGEMENT
    # ---------------------------------------------------------

    def add_module(self, name: str):
        """Registers a module in the dependency graph with safety checks."""

        if not self._validate_name(name):
            return {"error": "invalid_module_name"}

        if len(self.graph) >= self.max_modules:
            return {"error": "module_limit_reached"}

        if name not in self.graph:
            self.graph[name] = []

        return {"status": "module_added"}

    def add_dependency(self, module: str, depends_on: str):
        """
        Declares that `module` depends on `depends_on`.
        Prevents duplicate dependencies and invalid names.
        """

        if not self._validate_name(module):
            return {"error": "invalid_module_name"}

        if not self._validate_dependency(depends_on):
            return {"error": "invalid_dependency_name"}

        # Prevent self-dependency
        if module == depends_on:
            return {"error": "self_dependency_not_allowed"}

        # Ensure module exists
        if module not in self.graph:
            self.graph[module] = []

        # Ensure dependency exists
        if depends_on not in self.graph:
            self.graph[depends_on] = []

        # Prevent duplicates
        if depends_on not in self.graph[module]:
            self.graph[module].append(depends_on)

        return {"status": "dependency_added"}

    def get_dependencies(self, module: str):
        """Returns all modules that the given module depends on."""
        if not self._validate_name(module):
            return []
        return self.graph.get(module, [])

    # ---------------------------------------------------------
    # EXECUTION ORDER
    # ---------------------------------------------------------

    def resolve_order(self):
        """
        Performs a topological sort to determine safe execution order.
        Includes cycle detection and graph integrity validation.
        """

        # Validate graph structure
        if not self._validate_graph_integrity():
            return {"error": "invalid_graph_structure"}

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
                raise ValueError("Invalid dependency list type")

            for dep in deps:
                if not self._validate_dependency(dep):
                    raise ValueError("Invalid dependency name")
                visit(dep)

            order.append(node)

        for module in list(self.graph.keys()):
            visit(module)

        return order

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    def has_cycles(self) -> bool:
        """
        Detects circular dependencies with full safety validation.
        """

        visited = set()
        stack = set()

        def visit(node):
            if not self._validate_name(node):
                return True  # invalid node = unsafe

            if node in stack:
                return True

            if node in visited:
                return False

            visited.add(node)
            stack.add(node)

            deps = self.graph.get(node, [])
            if not isinstance(deps, list):
                return True

            for dep in deps:
                if not self._validate_dependency(dep):
                    return True
                if visit(dep):
                    return True

            stack.remove(node)
            return False

        return any(visit(m) for m in self.graph)
