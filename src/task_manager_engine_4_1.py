"""
Task Manager Engine 4.1
-----------------------

Safe process-level diagnostics module for SIRIUS LOCAL AI v4.1.0.

Účel:
- analyzovať bežiace procesy
- detegovať procesy s vysokým CPU/RAM zaťažením
- detegovať neodpovedajúce procesy
- navrhovať bezpečné akcie (reštart Explorer, ukončenie nepotrebných procesov)
- poskytovať dáta pre System Health Engine 4.1 a VYSLANEC 4.1

Tento modul:
- NEUKONČUJE procesy priamo
- NEMENÍ systém
- len analyzuje a navrhuje akcie, ktoré má vykonať VYSLANEC 4.1
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Literal
import time
import psutil
import os


TaskSeverity = Literal["info", "warning", "critical"]


@dataclass
class TaskProcessInfo:
    pid: int
    name: str
    cpu_percent: float
    ram_percent: float
    is_system: bool
    is_critical: bool
    status: str


@dataclass
class TaskIssue:
    id: str
    severity: TaskSeverity
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    related_pids: List[int] = field(default_factory=list)


@dataclass
class TaskReport:
    timestamp: float
    processes: List[TaskProcessInfo] = field(default_factory=list)
    issues: List[TaskIssue] = field(default_factory=list)


class TaskManagerEngine41:
    """
    Task Manager Engine 4.1

    - bezpečný diagnostický modul
    - žiadne priame ukončovanie procesov
    - všetky akcie musia ísť cez VYSLANEC 4.1
    """

    def __init__(self) -> None:
        self._critical_names = {
            "System",
            "Registry",
            "smss.exe",
            "csrss.exe",
            "wininit.exe",
            "services.exe",
            "lsass.exe",
            "winlogon.exe",
            "explorer.exe",  # špeciálny prípad – reštart, nie kill
        }

    # -------------------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------------------

    def analyze(self) -> TaskReport:
        """
        Hlavný vstupný bod pre Runtime Core 4.0.
        """
        processes = self._collect_processes()
        issues: List[TaskIssue] = []

        issues.extend(self._detect_high_cpu_processes(processes))
        issues.extend(self._detect_high_ram_processes(processes))
        issues.extend(self._detect_not_responding(processes))
        issues.extend(self._detect_explorer_restart_candidate(processes))

        return TaskReport(
            timestamp=time.time(),
            processes=processes,
            issues=issues,
        )

    # -------------------------------------------------------------------------
    # PROCESS COLLECTION
    # -------------------------------------------------------------------------

    def _collect_processes(self) -> List[TaskProcessInfo]:
        result: List[TaskProcessInfo] = []

        # prvé volanie na inicializáciu CPU percent
        for p in psutil.process_iter(["pid", "name"]):
            try:
                p.cpu_percent(interval=None)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        # krátka pauza na reálne CPU percentá
        time.sleep(0.3)

        for p in psutil.process_iter(["pid", "name", "memory_percent", "status", "username"]):
            try:
                name = p.info.get("name") or f"pid_{p.pid}"
                cpu = p.cpu_percent(interval=None)
                ram = p.info.get("memory_percent") or 0.0
                status = p.info.get("status") or "unknown"
                username = p.info.get("username") or ""

                is_system = username.lower().startswith("nt authority") or username.lower().startswith("system")
                is_critical = name in self._critical_names

                result.append(
                    TaskProcessInfo(
                        pid=p.pid,
                        name=name,
                        cpu_percent=cpu,
                        ram_percent=ram,
                        is_system=is_system,
                        is_critical=is_critical,
                        status=status,
                    )
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        return result

    # -------------------------------------------------------------------------
    # ANALYSIS HELPERS
    # -------------------------------------------------------------------------

    def _detect_high_cpu_processes(self, processes: List[TaskProcessInfo]) -> List[TaskIssue]:
        issues: List[TaskIssue] = []
        high_cpu = [p for p in processes if p.cpu_percent > 25.0 and not p.is_critical]

        if not high_cpu:
            return issues

        high_cpu_sorted = sorted(high_cpu, key=lambda p: p.cpu_percent, reverse=True)[:10]

        issues.append(
            TaskIssue(
                id="high_cpu_processes",
                severity="warning",
                title="Procesy s vysokým CPU zaťažením",
                description=(
                    "Niektoré procesy výrazne zaťažujú procesor. "
                    "To môže spôsobovať spomalenie systému a trhanie animácií."
                ),
                suggested_actions=[
                    "Zobraziť používateľovi zoznam procesov s najvyšším CPU zaťažením.",
                    "Navrhnúť ukončenie nepotrebných procesov cez VYSLANEC 4.1.",
                    "Skontrolovať, či nejde o hry, editory videa alebo iné náročné aplikácie.",
                ],
                related_pids=[p.pid for p in high_cpu_sorted],
            )
        )

        return issues

    def _detect_high_ram_processes(self, processes: List[TaskProcessInfo]) -> List[TaskIssue]:
        issues: List[TaskIssue] = []
        high_ram = [p for p in processes if p.ram_percent > 5.0 and not p.is_critical]

        if not high_ram:
            return issues

        high_ram_sorted = sorted(high_ram, key=lambda p: p.ram_percent, reverse=True)[:10]

        issues.append(
            TaskIssue(
                id="high_ram_processes",
                severity="warning",
                title="Procesy s vysokou spotrebou RAM",
                description=(
                    "Niektoré procesy používajú veľké množstvo pamäte RAM. "
                    "Pri nedostatku pamäte môže systém začať výrazne spomaľovať."
                ),
                suggested_actions=[
                    "Zobraziť používateľovi procesy s najvyššou spotrebou RAM.",
                    "Navrhnúť zatvorenie aplikácií, ktoré nie sú aktuálne potrebné.",
                ],
                related_pids=[p.pid for p in high_ram_sorted],
            )
        )

        return issues

    def _detect_not_responding(self, processes: List[TaskProcessInfo]) -> List[TaskIssue]:
        """
        Jednoduchá heuristika – procesy v stave 'not responding' (ak OS reportuje).
        """
        issues: List[TaskIssue] = []
        frozen = [p for p in processes if p.status.lower() == "not responding" and not p.is_critical]

        if not frozen:
            return issues

        issues.append(
            TaskIssue(
                id="not_responding_processes",
                severity="warning",
                title="Neodpovedajúce procesy",
                description=(
                    "Niektoré aplikácie neodpovedajú. "
                    "Môžu byť zamrznuté alebo čakať na operáciu, ktorá trvá príliš dlho."
                ),
                suggested_actions=[
                    "Ponúknuť možnosť ukončiť neodpovedajúce aplikácie cez VYSLANEC 4.1.",
                    "Navrhnúť uloženie práce v iných aplikáciách pred zásahom.",
                ],
                related_pids=[p.pid for p in frozen],
            )
        )

        return issues

    def _detect_explorer_restart_candidate(self, processes: List[TaskProcessInfo]) -> List[TaskIssue]:
        """
        Deteguje, či beží explorer.exe a či je vhodný kandidát na reštart.
        (Nerieši priamo reštart – to je úloha VYSLANEC 4.1)
        """
        issues: List[TaskIssue] = []
        explorer = [p for p in processes if p.name.lower() == "explorer.exe"]

        if not explorer:
            return issues

        # jednoduchá heuristika – ak explorer žerie veľa RAM alebo CPU
        exp = explorer[0]
        if exp.cpu_percent > 20.0 or exp.ram_percent > 5.0:
            issues.append(
                TaskIssue(
                    id="explorer_restart_suggestion",
                    severity="info",
                    title="Možný reštart Prieskumníka (explorer.exe)",
                    description=(
                        "Prieskumník Windows (explorer.exe) používa viac zdrojov, než je bežné. "
                        "Reštart môže obnoviť stabilitu panela úloh a okien."
                    ),
                    suggested_actions=[
                        "Ponúknuť bezpečný reštart explorer.exe cez VYSLANEC 4.1.",
                        "Upozorniť používateľa, že na chvíľu zmizne panel úloh a okná.",
                    ],
                    related_pids=[exp.pid],
                )
            )

        return issues

    # -------------------------------------------------------------------------
    # SUMMARY FOR SYSTEM HEALTH ENGINE
    # -------------------------------------------------------------------------

    def get_task_summary(self) -> dict:
        """
        Poskytne System Health Engine 4.1 základné info o procesoch.
        """
        processes = self._collect_processes()
        high_cpu = len([p for p in processes if p.cpu_percent > 25.0 and not p.is_critical])
        high_ram = len([p for p in processes if p.ram_percent > 5.0 and not p.is_critical])

        return {
            "total_processes": len(processes),
            "high_cpu_processes": high_cpu,
            "high_ram_processes": high_ram,
        }
