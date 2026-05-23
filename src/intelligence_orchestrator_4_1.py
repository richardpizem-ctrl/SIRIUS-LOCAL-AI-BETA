# intelligence_orchestrator_4_5.py
# SIRIUS LOCAL AI – Intelligence Orchestrator 4.5.0 PRO
# High-level, AI-aware orchestration layer (deterministic, safe-mode compatible, Phase‑5 ready)

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Any, Literal, Optional
import time

from system_health_engine_4_5 import SystemHealthEngine45, HealthIssue45, HealthReport45
from driver_manager_engine_4_5 import DriverManagerEngine45, DriverIssue45, DriverReport45
from task_manager_engine_4_5 import TaskManagerEngine45, TaskIssue45, TaskReport45
from service_manager_engine_4_5 import ServiceManagerEngine45, ServiceIssue45, ServiceReport45
from education_engine_4_5 import (
    EducationEngine45,
    EducationBundle45,
    ExplanationBlock45,
    IdentityType,
)
from system_agent_4_5 import (
    SystemAgent45,
    AgentAction45,
    AgentResult45,
    ActionType45,
)


Severity = Literal["info", "warning", "critical"]


# ---------------------------------------------------------
# DATA STRUCTURES (4.5.0 PRO)
# ---------------------------------------------------------

@dataclass
class PrioritizedItem45:
    id: str
    domain: str
    title: str
    description: str
    severity: Severity
    priority_score: int
    explanation: str
    suggested_actions: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OrchestrationPlan45:
    identity: IdentityType
    created_at: float
    issues: List[PrioritizedItem45]
    actions: List[AgentAction45]
    dry_run: bool
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ORCHESTRATOR 4.5.0 PRO
# ---------------------------------------------------------

