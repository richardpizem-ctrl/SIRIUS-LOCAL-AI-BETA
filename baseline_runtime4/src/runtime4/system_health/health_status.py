# Baseline version of HealthStatus
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class HealthStatus:
    def __init__(self, ok: bool, details: dict | None = None):
        self.ok = ok
        self.details = details or {}

    def summarize(self) -> dict:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active summarization logic is implemented here.
        """
        return {
            "ok": self.ok,
            "details": self.details
        }
