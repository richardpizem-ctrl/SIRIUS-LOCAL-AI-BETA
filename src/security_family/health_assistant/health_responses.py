"""
Health Responses – Safe Recommendation Generator
------------------------------------------------
Generates non-medical, offline, identity-aware recommendations based on
classified categories from health_rules.py.

This module NEVER:
- dáva diagnózy
- odporúča lieky
- robí medicínske tvrdenia

Len bezpečné, všeobecné odporúčania.
"""

from typing import Dict


BASE_RESPONSES = {
    "hydration": "Skús sa napiť vody. Niekedy aj mierna dehydratácia spôsobí nepríjemné pocity.",
    "rest": "Skús si na chvíľu oddýchnuť. Krátka pauza alebo spánok môže výrazne pomôcť.",
    "stress": "Skús sa na chvíľu zhlboka nadýchnuť a uvoľniť. Pomalé dýchanie často zníži napätie.",
    "temperature": "Skontroluj si teplotu. Ak je ti príliš teplo alebo zima, skús upraviť prostredie.",
    "pain": "Skús si na chvíľu sadnúť alebo zmeniť polohu. Ak bolesť pretrváva, sleduj ju a odpočívaj.",
    "unknown": "Nie som si istý, čo presne cítiš. Skús mi to opísať trochu podrobnejšie.",
}


IDENTITY_NOTES = {
    "OWNER": "Ak by sa tvoj stav zhoršil, určite to sleduj a v prípade potreby kontaktuj odborníka.",
    "FAMILY": "Ak sa to nezlepší, skús si oddýchnuť a sleduj svoj stav.",
    "CHILD": "Ak sa necítiš dobre, povedz to dospelému, ktorému dôveruješ.",
    "STRANGER": "Ak sa necítiš dobre, skús si oddýchnuť a sleduj svoj stav.",
}


def build_response(category: str, context) -> Dict[str, str]:
    """
    Build a safe, identity-aware response dictionary.

    Returns:
    {
        "category": str,
        "message": str,
        "safety_note": str
    }
    """

    message = BASE_RESPONSES.get(category, BASE_RESPONSES["unknown"])
    safety_note = IDENTITY_NOTES.get(context.identity, IDENTITY_NOTES["STRANGER"])

    return {
        "category": category,
        "message": message,
        "safety_note": safety_note,
    }
