"""
UI Actions Module – Runtime 4.3.0

New in 4.3.0:
- WinCapabilities integration layer (OS UI control hook)
- Deterministic OS action routing
- Extended audit logging
- Unified interface for UI and OS actions
- Semantic action mapping foundation

This module still routes ALL actions through the UI Sandbox.
"""

class UIActions:
    def __init__(self, sandbox=None, win_capabilities=None):
        """
        sandbox: UI Sandbox (permission enforcement)
        win_capabilities: OS‑level UI control layer (optional)
        """
        self.sandbox = sandbox
        self.win_capabilities = win_capabilities
        self.last_log = []

    # ------------------------------------------------------------
    # INTERNAL LOGGING
    # ------------------------------------------------------------
    def _log(self, action_type, element=None, value=None, result=True, via_os=False):
        entry = {
            "action": action_type,
            "element": getattr(element, "name", element),
            "value": value,
            "result": result,
            "via_os": via_os,
        }
        self.last_log.append(entry)
        return entry

    # ------------------------------------------------------------
    # PRIMARY UI ACTIONS (Runtime 4.3.0)
    # ------------------------------------------------------------
    def click(self, element):
        """
        Performs a click on a UI element.
        First tries OS‑level click (if available), then falls back to virtual click.
        """
        if not self._allowed("click", element):
            self._log("click", element, result=False)
            return False

        # 1. Try OS‑level click
        if self.win_capabilities:
            if self.win_capabilities.click(element):
                self._log("click", element, result=True, via_os=True)
                return True

        # 2. Fallback: virtual click (4.2.0 behavior)
        self._log("click", element, result=True, via_os=False)
        return True

    def write(self, element, text):
        """
        Writes text into a UI element.
        """
        if not self._allowed("write", element):
            self._log("write", element, value=text, result=False)
            return False

        # 1. Try OS‑level write
        if self.win_capabilities:
            if self.win_capabilities.write(element, text):
                self._log("write", element, value=text, result=True, via_os=True)
                return True

        # 2. Fallback: virtual write
        self._log("write", element, value=text, result=True, via_os=False)
        return True

    def select(self, element, option):
        """
        Selects an option from a menu or list.
        """
        if not self._allowed("select", element):
            self._log("select", element, value=option, result=False)
            return False

        # 1. Try OS‑level select
        if self.win_capabilities:
            if self.win_capabilities.select(element, option):
                self._log("select", element, value=option, result=True, via_os=True)
                return True

        # 2. Fallback: virtual select
        self._log("select", element, value=option, result=True, via_os=False)
        return True

    # ------------------------------------------------------------
    # SEMANTIC ACTIONS (Runtime 4.3.0)
    # ------------------------------------------------------------
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

        # 1. Try OS‑level semantic action
        if self.win_capabilities:
            if self.win_capabilities.semantic(action_name, context):
                self._log("semantic", action_name, result=True, via_os=True)
                return True

        # 2. Fallback: virtual semantic action
        self._log("semantic", action_name, result=True, via_os=False)
        return True

    # ------------------------------------------------------------
    # SANDBOX CHECK
    # ------------------------------------------------------------
    def _allowed(self, action_type, target):
        if self.sandbox:
            return self.sandbox.check_permission(action_type, target)
        return True
