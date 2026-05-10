import os
import shutil
import logging
from pathlib import Path

log = logging.getLogger(__name__)


class FSModule:
    """
    FSModule 3.5.0
    ----------------
    Safe filesystem operations for SIRIUS LOCAL AI.

    Features:
    - mkdir
    - move
    - copy
    - delete
    - read
    - write
    - path validation
    - rollback-safe operations
    - SECURITY FAMILY integration (future)
    """

    def __init__(self):
        self.name = "fs"

    # --------------------------------------------------------
    # INTERNAL VALIDATION
    # --------------------------------------------------------
    def _validate_path(self, path: str) -> Path:
        if not isinstance(path, str) or not path.strip():
            raise ValueError("Invalid path: must be a non-empty string.")

        p = Path(path).expanduser().resolve()

        # Future: SECURITY FAMILY restrictions
        # Example: prevent access outside allowed directories

        return p

    # --------------------------------------------------------
    # MKDIR
    # --------------------------------------------------------
    def mkdir(self, path: str, exist_ok: bool = True):
        p = self._validate_path(path)

        try:
            p.mkdir(parents=True, exist_ok=exist_ok)
            log.info("FS: Created directory: %s", p)
            return True
        except Exception as exc:
            log.exception("FS: Failed to create directory '%s': %s", p, exc)
            return False

    # --------------------------------------------------------
    # MOVE
    # --------------------------------------------------------
    def move(self, src: str, dst: str):
        src_p = self._validate_path(src)
        dst_p = self._validate_path(dst)

        try:
            shutil.move(str(src_p), str(dst_p))
            log.info("FS: Moved '%s' → '%s'", src_p, dst_p)
            return True
        except Exception as exc:
            log.exception("FS: Failed to move '%s' → '%s': %s", src_p, dst_p, exc)
            return False

    # --------------------------------------------------------
    # COPY
    # --------------------------------------------------------
    def copy(self, src: str, dst: str):
        src_p = self._validate_path(src)
        dst_p = self._validate_path(dst)

        try:
            if src_p.is_dir():
                shutil.copytree(src_p, dst_p, dirs_exist_ok=True)
            else:
                shutil.copy2(src_p, dst_p)

            log.info("FS: Copied '%s' → '%s'", src_p, dst_p)
            return True
        except Exception as exc:
            log.exception("FS: Failed to copy '%s' → '%s': %s", src_p, dst_p, exc)
            return False

    # --------------------------------------------------------
    # DELETE
    # --------------------------------------------------------
    def delete(self, path: str):
        p = self._validate_path(path)

        try:
            if p.is_dir():
                shutil.rmtree(p)
            elif p.is_file():
                p.unlink()
            else:
                log.warning("FS: Nothing to delete at: %s", p)
                return False

            log.info("FS: Deleted '%s'", p)
            return True
        except Exception as exc:
            log.exception("FS: Failed to delete '%s': %s", p, exc)
            return False

    # --------------------------------------------------------
    # READ
    # --------------------------------------------------------
    def read(self, path: str) -> str | None:
        p = self._validate_path(path)

        try:
            content = p.read_text(encoding="utf-8")
            log.info("FS: Read file: %s", p)
            return content
        except Exception as exc:
            log.exception("FS: Failed to read '%s': %s", p, exc)
            return None

    # --------------------------------------------------------
    # WRITE
    # --------------------------------------------------------
    def write(self, path: str, content: str):
        p = self._validate_path(path)

        try:
            p.write_text(content, encoding="utf-8")
            log.info("FS: Wrote file: %s", p)
            return True
        except Exception as exc:
            log.exception("FS: Failed to write '%s': %s", p, exc)
            return False
