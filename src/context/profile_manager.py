import copy
import os
import json
import re


class ProfileManager:
    """
    ProfileManager 4.4
    Handles saving, loading, listing, deleting, and inspecting
    context profiles for SIRIUS LOCAL AI.

    New in 4.4:
        - Deterministic behavior for Runtime4.4
        - Strict filename validation (stable, audit‑friendly)
        - Deep‑copy safety for all operations
        - Snapshot‑compatible structure
        - max_history enforcement
        - Stable, predictable structure for commands and Self‑Repair 4.4
    """

    VALID_NAME = re.compile(r"^[A-Za-z0-9_\-]+$")

    def __init__(self, context_manager, base_path: str = "profiles"):
        self.context = context_manager
        self.base_path = base_path

        # No side effects beyond required fs init
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    # ============================================================
    #  INTERNAL HELPERS
    # ============================================================

    def _profile_path(self, name: str) -> str:
        return os.path.join(self.base_path, f"{name}.json")

    def _exists(self, name: str) -> bool:
        return os.path.isfile(self._profile_path(name))

    def _validate_name(self, name: str) -> bool:
        return bool(self.VALID_NAME.match(name))

    # ============================================================
    #  SAVE PROFILE
    # ============================================================

    def save_profile(self, name: str) -> bool:
        """
        Save the current context into a profile file.
        Deterministic, deep‑copy safe.
        """
        if not self._validate_name(name):
            return False

        data = {
            "session": copy.deepcopy(self.context.session_memory),
            "persistent": copy.deepcopy(self.context.persistent_memory),
            "state": copy.deepcopy(self.context.state),
            "history": copy.deepcopy(self.context.history),
        }

        try:
            with open(self._profile_path(name), "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception:
            return False

        return True

    # ============================================================
    #  LOAD PROFILE
    # ============================================================

    def load_profile(self, name: str):
        """
        Load a profile and restore the context.
        Returns True on success, None on failure.
        """
        if not self._exists(name):
            return None

        try:
            with open(self._profile_path(name), "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            return None

        # Validate structure
        if not isinstance(data, dict):
            return None

        session = data.get("session", [])
        persistent = data.get("persistent", {})
        state = data.get("state", {})
        history = data.get("history", [])

        if not isinstance(session, list):
            return None
        if not isinstance(persistent, dict):
            return None
        if not isinstance(state, dict):
            return None
        if not isinstance(history, list):
            return None

        # Restore context (deep copy)
        self.context.session_memory = copy.deepcopy(session)
        self.context.persistent_memory = copy.deepcopy(persistent)
        self.context.state = copy.deepcopy(state)

        # Enforce max_history deterministically
        self.context.history = copy.deepcopy(
            history[-self.context.max_history :]
        )

        return True

    # ============================================================
    #  LIST PROFILES
    # ============================================================

    def list_profiles(self):
        """
        Return a sorted list of all saved profile names.
        Deterministic ordering.
        """
        try:
            files = os.listdir(self.base_path)
        except Exception:
            return []

        profiles = [
            f[:-5] for f in files
            if f.endswith(".json")
        ]
        return sorted(profiles)

    # ============================================================
    #  DELETE PROFILE
    # ============================================================

    def delete_profile(self, name: str) -> bool:
        """
        Delete a profile file.
        Returns True on success, False on failure.
        """
        if not self._exists(name):
            return False

        try:
            os.remove(self._profile_path(name))
        except Exception:
            return False

        return True

    # ============================================================
    #  PROFILE INFO
    # ============================================================

    def get_profile_info(self, name: str):
        """
        Return metadata about a profile.
        Returns dict on success, None on failure.
        """
        if not self._exists(name):
            return None

        try:
            with open(self._profile_path(name), "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            return None

        return {
            "session_items": len(data.get("session", [])),
            "persistent_items": len(data.get("persistent", {})),
            "state_items": len(data.get("state", {})),
            "history_snapshots": len(data.get("history", [])),
        }
