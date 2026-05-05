# metadata_builder.py
# Automatic Input Triage Engine – MetadataBuilder
# SIRIUS LOCAL AI – v2.1.0 (Extended English Version)

import os
import time
from typing import Dict, Any, Optional


class MetadataBuilder:
    """
    MetadataBuilder 2.1 (Extended)

    Responsibilities:
        - Generate metadata for input files
        - Provide type-specific metadata categories
        - Safely extract file statistics
        - Prepare metadata for FS-AGENT operations

    Used by:
        AITEController.process()
    """

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def build(self, input_path: str, input_type: str) -> Dict[str, Any]:
        """
        Build metadata for the given input file.

        Returns:
            A dictionary containing:
                - filename
                - extension
                - type
                - timestamp
                - size_bytes (if available)
                - category (type-specific)
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

        # File size (safe)
        meta["size_bytes"] = self._safe_file_size(input_path)

        # Type-specific category
        meta["category"] = self._resolve_category(input_type)

        # Future expansion hooks (Phase 5)
        meta["is_executable"] = self._is_executable(ext)
        meta["is_potentially_harmful"] = self._is_potentially_harmful(ext)

        return meta

    # ---------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------

    def _safe_file_size(self, path: str) -> Optional[int]:
        """
        Safely return file size in bytes.
        Returns None if the file cannot be accessed.
        """
        try:
            return os.stat(path).st_size
        except Exception:
            return None

    def _resolve_category(self, input_type: str) -> str:
        """
        Map input types to metadata categories.
        """
        mapping = {
            "audio": "media",
            "midi": "music",
            "image": "visual",
            "video": "media",
            "log": "system",
            "config": "settings",
            "project": "project",
            "text": "document",
            "binary": "binary",
            "unknown": "unknown",
        }
        return mapping.get(input_type, "unknown")

    # ---------------------------------------------------------
    # Future expansion hooks (Phase 5)
    # ---------------------------------------------------------

    def _is_executable(self, ext: str) -> bool:
        """
        Detect if the file extension represents an executable.
        Used for sandbox/quarantine logic in future versions.
        """
        return ext in (".exe", ".dll", ".so", ".bin")

    def _is_potentially_harmful(self, ext: str) -> bool:
        """
        Placeholder for malware heuristics.
        Currently returns False, but reserved for Architecture 4.0.
        """
        return False
