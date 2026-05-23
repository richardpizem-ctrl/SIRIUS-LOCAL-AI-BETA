# File: src/runtime4/self_repair/integrity_scanner.py
"""
Integrity Scanner
Version: 4.5.0
Component of: Self-Repair Layer (Phase‑5)

Responsible for:
- Scanning runtime modules for corruption
- Hash verification against integrity map
- Detecting missing or modified files
- Producing structured integrity reports

Notes:
- Deterministic, offline, isolated
- No dynamic imports, no eval, no reflection
- Fully compatible with Runtime 4.5
"""

import os
import hashlib
import json


class IntegrityScanner:
    """
    Performs deterministic integrity checks on runtime modules.
    Compares file hashes with the baseline integrity map.
    """

    def __init__(self, integrity_map_path="config/integrity_map.json"):
        self.version = "4.5.0"
        self.integrity_map_path = integrity_map_path
        self.integrity_map = self._load_integrity_map()

    # ---------------------------------------------------------
    # LOAD INTEGRITY MAP
    # ---------------------------------------------------------
    def _load_integrity_map(self):
        """Loads the baseline integrity map from JSON."""
        if not os.path.exists(self.integrity_map_path):
            return {}

        try:
            with open(self.integrity_map_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    # ---------------------------------------------------------
    # HASH FILE
    # ---------------------------------------------------------
    def _hash_file(self, path):
        """Returns SHA256 hash of a file."""
        try:
            sha = hashlib.sha256()
            with open(path, "rb") as f:
                while chunk := f.read(8192):
                    sha.update(chunk)
            return sha.hexdigest()
        except Exception:
            return None

    # ---------------------------------------------------------
    # SCAN MODULES
    # ---------------------------------------------------------
    def scan(self):
        """
        Scans all files listed in the integrity map.
        Returns a structured integrity report.
        """

        if not self.integrity_map:
            return {
                "status": "UNKNOWN",
                "details": "Integrity map missing or unreadable",
                "corrupted_modules": [],
                "version": self.version,
            }

        corrupted = []

        for module, files in self.integrity_map.items():
            for file_path, expected_hash in files.items():
                if not os.path.exists(file_path):
                    corrupted.append((module, file_path, "missing"))
                    continue

                actual_hash = self._hash_file(file_path)
                if actual_hash != expected_hash:
                    corrupted.append((module, file_path, "modified"))

        if not corrupted:
            return {
                "status": "OK",
                "details": "All modules verified",
                "corrupted_modules": [],
                "version": self.version,
            }

        return {
            "status": "CORRUPTED",
            "details": f"{len(corrupted)} issues detected",
            "corrupted_modules": corrupted,
            "version": self.version,
        }
