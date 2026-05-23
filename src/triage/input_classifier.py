# input_classifier_4_5.py
# SIRIUS LOCAL AI – InputClassifier 4.5.0 PRO
# Deterministic, offline-only classifier with Phase‑5 security hooks.

from typing import Literal


InputType45 = Literal[
    "log",
    "config",
    "project",
    "audio",
    "midi",
    "image",
    "video",
    "text",
    "binary",
    "document",
    "archive",
    "unknown",
]


class InputClassifier45:
    """
    InputClassifier 4.5.0 PRO

    Responsibilities:
        - Deterministic input type detection based on file extension and path patterns
        - Forbidden extension detection (Phase‑4/5)
        - Sandbox & quarantine hooks (Phase‑5 ready)
        - Safe fallback classification
        - Safe‑mode and degraded‑mode compatible
        - Offline-only behavior

    Used by:
        AITEController45.process()
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

        # Phase‑4/5 forbidden extensions (expanded)
        self.forbidden_ext = {
            ".bat", ".cmd", ".sh", ".ps1", ".vbs", ".js", ".jar",
            ".scr", ".pif", ".msi", ".msix", ".apk", ".ipa",
            ".reg", ".gadget", ".com", ".cpl", ".hta",
        }

        # Document formats (4.5)
        self.document_ext = {
            ".pdf", ".doc", ".docx", ".odt", ".rtf"
        }

        # Archive formats (4.5)
        self.archive_ext = {
            ".zip", ".rar", ".7z", ".tar", ".gz"
        }

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def classify(self, input_path: str) -> InputType45:
        """
        Determine the input type based on file extension and known patterns.
        Deterministic, offline-only, safe-mode aware.
        """

        if self.safe_mode:
            return "unknown"

        try:
            if not input_path or not isinstance(input_path, str):
                return "unknown"

            lower = input_path.lower().strip()

            # Forbidden extension check (Phase‑4/5)
            if self._is_forbidden(lower):
                return "binary"

            # LOG FILES
            if lower.endswith(".log") or "/logs/" in lower or "\\logs\\" in lower:
                return "log"

            # CONFIG FILES
            if lower.endswith((".ini", ".cfg", ".conf", ".yaml", ".yml", ".json")):
                return "config"

            # PROJECT ROOTS
            if lower.endswith((
                ".sln", ".csproj", ".vcxproj", ".pyproj",
                "package.json", "pyproject.toml",
            )):
                return "project"

            # DOCUMENTS (4.5)
            if lower.endswith(tuple(self.document_ext)):
                return "document"

            # ARCHIVES (4.5)
            if lower.endswith(tuple(self.archive_ext)):
                return "archive"

            # AUDIO
            if lower.endswith((".wav", ".mp3", ".flac", ".ogg", ".aiff")):
                return "audio"

            # MIDI
            if lower.endswith((".mid", ".midi")):
                return "midi"

            # IMAGE
            if lower.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp")):
                return "image"

            # VIDEO
            if lower.endswith((".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm")):
                return "video"

            # TEXT / CODE
            if lower.endswith((
                ".txt", ".md", ".rst",
                ".py", ".cs", ".cpp", ".h", ".hpp",
                ".js", ".ts", ".html", ".css",
            )):
                return "text"

            # BINARY
            if lower.endswith((".exe", ".dll", ".so", ".bin", ".dat")):
                return "binary"

            return "unknown"

        except Exception:
            self.degraded_mode = True
            return "unknown"

    # ---------------------------------------------------------
    # Phase‑4/5 Security Hooks
    # ---------------------------------------------------------

    def _is_forbidden(self, lower: str) -> bool:
        """Detect forbidden extensions (sandbox, quarantine rules)."""
        for ext in self.forbidden_ext:
            if lower.endswith(ext):
                return True
        return False

    def is_potentially_harmful(self, input_path: str) -> bool:
        """
        Placeholder for malware heuristics (Phase‑5).
        Deterministic stub.
        """
        return False
