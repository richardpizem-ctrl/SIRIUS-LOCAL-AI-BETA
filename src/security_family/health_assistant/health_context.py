"""
Health Context – Identity & Safety Context for Health Assistant
---------------------------------------------------------------
Provides identity-aware context for safe, non-medical recommendations.

This module NEVER:
- interpretuje zdravotné údaje
- ukladá citlivé informácie
- robí medicínske rozhodnutia

Slúži len ako bezpečný kontextový objekt.
"""


class HealthContext:
    """
    Context object used by HealthAssistant.
    Holds identity and global safety notes.
    """

    def __init__(self, identity: str = "OWNER") -> None:
        # identity: OWNER / FAMILY / CHILD / STRANGER
        self.identity = identity.upper().strip()

        # Default safety note for unknown categories
        self.default_safety_note = self._build_default_note()

    def _build_default_note(self) -> str:
        """
        Returns a safe fallback note depending on identity.
        """

        if self.identity == "CHILD":
            return "Ak sa necítiš dobre, povedz to dospelému, ktorému dôveruješ."

        if self.identity == "FAMILY":
            return "Ak sa to nezlepší, skús si oddýchnuť a sleduj svoj stav."

        if self.identity == "OWNER":
            return "Ak by sa tvoj stav zhoršil, sleduj to a v prípade potreby kontaktuj odborníka."

        return "Ak sa necítiš dobre, skús si oddýchnuť a sleduj svoj stav."
