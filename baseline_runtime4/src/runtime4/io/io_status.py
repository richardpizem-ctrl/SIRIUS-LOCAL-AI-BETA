# Baseline version of IOStatus
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class IOStatus:
    def __init__(self, last_sent: str | None = None, last_received: str | None = None):
        self.last_sent = last_sent
        self.last_received = last_received

    def to_dict(self) -> dict:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active status formatting logic is implemented here.
        """
        return {
            "last_sent": self.last_sent,
            "last_received": self.last_received
        }
