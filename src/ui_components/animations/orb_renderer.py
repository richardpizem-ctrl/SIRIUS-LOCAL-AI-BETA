# orb_renderer.py
# SIRIUS LOCAL AI – ORB RENDERER 4.3.x
# Phase‑4 safe-mode compatible QPainter renderer

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtCore import Qt, QTimer
import math

from .engine import (
    OrbAwarenessBloom,
    OrbEchoNetwork,
    OrbInsightSingularity
)


class OrbRenderer(QWidget):
    """
    OrbRenderer 4.3.x

    Responsibilities:
        - Render ORB layers using QPainter
        - Integrate with AnimationEngine 4.3.x
        - Provide safe-mode and degraded-mode behavior
        - Provide structured fallback UI
        - Deterministic, offline-only rendering
        - Error-safe update loop
    """

    def __init__(self, engine, orb, parent=None):
        super().__init__(parent)

        self.engine = engine
        self.orb = orb

        self.safe_mode = False
        self.degraded_mode = False

        # 60 FPS timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick)
        self.timer.start(16)

        self.setMinimumSize(300, 300)
        self.setAutoFillBackground(False)

    # ---------------------------------------------------------
    # Safe-mode
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False

    # ---------------------------------------------------------
    # Update loop
    # ---------------------------------------------------------

    def _tick(self):
        if self.safe_mode:
            return

        try:
            self.engine.update(0.016)  # ~60 FPS
        except Exception:
            self.degraded_mode = True

        self.update()

    # ---------------------------------------------------------
    # Paint event
    # ---------------------------------------------------------

    def paintEvent(self, event):
        if self.safe_mode:
            self._paint_safe_mode()
            return

        if self.degraded_mode:
            self._paint_degraded_mode()
            return

        try:
            self._paint_orb()
        except Exception:
            self.degraded_mode = True
            self._paint_degraded_mode()

    # ---------------------------------------------------------
    # Safe-mode placeholder
    # ---------------------------------------------------------

    def _paint_safe_mode(self):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(150, 150, 150), 2))
        painter.drawText(self.rect(), Qt.AlignCenter, "ORB disabled in SAFE MODE")
        painter.end()

    # ---------------------------------------------------------
    # Degraded-mode placeholder
    # ---------------------------------------------------------

    def _paint_degraded_mode(self):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 100, 100), 2))
        painter.drawText(self.rect(), Qt.AlignCenter, "ORB RENDER ERROR\n(DEGRADED MODE)")
        painter.end()

    # ---------------------------------------------------------
    # Main ORB rendering
    # ---------------------------------------------------------

    def _paint_orb(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()
        cx = w / 2
        cy = h / 2

        base = min(w, h) * 0.25

        # ORB core
        r_inner = base * self.orb.inner_scale
        r_mid   = base * self.orb.mid_scale
        r_outer = base * self.orb.outer_scale

        r, g, b = self.orb.color
        core_color = QColor(int(r * 255), int(g * 255), int(b * 255))

        # Outer glow
        painter.setBrush(QBrush(core_color.lighter(180)))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(cx - r_outer, cy - r_outer, r_outer * 2, r_outer * 2)

        # Mid layer
        painter.setBrush(QBrush(core_color))
        painter.drawEllipse(cx - r_mid, cy - r_mid, r_mid * 2, r_mid * 2)

        # Inner core
        painter.setBrush(QBrush(core_color.darker(150)))
        painter.drawEllipse(cx - r_inner, cy - r_inner, r_inner * 2, r_inner * 2)

        # Draw effects
        for obj in list(self.engine._objects):
            try:
                self._draw_effect(painter, obj, cx, cy, base)
            except Exception:
                # Individual effect failure → skip, renderer continues
                self.degraded_mode = True

        painter.end()

    # ---------------------------------------------------------
    # Effect rendering
    # ---------------------------------------------------------

    def _draw_effect(self, painter, obj, cx, cy, base):

        # TEMPORAL ECHOES
        if obj.__class__.__name__ == "OrbTemporalEchoes":
            pen = QPen(QColor(150, 200, 255, 120), 2)
            painter.setPen(pen)
            painter.setBrush(Qt.NoBrush)

            for e in obj.echoes:
                r = base * e[2] * 1.2
                alpha = int(e[4] * 255)
                pen.setColor(QColor(150, 200, 255, alpha))
                painter.setPen(pen)
                painter.drawEllipse(cx - r, cy - r, r * 2, r * 2)

        # PREDICTIVE TRAILS
        if obj.__class__.__name__ == "OrbPredictiveTrails":
            pen = QPen(QColor(100, 255, 200, 180), 2)
            painter.setPen(pen)

            for t in obj.trails:
                angle = math.radians(t[0])
                length = base * t[1]
                x2 = cx + math.cos(angle) * length
                y2 = cy + math.sin(angle) * length
                painter.drawLine(cx, cy, x2, y2)

        # COGNITIVE MESH
        if obj.__class__.__name__ == "OrbCognitiveMesh":
            pen = QPen(QColor(120, 180, 255, 150), 2)
            painter.setPen(pen)

            for m in obj.mesh_points:
                angle = math.radians(m[0])
                r = base * m[1]
                x = cx + math.cos(angle) * r
                y = cy + math.sin(angle) * r
                painter.drawPoint(x, y)

        # AWARENESS BLOOM
        if isinstance(obj, OrbAwarenessBloom):
            alpha = int(obj.life * 255)
            pen = QPen(QColor(255, 255, 200, alpha), 3)
            painter.setPen(pen)
            r = base * obj.radius
            painter.drawEllipse(cx - r, cy - r, r * 2, r * 2)

        # PROBABILITY CLOUD
        if obj.__class__.__name__ == "OrbProbabilityCloud":
            for p in obj.points:
                angle = math.radians(p[0])
                r = base * p[1]
                prob = p[2]
                alpha = int(prob * 255)

                pen = QPen(QColor(255, 255, 255, alpha), 2)
                painter.setPen(pen)

                x = cx + math.cos(angle) * r
                y = cy + math.sin(angle) * r
                painter.drawPoint(x, y)

        # ECHO NETWORK
        if isinstance(obj, OrbEchoNetwork):
            for e in obj.echoes:
                alpha = int(e[2] * 255)
                pen = QPen(QColor(200, 255, 255, alpha), 2)
                painter.setPen(pen)
                r = base * e[0]
                painter.drawEllipse(cx - r, cy - r, r * 2, r * 2)

        # RIPPLE WAVES
        if obj.__class__.__name__ == "OrbCognitiveRipple":
            for r in obj.ripples:
                alpha = int(r[1] * 255)
                pen = QPen(QColor(180, 220, 255, alpha), 2)
                painter.setPen(pen)
                radius = base * r[0]
                painter.drawEllipse(cx - radius, cy - radius, radius * 2, radius * 2)

        # INSIGHT SINGULARITY
        if isinstance(obj, OrbInsightSingularity) and obj.active:
            alpha = int(obj.intensity * 255)
            pen = QPen(QColor(255, 255, 150, alpha), 4)
            painter.setPen(pen)
            r = base * obj.radius
            painter.drawEllipse(cx - r, cy - r, r * 2, r * 2)
