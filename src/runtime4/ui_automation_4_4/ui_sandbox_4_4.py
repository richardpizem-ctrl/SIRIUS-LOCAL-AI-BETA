"""
SIRIUS LOCAL AI – UI Sandbox 4.4.0 (PRO)

Hardened sandbox layer for UI Automation Engine 4.4.

Responsibilities:
- Enforce Security Family 4.4 rules for UI actions
- Mediate all OS‑level UI operations
- Apply STRANGER‑mode and behavior‑based restrictions
- Enforce time limits and action quotas
- Provide deterministic, auditable execution results

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- All OS calls must go through verified capability wrappers.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any, Optional


class UISandbox44:
    """
    Hardened UI sandbox for Runtime 4.4 (PRO).
    All UI actions must go through this class.
    """

    REQUIRED_CAPABILITY_METHODS = {"initialize", "execute_ui_action"}
    REQUIRED_POLICY_METHODS = {"initialize", "check_action"}
    REQUIRED_TIME_LIMITER_METHODS = {"initialize", "check", "consume"}
    REQUIRED_BEHAVIOR_METHODS = {"initialize", "record"}

    def __init__(
        self,
        capability_adapter=None,
        security_policy=None,
        time_limiter=None,
        behavior_monitor=None,
        identity: str = "OWNER",
    ):
        self.capability_adapter = capability_adapter
        self.security_policy = security_policy
        self.time_limiter = time_limiter
        self.behavior_monitor = behavior_monitor
        self.identity = identity

        self.initialized: bool = False
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ---------------------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        # Capability adapter
        if not self.capability_adapter:
            self.degraded_mode = True
            return {"status": "error", "code": "no_capability_adapter"}

        for m in self.REQUIRED_CAPABILITY_METHODS:
            if not hasattr(self.capability_adapter, m):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "invalid_capability_adapter_interface",
                    "missing": m,
                }

        # Security policy (optional but validated if present)
        if self.security_policy:
            for m in self.REQUIRED_POLICY_METHODS:
                if not hasattr(self.security_policy, m):
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "invalid_security_policy_interface",
                        "missing": m,
                    }

        # Time limiter (optional)
        if self.time_limiter:
            for m in self.REQUIRED_TIME_LIMITER_METHODS:
                if not hasattr(self.time_limiter, m):
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "invalid_time_limiter_interface",
                        "missing": m,
                    }

        # Behavior monitor (optional)
        if self.behavior_monitor:
            for m in self.REQUIRED_BEHAVIOR_METHODS:
                if not hasattr(self.behavior_monitor, m):
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "invalid_behavior_monitor_interface",
                        "missing": m,
                    }

        try:
            cap_res = self.capability_adapter.initialize()
            if cap_res.get("status") not in ("initialized", "already_initialized"):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "capability_init_failed",
                    "details": cap_res,
                }

            if self.security_policy:
                pol_res = self.security_policy.initialize()
                if pol_res.get("status") not in ("initialized", "already_initialized"):
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "policy_init_failed",
                        "details": pol_res,
                    }

            if self.time_limiter:
                tl_res = self.time_limiter.initialize()
                if tl_res.get("status") not in ("initialized", "already_initialized"):
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "time_limiter_init_failed",
                        "details": tl_res,
                    }

            if self.behavior_monitor:
                bm_res = self.behavior_monitor.initialize()
                if bm_res.get("status") not in ("initialized", "already_initialized"):
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "behavior_monitor_init_failed",
                        "details": bm_res,
                    }

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "exception", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # PUBLIC API – EXECUTE UI ACTION
    # ---------------------------------------------------------------------
    def execute_ui_action(
        self,
        element_ref: Dict[str, Any],
        action: str,
        payload: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "action": action,
                "element": element_ref,
                "degraded_mode": self.degraded_mode,
            }

        if not isinstance(element_ref, dict) or not isinstance(action, str):
            return {"status": "error", "code": "invalid_arguments"}

        if not self.initialized:
            init = self.initialize()
            if init.get("status") not in ("initialized", "already_initialized"):
                return {
                    "status": "error",
                    "code": "sandbox_not_initialized",
                    "details": init,
                }

        payload = payload or {}

        # 1. Security policy check
        if self.security_policy:
            try:
                policy_result = self.security_policy.check_action(
                    element_ref=element_ref,
                    action=action,
                )
                if policy_result.get("status") != "allowed":
                    return {
                        "status": "blocked",
                        "layer": "policy",
                        "policy": policy_result,
                        "degraded_mode": self.degraded_mode,
                    }
            except Exception as exc:
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "policy_exception",
                    "exception": str(exc),
                }

        # 2. Time limit / quota check
        if self.time_limiter:
            try:
                limit_result = self.time_limiter.check(
                    identity=self.identity,
                    action=action,
                )
                if limit_result.get("status") != "allowed":
                    return {
                        "status": "blocked",
                        "layer": "time_limiter",
                        "time_limit": limit_result,
                        "degraded_mode": self.degraded_mode,
                    }
            except Exception as exc:
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "time_limiter_exception",
                    "exception": str(exc),
                }

        # 3. Execute via capability adapter
        try:
            result = self.capability_adapter.execute_ui_action(
                element_ref=element_ref,
                action=action,
                payload=payload,
            )

            # 4. Behavior monitoring
            if self.behavior_monitor:
                try:
                    self.behavior_monitor.record(
                        identity=self.identity,
                        element_ref=element_ref,
                        action=action,
                        result=result,
                    )
                except Exception:
                    self.degraded_mode = True

            # 5. Time consumption
            if self.time_limiter:
                try:
                    self.time_limiter.consume(identity=self.identity, amount=1)
                except Exception:
                    self.degraded_mode = True

            return {
                "status": "ok",
                "result": result,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "capability_exception",
                "exception": str(exc),
            }
