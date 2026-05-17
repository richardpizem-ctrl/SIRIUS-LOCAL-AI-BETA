"""
Health Router – Natural Language Routing Layer
----------------------------------------------
Routes natural language input into the HealthAssistant module.

This router:
- prijíma text od NL Router v4 alebo iných modulov
- normalizuje vstup
- odosiela ho do HealthAssistant
- vracia bezpečný, deterministický výstup

Žiadne diagnózy, žiadne lieky, žiadne medicínske tvrdenia.
"""

from . import HealthAssistant


class HealthRouter:
    """
    Lightweight NL routing wrapper for HealthAssistant.
    """

    def __init__(self, identity: str = "OWNER") -> None:
        self.assistant = HealthAssistant(identity=identity)

    def route(self, text: str) -> dict:
        """
        Route natural language text into the HealthAssistant.

        Returns dict:
        {
            "category": str,
            "message": str,
            "safety_note": str
        }
        """
        if not text or not text.strip():
            return {
                "category": "unknown",
                "message": "Skús mi opísať, ako sa cítiš.",
                "safety_note": self.assistant.context.default_safety_note,
            }

        return self.assistant.handle(text)
