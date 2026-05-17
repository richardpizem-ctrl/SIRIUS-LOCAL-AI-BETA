# engine.py
# SIRIUS LOCAL AI – ORB ANIMATION SYSTEM 4.3.x
# Phase‑4 deterministic animation engine with safe‑mode and degraded‑mode

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
# ANIMATION ENGINE – Phase‑4 core update loop
# ------------------------------------------------------------
class AnimationEngine:
    """
    AnimationEngine 4.3.x

    Responsibilities:
        - Deterministic update loop
        - Safe‑mode and degraded‑mode support
        - Global animation governor
        - Object registry (Phase‑4)
        - Error‑safe update cycle
        - Offline-only behavior
    """

    def __init__(self) -> None:
        self._objects: List[Animatable] = []
        self._running: bool = True
        self._animations_enabled: bool = True

        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # Object management
    # ---------------------------------------------------------

    def add_object(self, obj: Animatable) -> None:
        if obj not in self._objects:
            self._objects.append(obj)

    def remove_object(self, obj: Animatable) -> None:
        if obj in self._objects:
            self._objects.remove(obj)

    def clear(self) -> None:
        self._objects.clear()

    # ---------------------------------------------------------
    # Engine control
    # ---------------------------------------------------------

    def stop(self) -> None:
        self._running = False

    def start(self) -> None:
        self._running = True

    def set_animations_enabled(self, enabled: bool) -> None:
        self._animations_enabled = enabled

    # ---------------------------------------------------------
    # Safe‑mode
    # ---------------------------------------------------------

    def enter_safe_mode(self) -> None:
        self.safe_mode = True
        self._animations_enabled = False

    def exit_safe_mode(self) -> None:
        self.safe_mode = False
        self._animations_enabled = True

    # ---------------------------------------------------------
    # Update loop (Phase‑4)
    # ---------------------------------------------------------

    def update(self, delta_time: float) -> None:
        """
        Deterministic update loop with:
            - safe‑mode bypass
            - degraded‑mode fallback
            - error‑safe object updates
        """

        if self.safe_mode:
            return

        if not self._running or not self._animations_enabled:
            return

        try:
            for obj in list(self._objects):
                try:
                    obj.update(delta_time)
                except Exception:
                    # Individual object failure → remove object, engine continues
                    self._objects.remove(obj)

        except Exception:
            # Global failure → degraded mode
            self.degraded_mode = True
            self._animations_enabled = False
