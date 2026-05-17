import os
import json


class EmailProfileManager:
    """
    EmailProfileManager 4.3
    Handles creation, loading, listing, and deletion of
    email sender profiles for SIRIUS LOCAL AI.

    Improvements in 4.3:
    - deterministic Runtime4 behavior
    - strict validation of profile names
    - safe file operations with error handling
    - consistent return structure for EmailManager and commands
    - Self‑Repair 4.4 compatible
    """

    VALID_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"

    def __init__(self, base_path="email_profiles"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    # ---------------------------------------------------------
    # PATH HELPERS
    # ---------------------------------------------------------
    def _path(self, name: str):
        return os.path.join(self.base_path, f"{name}.json")

    def _exists(self, name: str):
        return os.path.isfile(self._path(name))

    def _valid_name(self, name: str):
        return (
            isinstance(name, str)
            and len(name) > 0
            and all(c in self.VALID_CHARS for c in name)
        )

    # ---------------------------------------------------------
    # SAVE PROFILE
    # ---------------------------------------------------------
    def save_profile(self, name: str, profile: dict):
        """
        Saves a profile to disk.
        Returns True on success, False on failure.
        """
        if not self._valid_name(name):
            return False

        try:
            with open(self._path(name), "w", encoding="utf-8") as f:
                json.dump(profile, f, indent=2, ensure_ascii=False)
        except Exception:
            return False

        return True

    # ---------------------------------------------------------
    # LOAD PROFILE
    # ---------------------------------------------------------
    def load_profile(self, name: str):
        """
        Loads a profile by name.
        Returns dict on success, None on failure.
        """
        if not self._exists(name):
            return None

        try:
            with open(self._path(name), "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    # ---------------------------------------------------------
    # LIST PROFILES
    # ---------------------------------------------------------
    def list_profiles(self):
        """
        Returns a sorted list of all profile names.
        """
        try:
            files = os.listdir(self.base_path)
        except Exception:
            return []

        profiles = [
            f.replace(".json", "")
            for f in files
            if f.endswith(".json")
        ]

        return sorted(profiles)

    # ---------------------------------------------------------
    # DELETE PROFILE
    # ---------------------------------------------------------
    def delete_profile(self, name: str):
        """
        Deletes a profile by name.
        Returns True on success, False on failure.
        """
        if not self._exists(name):
            return False

        try:
            os.remove(self._path(name))
        except Exception:
            return False

        return True
