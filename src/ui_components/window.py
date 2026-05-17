# window.py
# SIRIUS LOCAL AI – UI Window Component 4.3.x
# Deterministic, safe-mode compatible UI component

from .manager import UIComponent


class Window(UIComponent):
    """
    Window 4.3.x

    Responsibilities:
        - Provide a simple window UI component
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
        print("Window mounted")

    def unmount(self):
        self.mounted = False
        print("Window unmounted")

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
                {"type": "text", "value": "Window (SAFE MODE)", "x": 0, "y": 0}
            ]

        if self.degraded_mode:
            return [
                {"type": "text", "value": "Window (DEGRADED MODE)", "x": 0, "y": 0}
            ]

        try:
            # Phase‑4 layout block format
            return [
                {"type": "text", "value": "Rendering Window", "x": 0, "y": 0}
            ]

        except Exception:
            self.degraded_mode = True
            return [
                {"type": "text", "value": "Window Render Error", "x": 0, "y": 0}
            ]
