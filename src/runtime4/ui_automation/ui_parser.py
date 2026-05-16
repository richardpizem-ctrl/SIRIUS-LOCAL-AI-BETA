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

        # Reset – parser musí byť čistý pri každom cykle workflowu
        self.parsed_elements = []

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
        Podporuje:
        - presnú zhodu
        - case-insensitive zhodu
        - partial match (napr. 'Set' → 'Settings')
        """
        if not self.parsed_elements:
            return []

        results = []

        for el in self.parsed_elements:
            el_name = el.get("name", "")
            el_type = el.get("type", "")

            # 1. Presná zhoda mena
            if name and el_name == name:
                results.append(el)
                continue

            # 2. Case-insensitive zhoda
            if name and el_name.lower() == name.lower():
                results.append(el)
                continue

            # 3. Partial match
            if name and name.lower() in el_name.lower():
                results.append(el)
                continue

            # 4. Zhoda typu
            if element_type and el_type == element_type:
                results.append(el)

        return results
