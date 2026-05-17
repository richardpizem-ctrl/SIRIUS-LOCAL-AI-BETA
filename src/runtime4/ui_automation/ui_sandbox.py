"""
UI Sandbox Module – Runtime 4.3.x

Responsible for:
- security rules for UI actions
- identity-based permission control (OWNER / FAMILY / STRANGER / CHILD)
- auditing UI operations
- permissions for click, write, select and semantic actions
- safe-mode and degraded-mode behavior

UI Sandbox is the ONLY layer that decides
whether a UI action is allowed to execute.
"""


class UISandbox:
    def __init__(self, identity: str = "OWNER"):
        """
        identity: current user identity
        - OWNER    = full access
        - FAMILY   = limited UI actions
        - STRANGER = minimal UI actions
        - CHILD    = very restricted actions
        """
        self.identity = identity
        self.audit_log = []  # audit trail

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ------------------------------------------------------------
    # MAIN PERMISSION LOGIC
    # ------------------------------------------------------------
    def check_permission(self, action_type, target):
        """
        Checks whether the action is allowed based on identity.
        action_type: "click", "write", "select", "semantic"
        target: UI element or semantic action name

        Returns:
            bool – True if allowed, False otherwise.
        """

        # Safe-mode: deny everything, but still audit
        if self.safe_mode:
            self.audit(action_type, target, allowed=False, reason="safe_mode")
            return False

        allowed = False

        try:
            if self.identity == "OWNER":
                allowed = True

            elif self.identity == "FAMILY":
                allowed = self._family_rules(action_type, target)

            elif self.identity == "STRANGER":
                allowed = self._stranger_rules(action_type, target)

            elif self.identity == "CHILD":
                allowed = self._child_rules(action_type, target)

            else:
                # Unknown identity → safest behavior
                allowed = False
                self.degraded_mode = True

            self.audit(action_type, target, allowed)
            return allowed

        except Exception:
            # Any unexpected error → deny and mark degraded mode
            self.degraded_mode = True
            self.audit(action_type, target, allowed=False, reason="exception")
            return False

    # ------------------------------------------------------------
    # FAMILY RULES
    # ------------------------------------------------------------
    def _family_rules(self, action_type, target):
        """
        FAMILY can:
        - click harmless elements
        - write only into safe fields (future extension)
        - cannot trigger system-level semantic actions
        """
        if action_type == "semantic":
            if isinstance(target, str) and "settings" in target.lower():
                return False
        return True

    # ------------------------------------------------------------
    # STRANGER RULES
    # ------------------------------------------------------------
    def _stranger_rules(self, action_type, target):
        """
        STRANGER can:
        - read UI only (no actions allowed)
        """
        return False

    # ------------------------------------------------------------
    # CHILD RULES
    # ------------------------------------------------------------
    def _child_rules(self, action_type, target):
        """
        CHILD can:
        - click only on elements marked as safe
        - cannot write text
        - cannot execute semantic actions
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
    def audit(self, action_type, target, allowed, reason=None):
        """
        Audit log for UI actions.
        (Currently local only – will be connected to EventBus later.)
        """
        entry = {
            "action": action_type,
            "target": getattr(target, "name", target),
            "allowed": bool(allowed),
            "identity": self.identity,
            "reason": reason,
            "degraded_mode": self.degraded_mode,
        }
        self.audit_log.append(entry)
        return entry
