"""
SIRIUS LOCAL AI – UI Action Router 4.4.0

This module routes UI actions in a deterministic, offline‑safe manner.
It is part of the UI Automation Engine 4.4 and provides:

- Action validation (allowed actions only)
- Element reference validation
- Security Family 4.4 compliance
- STRANGER‑mode restrictions
- Deterministic routing to the UI Sandbox 4.4

All logic is deterministic, offline, and fully isolated.

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- All OS interaction must go through the sandbox.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any, Optional, List


class UIActionRouter44:
    """
    Deterministic UI action router for Runtime 4.4.
    """

    # Allowed UI actions in 4.4.0
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

    def __init__(self, sandbox=None, security_policy=None):
        self.sandbox = sandbox
        self.security_policy = security_policy
        self.initialized = False
        self.degraded_mode = False

    # ---------------------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.sandbox:
                self.sandbox.initialize()

            if self.security_policy:
                self.security_policy.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # PUBLIC API – ROUTE ACTION
    # ---------------------------------------------------------------------
    def route(self, element_ref: Dict[str, Any], action: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Routes a UI action to the sandbox after validating:
        - action type
        - element reference
        - security policy
        """
        if not self.initialized:
            init_result = self.initialize()
            if init_result.get("status") not in ("initialized", "already_initialized"):
                return {"status": "error", "reason": "router_not_initialized", "details": init_result}

        # 1. Validate action
        if action not in self.ALLOWED_ACTIONS:
            return {"status": "error", "reason": "action_not_allowed", "action": action}

        # 2. Validate element reference
        if not self._validate_element_ref(element_ref):
            return {"status": "error", "reason": "invalid_element_reference"}

        # 3. Security policy check
        if self.security_policy:
            sec = self.security_policy.check_action(element_ref, action)
            if sec.get("status") != "allowed":
                return {"status": "blocked", "policy": sec}

        # 4. Dispatch to sandbox
        try:
            result = self.sandbox.execute_ui_action(
                element_ref=element_ref,
                action=action,
                payload=payload or {}
            )
            return {"status": "ok", "result": result}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # INTERNAL – ELEMENT REF VALIDATION
    # ---------------------------------------------------------------------
    def _validate_element_ref(self, ref: Dict[str, Any]) -> bool:
        """
        Ensures element reference contains required deterministic fields.
        """
        if not isinstance(ref, dict):
            return False

        required = ("id", "role", "path")
        for key in required:
            if key not in ref:
                return False

        # path must be deterministic (list of indices or names)
        if not isinstance(ref.get("path"), list):
            return False

        return True
