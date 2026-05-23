"""
SIRIUS LOCAL AI – UI Action Router 4.5.0 (PRO)

Responsible for deterministic routing of UI actions inside Runtime 4.5.
Provides:
- Action validation
- Element reference validation
- Security Family 4.5 compliance
- STRANGER-mode restrictions
- Deterministic routing to UI Sandbox 4.5
- Safe-mode and degraded-mode behavior
- Structured result surface

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- All OS interaction must go through the sandbox.
- Fully compatible with Security Family 4.5.
"""

from typing import Dict, Any, Optional


class UIActionRouter45:
    """
    Deterministic UI action router for Runtime 4.5 (PRO).
    """

    ALLOWED_ACTIONS = {
        "click",
        "double_click",
        "right_click",
        "set_text",
        "focus",
        "invoke",
        "select",
        "expand",
        "collapse",
        "scroll",
    }

    REQUIRED_ELEMENT_FIELDS = ("id", "role", "path")

    def __init__(self, sandbox=None, security_policy=None):
        self.version = "4.5.0"

        self.sandbox = sandbox
        self.security_policy = security_policy

        self.initialized = False
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": self.version}

        try:
            if self.sandbox and hasattr(self.sandbox, "initialize"):
                self.sandbox.initialize()

            if self.security_policy and hasattr(self.security_policy, "initialize"):
                self.security_policy.initialize()

            self.initialized = True
            return {"status": "initialized", "version": self.version}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
                "version": self.version,
            }

    # ---------------------------------------------------------------------
    # PUBLIC API – ROUTE ACTION
    # ---------------------------------------------------------------------
    def route(
        self,
        element_ref: Dict[str, Any],
        action: str,
        payload: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:

        # Safe-mode → block everything
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "action": action,
                "element": element_ref,
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

        # Ensure initialized
        if not self.initialized:
            init = self.initialize()
            if init.get("status") not in ("initialized", "already_initialized"):
                return {
                    "status": "error",
                    "code": "router_not_initialized",
                    "details": init,
                    "version": self.version,
                }

        # 1. Validate action
        if action not in self.ALLOWED_ACTIONS:
            return {
                "status": "error",
                "code": "action_not_allowed",
                "action": action,
                "version": self.version,
            }

        # 2. Validate element reference
        if not self._validate_element_ref(element_ref):
            return {
                "status": "error",
                "code": "invalid_element_reference",
                "element": element_ref,
                "version": self.version,
            }

        # 3. Security policy check
        if self.security_policy:
            try:
                sec = self.security_policy.check_action(element_ref, action)
                if sec.get("status") != "allowed":
                    return {
                        "status": "blocked",
                        "layer": "policy",
                        "policy": sec,
                        "version": self.version,
                    }
            except Exception as exc:
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "policy_exception",
                    "exception": str(exc),
                    "version": self.version,
                }

        # 4. Dispatch to sandbox
        try:
            result = self.sandbox.execute_ui_action(
                element_ref=element_ref,
                action=action,
                payload=payload or {}
            )

            return {
                "status": "ok",
                "action": action,
                "element": element_ref,
                "result": result,
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "sandbox_exception",
                "exception": str(exc),
                "action": action,
                "element": element_ref,
                "version": self.version,
            }

    # ---------------------------------------------------------------------
    # INTERNAL – ELEMENT REF VALIDATION
    # ---------------------------------------------------------------------
    def _validate_element_ref(self, ref: Dict[str, Any]) -> bool:
        if not isinstance(ref, dict):
            return False

        for key in self.REQUIRED_ELEMENT_FIELDS:
            if key not in ref:
                return False

        if not isinstance(ref.get("path"), list):
            return False

        return True
