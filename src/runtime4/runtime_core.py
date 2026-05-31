"""
SIRIUS LOCAL AI – Runtime Core 4.5.0 (PRO)

Central orchestrator of the Runtime 4.5 architecture.
Coordinates:
- module loading
- sandbox isolation
- dependency graph
- scheduler
- Knowledge Packs 2.0
- ENVOY 4.x integration
- offline reasoning engines
- PC automation runtime
- diagnostics & Self‑Repair Layer 4.5 (Phase‑5)
- UI Automation Engine 4.5 (OS bridge, resolver, router, sandbox, workflow)

All logic is deterministic, offline, and fully isolated.

Security Notes (Runtime 4.5.0):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- Fully compatible with Security Family 4.5.
- Self‑Repair Layer Phase‑5 ready.
"""

from typing import Optional, Dict, Any

# -------------------------------------------------------------------------
# SYSTEM INTELLIGENCE LAYER 4.1 – STATIC IMPORTS
# -------------------------------------------------------------------------

from system_health_engine_4_1 import SystemHealthEngine41
from driver_manager_engine_4_1 import DriverManagerEngine41
from task_manager_engine_4_1 import TaskManagerEngine41
from service_manager_engine_4_1 import ServiceManagerEngine41
from education_engine_4_1 import EducationEngine41
from system_agent_4_1 import SystemAgent41

# -------------------------------------------------------------------------
# RUNTIME4 ORCHESTRATOR – STATIC IMPORT
# -------------------------------------------------------------------------

from runtime4.runtime_manager.runtime_manager45 import RuntimeManager45


