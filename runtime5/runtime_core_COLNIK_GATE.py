from .logging_5 import log5
from .health_monitor_5 import HealthMonitor5
from .workflow_engine_5 import WorkflowEngine5
from .reasoning_engine_5 import ReasoningEngine5
from .system_hooks_5 import SystemHooks5
from .kg_core import KnowledgeGraph

from .input_parser_5 import InputParser5

from .kg_query import KGQuery
from .kg_reasoner import KGReasoner
from .kg_router import KGRouter

from .system_agent_5 import SystemAgent5
from .envoy_quarantine_5 import EnvoyQuarantine5
from .envoy_permission_layer_5 import PermissionLayer5
from .envoy_execution_layer_5 import EnvoyExecutionLayer5
from .envoy_normalizer_5 import EnvoyNormalizer5
from .envoy_client_5 import EnvoyClient5

from .self_repair_5 import SelfRepair5

from .security.security_family_5_x import SecurityFamily5_x as SecurityFamily5
from .behavior_filter_5 import BehaviorFilter5
from .security.family_safety_rules_5_x import FamilySafetyRules5_x

from .security.identity_engine_3_1 import IdentityEngine3_1

from .contextual_behavior_engine_5 import ContextualBehaviorEngine5
from .kg_light_5 import KGLight5

from .query_normalizer_5 import QueryNormalizer5
from .anchor_resolver_5 import AnchorResolver5

# ⭐ RRE – ReasoningRulesEngine5
from .reasoning_rules_engine_5 import ReasoningRulesEngine5


class RuntimeCore:
    """
    Central orchestrator for Runtime 5.x (SAFE MODE – FÁZA 3).
    """

    def __init__(self, kg: KnowledgeGraph = None):
        log5("[RuntimeCore] Initializing Runtime 5.x")

        self.permission_layer = PermissionLayer5()
        self.kg = kg if kg is not None else KnowledgeGraph()

        # AUTOLOAD KG SNAPSHOT
        try:
            from .kg_export_import_5 import KGExportImport5
            loader = KGExportImport5(self.kg)
            result = loader.import_from_file("autosave_kg.json")

            if result.get("status") == "ok":
                log5(
                    f"[RuntimeCore] AUTOLOAD completed → autosave_kg.json "
                    f"(entities={result.get('loaded_entities')}, "
                    f"relations={result.get('loaded_relations')})"
                )
            else:
                log5(
                    f"[RuntimeCore] AUTOLOAD skipped/failed: "
                    f"{result.get('error', 'unknown error')}"
                )
        except Exception as e:
            log5(f"[RuntimeCore] AUTOLOAD skipped/failed: {e}")

        # KG modules
        self.kg_query = KGQuery(self.kg)

        # ⭐ RRE – dostáva RuntimeCore
        self.rre = ReasoningRulesEngine5(self)

        # ⭐ KGReasoner – musí dostať query aj rre
        self.kg_reasoner = KGReasoner(self.kg, self.kg_query, self.rre)

        self.kg_router = KGRouter(self.kg, self.kg_reasoner)
        self.kg_light = KGLight5(self.kg)

        # ENVOY
        self.quarantine = EnvoyQuarantine5()
        self.envoy_client = EnvoyClient5()
        self.envoy_normalizer = EnvoyNormalizer5()
        self.envoy_execution_layer = EnvoyExecutionLayer5(self)

        # SYSTEM
        self.health = HealthMonitor5()
        self.workflow = WorkflowEngine5(self)
        self.self_repair = SelfRepair5()

        self.system_agent = SystemAgent5(
            kg=self.kg,
            quarantine=self.quarantine
        )
        self.system_agent.runtime = self

        # ReasoningEngine5 – bez rre argumentu
        self.reasoner = ReasoningEngine5(
            kg=self.kg,
            reasoner=self.kg_reasoner
        )

        # INPUT
        self.parser = InputParser5()
        self.security = SecurityFamily5("config/security_identity.json")
        self.identity_engine = IdentityEngine3_1("config/security_identity.json")
        self.behavior_filter = BehaviorFilter5()
        self.family_safety = FamilySafetyRules5_x()
        self.context_engine = ContextualBehaviorEngine5()

        self.query_normalizer = QueryNormalizer5()
        self.anchor_resolver = AnchorResolver5(self.kg)

        log5("[RuntimeCore] Initialization complete")

    # ---------------------------------------------------------
    # MAIN EXECUTION ENTRY
    # ---------------------------------------------------------
    def process(self, data: dict):
        raw_input = data.get("input", "")
        log5(f"[RuntimeCore] Processing input: {data}")

        parsed = self.parser.parse(raw_input)

        if raw_input.lower().startswith("kg"):
            normalized = raw_input
            log5(f"[RuntimeCore] Normalized input (KG-safe): {normalized}")
        else:
            normalized = self.query_normalizer.normalize(raw_input)
            log5(f"[RuntimeCore] Normalized input: {normalized}")

        if normalized.lower().startswith("kg set "):
            anchor = {"source": None, "relation": None, "target": None}
            log5("[RuntimeCore] AnchorResolver skipped for KG SET")
        else:
            anchor = self.anchor_resolver.resolve(normalized)

        intent = parsed.get("intent")
        entity = parsed.get("entity")
        args = parsed.get("args") or {}

        if intent == "kg.set":
            attr = args.get("attribute")
            value = args.get("value")
            args["key"] = attr
            args["value"] = value

        args["raw_input"] = raw_input
        args["anchor"] = anchor

        reasoning_output = self.reasoner.reason(
            intent=intent,
            entity=entity,
            args=args
        )

        # ⭐⭐⭐ COLNIK – bezpečnostná brána pred workflow ⭐⭐⭐
        try:
            identity = self.identity_engine.get_identity({"input": raw_input})
            log5(f"[RuntimeCore] COLNIK identity={identity}")
            # Tu môžeš prípadne blokovať podľa identity, ak chceš:
            # if identity in ["STRANGER", "UNKNOWN", None]:
            #     return {
            #         "status": "denied",
            #         "message": "Blocked by COLNIK (identity)"
            #     }
        except Exception as e:
            log5(f"[RuntimeCore] COLNIK error: {e}")

        return self.workflow.execute(reasoning_output)

    # ---------------------------------------------------------
    # AUTOSAVE KG SNAPSHOT
    # ---------------------------------------------------------
    def autosave_kg(self, filename: str = "autosave_kg.json"):
        try:
            from .kg_export_import_5 import KGExportImport5
            saver = KGExportImport5(self.kg)
            result = saver.export_to_file(filename)
            log5(
                f"[RuntimeCore] AUTOSAVE completed → {filename} "
                f"(entities={result.get('entities')}, relations={result.get('relations')})"
            )
        except Exception as e:
            log5(f"[RuntimeCore] AUTOSAVE ERROR: {e}")

    def shutdown(self):
        self.autosave_kg()
        SystemHooks5.on_shutdown(self)
        log5("[RuntimeCore] Shutdown complete.")
