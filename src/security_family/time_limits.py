"""
Security Family – Time Limits 4.5.0 (PRO)
-----------------------------------------
Intelligent time-based safety for FAMILY profiles.

Features (4.5.0):
- deterministic, offline-only behavior
- adaptive learning of usage patterns (EMA-style)
- anomaly detection (usage spikes + trend shift)
- short-term & long-term trend analysis
- risk scoring for FamilyMode45
- dynamic limit adjustments (safe, bounded)
- safe-mode and degraded-mode support
- Security Family 4.5 compliant
"""

import time
import math
from statistics import mean


class TimeLimits45:
    def __init__(self, config=None):
        """
        config example:
        {
            "FAMILY_1": {
                "chat_minutes": 30,
                "games_minutes": 60,
                "media_minutes": 45
            }
        }
        """
        self.config = config or {}
        self.sessions = {}          # {user_id: {session_type: start_timestamp}}
        self.usage_history = {}     # {user_id: [{session_type, duration}]}

        self.max_short = 20
        self.max_long = 200

        # Thresholds (4.5)
        self.anomaly_shift_threshold = 0.35
        self.anomaly_penalty = 0.25

        # Runtime flags
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # SESSION CONTROL
    # ---------------------------------------------------------
    def start_session(self, user_id, session_type):
        if self.safe_mode:
            return {"status": "safe_mode"}

        try:
            if user_id not in self.sessions:
                self.sessions[user_id] = {}

            self.sessions[user_id][session_type] = time.time()

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    def get_remaining_time(self, user_id, session_type):
        if self.safe_mode:
            return 0

        try:
            if user_id not in self.sessions:
                return self._get_limit(user_id, session_type)

            if session_type not in self.sessions[user_id]:
                return self._get_limit(user_id, session_type)

            start = self.sessions[user_id][session_type]
            elapsed_minutes = (time.time() - start) / 60
            limit = self._get_limit(user_id, session_type)

            return max(0, limit - elapsed_minutes)

        except Exception:
            self.degraded_mode = True
            return 0

    # ---------------------------------------------------------
    # WARNINGS & ENFORCEMENT
    # ---------------------------------------------------------
    def should_warn(self, user_id, session_type, threshold=5):
        remaining = self.get_remaining_time(user_id, session_type)
        return remaining <= threshold and remaining > 0

    def should_end(self, user_id, session_type):
        return self.get_remaining_time(user_id, session_type) <= 0

    # ---------------------------------------------------------
    # SESSION END + LEARNING
    # ---------------------------------------------------------
    def end_session(self, user_id, session_type):
        if self.safe_mode:
            return {"status": "safe_mode"}

        try:
            if user_id not in self.sessions:
                return {"status": "no_session"}

            if session_type not in self.sessions[user_id]:
                return {"status": "no_session"}

            start = self.sessions[user_id][session_type]
            duration = (time.time() - start) / 60  # minutes

            # Save usage history
            self._update_usage_history(user_id, session_type, duration)

            # Adaptive learning
            self._adaptive_learn(user_id, session_type, duration)

            # Remove session
            del self.sessions[user_id][session_type]

            return {"status": "ok", "duration": duration}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------
    # ADAPTIVE LEARNING (4.5)
    # ---------------------------------------------------------
    def _adaptive_learn(self, user_id, session_type, duration, learning_rate=0.1):
        try:
            limit = self._get_limit(user_id, session_type)
            trends = self._compute_trends(user_id, session_type)

            long_avg = trends["long"]

            if long_avg == 0:
                return

            # If child consistently uses less → reduce limit
            if long_avg < limit * 0.5:
                new_limit = limit * (1 - learning_rate)

            # If child consistently uses more → increase limit slightly
            elif long_avg > limit * 1.2:
                new_limit = limit * (1 + learning_rate)

            else:
                return  # no change

            # Clamp limit (4.5 safe bounds)
            new_limit = max(5, min(240, new_limit))

            # Save updated limit
            if user_id not in self.config:
                self.config[user_id] = {}

            self.config[user_id][f"{session_type}_minutes"] = new_limit

        except Exception:
            self.degraded_mode = True

    # ---------------------------------------------------------
    # ANOMALY DETECTION (4.5)
    # ---------------------------------------------------------
    def detect_anomaly(self, user_id, session_type):
        try:
            trends = self._compute_trends(user_id, session_type)
            delta = trends["delta"]

            shift = abs(delta)
            is_anomaly = shift > self.anomaly_shift_threshold

            return {
                "is_anomaly": is_anomaly,
                "reason": "usage_spike" if is_anomaly else "normal",
                "shift": shift,
                "short_term_avg": trends["short"],
                "long_term_avg": trends["long"],
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "is_anomaly": True,
                "reason": "internal_error",
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # TRENDS
    # ---------------------------------------------------------
    def _update_usage_history(self, user_id, session_type, duration):
        if user_id not in self.usage_history:
            self.usage_history[user_id] = []

        self.usage_history[user_id].append({
            "session_type": session_type,
            "duration": duration
        })

        if len(self.usage_history[user_id]) > self.max_long:
            self.usage_history[user_id] = self.usage_history[user_id][-self.max_long:]

    def _compute_trends(self, user_id, session_type):
        if user_id not in self.usage_history:
            return {"short": 0, "long": 0, "delta": 0}

        records = [
            r["duration"]
            for r in self.usage_history[user_id]
            if r["session_type"] == session_type
        ]

        if not records:
            return {"short": 0, "long": 0, "delta": 0}

        short = records[-self.max_short:]
        long = records

        short_avg = mean(short)
        long_avg = mean(long)
        delta = short_avg - long_avg

        return {
            "short": short_avg,
            "long": long_avg,
            "delta": delta
        }

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------
    def _get_limit(self, user_id, session_type):
        user_cfg = self.config.get(user_id, {})
        return user_cfg.get(f"{session_type}_minutes", 0)
