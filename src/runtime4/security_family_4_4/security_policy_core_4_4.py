security_family_4_4/security_policy_core_4_4.py
"""
SIRIUS LOCAL AI – Security Policy Core 4.4.0

Security Policy Core 4.4 is the central rule engine of Security Family 4.4.
It provides deterministic, offline‑safe enforcement of:

- Identity rules (OWNER / FAMILY / STRANGER)
- Action permissions
- Sensitive operation restrictions
- UI safety constraints
- Behavior‑aware adjustments (safe subset)
- Integration with Policy Router 4.4

All logic is deterministic, offline, and fully isolated.

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No personal data stored.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any


class SecurityPolicyCore44:
    """
    Deterministic rule engine for Runtime 4.4.
    """

    # Sensitive actions always blocked for FAMILY + STRANGER
    SENSITIVE_ACTIONS = {
        "delete",
        "edit_advanced",
        "open_sensitive",
        "invoke_critical",
    }

    # OWNER‑only actions
    OWNER_ONLY_ACTIONS = {
        "invoke_critical",
        "edit_advanced",
    }

    def __init__(self):
        self.initialized = False
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
    # IDENTITY OVERRIDE (OPTIONAL)
    # ------------------------------------------------------------------
    def identity_override(self, element_ref: Dict[str, Any]):
        """
        Optional deterministic override based on element metadata.
        Example:
        - Elements tagged as "trusted" → OWNER
        - Elements tagged as "child" → FAMILY
        - Elements tagged as "unknown" → STRANGER
        """
        tag = element_ref.get("tag")

        if tag == "trusted":
            return "OWNER"
        if tag == "child":
            return "FAMILY"
        if tag == "unknown":
            return "STRANGER"

        return None  # no override

    # ------------------------------------------------------------------
    # MAIN POLICY CHECK
    # ------------------------------------------------------------------
    def check(self, identity: str, element_ref: Dict[str, Any], action: str) -> Dict[str, Any]:
        """
        Determines whether an action is allowed based on identity and rules.
        """

        # 1. OWNER has full access except explicit forbidden cases
        if identity == "OWNER":
            # OWNER‑only actions are allowed
            return {"status": "allowed"}

        # 2. FAMILY restrictions
        if identity == "FAMILY":
            if action in self.SENSITIVE_ACTIONS:
                return {
                    "status": "blocked",
                    "reason": "sensitive_action_blocked_for_family",
                    "action": action,
                }
            return {"status": "allowed"}

        # 3. STRANGER restrictions
        if identity == "STRANGER":
            # STRANGER cannot perform sensitive or owner‑only actions
            if action in self.SENSITIVE_ACTIONS or action in self.OWNER_ONLY_ACTIONS:
                return {
                    "status": "blocked",
                    "reason": "action_blocked_for_stranger",
                    "action": action,
                }
            return {"status": "allowed"}

        # 4. Unknown identity → block
        return {
            "status": "blocked",
            "reason": "unknown_identity",
            "identity": identity,
        }

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
