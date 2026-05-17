# input_router.py
# Automatic Input Triage Engine – InputRouter 4.3.x
# SIRIUS LOCAL AI – deterministic, offline-only routing engine

from typing import Dict


class InputRouter:
    """
    InputRouter 4.3.x

    Responsibilities:
        - Deterministic mapping of input types to storage directories
        - Safe fallback routing for unknown types
        - Dynamic route overrides (Phase‑4)
        - Restricted-path detection (Phase‑4)
        - Sandbox & quarantine routing hooks
        - Safe‑mode and degraded‑mode compatible

    Used by:
        AITEController.process()
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

        # Base routing table (type → target directory)
        self.routes: Dict[str, str] = {
            "log": "storage/logs/",
            "config": "storage/config/",
            "project": "storage/projects/",
            "audio": "storage/audio/",
            "midi": "storage/midi/",
            "image": "storage/images/",
            "video": "storage/video/",
            "text": "storage/text/",
            "binary": "storage/bin/",
            "unknown": "storage/unknown/",
        }

        # Phase‑4 restricted directories
        self.restricted_paths = {
            "storage/system/",
            "storage/runtime/",
            "storage/security/",
        }

        # Phase‑4 quarantine directory
        self.quarantine_path = "storage/quarantine/"

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def route(self, input_type: str) -> str:
        """
        Return the target directory for the given input type.
        Deterministic, safe-mode aware, degraded-mode safe.
        """

        if self.safe_mode:
            return "storage/unknown/"

        try:
            # Normal routing
            target = self.routes.get(input_type, "storage/unknown/")

            # Restricted-path protection
            if self._is_restricted(target):
                return self.quarantine_path

            return target

        except Exception:
            self.degraded_mode = True
            return "storage/unknown/"

    def override_route(self, input_type: str, new_path: str) -> None:
        """
        Dynamically override a route at runtime.
        Useful for:
            - user-defined routing rules
            - plugin-based routing
            - experimental pipelines
        """

        if self.safe_mode:
            return

        if not isinstance(input_type, str):
            raise TypeError("input_type must be a string")

        if not isinstance(new_path, str):
            raise TypeError("new_path must be a string")

        if new_path.strip() == "":
            raise ValueError("new_path cannot be empty")

        # Normalize path
        new_path = new_path.rstrip("/") + "/"

        # Restricted-path protection
        if self._is_restricted(new_path):
            raise ValueError("Cannot override route to a restricted directory")

        self.routes[input_type] = new_path

    def reset_routes(self) -> None:
        """Reset routing table to default values."""
        self.__init__()

    def get_all_routes(self) -> Dict[str, str]:
        """Return a copy of the routing table."""
        return dict(self.routes)

    # ---------------------------------------------------------
    # Phase‑4 Security Hooks
    # ---------------------------------------------------------

    def _is_restricted(self, path: str) -> bool:
        """
        Detect restricted directories (sandbox isolation).
        """
        for restricted in self.restricted_paths:
            if path.startswith(restricted):
                return True
        return False

    def quarantine(self, input_type: str) -> str:
        """
        Explicit quarantine routing (Phase‑4).
        """
        return self.quarantine_path
