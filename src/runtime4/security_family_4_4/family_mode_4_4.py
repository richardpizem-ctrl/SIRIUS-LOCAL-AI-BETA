"""
SIRIUS LOCAL AI – Family Mode 4.5.0 (PRO)

FamilyMode 4.5 is the child‑safe identity layer inside Security Family 4.5.
It activates when:

- Identity Engine classifies the user as FAMILY
- Behavior patterns match low‑risk, non‑OWNER usage
- Policy Core enforces child‑safe restrictions

FamilyMode enforces:
- Restricted UI actions
- Blocked access to sensitive operations
- Safe‑interaction rules
- Deterministic isolation
- Integration with Behavior Monitor 4.5 and TimeLimits 4.5

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No personal data stored.
- Fully compatible with Security Family 4.5.
"""

from typing import Dict, Any


class FamilyMode45:
    """
    Child‑safe restricted identity mode for Runtime 4.5 (PRO).
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
        self.safe_mode = False
        self.degraded_mode = False
        self.version = "4.5"

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": self.version}

        try:
            self.initialized = True
            return {"status": "ok", "version": self.version}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
                "version": self.version,
            }

    # ------------------------------------------------------------------
    # ACTIVATE FAMILY MODE
    # ------------------------------------------------------------------
    def activate(self, reason: str) -> Dict[str, Any]:
        """Activates FamilyMode with a deterministic reason."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "FamilyMode activation disabled in safe-mode.",
                "version": self.version,
            }

        if not isinstance(reason, str) or not reason.strip():
            return {"status": "error", "code": "invalid_reason", "version": self.version}

        self.active = True
        self.reason = reason
        return {"status": "activated", "reason": reason, "version": self.version}

    # ------------------------------------------------------------------
    # DEACTIVATE FAMILY MODE
    # ------------------------------------------------------------------
    def deactivate(self) -> Dict[str, Any]:
        self.active = False
        self.reason = None
        return {"status": "deactivated", "version": self.version}

    # ------------------------------------------------------------------
    # CHECK ACTION PERMISSION
    # ------------------------------------------------------------------
    def check_action(self, action: str) -> Dict[str, Any]:
        """Determines whether a UI action is allowed under FamilyMode."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Action validation disabled in safe-mode.",
                "version": self.version,
            }

        if not isinstance(action, str) or not action.strip():
            return {"status": "error", "code": "invalid_action", "version": self.version}

        if not self.active:
            return {"status": "allowed", "mode": "inactive", "version": self.version}

        # Blocked actions
        if action in self.BLOCKED_ACTIONS:
            return {
                "status": "blocked",
                "mode": "FAMILY",
                "reason": "action_forbidden_in_family_mode",
                "action": action,
                "version": self.version,
            }

        # Allowed actions
        if action in self.ALLOWED_ACTIONS:
            return {"status": "allowed", "mode": "FAMILY", "version": self.version}

        # Unknown action → block by default
        return {
            "status": "blocked",
            "mode": "FAMILY",
            "reason": "unknown_action",
            "action": action,
            "version": self.version,
        }

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "active": self.active,
            "reason": self.reason,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "version": self.version,
        }
