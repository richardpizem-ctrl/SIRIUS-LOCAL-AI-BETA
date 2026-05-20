"""
Security Family – Family Mode 4.4.0 (PRO)
-----------------------------------------
Safe environment for children of the owner.

Features (4.4.0):
- behavior-based risk scoring (via BehaviorAudit44)
- anomaly-aware safety mode
- time-limit enforcement (TimeLimits44)
- schoolwork priority mode
- deterministic, offline-only behavior
- safe-mode and degraded-mode support
- Security Family 4.4 compliant
"""

import math


class FamilyMode44:
    def __init__(self, access_control, behavior_audit, time_limits):
        self.access_control = access_control        # AccessControl44
        self.behavior_audit = behavior_audit        # BehaviorAudit44
        self.time_limits = time_limits              # TimeLimits44

        self.active = False
        self.school_mode = False

        # Behavior history for trends
        self.history = []
        self.max_short = 20
        self.max_long = 200

        # Thresholds
        self.safe_mode_threshold = 0.65
        self.anomaly_penalty = 0.25

        # Runtime flags
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # MAIN ACTIVATION
    # ---------------------------------------------------------
    def activate(self, behavior_data=None):
        """
        Returns:
        {
            "status": "ok" | "safe_mode" | "error",
            "mode": "FAMILY_MODE" | "SAFE_MODE",
            "school_mode": bool,
            "risk_score": float,
            "anomaly": dict,
            "time_limit_exceeded": bool,
            "permissions": list,
            "degraded_mode": bool
        }
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "mode": "SAFE_MODE",
                "school_mode": self.school_mode,
                "risk_score": 1.0,
                "anomaly": {"is_anomaly": False, "reason": "safe_mode"},
                "time_limit_exceeded": False,
                "permissions": ["restricted_mode", "no_sensitive_actions"],
                "degraded_mode": self.degraded_mode,
            }

        try:
            self.active = True

            # 1. Behavior audit → risk score
            risk, audit_scores, anomaly = self._calculate_risk(behavior_data)

            # 2. Time limit enforcement
            time_exceeded = self.time_limits.exceeded("FAMILY")

            # 3. Build context for AccessControl44
            context = {
                "risk_score": risk,
                "school_mode": self.school_mode,
                "time_limit_exceeded": time_exceeded,
                "behavior_vector": behavior_data or {},
                "owner_similarity": audit_scores.get("OWNER", 0),
                "family_similarity": audit_scores.get("FAMILY", 0),
            }

            # 4. Get dynamic permissions
            permissions = self.access_control.get_permissions("FAMILY", context)

            # 5. Determine mode
            mode = "SAFE_MODE" if risk > self.safe_mode_threshold else "FAMILY_MODE"

            return {
                "status": "ok",
                "mode": mode,
                "school_mode": self.school_mode,
                "risk_score": risk,
                "anomaly": anomaly,
                "time_limit_exceeded": time_exceeded,
                "permissions": permissions,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "mode": "SAFE_MODE",
                "school_mode": self.school_mode,
                "risk_score": 1.0,
                "anomaly": {"is_anomaly": True, "reason": "internal_error"},
                "time_limit_exceeded": False,
                "permissions": ["restricted_mode", "no_sensitive_actions"],
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # SCHOOL MODE
    # ---------------------------------------------------------
    def enable_school_mode(self):
        self.school_mode = True

    def disable_school_mode(self):
        self.school_mode = False

    # ---------------------------------------------------------
    # INTERNAL RISK CALCULATION
    # ---------------------------------------------------------
    def _calculate_risk(self, behavior_data):
        if not behavior_data:
            return 0.0, {}, {"is_anomaly": False, "reason": "no_data"}

        try:
            # 1. Behavior audit
            audit_scores = self.behavior_audit.audit(behavior_data)
            family_score = audit_scores.get("FAMILY", 0)
            stranger_score = audit_scores.get("STRANGER", 0)

            # 2. Update history
            self._update_history(behavior_data)
            trends = self._compute_trends()

            # 3. Detect anomaly
            anomaly = self._detect_anomaly(audit_scores, trends)

            # 4. Base risk = stranger score
            risk = stranger_score

            # 5. Add anomaly penalty
            if anomaly["is_anomaly"]:
                risk += self.anomaly_penalty

            # 6. Clamp
            risk = max(0.0, min(1.0, risk))

            return risk, audit_scores, anomaly

        except Exception:
            self.degraded_mode = True
            return 1.0, {}, {"is_anomaly": True, "reason": "internal_error"}

    # ---------------------------------------------------------
    # HISTORY & TRENDS
    # ---------------------------------------------------------
    def _update_history(self, vector):
        self.history.append(vector)
        if len(self.history) > self.max_long:
            self.history = self.history[-self.max_long:]

    def _compute_trends(self):
        if not self.history:
            return {"short": {}, "long": {}, "delta": {}}

        short = self.history[-self.max_short:]
        long = self.history

        def avg(vectors):
            keys = set().union(*vectors)
            return {k: sum(v.get(k, 0) for v in vectors) / len(vectors) for k in keys}

        short_avg = avg(short)
        long_avg = avg(long)

        delta = {
            k: short_avg.get(k, 0) - long_avg.get(k, 0)
            for k in set(short_avg) | set(long_avg)
        }

        return {"short": short_avg, "long": long_avg, "delta": delta}

    # ---------------------------------------------------------
    # ANOMALY DETECTION
    # ---------------------------------------------------------
    def _detect_anomaly(self, audit_scores, trends):
        family_sim = audit_scores.get("FAMILY", 0)
        stranger_sim = audit_scores.get("STRANGER", 0)

        delta = trends.get("delta", {})
        shift = math.sqrt(sum(v * v for v in delta.values()))

        low_family = family_sim < 0.35
        high_stranger = stranger_sim > 0.65
        big_shift = shift > 0.25

        is_anomaly = low_family or high_stranger or big_shift

        if is_anomaly:
            if high_stranger:
                reason = "high_stranger_similarity"
            elif low_family and big_shift:
                reason = "low_family_and_behavior_shift"
            elif low_family:
                reason = "low_family_similarity"
            else:
                reason = "behavior_shift"
        else:
            reason = "normal"

        return {
            "is_anomaly": is_anomaly,
            "reason": reason,
            "trend_delta": delta,
            "similarity": {
                "FAMILY": family_sim,
                "STRANGER": stranger_sim,
            },
        }
