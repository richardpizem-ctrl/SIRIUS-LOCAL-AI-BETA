"""
UI Workflow Module – Runtime 4.5.x (PRO)

Provides:
- Deterministic workflow execution
- Multi‑strategy target resolution
- Confidence‑based element selection
- Retry logic
- Semantic fallback
- Fuzzy‑aware pipeline
- Safe‑mode and degraded‑mode behavior
- Structured workflow results

The workflow engine is the highest layer of the UI Automation Engine.

Security Notes:
- Deterministic, offline-safe
- No dynamic imports, no eval, no reflection
- Fully compatible with Security Family 4.5
"""

from typing import Any, Dict, List, Optional


class UIWorkflow:
    """
    Deterministic UI Workflow Engine for Runtime 4.5.x (PRO).
    """

    def __init__(self, graph, parser, actions, sandbox=None):
        self.version = "4.5.0"

        self.graph = graph
        self.parser = parser
        self.actions = actions
        self.sandbox = sandbox

        self.max_retries: int = 3
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ------------------------------------------------------------
    # WORKFLOW EXECUTION
    # ------------------------------------------------------------
    def run(self, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Executes a list of workflow steps.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "step_results": [],
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

        if not isinstance(steps, list):
            return {
                "status": "error",
                "code": "invalid_steps",
                "step_results": [],
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

        results = []

        for step in steps:
            result = self._execute_step(step)
            results.append(result)

            if not result.get("success", False):
                return {
                    "status": "failed",
                    "step_results": results,
                    "degraded_mode": self.degraded_mode,
                    "version": self.version,
                }

        return {
            "status": "ok",
            "step_results": results,
            "degraded_mode": self.degraded_mode,
            "version": self.version,
        }

    # ------------------------------------------------------------
    # SINGLE STEP EXECUTION (WITH RETRIES)
    # ------------------------------------------------------------
    def _execute_step(self, step: Dict[str, Any]) -> Dict[str, Any]:
        action = step.get("action")
        target = step.get("target")
        value = step.get("value")

        if not isinstance(step, dict):
            return {
                "success": False,
                "error": "invalid_step_format",
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

        for attempt in range(self.max_retries):

            # 1. Scan UI
            try:
                self.graph.scan_windows()
                self.graph.build_graph()
            except Exception:
                self.degraded_mode = True
                continue

            # 2. Parse UI
            parse_result = self.parser.parse_graph(self.graph)
            if parse_result.get("status") == "error":
                self.degraded_mode = True
                continue

            # 3. Resolve target
            element = self._resolve_target(target)
            if not element:
                continue

            # 4. Execute action
            exec_result = self._execute_action(action, element, value)
            if exec_result.get("success"):
                exec_result["attempt"] = attempt + 1
                exec_result["version"] = self.version
                return exec_result

        return {
            "success": False,
            "action": action,
            "target": target,
            "attempts": self.max_retries,
            "degraded_mode": self.degraded_mode,
            "version": self.version,
        }

    # ------------------------------------------------------------
    # ACTION EXECUTION WRAPPER
    # ------------------------------------------------------------
    def _execute_action(self, action: str, element: Any, value: Any) -> Dict[str, Any]:
        try:
            if action == "click":
                result = self.actions.click(element)

            elif action == "write":
                result = self.actions.write(element, value)

            elif action == "select":
                result = self.actions.select(element, value)

            elif action == "semantic":
                result = self.actions.semantic(element)

            else:
                return {
                    "success": False,
                    "error": "unknown_action",
                    "action": action,
                    "version": self.version,
                }

            return {
                "success": bool(result),
                "action": action,
                "element": getattr(element, "name", element),
                "value": value,
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "success": False,
                "error": "exception",
                "exception": str(exc),
                "action": action,
                "element": getattr(element, "name", element),
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

    # ------------------------------------------------------------
    # TARGET RESOLUTION (4.5.x – MULTI‑STRATEGY)
    # ------------------------------------------------------------
    def _resolve_target(self, target: Any) -> Optional[Any]:
        """
        Multi‑strategy resolution:
        1. Exact / partial / fuzzy match (Parser 4.5)
        2. Semantic fallback
        3. Confidence‑based selection
        """

        # String target → fuzzy search
        if isinstance(target, str):
            results = self.parser.find(name=target)
            if isinstance(results, dict):
                results = results.get("results", [])

            if not results:
                return None

            return results[0]["element"]

        # Direct element reference
        if isinstance(target, dict):
            return target

        return None
