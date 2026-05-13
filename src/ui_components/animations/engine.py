# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# Animations 5.0 – Deep Breathing, Multi-Core, Intelligence Pulse,
# Link Effect, Energy Field
# ============================================================

import math
import random
from typing import Protocol, List


# ------------------------------------------------------------
# PROTOKOL – všetko, čo sa má animovať, musí mať update()
# ------------------------------------------------------------
class Animatable(Protocol):
    def update(self, delta_time: float) -> None:
        ...


# ------------------------------------------------------------
# ANIMATION ENGINE 2.0 (bez zmeny)
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
# ORBOBJECT 3.0 – viacvrstvové jadro
# ------------------------------------------------------------
class OrbObject:
    def __init__(self):
        self.inner_scale = 0.8
        self.mid_scale = 1.0
        self.outer_scale = 1.2

        self.intensity = 1.0
        self.color = (0.2, 0.6, 1.0)

        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # Inner core – rýchlejšie pulzovanie
        self.inner_scale = 0.8 + 0.03 * math.sin(self._time * 3.5)

        # Mid core – stredné pulzovanie
        self.mid_scale = 1.0 + 0.05 * math.sin(self._time * 2.0)

        # Outer core – pomalé hlboké dýchanie
        self.outer_scale = 1.2 + 0.07 * math.sin(self._time * 1.0)

        # Inteligentný pulz (AI heartbeat)
        self.intensity = 1.0 + 0.15 * math.sin(self._time * 4.0)


# ------------------------------------------------------------
# ORB BREATHING 2.0 – hlboké AI dýchanie
# ------------------------------------------------------------
class OrbBreathingEffect:
    def __init__(self, orb: OrbObject):
        self.orb = orb
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # Hlboké dýchanie ovplyvňuje outer core
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

        # Inteligentný pulz – rýchlejšie, jemné vibrácie
        self.orb.intensity = 1.0 + 0.2 * math.sin(self._time * 6.0)


# ------------------------------------------------------------
# ORB LINK EFFECT – prepojenie s agentom
# ------------------------------------------------------------
class OrbLinkEffect:
    def __init__(self):
        self.lines = []  # (angle, length, life)

    def trigger(self):
        # Vytvorenie energetických vlákien
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
# ORB ENERGY FIELD – dynamické pole okolo ORBu
# ------------------------------------------------------------
class OrbEnergyField:
    def __init__(self):
        self.offset = 0.0
        self.strength = 1.0

    def update(self, delta_time: float) -> None:
        # Plynulé prúdenie energie
        self.offset = (self.offset + delta_time * 0.5) % 1.0

        # Jemné pulzovanie sily poľa
        self.strength = 1.0 + 0.1 * math.sin(self.offset * 6.28)
