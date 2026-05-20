"""
SIRIUS LOCAL AI – Pack Delta Updater 4.4.0 (PRO)

This module provides deterministic, offline‑safe delta updates for
Knowledge Packs 4.4.

It supports:
- Computing diffs between pack versions
- Applying diffs to produce updated pack data
- Safe rollback
- Zero code execution (data‑only)
- Integration with KP Registry 4.4 and KP Validator 4.4

Security Notes (PRO):
- No dynamic imports, no eval, no reflection.
- Only JSON/dict structures are processed.
- Deltas must be deterministic and reversible.
"""

from typing import Dict, Any


class PackDeltaUpdater44:
    """
    Deterministic delta generator + applier for Knowledge Packs 4.4.
    """

    def __init__(self, validator=None):
        self.validator = validator
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
    # ------------------------------------------------------------------
    def _validate_dict(self, value: Any) -> bool:
        return isinstance(value, dict)

    def _validate_json_safe(self, value: Any) -> bool:
        return isinstance(value, (str, int, float, bool, dict, list))

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.validator:
                res = self.validator.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "validator_init_failed"}

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "init_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # COMPUTE DELTA
    # ------------------------------------------------------------------
    def compute_delta(self, old_pack: Dict[str, Any], new_pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Computes a deterministic delta between two pack versions.
        Only JSON‑safe structures are compared.
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Delta updater disabled in safe-mode."}

        if not self._validate_dict(old_pack) or not self._validate_dict(new_pack):
            return {"status": "error", "code": "invalid_pack_structure"}

        try:
            delta = {
                "added": {},
                "removed": {},
                "modified": {},
            }

            old_keys = set(old_pack.keys())
            new_keys = set(new_pack.keys())

            # Added keys
            for key in sorted(new_keys - old_keys):
                if self._validate_json_safe(new_pack[key]):
                    delta["added"][key] = new_pack[key]
                else:
                    return {"status": "error", "code": "unsafe_value_added", "key": key}

            # Removed keys
            for key in sorted(old_keys - new_keys):
                delta["removed"][key] = old_pack[key]

            # Modified keys
            for key in sorted(old_keys & new_keys):
                if old_pack[key] != new_pack[key]:
                    if not self._validate_json_safe(new_pack[key]):
                        return {"status": "error", "code": "unsafe_modified_value", "key": key}

                    delta["modified"][key] = {
                        "old": old_pack[key],
                        "new": new_pack[key],
                    }

            return {"status": "ok", "delta": delta}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "delta_compute_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # APPLY DELTA
    # ------------------------------------------------------------------
    def apply_delta(self, base_pack: Dict[str, Any], delta: Dict[str, Any]) -> Dict[str, Any]:
        """
        Applies a delta to a base pack and returns the updated pack.
        Deterministic, reversible, validator‑checked.
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Delta updater disabled in safe-mode."}

        if not self._validate_dict(base_pack) or not self._validate_dict(delta):
            return {"status": "error", "code": "invalid_structure"}

        try:
            updated = dict(base_pack)

            # Apply removals
            for key in delta.get("removed", {}):
                if key in updated:
                    del updated[key]

            # Apply additions
            for key, value in delta.get("added", {}).items():
                updated[key] = value

            # Apply modifications
            for key, change in delta.get("modified", {}).items():
                updated[key] = change.get("new")

            # Validate updated pack
            if self.validator:
                valid = self.validator.validate(updated)
                if valid.get("status") != "ok":
                    return {
                        "status": "error",
                        "code": "validation_failed_after_delta",
                        "details": valid,
                    }

            return {"status": "ok", "updated_pack": updated}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "apply_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # ROLLBACK DELTA
    # ------------------------------------------------------------------
    def rollback_delta(self, updated_pack: Dict[str, Any], delta: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reverses a previously applied delta.
        Deterministic, reversible, no validation required.
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Delta updater disabled in safe-mode."}

        if not self._validate_dict(updated_pack) or not self._validate_dict(delta):
            return {"status": "error", "code": "invalid_structure"}

        try:
            rolled_back = dict(updated_pack)

            # Undo additions
            for key in delta.get("added", {}):
                if key in rolled_back:
                    del rolled_back[key]

            # Undo removals
            for key, value in delta.get("removed", {}).items():
                rolled_back[key] = value

            # Undo modifications
            for key, change in delta.get("modified", {}).items():
                rolled_back[key] = change.get("old")

            return {"status": "ok", "rolled_back_pack": rolled_back}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "rollback_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }
