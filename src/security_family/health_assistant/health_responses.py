"""
Health Responses – Safe Recommendation Generator 4.4.0 (PRO)
------------------------------------------------------------
Generates non‑medical, offline, identity‑aware recommendations based on
classified categories from health_rules_4_4.py.

This module NEVER:
- dáva diagnózy
- odporúča lieky
- robí medicínske tvrdenia

Len bezpečné, všeobecné, deterministické odporúčania.
"""

from typing import Dict


# ---------------------------------------------------------------------
# BASE RESPONSES (DETERMINISTIC, OFFLINE, NON‑MEDICAL)
# ---------------------------------------------------------------------
BASE_RESPONSES = {
    "hydration": "Skús sa napiť vody. Niekedy aj mierna dehydratácia spôsobí nepríjemné pocity.",
    "rest": "Skús si na chvíľu oddýchnuť. Krátka pauza alebo spánok môže výrazne pomôcť.",
    "stress": "Skús sa na chvíľu zhlboka nadýchnuť a uvoľniť. Pomalé dýchanie často zníži napätie.",
    "temperature": "Skontroluj si teplotu. Ak je ti príliš teplo alebo zima, skús upraviť prostredie.",
    "pain": "Skús si na chvíľu sadnúť alebo zmeniť polohu. Ak bolesť pretrváva, sleduj ju a odpočívaj.",
    "unknown": "Nie som si istý, čo presne cítiš. Skús mi to opísať trochu podrobnejšie.",
}


# ---------------------------------------------------------------------
# IDENTITY‑AWARE SAFETY NOTES (Security Family 4.4)
# ---------------------------------------------------------------------
IDENTITY_NOTES = {
    "OWNER": "Ak by sa tvoj stav zhoršil, sleduj to a v prípade potreby kontaktuj odborníka.",
    "FAMILY": "Ak sa to nezlepší, skús si oddýchnuť a sleduj svoj stav.",
    "CHILD": "Ak sa necítiš dobre, povedz to dospelému, ktorému dôveruješ.",
    "STRANGER": "Ak sa necítiš dobre, skús si oddýchnuť a sleduj svoj stav.",
}


# ---------------------------------------------------------------------
# PUBLIC API – BUILD SAFE RESPONSE
# ---------------------------------------------------------------------
def build_response(category: str, context) -> Dict[str, str]:
    """
    Build a safe, identity‑aware response dictionary.

    Returns:
    {
        "status": "ok" | "safe_mode" | "error",
        "category": str,
        "message": str,
        "safety_note": str,
        "identity": str,
        "degraded_mode": bool
    }
    """

    # SAFE‑MODE → only safe fallback
    if getattr(context, "safe_mode", False):
        return {
            "status": "safe_mode",
            "category": "unknown",
            "message": BASE_RESPONSES["unknown"],
            "safety_note": context.default_safety_note,
            "identity": context.identity,
            "degraded_mode": getattr(context, "degraded_mode", False),
        }

    try:
        # Deterministic lookup
        message = BASE_RESPONSES.get(category, BASE_RESPONSES["unknown"])
        safety_note = IDENTITY_NOTES.get(context.identity, IDENTITY_NOTES["STRANGER"])

        return {
            "status": "ok",
            "category": category,
            "message": message,
            "safety_note": safety_note,
            "identity": context.identity,
            "degraded_mode": getattr(context, "degraded_mode", False),
        }

    except Exception as exc:
        # Any unexpected error → degraded mode
        if hasattr(context, "mark_degraded"):
            context.mark_degraded()

        return {
            "status": "error",
            "category": "unknown",
            "message": BASE_RESPONSES["unknown"],
            "safety_note": context.default_safety_note,
            "identity": context.identity,
            "exception": str(exc),
            "degraded_mode": True,
        }


__all__ = ["build_response"]
