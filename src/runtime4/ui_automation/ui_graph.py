"""
UI Graph Module – Runtime 4.3.0 (PRO)

Responsible for:
- Reading the UI window tree
- Mapping windows and UI elements
- Building a deterministic graph representation of the UI
- Safe‑mode and degraded‑mode behavior
- Optional WinCapabilities integration (OS‑level enumeration)

Security Notes:
- No dynamic imports, no eval, no reflection
- Deterministic fallback behavior
- Fully offline‑safe
- Compatible with Security Family 4.4 and UI Sandbox 4.3.x
"""

from typing import Any, Dict, List, Optional


class FakeElement:
    """
    Simple placeholder UI element.
    Used for workflow testing without OS integration.
    """
    def __init__(self, name: str, type: str = "button", properties: Optional[dict] = None):
        self.name = name
        self.type = type
        self.properties = properties or {}


class UIGraph:
    """
    Deterministic UI Graph Engine for Runtime 4.3.x (PRO).
    """

    def __init__(self, win_capabilities=None):
        """
        win_capabilities: optional OS-level UI enumeration layer
        """
        self.win_capabilities = win_capabilities

        self.windows: List[Any] = []
        self.elements: List[Any] = []

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ------------------------------------------------------------
    # INTERNAL OS‑LEVEL WRAPPER
    # ------------------------------------------------------------
    def _try_os(self, method: str, *args):
        """
        Attempts OS-level enumeration via WinCapabilities.
        Returns:
            list → success
            None → not available
            False → OS error
        """
        if not self.win_capabilities:
            return None

        if not hasattr(self.win_capabilities, method):
            return None

        try:
            result = getattr(self.win_capabilities, method)(*args)
            return result
        except Exception:
            self.degraded_mode = True
            return False

    # ------------------------------------------------------------
    # WINDOW SCANNING
    # ------------------------------------------------------------
    def scan_windows(self) -> Dict[str, Any]:
        """
        Scans all visible windows.
        OS-level enumeration if available, otherwise deterministic fallback.
        """

        if self.safe_mode:
            self.windows = []
            return {
                "status": "safe_mode",
                "windows": [],
                "degraded_mode": self.degraded_mode,
            }

        os_result = self._try_os("enumerate_windows")

        if os_result is False:
            return {
                "status": "error",
                "code": "os_window_enum_failed",
                "windows": [],
                "via_os": True,
                "degraded_mode": self.degraded_mode,
            }

        if isinstance(os_result, list):
            self.windows = os_result
            return {
                "status": "ok",
                "windows": self.windows,
                "via_os": True,
                "degraded_mode": self.degraded_mode,
            }

        # Deterministic fallback
        self.windows = ["MainWindow"]
        return {
            "status": "ok",
            "windows": self.windows,
            "via_os": False,
            "degraded_mode": self.degraded_mode,
        }

    # ------------------------------------------------------------
    # GRAPH BUILDING
    # ------------------------------------------------------------
    def build_graph(self) -> Dict[str, Any]:
        """
        Builds the UI element graph.
        OS-level enumeration if available, otherwise deterministic fallback.
        """

        if self.safe_mode:
            self.elements = []
            return {
                "status": "safe_mode",
                "elements": [],
                "degraded_mode": self.degraded_mode,
            }

        os_result = self._try_os("enumerate_elements")

        if os_result is False:
            return {
                "status": "error",
                "code": "os_element_enum_failed",
                "elements": [],
                "via_os": True,
                "degraded_mode": self.degraded_mode,
            }

        if isinstance(os_result, list):
            self.elements = os_result
            return {
                "status": "ok",
                "elements": self.elements,
                "via_os": True,
                "degraded_mode": self.degraded_mode,
            }

        # Deterministic fallback
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
            "degraded_mode": self.degraded_mode,
        }

    # ------------------------------------------------------------
    # ELEMENT SEARCH
    # ------------------------------------------------------------
    def find_element(self, query: str) -> Optional[Any]:
        """
        Finds a UI element by exact name match.
        Deterministic, no fuzzy matching in 4.3.x.
        """

        if not isinstance(query, str) or not query.strip():
            return None

        for el in self.elements:
            if getattr(el, "name", None) == query:
                return el

        return None
