# SIRIUS COLNIK-6.x — Detection Module (PRE-FINAL)
# This module detects anomalies, invalid operations, and rule violations.

class Detection:
    def __init__(self):
        self.last_event = None

    def record_event(self, event: str):
        """Record the last detected event."""
        self.last_event = event
        return f"[DETECTION] Event recorded: {event}"

    # --- ORIGINAL METHODS ---
    def detect_anomaly(self, data):
        """Placeholder for anomaly detection logic."""
        return "[DETECTION] Anomaly detection not implemented yet."

    def detect_violation(self, rule_name: str):
        """Placeholder for rule violation detection."""
        return f"[DETECTION] Violation check for '{rule_name}' not implemented yet."

    # --- COMPATIBILITY METHODS (used by tests & decision_engine) ---
    def check_anomaly(self, data):
        """Alias for detect_anomaly (compatibility layer)."""
        return self.detect_anomaly(data)

    def check_violation(self, data):
        """Alias for detect_violation (compatibility layer)."""
        rule = data.get("action", "UNKNOWN")
        return self.detect_violation(rule)
