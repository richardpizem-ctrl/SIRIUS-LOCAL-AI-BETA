# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# AnimationEngine 2.0 + ORB 2.0 + Ring 1.0 + Glow 1.0 + State 1.0
# + ThinkingEffect 1.0 + WarningFlash 1.0 + SuccessBurst 1.0
# + EnergyFlow 1.0
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
# ORBOBJECT 2.0 – AI ORB
# ------------------------------------------------------------
class OrbObject:
    def __init__(self):
        self.scale = 1.0
        self.intensity = 1.0
        self.color = (0.2, 0.6, 1.0)
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        self.scale = 1.0 + 0.05 * math.sin(self._time * 2.0)
        self.intensity = 1.0 + 0.1 * math.sin(self._time * 3.0)


# ------------------------------------------------------------
# ORBRINGOBJECT 1.0 – rotujúci prstenec
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


# ------------------------------------------------------------
# ORBGLOWOBJECT 1.0 – svetelná aura
# ------------------------------------------------------------
class OrbGlowObject:
    def __init__(self):
        self.radius = 1.5
        self.intensity = 0.5
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time
        self.radius = 1.5 + 0.1 * math.sin(self._time * 1.2)
        self.intensity = 0.5 + 0.1 * math.sin(self._time * 2.5)


# ------------------------------------------------------------
# ORBSTATECONTROLLER 1.0 – farby podľa stavu agenta
# ------------------------------------------------------------
class OrbStateController:
    STATE_COLORS = {
        "idle":     (0.2, 0.6, 1.0),
        "thinking": (0.4, 0.8, 1.0),
        "analyzing":(0.1, 0.9, 0.9),
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
# THINKING EFFECT 1.0 – iskry pri premýšľaní
# ------------------------------------------------------------
class OrbThinkingEffect:
    def __init__(self):
        self.sparks = []  # list of (angle, speed, life)

    def update(self, delta_time: float) -> None:
        # generovanie nových iskier
        if random.random() < 0.15:
            self.sparks.append([
                random.uniform(0, 360),   # angle
                random.uniform(20, 60),   # speed
                1.0                       # life
            ])

        # aktualizácia iskier
        for spark in self.sparks:
            spark[2] -= delta_time * 1.5  # life decay

        # odstránenie mŕtvych iskier
        self.sparks = [s for s in self.sparks if s[2] > 0]


# ------------------------------------------------------------
# WARNING FLASH 1.0 – červený výstražný záblesk
# ------------------------------------------------------------
class OrbWarningFlash:
    def __init__(self):
        self.flash_intensity = 0.0

    def trigger(self):
        self.flash_intensity = 1.0

    def update(self, delta_time: float) -> None:
        if self.flash_intensity > 0:
            self.flash_intensity -= delta_time * 2.5
            if self.flash_intensity < 0:
                self.flash_intensity = 0


# ------------------------------------------------------------
# SUCCESS BURST 1.0 – zelený energetický výbuch
# ------------------------------------------------------------
class OrbSuccessBurst:
    def __init__(self):
        self.radius = 0.0
        self.active = False

    def trigger(self):
        self.radius = 0.0
        self.active = True

    def update(self, delta_time: float) -> None:
        if self.active:
            self.radius += delta_time * 4.0
            if self.radius > 2.0:
                self.active = False


# ------------------------------------------------------------
# ENERGY FLOW 1.0 – prúdenie energie okolo ORBu
# ------------------------------------------------------------
class OrbEnergyFlow:
    def __init__(self):
        self.offset = 0.0

    def update(self, delta_time: float) -> None:
        self.offset = (self.offset + delta_time * 0.8) % 1.0
