security_family_4_4/identity_engine_4_4.py
"""
SIRIUS LOCAL AI – Identity Engine 4.4.0

Identity Engine 4.4 is the deterministic identity classifier used by
Security Family 4.4. It determines whether the interacting entity is:

- OWNER   (full permissions)
- FAMILY  (child‑safe, restricted)
- STRANGER (untrusted, heavily restricted)

Identity is determined using:
- Element reference metadata (role, source, trust level)
- Behavior patterns (via Behavior Monitor 4.4)
- Security Policy Core 4.4 rules
- Deterministic fallback logic

Identity Engine NEVER uses:
- Personal data
- Biometrics
- Network identifiers
- External services

All logic is deterministic, offline, and fully isolated.
"""

from typing import Dict, Any


class IdentityEngine44:
    """
    Deterministic identity classifier for Runtime 4.4.
    """

    def __init__(self, behavior_monitor=None, policy_core=None):
        self.behavior_monitor = behavior_monitor
        self.policy_core = policy_core

        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.behavior_monitor:
                self.behavior_monitor.initialize()

            if self.policy_core:
                self.policy_core.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # PUBLIC API – GET IDENTITY
    # ------------------------------------------------------------------
    def get_identity(self, element_ref: Dict[str, Any]) -> str:
        """
        Determines identity based on deterministic rules.

        Priority:
        1. Explicit role in element_ref
        2. Policy Core override
        3. Behavior‑based fallback
        4. Default: STRANGER
        """

        # 1. Explicit role
        role = element_ref.get("role")
        if role in ("OWNER", "FAMILY", "STRANGER"):
            return role

        # 2. Policy Core override
        if self.policy_core:
            override = self.policy_core.identity_override(element_ref)
            if override in ("OWNER", "FAMILY", "STRANGER"):
                return override

        # 3. Behavior‑based fallback
        if self.behavior_monitor:
            risk_owner = self.behavior_monitor.risk_scores.get("OWNER", 0)
            risk_family = self.behavior_monitor.risk_scores.get("FAMILY", 0)
            risk_stranger = self.behavior_monitor.risk_scores.get("STRANGER", 0)

            # If OWNER has extremely low risk → trust OWNER
            if risk_owner == 0:
                return "OWNER"

            # If FAMILY has low risk → trust FAMILY
            if risk_family < 5:
                return "FAMILY"

            # If STRANGER risk is high → STRANGER
            if risk_stranger >= 5:
                return "STRANGER"

        # 4. Default fallback
        return "STRANGER"

    # ------------------------------------------------------------------
    # PUBLIC API – GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
