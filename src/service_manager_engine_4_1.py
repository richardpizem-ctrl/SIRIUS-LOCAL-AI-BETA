"""
Service Manager Engine 4.1
--------------------------

Bezpečný diagnostický modul pre SIRIUS LOCAL AI v4.1.0.

Účel:
- detegovať nefunkčné alebo zastavené služby
- detegovať služby, ktoré zlyhali pri štarte
- detegovať služby, ktoré sú kritické pre Windows
- navrhovať bezpečné akcie (reštart Audio, Windows Update, Network)
- poskytovať dáta pre System Health Engine 4.1 a VYSLANEC 4.1

Tento modul:
- NEREŠTARTUJE služby priamo
- NEZASTAVUJE služby
- NEZASAHUJE do systému
- len analyzuje a navrhuje akcie, ktoré vykoná VYSLANEC 4.1
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import List, Literal

import psutil


ServiceSeverity = Literal["info", "warning", "critical"]


@dataclass
class ServiceInfo:
    name: str
    status: str
    pid: int | None
    is_critical: bool


@dataclass
class ServiceIssue:
    id: str
    severity: ServiceSeverity
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    related_services: List[str] = field(default_factory=list)


@dataclass
class ServiceReport:
    timestamp: float
    services: List[ServiceInfo] = field(default_factory=list)
    issues: List[ServiceIssue] = field(default_factory=list)


class ServiceManagerEngine41:
    """
    Service Manager Engine 4.1

    - bezpečný diagnostický modul
    - žiadne priame zásahy do Windows služieb
    - všetky akcie vykonáva VYSLANEC 4.1
    """

    def __init__(self):
        # kritické služby Windows
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

    # -------------------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------------------

    def analyze(self) -> ServiceReport:
        """
        Hlavný vstupný bod pre Runtime Core 4.0.
        """
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
        )

    # -------------------------------------------------------------------------
    # SERVICE COLLECTION
    # -------------------------------------------------------------------------

    def _collect_services(self) -> List[ServiceInfo]:
        result: List[ServiceInfo] = []

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
                continue

        return result

    # -------------------------------------------------------------------------
    # ANALYSIS HELPERS
    # -------------------------------------------------------------------------

    def _detect_stopped_critical_services(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        stopped = [s for s in services if s.is_critical and s.status != "running"]

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
                    "Navrhnúť reštart kritických služieb cez VYSLANEC 4.1.",
                    "Zobraziť používateľovi zoznam zastavených služieb.",
                ],
                related_services=[s.name for s in stopped],
            )
        )

        return issues

    def _detect_failed_services(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        failed = [s for s in services if s.status == "stopped" and not s.is_critical]

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
                    "Ponúknuť možnosť reštartu týchto služieb cez VYSLANEC 4.1.",
                ],
                related_services=[s.name for s in failed],
            )
        )

        return issues

    def _detect_audio_restart_candidate(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        audio = [s for s in services if s.name.lower() in ("audiosrv", "audiosrv")]

        if not audio:
            return issues

        svc = audio[0]
        if svc.status != "running":
            issues.append(
                ServiceIssue(
                    id="audio_service_down",
                    severity="warning",
                    title="Windows Audio nie je spustené",
                    description="Zvuk nemusí fungovať správne.",
                    suggested_actions=[
                        "Navrhnúť reštart Windows Audio cez VYSLANEC 4.1.",
                    ],
                    related_services=[svc.name],
                )
            )

        return issues

    def _detect_network_restart_candidate(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        dhcp = [s for s in services if s.name.lower() == "dhcp"]
        dns = [s for s in services if s.name.lower() == "dnscache"]

        if dhcp and dhcp[0].status != "running":
            issues.append(
                ServiceIssue(
                    id="dhcp_down",
                    severity="warning",
                    title="DHCP Client nie je spustený",
                    description="Sieť nemusí fungovať správne.",
                    suggested_actions=[
                        "Navrhnúť reštart DHCP Client cez VYSLANEC 4.1.",
                    ],
                    related_services=["Dhcp"],
                )
            )

        if dns and dns[0].status != "running":
            issues.append(
                ServiceIssue(
                    id="dns_down",
                    severity="warning",
                    title="DNS Client nie je spustený",
                    description="Môžu sa vyskytnúť problémy s internetom.",
                    suggested_actions=[
                        "Navrhnúť reštart DNS Client cez VYSLANEC 4.1.",
                    ],
                    related_services=["Dnscache"],
                )
            )

        return issues

    def _detect_windows_update_issues(self, services: List[ServiceInfo]) -> List[ServiceIssue]:
        issues: List[ServiceIssue] = []

        wu = [s for s in services if s.name.lower() == "wuauserv"]

        if wu and wu[0].status != "running":
            issues.append(
                ServiceIssue(
                    id="windows_update_down",
                    severity="info",
                    title="Windows Update nie je spustený",
                    description="Aktualizácie systému nemusia fungovať.",
                    suggested_actions=[
                        "Navrhnúť reštart Windows Update cez VYSLANEC 4.1.",
                    ],
                    related_services=["wuauserv"],
                )
            )

        return issues

    # -------------------------------------------------------------------------
    # SUMMARY FOR SYSTEM HEALTH ENGINE
    # -------------------------------------------------------------------------

    def get_service_summary(self) -> dict:
        services = self._collect_services()
        stopped = len([s for s in services if s.status != "running"])
        critical_stopped = len([s for s in services if s.is_critical and s.status != "running"])

        return {
            "total_services": len(services),
            "stopped_services": stopped,
            "critical_stopped": critical_stopped,
        }
