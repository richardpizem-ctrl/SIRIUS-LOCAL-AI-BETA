# timeline_ui_component.py
# SIRIUS LOCAL AI – Timeline UI Component 4.3.x
# Phase‑4 deterministic wrapper for TimelineUI

from .manager import UIComponent
from timeline.timeline_ui import TimelineUI


class TimelineUIComponent(UIComponent):
    """
    TimelineUIComponent 4.3.x

    Responsibilities:
        - Wrap TimelineUI for UIManager
        - Provide safe-mode and degraded-mode behavior
        - Provide deterministic layout blocks for PixelLayoutEngine
        - Provide error-safe lifecycle and rendering
    """

    def __init__(self):
        super().__init__()
        self.timeline = TimelineUI()
        self._mounted = False

    # ---------------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------------

    def mount(self):
        if self.safe_mode:
            return
        self._mounted = True
        print("TimelineUI mounted")

    def unmount(self):
        self._mounted = False
        print("TimelineUI unmounted")

    # ---------------------------------------------------------
    # Layout generation
    # ---------------------------------------------------------

    def generate_layout(self):
        """
        TimelineUI will later return real pixel blocks.
        For now this is a placeholder so PixelLayoutEngine
        always receives a consistent input.
        """

        if self.safe_mode:
            return [
                {"type": "text", "x": 10, "y": 10, "value": "TimelineUI (SAFE MODE)"}
            ]

        if self.degraded_mode:
            return [
                {"type": "text", "x": 10, "y": 10, "value": "TimelineUI (DEGRADED MODE)"}
            ]

        try:
            if hasattr(self.timeline, "generate_layout"):
                blocks = self.timeline.generate_layout()

                # Normalize block format (Phase‑4)
                normalized = []
                for b in blocks:
                    block = {
                        "type": b.get("type", "text"),
                        "x": b.get("x", 0),
                        "y": b.get("y", 0),
                        "value": b.get("value") or b.get("content") or "",
                    }
                    normalized.append(block)

                return normalized

            # Fallback placeholder
            return [
                {"type": "text", "x": 10, "y": 10, "value": "TimelineUI – placeholder"}
            ]

        except Exception:
            self.degraded_mode = True
            return [
                {"type": "text", "x": 10, "y": 10, "value": "TimelineUI Render Error"}
            ]

    # ---------------------------------------------------------
    # Rendering
    # ---------------------------------------------------------

    def render(self):
        """
        UIManager calls render() → must return layout blocks.
        PixelLayoutEngine will then render them.
        """
        return self.generate_layout()
