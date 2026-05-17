# panel.py
# SIRIUS LOCAL AI – UI Panel Component 4.3.x
# Deterministic, safe-mode compatible UI component

from .manager import UIComponent


class Panel(UIComponent):
    """
    Panel 4.3.x

    Responsibilities:
        - Provide a simple UI component for testing
        - Demonstrate Phase‑4 lifecycle behavior
        - Produce deterministic layout blocks
        - Support safe-mode and degraded-mode
    """

    def __init__(self):
        super().__init__()
        self.mounted = False

    # ---------------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------------

    def mount(self):
        if self.safe_mode:
            return
        self.mounted = True
        print("Panel mounted")

    def unmount(self):
        self.mounted = False
        print("Panel unmounted")

    # ---------------------------------------------------------
    # Rendering
    # ---------------------------------------------------------

    def render(self):
        """
        Return layout blocks for PixelLayoutEngine.
        Phase‑4 requires deterministic, structured output.
        """

        if self.safe_mode:
            return [
                {"type": "text", "value": "Panel (SAFE MODE)", "x": 0, "y": 0}
            ]

        if self.degraded_mode:
            return [
                {"type": "text", "value": "Panel (DEGRADED MODE)", "x": 0, "y": 0}
            ]

        try:
            # Phase‑4 layout block format
            return [
                {"type": "text", "value": "Rendering Panel", "x": 0, "y": 0}
            ]

        except Exception:
            self.degraded_mode = True
            return [
                {"type": "text", "value": "Panel Render Error", "x": 0, "y": 0}
            ]
