"""
SIRIUS LOCAL AI – Security Family / Health Assistant
----------------------------------------------------
Non-medical, offline, rule-based helper for basic well‑being and "first aid"
style recommendations. No diagnoses, no medication advice, no medical claims.

This module:
- accepts natural language descriptions of how the user feels
- maps them to safe, generic recommendation categories
- returns short, identity‑aware, sandbox‑safe responses
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

    def handle(self, user_text: str) -> dict:
        """
        Process user input and return a safe, non-medical recommendation.

        Returns a dict:
        {
            "category": "hydration" | "rest" | "stress" | "unknown" | ...,
            "message": str,
            "safety_note": str
        }
        """
        user_text = (user_text or "").strip()
        if not user_text:
            return {
                "category": "unknown",
                "message": "Nerozumiem presne, čo cítiš. Skús mi to opísať trochu konkrétnejšie.",
                "safety_note": self.context.default_safety_note,
            }

        category = classify_health_state(user_text, self.context)
        response = build_response(category, self.context)
        return response


__all__ = ["HealthAssistant"]
