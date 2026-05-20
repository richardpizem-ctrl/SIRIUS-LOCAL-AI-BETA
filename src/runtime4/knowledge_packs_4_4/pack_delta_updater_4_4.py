knowledge_packs_4_4/pack_delta_updater_4_4.py
"""
SIRIUS LOCAL AI – Pack Delta Updater 4.4.0

This module provides deterministic, offline‑safe delta updates for
Knowledge Packs 4.4.

It supports:
- Computing diffs between pack versions
- Applying diffs to produce updated pack data
- Safe rollback
- Zero code execution (data‑only)
- Integration with KP Registry 4.4 and KP Validator 4.4

Security Notes:
- No dynamic imports, no eval, no reflection.
- Only JSON/dict structures are processed.
- Deltas are reversible and deterministic.
"""

from typing import Dict, Any, List


class PackDeltaUpdater44:
    """
    Deterministic delta generator + applier for Knowledge Packs 4.4.
    """

    def __init__(self, validator=None):
        self.validator = validator
        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.validator:
                self.validator.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # COMPUTE DELTA
    # ------------------------------------------------------------------
    def compute_delta(self, old_pack: Dict[str, Any], new_pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Computes a deterministic delta between two pack versions.
        Only JSON‑safe structures are compared.
        """

        delta = {
            "added": {},
            "removed": {},
            "modified": {},
        }

        old_keys = set(old_pack.keys())
        new_keys = set(new_pack.keys())

        # Added keys
        for key in new_keys - old_keys:
            delta["added"][key] = new_pack[key]

        # Removed keys
        for key in old_keys - new_keys:
            delta["removed"][key] = old_pack[key]

        # Modified keys
        for key in old_keys & new_keys:
            if old_pack[key] != new_pack[key]:
                delta["modified"][key] = {
                    "old": old_pack[key],
                    "new": new_pack[key],
                }

        return {"status": "ok", "delta": delta}

    # ------------------------------------------------------------------
    # APPLY DELTA
    # ------------------------------------------------------------------
    def apply_delta(self, base_pack: Dict[str, Any], delta: Dict[str, Any]) -> Dict[str, Any]:
        """
        Applies a delta to a base pack and returns the updated pack.
        """

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
                    "reason": "validation_failed_after_delta",
                    "details": valid,
                }

        return {"status": "ok", "updated_pack": updated}

    # ------------------------------------------------------------------
    # ROLLBACK DELTA
    # ------------------------------------------------------------------
    def rollback_delta(self, updated_pack: Dict[str, Any], delta: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reverses a previously applied delta.
        """

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

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
