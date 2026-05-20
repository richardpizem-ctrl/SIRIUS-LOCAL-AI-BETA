"""
Health Context – Identity & Safety Context for Health Assistant 4.4.0 (PRO)
---------------------------------------------------------------------------
Provides identity‑aware, deterministic, offline‑safe context for the
Health Assistant 4.4.0.

This module NEVER:
- interpretuje zdravotné údaje
- ukladá citlivé informácie
- robí medicínske rozhodnutia
- generuje medicínske odporúčania

Slúži len ako bezpečný, izolovaný kontextový objekt pre Security Family 4.4.
"""

class HealthContext44:
    """
    Context object used by HealthAssistant44.
    Holds identity, safety notes, and runtime flags.
    Deterministic, offline, Security Family 4.4 compliant.
    """

    VALID_IDENTITIES = {"OWNER", "FAMILY", "CHILD", "STRANGER"}

    def __init__(self, identity: str = "OWNER") -> None:
        # Normalize identity
        identity = (identity or "OWNER").upper().strip()
        if identity not in self.VALID_IDENTITIES:
            identity = "STRANGER"

        self.identity: str = identity

        # Runtime flags
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        # Deterministic default safety note
        self.default_safety_note: str = self._build_default_note()

    # ------------------------------------------------------------------
    # SAFETY NOTE BUILDER (DETERMINISTIC, OFFLINE)
    # ------------------------------------------------------------------
    def _build_default_note(self) -> str:
        """
        Returns a safe fallback note depending on identity.
        Deterministic, offline, non‑medical.
        """

        if self.identity == "CHILD":
            return "Ak sa necítiš dobre, povedz to dospelému, ktorému dôveruješ."

        if self.identity == "FAMILY":
            return "Ak sa to nezlepší, skús si oddýchnuť a sleduj svoj stav."

        if self.identity == "OWNER":
            return "Ak by sa tvoj stav zhoršil, sleduj to a v prípade potreby kontaktuj odborníka."

        # STRANGER (default)
        return "Ak sa necítiš dobre, skús si oddýchnuť a sleduj svoj stav."

    # ------------------------------------------------------------------
    # SAFE‑MODE / DEGRADED‑MODE HELPERS
    # ------------------------------------------------------------------
    def enable_safe_mode(self) -> None:
        """Enables safe‑mode (no processing, only safe defaults)."""
        self.safe_mode = True

    def disable_safe_mode(self) -> None:
        """Disables safe‑mode."""
        self.safe_mode = False

    def mark_degraded(self) -> None:
        """Marks context as degraded‑mode after internal error."""
        self.degraded_mode = True


__all__ = ["HealthContext44"]
