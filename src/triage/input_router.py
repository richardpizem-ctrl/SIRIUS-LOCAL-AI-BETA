# input_router.py
# Automatic Input Triage Engine – InputRouter
# SIRIUS LOCAL AI – v2.1.0 (Extended English Version)

from typing import Dict


class InputRouter:
    """
    InputRouter 2.1 (Extended)

    Responsibilities:
        - Map input types to target storage directories
        - Provide deterministic routing for AITEController
        - Allow dynamic route overrides (Phase 4+)
        - Provide safety fallback for unknown types

    Used by:
        AITEController.process()
    """

    def __init__(self):
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

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def route(self, input_type: str) -> str:
        """
        Return the target directory for the given input type.

        Unknown types always fall back to:
            storage/unknown/
        """
        return self.routes.get(input_type, "storage/unknown/")

    def override_route(self, input_type: str, new_path: str) -> None:
        """
        Dynamically override a route at runtime.

        Example:
            router.override_route("audio", "storage/custom_audio/")

        This is useful for:
            - user-defined routing rules
            - plugin-based routing
            - experimental pipelines
        """
        if not isinstance(input_type, str):
            raise TypeError("input_type must be a string")

        if not isinstance(new_path, str):
            raise TypeError("new_path must be a string")

        if new_path.strip() == "":
            raise ValueError("new_path cannot be empty")

        self.routes[input_type] = new_path.rstrip("/") + "/"

    def reset_routes(self) -> None:
        """
        Reset routing table to default values.
        Useful for testing or sandbox mode.
        """
        self.__init__()

    def get_all_routes(self) -> Dict[str, str]:
        """
        Return a copy of the routing table.
        """
        return dict(self.routes)

    # ---------------------------------------------------------
    # Future expansion hooks (Phase 5)
    # ---------------------------------------------------------

    def is_restricted_path(self, path: str) -> bool:
        """
        Placeholder for future security rules:
            - restricted directories
            - sandbox isolation
            - quarantine routing

        Currently unused, reserved for Architecture 4.0.
        """
        return False
