"""
WinCapabilities Module – Runtime 4.3.x (PRO)

Responsible for:
- Providing an OS UI control interface for UIActions
- Abstracting real OS automation (click, write, select, semantic)
- Keeping Runtime 4.x deterministic and testable

In 4.3.x this module is a SAFE ADAPTER:
- No real OS integration yet
- All methods are deterministic
- Ready for future Win32/UIA/WinRT bindings in 4.4.0+
- Supports safe-mode and degraded-mode behavior
- Strict error codes and unified result surface
"""

from typing import Any, Dict, List, Optional


class WinCapabilities:
    """
    Deterministic OS‑level UI control adapter for Runtime 4.3.x (PRO).
    """

    VALID_ACTIONS = {"click", "write", "select", "semantic"}

    def __init__(self, dry_run: bool = True):
        """
        dry_run:
            True  = simulate OS actions (4.3.x default)
            False = reserved for future real OS integration (4.4+)
        """
        self.dry_run = dry_run
        self.last_calls: List[Dict[str, Any]] = []

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
        error_code: Optional[str] = None,
    ) -> Dict[str, Any]:

        entry = {
            "action": action_type,
            "element": getattr(element, "name", element),
            "value": value,
            "result": result,
            "error": error_code,
            "dry_run": self.dry_run,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }

        self.last_calls.append(entry)
        return entry

    # ------------------------------------------------------------
    # INTERNAL SAFE EXECUTION WRAPPER
    # ------------------------------------------------------------
    def _safe_stub(self, action_type: str, element: Any = None, value: Any = None):
        """
        Unified deterministic stub for all OS-level actions.
        """

        if self.safe_mode:
            return self._log(
                action_type,
                element,
                value,
                result=False,
                error_code="safe_mode",
            )

        try:
            # In 4.3.x → always deterministic success
            return self._log(action_type, element, value, result=True)

        except Exception:
            self.degraded_mode = True
            return self._log(
                action_type,
                element,
                value,
                result=False,
                error_code="exception",
            )

    # ------------------------------------------------------------
    # VALIDATION
    # ------------------------------------------------------------
    def _validate_action(self, action_type: str) -> Optional[Dict[str, Any]]:
        if action_type not in self.VALID_ACTIONS:
            return self._log(
                action_type,
                result=False,
                error_code="invalid_action_type",
            )
        return None

    # ------------------------------------------------------------
    # OS-LEVEL ACTIONS (INTERFACE ONLY IN 4.3.x)
    # ------------------------------------------------------------
    def click(self, element: Any) -> Dict[str, Any]:
        err = self._validate_action("click")
        if err:
            return err
        return self._safe_stub("click", element)

    def write(self, element: Any, text: Any) -> Dict[str, Any]:
        err = self._validate_action("write")
        if err:
            return err

        if not isinstance(text, str):
            return self._log(
                "write",
                element,
                value=text,
                result=False,
                error_code="invalid_text_type",
            )

        return self._safe_stub("write", element, text)

    def select(self, element: Any, option: Any) -> Dict[str, Any]:
        err = self._validate_action("select")
        if err:
            return err

        return self._safe_stub("select", element, option)

    def semantic(self, action_name: Any, context: Optional[dict] = None) -> Dict[str, Any]:
        err = self._validate_action("semantic")
        if err:
            return err

        if not isinstance(action_name, str) or not action_name.strip():
            return self._log(
                "semantic",
                action_name,
                value=context,
                result=False,
                error_code="invalid_action_name",
            )

        if context is not None and not isinstance(context, dict):
            return self._log(
                "semantic",
                action_name,
                value=context,
                result=False,
                error_code="invalid_context_type",
            )

        return self._safe_stub("semantic", action_name, context)

    # ------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "dry_run": self.dry_run,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "last_call_count": len(self.last_calls),
        }
