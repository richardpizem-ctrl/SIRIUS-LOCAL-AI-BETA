import datetime
import os


class WorkflowLogger:
    """
    Simple workflow logger (mock).
    Writes text logs into workflow.log.
    Will be replaced by a UI log panel later.
    """

    def __init__(self, log_file: str = "workflow.log"):
        self.log_file = log_file
        self._ensure_log_file()

    def _ensure_log_file(self):
        """
        Create an empty log file if it does not exist.
        """
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", encoding="utf-8") as f:
                f.write("=== SIRIUS WORKFLOW LOG ===\n")

    def _write(self, level: str, message: str):
        """
        Write a log entry into the log file.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] [{level}] {message}\n"

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(line)

    def info(self, message: str):
        self._write("INFO", message)

    def warning(self, message: str):
        self._write("WARNING", message)

    def error(self, message: str):
        self._write("ERROR", message)
