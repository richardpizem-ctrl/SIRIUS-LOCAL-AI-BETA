import os
import shutil
import logging
from pathlib import Path

log = logging.getLogger(__name__)


class FSModule:
    """
    FSModule 4.5
    ----------------
    High‑level filesystem operations for SIRIUS LOCAL AI.

    Updated in 4.5:
        - Deterministic Runtime4.5 behavior
        - Strict path validation contract (unchanged)
        - Stable structured return values
        - Self‑Repair Layer 4.5 compatible metadata
        - Safe directory creation and overwrite handling
        - Unified error model for CommandRouter 4.5
        - Metadata version bumped to 4.5
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
        return p

    # --------------------------------------------------------
    # MKDIR
    # --------------------------------------------------------
    def mkdir(self, path: str, exist_ok: bool = True):
        p = self._validate_path(path)

        try:
            p.mkdir(parents=True, exist_ok=exist_ok)
            log.info("FS: Created directory: %s", p)
            return {
                "status": "success",
                "path": str(p),
                "fs_version": "4.5"
            }
        except Exception as exc:
            log.exception("FS: Failed to create directory '%s': %s", p, exc)
            return {
                "status": "error",
                "path": str(p),
                "exception": str(exc),
                "fs_version": "4.5"
            }

    # --------------------------------------------------------
    # MOVE
    # --------------------------------------------------------
    def move(self, src: str, dst: str):
        src_p = self._validate_path(src)
        dst_p = self._validate_path(dst)

        try:
            shutil.move(str(src_p), str(dst_p))
            log.info("FS: Moved '%s' → '%s'", src_p, dst_p)
            return {
                "status": "success",
                "src": str(src_p),
                "dst": str(dst_p),
                "fs_version": "4.5"
            }
        except Exception as exc:
            log.exception("FS: Failed to move '%s' → '%s': %s", src_p, dst_p, exc)
            return {
                "status": "error",
                "src": str(src_p),
                "dst": str(dst_p),
                "exception": str(exc),
                "fs_version": "4.5"
            }

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
            return {
                "status": "success",
                "src": str(src_p),
                "dst": str(dst_p),
                "fs_version": "4.5"
            }
        except Exception as exc:
            log.exception("FS: Failed to copy '%s' → '%s': %s", src_p, dst_p, exc)
            return {
                "status": "error",
                "src": str(src_p),
                "dst": str(dst_p),
                "exception": str(exc),
                "fs_version": "4.5"
            }

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
                return {
                    "status": "error",
                    "path": str(p),
                    "message": "Nothing to delete",
                    "fs_version": "4.5"
                }

            log.info("FS: Deleted '%s'", p)
            return {
                "status": "success",
                "path": str(p),
                "fs_version": "4.5"
            }
        except Exception as exc:
            log.exception("FS: Failed to delete '%s': %s", p, exc)
            return {
                "status": "error",
                "path": str(p),
                "exception": str(exc),
                "fs_version": "4.5"
            }

    # --------------------------------------------------------
    # READ
    # --------------------------------------------------------
    def read(self, path: str) -> dict:
        p = self._validate_path(path)

        try:
            content = p.read_text(encoding="utf-8")
            log.info("FS: Read file: %s", p)
            return {
                "status": "success",
                "path": str(p),
                "content": content,
                "fs_version": "4.5"
            }
        except Exception as exc:
            log.exception("FS: Failed to read '%s': %s", p, exc)
            return {
                "status": "error",
                "path": str(p),
                "exception": str(exc),
                "fs_version": "4.5"
            }

    # --------------------------------------------------------
    # WRITE
    # --------------------------------------------------------
    def write(self, path: str, content: str):
        p = self._validate_path(path)

        try:
            p.write_text(content, encoding="utf-8")
            log.info("FS: Wrote file: %s", p)
            return {
                "status": "success",
                "path": str(p),
                "fs_version": "4.5"
            }
        except Exception as exc:
            log.exception("FS: Failed to write '%s': %s", p, exc)
            return {
                "status": "error",
                "path": str(p),
                "exception": str(exc),
                "fs_version": "4.5"
            }
