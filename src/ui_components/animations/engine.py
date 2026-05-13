# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# AnimationEngine 2.0 + OrbObject 2.0 + OrbRingObject 1.0
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
# - registry objektov
# - add/remove
# - update loop
# - podpora vrstiev (základ pre viac objektov)
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
# - pulzovanie (dýchanie)
# - intenzita svetla
# - farba
# - pripravené na reakcie agenta
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

        # Farba zatiaľ statická – v 3.0 bude reagovať na stavy agenta


# ------------------------------------------------------------
# ORBRINGOBJECT 1.0 – rotujúci prstenec okolo ORBu
# - rotácia
# - zmena hrúbky
# - zmena intenzity
# ------------------------------------------------------------
class OrbRingObject:
    def __init__(self):
        self.rotation = 0.0          # rotácia v stupňoch
        self.thickness = 1.0         # hrúbka prstenca
        self.intensity = 0.8         # svetelná intenzita
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        self._time += delta_time

        # Rotácia prstenca
        self.rotation = (self.rotation + delta_time * 40.0) % 360.0

        # Jemné pulzovanie hrúbky
        self.thickness = 1.0 + 0.05 * math.sin(self._time * 1.5)

        # Pulzovanie intenzity
        self.intensity = 0.8 + 0.1 * math.sin(self._time * 2.0)
