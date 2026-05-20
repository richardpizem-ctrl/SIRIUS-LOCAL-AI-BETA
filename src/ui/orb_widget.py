# orb_widget_4_4.py
# SIRIUS LOCAL AI – ORB UI Widget 4.4.0 PRO
# Phase‑4 UI Manager compatible ORB wrapper (Phase‑5 ready)

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

# ORB engine + renderer (4.4 PRO)
from ui_components.animations.orb_factory_4_4 import create_sirius_orb_44
from ui_components.animations.orb_renderer_4_4 import OrbRenderer44


class OrbWidget44(QWidget):
    """
    OrbWidget 4.4.0 PRO

    Responsibilities:
        - Create ORB engine + core object via factory (4.4)
        - Wrap OrbRenderer44 into a QWidget
        - Provide safe-mode and degraded-mode behavior (Security Family 4.4)
        - Provide structured fallback UI
        - Provide external trigger API (success, warning, insight)
        - Deterministic, offline-only behavior
        - Self‑Repair 4.4 compatible
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.safe_mode = False
        self.degraded_mode = False

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)

        try:
            # Create ORB engine + core object (4.4)
            self.engine, self.orb = create_sirius_orb_44()

            # Create renderer (4.4)
            self.renderer = OrbRenderer44(self.engine, self.orb)

            layout.addWidget(self.renderer)

        except Exception as exc:
            self.degraded_mode = True
            layout.addWidget(self._build_error_placeholder(str(exc)))

        self.setLayout(layout)
        self.setMinimumSize(300, 300)

    # ---------------------------------------------------------
    # Fallback UI (degraded-mode)
    # ---------------------------------------------------------

    def _build_error_placeholder(self, message: str) -> QWidget:
        label = QLabel(f"ORB Error (DEGRADED MODE)\n{message}")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: red; font-size: 14px;")
        return label

    # ---------------------------------------------------------
    # Safe-mode
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True
        self._replace_with_safe_placeholder()

    def exit_safe_mode(self):
        self.safe_mode = False
        # UI Manager 4.4/5 will re-create the widget if needed

    def _replace_with_safe_placeholder(self):
        """Replace ORB with a safe-mode placeholder."""
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().deleteLater()

        label = QLabel("ORB disabled in SAFE MODE")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: gray; font-size: 14px;")
        self.layout().addWidget(label)

    # ---------------------------------------------------------
    # External triggers (Phase‑4 / Phase‑5 ready)
    # ---------------------------------------------------------

    def set_state(self, state: str):
        """Proxy to ORB state controller."""
        if self.safe_mode or self.degraded_mode:
            return

        for obj in self.engine._objects:
            if obj.__class__.__name__ == "OrbStateController":
                obj.set_state(state)

    def trigger_success(self):
        if self.safe_mode or self.degraded_mode:
            return

        for obj in self.engine._objects:
            if obj.__class__.__name__ == "OrbSuccessBurst":
                obj.trigger()

    def trigger_warning(self):
        if self.safe_mode or self.degraded_mode:
            return

        for obj in self.engine._objects:
            if obj.__class__.__name__ == "OrbWarningFlash":
                obj.trigger()

    def trigger_insight(self):
        if self.safe_mode or self.degraded_mode:
            return

        for obj in self.engine._objects:
            if obj.__class__.__name__ == "OrbDeepInsightBurst":
                obj.trigger()
