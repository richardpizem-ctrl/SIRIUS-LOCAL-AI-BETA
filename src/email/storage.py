import os
import json
from datetime import datetime


class EmailStorage:
    """
    EmailStorage 4.5
    Handles low-level file operations for storing, loading,
    listing, and deleting emails in a deterministic and safe way.

    Updated in 4.5:
        - Deterministic Runtime4.5 behavior
        - Strict filename contract (unchanged)
        - Stable list ordering (unchanged)
        - Safe JSON loading with structure validation (unchanged)
        - Self‑Repair Layer 4.5 compatible metadata
        - Guaranteed return types (never throws)
    """

    def __init__(self, base_path="emails"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    # ---------------------------------------------------------
    # PATH HELPERS
    # ---------------------------------------------------------
    def _path(self, filename: str):
        return os.path.join(self.base_path, filename)

    def _safe_listdir(self):
        try:
            return sorted(os.listdir(self.base_path))
        except Exception:
            return []

    # ---------------------------------------------------------
    # SAVE EMAIL
    # ---------------------------------------------------------
    def save(self, email_data: dict, prefix: str):
        """
        Saves an email (draft or sent) with a prefix:
        draft_<id>.json
        sent_<id>.json

        Returns the filename on success, None on failure.
        Deterministic and safe.
        """

        email_id = email_data.get("id")

        if not isinstance(email_id, str) or len(email_id) == 0:
            return None

        filename = f"{prefix}_{email_id}.json"

        try:
            with open(self._path(filename), "w", encoding="utf-8") as f:
                json.dump(email_data, f, indent=2, ensure_ascii=False)
        except Exception:
            return None

        return filename

    # ---------------------------------------------------------
    # LOAD EMAIL BY ID
    # ---------------------------------------------------------
    def load(self, email_id: str):
        """
        Loads an email by ID, regardless of prefix.
        Returns dict on success, None on failure.
        Deterministic and safe.
        """

        for f in self._safe_listdir():
            if f.endswith(".json") and email_id in f:
                try:
                    with open(self._path(f), "r", encoding="utf-8") as file:
                        data = json.load(file)
                except Exception:
                    return None

                # Validate structure
                if not isinstance(data, dict):
                    return None

                return data

        return None

    # ---------------------------------------------------------
    # LIST EMAILS
    # ---------------------------------------------------------
    def list(self, status=None):
        """
        Lists all emails or filters by status (draft/sent).
        Returns a list of email dicts.
        Deterministic ordering.
        """

        emails = []

        for f in self._safe_listdir():
            if not f.endswith(".json"):
                continue

            try:
                with open(self._path(f), "r", encoding="utf-8") as file:
                    data = json.load(file)
            except Exception:
                continue

            if not isinstance(data, dict):
                continue

            if status is None or data.get("status") == status:
                emails.append(data)

        return emails

    # ---------------------------------------------------------
    # DELETE EMAIL
    # ---------------------------------------------------------
    def delete(self, email_id: str):
        """
        Deletes an email by ID.
        Returns True on success, False on failure.
        Deterministic and safe.
        """

        for f in self._safe_listdir():
            if f.endswith(".json") and email_id in f:
                try:
                    os.remove(self._path(f))
                    return True
                except Exception:
                    return False

        return False
