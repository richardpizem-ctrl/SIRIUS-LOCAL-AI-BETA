# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# Animations 6.0 – Neural Pathways, Decision Map, Synapse Sparks,
# Memory Rings, Logic Flow
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
# ORBOBJECT 4.0 – neurónové jadro
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

        # Inner core – rýchle neurónové vibrácie
        self.inner_scale = 0.8 + 0.04 * math.sin(self._time * 4.5)

        # Mid core – AI processing
        self.mid_scale = 1.0 + 0.06 * math.sin(self._time * 2.2)

        # Outer core – hlboké AI dýchanie
        self.outer_scale = 1.2 + 0.08 * math.sin(self._time * 1.1)

        # Inteligentný pulz
        self.intensity = 1.0 + 0.18 * math.sin(self._time * 5.0)


# ------------------------------------------------------------
# NEURAL PATHWAYS – neurónové spojenia
# ------------------------------------------------------------
class OrbNeuralPathways:
    def __init__(self):
        self.paths = []  # (angle, length, life)

    def trigger(self):
        # Aktivácia neurónových spojení
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
# DECISION MAP – vizualizácia rozhodovania
# ------------------------------------------------------------
class OrbDecisionMap:
    def __init__(self):
        self.nodes = []  # (angle, radius, life)

    def activate(self):
        # Vytvorenie rozhodovacích uzlov
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


# ------------------------------------------------------------
# SYNAPSE SPARKS – synaptické výboje
# ------------------------------------------------------------
class OrbSynapseSparks:
    def __init__(self):
        self.sparks = []  # (angle, speed, life)

    def update(self, delta_time: float) -> None:
        # Náhodné synaptické výboje
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
# MEMORY RINGS – pamäťové vrstvy
# ------------------------------------------------------------
class OrbMemoryRings:
    def __init__(self):
        self.rings = []  # (radius, life)

    def store(self):
        # Vytvorenie pamäťového kruhu
        self.rings.append([
            random.uniform(1.3, 1.8),
            1.0
        ])

    def update(self, delta_time: float) -> None:
        for r in self.rings:
            r[1] -= delta_time * 0.5

        self.rings = [r for r in self.rings if r[1] > 0]


# ------------------------------------------------------------
# LOGIC FLOW – tok logiky medzi vrstvami
# ------------------------------------------------------------
class OrbLogicFlow:
    def __init__(self):
        self.offset = 0.0
        self.speed = 1.0

    def update(self, delta_time: float) -> None:
        self.offset = (self.offset + delta_time * self.speed) % 1.0
