# workflow/logger_4_5.py
# SIRIUS LOCAL AI – Workflow Logger 4.5.0 PRO
# Deterministic, safe-mode compatible logging subsystem (Phase‑4/5 ready)

import datetime
import os
from typing import Optional


class WorkflowLogger45:
    """
    WorkflowLogger 4.5.0 PRO

    Responsibilities:
        - Deterministic workflow logging
        - Safe-mode and degraded-mode behavior (Security Family 4.5)
        - Error-safe file writes
        - Structured log formatting
        - Offline-only, no side-effects outside log file
        - Self‑Repair 4.5 compatible
        - Phase‑5 ready (sandbox logging hooks)
    """

    def __init__(self, log_file: str = "workflow.log"):
        self.log_file = log_file
        self.safe_mode = False
        self.degraded_mode = False
        self._ensure_log_file()

    # ---------------------------------------------------------
    # File initialization
    # ---------------------------------------------------------

    def _ensure_log_file(self):
        """Create an empty log file if it does not exist."""
        try:
            if not os.path.exists(self.log_file):
                with open(self.log_file, "w", encoding="utf-8") as f:
                    f.write("=== SIRIUS WORKFLOW LOG (4.5.0 PRO) ===\n")
        except Exception:
            self.degraded_mode = True

    # ---------------------------------------------------------
    # Internal write
    # ---------------------------------------------------------

    def _write(self, level: str, message: str):
        """
        Write a log entry into the log file.
        Error-safe, deterministic, safe-mode aware.
        """

        if self.safe_mode:
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Sanitize message (Phase‑4)
        safe_message = str(message).replace("\n", " ").strip()

        line = f"[{timestamp}] [{level}] {safe_message}\n"

        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(line)
        except Exception:
            self.degraded_mode = True

    # ---------------------------------------------------------
    # Public logging API
    # ---------------------------------------------------------

    def info(self, message: str):
        self._write("INFO", message)

    def warning(self, message: str):
        self._write("WARNING", message)

    def error(self, message: str):
        self._write("ERROR", message)

    # ---------------------------------------------------------
    # Safe-mode
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False

    # ---------------------------------------------------------
    # Introspection
    # ---------------------------------------------------------

    def is_safe_mode(self) -> bool:
        return self.safe_mode

    def is_degraded_mode(self) -> bool:
        return self.degraded_mode
