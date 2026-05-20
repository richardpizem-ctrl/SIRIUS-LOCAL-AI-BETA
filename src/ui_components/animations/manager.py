# manager_4_4.py
# SIRIUS LOCAL AI – Animation Manager 4.4.0 PRO
# Phase‑4/5 scene controller with safe‑mode and degraded‑mode

from .animation_scenes_4_4 import (
    MoveScene44,
    CopyScene44,
    DeleteScene44,
    CreateFolderScene44
)


class AnimationManager44:
    """
    AnimationManager 4.4.0 PRO

    Responsibilities:
        - Manage animation scenes (Phase‑4)
        - Deterministic scene switching
        - Error‑safe lifecycle control
        - Safe‑mode and degraded‑mode support (Security Family 4.4)
        - Structured fallback behavior
        - Offline-only, no side-effects
        - Phase‑5 ready (sandbox, restricted-mode)
        - Self‑Repair 4.4 compatible
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

        self.current_scene = None

        # Preloaded scenes (Phase‑4 static registry)
        try:
            self.scenes = {
                "move": MoveScene44(),
                "copy": CopyScene44(),
                "delete": DeleteScene44(),
                "create_folder": CreateFolderScene44(),
            }
        except Exception:
            # If scene creation fails → degraded mode
            self.scenes = {}
            self.degraded_mode = True

    # ---------------------------------------------------------
    # Scene control
    # ---------------------------------------------------------

    def play(self, scene_name: str):
        """
        Start the requested scene by name.
        Safe-mode blocks all animations.
        """

        if self.safe_mode:
            return {"status": "safe_mode", "scene": None}

        try:
            if self.current_scene:
                self.current_scene.stop()

            scene = self.scenes.get(scene_name)

            if scene:
                self.current_scene = scene
                self.current_scene.start()
                return {"status": "ok", "scene": scene_name}

            return {"status": "not_found", "scene": scene_name}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "scene": scene_name,
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # Update loop
    # ---------------------------------------------------------

    def update(self, delta_time: float):
        """
        Update the active scene.
        Deterministic, safe-mode aware, error-safe.
        """

        if self.safe_mode:
            return

        if not self.current_scene:
            return

        try:
            if self.current_scene.active:
                self.current_scene.update(delta_time)

        except Exception:
            # Scene failure → degraded mode
            self.degraded_mode = True
            self.current_scene = None

    # ---------------------------------------------------------
    # Safe-mode
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True
        if self.current_scene:
            self.current_scene.stop()

    def exit_safe_mode(self):
        self.safe_mode = False

    def is_safe_mode(self) -> bool:
        return self.safe_mode

    def is_degraded_mode(self) -> bool:
        return self.degraded_mode
