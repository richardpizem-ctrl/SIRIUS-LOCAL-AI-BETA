# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# Animations 11.0 – Emergent Thought Layers, Cognitive Resonance,
# Insight Convergence, Awareness Halo, Deep Reflection Field
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
# EMERGENT THOUGHT LAYERS – appear only during complex reasoning
# ------------------------------------------------------------
class OrbEmergentThoughtLayers:
    def __init__(self):
        self.layers = []  # (radius, intensity, life)

    def activate(self) -> None:
        for _ in range(3):
            self.layers.append([
                random.uniform(1.0, 1.7),
                random.uniform(0.4, 0.9),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for layer in self.layers:
            layer[0] += delta_time * 0.3   # expand
            layer[2] -= delta_time * 0.5   # fade
        self.layers = [l for l in self.layers if l[2] > 0]


# ------------------------------------------------------------
# COGNITIVE RESONANCE – harmonic resonance between orb layers
# ------------------------------------------------------------
class OrbCognitiveResonance:
    def __init__(self, orb):
        self.orb = orb
        self.phase = 0.0

    def update(self, delta_time: float) -> None:
        self.phase += delta_time * 2.0

        resonance = 0.03 * math.sin(self.phase * 3.0)

        # resonance affects all layers differently
        self.orb.inner_scale += resonance * 1.0
        self.orb.mid_scale += resonance * 0.6
        self.orb.outer_scale += resonance * 0.3


# ------------------------------------------------------------
# INSIGHT CONVERGENCE – merging multiple thought branches
# ------------------------------------------------------------
class OrbInsightConvergence:
    def __init__(self):
        self.branches = []  # (angle, radius, life)

    def converge(self) -> None:
        for _ in range(6):
            self.branches.append([
                random.uniform(0, 360),
                random.uniform(0.5, 1.5),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for b in self.branches:
            b[1] -= delta_time * 0.4   # branches collapse inward
            b[2] -= delta_time * 0.7
        self.branches = [b for b in self.branches if b[2] > 0]


# ------------------------------------------------------------
# AWARENESS HALO – subtle halo expanding with attention
# ------------------------------------------------------------
class OrbAwarenessHalo:
    def __init__(self):
        self.radius = 1.5
        self.intensity = 0.0
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # halo pulses gently
        self.radius = 1.5 + 0.1 * math.sin(self._time * 1.3)
        self.intensity = 0.3 + 0.2 * math.sin(self._time * 2.0)


# ------------------------------------------------------------
# DEEP REFLECTION FIELD – activated during introspection
# ------------------------------------------------------------
class OrbDeepReflectionField:
    def __init__(self):
        self.strength = 0.0
        self.active = False

    def engage(self) -> None:
        self.active = True
        self.strength = 1.0

    def disengage(self) -> None:
        self.active = False

    def update(self, delta_time: float) -> None:
        if self.active:
            self.strength = max(0.0, self.strength - delta_time * 0.3)
        else:
            self.strength = max(0.0, self.strength - delta_time * 0.8)
