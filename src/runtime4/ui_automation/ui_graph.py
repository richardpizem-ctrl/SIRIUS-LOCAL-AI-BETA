"""
UI Graph Module – Runtime 4.2.0

Zodpovedá za:
- čítanie UI stromu (window tree)
- mapovanie okien a prvkov
- vytváranie grafovej reprezentácie UI
"""

class FakeElement:
    """
    Jednoduchý placeholder UI prvku.
    Slúži na testovanie workflowu bez OS.
    """
    def __init__(self, name, type="button", properties=None):
        self.name = name
        self.type = type
        self.properties = properties or {}


class UIGraph:
    def __init__(self):
        self.windows = []
        self.elements = []

    def scan_windows(self):
        """
        Naskenuje všetky viditeľné okná v systéme.
        Zatiaľ fake dáta – neskôr sa napojí na WinCapabilities.
        """
        self.windows = ["MainWindow"]

    def build_graph(self):
        """
        Vytvorí graf UI prvkov a ich vzťahov.
        Zatiaľ fake prvky pre workflow test.
        """
        self.elements = [
            FakeElement("OK"),
            FakeElement("Cancel"),
            FakeElement("Settings"),
            FakeElement("SearchBox", type="input"),
        ]

    def find_element(self, query):
        """
        Vyhľadá UI prvok podľa názvu, typu alebo vlastností.
        """
        for el in self.elements:
            if el.name == query:
                return el
        return None
