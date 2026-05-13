# ============================================================
# SIRIUS LOCAL AI – ui_components/animations
# AnimationEngine 1.0 + OrbObject 1.0 (kompletný základ)
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
# ANIMATION ENGINE 1.0
# - registry objektov
# - add/remove
# - update loop
# ------------------------------------------------------------
class AnimationEngine:
    def __init__(self) -> None:
        self._objects: List[Animatable] = []
        self._running: bool = True

    def add_object(self, obj: Animatable) -> None:
        """Zaregistruje nový animovateľný objekt (napr. AI ORB)."""
        if obj not in self._objects:
            self._objects.append(obj)

    def remove_object(self, obj: Animatable) -> None:
        """Odstráni objekt z animácií."""
        if obj in self._objects:
            self._objects.remove(obj)

    def clear(self) -> None:
        """Vyčistí všetky animovateľné objekty."""
        self._objects.clear()

    def stop(self) -> None:
        """Zastaví animácie."""
        self._running = False

    def start(self) -> None:
        """Znovu spustí animácie."""
        self._running = True

    def update(self, delta_time: float) -> None:
        """Volá sa z hlavného UI loopu."""
        if not self._running:
            return

        for obj in list(self._objects):
            obj.update(delta_time)


# ------------------------------------------------------------
# ORBOBJECT 1.0 – základ AI ORB
# - pulzovanie (dýchanie)
# - intenzita svetla
# - farba (statická zatiaľ)
# ------------------------------------------------------------
class OrbObject:
    def __init__(self):
        self.scale = 1.0
        self.intensity = 1.0
        self.color = (0.2, 0.6, 1.0)  # SIRIUS modro-tyrkysová
        self._time = 0.0

    def update(self, delta_time: float) -> None:
        """Základné pulzovanie ORBu."""
        self._time += delta_time

        # Pulzovanie veľkosti (dýchanie)
        self.scale = 1.0 + 0.05 * math.sin(self._time * 2.0)

        # Pulzovanie intenzity svetla
        self.intensity = 1.0 + 0.1 * math.sin(self._time * 3.0)

        # Farba zatiaľ statická – verzia 1.0
        # (v 2.0 bude reagovať na stavy agenta)
