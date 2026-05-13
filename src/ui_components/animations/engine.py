# ============================================================
# SIRIUS LOCAL AI – ui_components/animations/engine.py
# SIRIUS ORB ANIMATION SYSTEM – FINAL MERGED VERSION (1.0–12.0)
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
# ANIMATION ENGINE – core update loop
# ------------------------------------------------------------
class AnimationEngine:
    def __init__(self) -> None:
        self._objects: List[Animatable] = []
        self._running: bool = True
        # global toggle for all animations
        self._animations_enabled: bool = True

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

    def set_animations_enabled(self, enabled: bool) -> None:
        self._animations_enabled = enabled

    def update(self, delta_time: float) -> None:
        if not self._running or not self._animations_enabled:
            return
        for obj in list(self._objects):
            obj.update(delta_time)


# ------------------------------------------------------------
# ORB OBJECT – neural multi-layer core
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
# BASIC ORB VISUAL ELEMENTS (RING, GLOW, STATE)
# ------------------------------------------------------------
class OrbRingObject:
    def __init__(self):
        self.rotation = 0.0
        self.thickness = 1.0
        self.intensity = 0.8
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.rotation = (self.rotation + delta_time * 40.0) % 360.0
        self.thickness = 1.0 + 0.05 * math.sin(self._time * 1.5)
        self.intensity = 0.8 + 0.1 * math.sin(self._time * 2.0)


class OrbGlowObject:
    def __init__(self):
        self.radius = 1.5
        self.intensity = 0.5
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.radius = 1.5 + 0.1 * math.sin(self._time * 1.2)
        self.intensity = 0.5 + 0.1 * math.sin(self._time * 2.5)


class OrbStateController:
    STATE_COLORS = {
        "idle":     (0.2, 0.6, 1.0),
        "thinking": (0.4, 0.8, 1.0),
        "analyzing": (0.1, 0.9, 0.9),
        "warning":  (1.0, 0.3, 0.3),
        "success":  (0.2, 1.0, 0.4),
    }

    def __init__(self, orb: OrbObject):
        self.orb = orb
        self.state = "idle"
        self.transition_speed = 3.0

    def set_state(self, new_state: str) -> None:
        if new_state in self.STATE_COLORS:
            self.state = new_state

    def update(self, delta_time: float) -> None:
        target = self.STATE_COLORS[self.state]
        r, g, b = self.orb.color
        self.orb.color = (
            r + (target[0] - r) * delta_time * self.transition_speed,
            g + (target[1] - g) * delta_time * self.transition_speed,
            b + (target[2] - b) * delta_time * self.transition_speed,
        )


# ------------------------------------------------------------
# THINKING / WARNING / SUCCESS / ENERGY FLOW
# ------------------------------------------------------------
class OrbThinkingEffect:
    def __init__(self):
        self.sparks = []  # (angle, speed, life)

    def update(self, delta_time: float) -> None:
        if random.random() < 0.15:
            self.sparks.append([
                random.uniform(0, 360),
                random.uniform(20, 60),
                1.0
            ])
        for spark in self.sparks:
            spark[2] -= delta_time * 1.5
        self.sparks = [s for s in self.sparks if s[2] > 0]


class OrbWarningFlash:
    def __init__(self):
        self.flash_intensity = 0.0

    def trigger(self) -> None:
        self.flash_intensity = 1.0

    def update(self, delta_time: float) -> None:
        if self.flash_intensity > 0:
            self.flash_intensity -= delta_time * 2.5
            if self.flash_intensity < 0:
                self.flash_intensity = 0.0


class OrbSuccessBurst:
    def __init__(self):
        self.radius = 0.0
        self.active = False

    def trigger(self) -> None:
        self.radius = 0.0
        self.active = True

    def update(self, delta_time: float) -> None:
        if self.active:
            self.radius += delta_time * 4.0
            if self.radius > 2.0:
                self.active = False


class OrbEnergyFlow:
    def __init__(self):
        self.offset = 0.0

    def update(self, delta_time: float) -> None:
        self.offset = (self.offset + delta_time * 0.8) % 1.0