class IntelligenceOrchestrator45:
    """
    Intelligence Orchestrator 4.5.0 PRO
    """

    def __init__(self, dry_run: bool = True) -> None:
        self.health_engine = SystemHealthEngine45()
        self.driver_engine = DriverManagerEngine45()
        self.task_engine = TaskManagerEngine45()
        self.service_engine = ServiceManagerEngine45()
        self.education_engine = EducationEngine45()
        self.agent = SystemAgent45(dry_run=dry_run)

        self.dry_run = dry_run
        self.safe_mode = False
        self.degraded_mode = False

        self._severity_weight = {"critical": 100, "warning": 50, "info": 10}
        self._domain_weight = {"health": 30, "drivers": 25, "tasks": 15, "services": 10}

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def build_plan(self, identity: IdentityType = "OWNER") -> OrchestrationPlan45:

        if self.safe_mode:
            return OrchestrationPlan45(
                identity=identity,
                created_at=time.time(),
                issues=[],
                actions=[],
                dry_run=self.dry_run,
                safe_mode=True,
                degraded_mode=False,
            )

        try:
            # Diagnostics
            health_report = self.health_engine.analyze()
            driver_report = self.driver_engine.analyze()
            task_report = self.task_engine.analyze()
            service_report = self.service_engine.analyze()

            # Explanations
            health_expl = self.education_engine.explain_system_health(identity, health_report)
            driver_expl = self.education_engine.explain_drivers(identity, driver_report)
            task_expl = self.education_engine.explain_tasks(identity, task_report)
            service_expl = self.education_engine.explain_services(identity, service_report)

            # Collect issues
            issues = []
            issues.extend(self._collect_health_issues(health_report, health_expl))
            issues.extend(self._collect_driver_issues(driver_report, driver_expl))
            issues.extend(self._collect_task_issues(task_report, task_expl))
            issues.extend(self._collect_service_issues(service_report, service_expl))

            # Normalize
            issues = self._normalize_and_sort_issues(issues, identity)

            # Actions
            actions = self._build_agent_actions(
                identity,
                health_report,
                driver_report,
                task_report,
                service_report,
                issues,
            )

            return OrchestrationPlan45(
                identity=identity,
                created_at=time.time(),
                issues=issues,
                actions=actions,
                dry_run=self.dry_run,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )

        except Exception:
            self.degraded_mode = True
            return OrchestrationPlan45(
                identity=identity,
                created_at=time.time(),
                issues=[],
                actions=[],
                dry_run=self.dry_run,
                safe_mode=False,
                degraded_mode=True,
            )

    # ---------------------------------------------------------
    # ISSUE COLLECTION
    # ---------------------------------------------------------

    def _collect_health_issues(self, report, bundle):
        items = []
        blocks = {b.title: b for b in bundle.blocks}

        for issue in report.issues:
            block = blocks.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, "health", issue)

            items.append(PrioritizedItem45(
                id=issue.id,
                domain="health",
                title=issue.title,
                description=issue.description,
                severity=issue.severity,
                priority_score=score,
                explanation=explanation,
                suggested_actions=issue.suggested_actions,
                metadata={"health_score": getattr(report, "health_score", None)},
            ))

        return items

    def _collect_driver_issues(self, report, bundle):
        items = []
        blocks = {b.title: b for b in bundle.blocks}

        for issue in report.issues:
            block = blocks.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, "drivers", issue)

            items.append(PrioritizedItem45(
                id=issue.id,
                domain="drivers",
                title=issue.title,
                description=issue.description,
                severity=issue.severity,
                priority_score=score,
                explanation=explanation,
                suggested_actions=issue.suggested_actions,
                metadata={
                    "related_files": getattr(issue, "related_files", []),
                    "related_devices": getattr(issue, "related_devices", []),
                },
            ))

        return items

    def _collect_task_issues(self, report, bundle):
        items = []
        blocks = {b.title: b for b in bundle.blocks}

        for issue in report.issues:
            block = blocks.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, "tasks", issue)

            items.append(PrioritizedItem45(
                id=issue.id,
                domain="tasks",
                title=issue.title,
                description=issue.description,
                severity=issue.severity,
                priority_score=score,
                explanation=explanation,
                suggested_actions=issue.suggested_actions,
                metadata={"related_pids": getattr(issue, "related_pids", [])},
            ))

        return items

    def _collect_service_issues(self, report, bundle):
        items = []
        blocks = {b.title: b for b in bundle.blocks}

        for issue in report.issues:
            block = blocks.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, "services", issue)

            items.append(PrioritizedItem45(
                id=issue.id,
                domain="services",
                title=issue.title,
                description=issue.description,
                severity=issue.severity,
                priority_score=score,
                explanation=explanation,
                suggested_actions=issue.suggested_actions,
                metadata={"related_services": getattr(issue, "related_services", [])},
            ))

        return items

    # ---------------------------------------------------------
    # PRIORITY MODEL 4.5
    # ---------------------------------------------------------

    def _compute_priority(self, severity, domain, issue):
        base = self._severity_weight.get(severity, 10)
        domain_offset = self._domain_weight.get(domain, 0)

        impact_bonus = 0
        quick_win_bonus = 0

        impact = getattr(issue, "impact", None)
        if impact == "system_stability":
            impact_bonus += 25
        elif impact == "performance":
            impact_bonus += 15
        elif impact == "security":
            impact_bonus += 30
        elif impact == "usability":
            impact_bonus += 10

        if getattr(issue, "quick_fix", False):
            quick_win_bonus += 10

        return base + domain_offset + impact_bonus + quick_win_bonus

    # ---------------------------------------------------------
    # NORMALIZATION 4.5
    # ---------------------------------------------------------

    def _normalize_and_sort_issues(self, issues, identity):
        if not issues:
            return []

        max_score = max(i.priority_score for i in issues) or 1
        adjusted = []

        for item in issues:
            score = item.priority_score / max_score * 100

            if identity == "FAMILY" and item.domain in ("tasks", "services"):
                score *= 0.7
            elif identity == "STRANGER" and item.domain != "health":
                score *= 0.4

            adjusted.append(PrioritizedItem45(
                id=item.id,
                domain=item.domain,
                title=item.title,
                description=item.description,
                severity=item.severity,
                priority_score=int(score),
                explanation=item.explanation,
                suggested_actions=item.suggested_actions,
                metadata=item.metadata,
            ))

        adjusted.sort(key=lambda x: x.priority_score, reverse=True)
        return adjusted

    # ---------------------------------------------------------
    # ACTION MAPPING (4.5 PRO)
    # ---------------------------------------------------------

    def _build_agent_actions(self, identity, health_report, driver_report, task_report, service_report, issues):
        actions = []

        for issue in driver_report.issues:
            if issue.severity in ("warning", "critical"):
                actions.append(AgentAction45(
                    id=f"install_driver_{issue.id}",
                    type="INSTALL_DRIVER",
                    label="Install missing or updated driver",
                    description=issue.description,
                    identity_required="OWNER",
                    payload={
                        "related_files": getattr(issue, "related_files", []),
                        "related_devices": getattr(issue, "related_devices", []),
                    },
                ))

        for issue in task_report.issues:
            if getattr(issue, "id", "") == "explorer_restart_suggestion":
                actions.append(AgentAction45(
                    id="restart_explorer",
                    type="RESTART_EXPLORER",
                    label="Restart Windows Explorer",
                    description=issue.description,
                    identity_required="OWNER",
                    payload={},
                ))

            if getattr(issue, "id", "") in ("high_cpu_processes", "high_ram_processes"):
                for pid in getattr(issue, "related_pids", []):
                    actions.append(AgentAction45(
                        id=f"kill_process_{pid}",
                        type="KILL_PROCESS",
                        label=f"Terminate process {pid}",
                        description=issue.description,
                        identity_required="OWNER",
                        payload={"pid": pid},
                    ))

        for issue in service_report.issues:
            for svc in getattr(issue, "related_services", []):
                actions.append(AgentAction45(
                    id=f"restart_service_{svc}",
                    type="RESTART_SERVICE",
                    label=f"Restart service {svc}",
                    description=issue.description,
                    identity_required="OWNER",
                    payload={"service_name": svc},
                ))

        for issue in health_report.issues:
            if getattr(issue, "id", "") == "disk_cleanup_recommended":
                actions.append(AgentAction45(
                    id="run_disk_cleanup",
                    type="RUN_DISK_CLEANUP",
                    label="Run disk cleanup",
                    description=issue.description,
                    identity_required="OWNER",
                    payload={},
                ))

        return actions

    # ---------------------------------------------------------
    # SAFE MODE
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
