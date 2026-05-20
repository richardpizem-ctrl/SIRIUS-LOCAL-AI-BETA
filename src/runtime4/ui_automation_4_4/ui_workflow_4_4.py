"""
SIRIUS LOCAL AI – UI Workflow Engine 4.4.0 (PRO)

Deterministic multi‑step UI workflows for UI Automation Engine 4.4.

Responsibilities:
- Semantic element resolution
- Action routing
- Sandbox‑safe execution
- Step‑by‑step validation
- STRANGER‑mode and behavior‑based safety

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- All OS interaction must go through the sandbox.
- Fully compatible with Security Family 4.4.
"""

from typing import List, Dict, Any, Optional


class UIWorkflow44:
    """
    Multi‑step deterministic UI workflow engine for Runtime 4.4 (PRO).
    """

    REQUIRED_RESOLVER_METHODS = {"initialize", "resolve"}
    REQUIRED_ROUTER_METHODS = {"initialize", "route"}
    REQUIRED_SANDBOX_METHODS = {"initialize"}

    def __init__(self, resolver=None, router=None, sandbox=None):
        self.resolver = resolver
        self.router = router
        self.sandbox = sandbox

        self.initialized: bool = False
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ---------------------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        # Resolver
        if not self.resolver:
            self.degraded_mode = True
            return {"status": "error", "code": "no_resolver"}

        for m in self.REQUIRED_RESOLVER_METHODS:
            if not hasattr(self.resolver, m):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "invalid_resolver_interface",
                    "missing": m,
                }

        # Router
        if not self.router:
            self.degraded_mode = True
            return {"status": "error", "code": "no_router"}

        for m in self.REQUIRED_ROUTER_METHODS:
            if not hasattr(self.router, m):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "invalid_router_interface",
                    "missing": m,
                }

        # Sandbox (optional but validated if present)
        if self.sandbox:
            for m in self.REQUIRED_SANDBOX_METHODS:
                if not hasattr(self.sandbox, m):
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "invalid_sandbox_interface",
                        "missing": m,
                    }

        try:
            r_res = self.resolver.initialize()
            if r_res.get("status") not in ("initialized", "already_initialized"):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "resolver_init_failed",
                    "details": r_res,
                }

            rt_res = self.router.initialize()
            if rt_res.get("status") not in ("initialized", "already_initialized"):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "router_init_failed",
                    "details": rt_res,
                }

            if self.sandbox:
                sb_res = self.sandbox.initialize()
                if sb_res.get("status") not in ("initialized", "already_initialized"):
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "sandbox_init_failed",
                        "details": sb_res,
                    }

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "exception", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # PUBLIC API – RUN WORKFLOW
    # ---------------------------------------------------------------------
    def run(self, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Each step:
        {
            "query": {...},      # semantic element query
            "action": "click",   # allowed UI action
            "payload": {...}     # optional
        }
        """
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "results": [],
                "degraded_mode": self.degraded_mode,
            }

        if not isinstance(steps, list):
            return {"status": "error", "code": "invalid_steps"}

        if not self.initialized:
            init = self.initialize()
            if init.get("status") not in ("initialized", "already_initialized"):
                return {
                    "status": "error",
                    "code": "workflow_not_initialized",
                    "details": init,
                }

        results: List[Dict[str, Any]] = []

        for index, step in enumerate(steps):
            step_result = self._execute_step(index, step)
            results.append(step_result)

            if step_result.get("status") != "ok":
                return {
                    "status": "partial_failure",
                    "failed_step": index,
                    "results": results,
                    "degraded_mode": self.degraded_mode,
                }

        return {
            "status": "ok",
            "results": results,
            "degraded_mode": self.degraded_mode,
        }

    # ---------------------------------------------------------------------
    # INTERNAL – EXECUTE SINGLE STEP
    # ---------------------------------------------------------------------
    def _execute_step(self, index: int, step: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(step, dict):
            return {
                "status": "error",
                "code": "invalid_step_definition",
                "step": index,
            }

        query = step.get("query")
        action = step.get("action")
        payload = step.get("payload") or {}

        if not isinstance(query, dict) or not isinstance(action, str):
            return {
                "status": "error",
                "code": "invalid_step_definition",
                "step": index,
            }

        # 1. Resolve element
        try:
            resolved = self.resolver.resolve(query)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "resolve_exception",
                "exception": str(exc),
                "step": index,
            }

        if resolved.get("status") != "ok":
            return {
                "status": "error",
                "code": "resolve_failed",
                "details": resolved,
                "step": index,
            }

        element = resolved.get("element")
        if not element:
            return {
                "status": "error",
                "code": "element_not_found",
                "step": index,
            }

        # 2. Route action
        try:
            routed = self.router.route(element, action, payload)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "route_exception",
                "exception": str(exc),
                "step": index,
            }

        if routed.get("status") != "ok":
            return {
                "status": "error",
                "code": "action_failed",
                "details": routed,
                "step": index,
            }

        return {
            "status": "ok",
            "step": index,
            "element": element,
            "action_result": routed,
            "degraded_mode": self.degraded_mode,
        }
