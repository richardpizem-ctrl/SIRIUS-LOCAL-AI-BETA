# Baseline version of ServiceRegistry
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class ServiceRegistry:
    def __init__(self, logger):
        self.logger = logger
        self.services = {}

    def register(self, name: str, service) -> None:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active registration logic is implemented here.
        """
        self.logger.log(f"[Baseline] ServiceRegistry.register() called for: {name}")
        self.services[name] = service

    def get(self, name: str):
        """
        Baseline version:
        Always returns None.
        """
        self.logger.log(f"[Baseline] ServiceRegistry.get() called for: {name}")
        return None
