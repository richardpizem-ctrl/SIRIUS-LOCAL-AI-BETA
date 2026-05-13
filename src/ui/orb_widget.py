# ============================================================
# SIRIUS LOCAL AI – ORB UI WIDGET
# Wraps OrbRenderer into a PySide6 QWidget for use in the UI
# ============================================================

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

# Import ORB factory + renderer
from ui_components.animations.orb_factory import create_sirius_orb
from ui_components.animations.orb_renderer import OrbRenderer


class OrbWidget(QWidget):
    """
    UI widget that displays the SIRIUS ORB.
    Creates:
        - engine + orb via factory
        - OrbRenderer for drawing
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Create ORB engine + core object
        self.engine, self.orb = create_sirius_orb()

        # Create renderer
        self.renderer = OrbRenderer(self.engine, self.orb)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.renderer)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.setMinimumSize(300, 300)

    # Optional: expose ORB state controller for external triggers
    def set_state(self, state: str):
        """Proxy to ORB state controller."""
        for obj in self.engine._objects:
            if obj.__class__.__name__ == "OrbStateController":
                obj.set_state(state)

    def trigger_success(self):
        for obj in self.engine._objects:
            if obj.__class__.__name__ == "OrbSuccessBurst":
                obj.trigger()

    def trigger_warning(self):
        for obj in self.engine._objects:
            if obj.__class__.__name__ == "OrbWarningFlash":
                obj.trigger()

    def trigger_insight(self):
        for obj in self.engine._objects:
            if obj.__class__.__name__ == "OrbDeepInsightBurst":
                obj.trigger()

