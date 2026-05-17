"""
UI Graph Module – Runtime 4.3.0

Responsible for:
- reading the UI window tree
- mapping windows and UI elements
- building a graph representation of the UI
- safe-mode and degraded-mode behavior
- WinCapabilities integration for real OS-level enumeration (4.3+)

This module currently uses fake data for testing.
In Runtime 4.3 it supports optional WinCapabilities injection.
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
    def __init__(self, win_capabilities=None):
        """
        win_capabilities: optional OS-level UI enumeration layer
        """
        self.win_capabilities = win_capabilities

        self.windows = []
        self.elements = []

        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------
    # WINDOW SCANNING
    # ------------------------------------------------------------
    def scan_windows(self):
        """
        Scans all visible windows in the system.
        If WinCapabilities is available, uses real OS enumeration.
        Otherwise returns deterministic fake data.
        """

        if self.safe_mode:
            self.windows = []
            return {
                "status": "safe_mode",
                "windows": [],
                "degraded_mode": self.degraded_mode
            }

        # 1. Try OS-level enumeration
        if self.win_capabilities and hasattr(self.win_capabilities, "enumerate_windows"):
            try:
                self.windows = self.win_capabilities.enumerate_windows()
                return {
                    "status": "ok",
                    "windows": self.windows,
                    "via_os": True,
                    "degraded_mode": self.degraded_mode
                }
            except Exception:
                self.degraded_mode = True

        # 2. Fallback: deterministic fake window list
        self.windows = ["MainWindow"]
        return {
            "status": "ok",
            "windows": self.windows,
            "via_os": False,
            "degraded_mode": self.degraded_mode
        }

    # ------------------------------------------------------------
    # GRAPH BUILDING
    # ------------------------------------------------------------
    def build_graph(self):
        """
        Builds the UI element graph and relationships.
        If WinCapabilities is available, uses real OS enumeration.
        Otherwise uses deterministic fake elements.
        """

        if self.safe_mode:
            self.elements = []
            return {
                "status": "safe_mode",
                "elements": [],
                "degraded_mode": self.degraded_mode
            }

        # 1. Try OS-level element enumeration
        if self.win_capabilities and hasattr(self.win_capabilities, "enumerate_elements"):
            try:
                self.elements = self.win_capabilities.enumerate_elements()
                return {
                    "status": "ok",
                    "elements": self.elements,
                    "via_os": True,
                    "degraded_mode": self.degraded_mode
                }
            except Exception:
                self.degraded_mode = True

        # 2. Fallback: deterministic fake elements
        self.elements = [
            FakeElement("OK"),
            FakeElement("Cancel"),
            FakeElement("Settings"),
            FakeElement("SearchBox", type="input"),
        ]

        return {
            "status": "ok",
            "elements": self.elements,
            "via_os": False,
            "degraded_mode": self.degraded_mode
        }

    # ------------------------------------------------------------
    # ELEMENT SEARCH
    # ------------------------------------------------------------
    def find_element(self, query):
        """
        Finds a UI element by name, type, or properties.
        Basic exact match for now – extended matching will be
        implemented in Runtime 4.3.
        """

        if not isinstance(query, str) or not query.strip():
            return None

        for el in self.elements:
            if el.name == query:
                return el

        return None
