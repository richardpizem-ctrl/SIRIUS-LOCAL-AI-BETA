"""
UI Actions Module – Runtime 4.2.0

Responsible for:
- executing UI actions (click, write, select…)
- semantic actions (open_settings, confirm, cancel…)
- safe invocation through the UI Sandbox
- integration with UI Parser and UI Graph

This module DOES NOT interact with the OS directly.
All actions must pass through the security layer (UI Sandbox).
"""

class UIActions:
    def __init__(self, sandbox=None):
        self.sandbox = sandbox
        self.last_log = []  # simple audit trail

    # ------------------------------------------------------------
    # INTERNAL LOGGING MECHANISM
    # ------------------------------------------------------------
    def _log(self, action_type, element=None, value=None, result=True):
        entry = {
            "action": action_type,
            "element": getattr(element, "name", element),
            "value": value,
            "result": result,
        }
        self.last_log.append(entry)
        return entry

    # ------------------------------------------------------------
    # PRIMARY UI ACTIONS
    # ------------------------------------------------------------
    def click(self, element):
        """
        Performs a click on a UI element.
        """
        if not self._allowed("click", element):
            self._log("click", element, result=False)
            return False

        # TODO: implement via ENVOY / WinCapabilities
        self._log("click", element, result=True)
        return True

    def write(self, element, text):
        """
        Writes text into a UI element.
        """
        if not self._allowed("write", element):
            self._log("write", element, value=text, result=False)
            return False

        # TODO: implement safe text input
        self._log("write", element, value=text, result=True)
        return True

    def select(self, element, option):
        """
        Selects an option from a menu or list.
        """
        if not self._allowed("select", element):
            self._log("select", element, value=option, result=False)
            return False

        # TODO: implement option selection
        self._log("select", element, value=option, result=True)
        return True

    def semantic(self, action_name, context=None):
        """
        Executes a semantic UI action:
        - open_settings
        - confirm
        - cancel
        - open_window
        - close_window
        """
        if not self._allowed("semantic", action_name):
            self._log("semantic", action_name, result=False)
            return False

        # TODO: implement semantic action mapping
        self._log("semantic", action_name, result=True)
        return True

    # ------------------------------------------------------------
    # SANDBOX CHECK
    # ------------------------------------------------------------
    def _allowed(self, action_type, target):
        """
        Checks whether the action is allowed by the UI Sandbox.
        """
        if self.sandbox:
            return self.sandbox.check_permission(action_type, target)
        return True
