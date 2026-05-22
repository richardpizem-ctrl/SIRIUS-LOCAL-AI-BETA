# Runtime4 Runtime Context
# Baseline module
# Version: 4.5.0

class RuntimeContext:
    def __init__(self, config: dict | None = None):
        self.config = config or {}

    def get(self, key: str, default=None):
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active context logic is implemented here.
        """
        return self.config.get(key, default)
