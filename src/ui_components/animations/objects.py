# objects.py
# SIRIUS LOCAL AI – UI Drawable Objects 4.3.x
# Deterministic, safe-mode compatible drawing primitives for UI components

from dataclasses import dataclass


@dataclass
class DrawableObject:
    """
    Base graphical object – all shapes inherit from this.

    Phase‑4 Features:
        - safe-mode compatibility
        - degraded-mode fallback
        - deterministic draw() behavior
        - PixelLayoutEngine-ready structure
    """

    x: float
    y: float
    color: tuple
    visible: bool = True

    safe_mode: bool = False
    degraded_mode: bool = False

    def draw(self):
        """
        Base draw method.
        Subclasses override this with DearPyGUI or custom renderers.
        """
        if self.safe_mode or not self.visible:
            return

        try:
            # Subclasses implement actual drawing
            pass
        except Exception:
            self.degraded_mode = True


# ---------------------------------------------------------
# CIRCLE
# ---------------------------------------------------------

class Circle(DrawableObject):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self):
        if self.safe_mode or not self.visible:
            return

        try:
            # DearPyGUI draw_circle will go here (Phase‑5)
            pass
        except Exception:
            self.degraded_mode = True


# ---------------------------------------------------------
# RECTANGLE
# ---------------------------------------------------------

class Rectangle(DrawableObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self):
        if self.safe_mode or not self.visible:
            return

        try:
            # DearPyGUI draw_rectangle will go here (Phase‑5)
            pass
        except Exception:
            self.degraded_mode = True


# ---------------------------------------------------------
# LINE
# ---------------------------------------------------------

class Line(DrawableObject):
    def __init__(self, x, y, x2, y2, color):
        super().__init__(x, y, color)
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        if self.safe_mode or not self.visible:
            return

        try:
            # DearPyGUI draw_line will go here (Phase‑5)
            pass
        except Exception:
            self.degraded_mode = True
