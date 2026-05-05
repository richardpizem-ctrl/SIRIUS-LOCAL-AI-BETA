# metadata_builder.py
# Automatic Input Triage Engine – MetadataBuilder
# SIRIUS-LOCAL-AI-ALFA v2.0.0

import os
import time
from typing import Dict, Any, Optional


class MetadataBuilder:
    """
    MetadataBuilder 2.0
    - builds metadata for input files
    - used in AITEController.process()
    """

    def build(self, input_path: str, input_type: str) -> Dict[str, Any]:
        """
        Build metadata for the given input.
        """
        if not input_path or not isinstance(input_path, str):
            return {
                "error": "Invalid input path",
                "type": input_type,
            }

        filename = os.path.basename(input_path)
        ext = os.path.splitext(filename)[1].lower()

        # Base metadata
        meta: Dict[str, Any] = {
            "filename": filename,
            "extension": ext,
            "type": input_type,
            "timestamp": int(time.time()),
        }

        # Extended metadata – file size
        meta["size_bytes"] = self._safe_file_size(input_path)

        # Type-specific category
        meta["category"] = self._resolve_category(input_type)

        return meta

    # ---------------- internal helpers ----------------

    def _safe_file_size(self, path: str) -> Optional[int]:
        try:
            return os.stat(path).st_size
        except Exception:
            return None

    def _resolve_category(self, input_type: str) -> str:
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
