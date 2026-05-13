# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# Animations 8.0 – Temporal Echoes, Predictive Trails,
# Cognitive Mesh, Focus Beam, Awareness Bloom
# ============================================================

import math
import random
from typing import Protocol, List


# ------------------------------------------------------------
# PROTOCOL – anything animated must implement update()
# ------------------------------------------------------------
class Animatable(Protocol):
    def update(self, delta_time: float) -> None:
        ...


# ------------------------------------------------------------
# TEMPORAL ECHOES – fading echoes of past states
# ------------------------------------------------------------
class OrbTemporalEchoes:
    def __init__(self):
        self.echoes = []  # (inner_scale, mid_scale, outer_scale, intensity, life)

    def capture(self, orb) -> None:
        self.echoes.append([
            orb.inner_scale,
            orb.mid_scale,
            orb.outer_scale,
            orb.intensity,
            1.0
        ])

    def update(self, delta_time: float) -> None:
        for e in self.echoes:
            e[4] -= delta_time * 0.6
        self.echoes = [e for e in self.echoes if e[4] > 0]


# ------------------------------------------------------------
# PREDICTIVE TRAILS – AI prediction lines
# ------------------------------------------------------------
class OrbPredictiveTrails:
    def __init__(self):
        self.trails = []  # (angle, length, life)

    def predict(self) -> None:
        for _ in range(3):
            self.trails.append([
                random.uniform(0, 360),
                random.uniform(0.8, 1.6),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for t in self.trails:
            t[2] -= delta_time * 0.7
        self.trails = [t for t in self.trails if t[2] > 0]


# ------------------------------------------------------------
# COGNITIVE MESH – neural mesh around the orb
# ------------------------------------------------------------
class OrbCognitiveMesh:
    def __init__(self):
        self.mesh_points = []  # (angle, radius, life)

    def activate(self) -> None:
        for _ in range(12):
            self.mesh_points.append([
                random.uniform(0, 360),
                random.uniform(1.0, 1.8),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for m in self.mesh_points:
            m[2] -= delta_time * 0.5
        self.mesh_points = [m for m in self.mesh_points if m[2] > 0]


# ------------------------------------------------------------
# FOCUS BEAM – AI attention beam
# ------------------------------------------------------------
class OrbFocusBeam:
    def __init__(self):
        self.active = False
        self.intensity = 0.0

    def engage(self) -> None:
        self.active = True
        self.intensity = 1.0

    def disengage(self) -> None:
        self.active = False

    def update(self, delta_time: float) -> None:
        if self.active:
            self.intensity = max(0.0, self.intensity - delta_time * 0.4)
        else:
            self.intensity = max(0.0, self.intensity - delta_time * 1.0)


# ------------------------------------------------------------
# AWARENESS BLOOM – expansion of AI awareness
# ------------------------------------------------------------
class OrbAwarenessBloom:
    def __init__(self):
        self.radius = 0.0
        self.life = 0.0

    def trigger(self) -> None:
        self.radius = 0.0
        self.life = 1.0

    def update(self, delta_time: float) -> None:
        if self.life > 0:
            self.radius += delta_time * 2.0
            self.life -= delta_time * 0.7
        if self.life < 0:
            self.life = 0
