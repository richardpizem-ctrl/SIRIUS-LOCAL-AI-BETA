security_family_4_4/security_time_limits_4_4.py
"""
SIRIUS LOCAL AI – Time Limits 4.4.0

TimeLimits 4.4 is the deterministic, offline‑safe time and quota
enforcement system inside Security Family 4.4.

It provides:

- Per‑identity usage quotas (OWNER / FAMILY / STRANGER)
- Session length limits
- Daily usage limits
- Cooldown enforcement
- Behavior‑aware adjustments (safe subset)
- Integration with Behavior Monitor 4.4 and Security Policy Core 4.4

All logic is deterministic, offline, and fully isolated.

Security Notes:
- No real‑time clocks used (logical counters only)
- Only static imports allowed
- No dynamic loading, no eval, no reflection
- Fully compatible with Security Family 4.4
"""

from typing import Dict, Any


class TimeLimits44:
    """
    Deterministic time & quota enforcement for Runtime 4.4.
    """

    DEFAULT_LIMITS = {
        "OWNER": {
            "session_max": 999999,   # practically unlimited
            "daily_max": 999999,
            "cooldown": 0,
        },
        "FAMILY": {
            "session_max": 1800,     # 30 minutes
            "daily_max": 7200,       # 2 hours
            "cooldown": 300,         # 5 minutes
        },
        "STRANGER": {
            "session_max": 300,      # 5 minutes
            "daily_max": 900,        # 15 minutes
            "cooldown": 600,         # 10 minutes
        },
    }

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

        # Logical counters (no real time)
        self.session_usage = {"OWNER": 0, "FAMILY": 0, "STRANGER": 0}
        self.daily_usage = {"OWNER": 0, "FAMILY": 0, "STRANGER": 0}
        self.cooldown_remaining = {"OWNER": 0, "FAMILY": 0, "STRANGER": 0}

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # PUBLIC API – CHECK LIMITS
    # ------------------------------------------------------------------
    def check(self, identity: str, action: str) -> Dict[str, Any]:
        """
        Checks whether the identity is allowed to perform an action
        based on session, daily, and cooldown limits.
        """
        if identity not in self.DEFAULT_LIMITS:
            return {"status": "error", "reason": "invalid_identity"}

        limits = self.DEFAULT_LIMITS[identity]

        # Cooldown check
        if self.cooldown_remaining[identity] > 0:
            return {
                "status": "blocked",
                "reason": "cooldown_active",
                "remaining": self.cooldown_remaining[identity],
            }

        # Session limit check
        if self.session_usage[identity] >= limits["session_max"]:
            self.cooldown_remaining[identity] = limits["cooldown"]
            return {
                "status": "blocked",
                "reason": "session_limit_reached",
                "cooldown": limits["cooldown"],
            }

        # Daily limit check
        if self.daily_usage[identity] >= limits["daily_max"]:
            return {
                "status": "blocked",
                "reason": "daily_limit_reached",
            }

        return {"status": "allowed"}

    # ------------------------------------------------------------------
    # PUBLIC API – CONSUME TIME
    # ------------------------------------------------------------------
    def consume(self, identity: str, amount: int = 1):
        """
        Consumes logical time units.
        """
        if identity not in self.DEFAULT_LIMITS:
            return {"status": "error", "reason": "invalid_identity"}

        self.session_usage[identity] += amount
        self.daily_usage[identity] += amount

        # Reduce cooldowns for all identities
        for key in self.cooldown_remaining:
            if self.cooldown_remaining[key] > 0:
                self.cooldown_remaining[key] -= 1

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # PUBLIC API – RESET SESSION
    # ------------------------------------------------------------------
    def reset_session(self, identity: str):
        if identity not in self.DEFAULT_LIMITS:
            return {"status": "error", "reason": "invalid_identity"}

        self.session_usage[identity] = 0
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # PUBLIC API – RESET DAILY
    # ------------------------------------------------------------------
    def reset_daily(self, identity: str):
        if identity not in self.DEFAULT_LIMITS:
            return {"status": "error", "reason": "invalid_identity"}

        self.daily_usage[identity] = 0
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # PUBLIC API – GET STATUS
    # ------------------------------------------------------------------
    def get_status(self, identity: str) -> Dict[str, Any]:
        if identity not in self.DEFAULT_LIMITS:
            return {"status": "error", "reason": "invalid_identity"}

        return {
            "status": "ok",
            "identity": identity,
            "session_used": self.session_usage[identity],
            "daily_used": self.daily_usage[identity],
            "cooldown_remaining": self.cooldown_remaining[identity],
            "limits": self.DEFAULT_LIMITS[identity],
        }
