"""
System Health Engine 4.1
------------------------

Continuous diagnostic and optimization engine for SIRIUS LOCAL AI 4.1.0.

Responsibilities:
- monitor CPU / RAM / DISK / NETWORK
- detect frozen processes
- detect bottlenecks
- detect failing services (via integration hooks)
- detect missing/corrupted drivers (via integration hooks)
- compute PC Health Score
- generate safe optimization / repair suggestions (to be executed via VYSLANEC)

This module:
- NEVYKONÁVA žiadne priame systémové zmeny
- len ANALYZUJE a NAVRHUJE
- všetky akcie musia ísť cez VYSLANEC 4.1
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Literal
import time
import psutil  # predpoklad: bude pridané do dependencies


HealthSeverity = Literal["info", "warning", "critical"]


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
    category: str  # "cpu", "ram", "disk", "network", "process", "service", "driver", ...
    severity: HealthSeverity
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    related_pids: List[int] = field(default_factory=list)


@dataclass
class HealthReport:
    snapshot: MetricSnapshot
    health_score: int  # 0–100
    issues: List[HealthIssue] = field(default_factory=list)


class SystemHealthEngine41:
    """
    System Health Engine 4.1

    - volá sa z Runtime Core 4.0 / Workflow Engine 4.0
    - nepozná GUI, len vracia štruktúry
    - nepozná VYSLANEC implementačne, len generuje návrhy akcií
    """

    def __init__(self) -> None:
        self._history: List[MetricSnapshot] = []

    # -------------------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------------------

    def collect_snapshot(self) -> MetricSnapshot:
        """
        Odčíta aktuálny stav systému a vráti snapshot.
        Nevykonáva žiadne zmeny.
        """
        cpu = psutil.cpu_percent(interval=0.5)
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

    def analyze(self) -> HealthReport:
        """
        Hlavný vstupný bod:
        - zoberie aktuálny snapshot
        - analyzuje stav
        - vygeneruje health score + issues
        """
        snapshot = self.collect_snapshot()
        issues: List[HealthIssue] = []

        issues.extend(self._analyze_cpu(snapshot))
        issues.extend(self._analyze_ram(snapshot))
        issues.extend(self._analyze_disk(snapshot))
        # network zatiaľ len placeholder
        # issues.extend(self._analyze_network(snapshot))

        score = self._compute_health_score(snapshot, issues)

        return HealthReport(
            snapshot=snapshot,
            health_score=score,
            issues=issues,
        )

    # -------------------------------------------------------------------------
    # INTERNAL ANALYSIS HELPERS
    # -------------------------------------------------------------------------

    def _analyze_cpu(self, snapshot: MetricSnapshot) -> List[HealthIssue]:
        issues: List[HealthIssue] = []

        if snapshot.cpu_percent > 90:
            issues.append(
                HealthIssue(
                    id="cpu_high_usage",
                    category="cpu",
                    severity="critical",
                    title="Vysoké vyťaženie procesora",
                    description=(
                        f"Procesor je aktuálne vyťažený na {snapshot.cpu_percent:.1f} %. "
                        "To môže spôsobovať spomalenie systému, trhanie animácií a oneskorené reakcie."
                    ),
                    suggested_actions=[
                        "Identifikovať procesy s najvyšším CPU zaťažením.",
                        "Navrhnúť ukončenie nepotrebných procesov (cez VYSLANEC).",
                        "Skontrolovať, či neprebieha náročné pozadie (indexovanie, update, antivírus).",
                    ],
                )
            )
        elif snapshot.cpu_percent > 75:
            issues.append(
                HealthIssue(
                    id="cpu_medium_usage",
                    category="cpu",
                    severity="warning",
                    title="Zvýšené vyťaženie procesora",
                    description=(
                        f"Procesor je aktuálne vyťažený na {snapshot.cpu_percent:.1f} %. "
                        "Systém môže byť mierne spomalený pri náročnejších úlohách."
                    ),
                    suggested_actions=[
                        "Skontrolovať procesy s vyšším CPU zaťažením.",
                        "Navrhnúť optimalizáciu aplikácií bežiacich na pozadí.",
                    ],
                )
            )

        return issues

    def _analyze_ram(self, snapshot: MetricSnapshot) -> List[HealthIssue]:
        issues: List[HealthIssue] = []

        if snapshot.ram_percent > 90:
            issues.append(
                HealthIssue(
                    id="ram_critical",
                    category="ram",
                    severity="critical",
                    title="Nedostatok pamäte RAM",
                    description=(
                        f"Využitie pamäte RAM je {snapshot.ram_percent:.1f} %. "
                        "Systém môže výrazne swapovať na disk, čo spôsobuje extrémne spomalenie."
                    ),
                    suggested_actions=[
                        "Identifikovať aplikácie s najvyššou spotrebou RAM.",
                        "Navrhnúť zatvorenie nepotrebných aplikácií.",
                        "Zvážiť reštart systému, ak je stav dlhodobo kritický.",
                    ],
                )
            )
        elif snapshot.ram_percent > 80:
            issues.append(
                HealthIssue(
                    id="ram_high",
                    category="ram",
                    severity="warning",
                    title="Vysoké využitie pamäte RAM",
                    description=(
                        f"Využitie pamäte RAM je {snapshot.ram_percent:.1f} %. "
                        "Pri spúšťaní ďalších aplikácií môže dôjsť k spomaleniu."
                    ),
                    suggested_actions=[
                        "Navrhnúť zatvorenie aplikácií bežiacich na pozadí.",
                        "Skontrolovať, či nebežia zbytočné procesy pri štarte systému.",
                    ],
                )
            )

        return issues

    def _analyze_disk(self, snapshot: MetricSnapshot) -> List[HealthIssue]:
        issues: List[HealthIssue] = []

        if snapshot.disk_percent > 95:
            issues.append(
                HealthIssue(
                    id="disk_full",
                    category="disk",
                    severity="critical",
                    title="Disk je takmer plný",
                    description=(
                        f"Disk je zaplnený na {snapshot.disk_percent:.1f} %. "
                        "To môže spôsobovať chyby pri ukladaní súborov a výrazné spomalenie systému."
                    ),
                    suggested_actions=[
                        "Navrhnúť vyčistenie dočasných súborov.",
                        "Navrhnúť presun veľkých súborov na iný disk alebo externé úložisko.",
                        "Skontrolovať priečinky Downloads, Videos, Games.",
                    ],
                )
            )
        elif snapshot.disk_percent > 85:
            issues.append(
                HealthIssue(
                    id="disk_high",
                    category="disk",
                    severity="warning",
                    title="Disk je výrazne zaplnený",
                    description=(
                        f"Disk je zaplnený na {snapshot.disk_percent:.1f} %. "
                        "Systém môže mať menej priestoru pre dočasné súbory a aktualizácie."
                    ),
                    suggested_actions=[
                        "Navrhnúť základné čistenie disku.",
                        "Identifikovať najväčšie priečinky a súbory.",
                    ],
                )
            )

        return issues

    def _compute_health_score(
        self,
        snapshot: MetricSnapshot,
        issues: List[HealthIssue],
    ) -> int:
        """
        Jednoduchý prvý model health score (0–100).
        Neskôr sa môže nahradiť sofistikovanejším algoritmom.
        """
        score = 100

        # penalizácia podľa CPU
        if snapshot.cpu_percent > 90:
            score -= 25
        elif snapshot.cpu_percent > 75:
            score -= 10

        # penalizácia podľa RAM
        if snapshot.ram_percent > 90:
            score -= 25
        elif snapshot.ram_percent > 80:
            score -= 10

        # penalizácia podľa disku
        if snapshot.disk_percent > 95:
            score -= 25
        elif snapshot.disk_percent > 85:
            score -= 10

        # penalizácia podľa počtu issues
        score -= len(issues) * 2

        if score < 0:
            score = 0
        if score > 100:
            score = 100

        return score

    # -------------------------------------------------------------------------
    # INTEGRATION HOOKS (PLACEHOLDERS)
    # -------------------------------------------------------------------------

    def integrate_process_inspector(self, process_data: Dict) -> None:
        """
        Hook pre Task Manager Engine 4.1:
        - sem môžeš neskôr napojiť detailné info o procesoch
        - System Health Engine ich môže použiť pri generovaní issues
        """
        # TODO: implementovať podľa štruktúry Task Manager Engine
        pass

    def integrate_service_inspector(self, service_data: Dict) -> None:
        """
        Hook pre Service Manager Engine 4.1.
        """
        # TODO: implementovať podľa štruktúry Service Manager Engine
        pass

    def integrate_driver_inspector(self, driver_data: Dict) -> None:
        """
        Hook pre Driver Manager Engine 4.1.
        """
        # TODO: implementovať podľa štruktúry Driver Manager Engine
        pass
