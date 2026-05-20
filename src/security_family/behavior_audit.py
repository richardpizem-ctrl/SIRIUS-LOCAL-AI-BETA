"""
Security Family – Behavior Audit 4.4.0 (PRO)
--------------------------------------------
Deterministic behavior-based identity scoring engine.

Behavior Vector 3.1 – Dimensions (normalized 0–1):
- typing_speed
- command_pattern
- vocabulary
- task_type
- time_of_day
- error_rate

Features (4.4.0):
- weighted cosine similarity (OWNER / FAMILY)
- stranger score = 1 - max(OWNER_sim, FAMILY_sim)
- adaptive learning (EMA-style, deterministic)
- short-term vs long-term trend analysis
- anomaly detection (similarity + behavior shift)
- safe-mode and degraded-mode support
- Security Family 4.4 compliant
- no dynamic imports, no eval, no reflection
"""

import math
from statistics import mean


class BehaviorAudit44:
    def __init__(self, profile_store):
        self.profile_store = profile_store

        # Weighted importance of each dimension
        self.weights = {
            "command_pattern": 0.40,
            "typing_speed": 0.25,
            "vocabulary": 0.15,
            "task_type": 0.10,
            "error_rate": 0.05,
            "time_of_day": 0.05,
        }

        # Normalization ranges
        self.norm_ranges = {
            "typing_speed": (0, 300),
            "command_pattern": (0, 1),
            "vocabulary": (0, 1),
            "task_type": (0, 1),
            "time_of_day": (0, 24),
            "error_rate": (0, 1),
        }

        # Behavior history
        self.history = {
            "OWNER": [],
            "FAMILY": [],
            "GLOBAL": [],
        }

        self.max_short_term = 20
        self.max_long_term = 200

        # Thresholds
        self.anomaly_similarity_threshold = 0.35
        self.anomaly_trend_delta_threshold = 0.25

        # Runtime flags
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------
    def audit(self, data):
        """
        Returns:
        {
            "OWNER": float,
            "FAMILY": float,
            "STRANGER": float,
            "ANOMALY": {...},
            "TRENDS": {...},
            "degraded_mode": bool
        }
        """

        if self.safe_mode:
            return {
                "OWNER": 0.0,
                "FAMILY": 0.0,
                "STRANGER": 1.0,
                "ANOMALY": {"is_anomaly": False, "reason": "safe_mode"},
                "TRENDS": {},
                "degraded_mode": self.degraded_mode,
            }

        try:
            owner = self.profile_store.get("OWNER", {})
            family = self.profile_store.get("FAMILY", {})

            # Build normalized vector
            vector = self._build_behavior_vector(data)

            # Similarities
            owner_score = self._compare_profiles(vector, owner)
            family_score = self._compare_profiles(vector, family)
            stranger_score = self._stranger_score(vector, owner, family)

            # Update history
            self._update_history("GLOBAL", vector)

            # Trends
            trends = self._compute_trends("GLOBAL")

            # Anomaly detection
            anomaly = self._detect_anomaly(
                vector,
                owner_score,
                family_score,
                trends,
            )

            return {
                "OWNER": owner_score,
                "FAMILY": family_score,
                "STRANGER": stranger_score,
                "ANOMALY": anomaly,
                "TRENDS": trends,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "OWNER": 0.0,
                "FAMILY": 0.0,
                "STRANGER": 1.0,
                "ANOMALY": {"is_anomaly": True, "reason": "internal_error"},
                "TRENDS": {},
                "exception": str(exc),
                "degraded_mode": True,
            }

    def learn(self, label, data, learning_rate=0.2):
        """
        Adaptive learning of OWNER/FAMILY profiles (deterministic EMA).
        """
        if label not in ("OWNER", "FAMILY"):
            return

        try:
            vector = self._build_behavior_vector(data)
            profile = self.profile_store.get(label, {})

            if not profile:
                self.profile_store[label] = vector.copy()
            else:
                updated = {}
                for k in self.weights.keys():
                    old = profile.get(k, vector.get(k, 0.0))
                    new = vector.get(k, old)
                    updated[k] = (1 - learning_rate) * old + learning_rate * new
                self.profile_store[label] = updated

            self._update_history(label, vector)

        except Exception:
            self.degraded_mode = True

    # ---------------------------------------------------------
    # INTERNAL – VECTOR BUILDING
    # ---------------------------------------------------------
    def _build_behavior_vector(self, data):
        vector = {}
        for k in self.weights.keys():
            if k in data:
                vector[k] = self._normalize(k, data[k])
        return vector

    def _normalize(self, key, value):
        if key not in self.norm_ranges:
            return 0.0

        min_v, max_v = self.norm_ranges[key]
        if max_v == min_v:
            return 0.0

        norm = (value - min_v) / (max_v - min_v)
        return max(0.0, min(1.0, norm))

    # ---------------------------------------------------------
    # INTERNAL – SIMILARITY
    # ---------------------------------------------------------
    def _compare_profiles(self, vector, profile):
        if not profile:
            return 0.0

        keys = set(vector.keys()) & set(profile.keys()) & set(self.weights.keys())
        if not keys:
            return 0.0

        v1 = [vector[k] for k in keys]
        v2 = [profile[k] for k in keys]
        w = [self.weights[k] for k in keys]

        dot = sum(a * b * weight for a, b, weight in zip(v1, v2, w))
        mag1 = math.sqrt(sum((a * weight) ** 2 for a, weight in zip(v1, w)))
        mag2 = math.sqrt(sum((b * weight) ** 2 for b, weight in zip(v2, w)))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot / (mag1 * mag2)

    def _stranger_score(self, vector, owner, family):
        owner_sim = self._compare_profiles(vector, owner)
        family_sim = self._compare_profiles(vector, family)
        return 1 - max(owner_sim, family_sim)

    # ---------------------------------------------------------
    # INTERNAL – HISTORY & TRENDS
    # ---------------------------------------------------------
    def _update_history(self, label, vector):
        if label not in self.history:
            self.history[label] = []

        self.history[label].append(vector)

        if len(self.history[label]) > self.max_long_term:
            self.history[label] = self.history[label][-self.max_long_term:]

    def _compute_trends(self, label):
        records = self.history.get(label, [])
        if not records:
            return {"short_term_avg": {}, "long_term_avg": {}, "delta": {}}

        short = records[-self.max_short_term:]
        long = records

        def avg(vectors):
            if not vectors:
                return {}
            keys = set().union(*vectors)
            return {k: mean([v.get(k, 0.0) for v in vectors]) for k in keys}

        short_avg = avg(short)
        long_avg = avg(long)

        delta = {
            k: short_avg.get(k, 0.0) - long_avg.get(k, 0.0)
            for k in set(short_avg) | set(long_avg)
        }

        return {
            "short_term_avg": short_avg,
            "long_term_avg": long_avg,
            "delta": delta,
        }

    # ---------------------------------------------------------
    # INTERNAL – ANOMALY DETECTION
    # ---------------------------------------------------------
    def _detect_anomaly(self, vector, owner_sim, family_sim, trends):
        max_sim = max(owner_sim, family_sim)
        delta = trends.get("delta", {})

        shift = math.sqrt(sum(v * v for v in delta.values()))

        low_similarity = max_sim < self.anomaly_similarity_threshold
        big_shift = shift > self.anomaly_trend_delta_threshold

        is_anomaly = low_similarity or big_shift

        if is_anomaly:
            if low_similarity and big_shift:
                reason = "low_similarity_and_behavior_shift"
            elif low_similarity:
                reason = "low_similarity"
            else:
                reason = "behavior_shift"
        else:
            reason = "normal"

        return {
            "is_anomaly": is_anomaly,
            "reason": reason,
            "similarity": {"OWNER": owner_sim, "FAMILY": family_sim},
            "trend_delta": delta,
        }
