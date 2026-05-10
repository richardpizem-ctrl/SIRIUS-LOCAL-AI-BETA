import subprocess
import logging
from pathlib import Path

log = logging.getLogger(__name__)


class EditorModule:
    """
    EditorModule 3.5.0
    -------------------
    Safe interface for opening files and folders in VS Code.

    Features:
    - open_file(path)
    - open_folder(path)
    - open_at_line(path, line)
    - highlight(path, line)
    """

    def __init__(self):
        self.name = "editor"
        self.vscode_cmd = "code"  # assumes VS Code is in PATH

    # --------------------------------------------------------
    # INTERNAL VALIDATION
    # --------------------------------------------------------
    def _validate_path(self, path: str) -> Path:
        if not isinstance(path, str) or not path.strip():
            raise ValueError("Invalid path: must be a non-empty string.")

        p = Path(path).expanduser().resolve()
        return p

    # --------------------------------------------------------
    # OPEN FILE
    # --------------------------------------------------------
    def open_file(self, path: str):
        p = self._validate_path(path)

        try:
            subprocess.Popen([self.vscode_cmd, str(p)])
            log.info("EDITOR: Opened file in VS Code: %s", p)
            return True
        except Exception as exc:
            log.exception("EDITOR: Failed to open file '%s': %s", p, exc)
            return False

    # --------------------------------------------------------
    # OPEN FOLDER
    # --------------------------------------------------------
    def open_folder(self, path: str):
        p = self._validate_path(path)

        try:
            subprocess.Popen([self.vscode_cmd, str(p)])
            log.info("EDITOR: Opened folder in VS Code: %s", p)
            return True
        except Exception as exc:
            log.exception("EDITOR: Failed to open folder '%s': %s", p, exc)
            return False

    # --------------------------------------------------------
    # OPEN FILE AT LINE
    # --------------------------------------------------------
    def open_at_line(self, path: str, line: int):
        p = self._validate_path(path)

        try:
            subprocess.Popen([self.vscode_cmd, "-g", f"{p}:{line}"])
            log.info("EDITOR: Opened file at line %s: %s", line, p)
            return True
        except Exception as exc:
            log.exception("EDITOR: Failed to open '%s' at line %s: %s", p, line, exc)
            return False

    # --------------------------------------------------------
    # HIGHLIGHT (alias for open_at_line)
    # --------------------------------------------------------
    def highlight(self, path: str, line: int):
        return self.open_at_line(path, line)
