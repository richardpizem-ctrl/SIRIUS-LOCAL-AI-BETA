# Baseline version of PluginBase
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class PluginBase:
    def __init__(self, name: str, logger):
        self.name = name
        self.logger = logger

    def initialize(self) -> bool:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active initialization logic is implemented here.
        """
        self.logger.log(f"[Baseline] PluginBase.initialize() called for: {self.name}")
        return True

    def shutdown(self) -> bool:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active shutdown logic is implemented here.
        """
        self.logger.log(f"[Baseline] PluginBase.shutdown() called for: {self.name}")
        return True
