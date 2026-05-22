# Baseline version of RuntimeState
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class RuntimeState:
    def __init__(self):
        self.state = {}

    def set(self, key: str, value):
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active state logic is implemented here.
        """
        self.state[key] = value

    def get(self, key: str, default=None):
        """
        Baseline version:
        Returns default instead of performing real state operations.
        """
        return self.state.get(key, default)
