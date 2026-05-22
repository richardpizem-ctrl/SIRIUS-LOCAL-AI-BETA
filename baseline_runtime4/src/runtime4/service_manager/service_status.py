# Baseline version of ServiceStatus
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class ServiceStatus:
    def __init__(self, name: str, running: bool, details: dict | None = None):
        self.name = name
        self.running = running
        self.details = details or {}

    def to_dict(self) -> dict:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active status formatting logic is implemented here.
        """
        return {
            "name": self.name,
            "running": self.running,
            "details": self.details
        }
