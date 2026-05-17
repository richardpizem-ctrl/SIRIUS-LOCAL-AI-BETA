"""
WinCapabilities Module – Runtime 4.3.x

Responsible for:
- providing an OS UI control interface for UIActions
- abstracting real OS automation (click, write, select, semantic)
- keeping Runtime 4.x deterministic and testable

In 4.3.x this module is a SAFE ADAPTER:
- no real OS integration yet
- all methods are deterministic
- ready for future Win32/UIA/WinRT bindings in 4.4.0+
- supports safe-mode and degraded-mode behavior
"""

from typing import Any, Dict, List, Optional


class WinCapabilities:
    def __init__(self, dry_run: bool = True):
        """
        dry_run:
            True  = do not touch real OS, only simulate success
            False = future flag for real OS integration (4.4.0+)
        """
        self.dry_run = dry_run
        self.last_calls: List[Dict[str, Any]] = []

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ------------------------------------------------------------
    # INTERNAL LOGGING
    # ------------------------------------------------------------
    def _log(self, action_type, element=None, value=None, result=True, error_code=None):
        entry = {
            "action": action_type,
            "element": getattr(element, "name", element),
            "value": value,
            "result": result,
            "error": error_code,
            "dry_run": self.dry_run,
            "degraded_mode": self.degraded_mode,
        }
        self.last_calls.append(entry)
        return entry

    # ------------------------------------------------------------
    # INTERNAL SAFE EXECUTION WRAPPER
    # ------------------------------------------------------------
    def _safe_stub(self, action_type, element=None, value=None):
        """
        Unified deterministic stub for all OS-level actions.
        """
        if self.safe_mode:
            return self._log(action_type, element, value, result=False, error_code="safe_mode")

        try:
            # In 4.3.x → always deterministic success
            return self._log(action_type, element, value, result=True)
        except Exception:
            self.degraded_mode = True
            return self._log(action_type, element, value, result=False, error_code="exception")

    # ------------------------------------------------------------
    # OS-LEVEL ACTIONS (INTERFACE ONLY IN 4.3.x)
    # ------------------------------------------------------------
    def click(self, element):
        """
        OS-level click on a UI element.
        Deterministic stub in 4.3.x.
        """
        return self._safe_stub("click", element)

    def write(self, element, text):
        """
        OS-level text input.
        Deterministic stub in 4.3.x.
        """
        if not isinstance(text, str):
            return self._log("write", element, value=text, result=False, error_code="invalid_text_type")
        return self._safe_stub("write", element, text)

    def select(self, element, option):
        """
        OS-level selection in menus/lists.
        Deterministic stub in 4.3.x.
        """
        return self._safe_stub("select", element, option)

    def semantic(self, action_name, context=None):
        """
        OS-level semantic actions:
        - open_settings
        - confirm
        - cancel
        - open_window
        - close_window

        Deterministic stub in 4.3.x.
        """
        if not isinstance(action_name, str) or not action_name.strip():
            return self._log("semantic", action_name, value=context, result=False, error_code="invalid_action_name")

        return self._safe_stub("semantic", action_name, context)
