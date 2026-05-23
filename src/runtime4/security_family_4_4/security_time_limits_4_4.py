"""
SIRIUS LOCAL AI – Time Limits 4.5.0 (PRO)

TimeLimits 4.5 is the deterministic, offline‑safe time and quota
enforcement system inside Security Family 4.5.

It provides:
- Per‑identity usage quotas (OWNER / FAMILY / STRANGER)
- Session length limits
- Daily usage limits
- Cooldown enforcement
- Behavior‑aware adjustments (safe subset)
- Integration with Behavior Monitor 4.5 and Security Policy Core 4.5

Security Notes:
- No real‑time clocks used (logical counters only)
- Only static imports allowed
- No dynamic loading, no eval, no reflection
- Fully compatible with Security Family 4.5
"""

from typing import Dict, Any


class TimeLimits45:
    """
    Deterministic time & quota enforcement for Runtime 4.5 (PRO).
    """

    VALID_IDENTITIES = {"OWNER", "FAMILY", "STRANGER"}

    DEFAULT_LIMITS = {
        "OWNER": {
            "session_max": 999999,
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
        self.safe_mode = False
        self.degraded_mode = False
        self.version = "4.5"

        # Logical counters (no real time)
        self.session_usage = {"OWNER": 0, "FAMILY": 0, "STRANGER": 0}
        self.daily_usage = {"OWNER": 0, "FAMILY": 0, "STRANGER": 0}
        self.cooldown_remaining = {"OWNER": 0, "FAMILY": 0, "STRANGER": 0}

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
    # PUBLIC API – CHECK LIMITS
    # ------------------------------------------------------------------
    def check(self, identity: str, action: str) -> Dict[str, Any]:
        """
        Checks whether the identity is allowed to perform an action
        based on session, daily, and cooldown limits.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Time limit checks disabled in safe-mode.",
                "version": self.version,
            }

        if identity not in self.VALID_IDENTITIES:
            return {"status": "error", "code": "invalid_identity", "version": self.version}

        limits = self.DEFAULT_LIMITS[identity]

        # Cooldown check
        if self.cooldown_remaining[identity] > 0:
            return {
                "status": "blocked",
                "layer": "time_limits",
                "reason": "cooldown_active",
                "remaining": self.cooldown_remaining[identity],
                "version": self.version,
            }

        # Session limit check
        if self.session_usage[identity] >= limits["session_max"]:
            self.cooldown_remaining[identity] = limits["cooldown"]
            return {
                "status": "blocked",
                "layer": "time_limits",
                "reason": "session_limit_reached",
                "cooldown": limits["cooldown"],
                "version": self.version,
            }

        # Daily limit check
        if self.daily_usage[identity] >= limits["daily_max"]:
            return {
                "status": "blocked",
                "layer": "time_limits",
                "reason": "daily_limit_reached",
                "version": self.version,
            }

        return {"status": "allowed", "layer": "time_limits", "version": self.version}

    # ------------------------------------------------------------------
    # PUBLIC API – CONSUME TIME
    # ------------------------------------------------------------------
    def consume(self, identity: str, amount: int = 1) -> Dict[str, Any]:
        """
        Consumes logical time units.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Time consumption disabled in safe-mode.",
                "version": self.version,
            }

        if identity not in self.VALID_IDENTITIES:
            return {"status": "error", "code": "invalid_identity", "version": self.version}

        if not isinstance(amount, int) or amount <= 0:
            return {"status": "error", "code": "invalid_amount", "version": self.version}

        try:
            self.session_usage[identity] += amount
            self.daily_usage[identity] += amount

            # Reduce cooldowns for all identities
            for key in self.cooldown_remaining:
                if self.cooldown_remaining[key] > 0:
                    self.cooldown_remaining[key] -= 1

            return {"status": "ok", "version": self.version}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "consume_failed",
                "exception": str(exc),
                "version": self.version,
            }

    # ------------------------------------------------------------------
    # PUBLIC API – RESET SESSION
    # ------------------------------------------------------------------
    def reset_session(self, identity: str) -> Dict[str, Any]:
        if identity not in self.VALID_IDENTITIES:
            return {"status": "error", "code": "invalid_identity", "version": self.version}

        self.session_usage[identity] = 0
        return {"status": "ok", "version": self.version}

    # ------------------------------------------------------------------
    # PUBLIC API – RESET DAILY
    # ------------------------------------------------------------------
    def reset_daily(self, identity: str) -> Dict[str, Any]:
        if identity not in self.VALID_IDENTITIES:
            return {"status": "error", "code": "invalid_identity", "version": self.version}

        self.daily_usage[identity] = 0
        return {"status": "ok", "version": self.version}

    # ------------------------------------------------------------------
    # PUBLIC API – GET STATUS
    # ------------------------------------------------------------------
    def get_status(self, identity: str) -> Dict[str, Any]:
        if identity not in self.VALID_IDENTITIES:
            return {"status": "error", "code": "invalid_identity", "version": self.version}

        return {
            "status": "ok",
            "identity": identity,
            "session_used": self.session_usage[identity],
            "daily_used": self.daily_usage[identity],
            "cooldown_remaining": self.cooldown_remaining[identity],
            "limits": self.DEFAULT_LIMITS[identity],
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "version": self.version,
        }
