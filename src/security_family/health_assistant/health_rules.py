"""
Health Rules – Deterministic Classification Layer 4.3.x
-------------------------------------------------------
This module classifies user text into safe, non-medical categories.
No diagnoses, no medication advice, no medical claims.

Categories:
- hydration
- rest
- stress
- temperature
- pain
- unknown
"""

import re
from typing import Optional


# --- SIMPLE KEYWORD MAP ------------------------------------------------------

KEYWORDS = {
    "hydration": [
        "smäd", "smad", "dehydrat", "málo pijem", "malo pijem",
        "sucho v ústach", "suche usta"
    ],
    "rest": [
        "únava", "unava", "som unavený", "som unavena",
        "slabosť", "slabost", "vyčerpaný", "vycerpany"
    ],
    "stress": [
        "stres", "nervozita", "úzkosť", "uzkost",
        "napätie", "napatie", "som v strese"
    ],
    "temperature": [
        "horúčka", "horucka", "teplota", "zimnica",
        "je mi teplo", "je mi zima"
    ],
    "pain": [
        "bolí ma", "bolest", "boli ma hlava", "boli ma brucho",
        "pichá", "picha", "tlačí", "tlaci"
    ],
}


# --- CLASSIFICATION LOGIC ----------------------------------------------------

def classify_health_state(text: str, context) -> str:
    """
    Deterministic rule-based classifier.
    Returns one of:
        hydration | rest | stress | temperature | pain | unknown

    Safe-mode → always return "unknown".
    Degraded-mode → still return deterministic category.
    """

    # Safe-mode: no classification
    if getattr(context, "safe_mode", False):
        return "unknown"

    try:
        normalized = (text or "").lower().strip()

        # Identity-aware restrictions
        if context.identity == "CHILD":
            # children get simplified categories only
            if any(k in normalized for k in KEYWORDS["pain"]):
                return "pain"
            if any(k in normalized for k in KEYWORDS["stress"]):
                return "stress"
            return "rest"

        # Standard classification
        for category, words in KEYWORDS.items():
            for w in words:
                if w in normalized:
                    return category

        return "unknown"

    except Exception:
        # Mark degraded-mode
        if hasattr(context, "mark_degraded"):
            context.mark_degraded()
        return "unknown"
