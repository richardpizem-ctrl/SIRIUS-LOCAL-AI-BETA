# Baseline version of ServiceManager
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class ServiceManager:
    def __init__(self, registry, logger):
        self.registry = registry
        self.logger = logger

    def start(self, name: str) -> bool:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active service start logic is implemented here.
        """
        self.logger.log(f"[Baseline] ServiceManager.start() called for: {name}")
        return True

    def stop(self, name: str) -> bool:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active service stop logic is implemented here.
        """
        self.logger.log(f"[Baseline] ServiceManager.stop() called for: {name}")
        return True
