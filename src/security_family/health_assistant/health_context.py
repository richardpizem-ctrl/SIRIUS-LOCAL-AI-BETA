"""
Health Context – Identity & Safety Context for Health Assistant 4.3.x
---------------------------------------------------------------------
Provides identity-aware context for safe, non-medical recommendations.

This module NEVER:
- interpretuje zdravotné údaje
- ukladá citlivé informácie
- robí medicínske rozhodnutia

Slúži len ako bezpečný, deterministický kontextový objekt.
"""


class HealthContext:
    """
    Context object used by HealthAssistant.
    Holds identity, safety notes, and runtime flags.
    """

    def __init__(self, identity: str = "OWNER") -> None:
        # Normalize identity
        self.identity = (identity or "OWNER").upper().strip()

        # Runtime flags
        self.safe_mode = False
        self.degraded_mode = False

        # Default safety note for unknown categories
        self.default_safety_note = self._build_default_note()

    # ------------------------------------------------------------
    # SAFETY NOTE BUILDER
    # ------------------------------------------------------------
    def _build_default_note(self) -> str:
        """
        Returns a safe fallback note depending on identity.
        Deterministic, offline, non-medical.
        """

        if self.identity == "CHILD":
            return "Ak sa necítiš dobre, povedz to dospelému, ktorému dôveruješ."

        if self.identity == "FAMILY":
            return "Ak sa to nezlepší, skús si oddýchnuť a sleduj svoj stav."

        if self.identity == "OWNER":
            return "Ak by sa tvoj stav zhoršil, sleduj to a v prípade potreby kontaktuj odborníka."

        # STRANGER or unknown identity
        return "Ak sa necítiš dobre, skús si oddýchnuť a sleduj svoj stav."

    # ------------------------------------------------------------
    # SAFE-MODE / DEGRADED-MODE HELPERS
    # ------------------------------------------------------------
    def enable_safe_mode(self):
        """Enables safe-mode (no processing, only safe defaults)."""
        self.safe_mode = True

    def disable_safe_mode(self):
        """Disables safe-mode."""
        self.safe_mode = False

    def mark_degraded(self):
        """Marks context as degraded-mode after internal error."""
        self.degraded_mode = True
