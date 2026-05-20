security_family_4_4/family_mode_4_4.py
"""
SIRIUS LOCAL AI – Family Mode 4.4.0

FamilyMode 4.4 is the child‑safe identity layer inside Security Family 4.4.
It activates when:

- Identity Engine classifies the user as FAMILY
- Behavior patterns match low‑risk, non‑OWNER usage
- Policy Core enforces child‑safe restrictions

FamilyMode enforces:
- Restricted UI actions
- Blocked access to sensitive operations
- Safe‑interaction rules
- Deterministic isolation
- Integration with Behavior Monitor 4.4 and TimeLimits 4.4

All logic is deterministic, offline, and fully isolated.

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No personal data stored.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any


class FamilyMode44:
    """
    Child‑safe restricted identity mode for Runtime 4.4.
    """

    # Allowed actions for FAMILY identity (safe subset)
    ALLOWED_ACTIONS = {
        "click",
        "focus",
        "scroll",
        "select",
    }

    # Blocked actions (unsafe for children)
    BLOCKED_ACTIONS = {
        "set_text",
        "invoke",
        "expand",
        "collapse",
        "double_click",
        "right_click",
        "open_sensitive",
        "delete",
        "edit_advanced",
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
    # ACTIVATE FAMILY MODE
    # ------------------------------------------------------------------
    def activate(self, reason: str):
        """
        Activates FamilyMode with a deterministic reason.
        """
        self.active = True
        self.reason = reason
        return {"status": "activated", "reason": reason}

    # ------------------------------------------------------------------
    # DEACTIVATE FAMILY MODE
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
        Determines whether a UI action is allowed under FamilyMode.
        """
        if not self.active:
            return {"status": "allowed", "mode": "inactive"}

        # Blocked actions
        if action in self.BLOCKED_ACTIONS:
            return {
                "status": "blocked",
                "mode": "FAMILY",
                "reason": "action_forbidden_in_family_mode",
                "action": action,
            }

        # Allowed actions
        if action in self.ALLOWED_ACTIONS:
            return {"status": "allowed", "mode": "FAMILY"}

        # Unknown action → block by default
        return {
            "status": "blocked",
            "mode": "FAMILY",
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
