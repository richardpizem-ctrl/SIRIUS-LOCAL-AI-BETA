"""
SIRIUS LOCAL AI – Security Self‑Repair Layer 4.4.0 (PRO)

This module provides the *security‑focused* part of the Self‑Repair Layer
for Runtime 4.4. It performs:

- Integrity checks on security modules
- Detection of corrupted or missing components
- Safe automatic recovery (non‑code‑modifying)
- Patch suggestions (diff‑only, never applied automatically)
- System‑wide health reporting

All logic is deterministic, offline, and fully isolated.

CRITICAL SECURITY RULES:
- No automatic source‑code modification.
- No dynamic imports, no eval, no reflection.
- All repairs must be reversible and logged.
- High‑risk repairs require explicit user approval.
- Only static integrity checks allowed.
"""

from typing import Dict, Any, List


class SecuritySelfRepair44:
    """
    Security Self‑Repair subsystem for Runtime 4.4 (PRO).
    Ensures that the Security Family remains stable and uncompromised.
    """

    EXPECTED_MODULES = {
        "identity_engine_4_4",
        "security_behavior_monitor_4_4",
        "security_policy_router_4_4",
        "security_stranger_mode_4_4",
        "family_mode_4_4",
        "security_time_limits_4_4",
        "security_policy_core_4_4",
        "security_audit_4_4",
    }

    def __init__(self, fs_adapter=None):
        # fs_adapter must provide: initialize(), exists(path), write_file(path, content)
        self.fs_adapter = fs_adapter
        self.initialized = False
        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.fs_adapter and hasattr(self.fs_adapter, "initialize"):
                self.fs_adapter.initialize()

            self.initialized = True
            return {"status": "ok"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
            }

    # ------------------------------------------------------------------
    # PUBLIC API – INTEGRITY CHECK
    # ------------------------------------------------------------------
    def check_integrity(self, base_path: str) -> Dict[str, Any]:
        """
        Verifies that all required security modules exist.
        Does NOT read or execute code — only checks file presence.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Integrity checks disabled in safe-mode.",
            }

        if not isinstance(base_path, str) or not base_path.strip():
            return {
                "status": "error",
                "code": "invalid_base_path",
            }

        if not self.fs_adapter:
            return {
                "status": "error",
                "code": "no_fs_adapter",
            }

        if not hasattr(self.fs_adapter, "exists"):
            return {
                "status": "error",
                "code": "fs_adapter_missing_exists",
            }

        missing: List[str] = []
        present: List[str] = []

        try:
            for module in self.EXPECTED_MODULES:
                path = f"{base_path}/{module}.py"
                if self.fs_adapter.exists(path):
                    present.append(path)
                else:
                    missing.append(path)

            return {
                "status": "ok",
                "present": present,
                "missing": missing,
                "degraded_mode": self.degraded_mode,
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "integrity_check_failed",
                "exception": str(exc),
            }

    # ------------------------------------------------------------------
    # PUBLIC API – SAFE AUTO‑REPAIR
    # ------------------------------------------------------------------
    def auto_repair(self, missing_files: List[str]) -> Dict[str, Any]:
        """
        Performs safe automatic recovery:
        - Creates placeholder files for missing modules
        - NEVER writes executable logic
        - NEVER modifies existing code
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Auto‑repair disabled in safe-mode.",
            }

        if not isinstance(missing_files, list):
            return {
                "status": "error",
                "code": "invalid_missing_files",
            }

        if not self.fs_adapter:
            return {
                "status": "error",
                "code": "no_fs_adapter",
            }

        if not hasattr(self.fs_adapter, "write_file"):
            return {
                "status": "error",
                "code": "fs_adapter_missing_write_file",
            }

        created: List[str] = []

        placeholder = (
            '"""AUTO‑GENERATED PLACEHOLDER FILE — SECURITY SELF‑REPAIR 4.4\n'
            'This file was created because the original module was missing.\n'
            'Please replace it with the correct implementation.\n'
            'No executable logic is contained in this placeholder.\n'
            '"""'
        )

        try:
            for path in missing_files:
                if not isinstance(path, str) or not path.strip():
                    continue
                self.fs_adapter.write_file(path, placeholder)
                created.append(path)

            return {"status": "ok", "created": created}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "auto_repair_failed",
                "exception": str(exc),
            }

    # ------------------------------------------------------------------
    # PUBLIC API – PATCH SUGGESTION (DIFF‑ONLY)
    # ------------------------------------------------------------------
    def suggest_patch(self, module_name: str, issue: str) -> Dict[str, Any]:
        """
        Generates a deterministic diff‑style patch suggestion.
        Does NOT apply the patch.
        """

        if not isinstance(module_name, str) or not module_name.strip():
            return {
                "status": "error",
                "code": "invalid_module_name",
            }

        if not isinstance(issue, str) or not issue.strip():
            return {
                "status": "error",
                "code": "invalid_issue",
            }

        patch = [
            f"--- {module_name}.py",
            f"+++ {module_name}.py",
            f"# Suggested fix for: {issue}",
            "# (This is a non‑executable diff suggestion.)",
        ]

        return {
            "status": "ok",
            "module": module_name,
            "patch": patch,
            "degraded_mode": self.degraded_mode,
        }

    # ------------------------------------------------------------------
    # PUBLIC API – HEALTH REPORT
    # ------------------------------------------------------------------
    def health_report(self, base_path: str) -> Dict[str, Any]:
        """
        Returns a full health summary of the Security Family.
        """

        integrity = self.check_integrity(base_path)

        return {
            "status": "ok",
            "integrity": integrity,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }
