# task_manager_engine_4_4.py
# SIRIUS LOCAL AI – Task Manager Engine 4.4.0 PRO
# Deterministic, sandboxed process diagnostics (Phase‑5 ready)

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Literal, Dict, Any
import time
import psutil


TaskSeverity44 = Literal["info", "warning", "critical"]


# ---------------------------------------------------------
# DATA STRUCTURES (4.4.0 PRO)
# ---------------------------------------------------------

@dataclass
class TaskProcessInfo44:
    pid: int
    name: str
    cpu_percent: float
    ram_percent: float
    is_system: bool
    is_critical: bool
    status: str


@dataclass
class TaskIssue44:
    id: str
    severity: TaskSeverity44
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    related_pids: List[int] = field(default_factory=list)
    impact: Optional[str] = None
    quick_fix: bool = False


@dataclass
class TaskReport44:
    timestamp: float
    processes: List[TaskProcessInfo44] = field(default_factory=list)
    issues: List[TaskIssue44] = field(default_factory=list)
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ENGINE 4.4.0 PRO
# ---------------------------------------------------------

class TaskManagerEngine44:
    """
    Task Manager Engine 4.4.0 PRO

    Responsibilities:
        - analyze running processes
        - detect high CPU/RAM usage
        - detect frozen processes
        - detect explorer restart candidates
        - generate safe suggestions (executed via SystemAgent44)
        - deterministic, offline, sandbox-friendly
        - safe-mode and degraded-mode aware
        - Phase‑5 ready
    """

    def __init__(self) -> None:
        self.safe_mode = False
        self.degraded_mode = False

        self._critical_names = {
            "System",
            "Registry",
            "smss.exe",
            "csrss.exe",
            "wininit.exe",
            "services.exe",
            "lsass.exe",
            "winlogon.exe",
            "explorer.exe",
        }

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def analyze(self) -> TaskReport44:

        if self.safe_mode:
            return TaskReport44(
                timestamp=time.time(),
                processes=[],
                issues=[],
                safe_mode=True,
                degraded_mode=False,
            )

        try:
            processes = self._collect_processes()
            issues: List[TaskIssue44] = []

            issues.extend(self._detect_high_cpu_processes(processes))
            issues.extend(self._detect_high_ram_processes(processes))
            issues.extend(self._detect_not_responding(processes))
            issues.extend(self._detect_explorer_restart_candidate(processes))

            return TaskReport44(
                timestamp=time.time(),
                processes=processes,
                issues=issues,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )

        except Exception:
            self.degraded_mode = True
            return TaskReport44(
                timestamp=time.time(),
                processes=[],
                issues=[],
                safe_mode=False,
                degraded_mode=True,
            )

    # ---------------------------------------------------------
    # PROCESS COLLECTION (SANDBOXED)
    # ---------------------------------------------------------

    def _collect_processes(self) -> List[TaskProcessInfo44]:
        result: List[TaskProcessInfo44] = []

        try:
            # First pass: initialize CPU counters
            for p in psutil.process_iter(["pid", "name"]):
                try:
                    p.cpu_percent(interval=None)
                except Exception:
                    continue

            time.sleep(0.25)

            for p in psutil.process_iter(["pid", "name", "memory_percent", "status", "username"]):
                try:
                    name = p.info.get("name") or f"pid_{p.pid}"
                    cpu = p.cpu_percent(interval=None)
                    ram = p.info.get("memory_percent") or 0.0
                    status = p.info.get("status") or "unknown"
                    username = p.info.get("username") or ""

                    is_system = username.lower().startswith("nt authority") or username.lower().startswith("system")
                    is_critical = name.lower() in {n.lower() for n in self._critical_names}

                    result.append(
                        TaskProcessInfo44(
                            pid=p.pid,
                            name=name,
                            cpu_percent=cpu,
                            ram_percent=ram,
                            is_system=is_system,
                            is_critical=is_critical,
                            status=status,
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

    def _detect_high_cpu_processes(self, processes: List[TaskProcessInfo44]) -> List[TaskIssue44]:
        issues: List[TaskIssue44] = []
        high_cpu = [p for p in processes if p.cpu_percent > 25.0 and not p.is_critical]

        if not high_cpu:
            return issues

        top = sorted(high_cpu, key=lambda p: p.cpu_percent, reverse=True)[:10]

        issues.append(
            TaskIssue44(
                id="high_cpu_processes",
                severity="warning",
                title="Procesy s vysokým CPU zaťažením",
                description="Niektoré procesy výrazne zaťažujú procesor.",
                suggested_actions=[
                    "Zobraziť procesy s najvyšším CPU zaťažením.",
                    "Navrhnúť ukončenie nepotrebných procesov.",
                ],
                related_pids=[p.pid for p in top],
                impact="performance",
                quick_fix=True,
            )
        )

        return issues

    def _detect_high_ram_processes(self, processes: List[TaskProcessInfo44]) -> List[TaskIssue44]:
        issues: List[TaskIssue44] = []
        high_ram = [p for p in processes if p.ram_percent > 5.0 and not p.is_critical]

        if not high_ram:
            return issues

        top = sorted(high_ram, key=lambda p: p.ram_percent, reverse=True)[:10]

        issues.append(
            TaskIssue44(
                id="high_ram_processes",
                severity="warning",
                title="Procesy s vysokou spotrebou RAM",
                description="Niektoré procesy používajú veľké množstvo pamäte RAM.",
                suggested_actions=[
                    "Zobraziť procesy s najvyššou spotrebou RAM.",
                    "Navrhnúť zatvorenie nepotrebných aplikácií.",
                ],
                related_pids=[p.pid for p in top],
                impact="performance",
                quick_fix=True,
            )
        )

        return issues

    def _detect_not_responding(self, processes: List[TaskProcessInfo44]) -> List[TaskIssue44]:
        issues: List[TaskIssue44] = []
        frozen = [p for p in processes if p.status.lower() == "not responding" and not p.is_critical]

        if not frozen:
            return issues

        issues.append(
            TaskIssue44(
                id="not_responding_processes",
                severity="warning",
                title="Neodpovedajúce procesy",
                description="Niektoré aplikácie neodpovedajú.",
                suggested_actions=[
                    "Ponúknuť ukončenie neodpovedajúcich aplikácií.",
                ],
                related_pids=[p.pid for p in frozen],
                impact="stability",
                quick_fix=True,
            )
        )

        return issues

    def _detect_explorer_restart_candidate(self, processes: List[TaskProcessInfo44]) -> List[TaskIssue44]:
        issues: List[TaskIssue44] = []
        explorer = [p for p in processes if p.name.lower() == "explorer.exe"]

        if not explorer:
            return issues

        exp = explorer[0]
        if exp.cpu_percent > 20.0 or exp.ram_percent > 5.0:
            issues.append(
                TaskIssue44(
                    id="explorer_restart_suggestion",
                    severity="info",
                    title="Možný reštart Prieskumníka (explorer.exe)",
                    description="Prieskumník Windows používa viac zdrojov, než je bežné.",
                    suggested_actions=[
                        "Ponúknuť bezpečný reštart explorer.exe.",
                    ],
                    related_pids=[exp.pid],
                    impact="usability",
                    quick_fix=True,
                )
            )

        return issues

    # ---------------------------------------------------------
    # SUMMARY FOR SYSTEM HEALTH ENGINE 4.4
    # ---------------------------------------------------------

    def get_task_summary(self) -> Dict[str, Any]:
        try:
            processes = self._collect_processes()
            high_cpu = len([p for p in processes if p.cpu_percent > 25.0 and not p.is_critical])
            high_ram = len([p for p in processes if p.ram_percent > 5.0 and not p.is_critical])

            return {
                "total_processes": len(processes),
                "high_cpu_processes": high_cpu,
                "high_ram_processes": high_ram,
                "safe_mode": self.safe_mode,
                "degraded_mode": self.degraded_mode,
            }
        except Exception:
            self.degraded_mode = True
            return {
                "total_processes": 0,
                "high_cpu_processes": 0,
                "high_ram_processes": 0,
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
