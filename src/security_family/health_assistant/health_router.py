"""
Health Router – Natural Language Routing Layer 4.5.0 (PRO)
----------------------------------------------------------
Routes natural‑language input into the HealthAssistant45 module.

Responsibilities:
- Accept text from NL Router v4 or other modules
- Normalize input
- Forward it to HealthAssistant45
- Enforce Security Family 4.5 rules
- Provide deterministic, identity‑aware, sandbox‑safe output
- Support safe‑mode and degraded‑mode behavior

No diagnoses, no medication advice, no medical claims.
"""

from .health_assistant_4_5 import HealthAssistant45


class HealthRouter45:
    """
    Lightweight NL routing wrapper for HealthAssistant45.
    Provides:
    - safe‑mode behavior
    - degraded‑mode detection
    - deterministic structured output
    """

    def __init__(self, identity: str = "OWNER") -> None:
        self.version = "4.5.0"
        self.assistant = HealthAssistant45(identity=identity)

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.initialized: bool = True  # deterministic, no external deps

    # ------------------------------------------------------------------
    # ROUTING LOGIC
    # ------------------------------------------------------------------
    def route(self, text: str) -> dict:
        """
        Route natural‑language text into the HealthAssistant45.

        Returns dict:
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

        # SAFE‑MODE → no processing
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "category": "unknown",
                "message": "Health Router je v režime safe‑mode.",
                "safety_note": self.assistant.context.default_safety_note,
                "identity": self.assistant.context.identity,
                "degraded_mode": self.degraded_mode,
                "version": self.version,
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
                    "version": self.version,
                }

            # Delegate to HealthAssistant45
            result = self.assistant.handle(text)

            # Merge degraded‑mode flags
            if result.get("degraded_mode"):
                self.degraded_mode = True

            # Inject version for consistency
            result["version"] = self.version
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
                "version": self.version,
            }


__all__ = ["HealthRouter45"]
