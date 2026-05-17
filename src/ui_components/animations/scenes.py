# scenes.py
# SIRIUS LOCAL AI – Animation Scenes 4.3.x
# Phase‑4 safe-mode compatible animation scene system


class BaseScene:
    """
    BaseScene 4.3.x

    Responsibilities:
        - Provide deterministic scene lifecycle
        - Support safe-mode and degraded-mode
        - Provide structured update behavior
        - Host graphical objects (Phase‑5)
    """

    def __init__(self):
        self.objects = []      # graphical objects (Phase‑5)
        self.active = False
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------------

    def start(self):
        """Start the scene."""
        if self.safe_mode:
            return
        self.active = True

    def stop(self):
        """Stop the scene."""
        self.active = False

    def reset(self):
        """Reset scene state (Phase‑4)."""
        self.objects.clear()
        self.degraded_mode = False

    # ---------------------------------------------------------
    # Update loop
    # ---------------------------------------------------------

    def update(self, delta_time: float):
        """
        Scene update – implemented in subclasses.
        Must be error-safe and deterministic.
        """
        if self.safe_mode or not self.active:
            return

        try:
            self._update_impl(delta_time)
        except Exception:
            self.degraded_mode = True

    def _update_impl(self, delta_time: float):
        """Subclasses override this."""
        pass


# ---------------------------------------------------------
# MOVE SCENE
# ---------------------------------------------------------

class MoveScene(BaseScene):
    """Animation for moving files (postman)."""

    def __init__(self):
        super().__init__()

    def _update_impl(self, delta_time: float):
        # Movement animation logic (Phase‑5)
        pass


# ---------------------------------------------------------
# COPY SCENE
# ---------------------------------------------------------

class CopyScene(BaseScene):
    """Animation for copying (copy machine)."""

    def __init__(self):
        super().__init__()

    def _update_impl(self, delta_time: float):
        # Copy animation logic (Phase‑5)
        pass


# ---------------------------------------------------------
# DELETE SCENE
# ---------------------------------------------------------

class DeleteScene(BaseScene):
    """Animation for deleting (shredder)."""

    def __init__(self):
        super().__init__()

    def _update_impl(self, delta_time: float):
        # Shredding animation logic (Phase‑5)
        pass


# ---------------------------------------------------------
# CREATE FOLDER SCENE
# ---------------------------------------------------------

class CreateFolderScene(BaseScene):
    """Animation for creating a folder."""

    def __init__(self):
        super().__init__()

    def _update_impl(self, delta_time: float):
        # Folder creation animation logic (Phase‑5)
        pass
