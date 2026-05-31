"""
SIRIUS Runtime 5.1.0 – Runtime Integrity Engine 1.0
Dependency Graph Validator

Účel:
- validovať závislostný graf modulov
- detegovať cykly, chýbajúce moduly, neplatné odkazy
- poskytovať Self‑Repair Layeru presné diagnostické dáta
"""

from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class DependencyValidationResult:
    module: str
    ok: bool
    missing: List[str]
    cycles: List[List[str]]
    invalid: List[str]
    details: Dict[str, Any]


class DependencyGraphValidator:
    """
    Validator pre DependencyGraph (Runtime 4.x aj 5.x).

    Očakáva graf vo formáte:
    {
        "moduleA": ["moduleB", "moduleC"],
        "moduleB": [],
        ...
    }
    """

    def __init__(self, logger):
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def validate(self, graph: Dict[str, List[str]], module: str) -> DependencyValidationResult:
        """
        Validuje závislosti pre jeden modul.
        """
        self.logger.info(
            "DependencyGraphValidator: validating module",
            extra={"module": module}
        )

        if module not in graph:
            return DependencyValidationResult(
                module=module,
                ok=False,
                missing=[],
                cycles=[],
                invalid=[module],
                details={"reason": "module_not_in_graph"}
            )

        deps = graph.get(module, [])

        missing = self._find_missing(graph, deps)
        cycles = self._find_cycles(graph, module)
        invalid = self._find_invalid(graph, deps)

        ok = not missing and not cycles and not invalid

        self.logger.info(
            "DependencyGraphValidator: validation finished",
            extra={
                "module": module,
                "ok": ok,
                "missing": len(missing),
                "cycles": len(cycles),
                "invalid": len(invalid)
            }
        )

        return DependencyValidationResult(
            module=module,
            ok=ok,
            missing=missing,
            cycles=cycles,
            invalid=invalid,
            details={}
        )

    # ---------------------------------------------------------
    # INTERNAL CHECKS
    # ---------------------------------------------------------

    def _find_missing(self, graph: Dict[str, List[str]], deps: List[str]) -> List[str]:
        """
        Nájde závislosti, ktoré v grafe neexistujú.
        """
        return [d for d in deps if d not in graph]

    def _find_invalid(self, graph: Dict[str, List[str]], deps: List[str]) -> List[str]:
        """
        Nájde neplatné názvy modulov (prázdne, None, whitespace).
        """
        invalid = []
        for d in deps:
            if not isinstance(d, str) or not d.strip():
                invalid.append(d)
        return invalid

    def _find_cycles(self, graph: Dict[str, List[str]], start: str) -> List[List[str]]:
        """
        Deteguje cykly pomocou DFS.
        Výstup: zoznam cyklov (každý cyklus je zoznam modulov).
        """
        visited = set()
        stack = []

        cycles = []

        def dfs(node: str):
            if node in stack:
                # cyklus = časť stacku od prvého výskytu node
                idx = stack.index(node)
                cycles.append(stack[idx:] + [node])
                return

            if node in visited:
                return

            visited.add(node)
            stack.append(node)

            for dep in graph.get(node, []):
                dfs(dep)

            stack.pop()

        dfs(start)
        return cycles
