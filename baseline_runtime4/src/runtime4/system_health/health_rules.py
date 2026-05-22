# Baseline version of HealthRules
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class HealthRules:
    def __init__(self, logger):
        self.logger = logger

    def evaluate(self, metrics: dict) -> bool:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active rule evaluation logic is implemented here.
        """
        self.logger.log("[Baseline] HealthRules.evaluate() called.")
        return True
