"""
SIRIUS LOCAL AI – Runtime 4.3 Dependency Graph

Responsible for:
- module dependencies
- task execution order
- parallelization rules
- blocking constraints
- safe‑mode restrictions
- schoolwork priority overrides

This component ensures deterministic, safe and Self‑Repair‑ready execution flow.
"""

from typing import Any, Dict, List


class DependencyGraph4:
    """
    Graph-based dependency manager for Runtime 4.3.
    Tracks relationships between modules and tasks.
    Provides:
    - strict validation
    - structured error surface
    - deterministic topological sorting
    - cycle diagnostics
    - safe-mode compatibility
    """

    def __init__(self, max_modules: int = 300):
        self.graph: Dict[str, List[str]] = {}
        self.max_modules = max_modules

    # ---------------------------------------------------------
    # VALIDATION HELPERS
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

    def add_module(self, name: str) -> Dict[str, Any]:
        """Registers a module in the dependency graph with safety checks."""

        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_module_name"}

        if len(self.graph) >= self.max_modules:
            return {"status": "error", "code": "module_limit_reached"}

        if name not in self.graph:
            self.graph[name] = []

        return {"status": "success", "module": name}

    def add_dependency(self, module: str, depends_on: str) -> Dict[str, Any]:
        """
        Declares that `module` depends on `depends_on`.
        Prevents duplicate dependencies and invalid names.
        """

        if not self._validate_name(module):
            return {"status": "error", "code": "invalid_module_name"}

        if not self._validate_dependency(depends_on):
            return {"status": "error", "code": "invalid_dependency_name"}

        if module == depends_on:
            return {"status": "error", "code": "self_dependency_not_allowed"}

        if module not in self.graph:
            self.graph[module] = []

        if depends_on not in self.graph:
            self.graph[depends_on] = []

        if depends_on not in self.graph[module]:
            self.graph[module].append(depends_on)

        return {"status": "success", "module": module, "depends_on": depends_on}

    def get_dependencies(self, module: str) -> List[str]:
        if not self._validate_name(module):
            return []
        return self.graph.get(module, [])

    # ---------------------------------------------------------
    # EXECUTION ORDER (TOPOLOGICAL SORT)
    # ---------------------------------------------------------

    def resolve_order(self) -> Dict[str, Any]:
        """
        Performs a topological sort to determine safe execution order.
        Returns structured result with telemetry and diagnostics.
        """

        # Validate graph structure
        if not self._validate_graph_integrity():
            return {"status": "error", "code": "invalid_graph_structure"}

        # Detect cycles
        cycle_info = self._detect_cycle_path()
        if cycle_info:
            return {
                "status": "error",
                "code": "cycle_detected",
                "cycle": cycle_info,
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

        for module in list(self.graph.keys()):
            visit(module)

        return {
            "status": "success",
            "order": order,
            "modules": len(order),
        }

    # ---------------------------------------------------------
    # CYCLE DETECTION WITH DIAGNOSTICS
    # ---------------------------------------------------------

    def _detect_cycle_path(self):
        """
        Returns the cycle path if a cycle exists, otherwise None.
        """

        visited = set()
        stack = []

        def visit(node):
            if node in stack:
                # Return cycle path
                cycle_start = stack.index(node)
                return stack[cycle_start:] + [node]

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

        for module in self.graph:
            result = visit(module)
            if result:
                return result

        return None
