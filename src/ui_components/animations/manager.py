from .animation_scenes import (
    MoveScene,
    CopyScene,
    DeleteScene,
    CreateFolderScene
)


class AnimationManager:
    """Animation controller – switches scenes based on operation type."""

    def __init__(self):
        self.current_scene = None

        # Preloaded scenes
        self.scenes = {
            "move": MoveScene(),
            "copy": CopyScene(),
            "delete": DeleteScene(),
            "create_folder": CreateFolderScene()
        }

    def play(self, scene_name: str):
        """Start the requested scene by name."""
        if self.current_scene:
            self.current_scene.stop()

        scene = self.scenes.get(scene_name)
        if scene:
            self.current_scene = scene
            self.current_scene.start()

    def update(self, delta_time: float):
        """Update the active scene."""
        if self.current_scene and self.current_scene.active:
            self.current_scene.update(delta_time)
