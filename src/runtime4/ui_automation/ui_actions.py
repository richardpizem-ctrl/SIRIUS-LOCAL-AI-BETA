"""
UI Actions Module – Runtime 4.3.1

New in 4.3.x:
- WinCapabilities integration layer (OS UI control hook)
- Deterministic OS action routing
- Extended audit logging
- Unified interface for UI and OS actions
- Semantic action mapping foundation
- Safe-mode and degraded-mode behavior
- Structured, deterministic result surface

All actions are ALWAYS routed through the UI Sandbox when present.
"""

from typing import Any, Dict, List, Optional


class UIActions:
    def __init__(self, sandbox=None, win_capabilities=None):
        """
        sandbox: UI Sandbox (permission enforcement, must expose check_permission)
        win_capabilities: OS‑level UI control layer (optional, click/write/select/semantic)
        """
        self.sandbox = sandbox
        self.win_capabilities = win_capabilities
        self.last_log: List[Dict[str, Any]] = []

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ------------------------------------------------------------
    # INTERNAL LOGGING
    # ------------------------------------------------------------
    def _log(
        self,
        action_type: str,
        element: Any = None,
        value: Any = None,
        result: bool = True,
        via_os: bool = False,
        error_code: Optional[str] = None,
    ) -> Dict[str, Any]:
        entry = {
            "action": action_type,
            "element": getattr(element, "name", element),
            "value": value,
            "result": result,
            "via_os": via_os,
            "error": error_code,
            "degraded_mode": self.degraded_mode,
        }
        self.last_log.append(entry)
        return entry

    # ------------------------------------------------------------
    # SANDBOX CHECK
    # ------------------------------------------------------------
    def _allowed(self, action_type: str, target: Any) -> bool:
        if self.safe_mode:
            return False
        if self.sandbox and hasattr(self.sandbox, "check_permission"):
            try:
                return bool(self.sandbox.check_permission(action_type, target))
            except Exception:
                self.degraded_mode = True
                return False
        return True

    # ------------------------------------------------------------
    # PRIMARY UI ACTIONS (Runtime 4.3.x)
    # ------------------------------------------------------------
    def click(self, element: Any) -> Dict[str, Any]:
        """
        Performs a click on a UI element.
        First tries OS‑level click (if available), then falls back to virtual click.
        """

        if self.safe_mode:
            return self._log("click", element, result=False, error_code="safe_mode")

        if not self._allowed("click", element):
            return self._log("click", element, result=False, error_code="permission_denied")

        # 1. Try OS‑level click
        if self.win_capabilities and hasattr(self.win_capabilities, "click"):
            try:
                if self.win_capabilities.click(element):
                    return self._log("click", element, result=True, via_os=True)
            except Exception:
                self.degraded_mode = True
                return self._log("click", element, result=False, via_os=True, error_code="os_click_failed")

        # 2. Fallback: virtual click
        return self._log("click", element, result=True, via_os=False)

    def write(self, element: Any, text: str) -> Dict[str, Any]:
        """
        Writes text into a UI element.
        """

        if self.safe_mode:
            return self._log("write", element, value=text, result=False, error_code="safe_mode")

        if not isinstance(text, str):
            return self._log("write", element, value=text, result=False, error_code="invalid_text_type")

        if not self._allowed("write", element):
            return self._log("write", element, value=text, result=False, error_code="permission_denied")

        # 1. Try OS‑level write
        if self.win_capabilities and hasattr(self.win_capabilities, "write"):
            try:
                if self.win_capabilities.write(element, text):
                    return self._log("write", element, value=text, result=True, via_os=True)
            except Exception:
                self.degraded_mode = True
                return self._log("write", element, value=text, result=False, via_os=True, error_code="os_write_failed")

        # 2. Fallback: virtual write
        return self._log("write", element, value=text, result=True, via_os=False)

    def select(self, element: Any, option: Any) -> Dict[str, Any]:
        """
        Selects an option from a menu or list.
        """

        if self.safe_mode:
            return self._log("select", element, value=option, result=False, error_code="safe_mode")

        if not self._allowed("select", element):
            return self._log("select", element, value=option, result=False, error_code="permission_denied")

        # 1. Try OS‑level select
        if self.win_capabilities and hasattr(self.win_capabilities, "select"):
            try:
                if self.win_capabilities.select(element, option):
                    return self._log("select", element, value=option, result=True, via_os=True)
            except Exception:
                self.degraded_mode = True
                return self._log("select", element, value=option, result=False, via_os=True, error_code="os_select_failed")

        # 2. Fallback: virtual select
        return self._log("select", element, value=option, result=True, via_os=False)

    # ------------------------------------------------------------
    # SEMANTIC ACTIONS (Runtime 4.3.x)
    # ------------------------------------------------------------
    def semantic(self, action_name: str, context: Optional[dict] = None) -> Dict[str, Any]:
        """
        Executes a semantic UI action:
        - open_settings
        - confirm
        - cancel
        - open_window
        - close_window
        """

        if self.safe_mode:
            return self._log("semantic", action_name, result=False, error_code="safe_mode")

        if not isinstance(action_name, str) or not action_name.strip():
            return self._log("semantic", action_name, result=False, error_code="invalid_action_name")

        if context is not None and not isinstance(context, dict):
            return self._log("semantic", action_name, value=context, result=False, error_code="invalid_context_type")

        if not self._allowed("semantic", action_name):
            return self._log("semantic", action_name, result=False, error_code="permission_denied")

        # 1. Try OS‑level semantic action
        if self.win_capabilities and hasattr(self.win_capabilities, "semantic"):
            try:
                if self.win_capabilities.semantic(action_name, context):
                    return self._log("semantic", action_name, result=True, via_os=True)
            except Exception:
                self.degraded_mode = True
                return self._log("semantic", action_name, result=False, via_os=True, error_code="os_semantic_failed")

        # 2. Fallback: virtual semantic action
        return self._log("semantic", action_name, result=True, via_os=False)
