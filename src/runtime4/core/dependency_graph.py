"""
SIRIUS LOCAL AI – Runtime 4.4 Scheduler Manager

Responsible for:
- executing modules in dependency‑safe order
- integrating with DependencyGraph4
- integrating with SandboxManager4
- enforcing safe‑mode and degraded‑mode rules
- providing deterministic scheduling
- exposing telemetry for RuntimeEngine 4.4
- supporting Self‑Repair Layer 4.4 diagnostics
"""

from typing import Dict, Any


class SchedulerManager4:
    """
    Deterministic scheduler for Runtime 4.4.
    - Stable structured return values
    - Safe‑mode aware
    - Degraded‑mode propagation
    """

    def __init__(self, dependency_graph, sandbox_manager):
        self.graph = dependency_graph
        self.sandbox = sandbox_manager
        self.degraded_mode = False
        self.safe_mode = False

    # ---------------------------------------------------------
    # EXECUTION PIPELINE
    # ---------------------------------------------------------
    def execute_all(self, modules: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes all modules in dependency‑safe order.
        Returns structured telemetry and degraded‑mode status.
        """

        # SAFE MODE
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Scheduler disabled in safe‑mode.",
                "order": [],
                "results": {},
                "errors": [],
                "degraded_mode": False,
            }

        # Resolve dependency order
        order_result = self.graph.resolve_order()

        if order_result.get("status") == "error":
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "dependency_resolution_failed",
                "details": order_result,
                "order": [],
                "results": {},
                "errors": [],
                "degraded_mode": True,
            }

        order = order_result.get("order", [])
        results: Dict[str, Any] = {}
        errors: list[str] = []

        # Execute modules in order
        for module_name in order:
            module = modules.get(module_name)

            if not module:
                results[module_name] = {
                    "status": "error",
                    "code": "module_not_found",
                }
                errors.append(module_name)
                continue

            # Ensure sandbox exists
            ctx = self.sandbox.get_context(module_name)
            if ctx is None:
                results[module_name] = {
                    "status": "error",
                    "code": "sandbox_missing",
                }
                errors.append(module_name)
                continue

            # Execute module
            try:
                instance = module.get("instance", module)
                if hasattr(instance, "start") and callable(instance.start):
                    start_res = instance.start()
                    if isinstance(start_res, dict) and start_res.get("status") == "error":
                        results[module_name] = {
                            "status": "error",
                            "code": "execution_failed",
                            "details": start_res,
                        }
                        errors.append(module_name)
                    else:
                        results[module_name] = {"status": "executed"}
                else:
                    results[module_name] = {
                        "status": "skipped",
                        "reason": "no_start_method",
                    }
            except Exception as exc:
                results[module_name] = {
                    "status": "error",
                    "code": "execution_exception",
                    "exception": str(exc),
                }
                errors.append(module_name)

        self.degraded_mode = bool(errors)

        return {
            "status": "degraded" if errors else "success",
            "order": order,
            "results": results,
            "errors": errors,
            "degraded_mode": self.degraded_mode,
        }
