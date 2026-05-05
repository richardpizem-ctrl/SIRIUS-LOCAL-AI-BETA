# timeline_ui_component.py
# Wrapper component for TimelineUI to integrate with UIManager
# SIRIUS LOCAL AI – ui_components (Phase 4)

from .manager import UIComponent
from timeline.timeline_ui import TimelineUI  # your existing TimelineUI

class TimelineUIComponent(UIComponent):
    """
    UI wrapper for TimelineUI.
    Provides:
        - mount / unmount lifecycle
        - render() → returns layout blocks
        - generate_layout() → prepares pixel blocks for PixelLayoutEngine
    """

    def __init__(self):
        self.timeline = TimelineUI()
        self._mounted = False

    def mount(self):
        self._mounted = True
        print("TimelineUI mounted")

    def unmount(self):
        self._mounted = False
        print("TimelineUI unmounted")

    def generate_layout(self):
        """
        TimelineUI will later return real pixel blocks.
        For now this is a placeholder so PixelLayoutEngine
        always receives a consistent input.
        """
        if hasattr(self.timeline, "generate_layout"):
            return self.timeline.generate_layout()

        # Fallback placeholder – safe for Phase 4
        return [
            {
                "type": "text",
                "x": 10,
                "y": 10,
                "content": "TimelineUI – layout placeholder",
            }
        ]

    def render(self):
        """
        UIManager calls render() → it must return layout blocks.
        PixelLayoutEngine will then render them.
        """
        layout = self.generate_layout()
        return layout
