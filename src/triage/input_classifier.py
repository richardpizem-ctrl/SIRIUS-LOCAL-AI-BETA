# input_classifier.py
# Automatic Input Triage Engine – InputClassifier
# SIRIUS LOCAL AI – v2.1.0 (Extended English Version)

from typing import Literal


InputType = Literal[
    "log",
    "config",
    "project",
    "audio",
    "midi",
    "image",
    "video",
    "text",
    "binary",
    "unknown",
]


class InputClassifier:
    """
    InputClassifier 2.1 (Extended)

    Responsibilities:
        - Deterministic input type detection based on file extension and path patterns
        - Safe fallback classification
        - Expandable rule set for future phases (sandbox, quarantine, forbidden extensions)

    Used by:
        AITEController.process()
    """

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def classify(self, input_path: str) -> InputType:
        """
        Determine the input type based on file extension and known patterns.

        Returns:
            One of InputType literals.
        """

        if not input_path or not isinstance(input_path, str):
            return "unknown"

        lower = input_path.lower().strip()

        # ---------------------------------------------------------
        # LOG FILES
        # ---------------------------------------------------------
        if lower.endswith(".log") or "/logs/" in lower or "\\logs\\" in lower:
            return "log"

        # ---------------------------------------------------------
        # CONFIG FILES
        # ---------------------------------------------------------
        if lower.endswith((".ini", ".cfg", ".conf", ".yaml", ".yml", ".json")):
            return "config"

        # ---------------------------------------------------------
        # PROJECT ROOTS (FOLDERS / KNOWN PROJECT FILES)
        # ---------------------------------------------------------
        if lower.endswith((
            ".sln",
            ".csproj",
            ".vcxproj",
            ".pyproj",
            "package.json",
            "pyproject.toml",
        )):
            return "project"

        # ---------------------------------------------------------
        # AUDIO
        # ---------------------------------------------------------
        if lower.endswith((".wav", ".mp3", ".flac", ".ogg", ".aiff")):
            return "audio"

        # ---------------------------------------------------------
        # MIDI
        # ---------------------------------------------------------
        if lower.endswith((".mid", ".midi")):
            return "midi"

        # ---------------------------------------------------------
        # IMAGE
        # ---------------------------------------------------------
        if lower.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp")):
            return "image"

        # ---------------------------------------------------------
        # VIDEO
        # ---------------------------------------------------------
        if lower.endswith((".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm")):
            return "video"

        # ---------------------------------------------------------
        # TEXT / CODE
        # ---------------------------------------------------------
        if lower.endswith((
            ".txt",
            ".md",
            ".rst",
            ".py",
            ".cs",
            ".cpp",
            ".h",
            ".hpp",
            ".js",
            ".ts",
            ".html",
            ".css",
        )):
            return "text"

        # ---------------------------------------------------------
        # BINARY (fallback for known binary formats)
        # ---------------------------------------------------------
        if lower.endswith((".exe", ".dll", ".so", ".bin", ".dat")):
            return "binary"

        # ---------------------------------------------------------
        # UNKNOWN (default fallback)
        # ---------------------------------------------------------
        return "unknown"

    # ---------------------------------------------------------
    # Future expansion hooks (Phase 5)
    # ---------------------------------------------------------

    def is_forbidden_extension(self, input_path: str) -> bool:
        """
        Placeholder for future security rules:
            - quarantine rules
            - forbidden extensions
            - sandbox restrictions

        Currently unused, but reserved for Architecture 4.0.
        """
        return False

    def is_potentially_harmful(self, input_path: str) -> bool:
        """
        Placeholder for future malware heuristics.
        """
        return False
