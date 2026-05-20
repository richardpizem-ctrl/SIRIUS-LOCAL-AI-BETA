"""
Health Router – Natural Language Routing Layer 4.4.0 (PRO)
----------------------------------------------------------
Routes natural‑language input into the HealthAssistant44 module.

Responsibilities:
- Accept text from NL Router v4 or other modules
- Normalize input
- Forward it to HealthAssistant44
- Enforce Security Family 4.4 rules
- Provide deterministic, identity‑aware, sandbox‑safe output
- Support safe‑mode and degraded‑mode behavior

No diagnoses, no medication advice, no medical claims.
"""

from .health_assistant_4_4 import HealthAssistant44


class HealthRouter44:
    """
    Lightweight NL routing wrapper for HealthAssistant44.
    Provides:
    - safe‑mode behavior
    - degraded‑mode detection
    - deterministic structured output
    """

    def __init__(self, identity: str = "OWNER") -> None:
        self.assistant = HealthAssistant44(identity=identity)

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.initialized: bool = True  # deterministic, no external deps

    # ------------------------------------------------------------------
    # ROUTING LOGIC
    # ------------------------------------------------------------------
    def route(self, text: str) -> dict:
        """
        Route natural‑language text into the HealthAssistant44.

        Returns dict:
        {
            "status": "ok" | "safe_mode" | "error",
            "category": str,
            "message": str,
            "safety_note": str,
            "identity": str,
            "degraded_mode": bool
        }
        """

        # SAFE‑MODE → no processing
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "category": "unknown",
                "message": "Health Router je v režime safe‑mode.",
                "safety_note": self.assistant.context.default_safety_note,
                "identity": self.assistant.context.identity,
                "degraded_mode": self.degraded_mode,
            }

        try:
            # Normalize input
            text = (text or "").strip()

            # Empty input → deterministic fallback
            if not text:
                return {
                    "status": "ok",
                    "category": "unknown",
                    "message": "Skús mi opísať, ako sa cítiš.",
                    "safety_note": self.assistant.context.default_safety_note,
                    "identity": self.assistant.context.identity,
                    "degraded_mode": self.degraded_mode,
                }

            # Delegate to HealthAssistant44
            result = self.assistant.handle(text)

            # Merge degraded‑mode flags
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
                "identity": self.assistant.context.identity,
                "exception": str(exc),
                "degraded_mode": True,
            }


__all__ = ["HealthRouter44"]
