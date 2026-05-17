# system_health_engine_4_3.py
# SIRIUS LOCAL AI – System Health Engine 4.3.x
# Deterministic, safe-mode compatible, AI-aware diagnostic engine

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Literal
import time
import psutil


HealthSeverity = Literal["info", "warning", "critical"]


# ---------------------------------------------------------
# DATA STRUCTURES
# ---------------------------------------------------------

@dataclass
class MetricSnapshot:
    timestamp: float
    cpu_percent: float
    ram_percent: float
    disk_percent: float
    net_bytes_sent: int
    net_bytes_recv: int


@dataclass
class HealthIssue:
    id: str
    category: str
    severity: HealthSeverity
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    related_pids: List[int] = field(default_factory=list)
    impact: Optional[str] = None       # "performance" | "stability" | "security" | ...
    quick_fix: bool = False            # hint for orchestrator


@dataclass
class HealthReport:
    snapshot: MetricSnapshot
    health_score: int
    issues: List[HealthIssue] = field(default_factory=list)
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ENGINE
# ---------------------------------------------------------

class SystemHealthEngine43:
    """
    System Health Engine 4.3.x

    Responsibilities:
        - monitor CPU / RAM / DISK / NETWORK
        - detect bottlenecks, frozen processes, resource spikes
        - compute PC Health Score (AI-aware)
        - generate safe optimization suggestions
        - deterministic, offline, sandbox-friendly
        - safe-mode and degraded-mode aware
    """

    def __init__(self) -> None:
        self._history: List[MetricSnapshot] = []
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def collect_snapshot(self) -> MetricSnapshot:
        """
        Collect current system metrics.
        Deterministic and safe.
        """
        try:
            cpu = psutil.cpu_percent(interval=0.3)
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage("/").percent
            net = psutil.net_io_counters()

            snapshot = MetricSnapshot(
                timestamp=time.time(),
                cpu_percent=cpu,
                ram_percent=ram,
                disk_percent=disk,
                net_bytes_sent=net.bytes_sent,
                net_bytes_recv=net.bytes_recv,
            )
            self._history.append(snapshot)
            return snapshot

        except Exception:
            self.degraded_mode = True
            return MetricSnapshot(
                timestamp=time.time(),
                cpu_percent=0.0,
                ram_percent=0.0,
                disk_percent=0.0,
                net_bytes_sent=0,
                net_bytes_recv=0,
            )

    def analyze(self) -> HealthReport:
        """
        Main entry point for Runtime Manager 4.3.x.
        Always returns a valid HealthReport.
        """

        if self.safe_mode:
            snapshot = self.collect_snapshot()
            return HealthReport(
                snapshot=snapshot,
                health_score=100,
                issues=[],
                safe_mode=True,
                degraded_mode=False,
            )

        try:
            snapshot = self.collect_snapshot()
            issues: List[HealthIssue] = []

            issues.extend(self._analyze_cpu(snapshot))
            issues.extend(self._analyze_ram(snapshot))
            issues.extend(self._analyze_disk(snapshot))
            issues.extend(self._analyze_network(snapshot))

            score = self._compute_health_score(snapshot, issues)

            return HealthReport(
                snapshot=snapshot,
                health_score=score,
                issues=issues,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )

        except Exception:
            self.degraded_mode = True
            snapshot = self.collect_snapshot()
            return HealthReport(
                snapshot=snapshot,
                health_score=50,
                issues=[],
                safe_mode=False,
                degraded_mode=True,
            )

    # ---------------------------------------------------------
    # INTERNAL ANALYSIS HELPERS
    # ---------------------------------------------------------

    def _analyze_cpu(self, snapshot: MetricSnapshot) -> List[HealthIssue]:
        issues: List[HealthIssue] = []
        cpu = snapshot.cpu_percent

        if cpu > 90:
            issues.append(
                HealthIssue(
                    id="cpu_high_usage",
                    category="cpu",
                    severity="critical",
                    title="Vysoké vyťaženie procesora",
                    description=(
                        f"Procesor je vyťažený na {cpu:.1f} %. "
                        "Systém môže byť výrazne spomalený."
                    ),
                    suggested_actions=[
                        "Identifikovať procesy s najvyšším CPU zaťažením.",
                        "Navrhnúť ukončenie nepotrebných procesov.",
                    ],
                    impact="performance",
                    quick_fix=True,
                )
            )
        elif cpu > 75:
            issues.append(
                HealthIssue(
                    id="cpu_medium_usage",
                    category="cpu",
                    severity="warning",
                    title="Zvýšené vyťaženie procesora",
                    description=(
                        f"Procesor je vyťažený na {cpu:.1f} %. "
                        "Systém môže byť mierne spomalený."
                    ),
                    suggested_actions=[
                        "Skontrolovať procesy s vyšším CPU zaťažením.",
                    ],
                    impact="performance",
                )
            )

        return issues

    def _analyze_ram(self, snapshot: MetricSnapshot) -> List[HealthIssue]:
        issues: List[HealthIssue] = []
        ram = snapshot.ram_percent

        if ram > 90:
            issues.append(
                HealthIssue(
                    id="ram_critical",
                    category="ram",
                    severity="critical",
                    title="Nedostatok pamäte RAM",
                    description=(
                        f"RAM je využitá na {ram:.1f} %. "
                        "Systém môže výrazne swapovať."
                    ),
                    suggested_actions=[
                        "Identifikovať aplikácie s najvyššou spotrebou RAM.",
                        "Navrhnúť zatvorenie nepotrebných aplikácií.",
                    ],
                    impact="performance",
                    quick_fix=True,
                )
            )
        elif ram > 80:
            issues.append(
                HealthIssue(
                    id="ram_high",
                    category="ram",
                    severity="warning",
                    title="Vysoké využitie RAM",
                    description=(
                        f"RAM je využitá na {ram:.1f} %. "
                        "Môže dôjsť k spomaleniu."
                    ),
                    suggested_actions=[
                        "Navrhnúť zatvorenie aplikácií bežiacich na pozadí.",
                    ],
                    impact="performance",
                )
            )

        return issues

    def _analyze_disk(self, snapshot: MetricSnapshot) -> List[HealthIssue]:
        issues: List[HealthIssue] = []
        disk = snapshot.disk_percent

        if disk > 95:
            issues.append(
                HealthIssue(
                    id="disk_full",
                    category="disk",
                    severity="critical",
                    title="Disk je takmer plný",
                    description=(
                        f"Disk je zaplnený na {disk:.1f} %. "
                        "To môže spôsobovať chyby a spomalenie."
                    ),
                    suggested_actions=[
                        "Vyčistiť dočasné súbory.",
                        "Presunúť veľké súbory na iný disk.",
                    ],
                    impact="stability",
                    quick_fix=True,
                )
            )
        elif disk > 85:
            issues.append(
                HealthIssue(
                    id="disk_high",
                    category="disk",
                    severity="warning",
                    title="Disk je výrazne zaplnený",
                    description=(
                        f"Disk je zaplnený na {disk:.1f} %. "
                        "Systém môže mať menej priestoru pre aktualizácie."
                    ),
                    suggested_actions=[
                        "Navrhnúť základné čistenie disku.",
                    ],
                    impact="usability",
                )
            )

        return issues

    def _analyze_network(self, snapshot: MetricSnapshot) -> List[HealthIssue]:
        """
        Basic network anomaly detection.
        """
        issues: List[HealthIssue] = []

        # Simple heuristic: extremely low traffic for long periods
        if len(self._history) > 5:
            last = self._history[-1]
            prev = self._history[-5]

            delta_sent = last.net_bytes_sent - prev.net_bytes_sent
            delta_recv = last.net_bytes_recv - prev.net_bytes_recv

            if delta_sent < 1000 and delta_recv < 1000:
                issues.append(
                    HealthIssue(
                        id="network_low_activity",
                        category="network",
                        severity="info",
                        title="Nízka sieťová aktivita",
                        description="Sieťová aktivita je minimálna.",
                        suggested_actions=[
                            "Skontrolovať pripojenie k internetu.",
                        ],
                        impact="usability",
                    )
                )

        return issues

    # ---------------------------------------------------------
    # HEALTH SCORE (AI-AWARE)
    # ---------------------------------------------------------

    def _compute_health_score(
        self,
        snapshot: MetricSnapshot,
        issues: List[HealthIssue],
    ) -> int:
        """
        AI-aware scoring:
        - CPU / RAM / DISK penalties
        - issue count penalty
        - impact-based penalty
        """

        score = 100

        # CPU
        if snapshot.cpu_percent > 90:
            score -= 25
        elif snapshot.cpu_percent > 75:
            score -= 10

        # RAM
        if snapshot.ram_percent > 90:
            score -= 25
        elif snapshot.ram_percent > 80:
            score -= 10

        # DISK
        if snapshot.disk_percent > 95:
            score -= 25
        elif snapshot.disk_percent > 85:
            score -= 10

        # Issues
        for issue in issues:
            if issue.severity == "critical":
                score -= 10
            elif issue.severity == "warning":
                score -= 5
            else:
                score -= 1

        return max(0, min(100, score))

    # ---------------------------------------------------------
    # SAFE-MODE CONTROL
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
