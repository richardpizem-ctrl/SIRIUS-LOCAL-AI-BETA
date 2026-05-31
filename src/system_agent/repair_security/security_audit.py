"""
SIRIUS Runtime 5.1.0 – System Agent Security
Security Audit 1.0
"""

from datetime import datetime


class SecurityAudit:
    """
    Audit bezpečnostných udalostí pre Self‑Repair a System Agent.
    """

    def __init__(self, logger):
        self.logger = logger
        self.events = []

    def record(self, event_type: str, details: dict):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": event_type,
            "details": details,
        }
        self.events.append(entry)

        self.logger.info(
            "SecurityAudit: event recorded",
            extra={"event_type": event_type, "details": details},
        )

    def get_events(self):
        return list(self.events)

    def clear(self):
        self.events = []
        self.logger.info("SecurityAudit: audit log cleared")
