# timeline_ui_component_4_5.py
# SIRIUS LOCAL AI – Timeline UI Component 4.5.0 PRO
# Phase‑4 deterministic wrapper for TimelineUI (Phase‑5 ready)

from .manager_4_5 import UIComponent45
from timeline.timeline_ui import TimelineUI


class TimelineUIComponent45(UIComponent45):
    """
    TimelineUIComponent 4.5.0 PRO

    Responsibilities:
        - Wrap TimelineUI for UIManager45
        - Provide safe-mode and degraded-mode behavior (Security Family 4.5)
        - Provide deterministic layout blocks for PixelLayoutEngine45
        - Provide error-safe lifecycle and rendering
        - Offline-only, no side-effects
        - Self‑Repair 4.5 compatible
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

    def unmount(self):
        self._mounted = False

    # ---------------------------------------------------------
    # Layout generation
    # ---------------------------------------------------------

    def generate_layout(self):
        """
        TimelineUI will later return real pixel blocks.
        For now this is a placeholder so PixelLayoutEngine45
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
        UIManager45 calls render() → must return layout blocks.
        PixelLayoutEngine45 will then render them.
        """
        return self.generate_layout()
