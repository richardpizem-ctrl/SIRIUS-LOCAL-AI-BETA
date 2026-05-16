"""
UI Parser Module – Runtime 4.2.0

Zodpovedá za:
- extrakciu UI prvkov z UI Graphu
- normalizáciu názvov, typov a vlastností
- prípravu dát pre UI Actions a UI Workflow

Parser nepracuje s OS priamo – dostáva iba dáta z UIGraph.
"""

class UIParser:
    def __init__(self):
        self.parsed_elements = []

    def parse_graph(self, ui_graph):
        """
        Prevezme UIGraph objekt a extrahuje z neho UI prvky.
        """
        if not ui_graph:
            return

        # základná štruktúra – neskôr sa doplní o reálne UI prvky
        for element in ui_graph.elements:
            normalized = self._normalize_element(element)
            self.parsed_elements.append(normalized)

    def _normalize_element(self, element):
        """
        Normalizuje UI prvok do jednotnej štruktúry:
        - názov
        - typ
        - vlastnosti
        """
        return {
            "name": getattr(element, "name", None),
            "type": getattr(element, "type", None),
            "properties": getattr(element, "properties", {}),
        }

    def find(self, name=None, element_type=None):
        """
        Vyhľadá UI prvok podľa názvu alebo typu.
        """
        results = []

        for el in self.parsed_elements:
            if name and el["name"] == name:
                results.append(el)
            if element_type and el["type"] == element_type:
                results.append(el)

        return results
