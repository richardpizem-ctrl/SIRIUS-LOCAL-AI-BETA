# File: src/runtime4/self_repair/recovery_protocol.py
"""
Recovery Protocol
Version: 4.5.0
Component of: Self-Repair Layer (Phase‑5)

Responsible for:
- Deterministic repair decision logic
- Mapping integrity scan results to recovery actions
- Coordinating safe, reversible repair steps
- Ensuring no destructive or unsafe operations occur
"""

class RecoveryProtocol:
    """
    Defines deterministic rules for how the system responds
    to detected corruption or instability.
    """

    def __init__(self):
        # Recovery rules can be extended in future versions
        self.rules = {
            "missing": self._handle_missing_file,
            "modified": self._handle_modified_file,
        }

    def apply(self, scan_result):
        """
        Applies recovery rules to the integrity scan result.
        Returns a list of executed recovery actions.
        """
        actions = []

        corrupted = scan_result.get("corrupted_modules", [])
        if not corrupted:
            return actions

        for module, file_path, issue_type in corrupted:
            handler = self.rules.get(issue_type)
            if handler:
                action = handler(module, file_path)
                if action:
                    actions.append(action)

        return actions

    # ---------------------------------------------------------
    # HANDLERS FOR SPECIFIC ISSUE TYPES
    # ---------------------------------------------------------

    def _handle_missing_file(self, module, file_path):
        """
        Handles missing files by marking them for rebuild.
        """
        return {
            "action": "mark_for_rebuild",
            "module": module,
            "file": file_path,
            "reason": "missing_file",
        }

    def _handle_modified_file(self, module, file_path):
        """
        Handles modified files by marking them for rebuild
        and triggering fallback logic.
        """
        return {
            "action": "mark_for_rebuild_and_fallback",
            "module": module,
            "file": file_path,
            "reason": "modified_file",
        }
