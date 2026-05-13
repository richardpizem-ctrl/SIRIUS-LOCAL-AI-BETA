# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# Animations 10.0 – Dimensional Shift, Reality Distortion,
# Multi-Orb Echo Network, Deep Insight Burst
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
# DIMENSIONAL SHIFT LAYERS – subtle dimensional offsets
# ------------------------------------------------------------
class OrbDimensionalShift:
    def __init__(self, orb):
        self.orb = orb
        self.shift = 0.0
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # dimensional oscillation
        self.shift = 0.03 * math.sin(self._time * 3.3)

        # apply dimensional shift to core layers
        self.orb.inner_scale += self.shift * 0.5
        self.orb.mid_scale += self.shift * 0.3
        self.orb.outer_scale += self.shift * 0.1


# ------------------------------------------------------------
# REALITY DISTORTION – bending space around the orb
# ------------------------------------------------------------
class OrbRealityDistortion:
    def __init__(self):
        self.distortion = 0.0
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # distortion wave
        self.distortion = 0.1 * math.sin(self._time * 1.5)


# ------------------------------------------------------------
# MULTI-ORB ECHO NETWORK – echo copies of the orb
# ------------------------------------------------------------
class OrbEchoNetwork:
    def __init__(self):
        self.echoes = []  # (scale, intensity, life)

    def spawn(self, orb) -> None:
        self.echoes.append([
            orb.outer_scale,
            orb.intensity,
            1.0
        ])

    def update(self, delta_time: float) -> None:
        for e in self.echoes:
            e[0] += delta_time * 0.4     # echo expands
            e[1] -= delta_time * 0.6     # intensity fades
            e[2] -= delta_time * 0.7     # life fades

        self.echoes = [e for e in self.echoes if e[2] > 0]


# ------------------------------------------------------------
# DEEP INSIGHT BURST – flash of deep understanding
# ------------------------------------------------------------
class OrbDeepInsightBurst:
    def __init__(self):
        self.radius = 0.0
        self.intensity = 0.0
        self.active = False

    def trigger(self) -> None:
        self.radius = 0.0
        self.intensity = 1.0
        self.active = True

    def update(self, delta_time: float) -> None:
        if not self.active:
            return

        # burst expands rapidly
        self.radius += delta_time * 3.0
        self.intensity -= delta_time * 1.2

        if self.intensity <= 0:
            self.intensity = 0
            self.active = False