class RuntimeCore45:
    """
    Main orchestrator for SIRIUS Runtime 4.5.0 (PRO).
    Responsible for initializing, connecting, and supervising all subsystems.
    """

    # Minimal interface contracts (duck-typing)
    REQUIRED_SCHEDULER_METHODS = {"submit"}
    REQUIRED_SANDBOX_METHODS = {"execute", "initialize"}
    REQUIRED_MODULE_LOADER_METHODS = {"load_all"}
    REQUIRED_DEP_GRAPH_METHODS = {"build"}
    REQUIRED_STATE_MANAGER_METHODS = {"initialize"}

    def __init__(
        self,
        # Core subsystems
        module_loader=None,
        sandbox_manager=None,
        state_manager=None,
        scheduler=None,
        dependency_graph=None,
        # Knowledge Packs 2.0
        pack_loader=None,
        pack_validator=None,
        pack_graph=None,
        pack_linker=None,
        # ENVOY 4.x
        envoy_receiver=None,
        envoy_quarantine=None,
        envoy_validator=None,
        envoy_converter=None,
        # Reasoning engines
        rule_engine=None,
        symbolic_engine=None,
        cot_engine=None,
        reasoning_router=None,
        # PC Automation Runtime 4.x
        fs_module=None,
        editor_module=None,
        workflow_module=None,
        command_parser=None,
        command_router=None,
        # Diagnostics & Self‑Repair
        health_check_engine=None,
        integrity_hash=None,
        crash_analyzer=None,
        repair_suggestions=None,
        # Runtime4 orchestrator (Task/Service/Health pipeline)
        runtime_manager: Optional[RuntimeManager45] = None,
    ):
        # Core subsystems
        self.scheduler = scheduler
        self.dependency_graph = dependency_graph
        self.module_loader = module_loader
        self.sandbox_manager = sandbox_manager
        self.state_manager = state_manager

        # Knowledge Packs 2.0
        self.pack_loader = pack_loader
        self.pack_validator = pack_validator
        self.pack_graph = pack_graph
        self.pack_linker = pack_linker

        # ENVOY 4.x
        self.envoy_receiver = envoy_receiver
        self.envoy_quarantine = envoy_quarantine
        self.envoy_validator = envoy_validator
        self.envoy_converter = envoy_converter

        # Reasoning Engine
        self.rule_engine = rule_engine
        self.symbolic_engine = symbolic_engine
        self.cot_engine = cot_engine
        self.reasoning_router = reasoning_router

        # PC Automation Runtime 4.x
        self.fs_module = fs_module
        self.editor_module = editor_module
        self.workflow_module = workflow_module
        self.command_parser = command_parser
        self.command_router = command_router

        # Diagnostics & Self‑Repair
        self.health_check_engine = health_check_engine
        self.integrity_hash = integrity_hash
        self.crash_analyzer = crash_analyzer
        self.repair_suggestions = repair_suggestions

        # Runtime4 orchestrator
        self.runtime_manager: Optional[RuntimeManager45] = runtime_manager

        # System Intelligence Layer 4.1
        self.health_engine_41 = SystemHealthEngine41()
        self.driver_engine_41 = DriverManagerEngine41()
        self.task_engine_41 = TaskManagerEngine41()
        self.service_engine_41 = ServiceManagerEngine41()
        self.education_engine_41 = EducationEngine41()
        self.agent_41 = SystemAgent41(dry_run=True)

        # Internal flags
        self._initialized: bool = False
        self._running: bool = False

        # Runtime 4.5 flags
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ---------------------------------------------------------------------
    # INTERNAL – INTERFACE VALIDATION
    # ---------------------------------------------------------------------
    def _validate_interfaces(self) -> Dict[str, Any]:
        # Scheduler
        if self.scheduler is not None:
            for m in self.REQUIRED_SCHEDULER_METHODS:
                if not hasattr(self.scheduler, m):
                    return {
                        "status": "error",
                        "code": "invalid_scheduler_interface",
                        "missing": m,
                    }

        # Sandbox manager
        if self.sandbox_manager is not None:
            for m in self.REQUIRED_SANDBOX_METHODS:
                if not hasattr(self.sandbox_manager, m):
                    return {
                        "status": "error",
                        "code": "invalid_sandbox_interface",
                        "missing": m,
                    }

        # Module loader
        if self.module_loader is not None:
            for m in self.REQUIRED_MODULE_LOADER_METHODS:
                if not hasattr(self.module_loader, m):
                    return {
                        "status": "error",
                        "code": "invalid_module_loader_interface",
                        "missing": m,
                    }

        # Dependency graph
        if self.dependency_graph is not None:
            for m in self.REQUIRED_DEP_GRAPH_METHODS:
                if not hasattr(self.dependency_graph, m):
                    return {
                        "status": "error",
                        "code": "invalid_dependency_graph_interface",
                        "missing": m,
                    }

        # State manager
        if self.state_manager is not None:
            for m in self.REQUIRED_STATE_MANAGER_METHODS:
                if not hasattr(self.state_manager, m):
                    return {
                        "status": "error",
                        "code": "invalid_state_manager_interface",
                        "missing": m,
                    }

        return {"status": "ok"}

    # ---------------------------------------------------------------------
    # INITIALIZATION PHASE
    # ---------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "version": "4.5.0"}

        if self._initialized:
            return {"status": "already_initialized", "degraded_mode": self.degraded_mode, "version": "4.5.0"}

        # Validate interfaces first
        iface = self._validate_interfaces()
        if iface.get("status") != "ok":
            self.degraded_mode = True
            iface["version"] = "4.5.0"
            return iface

        try:
            self._init_core()
            self._init_sandbox()
            self._init_packs()
            self._init_envoy()
            self._init_reasoning()
            self._init_automation()
            self._init_diagnostics()

            # Spusti RuntimeManager45, ak je prítomný
            if self.runtime_manager is not None:
                self.runtime_manager.start_runtime()

            self._initialized = True
            return {"status": "initialized", "degraded_mode": self.degraded_mode, "version": "4.5.0"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "init_exception", "exception": str(exc), "version": "4.5.0"}

    # ---------------------------------------------------------------------
    # SUBSYSTEM INITIALIZERS
    # ---------------------------------------------------------------------
    def _init_core(self) -> None:
        if self.module_loader:
            self.module_loader.load_all()
        if self.dependency_graph:
            self.dependency_graph.build()
        if self.state_manager:
            self.state_manager.initialize()

    def _init_sandbox(self) -> None:
        if self.sandbox_manager:
            self.sandbox_manager.initialize()

    def _init_packs(self) -> None:
        if self.pack_loader:
            self.pack_loader.load_all()
        if self.pack_validator:
            self.pack_validator.validate_all()
        if self.pack_graph:
            self.pack_graph.build()
        if self.pack_linker:
            self.pack_linker.link_all()

    def _init_envoy(self) -> None:
        if self.envoy_receiver:
            self.envoy_receiver.initialize()
        if self.envoy_quarantine:
            self.envoy_quarantine.initialize()
        if self.envoy_validator:
            self.envoy_validator.initialize()
        if self.envoy_converter:
            self.envoy_converter.initialize()

    def _init_reasoning(self) -> None:
        if self.rule_engine:
            self.rule_engine.initialize()
        if self.symbolic_engine:
            self.symbolic_engine.initialize()
        if self.cot_engine:
            self.cot_engine.initialize()
        if self.reasoning_router:
            self.reasoning_router.initialize()

    def _init_automation(self) -> None:
        if self.fs_module:
            self.fs_module.initialize()
        if self.editor_module:
            self.editor_module.initialize()
        if self.workflow_module:
            self.workflow_module.initialize()
        if self.command_parser:
            self.command_parser.initialize()
        if self.command_router:
            self.command_router.initialize()

    def _init_diagnostics(self) -> None:
        if self.health_check_engine:
            self.health_check_engine.initialize()
        if self.crash_analyzer:
            self.crash_analyzer.initialize()
        if self.repair_suggestions:
            self.repair_suggestions.initialize()

    # ---------------------------------------------------------------------
    # SYSTEM INTELLIGENCE LAYER 4.1 – FULL DIAGNOSTICS PIPELINE
    # ---------------------------------------------------------------------
    def run_full_diagnostics(self, identity: str = "OWNER") -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "version": "4.5.0"}

        try:
            health_report = self.health_engine_41.analyze()
            driver_report = self.driver_engine_41.analyze()
            task_report = self.task_engine_41.analyze()
            service_report = self.service_engine_41.analyze()

            health_expl = self.education_engine_41.explain_system_health(identity, health_report)
            driver_expl = self.education_engine_41.explain_drivers(identity, driver_report)
            task_expl = self.education_engine_41.explain_tasks(identity, task_report)
            service_expl = self.education_engine_41.explain_services(identity, service_report)

            suggested_actions = self._build_suggested_actions(
                identity, driver_report, task_report, service_report
            )

            return {
                "status": "ok",
                "reports": {
                    "health": health_report,
                    "drivers": driver_report,
                    "tasks": task_report,
                    "services": service_report,
                },
                "explanations": {
                    "health": health_expl,
                    "drivers": driver_expl,
                    "tasks": task_expl,
                    "services": service_expl,
                },
                "suggested_actions": suggested_actions,
                "degraded_mode": self.degraded_mode,
                "version": "4.5.0",
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "diagnostics_exception",
                "exception": str(exc),
                "version": "4.5.0",
            }

    # ---------------------------------------------------------------------
    # ACTION BUILDER (unchanged semantics, structured output)
    # ---------------------------------------------------------------------
    def _build_suggested_actions(self, identity, driver_report, task_report, service_report):
        actions = []

        # DRIVER ISSUES
        for issue in getattr(driver_report, "issues", []):
            if issue.severity in ("warning", "critical"):
                actions.append({
                    "type": "INSTALL_DRIVER",
                    "label": "Install missing or updated driver",
                    "payload": {"related_files": getattr(issue, "related_files", [])},
                    "identity_required": "OWNER",
                })

        # TASK ISSUES
        for issue in getattr(task_report, "issues", []):
            if issue.id == "explorer_restart_suggestion":
                actions.append({
                    "type": "RESTART_EXPLORER",
                    "label": "Restart Windows Explorer",
                    "payload": {},
                    "identity_required": "OWNER",
                })
            if issue.id in ("high_cpu_processes", "high_ram_processes"):
                for pid in getattr(issue, "related_pids", []):
                    actions.append({
                        "type": "KILL_PROCESS",
                        "label": f"Terminate process {pid}",
                        "payload": {"pid": pid},
                        "identity_required": "OWNER",
                    })

        # SERVICE ISSUES
        for issue in getattr(service_report, "issues", []):
            for svc in getattr(issue, "related_services", []):
                actions.append({
                    "type": "RESTART_SERVICE",
                    "label": f"Restart service {svc}",
                    "payload": {"service_name": svc},
                    "identity_required": "OWNER",
                })

        return actions

    # ---------------------------------------------------------------------
    # RUNTIME STEP – DIAGNOSTICS + RUNTIME MANAGER TICK
    # ---------------------------------------------------------------------
    def runtime_step(self, identity: str = "OWNER") -> Dict[str, Any]:
        """
        One deterministic runtime step:
        - runs full diagnostics (System Intelligence Layer 4.1)
        - runs RuntimeManager45.tick() if available
        """
        diag = self.run_full_diagnostics(identity=identity)

        if self.runtime_manager is not None:
            self.runtime_manager.tick()

        return {
            "status": "ok",
            "diagnostics": diag,
            "degraded_mode": self.degraded_mode,
            "version": "4.5.0",
        }
