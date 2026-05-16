"""
UI Parser Module – Runtime 4.3.0

New in 4.3.0:
- Fuzzy Matching Engine
- Multi‑strategy element resolution
- Levenshtein distance scoring
- Semantic alias map
- Confidence levels
- Deterministic fallback rules

The parser still does NOT interact with the OS directly.
It receives only abstracted data from UIGraph.
"""

import difflib


class UIParser:
    def __init__(self):
        self.parsed_elements = []

        # ------------------------------------------------------------
        # SEMANTIC ALIAS MAP (Runtime 4.3.0)
        # ------------------------------------------------------------
        # Allows matching synonyms or alternative names.
        self.semantic_aliases = {
            "ok": ["okay", "confirm", "accept"],
            "cancel": ["close", "abort", "dismiss"],
            "settings": ["preferences", "options", "config"],
            "exit": ["quit", "close app"],
        }

    # ------------------------------------------------------------
    # GRAPH PARSING
    # ------------------------------------------------------------
    def parse_graph(self, ui_graph):
        """
        Takes a UIGraph instance and extracts UI elements from it.
        """
        if not ui_graph:
            return

        self.parsed_elements = []

        for element in ui_graph.elements:
            normalized = self._normalize_element(element)
            self.parsed_elements.append(normalized)

    # ------------------------------------------------------------
    # ELEMENT NORMALIZATION
    # ------------------------------------------------------------
    def _normalize_element(self, element):
        """
        Normalizes a UI element into a unified structure:
        - name
        - type
        - properties
        """
        return {
            "name": getattr(element, "name", "") or "",
            "type": getattr(element, "type", "") or "",
            "properties": getattr(element, "properties", {}) or {},
        }

    # ------------------------------------------------------------
    # FUZZY MATCHING ENGINE (Runtime 4.3.0)
    # ------------------------------------------------------------
    def _levenshtein_ratio(self, a, b):
        """Returns similarity ratio using difflib."""
        return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()

    def _semantic_match(self, name, el_name):
        """Checks semantic alias map."""
        name = name.lower()
        el_name = el_name.lower()

        if name in self.semantic_aliases:
            for alias in self.semantic_aliases[name]:
                if alias in el_name:
                    return True
        return False

    # ------------------------------------------------------------
    # ELEMENT SEARCH (EXTENDED FOR 4.3.0)
    # ------------------------------------------------------------
    def find(self, name=None, element_type=None, min_confidence=0.55):
        """
        Searches for UI elements using:
        - exact match
        - case-insensitive match
        - partial match
        - semantic alias match
        - fuzzy match (Levenshtein ratio)
        - type match

        Returns:
            List of dicts with:
            {
                "element": <element>,
                "confidence": <0.0 - 1.0>
            }
        """
        if not self.parsed_elements:
            return []

        results = []

        for el in self.parsed_elements:
            el_name = el.get("name", "")
            el_type = el.get("type", "")

            confidence = 0.0

            # 1. Exact match
            if name and el_name == name:
                confidence = 1.0

            # 2. Case-insensitive match
            elif name and el_name.lower() == name.lower():
                confidence = 0.95

            # 3. Partial match
            elif name and name.lower() in el_name.lower():
                confidence = 0.85

            # 4. Semantic alias match
            elif name and self._semantic_match(name, el_name):
                confidence = 0.80

            # 5. Fuzzy match (Levenshtein ratio)
            elif name:
                ratio = self._levenshtein_ratio(name, el_name)
                if ratio >= min_confidence:
                    confidence = ratio

            # 6. Type match (fallback)
            if element_type and el_type == element_type:
                confidence = max(confidence, 0.75)

            # Add only if confidence is acceptable
            if confidence >= min_confidence:
                results.append({
                    "element": el,
                    "confidence": round(confidence, 3)
                })

        # Sort by confidence (highest first)
        results.sort(key=lambda x: x["confidence"], reverse=True)

        return results
