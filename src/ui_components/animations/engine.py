# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# Animations 7.0 – Neural Core, Pathways, Decision Map,
# Synapse Sparks, Memory Rings, Logic Flow,
# Consciousness Field, Reasoning Waves, Meta-Thought, Self-Reflection
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
# ANIMATION ENGINE 2.0
# ------------------------------------------------------------
class AnimationEngine:
    def __init__(self) -> None:
        self._objects: List[Animatable] = []
        self._running: bool = True

    def add_object(self, obj: Animatable) -> None:
        if obj not in self._objects:
            self._objects.append(obj)

    def remove_object(self, obj: Animatable) -> None:
        if obj in self._objects:
            self._objects.remove(obj)

    def clear(self) -> None:
        self._objects.clear()

    def stop(self) -> None:
        self._running = False

    def start(self) -> None:
        self._running = True

    def update(self, delta_time: float) -> None:
        if not self._running:
            return

        for obj in list(self._objects):
            obj.update(delta_time)


# ------------------------------------------------------------
# ORB OBJECT 4.0 – neural core
# ------------------------------------------------------------
class OrbObject:
    def __init__(self):
        # multi-layer core
        self.inner_scale = 0.8
        self.mid_scale = 1.0
        self.outer_scale = 1.2

        self.intensity = 1.0
        self.color = (0.2, 0.6, 1.0)

        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # inner core – fast neural vibration
        self.inner_scale = 0.8 + 0.04 * math.sin(self._time * 4.5)

        # mid core – processing layer
        self.mid_scale = 1.0 + 0.06 * math.sin(self._time * 2.2)

        # outer core – deep breathing
        self.outer_scale = 1.2 + 0.08 * math.sin(self._time * 1.1)

        # global intelligence pulse
        self.intensity = 1.0 + 0.18 * math.sin(self._time * 5.0)


# ------------------------------------------------------------
# ORB BREATHING 2.0 – deep AI breathing
# ------------------------------------------------------------
class OrbBreathingEffect:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.orb.outer_scale = 1.2 + 0.12 * math.sin(self._time * 0.7)


# ------------------------------------------------------------
# ORB INTELLIGENCE PULSE – AI heartbeat
# ------------------------------------------------------------
class OrbIntelligencePulse:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.orb.intensity = 1.0 + 0.2 * math.sin(self._time * 6.0)


# ------------------------------------------------------------
# ORB LINK EFFECT – link to agent
# ------------------------------------------------------------
class OrbLinkEffect:
    def __init__(self):
        self.lines = []  # (angle, length, life)

    def trigger(self) -> None:
        for _ in range(5):
            self.lines.append([
                random.uniform(0, 360),
                random.uniform(0.5, 1.5),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for line in self.lines:
            line[2] -= delta_time * 1.2
        self.lines = [l for l in self.lines if l[2] > 0]


# ------------------------------------------------------------
# ORB ENERGY FIELD – dynamic field around orb
# ------------------------------------------------------------
class OrbEnergyField:
    def __init__(self):
        self.offset = 0.0
        self.strength = 1.0

    def update(self, delta_time: float) -> None:
        self.offset = (self.offset + delta_time * 0.5) % 1.0
        self.strength = 1.0 + 0.1 * math.sin(self.offset * 6.28)


# ------------------------------------------------------------
# NEURAL PATHWAYS – neural connections
# ------------------------------------------------------------
class OrbNeuralPathways:
    def __init__(self):
        self.paths = []  # (angle, length, life)

    def trigger(self) -> None:
        for _ in range(8):
            self.paths.append([
                random.uniform(0, 360),
                random.uniform(0.3, 1.0),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for p in self.paths:
            p[2] -= delta_time * 1.0
        self.paths = [p for p in self.paths if p[2] > 0]


# ------------------------------------------------------------
# DECISION MAP – decision nodes
# ------------------------------------------------------------
class OrbDecisionMap:
    def __init__(self):
        self.nodes = []  # (angle, radius, life)

    def activate(self) -> None:
        for _ in range(5):
            self.nodes.append([
                random.uniform(0, 360),
                random.uniform(0.4, 1.2),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for n in self.nodes:
            n[2] -= delta_time * 0.8
        self.nodes = [n for n in self.nodes if n[1] > 0 and n[2] > 0]


# ------------------------------------------------------------
# SYNAPSE SPARKS – synaptic bursts
# ------------------------------------------------------------
class OrbSynapseSparks:
    def __init__(self):
        self.sparks = []  # (angle, speed, life)

    def update(self, delta_time: float) -> None:
        if random.random() < 0.25:
            self.sparks.append([
                random.uniform(0, 360),
                random.uniform(30, 80),
                1.0
            ])

        for s in self.sparks:
            s[2] -= delta_time * 1.8

        self.sparks = [s for s in self.sparks if s[2] > 0]


# ------------------------------------------------------------
# MEMORY RINGS – long-term memory layers
# ------------------------------------------------------------
class OrbMemoryRings:
    def __init__(self):
        self.rings = []  # (radius, life)

    def store(self) -> None:
        self.rings.append([
            random.uniform(1.3, 1.8),
            1.0
        ])

    def update(self, delta_time: float) -> None:
        for r in self.rings:
            r[1] -= delta_time * 0.5
        self.rings = [r for r in self.rings if r[1] > 0]


# ------------------------------------------------------------
# LOGIC FLOW – logical flow between layers
# ------------------------------------------------------------
class OrbLogicFlow:
    def __init__(self):
        self.offset = 0.0
        self.speed = 1.0

    def update(self, delta_time: float) -> None:
        self.offset = (self.offset + delta_time * self.speed) % 1.0


# ------------------------------------------------------------
# CONSCIOUSNESS FIELD – global awareness field
# ------------------------------------------------------------
class OrbConsciousnessField:
    def __init__(self):
        self.radius = 2.0
        self.intensity = 0.0
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.radius = 2.0 + 0.2 * math.sin(self._time * 0.4)
        self.intensity = 0.4 + 0.2 * math.sin(self._time * 0.9)


# ------------------------------------------------------------
# REASONING WAVES – waves of reasoning
# ------------------------------------------------------------
class OrbReasoningWaves:
    def __init__(self):
        self.phase = 0.0
        self.amplitude = 0.0

    def update(self, delta_time: float) -> None:
        self.phase = (self.phase + delta_time * 1.2) % (2 * math.pi)
        self.amplitude = 0.3 + 0.2 * math.sin(self.phase * 2.0)


# ------------------------------------------------------------
# META-THOUGHT LAYERS – higher-level thinking
# ------------------------------------------------------------
class OrbMetaThoughtLayers:
    def __init__(self):
        self.layers = []  # (radius, intensity, life)

    def spawn(self) -> None:
        self.layers.append([
            random.uniform(1.0, 1.6),
            random.uniform(0.3, 0.7),
            1.0
        ])

    def update(self, delta_time: float) -> None:
        for layer in self.layers:
            layer[2] -= delta_time * 0.6
        self.layers = [l for l in self.layers if l[2] > 0]


# ------------------------------------------------------------
# SELF-REFLECTION PULSE – introspective pulse
# ------------------------------------------------------------
class OrbSelfReflectionPulse:
    def __init__(self):
        self.intensity = 0.0

    def trigger(self) -> None:
        self.intensity = 1.0

    def update(self, delta_time: float) -> None:
        if self.intensity > 0:
            self.intensity -= delta_time * 1.5
            if self.intensity < 0:
                self.intensity = 0.0
