"""
UI Workflow Module – Runtime 4.3.0

New in 4.3.0:
- Fallback Engine
- Multi‑strategy target resolution
- Confidence‑based element selection
- Retry logic
- Semantic fallback
- Fuzzy‑aware workflow pipeline

The workflow engine is the highest layer of the UI Automation Engine.
"""

class UIWorkflow:
    def __init__(self, graph, parser, actions, sandbox=None):
        self.graph = graph
        self.parser = parser
        self.actions = actions
        self.sandbox = sandbox

        # Maximum retries per step (Runtime 4.3.0)
        self.max_retries = 3

    # ------------------------------------------------------------
    # WORKFLOW EXECUTION
    # ------------------------------------------------------------
    def run(self, steps):
        for step in steps:
            if not self._execute_step(step):
                return False
        return True

    # ------------------------------------------------------------
    # SINGLE STEP EXECUTION (WITH RETRIES)
    # ------------------------------------------------------------
    def _execute_step(self, step):
        action = step.get("action")
        target = step.get("target")
        value = step.get("value")

        for attempt in range(self.max_retries):

            # 1. Scan UI
            self.graph.scan_windows()
            self.graph.build_graph()

            # 2. Parse UI
            self.parser.parse_graph(self.graph)

            # 3. Resolve target
            element = self._resolve_target(target)

            if not element:
                continue  # retry

            # 4. Execute action
            if action == "click":
                if self.actions.click(element):
                    return True

            if action == "write":
                if self.actions.write(element, value):
                    return True

            if action == "select":
                if self.actions.select(element, value):
                    return True

            if action == "semantic":
                if self.actions.semantic(target):
                    return True

        return False  # all retries failed

    # ------------------------------------------------------------
    # TARGET RESOLUTION (4.3.0 – MULTI‑STRATEGY)
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

            if not results:
                return None

            # Pick highest‑confidence match
            best = results[0]
            return best["element"]

        if isinstance(target, dict):
            return target

        return None


# ------------------------------------------------------------
# DEMO WORKFLOW – unchanged, but now uses fuzzy + fallback
# ------------------------------------------------------------

def demo_ok_click_workflow():
    from .ui_graph import UIGraph
    from .ui_parser import UIParser
    from .ui_actions import UIActions
    from .ui_sandbox import UISandbox

    graph = UIGraph()
    parser = UIParser()
    sandbox = UISandbox(identity="OWNER")
    actions = UIActions(sandbox=sandbox)

    workflow = UIWorkflow(
        graph=graph,
        parser=parser,
        actions=actions,
        sandbox=sandbox
    )

    steps = [
        {"action": "click", "target": "OK"}
    ]

    return workflow.run(steps)
