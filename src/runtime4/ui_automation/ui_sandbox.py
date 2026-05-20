"""
UI Sandbox Module – Runtime 4.3.x (PRO)

Responsible for:
- Security rules for UI actions
- Identity-based permission control (OWNER / FAMILY / STRANGER / CHILD)
- Deterministic auditing of UI operations
- Permission enforcement for click, write, select, semantic actions
- Safe-mode and degraded-mode behavior

UI Sandbox is the ONLY layer that decides
whether a UI action is allowed to execute.

Security Notes:
- Deterministic, offline-safe
- No dynamic imports, no eval, no reflection
- Fully compatible with Security Family 4.4
"""

from typing import Any, Dict, Optional


class UISandbox:
    """
    Deterministic UI Sandbox for Runtime 4.3.x (PRO).
    """

    VALID_IDENTITIES = {"OWNER", "FAMILY", "STRANGER", "CHILD"}
    VALID_ACTIONS = {"click", "write", "select", "semantic"}

    def __init__(self, identity: str = "OWNER"):
        """
        identity: current user identity
        """
        self.identity = identity if identity in self.VALID_IDENTITIES else "STRANGER"

        self.audit_log: list = []
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ------------------------------------------------------------
    # MAIN PERMISSION LOGIC
    # ------------------------------------------------------------
    def check_permission(self, action_type: str, target: Any) -> bool:
        """
        Determines whether the action is allowed based on identity.
        Returns True/False.
        """

        # Safe-mode → deny everything
        if self.safe_mode:
            self._audit(action_type, target, allowed=False, reason="safe_mode")
            return False

        # Validate action
        if action_type not in self.VALID_ACTIONS:
            self._audit(action_type, target, allowed=False, reason="invalid_action")
            return False

        try:
            # OWNER
            if self.identity == "OWNER":
                allowed = True

            # FAMILY
            elif self.identity == "FAMILY":
                allowed = self._family_rules(action_type, target)

            # STRANGER
            elif self.identity == "STRANGER":
                allowed = self._stranger_rules(action_type, target)

            # CHILD
            elif self.identity == "CHILD":
                allowed = self._child_rules(action_type, target)

            # Unknown identity (should never happen)
            else:
                allowed = False
                self.degraded_mode = True

            self._audit(action_type, target, allowed)
            return allowed

        except Exception:
            self.degraded_mode = True
            self._audit(action_type, target, allowed=False, reason="exception")
            return False

    # ------------------------------------------------------------
    # FAMILY RULES
    # ------------------------------------------------------------
    def _family_rules(self, action_type: str, target: Any) -> bool:
        """
        FAMILY:
        - click allowed
        - write allowed only to safe fields (future extension)
        - semantic actions restricted (e.g., settings)
        """
        if action_type == "semantic":
            if isinstance(target, str) and "settings" in target.lower():
                return False
        return True

    # ------------------------------------------------------------
    # STRANGER RULES
    # ------------------------------------------------------------
    def _stranger_rules(self, action_type: str, target: Any) -> bool:
        """
        STRANGER:
        - cannot perform any UI actions
        """
        return False

    # ------------------------------------------------------------
    # CHILD RULES
    # ------------------------------------------------------------
    def _child_rules(self, action_type: str, target: Any) -> bool:
        """
        CHILD:
        - click only on elements marked as safe
        - cannot write
        - cannot semantic
        """
        if action_type in ("write", "semantic"):
            return False

        if action_type == "click":
            if hasattr(target, "properties"):
                return bool(target.properties.get("safe", False))
            return False

        return True

    # ------------------------------------------------------------
    # AUDIT
    # ------------------------------------------------------------
    def _audit(self, action_type: str, target: Any, allowed: bool, reason: Optional[str] = None) -> Dict[str, Any]:
        """
        Deterministic audit log entry.
        """
        entry = {
            "action": action_type,
            "target": getattr(target, "name", target),
            "allowed": bool(allowed),
            "identity": self.identity,
            "reason": reason,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }

        self.audit_log.append(entry)
        return entry

    # ------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "identity": self.identity,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "audit_count": len(self.audit_log),
        }
