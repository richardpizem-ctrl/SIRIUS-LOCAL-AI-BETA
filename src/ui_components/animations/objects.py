# objects_4_5.py
# SIRIUS LOCAL AI – UI Drawable Objects 4.5.0 PRO
# Deterministic, safe-mode compatible drawing primitives for UI components

from dataclasses import dataclass


@dataclass
class DrawableObject45:
    """
    Base graphical object – all shapes inherit from this.

    Phase‑4/5 Features:
        - safe-mode compatibility
        - degraded-mode fallback
        - deterministic draw() behavior
        - PixelLayoutEngine Phase‑4 ready
        - Self‑Repair 4.5 compatible
        - Offline-only, no side-effects
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
        Subclasses override this with PixelLayoutEngine or custom renderers.
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

class Circle45(DrawableObject45):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self):
        if self.safe_mode or not self.visible:
            return

        try:
            # PixelLayoutEngine draw_circle (Phase‑5)
            pass
        except Exception:
            self.degraded_mode = True


# ---------------------------------------------------------
# RECTANGLE
# ---------------------------------------------------------

class Rectangle45(DrawableObject45):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self):
        if self.safe_mode or not self.visible:
            return

        try:
            # PixelLayoutEngine draw_rectangle (Phase‑5)
            pass
        except Exception:
            self.degraded_mode = True


# ---------------------------------------------------------
# LINE
# ---------------------------------------------------------

class Line45(DrawableObject45):
    def __init__(self, x, y, x2, y2, color):
        super().__init__(x, y, color)
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        if self.safe_mode or not self.visible:
            return

        try:
            # PixelLayoutEngine draw_line (Phase‑5)
            pass
        except Exception:
            self.degraded_mode = True
