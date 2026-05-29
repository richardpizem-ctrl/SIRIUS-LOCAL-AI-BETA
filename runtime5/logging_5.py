# runtime5/logging_5.py

import datetime
import threading


class Logger5:
    """
    Thread‑safe diagnostic logger for Runtime 5.x.
    Provides:
    - INFO / WARN / ERROR / DEBUG levels
    - safe printing (never crashes)
    - timestamped output
    - Self‑Repair Layer compatibility
    """

    _lock = threading.Lock()

    @staticmethod
    def _timestamp():
        try:
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return "0000-00-00 00:00:00"

    @classmethod
    def _safe_print(cls, level: str, message: str):
        with cls._lock:
            try:
                msg = str(message)
            except Exception:
                msg = "<invalid log message>"

            if len(msg) > 5000:
                msg = msg[:5000] + "... [truncated]"

            try:
                print(f"[RUNTIME5 {cls._timestamp()}] [{level}] {msg}")
            except Exception:
                pass  # fail‑safe

    @classmethod
    def info(cls, message: str):
        cls._safe_print("INFO", message)

    @classmethod
    def warn(cls, message: str):
        cls._safe_print("WARN", message)

    @classmethod
    def error(cls, message: str):
        cls._safe_print("ERROR", message)

    @classmethod
    def debug(cls, message: str):
        cls._safe_print("DEBUG", message)


# --------------------------------------------------------
# PUBLIC API
# --------------------------------------------------------

def log5(message: str, level: str = "INFO"):
    """
    Unified logging entry point for Runtime 5.x.
    """
    if level == "INFO":
        Logger5.info(message)
    elif level == "WARN":
        Logger5.warn(message)
    elif level == "ERROR":
        Logger5.error(message)
    elif level == "DEBUG":
        Logger5.debug(message)
    else:
        Logger5.info(message)
