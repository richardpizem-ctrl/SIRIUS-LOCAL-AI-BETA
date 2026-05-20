"""
SIRIUS LOCAL AI – Security Policy Router 4.4.0 (PRO)

The Security Policy Router 4.4 is the central decision layer that connects:

- Identity Engine 4.4
- StrangerMode 4.4
- FamilyMode 4.4
- Behavior Monitor 4.4
- TimeLimits 4.4
- Security Policy Core 4.4

Its job is to:
- Determine which identity rules apply
- Route UI actions through the correct security layer
- Enforce restrictions deterministically
- Block unsafe actions
- Provide unified security decisions for Runtime 4.4

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No personal data stored.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any


class SecurityPolicyRouter44:
    """
    Central security decision router for Runtime 4.4 (PRO).
    """

    def __init__(
        self,
        identity_engine=None,
        stranger_mode=None,
        family_mode=None,
        behavior_monitor=None,
        time_limits=None,
        policy_core=None,
    ):
        self.identity_engine = identity_engine
        self.stranger_mode = stranger_mode
        self.family_mode = family_mode
        self.behavior_monitor = behavior_monitor
        self.time_limits = time_limits
        self.policy_core = policy_core

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
            if self.identity_engine:
                self.identity_engine.initialize()

            if self.stranger_mode:
                self.stranger_mode.initialize()

            if self.family_mode:
                self.family_mode.initialize()

            if self.behavior_monitor:
                self.behavior_monitor.initialize()

            if self.time_limits:
                self.time_limits.initialize()

            if self.policy_core:
                self.policy_core.initialize()

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
    # PUBLIC API – CHECK ACTION
    # ------------------------------------------------------------------
    def check_action(self, element_ref: Dict[str, Any], action: str) -> Dict[str, Any]:
        """
        Determines whether an action is allowed based on:
        - identity
        - StrangerMode / FamilyMode
        - time limits
        - behavior risk
        - policy core rules
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Security routing disabled in safe-mode.",
            }

        # Validate inputs
        if not isinstance(element_ref, dict):
            return {"status": "blocked", "code": "invalid_element_ref"}

        if not isinstance(action, str) or not action.strip():
            return {"status": "blocked", "code": "invalid_action"}

        # 1. Determine identity
        try:
            identity = self.identity_engine.get_identity(element_ref)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "blocked",
                "code": "identity_engine_failed",
                "exception": str(exc),
            }

        # 2. Time limits
        if self.time_limits:
            tl = self.time_limits.check(identity, action)
            if tl.get("status") == "blocked":
                return {
                    "status": "blocked",
                    "layer": "time_limits",
                    "details": tl,
                }

        # 3. StrangerMode
        if identity == "STRANGER" and self.stranger_mode and self.stranger_mode.active:
            sm = self.stranger_mode.check_action(action)
            if sm.get("status") == "blocked":
                return {
                    "status": "blocked",
                    "layer": "stranger_mode",
                    "details": sm,
                }

        # 4. FamilyMode
        if identity == "FAMILY" and self.family_mode and self.family_mode.active:
            fm = self.family_mode.check_action(action)
            if fm.get("status") == "blocked":
                return {
                    "status": "blocked",
                    "layer": "family_mode",
                    "details": fm,
                }

        # 5. Policy Core
        try:
            pc = self.policy_core.check(identity, element_ref, action)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "blocked",
                "code": "policy_core_failed",
                "exception": str(exc),
            }

        if pc.get("status") == "blocked":
            return {
                "status": "blocked",
                "layer": "policy_core",
                "details": pc,
            }

        # 6. Allowed
        return {
            "status": "allowed",
            "identity": identity,
            "layer": "policy_router",
        }

    # ------------------------------------------------------------------
    # PUBLIC API – RECORD ACTION RESULT
    # ------------------------------------------------------------------
    def record_action(self, element_ref: Dict[str, Any], action: str, result: Dict[str, Any]):
        """
        Records behavior and consumes time units.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Action recording disabled in safe-mode.",
            }

        # Validate inputs
        if not isinstance(element_ref, dict):
            return {"status": "error", "code": "invalid_element_ref"}

        if not isinstance(action, str) or not action.strip():
            return {"status": "error", "code": "invalid_action"}

        if not isinstance(result, dict):
            return {"status": "error", "code": "invalid_result"}

        try:
            identity = self.identity_engine.get_identity(element_ref)

            # Behavior monitor
            if self.behavior_monitor:
                self.behavior_monitor.record(identity, element_ref, action, result)

            # Time limits
            if self.time_limits:
                self.time_limits.consume(identity, amount=1)

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "record_failed",
                "exception": str(exc),
            }

    # ------------------------------------------------------------------
    # PUBLIC API – GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }
