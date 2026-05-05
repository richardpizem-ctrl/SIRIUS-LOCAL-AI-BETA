from dataclasses import dataclass

@dataclass
class DrawableObject:
    """Base graphical object – all shapes will inherit from this."""
    x: float
    y: float
    color: tuple
    visible: bool = True

    def draw(self):
        """Draw method – implemented in subclasses."""
        pass


class Circle(DrawableObject):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self):
        pass  # DearPyGUI draw_circle will go here


class Rectangle(DrawableObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self):
        pass  # DearPyGUI draw_rectangle will go here


class Line(DrawableObject):
    def __init__(self, x, y, x2, y2, color):
        super().__init__(x, y, color)
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        pass  # DearPyGUI draw_line will go here
