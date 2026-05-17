"""
SIRIUS LOCAL AI – Security Family / Health Assistant 4.3.x
----------------------------------------------------------
Non-medical, offline, rule-based helper for basic well‑being and
"first aid" style recommendations. No diagnoses, no medication advice,
no medical claims.

This module:
- accepts natural language descriptions of how the user feels
- maps them to safe, generic recommendation categories
- returns short, identity‑aware, sandbox‑safe responses
- supports safe-mode and degraded-mode behavior
"""

from .health_rules import classify_health_state
from .health_responses import build_response
from .health_context import HealthContext


class HealthAssistant:
    """
    Entry point for the Health Assistant inside Security Family.

    Usage:
        assistant = HealthAssistant(identity="OWNER")
        reply = assistant.handle("bolí ma hlava a som unavený")
    """

    def __init__(self, identity: str = "OWNER") -> None:
        # identity: OWNER / FAMILY / CHILD / STRANGER
        self.context = HealthContext(identity=identity)

        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------
    # MAIN HANDLER
    # ------------------------------------------------------------
    def handle(self, user_text: str) -> dict:
        """
        Process user input and return a safe, non-medical recommendation.

        Returns a dict:
        {
            "status": "ok" | "safe_mode" | "error",
            "category": str,
            "message": str,
            "safety_note": str,
            "degraded_mode": bool
        }
        """

        # Safe-mode → no processing
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "category": "unknown",
                "message": "Health Assistant je v safe-mode.",
                "safety_note": self.context.default_safety_note,
                "degraded_mode": self.degraded_mode,
            }

        try:
            user_text = (user_text or "").strip()
            if not user_text:
                return {
                    "status": "ok",
                    "category": "unknown",
                    "message": "Nerozumiem presne, čo cítiš. Skús mi to opísať trochu konkrétnejšie.",
                    "safety_note": self.context.default_safety_note,
                    "degraded_mode": self.degraded_mode,
                }

            # Classification (rule-based, deterministic)
            category = classify_health_state(user_text, self.context)

            # Build safe response
            response = build_response(category, self.context)

            return {
                "status": "ok",
                "category": response["category"],
                "message": response["message"],
                "safety_note": response["safety_note"],
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "category": "unknown",
                "message": "Vyskytla sa interná chyba pri spracovaní textu.",
                "safety_note": self.context.default_safety_note,
                "exception": str(exc),
                "degraded_mode": self.degraded_mode,
            }


__all__ = ["HealthAssistant"]
