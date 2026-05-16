"""
UI Workflow Module – Runtime 4.2.0

Zodpovedá za:
- deterministické UI sekvencie
- krokové workflowy (scan → parse → find → act)
- fallback mechanizmy pri zlyhaní UI akcie
- integráciu s UI Graph, UI Parser, UI Actions a UI Sandbox

Workflow je najvyššia vrstva UI Automation Engine.
"""

class UIWorkflow:
    def __init__(self, graph, parser, actions, sandbox=None):
        """
        graph: UIGraph
        parser: UIParser
        actions: UIActions
        sandbox: UISandbox (voliteľné)
        """
        self.graph = graph
        self.parser = parser
        self.actions = actions
        self.sandbox = sandbox

    def run(self, steps):
        """
        Spustí workflow definovaný ako zoznam krokov.
        Každý krok je dict:
        {
            "action": "click" | "write" | "select" | "semantic",
            "target": "OK" | "Cancel" | {...},
            "value": voliteľné (napr. text pre write)
        }
        """
        for step in steps:
            if not self._execute_step(step):
                return False  # workflow zlyhal
        return True  # workflow úspešný

    def _execute_step(self, step):
        """
        Vykoná jeden krok workflowu.
        """
        action = step.get("action")
        target = step.get("target")
        value = step.get("value")

        # 1. Naskenovať UI
        self.graph.scan_windows()
        self.graph.build_graph()

        # 2. Naparsovať UI
        self.parser.parse_graph(self.graph)

        # 3. Nájsť cieľový prvok
        element = self._resolve_target(target)

        if not element:
            return False

        # 4. Vykonať akciu
        if action == "click":
            return self.actions.click(element)

        if action == "write":
            return self.actions.write(element, value)

        if action == "select":
            return self.actions.select(element, value)

        if action == "semantic":
            return self.actions.semantic(target)

        return False

    def _resolve_target(self, target):
        """
        Preloží názov alebo štruktúru cieľa na UI prvok.
        """
        if isinstance(target, str):
            results = self.parser.find(name=target)
            return results[0] if results else None

        if isinstance(target, dict):
            # budúce rozšírenie pre komplexné dotazy
            return target

        return None


# ------------------------------------------------------------
# DEMO WORKFLOW – prvý vertikálny rez UI Automation Engine
# ------------------------------------------------------------

def demo_ok_click_workflow():
    """
    Jednoduchý demo workflow, ktorý prejde celým UI Automation Engine.
    Používa fake UI strom z UIGraph.
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
