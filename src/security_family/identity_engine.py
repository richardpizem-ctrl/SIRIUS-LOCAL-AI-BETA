"""
Security Family – Identity Engine 4.5.0 (PRO)
--------------------------------------------
Learns and recognizes OWNER and FAMILY behavior profiles.

Behavior Vector 3.1 – Dimensions (normalized 0–1):
- typing_speed
- command_pattern
- vocabulary
- task_type
- time_of_day
- error_rate

Features (4.5.0):
- Behavior Vector 3.1 normalization
- weighted cosine similarity
- adaptive learning (EMA, deterministic)
- multi-child FAMILY profiles (FAMILY_x)
- short-term vs long-term trends
- anomaly detection (similarity + behavior shift)
- stranger detection with penalties
- safe-mode and degraded-mode support
- Security Family 4.5 compliant
- no dynamic imports, no eval, no reflection
"""

import math
from statistics import mean


class IdentityEngine45:
    def __init__(self, profile_store):
        self.profile_store = profile_store

        # Behavior Vector 3.1 weights
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

        self.max_short = 20
        self.max_long = 200

        # Thresholds
        self.anomaly_similarity_threshold = 0.35
        self.anomaly_shift_threshold = 0.25
        self.stranger_penalty = 0.25
        self.high_stranger_threshold = 0.65

        # Runtime flags
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # LEARNING
    # ---------------------------------------------------------
    def learn_owner(self, data, learning_rate=0.2):
        if self.safe_mode:
            return

        try:
            vector = self._build_vector(data)
            self._update_profile("OWNER", vector, learning_rate=learning_rate)
            self._update_history("OWNER", vector)
        except Exception:
            self.degraded_mode = True

    def learn_family_member(self, data, member_id="default", learning_rate=0.2):
        if self.safe_mode:
            return

        try:
            key = f"FAMILY_{member_id}"
            vector = self._build_vector(data)
            self._update_profile(key, vector, learning_rate=learning_rate)
            self._update_history("FAMILY", vector)
        except Exception:
            self.degraded_mode = True

    # ---------------------------------------------------------
    # IDENTIFICATION
    # ---------------------------------------------------------
    def identify_user(self, data):
        """
        Returns:
        {
            "identity": str,
            "scores": {...},
            "anomaly": {...},
            "degraded_mode": bool
        }
        """

        if self.safe_mode:
            return {
                "identity": "STRANGER",
                "scores": {"OWNER": 0.0, "FAMILY": 0.0, "STRANGER": 1.0},
                "anomaly": {"is_anomaly": False, "reason": "safe_mode"},
                "degraded_mode": self.degraded_mode,
            }

        try:
            vector = self._build_vector(data)
            self._update_history("GLOBAL", vector)

            scores = {}

            # OWNER similarity
            owner_profile = self.profile_store.get("OWNER", {})
            scores["OWNER"] = self._similarity(vector, owner_profile)

            # FAMILY similarity (max across all children)
            family_scores = [
                self._similarity(vector, profile)
                for key, profile in self.profile_store.items()
                if key.startswith("FAMILY_")
            ]
            scores["FAMILY"] = max(family_scores) if family_scores else 0.0

            # Stranger score
            scores["STRANGER"] = 1 - max(scores["OWNER"], scores["FAMILY"])

            # Trends
            trends = self._compute_trends("GLOBAL")

            # Anomaly detection
            anomaly = self._detect_anomaly(scores, trends)

            # Penalize stranger score if anomaly detected
            if anomaly["is_anomaly"]:
                scores["STRANGER"] = min(1.0, scores["STRANGER"] + self.stranger_penalty)

            # Final identity
            identity = max(scores, key=scores.get)

            return {
                "identity": identity,
                "scores": scores,
                "anomaly": anomaly,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "identity": "STRANGER",
                "scores": {"OWNER": 0.0, "FAMILY": 0.0, "STRANGER": 1.0},
                "anomaly": {"is_anomaly": True, "reason": "internal_error"},
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # VECTOR BUILDING
    # ---------------------------------------------------------
    def _build_vector(self, data):
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
    # PROFILE UPDATE
    # ---------------------------------------------------------
    def _update_profile(self, key, vector, learning_rate=0.2):
        existing = self.profile_store.get(key, {})

        updated = {}
        for k, v in vector.items():
            if k in existing:
                updated[k] = (1 - learning_rate) * existing[k] + learning_rate * v
            else:
                updated[k] = v

        self.profile_store[key] = updated

    # ---------------------------------------------------------
    # SIMILARITY
    # ---------------------------------------------------------
    def _similarity(self, v1, v2):
        if not v2:
            return 0.0

        keys = set(v1.keys()) & set(v2.keys()) & set(self.weights.keys())
        if not keys:
            return 0.0

        a = [v1[k] for k in keys]
        b = [v2[k] for k in keys]
        w = [self.weights[k] for k in keys]

        dot = sum(x * y * w_i for x, y, w_i in zip(a, b, w))
        mag1 = math.sqrt(sum((x * w_i) ** 2 for x, w_i in zip(a, w)))
        mag2 = math.sqrt(sum((y * w_i) ** 2 for y, w_i in zip(b, w)))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot / (mag1 * mag2)

    # ---------------------------------------------------------
    # HISTORY & TRENDS
    # ---------------------------------------------------------
    def _update_history(self, label, vector):
        if label not in self.history:
            self.history[label] = []

        self.history[label].append(vector)

        if len(self.history[label]) > self.max_long:
            self.history[label] = self.history[label][-self.max_long:]

    def _compute_trends(self, label):
        records = self.history.get(label, [])
        if not records:
            return {"short": {}, "long": {}, "delta": {}}

        short = records[-self.max_short:]
        long = records

        def avg(vectors):
            keys = set().union(*vectors)
            return {k: mean([v.get(k, 0) for v in vectors]) for k in keys}

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
    def _detect_anomaly(self, scores, trends):
        owner_sim = scores.get("OWNER", 0.0)
        family_sim = scores.get("FAMILY", 0.0)
        stranger_sim = scores.get("STRANGER", 0.0)

        delta = trends.get("delta", {})
        shift = math.sqrt(sum(v * v for v in delta.values()))

        low_identity = max(owner_sim, family_sim) < self.anomaly_similarity_threshold
        high_stranger = stranger_sim > self.high_stranger_threshold
        big_shift = shift > self.anomaly_shift_threshold

        is_anomaly = low_identity or high_stranger or big_shift

        if is_anomaly:
            if high_stranger:
                reason = "high_stranger_similarity"
            elif low_identity and big_shift:
                reason = "low_identity_and_behavior_shift"
            elif low_identity:
                reason = "low_identity_similarity"
            else:
                reason = "behavior_shift"
        else:
            reason = "normal"

        return {
            "is_anomaly": is_anomaly,
            "reason": reason,
            "trend_delta": delta,
            "similarity": {
                "OWNER": owner_sim,
                "FAMILY": family_sim,
                "STRANGER": stranger_sim,
            },
        }
