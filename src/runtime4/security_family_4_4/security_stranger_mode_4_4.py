security_family_4_4/security_stranger_mode_4_4.py
"""
SIRIUS LOCAL AI – Stranger Mode 4.4.0

StrangerMode 4.4 is the restricted‑identity security layer inside
Security Family 4.4. It activates when:

- Behavior does not match OWNER or FAMILY identity
- Risk score exceeds safe thresholds
- Unknown or untrusted interaction patterns appear

StrangerMode enforces:
- Strict UI action restrictions
- Blocked access to sensitive operations
- Reduced permissions for automation
- Deterministic isolation rules
- Integration with Behavior Monitor 4.4 and Security Policy Core 4.4

All logic is deterministic, offline, and fully isolated.

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No content logging, no personal data stored.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any


class StrangerMode44:
    """
    Restricted identity mode for Runtime 4.4.
    Enforces strict limitations on actions and capabilities.
    """

    # Allowed actions for STRANGER identity (very limited)
    ALLOWED_ACTIONS = {
        "click",
        "focus",
        "scroll",
    }

    # Blocked actions (always forbidden)
    BLOCKED_ACTIONS = {
        "set_text",
        "invoke",
        "select",
        "expand",
        "collapse",
        "double_click",
        "right_click",
    }

    def __init__(self):
        self.initialized = False
        self.active = False
        self.reason = None
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # ACTIVATE STRANGER MODE
    # ------------------------------------------------------------------
    def activate(self, reason: str):
        """
        Activates StrangerMode with a deterministic reason.
        """
        self.active = True
        self.reason = reason
        return {"status": "activated", "reason": reason}

    # ------------------------------------------------------------------
    # DEACTIVATE STRANGER MODE
    # ------------------------------------------------------------------
    def deactivate(self):
        self.active = False
        self.reason = None
        return {"status": "deactivated"}

    # ------------------------------------------------------------------
    # CHECK ACTION PERMISSION
    # ------------------------------------------------------------------
    def check_action(self, action: str) -> Dict[str, Any]:
        """
        Determines whether a UI action is allowed under StrangerMode.
        """
        if not self.active:
            return {"status": "allowed", "mode": "inactive"}

        # Blocked actions
        if action in self.BLOCKED_ACTIONS:
            return {
                "status": "blocked",
                "mode": "STRANGER",
                "reason": "action_forbidden_in_stranger_mode",
                "action": action,
            }

        # Allowed actions
        if action in self.ALLOWED_ACTIONS:
            return {"status": "allowed", "mode": "STRANGER"}

        # Unknown action → block by default
        return {
            "status": "blocked",
            "mode": "STRANGER",
            "reason": "unknown_action",
            "action": action,
        }

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "active": self.active,
            "reason": self.reason,
        }
