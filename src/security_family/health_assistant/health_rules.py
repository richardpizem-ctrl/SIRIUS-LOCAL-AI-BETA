"""
Health Rules – Deterministic Classification Layer
-------------------------------------------------
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
    """

    normalized = text.lower().strip()

    # Identity-aware restrictions (example)
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