# ------------------------------------------------------------
# DEEP BREATHING / INTELLIGENCE PULSE / LINK / FIELD
# ------------------------------------------------------------
class OrbBreathingEffect:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.orb.outer_scale = 1.2 + 0.12 * math.sin(self._time * 0.7)


class OrbIntelligencePulse:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.orb.intensity = 1.0 + 0.2 * math.sin(self._time * 6.0)


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


class OrbEnergyField:
    def __init__(self):
        self.offset = 0.0
        self.strength = 1.0

    def update(self, delta_time: float) -> None:
        self.offset = (self.offset + delta_time * 0.5) % 1.0
        self.strength = 1.0 + 0.1 * math.sin(self.offset * 6.28)


# ------------------------------------------------------------
# NEURAL PATHWAYS / DECISION MAP / SYNAPSE / MEMORY / LOGIC
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
        self.nodes = [n for n in self.nodes if n[2] > 0]


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


class OrbLogicFlow:
    def __init__(self):
        self.offset = 0.0
        self.speed = 1.0

    def update(self, delta_time: float) -> None:
        self.offset = (self.offset + delta_time * self.speed) % 1.0


# ------------------------------------------------------------
# CONSCIOUSNESS / REASONING / META-THOUGHT / SELF-REFLECTION
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


class OrbReasoningWaves:
    def __init__(self):
        self.phase = 0.0
        self.amplitude = 0.0

    def update(self, delta_time: float) -> None:
        self.phase = (self.phase + delta_time * 1.2) % (2 * math.pi)
        self.amplitude = 0.3 + 0.2 * math.sin(self.phase * 2.0)


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


# ------------------------------------------------------------
# TEMPORAL / PREDICTIVE / COGNITIVE MESH / FOCUS / AWARENESS
# ------------------------------------------------------------
class OrbTemporalEchoes:
    def __init__(self):
        self.echoes = []  # (inner_scale, mid_scale, outer_scale, intensity, life)

    def capture(self, orb: OrbObject) -> None:
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
            self.life = 0.0


# ------------------------------------------------------------
# QUANTUM / SUPERPOSITION / PROBABILITY / HYPER-FOCUS
# ------------------------------------------------------------
class OrbQuantumFluctuations:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self._time = 0.0
        self.strength = 0.02

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        jitter = self.strength * math.sin(self._time * 50.0)
        self.orb.inner_scale += jitter
        self.orb.mid_scale += jitter * 0.7
        self.orb.outer_scale += jitter * 0.4


class OrbSuperposition:
    def __init__(self):
        self.states = []  # (inner_scale, mid_scale, outer_scale, intensity, life)

    def collapse(self, orb: OrbObject) -> None:
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


