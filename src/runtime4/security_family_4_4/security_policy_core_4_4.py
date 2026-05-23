"""
SIRIUS LOCAL AI – Security Policy Core 4.5.0 (PRO)

Security Policy Core 4.5 is the central rule engine of Security Family 4.5.
It provides deterministic, offline‑safe enforcement of:

- Identity rules (OWNER / FAMILY / STRANGER)
- Action permissions
- Sensitive operation restrictions
- UI safety constraints
- Behavior‑aware adjustments (safe subset)
- Integration with Policy Router 4.5

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No personal data stored.
- Fully compatible with Security Family 4.5.
"""

from typing import Dict, Any


class SecurityPolicyCore45:
    """
    Deterministic rule engine for Runtime 4.5 (PRO).
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
                "version": self.version,
            }

        # Validate identity
        if identity not in self.VALID_IDENTITIES:
            return {
                "status": "blocked",
                "code": "invalid_identity",
                "identity": identity,
                "version": self.version,
            }

        # Validate action
        if not isinstance(action, str) or not action.strip():
            return {
                "status": "blocked",
                "code": "invalid_action",
                "version": self.version,
            }

        # Validate element_ref
        if not isinstance(element_ref, dict):
            return {
                "status": "blocked",
                "code": "invalid_element_ref",
                "version": self.version,
            }

        # ------------------------------
        # OWNER
        # ------------------------------
        if identity == "OWNER":
            return {"status": "allowed", "layer": "policy_core", "version": self.version}

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
                    "version": self.version,
                }
            return {"status": "allowed", "layer": "policy_core", "version": self.version}

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
                    "version": self.version,
                }
            return {"status": "allowed", "layer": "policy_core", "version": self.version}

        # ------------------------------
        # Unknown identity (should never happen)
        # ------------------------------
        return {
            "status": "blocked",
            "layer": "policy_core",
            "reason": "unknown_identity",
            "identity": identity,
            "version": self.version,
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
            "version": self.version,
        }
