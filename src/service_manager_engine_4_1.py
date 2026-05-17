# service_manager_engine_4_3.py
# SIRIUS LOCAL AI – Service Manager Engine 4.3.x
# Safe, deterministic, sandboxed service diagnostics module

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import List, Literal, Optional, Dict, Any

import psutil


ServiceSeverity = Literal["info", "warning", "critical"]


# ---------------------------------------------------------
# DATA STRUCTURES
# ---------------------------------------------------------

@dataclass
class ServiceInfo:
    name: str
    status: str
    pid: Optional[int]
    is_critical: bool


@dataclass
class ServiceIssue:
    id: str
    severity: ServiceSeverity
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    related_services: List[str] = field(default_factory=list)
    impact: Optional[str] = None       # "system_stability" | "network" | "audio" | ...
    quick_fix: bool = False            # hint for orchestrator


@dataclass
class ServiceReport:
    timestamp: float
    services: List[ServiceInfo] = field(default_factory=list)
    issues: List[ServiceIssue] = field(default_factory=list)
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ENGINE
# ---------------------------------------------------------

class ServiceManagerEngine43:
    """
    Service Manager Engine 4.3.x

    - safe diagnostic module
    - no direct changes to Windows services
    - all actions are delegated to VYSLANEC / SystemAgent 4.3
    - deterministic, offline, sandbox-friendly
    - safe-mode and degraded-mode aware
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

        # critical Windows services
        self._critical_services = {
            "AudioSrv",          # Windows Audio
            "Audiosrv",
            "W32Time",           # Windows Time
            "wuauserv",          # Windows Update
            "WinDefend",         # Defender
            "Dhcp",              # DHCP Client
            "Dnscache",          # DNS Client
            "LanmanWorkstation", # Workstation
            "LanmanServer",      # Server
            "Spooler",           # Print Spooler
            "Themes",
            "EventLog",
        }

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def analyze(self) -> ServiceReport:
        """
        Main entry point for Runtime Manager 4.3.x.
        Always returns a valid ServiceReport.
        """

        if self.safe_mode:
            return ServiceReport(
                timestamp=time.time(),
                services=[],
                issues=[],
                safe_mode=True,
                degraded_mode=False,
            )

        try:
            services = self._collect_services()
            issues: List[ServiceIssue] = []

            issues.extend(self._detect_stopped_critical_services(services))
            issues.extend(self._detect_failed_services(services))
            issues.extend(self._detect_audio_restart_candidate(services))
            issues.extend(self._detect_network_restart_candidate(services))
            issues.extend(self._detect_windows_update_issues(services))

            return ServiceReport(
                timestamp=time.time(),
                services=services,
                issues=issues,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )

        except Exception:
            self.degraded_mode = True
            return ServiceReport(
                timestamp=time.time(),
                services=[],
                issues=[],
                safe_mode=False,
                degraded_mode=True,
            )

    # ---------------------------------------------------------
    # SERVICE COLLECTION (SANDBOXED)
    # ---------------------------------------------------------

    def _collect_services(self) -> List[ServiceInfo]:
        result: List[ServiceInfo] = []

        try:
            for svc in psutil.win_service_iter():
                try:
                    info = svc.as_dict()
                    name = info.get("name", "unknown")
                    status = info.get("status", "unknown")
                    pid = info.get("pid", None)

                    result.append(
                        ServiceInfo(
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
    # ANALYSIS HELPERS
    # ---------------------------------------------------------

    def _detect_stopped_critical_services(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        stopped = [s for s in services if s.is_critical and s.status.lower() != "running"]

        if not stopped:
            return issues

        issues.append(
            ServiceIssue(
                id="critical_services_stopped",
                severity="critical",
                title="Kritické služby Windows sú zastavené",
                description=(
                    "Jedna alebo viac kritických služieb Windows nie je spustená. "
                    "To môže spôsobovať problémy so zvukom, sieťou, aktualizáciami alebo stabilitou systému."
                ),
                suggested_actions=[
                    "Navrhnúť reštart kritických služieb cez VYSLANEC 4.3.",
                    "Zobraziť používateľovi zoznam zastavených služieb.",
                ],
                related_services=[s.name for s in stopped],
                impact="system_stability",
                quick_fix=True,
            )
        )

        return issues

    def _detect_failed_services(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        failed = [s for s in services if s.status.lower() == "stopped" and not s.is_critical]

        if not failed:
            return issues

        issues.append(
            ServiceIssue(
                id="noncritical_services_failed",
                severity="warning",
                title="Niektoré služby sú zastavené",
                description=(
                    "Niektoré služby Windows nie sú spustené. "
                    "Nemusia byť kritické, ale môžu ovplyvniť funkčnosť aplikácií."
                ),
                suggested_actions=[
                    "Ponúknuť možnosť reštartu týchto služieb cez VYSLANEC 4.3.",
                ],
                related_services=[s.name for s in failed],
                impact="usability",
                quick_fix=True,
            )
        )

        return issues

    def _detect_audio_restart_candidate(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        audio = [s for s in services if s.name.lower() in ("audiosrv", "audiosrv")]

        if not audio:
            return issues

        svc = audio[0]
        if svc.status.lower() != "running":
            issues.append(
                ServiceIssue(
                    id="audio_service_down",
                    severity="warning",
                    title="Windows Audio nie je spustené",
                    description="Zvuk nemusí fungovať správne.",
                    suggested_actions=[
                        "Navrhnúť reštart Windows Audio cez VYSLANEC 4.3.",
                    ],
                    related_services=[svc.name],
                    impact="audio",
                    quick_fix=True,
                )
            )

        return issues

    def _detect_network_restart_candidate(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        dhcp = [s for s in services if s.name.lower() == "dhcp"]
        dns = [s for s in services if s.name.lower() == "dnscache"]

        if dhcp and dhcp[0].status.lower() != "running":
            issues.append(
                ServiceIssue(
                    id="dhcp_down",
                    severity="warning",
                    title="DHCP Client nie je spustený",
                    description="Sieť nemusí fungovať správne.",
                    suggested_actions=[
                        "Navrhnúť reštart DHCP Client cez VYSLANEC 4.3.",
                    ],
                    related_services=["Dhcp"],
                    impact="network",
                    quick_fix=True,
                )
            )

        if dns and dns[0].status.lower() != "running":
            issues.append(
                ServiceIssue(
                    id="dns_down",
                    severity="warning",
                    title="DNS Client nie je spustený",
                    description="Môžu sa vyskytnúť problémy s internetom.",
                    suggested_actions=[
                        "Navrhnúť reštart DNS Client cez VYSLANEC 4.3.",
                    ],
                    related_services=["Dnscache"],
                    impact="network",
                    quick_fix=True,
                )
            )

        return issues

    def _detect_windows_update_issues(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        wu = [s for s in services if s.name.lower() == "wuauserv"]

        if wu and wu[0].status.lower() != "running":
            issues.append(
                ServiceIssue(
                    id="windows_update_down",
                    severity="info",
                    title="Windows Update nie je spustený",
                    description="Aktualizácie systému nemusia fungovať.",
                    suggested_actions=[
                        "Navrhnúť reštart Windows Update cez VYSLANEC 4.3.",
                    ],
                    related_services=["wuauserv"],
                    impact="usability",
                    quick_fix=False,
                )
            )

        return issues

    # ---------------------------------------------------------
    # SUMMARY FOR SYSTEM HEALTH ENGINE
    # ---------------------------------------------------------

    def get_service_summary(self) -> Dict[str, Any]:
        """
        Provide System Health Engine 4.3.x with basic service info.
        Error-safe, deterministic.
        """
        try:
            services = self._collect_services()
            stopped = len([s for s in services if s.status.lower() != "running"])
            critical_stopped = len(
                [s for s in services if s.is_critical and s.status.lower() != "running"]
            )

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