class OrbProbabilityCloud:
    def __init__(self):
        self.points = []  # (angle, radius, probability, life)

    def generate(self) -> None:
        for _ in range(20):
            self.points.append([
                random.uniform(0, 360),
                random.uniform(0.5, 2.0),
                random.uniform(0.1, 1.0),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for p in self.points:
            p[3] -= delta_time * 0.4
        self.points = [p for p in self.points if p[3] > 0]


class OrbHyperFocus:
    def __init__(self, orb: OrbObject):
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
            self.orb.inner_scale *= 0.995
            self.orb.mid_scale *= 0.997
            self.orb.outer_scale *= 0.999
            self.orb.intensity = min(2.0, self.orb.intensity + delta_time * 1.5)
            self.intensity = max(0.0, self.intensity - delta_time * 0.3)
        else:
            self.orb.intensity = max(1.0, self.orb.intensity - delta_time * 0.5)
            self.intensity = max(0.0, self.intensity - delta_time * 1.0)


# ------------------------------------------------------------
# DIMENSIONAL / REALITY / ECHO NETWORK / DEEP INSIGHT
# ------------------------------------------------------------
class OrbDimensionalShift:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self.shift = 0.0
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.shift = 0.03 * math.sin(self._time * 3.3)
        self.orb.inner_scale += self.shift * 0.5
        self.orb.mid_scale += self.shift * 0.3
        self.orb.outer_scale += self.shift * 0.1


class OrbRealityDistortion:
    def __init__(self):
        self.distortion = 0.0
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.distortion = 0.1 * math.sin(self._time * 1.5)


class OrbEchoNetwork:
    def __init__(self):
        self.echoes = []  # (scale, intensity, life)

    def spawn(self, orb: OrbObject) -> None:
        self.echoes.append([
            orb.outer_scale,
            orb.intensity,
            1.0
        ])

    def update(self, delta_time: float) -> None:
        for e in self.echoes:
            e[0] += delta_time * 0.4
            e[1] -= delta_time * 0.6
            e[2] -= delta_time * 0.7
        self.echoes = [e for e in self.echoes if e[2] > 0]


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
        self.radius += delta_time * 3.0
        self.intensity -= delta_time * 1.2
        if self.intensity <= 0:
            self.intensity = 0.0
            self.active = False


# ------------------------------------------------------------
# EMERGENT / RESONANCE / INSIGHT / HALO / REFLECTION FIELD
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
            layer[0] += delta_time * 0.3
            layer[2] -= delta_time * 0.5
        self.layers = [l for l in self.layers if l[2] > 0]


class OrbCognitiveResonance:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self.phase = 0.0

    def update(self, delta_time: float) -> None:
        self.phase += delta_time * 2.0
        resonance = 0.03 * math.sin(self.phase * 3.0)
        self.orb.inner_scale += resonance * 1.0
        self.orb.mid_scale += resonance * 0.6
        self.orb.outer_scale += resonance * 0.3


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
            b[1] -= delta_time * 0.4
            b[2] -= delta_time * 0.7
        self.branches = [b for b in self.branches if b[2] > 0]


class OrbAwarenessHalo:
    def __init__(self):
        self.radius = 1.5
        self.intensity = 0.0
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.radius = 1.5 + 0.1 * math.sin(self._time * 1.3)
        self.intensity = 0.3 + 0.2 * math.sin(self._time * 2.0)


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


# ------------------------------------------------------------
# UNIFIED CORE / HARMONIC MATRIX / SINGULARITY / RIPPLE / TOTALITY
# ------------------------------------------------------------
class OrbUnifiedCore:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self.phase = 0.0

    def update(self, delta_time: float) -> None:
        self.phase += delta_time * 1.5
        sync = 0.05 * math.sin(self.phase * 2.0)
        self.orb.inner_scale = 0.8 + sync * 1.2
        self.orb.mid_scale   = 1.0 + sync * 0.9
        self.orb.outer_scale = 1.2 + sync * 0.6
        self.orb.intensity = 1.0 + 0.25 * math.sin(self.phase * 3.0)


class OrbHarmonicFieldMatrix:
    def __init__(self):
        self.points = []  # (angle, radius, life)

    def activate(self) -> None:
        for _ in range(24):
            self.points.append([
                random.uniform(0, 360),
                random.uniform(1.0, 2.2),
                1.0
            ])

    def update(self, delta_time: float) -> None:
        for p in self.points:
            p[2] -= delta_time * 0.4
        self.points = [p for p in self.points if p[2] > 0]


class OrbInsightSingularity:
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
        self.radius += delta_time * 4.0
        self.intensity -= delta_time * 1.4
        if self.intensity <= 0:
            self.intensity = 0.0
            self.active = False


class OrbCognitiveRipple:
    def __init__(self):
        self.ripples = []  # (radius, life)

    def emit(self) -> None:
        self.ripples.append([0.0, 1.0])

    def update(self, delta_time: float) -> None:
        for r in self.ripples:
            r[0] += delta_time * 2.5
            r[1] -= delta_time * 0.8
        self.ripples = [r for r in self.ripples if r[1] > 0]


class OrbTotalityLayer:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self.phase = 0.0
        self.intensity = 0.0

    def update(self, delta_time: float) -> None:
        self.phase += delta_time * 0.9
        self.intensity = 0.2 + 0.15 * math.sin(self.phase * 1.7)
        factor = 1.0 + 0.02 * math.sin(self.phase * 2.3)
        self.orb.inner_scale *= factor
        self.orb.mid_scale   *= factor
        self.orb.outer_scale *= factor
