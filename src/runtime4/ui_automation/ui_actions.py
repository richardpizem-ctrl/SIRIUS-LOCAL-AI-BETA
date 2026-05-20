"""
SIRIUS LOCAL AI – UI Actions Module 4.3.1 (PRO)

New in 4.3.x:
- WinCapabilities integration layer (OS UI control hook)
- Deterministic OS action routing
- Extended audit logging
- Unified interface for UI and OS actions
- Semantic action mapping foundation
- Safe-mode and degraded-mode behavior
- Structured, deterministic result surface

All actions ALWAYS pass through the UI Sandbox when present.
"""

from typing import Any, Dict, List, Optional


class UIActions:
    """
    Deterministic UI Action Engine for Runtime 4.3.x (PRO).
    Provides:
    - OS-level action routing (WinCapabilities)
    - Virtual fallback actions
    - Strict sandbox enforcement
    - Deterministic logging
    - Safe-mode and degraded-mode behavior
    """

    VALID_ACTIONS = {
        "click",
        "write",
        "select",
        "semantic",
    }

    def __init__(self, sandbox=None, win_capabilities=None):
        """
        sandbox: UI Sandbox (must expose check_permission)
        win_capabilities: OS-level UI control layer (optional)
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
            "safe_mode": self.safe_mode,
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
    # OS‑LEVEL EXECUTION WRAPPER
    # ------------------------------------------------------------
    def _try_os_action(self, method: str, *args) -> Optional[bool]:
        """
        Attempts OS-level action via WinCapabilities.
        Returns:
            True  → OS action succeeded
            False → OS action failed
            None  → OS action not available
        """

        if not self.win_capabilities:
            return None

        if not hasattr(self.win_capabilities, method):
            return None

        try:
            return bool(getattr(self.win_capabilities, method)(*args))
        except Exception:
            self.degraded_mode = True
            return False

    # ------------------------------------------------------------
    # PRIMARY UI ACTIONS
    # ------------------------------------------------------------
    def click(self, element: Any) -> Dict[str, Any]:
        if self.safe_mode:
            return self._log("click", element, result=False, error_code="safe_mode")

        if not self._allowed("click", element):
            return self._log("click", element, result=False, error_code="permission_denied")

        os_result = self._try_os_action("click", element)
        if os_result is True:
            return self._log("click", element, result=True, via_os=True)
        if os_result is False:
            return self._log("click", element, result=False, via_os=True, error_code="os_click_failed")

        return self._log("click", element, result=True, via_os=False)

    def write(self, element: Any, text: str) -> Dict[str, Any]:
        if self.safe_mode:
            return self._log("write", element, value=text, result=False, error_code="safe_mode")

        if not isinstance(text, str):
            return self._log("write", element, value=text, result=False, error_code="invalid_text_type")

        if not self._allowed("write", element):
            return self._log("write", element, value=text, result=False, error_code="permission_denied")

        os_result = self._try_os_action("write", element, text)
        if os_result is True:
            return self._log("write", element, value=text, result=True, via_os=True)
        if os_result is False:
            return self._log("write", element, value=text, result=False, via_os=True, error_code="os_write_failed")

        return self._log("write", element, value=text, result=True, via_os=False)

    def select(self, element: Any, option: Any) -> Dict[str, Any]:
        if self.safe_mode:
            return self._log("select", element, value=option, result=False, error_code="safe_mode")

        if not self._allowed("select", element):
            return self._log("select", element, value=option, result=False, error_code="permission_denied")

        os_result = self._try_os_action("select", element, option)
        if os_result is True:
            return self._log("select", element, value=option, result=True, via_os=True)
        if os_result is False:
            return self._log("select", element, value=option, result=False, via_os=True, error_code="os_select_failed")

        return self._log("select", element, value=option, result=True, via_os=False)

    # ------------------------------------------------------------
    # SEMANTIC ACTIONS
    # ------------------------------------------------------------
    def semantic(self, action_name: str, context: Optional[dict] = None) -> Dict[str, Any]:
        if self.safe_mode:
            return self._log("semantic", action_name, result=False, error_code="safe_mode")

        if not isinstance(action_name, str) or not action_name.strip():
            return self._log("semantic", action_name, result=False, error_code="invalid_action_name")

        if context is not None and not isinstance(context, dict):
            return self._log("semantic", action_name, value=context, result=False, error_code="invalid_context_type")

        if not self._allowed("semantic", action_name):
            return self._log("semantic", action_name, result=False, error_code="permission_denied")

        os_result = self._try_os_action("semantic", action_name, context)
        if os_result is True:
            return self._log("semantic", action_name, result=True, via_os=True)
        if os_result is False:
            return self._log("semantic", action_name, result=False, via_os=True, error_code="os_semantic_failed")

        return self._log("semantic", action_name, result=True, via_os=False)
