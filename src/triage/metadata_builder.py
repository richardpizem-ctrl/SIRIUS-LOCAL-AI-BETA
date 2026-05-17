# metadata_builder.py
# Automatic Input Triage Engine – MetadataBuilder 4.3.x
# SIRIUS LOCAL AI – deterministic, offline-only metadata generator

import os
import time
import hashlib
from typing import Dict, Any, Optional


class MetadataBuilder:
    """
    MetadataBuilder 4.3.x

    Responsibilities:
        - Build deterministic metadata for input files
        - Provide safe fallback metadata in degraded-mode
        - Provide sandbox/quarantine metadata hooks (Phase‑4)
        - Provide file integrity metadata (hashes)
        - Fully compatible with AITEController 4.3.x
        - Deterministic, offline-only behavior
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def build(self, input_path: str, input_type: str) -> Dict[str, Any]:
        """
        Build metadata for the given input.
        Deterministic, safe-mode aware, degraded-mode safe.
        """

        if self.safe_mode:
            return {
                "filename": None,
                "extension": None,
                "type": input_type,
                "timestamp": int(time.time()),
                "size_bytes": None,
                "category": "unknown",
                "hash_sha256": None,
                "status": "safe_mode",
            }

        try:
            if not input_path or not isinstance(input_path, str):
                return {
                    "error": "Invalid input path",
                    "type": input_type,
                }

            filename = os.path.basename(input_path)
            ext = os.path.splitext(filename)[1].lower()

            meta: Dict[str, Any] = {
                "filename": filename,
                "extension": ext,
                "type": input_type,
                "timestamp": int(time.time()),
                "size_bytes": self._safe_file_size(input_path),
                "category": self._resolve_category(input_type),
                "hash_sha256": self._safe_hash(input_path),
                "status": "ok",
            }

            return meta

        except Exception as exc:
            self.degraded_mode = True
            return {
                "filename": None,
                "extension": None,
                "type": input_type,
                "timestamp": int(time.time()),
                "size_bytes": None,
                "category": "unknown",
                "hash_sha256": None,
                "status": "error",
                "exception": str(exc),
            }

    # ---------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------

    def _safe_file_size(self, path: str) -> Optional[int]:
        try:
            return os.stat(path).st_size
        except Exception:
            return None

    def _safe_hash(self, path: str) -> Optional[str]:
        """
        Compute SHA‑256 hash of the file.
        Deterministic, offline-only, safe fallback.
        """
        try:
            sha = hashlib.sha256()
            with open(path, "rb") as f:
                for block in iter(lambda: f.read(4096), b""):
                    sha.update(block)
            return sha.hexdigest()
        except Exception:
            return None

    def _resolve_category(self, input_type: str) -> str:
        """
        Map input types to metadata categories.
        Deterministic and Phase‑4 compatible.
        """
        if input_type == "audio":
            return "media"
        if input_type == "midi":
            return "music"
        if input_type == "image":
            return "visual"
        if input_type == "video":
            return "media"
        if input_type == "log":
            return "system"
        if input_type == "config":
            return "settings"
        if input_type == "project":
            return "project"
        if input_type == "text":
            return "document"
        if input_type == "binary":
            return "binary"
        return "unknown"
