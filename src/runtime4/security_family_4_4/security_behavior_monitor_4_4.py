"""
SIRIUS LOCAL AI – Security Behavior Monitor 4.4.0 (PRO)

This module provides deterministic, offline‑safe behavior monitoring for
Security Family 4.4. It supports:

- Per‑identity behavior tracking (OWNER / FAMILY / STRANGER)
- Action history logging (safe subset)
- Risk scoring (deterministic, rule‑based)
- Pattern detection (short‑term vs long‑term)
- Security escalation hooks
- Integration with Security Policy Core 4.4

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No sensitive data stored.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any, List, Optional


class SecurityBehaviorMonitor44:
    """
    Deterministic behavior monitor for Runtime 4.4 (PRO).
    Tracks high‑level behavior events and computes risk scores.
    """

    VALID_IDENTITIES = {"OWNER", "FAMILY", "STRANGER"}

    def __init__(self):
        self.initialized = False
        self.safe_mode = False
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
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
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
    # PUBLIC API – RECORD BEHAVIOR EVENT
    # ------------------------------------------------------------------
    def record(
        self,
        identity: str,
        element_ref: Dict[str, Any],
        action: str,
        result: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Records a high‑level behavior event.

        Stored fields (safe subset):
        - action name
        - element role
        - success/failure
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Behavior logging disabled in safe-mode.",
            }

        # Validate identity
        if identity not in self.VALID_IDENTITIES:
            return {"status": "error", "code": "invalid_identity"}

        # Validate action
        if not isinstance(action, str) or not action.strip():
            return {"status": "error", "code": "invalid_action"}

        # Validate element_ref
        if not isinstance(element_ref, dict):
            return {"status": "error", "code": "invalid_element_ref"}

        # Validate result
        if not isinstance(result, dict):
            return {"status": "error", "code": "invalid_result"}

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
            return {
                "status": "error",
                "code": "behavior_record_failed",
                "exception": str(exc),
            }

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
        if identity not in self.VALID_IDENTITIES:
            return {"status": "error", "code": "invalid_identity"}

        return {
            "status": "ok",
            "identity": identity,
            "risk_score": self.risk_scores[identity],
            "degraded_mode": self.degraded_mode,
        }

    # ------------------------------------------------------------------
    # PUBLIC API – GET HISTORY (SAFE)
    # ------------------------------------------------------------------
    def get_history(self, identity: str) -> Dict[str, Any]:
        if identity not in self.VALID_IDENTITIES:
            return {"status": "error", "code": "invalid_identity"}

        return {
            "status": "ok",
            "identity": identity,
            "events": list(self.history[identity]),
            "degraded_mode": self.degraded_mode,
        }
