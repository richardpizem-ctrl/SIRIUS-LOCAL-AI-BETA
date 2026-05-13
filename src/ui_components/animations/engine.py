# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# AnimationEngine 2.0 + OrbObject 2.0 + OrbRingObject 1.0
# OrbGlowObject 1.0 + OrbStateController 1.0
# ============================================================

import math
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
        self.color = (0.2, 0.6, 1.0)  # SIRIUS modro-tyrkysová
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # Pulzovanie veľkosti (dýchanie)
        self.scale = 1.0 + 0.05 * math.sin(self._time * 2.0)

        # Pulzovanie intenzity svetla
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

        # Rotácia
        self.rotation = (self.rotation + delta_time * 40.0) % 360.0

        # Pulzovanie hrúbky
        self.thickness = 1.0 + 0.05 * math.sin(self._time * 1.5)

        # Pulzovanie intenzity
        self.intensity = 0.8 + 0.1 * math.sin(self._time * 2.0)


# ------------------------------------------------------------
# ORBGLOWOBJECT 1.0 – svetelná aura okolo ORBu
# ------------------------------------------------------------
class OrbGlowObject:
    def __init__(self):
        self.radius = 1.5
        self.intensity = 0.5
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # Jemné pulzovanie svetelnej aury
        self.radius = 1.5 + 0.1 * math.sin(self._time * 1.2)
        self.intensity = 0.5 + 0.1 * math.sin(self._time * 2.5)


# ------------------------------------------------------------
# ORBSTATECONTROLLER 1.0 – farby podľa stavu agenta
# ------------------------------------------------------------
class OrbStateController:
    """
    Riadi farbu ORBu podľa stavu agenta.
    Stavy:
        idle
        thinking
        analyzing
        warning
        success
    """

    STATE_COLORS = {
        "idle":     (0.2, 0.6, 1.0),   # modrá
        "thinking": (0.4, 0.8, 1.0),   # svetlejšia modrá
        "analyzing":(0.1, 0.9, 0.9),   # tyrkysová
        "warning":  (1.0, 0.3, 0.3),   # červená
        "success":  (0.2, 1.0, 0.4),   # zelená
    }

    def __init__(self, orb: OrbObject):
        self.orb = orb
        self.state = "idle"
        self.transition_speed = 3.0  # rýchlosť prechodu farby

    def set_state(self, new_state: str) -> None:
        if new_state in self.STATE_COLORS:
            self.state = new_state

    def update(self, delta_time: float) -> None:
        target_color = self.STATE_COLORS[self.state]
        r, g, b = self.orb.color

        # Plynulý prechod farby
        self.orb.color = (
            r + (target_color[0] - r) * delta_time * self.transition_speed,
            g + (target_color[1] - g) * delta_time * self.transition_speed,
            b + (target_color[2] - b) * delta_time * self.transition_speed,
        )
