"""
Intelligence Orchestrator 4.1
-----------------------------

High-level intelligence layer for SIRIUS LOCAL AI v4.1.0.

Purpose:
- run all 4.1 diagnostic engines as a single pipeline
- aggregate and prioritize issues across health / drivers / tasks / services
- attach human-readable explanations from Education Engine 4.1
- prepare a prioritized action plan for System Agent 4.1
- optionally simulate execution via System Agent (dry-run by default)

This module:
- DOES NOT perform any direct OS operations
- delegates all system-changing actions to SystemAgent41
- is deterministic, offline, and fully isolated
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Any, Literal
import time

from system_health_engine_4_1 import SystemHealthEngine41, HealthIssue, HealthReport
from driver_manager_engine_4_1 import DriverManagerEngine41, DriverIssue, DriverReport
from task_manager_engine_4_1 import TaskManagerEngine41, TaskIssue, TaskReport
from service_manager_engine_4_1 import ServiceManagerEngine41, ServiceIssue, ServiceReport
from education_engine_4_1 import (
    EducationEngine41,
    EducationBundle,
    ExplanationBlock,
    IdentityType,
)
from system_agent_4_1 import SystemAgent41, AgentAction, AgentResult, ActionType


Severity = Literal["info", "warning", "critical"]


@dataclass
class PrioritizedItem:
    """
    Unified representation of a problem across all diagnostic domains.
    """
    id: str
    domain: str  # "health" | "drivers" | "tasks" | "services"
    title: str
    description: str
    severity: Severity
    priority_score: int
    explanation: str
    suggested_actions: List[str] = field(default_factory=list)


@dataclass
class OrchestrationPlan:
    """
    Final orchestration result:
    - prioritized issues
    - agent actions (not necessarily executed)
    - metadata
    """
    identity: IdentityType
    created_at: float
    issues: List[PrioritizedItem]
    actions: List[AgentAction]
    dry_run: bool


class IntelligenceOrchestrator41:
    """
    Intelligence Orchestrator 4.1

    - coordinates all 4.1 diagnostic engines
    - aggregates and prioritizes issues
    - prepares actions for SystemAgent41
    - does not perform direct OS operations
    """

    def __init__(self, dry_run: bool = True) -> None:
        # Engines
        self.health_engine = SystemHealthEngine41()
        self.driver_engine = DriverManagerEngine41()
        self.task_engine = TaskManagerEngine41()
        self.service_engine = ServiceManagerEngine41()
        self.education_engine = EducationEngine41()
        self.agent = SystemAgent41(dry_run=dry_run)

        self.dry_run = dry_run

        # Simple severity → base priority mapping
        self._severity_weight = {
            "critical": 100,
            "warning": 50,
            "info": 10,
        }

    # -------------------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------------------

    def build_plan(self, identity: IdentityType = "OWNER") -> OrchestrationPlan:
        """
        Run full diagnostics, build explanations, prioritize issues,
        and prepare a list of agent actions (not executed).
        """

        # 1) Run diagnostics
        health_report = self.health_engine.analyze()
        driver_report = self.driver_engine.analyze()
        task_report = self.task_engine.analyze()
        service_report = self.service_engine.analyze()

        # 2) Build explanations
        health_expl = self.education_engine.explain_system_health(identity, health_report)
        driver_expl = self.education_engine.explain_drivers(identity, driver_report)
        task_expl = self.education_engine.explain_tasks(identity, task_report)
        service_expl = self.education_engine.explain_services(identity, service_report)

        # 3) Aggregate and prioritize issues
        issues: List[PrioritizedItem] = []
        issues.extend(
            self._collect_health_issues(health_report, health_expl)
        )
        issues.extend(
            self._collect_driver_issues(driver_report, driver_expl)
        )
        issues.extend(
            self._collect_task_issues(task_report, task_expl)
        )
        issues.extend(
            self._collect_service_issues(service_report, service_expl)
        )

        # Sort by priority_score descending
        issues.sort(key=lambda x: x.priority_score, reverse=True)

        # 4) Build agent actions (not executed yet)
        actions = self._build_agent_actions(driver_report, task_report, service_report)

        return OrchestrationPlan(
            identity=identity,
            created_at=time.time(),
            issues=issues,
            actions=actions,
            dry_run=self.dry_run,
        )

    def execute_plan(
        self,
        identity: IdentityType,
        plan: OrchestrationPlan,
        max_actions: int | None = None,
    ) -> List[AgentResult]:
        """
        Optionally execute part of the plan via SystemAgent41.
        Respects identity and dry_run flag of the underlying agent.
        """
        results: List[AgentResult] = []
        actions = plan.actions

        if max_actions is not None:
            actions = actions[:max_actions]

        for action in actions:
            result = self.agent.execute_action(identity, action)
            results.append(result)

        return results

    # -------------------------------------------------------------------------
    # ISSUE COLLECTION & PRIORITIZATION
    # -------------------------------------------------------------------------

    def _collect_health_issues(
        self,
        report: HealthReport,
        bundle: EducationBundle,
    ) -> List[PrioritizedItem]:
        items: List[PrioritizedItem] = []
        blocks_by_title = {b.title: b for b in bundle.blocks}

        for issue in report.issues:
            block = blocks_by_title.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, domain="health")

            items.append(
                PrioritizedItem(
                    id=issue.id,
                    domain="health",
                    title=issue.title,
                    description=issue.description,
                    severity=issue.severity,
                    priority_score=score,
                    explanation=explanation,
                    suggested_actions=issue.suggested_actions,
                )
            )

        return items

    def _collect_driver_issues(
        self,
        report: DriverReport,
        bundle: EducationBundle,
    ) -> List[PrioritizedItem]:
        items: List[PrioritizedItem] = []
        blocks_by_title = {b.title: b for b in bundle.blocks}

        for issue in report.issues:
            block = blocks_by_title.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, domain="drivers")

            items.append(
                PrioritizedItem(
                    id=issue.id,
                    domain="drivers",
                    title=issue.title,
                    description=issue.description,
                    severity=issue.severity,
                    priority_score=score,
                    explanation=explanation,
                    suggested_actions=issue.suggested_actions,
                )
            )

        return items

    def _collect_task_issues(
        self,
        report: TaskReport,
        bundle: EducationBundle,
    ) -> List[PrioritizedItem]:
        items: List[PrioritizedItem] = []
        blocks_by_title = {b.title: b for b in bundle.blocks}

        for issue in report.issues:
            block = blocks_by_title.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, domain="tasks")

            items.append(
                PrioritizedItem(
                    id=issue.id,
                    domain="tasks",
                    title=issue.title,
                    description=issue.description,
                    severity=issue.severity,
                    priority_score=score,
                    explanation=explanation,
                    suggested_actions=issue.suggested_actions,
                )
            )

        return items

    def _collect_service_issues(
        self,
        report: ServiceReport,
        bundle: EducationBundle,
    ) -> List[PrioritizedItem]:
        items: List[PrioritizedItem] = []
        blocks_by_title = {b.title: b for b in bundle.blocks}

        for issue in report.issues:
            block = blocks_by_title.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, domain="services")

            items.append(
                PrioritizedItem(
                    id=issue.id,
                    domain="services",
                    title=issue.title,
                    description=issue.description,
                    severity=issue.severity,
                    priority_score=score,
                    explanation=explanation,
                    suggested_actions=issue.suggested_actions,
                )
            )

        return items

    def _compute_priority(self, severity: Severity, domain: str) -> int:
        """
        Simple priority model:
        - base on severity
        - small domain-specific offsets (e.g. health > drivers > tasks > services)
        """
        base = self._severity_weight.get(severity, 10)

        domain_offset = {
            "health": 30,
            "drivers": 20,
            "tasks": 10,
            "services": 5,
        }.get(domain, 0)

        return base + domain_offset

    # -------------------------------------------------------------------------
    # ACTION MAPPING
    # -------------------------------------------------------------------------

    def _build_agent_actions(
        self,
        driver_report: DriverReport,
        task_report: TaskReport,
        service_report: ServiceReport,
    ) -> List[AgentAction]:
        actions: List[AgentAction] = []

        # DRIVER ISSUES → INSTALL DRIVER / OPEN VENDOR PAGE
        for issue in driver_report.issues:
            if issue.severity in ("warning", "critical"):
                action_id = f"install_driver_{issue.id}"
                actions.append(
                    AgentAction(
                        id=action_id,
                        type="INSTALL_DRIVER",
                        label="Install missing or updated driver",
                        description=issue.description,
                        identity_required="OWNER",
                        payload={
                            "related_files": getattr(issue, "related_files", []),
                            "related_devices": getattr(issue, "related_devices", []),
                        },
                    )
                )

        # TASK ISSUES → KILL PROCESS / RESTART EXPLORER
        for issue in task_report.issues:
            if issue.id == "explorer_restart_suggestion":
                actions.append(
                    AgentAction(
                        id="restart_explorer",
                        type="RESTART_EXPLORER",
                        label="Restart Windows Explorer",
                        description=issue.description,
                        identity_required="OWNER",
                        payload={},
                    )
                )

            if issue.id in ("high_cpu_processes", "high_ram_processes"):
                for pid in getattr(issue, "related_pids", []):
                    actions.append(
                        AgentAction(
                            id=f"kill_process_{pid}",
                            type="KILL_PROCESS",
                            label=f"Terminate process {pid}",
                            description=issue.description,
                            identity_required="OWNER",
                            payload={"pid": pid},
                        )
                    )

        # SERVICE ISSUES → RESTART SERVICE
        for issue in service_report.issues:
            for svc in getattr(issue, "related_services", []):
                actions.append(
                    AgentAction(
                        id=f"restart_service_{svc}",
                        type="RESTART_SERVICE",
                        label=f"Restart service {svc}",
                        description=issue.description,
                        identity_required="OWNER",
                        payload={"service_name": svc},
                    )
                )

        return actions
