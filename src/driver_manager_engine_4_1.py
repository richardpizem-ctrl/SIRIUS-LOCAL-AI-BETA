# driver_manager_engine_4_3.py
# SIRIUS LOCAL AI – Driver Manager Engine 4.3.x
# Safe, deterministic, sandboxed driver diagnostics module

from __future__ import annotations

import os
import time
import zipfile
from dataclasses import dataclass, field
from typing import List, Optional, Literal

import psutil
import winreg


DriverSeverity = Literal["info", "warning", "critical"]


# ---------------------------------------------------------
# DATA STRUCTURES
# ---------------------------------------------------------

@dataclass
class DriverIssue:
    id: str
    severity: DriverSeverity
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    related_files: List[str] = field(default_factory=list)


@dataclass
class DriverReport:
    timestamp: float
    issues: List[DriverIssue] = field(default_factory=list)
    detected_inf_files: List[str] = field(default_factory=list)
    detected_packages: List[str] = field(default_factory=list)
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ENGINE
# ---------------------------------------------------------

class DriverManagerEngine43:
    """
    Driver Manager Engine 4.3.x

    - Safe, deterministic diagnostics
    - No installation, no system modification
    - Registry scanning sandbox
    - ZIP/EXE preview sandbox
    - Structured fallback behavior
    - Safe-mode and degraded-mode support
    - Self-Repair 4.4 ready
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False
        self.downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def analyze(self) -> DriverReport:
        """
        Main entry point for Runtime Manager 4.3.x.
        Always returns a valid DriverReport.
        """

        if self.safe_mode:
            return DriverReport(
                timestamp=time.time(),
                issues=[],
                detected_inf_files=[],
                detected_packages=[],
                safe_mode=True,
                degraded_mode=False,
            )

        try:
            inf_files = self._scan_downloads_for_inf()
            packages = self._scan_downloads_for_packages()

            issues = []
            issues.extend(self._detect_missing_drivers())
            issues.extend(self._detect_corrupted_drivers())
            issues.extend(self._detect_outdated_drivers())

            return DriverReport(
                timestamp=time.time(),
                issues=issues,
                detected_inf_files=inf_files,
                detected_packages=packages,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )

        except Exception:
            self.degraded_mode = True
            return DriverReport(
                timestamp=time.time(),
                issues=[],
                detected_inf_files=[],
                detected_packages=[],
                safe_mode=False,
                degraded_mode=True,
            )

    # ---------------------------------------------------------
    # DOWNLOADS SCANNING (SANDBOXED)
    # ---------------------------------------------------------

    def _scan_downloads_for_inf(self) -> List[str]:
        """Find INF files in Downloads (safe, deterministic)."""
        try:
            if not os.path.exists(self.downloads_path):
                return []

            return [
                os.path.join(self.downloads_path, f)
                for f in os.listdir(self.downloads_path)
                if f.lower().endswith(".inf")
            ]
        except Exception:
            self.degraded_mode = True
            return []

    def _scan_downloads_for_packages(self) -> List[str]:
        """Find ZIP/EXE driver packages in Downloads."""
        try:
            if not os.path.exists(self.downloads_path):
                return []

            return [
                os.path.join(self.downloads_path, f)
                for f in os.listdir(self.downloads_path)
                if f.lower().endswith(".zip") or f.lower().endswith(".exe")
            ]
        except Exception:
            self.degraded_mode = True
            return []

    # ---------------------------------------------------------
    # DRIVER DIAGNOSTICS (SANDBOXED)
    # ---------------------------------------------------------

    def _detect_missing_drivers(self) -> List[DriverIssue]:
        """Detect missing drivers via registry (safe, isolated)."""
        issues = []

        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SYSTEM\CurrentControlSet\Enum\PCI",
            )
        except Exception:
            return issues

        try:
            i = 0
            while True:
                try:
                    device = winreg.EnumKey(key, i)
                except OSError:
                    break

                try:
                    device_key = winreg.OpenKey(key, device)
                except Exception:
                    i += 1
                    continue

                j = 0
                while True:
                    try:
                        sub = winreg.EnumKey(device_key, j)
                    except OSError:
                        break

                    try:
                        subkey = winreg.OpenKey(device_key, sub)
                        winreg.QueryValueEx(subkey, "Driver")
                    except FileNotFoundError:
                        issues.append(
                            DriverIssue(
                                id=f"missing_driver_{device}_{sub}",
                                severity="critical",
                                title="Chýbajúci ovládač zariadenia",
                                description=(
                                    f"Zariadenie {device}/{sub} nemá priradený ovládač. "
                                    "Systém môže mať obmedzenú funkcionalitu."
                                ),
                                suggested_actions=[
                                    "Vyhľadať INF súbor v Downloads.",
                                    "Navrhnúť inštaláciu cez VYSLANEC 4.3.",
                                    "Navrhnúť otvorenie oficiálnej stránky výrobcu.",
                                ],
                            )
                        )
                    except Exception:
                        self.degraded_mode = True

                    j += 1

                i += 1

        except Exception:
            self.degraded_mode = True

        return issues

    def _detect_corrupted_drivers(self) -> List[DriverIssue]:
        """Placeholder for signature/integrity checks."""
        return []

    def _detect_outdated_drivers(self) -> List[DriverIssue]:
        """Placeholder for version comparison."""
        return []

    # ---------------------------------------------------------
    # SAFE PACKAGE PREVIEW
    # ---------------------------------------------------------

    def extract_zip_preview(self, path: str) -> List[str]:
        """Safely preview ZIP contents without extraction."""
        try:
            if not zipfile.is_zipfile(path):
                return []
            with zipfile.ZipFile(path, "r") as z:
                return z.namelist()
        except Exception:
            self.degraded_mode = True
            return []

    # ---------------------------------------------------------
    # SYSTEM HEALTH HOOK
    # ---------------------------------------------------------

    def get_driver_summary(self) -> dict:
        """Provide System Health Engine 4.3.x with basic driver info."""
        try:
            return {
                "missing": len(self._detect_missing_drivers()),
                "corrupted": 0,
                "outdated": 0,
                "safe_mode": self.safe_mode,
                "degraded_mode": self.degraded_mode,
            }
        except Exception:
            self.degraded_mode = True
            return {
                "missing": 0,
                "corrupted": 0,
                "outdated": 0,
                "safe_mode": self.safe_mode,
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # SAFE-MODE
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
