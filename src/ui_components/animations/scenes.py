class BaseScene:
    """Base scene – all animations will inherit from this."""
    def __init__(self):
        self.objects = []  # list of graphical objects in the scene
        self.active = False

    def start(self):
        """Start the scene."""
        self.active = True

    def stop(self):
        """Stop the scene."""
        self.active = False

    def update(self, delta_time: float):
        """Scene update – implemented in subclasses."""
        pass


class MoveScene(BaseScene):
    """Animation for moving files (postman)."""
    def __init__(self):
        super().__init__()

    def update(self, delta_time: float):
        pass  # movement logic will go here


class CopyScene(BaseScene):
    """Animation for copying (copy machine)."""
    def __init__(self):
        super().__init__()

    def update(self, delta_time: float):
        pass  # copy animation logic will go here


class DeleteScene(BaseScene):
    """Animation for deleting (shredder)."""
    def __init__(self):
        super().__init__()

    def update(self, delta_time: float):
        pass  # shredding animation logic will go here


class CreateFolderScene(BaseScene):
    """Animation for creating a folder."""
    def __init__(self):
        super().__init__()

    def update(self, delta_time: float):
        pass  # folder creation animation logic will go here
