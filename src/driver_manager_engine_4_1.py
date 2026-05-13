"""
Driver Manager Engine 4.1
-------------------------

Safe offline driver diagnostics module for SIRIUS LOCAL AI v4.1.0.

Účel:
- detekcia chýbajúcich ovládačov
- detekcia poškodených ovládačov
- detekcia zastaraných ovládačov
- čítanie INF súborov (bez inštalácie)
- extrakcia ZIP/EXE balíkov (bez spúšťania)
- monitorovanie priečinka Downloads
- generovanie návrhov pre VYSLANEC 4.1 (Bridge Layer)

Tento modul:
- NEINŠTALUJE ovládače
- NESPÚŠŤA EXE
- NEZASAHUJE do systému
- len analyzuje a navrhuje bezpečné akcie
"""

from __future__ import annotations

import os
import time
import zipfile
from dataclasses import dataclass, field
from typing import List, Optional, Literal

import psutil
import winreg


DriverSeverity = Literal["info", "warning", "critical"]


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


class DriverManagerEngine41:
    """
    Driver Manager Engine 4.1

    - bezpečný diagnostický modul
    - žiadne priame zásahy do systému
    - všetky akcie musia ísť cez VYSLANEC 4.1
    """

    def __init__(self):
        self.downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # -------------------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------------------

    def analyze(self) -> DriverReport:
        """
        Hlavný vstupný bod pre Runtime Core 4.0.
        """
        issues: List[DriverIssue] = []

        inf_files = self._scan_downloads_for_inf()
        packages = self._scan_downloads_for_packages()

        issues.extend(self._detect_missing_drivers())
        issues.extend(self._detect_corrupted_drivers())
        issues.extend(self._detect_outdated_drivers())

        return DriverReport(
            timestamp=time.time(),
            issues=issues,
            detected_inf_files=inf_files,
            detected_packages=packages,
        )

    # -------------------------------------------------------------------------
    # DOWNLOADS SCANNING
    # -------------------------------------------------------------------------

    def _scan_downloads_for_inf(self) -> List[str]:
        """
        Nájde INF súbory v Downloads.
        """
        found = []
        if not os.path.exists(self.downloads_path):
            return found

        for file in os.listdir(self.downloads_path):
            if file.lower().endswith(".inf"):
                found.append(os.path.join(self.downloads_path, file))

        return found

    def _scan_downloads_for_packages(self) -> List[str]:
        """
        Nájde ZIP/EXE balíky ovládačov v Downloads.
        """
        found = []
        if not os.path.exists(self.downloads_path):
            return found

        for file in os.listdir(self.downloads_path):
            if file.lower().endswith(".zip") or file.lower().endswith(".exe"):
                found.append(os.path.join(self.downloads_path, file))

        return found

    # -------------------------------------------------------------------------
    # DRIVER DIAGNOSTICS
    # -------------------------------------------------------------------------

    def _detect_missing_drivers(self) -> List[DriverIssue]:
        """
        Detekcia chýbajúcich ovládačov cez Windows registry.
        """
        issues = []

        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SYSTEM\CurrentControlSet\Enum\PCI",
            )
        except Exception:
            return issues

        # Prechádzame zariadenia
        try:
            i = 0
            while True:
                device = winreg.EnumKey(key, i)
                device_key = winreg.OpenKey(key, device)
                j = 0
                while True:
                    try:
                        sub = winreg.EnumKey(device_key, j)
                        subkey = winreg.OpenKey(device_key, sub)
                        try:
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
                                        "Navrhnúť inštaláciu cez VYSLANEC 4.1.",
                                        "Navrhnúť otvorenie oficiálnej stránky výrobcu.",
                                    ],
                                )
                            )
                        j += 1
                    except OSError:
                        break
                i += 1
        except OSError:
            pass

        return issues

    def _detect_corrupted_drivers(self) -> List[DriverIssue]:
        """
        Placeholder – neskôr doplníme kontrolu podpisov a integrity.
        """
        return []

    def _detect_outdated_drivers(self) -> List[DriverIssue]:
        """
        Placeholder – neskôr doplníme porovnávanie verzií.
        """
        return []

    # -------------------------------------------------------------------------
    # SAFE PACKAGE EXTRACTION
    # -------------------------------------------------------------------------

    def extract_zip_preview(self, path: str) -> List[str]:
        """
        Bezpečne zobrazí obsah ZIP súboru bez extrakcie.
        """
        if not zipfile.is_zipfile(path):
            return []

        with zipfile.ZipFile(path, "r") as z:
            return z.namelist()

    # -------------------------------------------------------------------------
    # HOOKS FOR SYSTEM HEALTH ENGINE
    # -------------------------------------------------------------------------

    def get_driver_summary(self) -> dict:
        """
        Poskytne System Health Engine 4.1 základné info o ovládačoch.
        """
        return {
            "missing": len(self._detect_missing_drivers()),
            "corrupted": 0,
            "outdated": 0,
        }
