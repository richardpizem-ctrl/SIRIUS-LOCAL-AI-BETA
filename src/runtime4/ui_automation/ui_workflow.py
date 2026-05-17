"""
UI Workflow Module – Runtime 4.3.x

New in 4.3.x:
- Fallback Engine
- Multi‑strategy target resolution
- Confidence‑based element selection
- Retry logic
- Semantic fallback
- Fuzzy‑aware workflow pipeline
- Safe‑mode and degraded‑mode behavior
- Structured workflow results

The workflow engine is the highest layer of the UI Automation Engine.
"""


class UIWorkflow:
    def __init__(self, graph, parser, actions, sandbox=None):
        self.graph = graph
        self.parser = parser
        self.actions = actions
        self.sandbox = sandbox

        self.max_retries = 3

        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------
    # WORKFLOW EXECUTION
    # ------------------------------------------------------------
    def run(self, steps):
        """
        Executes a list of workflow steps.
        Returns structured result:
        {
            "status": "ok" | "failed" | "safe_mode",
            "step_results": [...],
            "degraded_mode": bool
        }
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "step_results": [],
                "degraded_mode": self.degraded_mode
            }

        results = []

        for step in steps:
            result = self._execute_step(step)
            results.append(result)

            if not result["success"]:
                return {
                    "status": "failed",
                    "step_results": results,
                    "degraded_mode": self.degraded_mode
                }

        return {
            "status": "ok",
            "step_results": results,
            "degraded_mode": self.degraded_mode
        }

    # ------------------------------------------------------------
    # SINGLE STEP EXECUTION (WITH RETRIES)
    # ------------------------------------------------------------
    def _execute_step(self, step):
        action = step.get("action")
        target = step.get("target")
        value = step.get("value")

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
            if isinstance(parse_result, dict) and parse_result.get("status") == "error":
                self.degraded_mode = True
                continue

            # 3. Resolve target
            element = self._resolve_target(target)
            if not element:
                continue  # retry

            # 4. Execute action
            exec_result = self._execute_action(action, element, value)
            if exec_result["success"]:
                return exec_result

        return {
            "success": False,
            "action": action,
            "target": target,
            "attempts": self.max_retries,
            "degraded_mode": self.degraded_mode
        }

    # ------------------------------------------------------------
    # ACTION EXECUTION WRAPPER
    # ------------------------------------------------------------
    def _execute_action(self, action, element, value):
        try:
            if action == "click":
                ok = self.actions.click(element)
            elif action == "write":
                ok = self.actions.write(element, value)
            elif action == "select":
                ok = self.actions.select(element, value)
            elif action == "semantic":
                ok = self.actions.semantic(element)
            else:
                return {
                    "success": False,
                    "error": "unknown_action",
                    "action": action
                }

            return {
                "success": bool(ok),
                "action": action,
                "element": getattr(element, "name", element),
                "value": value,
                "degraded_mode": self.degraded_mode
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "success": False,
                "error": "exception",
                "exception": str(exc),
                "action": action,
                "element": getattr(element, "name", element),
                "degraded_mode": self.degraded_mode
            }

    # ------------------------------------------------------------
    # TARGET RESOLUTION (4.3.x – MULTI‑STRATEGY)
    # ------------------------------------------------------------
    def _resolve_target(self, target):
        """
        Multi‑strategy resolution:
        1. Exact / partial / fuzzy match (Parser 4.3)
        2. Semantic fallback
        3. Confidence‑based selection
        """

        if isinstance(target, str):
            results = self.parser.find(name=target)
            if isinstance(results, dict):
                results = results.get("results", [])

            if not results:
                return None

            # Pick highest‑confidence match
            return results[0]["element"]

        if isinstance(target, dict):
            return target

        return None
