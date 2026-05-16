"""
UI Sandbox Module – Runtime 4.2.0

Responsible for:
- security rules for UI actions
- identity-based permission control (OWNER / FAMILY / STRANGER / CHILD)
- auditing UI operations
- permissions for click, write, select and semantic actions

UI Sandbox is the ONLY layer that decides
whether a UI action is allowed to execute.
"""

class UISandbox:
    def __init__(self, identity="OWNER"):
        """
        identity: current user identity
        - OWNER    = full access
        - FAMILY   = limited UI actions
        - STRANGER = minimal UI actions
        - CHILD    = very restricted actions
        """
        self.identity = identity
        self.audit_log = []  # audit trail

    # ------------------------------------------------------------
    # MAIN PERMISSION LOGIC
    # ------------------------------------------------------------
    def check_permission(self, action_type, target):
        """
        Checks whether the action is allowed based on identity.
        action_type: "click", "write", "select", "semantic"
        target: UI element or semantic action name
        """
        allowed = False

        if self.identity == "OWNER":
            allowed = True

        elif self.identity == "FAMILY":
            allowed = self._family_rules(action_type, target)

        elif self.identity == "STRANGER":
            allowed = self._stranger_rules(action_type, target)

        elif self.identity == "CHILD":
            allowed = self._child_rules(action_type, target)

        # audit the decision
        self.audit(action_type, target, allowed)
        return allowed

    # ------------------------------------------------------------
    # FAMILY RULES
    # ------------------------------------------------------------
    def _family_rules(self, action_type, target):
        """
        FAMILY can:
        - click harmless elements
        - write only into safe fields
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
                return target.properties.get("safe", False)
            return False

        return True

    # ------------------------------------------------------------
    # AUDIT
    # ------------------------------------------------------------
    def audit(self, action_type, target, allowed):
        """
        Audit log for UI actions.
        (Currently local only – will be connected to EventBus later.)
        """
        entry = {
            "action": action_type,
            "target": getattr(target, "name", target),
            "allowed": allowed,
        }
        self.audit_log.append(entry)
