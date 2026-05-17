"""
Health Router – Natural Language Routing Layer 4.3.x
----------------------------------------------------
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
    Provides:
    - safe-mode behavior
    - degraded-mode detection
    - structured output
    """

    def __init__(self, identity: str = "OWNER") -> None:
        self.assistant = HealthAssistant(identity=identity)

        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------
    # ROUTING LOGIC
    # ------------------------------------------------------------
    def route(self, text: str) -> dict:
        """
        Route natural language text into the HealthAssistant.

        Returns dict:
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
                "message": "Health Router je v safe-mode.",
                "safety_note": self.assistant.context.default_safety_note,
                "degraded_mode": self.degraded_mode,
            }

        try:
            # Normalize input
            text = (text or "").strip()

            if not text:
                return {
                    "status": "ok",
                    "category": "unknown",
                    "message": "Skús mi opísať, ako sa cítiš.",
                    "safety_note": self.assistant.context.default_safety_note,
                    "degraded_mode": self.degraded_mode,
                }

            # Delegate to HealthAssistant
            result = self.assistant.handle(text)

            # Merge degraded-mode flags
            if result.get("degraded_mode"):
                self.degraded_mode = True

            return result

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "category": "unknown",
                "message": "Vyskytla sa interná chyba pri spracovaní textu.",
                "safety_note": self.assistant.context.default_safety_note,
                "exception": str(exc),
                "degraded_mode": True,
            }


__all__ = ["HealthRouter"]
