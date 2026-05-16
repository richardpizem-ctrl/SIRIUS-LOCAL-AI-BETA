"""
UI Parser Module – Runtime 4.2.0

Responsible for:
- extracting UI elements from the UI Graph
- normalizing names, types and properties
- preparing structured data for UI Actions and UI Workflow

The parser does NOT interact with the OS directly.
It receives only abstracted data from UIGraph.
"""

class UIParser:
    def __init__(self):
        self.parsed_elements = []

    # ------------------------------------------------------------
    # GRAPH PARSING
    # ------------------------------------------------------------
    def parse_graph(self, ui_graph):
        """
        Takes a UIGraph instance and extracts UI elements from it.
        """
        if not ui_graph:
            return

        # Reset – parser must be clean for every workflow cycle
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
            "name": getattr(element, "name", None),
            "type": getattr(element, "type", None),
            "properties": getattr(element, "properties", {}),
        }

    # ------------------------------------------------------------
    # ELEMENT SEARCH
    # ------------------------------------------------------------
    def find(self, name=None, element_type=None):
        """
        Searches for UI elements by name or type.

        Supports:
        - exact match
        - case-insensitive match
        - partial match (e.g., 'Set' → 'Settings')

        Extended fuzzy matching will be added in Runtime 4.3.
        """
        if not self.parsed_elements:
            return []

        results = []

        for el in self.parsed_elements:
            el_name = el.get("name", "")
            el_type = el.get("type", "")

            # 1. Exact name match
            if name and el_name == name:
                results.append(el)
                continue

            # 2. Case-insensitive match
            if name and el_name.lower() == name.lower():
                results.append(el)
                continue

            # 3. Partial match
            if name and name.lower() in el_name.lower():
                results.append(el)
                continue

            # 4. Type match
            if element_type and el_type == element_type:
                results.append(el)

        return results
