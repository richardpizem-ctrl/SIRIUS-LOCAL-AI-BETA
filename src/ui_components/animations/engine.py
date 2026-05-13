# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# Animations 9.0 – Quantum Fluctuations, Superposition,
# Probability Cloud, Hyper-Focus Mode
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
# QUANTUM FLUCTUATIONS – micro-vibrations of the quantum core
# ------------------------------------------------------------
class OrbQuantumFluctuations:
    def __init__(self, orb):
        self.orb = orb
        self._time = 0.0
        self.strength = 0.02  # subtle but visible

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # micro jitter on all core layers
        jitter = self.strength * math.sin(self._time * 50.0)

        self.orb.inner_scale += jitter
        self.orb.mid_scale += jitter * 0.7
        self.orb.outer_scale += jitter * 0.4


# ------------------------------------------------------------
# MULTI-STATE SUPERPOSITION – orb exists in multiple states
# ------------------------------------------------------------
class OrbSuperposition:
    def __init__(self):
        self.states = []  # (inner_scale, mid_scale, outer_scale, intensity, life)

    def collapse(self, orb) -> None:
        # capture current state as one branch of superposition
        self.states.append([
            orb.inner_scale,
            orb.mid_scale,
            orb.outer_scale,
            orb.intensity,
            1.0
        ])

    def update(self, delta_time: float) -> None:
        for s in self.states:
            s[4] -= delta_time * 0.5
        self.states = [s for s in self.states if s[4] > 0]


# ------------------------------------------------------------
# PROBABILITY CLOUD – probability distribution of AI reasoning
# ------------------------------------------------------------
class OrbProbabilityCloud:
    def __init__(self):
        self.points = []  # (angle, radius, probability, life)

    def generate(self) -> None:
        for _ in range(20):
            self.points.append([
                random.uniform(0, 360),
                random.uniform(0.5, 2.0),
                random.uniform(0.1, 1.0),  # probability weight
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for p in self.points:
            p[3] -= delta_time * 0.4
        self.points = [p for p in self.points if p[3] > 0]


# ------------------------------------------------------------
# HYPER-FOCUS MODE – extreme AI concentration
# ------------------------------------------------------------
class OrbHyperFocus:
    def __init__(self, orb):
        self.orb = orb
        self.active = False
        self.intensity = 0.0

    def engage(self) -> None:
        self.active = True
        self.intensity = 1.0

    def disengage(self) -> None:
        self.active = False

    def update(self, delta_time: float) -> None:
        if self.active:
            # orb shrinks slightly and intensifies
            self.orb.inner_scale *= 0.995
            self.orb.mid_scale *= 0.997
            self.orb.outer_scale *= 0.999

            self.orb.intensity = min(2.0, self.orb.intensity + delta_time * 1.5)

            self.intensity = max(0.0, self.intensity - delta_time * 0.3)
        else:
            # return to normal
            self.orb.intensity = max(1.0, self.orb.intensity - delta_time * 0.5)
            self.intensity = max(0.0, self.intensity - delta_time * 1.0)
