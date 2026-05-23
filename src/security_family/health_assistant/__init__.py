"""
SIRIUS LOCAL AI – Security Family / Health Assistant 4.5.0 (PRO)

Non‑medical, offline, deterministic helper for basic well‑being and
"first‑aid style" recommendations. No diagnoses, no medication advice,
no medical claims.

Responsibilities (4.5.0):
- Accept natural‑language descriptions of how the user feels
- Map them to safe, generic recommendation categories
- Produce identity‑aware, sandbox‑safe responses
- Enforce Security Family 4.5 rules
- Support safe‑mode and degraded‑mode behavior
- Deterministic, offline‑only rule engine

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- Fully compatible with Security Family 4.5.
"""

from .health_rules import classify_health_state
from .health_responses import build_response
from .health_context import HealthContext


class HealthAssistant45:
    """
    Entry point for the Health Assistant inside Security Family 4.5.

    Usage:
        assistant = HealthAssistant45(identity="OWNER")
        reply = assistant.handle("bolí ma hlava a som unavený")
    """

    VALID_IDENTITIES = {"OWNER", "FAMILY", "CHILD", "STRANGER"}

    def __init__(self, identity: str = "OWNER") -> None:
        # Validate identity
        if identity not in self.VALID_IDENTITIES:
            identity = "STRANGER"

        self.version = "4.5.0"
        self.context = HealthContext(identity=identity)

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.initialized: bool = True  # deterministic, no external deps

    # ------------------------------------------------------------------
    # PUBLIC API – MAIN HANDLER
    # ------------------------------------------------------------------
    def handle(self, user_text: str) -> dict:
        """
        Process user input and return a safe, non‑medical recommendation.

        Returns:
        {
            "status": "ok" | "safe_mode" | "error",
            "category": str,
            "message": str,
            "safety_note": str,
            "identity": str,
            "degraded_mode": bool,
            "version": "4.5.0"
        }
        """

        # Safe‑mode → no processing
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "category": "unknown",
                "message": "Health Assistant je v režime safe‑mode.",
                "safety_note": self.context.default_safety_note,
                "identity": self.context.identity,
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

        try:
            # Normalize input
            user_text = (user_text or "").strip()

            # Empty input → deterministic fallback
            if not user_text:
                return {
                    "status": "ok",
                    "category": "unknown",
                    "message": (
                        "Nerozumiem presne, čo cítiš. "
                        "Skús mi to opísať trochu konkrétnejšie."
                    ),
                    "safety_note": self.context.default_safety_note,
                    "identity": self.context.identity,
                    "degraded_mode": self.degraded_mode,
                    "version": self.version,
                }

            # 1. Deterministic classification
            category = classify_health_state(user_text, self.context)

            # 2. Build safe response
            response = build_response(category, self.context)

            return {
                "status": "ok",
                "category": response["category"],
                "message": response["message"],
                "safety_note": response["safety_note"],
                "identity": self.context.identity,
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "category": "unknown",
                "message": (
                    "Vyskytla sa interná chyba pri spracovaní textu. "
                    "Skús to prosím zopakovať."
                ),
                "safety_note": self.context.default_safety_note,
                "identity": self.context.identity,
                "exception": str(exc),
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }


__all__ = ["HealthAssistant45"]
