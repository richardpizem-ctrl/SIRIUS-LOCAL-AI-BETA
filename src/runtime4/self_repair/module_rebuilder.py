# File: src/runtime4/self_repair/module_rebuilder.py
"""
Module Rebuilder
Version: 4.5.0
Component of: Self-Repair Layer (Phase‑5)

Responsible for:
- Rebuilding corrupted or missing modules
- Restoring files from known-good baselines
- Coordinating safe, deterministic reconstruction steps
"""

import os
import shutil
from typing import List, Tuple, Dict, Any


class ModuleRebuilder:
    """
    Rebuilds modules that were marked as corrupted or missing
    by the IntegrityScanner and RecoveryProtocol.
    """

    def __init__(
        self,
        baseline_root: str = "baseline_runtime4",
        target_root: str = "src/runtime4",
    ):
        """
        :param baseline_root: Path to directory with known-good copies of modules.
        :param target_root:   Path to active runtime modules.
        """
        self.baseline_root = baseline_root
        self.target_root = target_root

    def _baseline_path_for(self, module: str, file_path: str) -> str:
        """
        Maps a runtime file path to its baseline counterpart.
        Example:
            module = "self_repair"
            file_path = "src/runtime4/self_repair/self_repair_engine.py"
        """
        # Naive mapping: replace 'src/runtime4' with 'baseline_runtime4'
        if file_path.startswith(self.target_root):
            relative = file_path[len(self.target_root) :].lstrip("/\\")
            return os.path.join(self.baseline_root, relative)
        return os.path.join(self.baseline_root, module, os.path.basename(file_path))

    def _ensure_directory(self, path: str) -> None:
        """Ensures that the parent directory for a file exists."""
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    def _restore_file(self, baseline: str, target: str) -> bool:
        """
        Restores a single file from baseline to target.
        Returns True if successful, False otherwise.
        """
        if not os.path.exists(baseline):
            return False

        try:
            self._ensure_directory(target)
            shutil.copy2(baseline, target)
            return True
        except Exception:
            return False

    def rebuild(self, corrupted_modules: List[Tuple[str, str, str]]) -> List[Dict[str, Any]]:
        """
        Rebuilds all files marked as corrupted or missing.

        :param corrupted_modules: List of tuples:
            (module_name, file_path, issue_type)
        :return: List of rebuild action results.
        """
        results: List[Dict[str, Any]] = []

        for module, file_path, issue_type in corrupted_modules:
            baseline_path = self._baseline_path_for(module, file_path)
            success = self._restore_file(baseline_path, file_path)

            result = {
                "module": module,
                "file": file_path,
                "baseline": baseline_path,
                "issue_type": issue_type,
                "restored": success,
            }
            results.append(result)

        return results
