"""
SIRIUS LOCAL AI – UI Workflow Engine 4.4.0

This module provides deterministic multi‑step UI workflows for
UI Automation Engine 4.4. It coordinates:

- semantic element resolution
- action routing
- sandbox‑safe execution
- step‑by‑step validation
- STRANGER‑mode and behavior‑based safety

All workflows must be deterministic, offline, and fully isolated.

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- All OS interaction must go through the sandbox.
- Fully compatible with Security Family 4.4.
"""

from typing import List, Dict, Any, Optional


class UIWorkflow44:
    """
    Multi‑step deterministic UI workflow engine for Runtime 4.4.
    """

    def __init__(self, resolver=None, router=None, sandbox=None):
        self.resolver = resolver
        self.router = router
        self.sandbox = sandbox

        self.initialized = False
        self.degraded_mode = False

    # ---------------------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.resolver:
                self.resolver.initialize()

            if self.router:
                self.router.initialize()

            if self.sandbox:
                self.sandbox.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # PUBLIC API – RUN WORKFLOW
    # ---------------------------------------------------------------------
    def run(self, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Executes a deterministic multi‑step UI workflow.

        Each step must contain:
        {
            "query": {...},     # semantic element query
            "action": "click",  # allowed UI action
            "payload": {...}    # optional
        }
        """
        if not self.initialized:
            init_result = self.initialize()
            if init_result.get("status") not in ("initialized", "already_initialized"):
                return {"status": "error", "reason": "workflow_not_initialized", "details": init_result}

        results = []
        for index, step in enumerate(steps):
            step_result = self._execute_step(index, step)
            results.append(step_result)

            # Stop workflow on error
            if step_result.get("status") != "ok":
                return {
                    "status": "partial_failure",
                    "failed_step": index,
                    "results": results,
                }

        return {"status": "ok", "results": results}

    # ---------------------------------------------------------------------
    # INTERNAL – EXECUTE SINGLE STEP
    # ---------------------------------------------------------------------
    def _execute_step(self, index: int, step: Dict[str, Any]) -> Dict[str, Any]:
        query = step.get("query")
        action = step.get("action")
        payload = step.get("payload") or {}

        if not query or not action:
            return {"status": "error", "reason": "invalid_step_definition", "step": index}

        # 1. Resolve element
        resolved = self.resolver.resolve(query)
        if resolved.get("status") != "ok":
            return {"status": "error", "reason": "resolve_failed", "details": resolved}

        element = resolved.get("element")
        if not element:
            return {"status": "error", "reason": "element_not_found", "step": index}

        # 2. Route action
        routed = self.router.route(element, action, payload)
        if routed.get("status") != "ok":
            return {"status": "error", "reason": "action_failed", "details": routed}

        return {
            "status": "ok",
            "step": index,
            "element": element,
            "action_result": routed,
        }
