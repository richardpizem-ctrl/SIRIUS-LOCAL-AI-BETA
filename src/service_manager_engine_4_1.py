# service_manager_engine_4_4.py
# SIRIUS LOCAL AI – Service Manager Engine 4.4.0 PRO
# Deterministic, sandboxed, safe-mode compatible diagnostics (Phase‑4/5 ready)

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import List, Literal, Optional, Dict, Any

import psutil


ServiceSeverity = Literal["info", "warning", "critical"]


# ---------------------------------------------------------
# DATA STRUCTURES (4.4.0 PRO)
# ---------------------------------------------------------

@dataclass
class ServiceInfo44:
    name: str
    status: str
    pid: Optional[int]
    is_critical: bool


@dataclass
class ServiceIssue44:
    id: str
    severity: ServiceSeverity
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    related_services: List[str] = field(default_factory=list)
    impact: Optional[str] = None
    quick_fix: bool = False


@dataclass
class ServiceReport44:
    timestamp: float
    services: List[ServiceInfo44] = field(default_factory=list)
    issues: List[ServiceIssue44] = field(default_factory=list)
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ENGINE 4.4.0 PRO
# ---------------------------------------------------------

class ServiceManagerEngine44:
    """
    Service Manager Engine 4.4.0 PRO

    - deterministic diagnostics
    - sandboxed service enumeration
    - no direct service modification
    - safe-mode & degraded-mode aware
    - Phase‑5 ready (restricted-mode hooks)
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

        self._critical_services = {
            "AudioSrv",
            "Audiosrv",
            "W32Time",
            "wuauserv",
            "WinDefend",
            "Dhcp",
            "Dnscache",
            "LanmanWorkstation",
            "LanmanServer",
            "Spooler",
            "Themes",
            "EventLog",
        }

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def analyze(self) -> ServiceReport44:
        """
        Main entry point for Runtime Manager 4.4.
        Always returns a valid ServiceReport44.
        """

        if self.safe_mode:
            return ServiceReport44(
                timestamp=time.time(),
                services=[],
                issues=[],
                safe_mode=True,
                degraded_mode=False,
            )

        try:
            services = self._collect_services()
            issues: List[ServiceIssue44] = []

            issues.extend(self._detect_stopped_critical_services(services))
            issues.extend(self._detect_failed_services(services))
            issues.extend(self._detect_audio_restart_candidate(services))
            issues.extend(self._detect_network_restart_candidate(services))
            issues.extend(self._detect_windows_update_issues(services))

            return ServiceReport44(
                timestamp=time.time(),
                services=services,
                issues=issues,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )

        except Exception:
            self.degraded_mode = True
            return ServiceReport44(
                timestamp=time.time(),
                services=[],
                issues=[],
                safe_mode=False,
                degraded_mode=True,
            )

    # ---------------------------------------------------------
    # SERVICE COLLECTION (SANDBOXED)
    # ---------------------------------------------------------

    def _collect_services(self) -> List[ServiceInfo44]:
        result: List[ServiceInfo44] = []

        try:
            for svc in psutil.win_service_iter():
                try:
                    info = svc.as_dict()
                    name = info.get("name", "unknown")
                    status = info.get("status", "unknown")
                    pid = info.get("pid", None)

                    result.append(
                        ServiceInfo44(
                            name=name,
                            status=status,
                            pid=pid,
                            is_critical=name in self._critical_services,
                        )
                    )
                except Exception:
                    self.degraded_mode = True
                    continue
        except Exception:
            self.degraded_mode = True

        return result

    # ---------------------------------------------------------
    # ANALYSIS HELPERS (4.4.0 PRO)
    # ---------------------------------------------------------

    def _detect_stopped_critical_services(self, services: List[ServiceInfo44]) -> List[ServiceIssue44]:
        issues: List[ServiceIssue44] = []

        stopped = [s for s in services if s.is_critical and s.status.lower() != "running"]

        if not stopped:
            return issues

        issues.append(
            ServiceIssue44(
                id="critical_services_stopped",
                severity="critical",
                title="Kritické služby Windows sú zastavené",
                description=(
                    "Jedna alebo viac kritických služieb Windows nie je spustená. "
                    "To môže spôsobovať problémy so zvukom, sieťou, aktualizáciami alebo stabilitou systému."
                ),
                suggested_actions=[
                    "Navrhnúť reštart kritických služieb cez VYSLANEC 4.4.",
                    "Zobraziť používateľovi zoznam zastavených služieb.",
                ],
                related_services=[s.name for s in stopped],
                impact="system_stability",
                quick_fix=True,
            )
        )

        return issues

    def _detect_failed_services(self, services: List[ServiceInfo44]) -> List[ServiceIssue44]:
        issues: List[ServiceIssue44] = []

        failed = [s for s in services if s.status.lower() == "stopped" and not s.is_critical]

        if not failed:
            return issues

        issues.append(
            ServiceIssue44(
                id="noncritical_services_failed",
                severity="warning",
                title="Niektoré služby sú zastavené",
                description=(
                    "Niektoré služby Windows nie sú spustené. "
                    "Nemusia byť kritické, ale môžu ovplyvniť funkčnosť aplikácií."
                ),
                suggested_actions=[
                    "Ponúknuť možnosť reštartu týchto služieb cez VYSLANEC 4.4.",
                ],
                related_services=[s.name for s in failed],
                impact="usability",
                quick_fix=True,
            )
        )

        return issues

    def _detect_audio_restart_candidate(self, services: List[ServiceInfo44]) -> List[ServiceIssue44]:
        issues: List[ServiceIssue44] = []

        audio = [s for s in services if s.name.lower() in ("audiosrv", "audiosrv")]

        if not audio:
            return issues

        svc = audio[0]
        if svc.status.lower() != "running":
            issues.append(
                ServiceIssue44(
                    id="audio_service_down",
                    severity="warning",
                    title="Windows Audio nie je spustené",
                    description="Zvuk nemusí fungovať správne.",
                    suggested_actions=[
                        "Navrhnúť reštart Windows Audio cez VYSLANEC 4.4.",
                    ],
                    related_services=[svc.name],
                    impact="audio",
                    quick_fix=True,
                )
            )

        return issues

    def _detect_network_restart_candidate(self, services: List[ServiceInfo44]) -> List[ServiceIssue44]:
        issues: List[ServiceIssue44] = []

        dhcp = [s for s in services if s.name.lower() == "dhcp"]
        dns = [s for s in services if s.name.lower() == "dnscache"]

        if dhcp and dhcp[0].status.lower() != "running":
            issues.append(
                ServiceIssue44(
                    id="dhcp_down",
                    severity="warning",
                    title="DHCP Client nie je spustený",
                    description="Sieť nemusí fungovať správne.",
                    suggested_actions=[
                        "Navrhnúť reštart DHCP Client cez VYSLANEC 4.4.",
                    ],
                    related_services=["Dhcp"],
                    impact="network",
                    quick_fix=True,
                )
            )

        if dns and dns[0].status.lower() != "running":
            issues.append(
                ServiceIssue44(
                    id="dns_down",
                    severity="warning",
                    title="DNS Client nie je spustený",
                    description="Môžu sa vyskytnúť problémy s internetom.",
                    suggested_actions=[
                        "Navrhnúť reštart DNS Client cez VYSLANEC 4.4.",
                    ],
                    related_services=["Dnscache"],
                    impact="network",
                    quick_fix=True,
                )
            )

        return issues

    def _detect_windows_update_issues(self, services: List[ServiceInfo44]) -> List[ServiceIssue44]:
        issues: List[ServiceIssue44] = []

        wu = [s for s in services if s.name.lower() == "wuauserv"]

        if wu and wu[0].status.lower() != "running":
            issues.append(
                ServiceIssue44(
                    id="windows_update_down",
                    severity="info",
                    title="Windows Update nie je spustený",
                    description="Aktualizácie systému nemusia fungovať.",
                    suggested_actions=[
                        "Navrhnúť reštart Windows Update cez VYSLANEC 4.4.",
                    ],
                    related_services=["wuauserv"],
                    impact="usability",
                    quick_fix=False,
                )
            )

        return issues

    # ---------------------------------------------------------
    # SUMMARY FOR SYSTEM HEALTH ENGINE 4.4
    # ---------------------------------------------------------

    def get_service_summary(self) -> Dict[str, Any]:
        try:
            services = self._collect_services()
            stopped = len([s for s in services if s.status.lower() != "running"])
            critical_stopped = len([s for s in services if s.is_critical and s.status.lower() != "running"])

            return {
                "total_services": len(services),
                "stopped_services": stopped,
                "critical_stopped": critical_stopped,
                "safe_mode": self.safe_mode,
                "degraded_mode": self.degraded_mode,
            }
        except Exception:
            self.degraded_mode = True
            return {
                "total_services": 0,
                "stopped_services": 0,
                "critical_stopped": 0,
                "safe_mode": self.safe_mode,
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # SAFE-MODE CONTROL
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
