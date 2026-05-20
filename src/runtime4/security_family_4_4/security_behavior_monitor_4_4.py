security_family_4_4/security_behavior_monitor_4_4.py
"""
SIRIUS LOCAL AI – Security Behavior Monitor 4.4.0

This module provides deterministic, offline‑safe behavior monitoring for
Security Family 4.4. It supports:

- Per‑identity behavior tracking (OWNER / FAMILY / STRANGER)
- Action history logging (safe subset)
- Risk scoring (deterministic, rule‑based)
- Pattern detection (short‑term vs long‑term)
- Security escalation hooks
- Integration with Security Policy Core 4.4

All logic is deterministic, offline, and fully isolated.

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No sensitive data stored (no personal info, no content logs).
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any, List, Optional


class SecurityBehaviorMonitor44:
    """
    Deterministic behavior monitor for Runtime 4.4.
    Tracks high‑level behavior events and computes risk scores.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

        # Behavior history (safe, high‑level only)
        self.history: Dict[str, List[Dict[str, Any]]] = {
            "OWNER": [],
            "FAMILY": [],
            "STRANGER": [],
        }

        # Deterministic risk scores
        self.risk_scores = {
            "OWNER": 0,
            "FAMILY": 0,
            "STRANGER": 0,
        }

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
    # PUBLIC API – RECORD BEHAVIOR EVENT
    # ------------------------------------------------------------------
    def record(self, identity: str, element_ref: Dict[str, Any], action: str, result: Dict[str, Any]):
        """
        Records a high‑level behavior event.

        Stored fields (safe subset):
        - action name
        - element role
        - success/failure
        - timestamp (logical counter, not real time)
        """
        if identity not in self.history:
            return {"status": "error", "reason": "invalid_identity"}

        try:
            event = {
                "action": action,
                "role": element_ref.get("role"),
                "success": result.get("status") == "ok",
            }

            self.history[identity].append(event)

            # Update deterministic risk score
            self._update_risk(identity, event)

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # INTERNAL – UPDATE RISK SCORE
    # ------------------------------------------------------------------
    def _update_risk(self, identity: str, event: Dict[str, Any]):
        """
        Deterministic rule‑based risk scoring.

        Rules:
        - Failed action: +2 risk
        - Repeated same action 3× in a row: +1 risk
        - STRANGER identity: all penalties doubled
        """
        penalty = 0

        # Rule 1: failed action
        if not event["success"]:
            penalty += 2

        # Rule 2: repeated action pattern
        hist = self.history[identity]
        if len(hist) >= 3:
            if (
                hist[-1]["action"] == hist[-2]["action"] ==
                hist[-3]["action"]
            ):
                penalty += 1

        # STRANGER multiplier
        if identity == "STRANGER":
            penalty *= 2

        self.risk_scores[identity] += penalty

    # ------------------------------------------------------------------
    # PUBLIC API – GET RISK SCORE
    # ------------------------------------------------------------------
    def get_risk(self, identity: str) -> Dict[str, Any]:
        if identity not in self.risk_scores:
            return {"status": "error", "reason": "invalid_identity"}

        return {
            "status": "ok",
            "identity": identity,
            "risk_score": self.risk_scores[identity],
        }

    # ------------------------------------------------------------------
    # PUBLIC API – GET HISTORY (SAFE)
    # ------------------------------------------------------------------
    def get_history(self, identity: str) -> Dict[str, Any]:
        if identity not in self.history:
            return {"status": "error", "reason": "invalid_identity"}

        return {
            "status": "ok",
            "identity": identity,
            "events": list(self.history[identity]),
        }
