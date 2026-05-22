# File: src/runtime4/self_repair/repair_log.py
"""
Repair Log
Version: 4.5.0
Component of: Self-Repair Layer (Phase‑5)

Responsible for:
- Recording integrity scans
- Logging repair actions
- Tracking fallback behavior
- Providing structured diagnostic history
"""

import os
import json
from datetime import datetime
from typing import Any, Dict


class RepairLog:
    """
    Lightweight structured logger for the Self‑Repair Layer.
    Stores logs in JSONL format for easy parsing.
    """

    def __init__(self, log_path="logs/self_repair.log"):
        self.log_path = log_path
        self._ensure_directory()

    def _ensure_directory(self):
        """Ensures that the log directory exists."""
        directory = os.path.dirname(self.log_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    def _write(self, entry: Dict[str, Any]):
        """Writes a single log entry as JSON."""
        entry["timestamp"] = datetime.utcnow().isoformat()
        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception:
            # Logging must never break runtime
            pass

    # ---------------------------------------------------------
    # PUBLIC LOGGING METHODS
    # ---------------------------------------------------------

    def record_scan(self, scan_result: Dict[str, Any]):
        """Logs the result of an integrity scan."""
        self._write({
            "event": "integrity_scan",
            "result": scan_result
        })

    def record_repair(self, repair_report: Dict[str, Any]):
        """Logs a repair action report."""
        self._write({
            "event": "repair_actions",
            "report": repair_report
        })

    def record_event(self, message: str):
        """Logs a generic event message."""
        self._write({
            "event": "runtime_event",
            "message": message
        })
