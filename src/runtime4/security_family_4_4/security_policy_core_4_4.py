"""
SIRIUS LOCAL AI – Security Policy Core 4.4.0 (PRO)

Security Policy Core 4.4 is the central rule engine of Security Family 4.4.
It provides deterministic, offline‑safe enforcement of:

- Identity rules (OWNER / FAMILY / STRANGER)
- Action permissions
- Sensitive operation restrictions
- UI safety constraints
- Behavior‑aware adjustments (safe subset)
- Integration with Policy Router 4.4

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No personal data stored.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any


class SecurityPolicyCore44:
    """
    Deterministic rule engine for Runtime 4.4 (PRO).
    """

    VALID_IDENTITIES = {"OWNER", "FAMILY", "STRANGER"}

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
        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "ok"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
            }

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

        if not isinstance(element_ref, dict):
            return None

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

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Policy checks disabled in safe-mode.",
            }

        # Validate identity
        if identity not in self.VALID_IDENTITIES:
            return {
                "status": "blocked",
                "code": "invalid_identity",
                "identity": identity,
            }

        # Validate action
        if not isinstance(action, str) or not action.strip():
            return {
                "status": "blocked",
                "code": "invalid_action",
            }

        # Validate element_ref
        if not isinstance(element_ref, dict):
            return {
                "status": "blocked",
                "code": "invalid_element_ref",
            }

        # ------------------------------
        # OWNER
        # ------------------------------
        if identity == "OWNER":
            # OWNER has full access except explicit forbidden cases
            return {"status": "allowed", "layer": "policy_core"}

        # ------------------------------
        # FAMILY
        # ------------------------------
        if identity == "FAMILY":
            if action in self.SENSITIVE_ACTIONS:
                return {
                    "status": "blocked",
                    "layer": "policy_core",
                    "reason": "sensitive_action_blocked_for_family",
                    "action": action,
                }
            return {"status": "allowed", "layer": "policy_core"}

        # ------------------------------
        # STRANGER
        # ------------------------------
        if identity == "STRANGER":
            if action in self.SENSITIVE_ACTIONS or action in self.OWNER_ONLY_ACTIONS:
                return {
                    "status": "blocked",
                    "layer": "policy_core",
                    "reason": "action_blocked_for_stranger",
                    "action": action,
                }
            return {"status": "allowed", "layer": "policy_core"}

        # ------------------------------
        # Unknown identity (should never happen)
        # ------------------------------
        return {
            "status": "blocked",
            "layer": "policy_core",
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
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }
