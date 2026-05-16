"""
UI Graph Module – Runtime 4.2.0

Responsible for:
- reading the UI window tree
- mapping windows and UI elements
- building a graph representation of the UI

This module currently uses fake data for testing.
In Runtime 4.3 it will be connected to WinCapabilities
for real OS‑level UI enumeration.
"""

class FakeElement:
    """
    Simple placeholder UI element.
    Used for workflow testing without OS integration.
    """
    def __init__(self, name, type="button", properties=None):
        self.name = name
        self.type = type
        self.properties = properties or {}


class UIGraph:
    def __init__(self):
        self.windows = []
        self.elements = []

    # ------------------------------------------------------------
    # WINDOW SCANNING
    # ------------------------------------------------------------
    def scan_windows(self):
        """
        Scans all visible windows in the system.
        Currently returns fake data – will be replaced by
        WinCapabilities integration in Runtime 4.3.
        """
        self.windows = ["MainWindow"]

    # ------------------------------------------------------------
    # GRAPH BUILDING
    # ------------------------------------------------------------
    def build_graph(self):
        """
        Builds the UI element graph and relationships.
        Currently uses fake elements for workflow testing.
        """
        self.elements = [
            FakeElement("OK"),
            FakeElement("Cancel"),
            FakeElement("Settings"),
            FakeElement("SearchBox", type="input"),
        ]

    # ------------------------------------------------------------
    # ELEMENT SEARCH
    # ------------------------------------------------------------
    def find_element(self, query):
        """
        Finds a UI element by name, type, or properties.
        Basic exact match for now – extended matching will be
        implemented in Runtime 4.3.
        """
        for el in self.elements:
            if el.name == query:
                return el
        return None
