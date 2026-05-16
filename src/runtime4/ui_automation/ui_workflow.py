"""
UI Workflow Module – Runtime 4.2.0

Responsible for:
- deterministic UI sequences
- step‑based workflows (scan → parse → find → act)
- fallback mechanisms when UI actions fail
- integration with UI Graph, UI Parser, UI Actions and UI Sandbox

The workflow engine is the highest layer of the UI Automation Engine.
"""

class UIWorkflow:
    def __init__(self, graph, parser, actions, sandbox=None):
        """
        graph:   UIGraph
        parser:  UIParser
        actions: UIActions
        sandbox: UISandbox (optional)
        """
        self.graph = graph
        self.parser = parser
        self.actions = actions
        self.sandbox = sandbox

    # ------------------------------------------------------------
    # WORKFLOW EXECUTION
    # ------------------------------------------------------------
    def run(self, steps):
        """
        Executes a workflow defined as a list of steps.

        Each step is a dict:
        {
            "action": "click" | "write" | "select" | "semantic",
            "target": "OK" | "Cancel" | {...},
            "value": optional (e.g., text for write)
        }
        """
        for step in steps:
            if not self._execute_step(step):
                return False  # workflow failed
        return True  # workflow succeeded

    # ------------------------------------------------------------
    # SINGLE STEP EXECUTION
    # ------------------------------------------------------------
    def _execute_step(self, step):
        """
        Executes a single workflow step.
        """
        action = step.get("action")
        target = step.get("target")
        value = step.get("value")

        # 1. Scan UI
        self.graph.scan_windows()
        self.graph.build_graph()

        # 2. Parse UI
        self.parser.parse_graph(self.graph)

        # 3. Resolve target element
        element = self._resolve_target(target)
        if not element:
            return False

        # 4. Execute action
        if action == "click":
            return self.actions.click(element)

        if action == "write":
            return self.actions.write(element, value)

        if action == "select":
            return self.actions.select(element, value)

        if action == "semantic":
            return self.actions.semantic(target)

        return False

    # ------------------------------------------------------------
    # TARGET RESOLUTION
    # ------------------------------------------------------------
    def _resolve_target(self, target):
        """
        Resolves a target name or structure into a UI element.
        """
        if isinstance(target, str):
            results = self.parser.find(name=target)
            return results[0] if results else None

        if isinstance(target, dict):
            # future extension for complex queries
            return target

        return None


# ------------------------------------------------------------
# DEMO WORKFLOW – first vertical slice of the UI Automation Engine
# ------------------------------------------------------------

def demo_ok_click_workflow():
    """
    Simple demo workflow that runs through the entire UI Automation Engine.
    Uses fake UI elements from UIGraph.
    """
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
