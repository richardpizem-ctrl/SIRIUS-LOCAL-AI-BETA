# Baseline version of HealthMonitor
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class HealthMonitor:
    def __init__(self, logger):
        self.logger = logger

    def check(self) -> bool:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active health-check logic is implemented here.
        """
        self.logger.log("[Baseline] HealthMonitor.check() called.")
        return True
