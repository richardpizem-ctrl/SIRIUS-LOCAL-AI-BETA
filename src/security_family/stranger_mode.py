"""
Security Family – Stranger Mode 4.5.0 (PRO)
-------------------------------------------
Activated when behavior does not match OWNER or FAMILY.

Provides:
- full isolation mode (4.5 hardened)
- safe-mode enforcement
- restricted permissions
- risk-aware activation
- anomaly-aware escalation
- deterministic, offline-only behavior
- safe-mode and degraded-mode support
- Security Family 4.5 compliant
"""

class StrangerMode45:
    def __init__(self, access_control, behavior_audit):
        self.access_control = access_control      # AccessControl45
        self.behavior_audit = behavior_audit      # BehaviorAudit45

        self.active = False
        self.safe_mode = False
        self.degraded_mode = False

        # Thresholds (4.5)
        self.high_risk_threshold = 0.65
        self.anomaly_penalty = 0.25

    # ---------------------------------------------------------
    # MAIN ACTIVATION
    # ---------------------------------------------------------
    def activate(self, behavior_data=None):
        """
        Returns:
        {
            "status": "ok" | "safe_mode" | "error",
            "mode": "STRANGER_MODE",
            "risk_score": float,
            "anomaly": dict,
            "permissions": list,
            "isolation": dict,
            "degraded_mode": bool
        }
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "mode": "STRANGER_MODE",
                "risk_score": 1.0,
                "anomaly": {"is_anomaly": False, "reason": "safe_mode"},
                "permissions": ["restricted_mode", "no_sensitive_actions"],
                "isolation": self._isolation_state(),
                "degraded_mode": self.degraded_mode,
            }

        try:
            self.active = True

            # 1. Calculate risk score
            risk, anomaly = self._calculate_risk(behavior_data)

            # 2. Build context for AccessControl45
            context = {
                "risk_score": risk,
                "school_mode": False,
                "time_limit_exceeded": False,
                "behavior_vector": behavior_data or {},
                "owner_similarity": 0.0,
                "family_similarity": 0.0,
            }

            # 3. Get restricted permissions
            permissions = self.access_control.get_permissions("STRANGER", context)

            return {
                "status": "ok",
                "mode": "STRANGER_MODE",
                "risk_score": risk,
                "anomaly": anomaly,
                "permissions": permissions,
                "isolation": self._isolation_state(),
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "mode": "STRANGER_MODE",
                "risk_score": 1.0,
                "anomaly": {"is_anomaly": True, "reason": "internal_error"},
                "permissions": ["restricted_mode", "no_sensitive_actions"],
                "isolation": self._isolation_state(),
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # INTERNAL RISK CALCULATION
    # ---------------------------------------------------------
    def _calculate_risk(self, behavior_data):
        if not behavior_data:
            return 1.0, {"is_anomaly": True, "reason": "no_data"}

        try:
            audit = self.behavior_audit.audit(behavior_data)

            stranger_score = audit.get("STRANGER", 1.0)
            anomaly = audit.get("ANOMALY", {"is_anomaly": False})

            risk = stranger_score

            if anomaly.get("is_anomaly"):
                risk += self.anomaly_penalty

            risk = max(0.0, min(1.0, risk))

            return risk, anomaly

        except Exception:
            self.degraded_mode = True
            return 1.0, {"is_anomaly": True, "reason": "internal_error"}

    # ---------------------------------------------------------
    # ISOLATION STATE (4.5 hardened)
    # ---------------------------------------------------------
    def _isolation_state(self):
        return {
            "fs_agent": True,
            "win_cap": True,
            "workflow_engine": True,
            "plugins": True,
            "network": True,
            "vault_access": False,
            "system_settings": False,
            "ui_automation": False,
            "clipboard": False,
            "local_storage": False
        }
