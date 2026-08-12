C:\SIRIUS_ARCHIVE\SIRIUS-LOCAL-AI-5.6.1>python runtime5_cli.py
[RUNTIME5 2026-08-12 11:03:48] [INFO] [RuntimeCore] Initializing Runtime 5.x
[RUNTIME5 2026-08-12 11:03:48] [INFO] [PermissionLayer5] Initialized ENVOY Permission Layer 5.x
[RUNTIME5 2026-08-12 11:03:48] [INFO] [PolicyEngine5] Loaded 4 rules.
[RUNTIME5 2026-08-12 11:03:48] [INFO] [PermissionLayer5] PolicyEngine5 loaded.
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KnowledgeGraph] Initialized KG Core (Unified Schema)
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: auto
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: osoba
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: zviera
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Set attribute: zviera.type = zviera
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: entita
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Set attribute: entita.type = zviera
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: chlpaty
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: je
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: existuje
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: fyzicka
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: kg_get
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: color
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added entity: kg_unset
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: zviera -[je]-> entita
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: zviera -[ma_vlastnost]-> chlpaty
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: entita -[ma_vlastnost]-> existuje
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: entita -[ma_vlastnost]-> fyzicka
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: kg_get -[auto]-> color
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: kg_unset -[auto]-> color
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: osoba -[ma_vlastnost]-> fyzicka
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: entita -[je]-> zviera
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: entita -[je]-> entita
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG] Added relation: entita -[orbits]-> entita
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KGExportImport5] AUTOLOAD completed: entities=11, relations=10
[RUNTIME5 2026-08-12 11:03:48] [INFO] [RuntimeCore] AUTOLOAD completed → autosave_kg.json (entities=11, relations=10)
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KGQuery] Initialized query engine (Unified Schema).
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KGReasoner] Initialized reasoning engine.
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KGReasoner] Linked to ReasoningRulesEngine5.
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KGRouter] Initialized KG router 5.x
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KGLight5] Initialized KG Light module
[RUNTIME5 2026-08-12 11:03:48] [INFO] [EnvoyQuarantine5] Initialized minimal quarantine store
[RUNTIME5 2026-08-12 11:03:48] [INFO] [EnvoyNormalizer5] Initialized normalizer 5.x
[RUNTIME5 2026-08-12 11:03:48] [INFO] [EnvoyExecutionLayer5] Initialized ENVOY Execution Layer 5.x (shared runtime)
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: WORKFLOW_CONTINUE
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: ENVOY_LEVEL1
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: COMPARE
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_LIGHT
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_ADD
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_REMOVE
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_RELATE
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_RELATIONS
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_VIEW
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_PATH
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_QUERY
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPORT
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_IMPORT
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_BACKUP
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_RESTORE
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_SET
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_GET
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG_UNSET] Initialized KG_UNSET step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_UNSET
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG_LIST] Initialized KG_LIST step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_LIST
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG_SEARCH] Initialized KG_SEARCH step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_SEARCH
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG_RENAME] Initialized KG_RENAME step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_RENAME
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG_EXISTS] Initialized KG_EXISTS step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXISTS
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG_STATS] Initialized KG_STATS step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_STATS
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG_DELETE] Initialized KG_DELETE step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_DELETE
[RUNTIME5 2026-08-12 11:03:48] [INFO] [KG_MERGE] Initialized KG_MERGE step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_MERGE
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_ATTRIBUTES
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: REASON_ORBITS
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepReasonInfer5] Initialized REASON_INFER step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: REASON_INFER
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_INFER
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLAIN
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLAIN_DEEP
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_REMOVE_RELATION
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLORE
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepReasonWhy5] Initialized REASON_WHY step
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Registered step: REASON_WHY
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowStepRegistry5] Default steps initialized
[RUNTIME5 2026-08-12 11:03:48] [INFO] [WorkflowEngine5] Initialized workflow engine.
[RUNTIME5 2026-08-12 11:03:48] [INFO] [SelfRepair5] Initialized self-repair layer 5.4
[RUNTIME5 2026-08-12 11:03:48] [INFO] [SystemAgent5] Initializing system agent
[RUNTIME5 2026-08-12 11:03:48] [INFO] [ReasoningEngine5] Initialized reasoning engine.
[RUNTIME5 2026-08-12 11:03:48] [INFO] [RRE] Registered rule: OrbitTypeInferenceRule
[RUNTIME5 2026-08-12 11:03:48] [INFO] [RRE] Registered rule: AutoTypeInferenceRule
[RUNTIME5 2026-08-12 11:03:48] [INFO] [RRE] Registered rule: MultiHopOrbitInferenceRule
[RUNTIME5 2026-08-12 11:03:48] [INFO] [RRE] Registered rule: DedicsnostVlastnostiRule
[RUNTIME5 2026-08-12 11:03:48] [INFO] [RRE] Registered rule: TranzitivneRelacieRule
[RUNTIME5 2026-08-12 11:03:48] [INFO] [InputParser5] Initialized Input Parser 5.x
[RUNTIME5 2026-08-12 11:03:48] [INFO] [BehaviorFilter5] Initialized behavior filter 5.x
[RUNTIME5 2026-08-12 11:03:48] [INFO] [FamilySafetyRules5_x] Initialized Family Safety Rules 5.x
[RUNTIME5 2026-08-12 11:03:48] [INFO] [ContextualBehaviorEngine5] Initialized
[RUNTIME5 2026-08-12 11:03:48] [INFO] [RuntimeCore] Initialization complete
[RUNTIME5 2026-08-12 11:03:48] [INFO] [BehaviorFilter5] Initialized behavior filter 5.x
[RUNTIME5 2026-08-12 11:03:48] [INFO] [Runtime5CLI] Initialized (v5.3.0)
Runtime5 CLI ready.
>>> kg.exists pes
[RUNTIME5 2026-08-12 11:04:02] [INFO] [RuntimeCore] Processing input: {'input': 'kg.exists pes'}
[RUNTIME5 2026-08-12 11:04:02] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.exists pes
[RUNTIME5 2026-08-12 11:04:02] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.exists, entity='pes'
[RUNTIME5 2026-08-12 11:04:02] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'pes'
[RUNTIME5 2026-08-12 11:04:02] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:04:02] [INFO] [PolicyEngine5] MATCH intent='kg.exists' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:04:02] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:04:02] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.exists' → route='KG_EXISTS'
[RUNTIME5 2026-08-12 11:04:02] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXISTS
[RUNTIME5 2026-08-12 11:04:02] [INFO] [KG_EXISTS] RAW DATA = {'intent': 'kg.exists', 'entity': 'pes', 'args': {'entity': 'pes', 'mode': 'developer', 'raw_input': 'kg.exists pes', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'reasoning_output': {'intent': 'kg.exists', 'entity': 'pes', 'args': {'entity': 'pes', 'mode': 'developer', 'raw_input': 'kg.exists pes', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'route': 'KG_EXISTS', 'mode': 'developer', 'degraded': False}}
[RUNTIME5 2026-08-12 11:04:02] [INFO] [KG_EXISTS] Entity 'pes' exists = False
--------------------------------------------------
{'status': 'OK', 'action': 'KG_EXISTS', 'entity': 'pes', 'message': "Workflow step 'KG_EXISTS' completed", 'data': {'status': 'ok', 'action': 'KG_EXISTS', 'entity': 'pes', 'exists': False, 'message': "Entity 'pes' exists = False"}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.exists entita
[RUNTIME5 2026-08-12 11:04:14] [INFO] [RuntimeCore] Processing input: {'input': 'kg.exists entita'}
[RUNTIME5 2026-08-12 11:04:14] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.exists entita
[RUNTIME5 2026-08-12 11:04:14] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.exists, entity='entita'
[RUNTIME5 2026-08-12 11:04:14] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:04:14] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:04:14] [INFO] [PolicyEngine5] MATCH intent='kg.exists' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:04:14] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:04:14] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.exists' → route='KG_EXISTS'
[RUNTIME5 2026-08-12 11:04:14] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXISTS
[RUNTIME5 2026-08-12 11:04:14] [INFO] [KG_EXISTS] RAW DATA = {'intent': 'kg.exists', 'entity': 'entita', 'args': {'entity': 'entita', 'mode': 'developer', 'raw_input': 'kg.exists entita', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'reasoning_output': {'intent': 'kg.exists', 'entity': 'entita', 'args': {'entity': 'entita', 'mode': 'developer', 'raw_input': 'kg.exists entita', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'route': 'KG_EXISTS', 'mode': 'developer', 'degraded': False}}
[RUNTIME5 2026-08-12 11:04:14] [INFO] [KG_EXISTS] Entity 'entita' exists = True
--------------------------------------------------
{'status': 'OK', 'action': 'KG_EXISTS', 'entity': 'entita', 'message': "Workflow step 'KG_EXISTS' completed", 'data': {'status': 'ok', 'action': 'KG_EXISTS', 'entity': 'entita', 'exists': True, 'message': "Entity 'entita' exists = True"}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.exists zviera
[RUNTIME5 2026-08-12 11:04:48] [INFO] [RuntimeCore] Processing input: {'input': 'kg.exists zviera'}
[RUNTIME5 2026-08-12 11:04:48] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.exists zviera
[RUNTIME5 2026-08-12 11:04:48] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.exists, entity='zviera'
[RUNTIME5 2026-08-12 11:04:48] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'zviera'
[RUNTIME5 2026-08-12 11:04:48] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:04:48] [INFO] [PolicyEngine5] MATCH intent='kg.exists' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:04:48] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:04:48] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.exists' → route='KG_EXISTS'
[RUNTIME5 2026-08-12 11:04:48] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXISTS
[RUNTIME5 2026-08-12 11:04:48] [INFO] [KG_EXISTS] RAW DATA = {'intent': 'kg.exists', 'entity': 'zviera', 'args': {'entity': 'zviera', 'mode': 'developer', 'raw_input': 'kg.exists zviera', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'reasoning_output': {'intent': 'kg.exists', 'entity': 'zviera', 'args': {'entity': 'zviera', 'mode': 'developer', 'raw_input': 'kg.exists zviera', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'route': 'KG_EXISTS', 'mode': 'developer', 'degraded': False}}
[RUNTIME5 2026-08-12 11:04:48] [INFO] [KG_EXISTS] Entity 'zviera' exists = True
--------------------------------------------------
{'status': 'OK', 'action': 'KG_EXISTS', 'entity': 'zviera', 'message': "Workflow step 'KG_EXISTS' completed", 'data': {'status': 'ok', 'action': 'KG_EXISTS', 'entity': 'zviera', 'exists': True, 'message': "Entity 'zviera' exists = True"}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.attributes entita
[RUNTIME5 2026-08-12 11:05:07] [INFO] [RuntimeCore] Processing input: {'input': 'kg.attributes entita'}
[RUNTIME5 2026-08-12 11:05:07] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.attributes entita
[RUNTIME5 2026-08-12 11:05:07] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.attributes, entity='entita'
[RUNTIME5 2026-08-12 11:05:07] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:05:07] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:05:07] [INFO] [PolicyEngine5] MATCH intent='kg.attributes' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:05:07] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:05:07] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.attributes' → route='KG_ATTRIBUTES'
[RUNTIME5 2026-08-12 11:05:07] [INFO] [WorkflowEngine5] Executing workflow step: KG_ATTRIBUTES
[RUNTIME5 2026-08-12 11:05:07] [INFO] [KG_ATTRIBUTES] Getting attributes for entity: entita → entita
--------------------------------------------------
{'status': 'OK', 'action': 'KG_ATTRIBUTES', 'entity': 'entita', 'message': "Workflow step 'KG_ATTRIBUTES' completed", 'data': {'status': 'ok', 'action': 'KG_ATTRIBUTES', 'entity': 'entita', 'attributes': {'type': 'zviera'}, 'count': 1, 'message': "Entity 'entita' has 1 attributes."}, 'counts': {'attributes': 1, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.attributes zviera
[RUNTIME5 2026-08-12 11:05:17] [INFO] [RuntimeCore] Processing input: {'input': 'kg.attributes zviera'}
[RUNTIME5 2026-08-12 11:05:17] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.attributes zviera
[RUNTIME5 2026-08-12 11:05:17] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.attributes, entity='zviera'
[RUNTIME5 2026-08-12 11:05:17] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'zviera'
[RUNTIME5 2026-08-12 11:05:17] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:05:17] [INFO] [PolicyEngine5] MATCH intent='kg.attributes' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:05:17] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:05:17] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.attributes' → route='KG_ATTRIBUTES'
[RUNTIME5 2026-08-12 11:05:17] [INFO] [WorkflowEngine5] Executing workflow step: KG_ATTRIBUTES
[RUNTIME5 2026-08-12 11:05:17] [INFO] [KG_ATTRIBUTES] Getting attributes for entity: zviera → zviera
--------------------------------------------------
{'status': 'OK', 'action': 'KG_ATTRIBUTES', 'entity': 'zviera', 'message': "Workflow step 'KG_ATTRIBUTES' completed", 'data': {'status': 'ok', 'action': 'KG_ATTRIBUTES', 'entity': 'zviera', 'attributes': {'type': 'zviera'}, 'count': 1, 'message': "Entity 'zviera' has 1 attributes."}, 'counts': {'attributes': 1, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.relations entita
[RUNTIME5 2026-08-12 11:05:27] [INFO] [RuntimeCore] Processing input: {'input': 'kg.relations entita'}
[RUNTIME5 2026-08-12 11:05:27] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.relations entita
[RUNTIME5 2026-08-12 11:05:27] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.relations, entity='entita'
[RUNTIME5 2026-08-12 11:05:27] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:05:27] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:05:27] [INFO] [PolicyEngine5] MATCH intent='kg.relations' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:05:27] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:05:27] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.relations' → route='KG_RELATIONS'
[RUNTIME5 2026-08-12 11:05:27] [INFO] [WorkflowEngine5] Executing workflow step: KG_RELATIONS
[RUNTIME5 2026-08-12 11:05:27] [INFO] [KG_RELATIONS] Resolving relations for: entita → entita
[RUNTIME5 2026-08-12 11:05:27] [INFO] [KG_RELATIONS] Entity 'entita' → 5 outgoing, 3 incoming relations.
--------------------------------------------------
{'status': 'OK', 'action': 'KG_RELATIONS', 'entity': 'entita', 'message': "Workflow step 'KG_RELATIONS' completed", 'data': {'status': 'ok', 'action': 'KG_RELATIONS', 'entity': 'entita', 'outgoing_relations': [{'source': 'entita', 'relation': 'ma_vlastnost', 'target': 'existuje'}, {'source': 'entita', 'relation': 'ma_vlastnost', 'target': 'fyzicka'}, {'source': 'entita', 'relation': 'je', 'target': 'zviera'}, {'source': 'entita', 'relation': 'je', 'target': 'entita'}, {'source': 'entita', 'relation': 'orbits', 'target': 'entita'}], 'incoming_relations': [{'source': 'zviera', 'relation': 'je', 'target': 'entita'}, {'source': 'entita', 'relation': 'je', 'target': 'entita'}, {'source': 'entita', 'relation': 'orbits', 'target': 'entita'}], 'outgoing_count': 5, 'incoming_count': 3, 'message': "Relations for 'entita': 5 outgoing, 3 incoming."}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.relations zviera
[RUNTIME5 2026-08-12 11:05:36] [INFO] [RuntimeCore] Processing input: {'input': 'kg.relations zviera'}
[RUNTIME5 2026-08-12 11:05:36] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.relations zviera
[RUNTIME5 2026-08-12 11:05:36] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.relations, entity='zviera'
[RUNTIME5 2026-08-12 11:05:36] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'zviera'
[RUNTIME5 2026-08-12 11:05:36] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:05:36] [INFO] [PolicyEngine5] MATCH intent='kg.relations' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:05:36] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:05:36] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.relations' → route='KG_RELATIONS'
[RUNTIME5 2026-08-12 11:05:36] [INFO] [WorkflowEngine5] Executing workflow step: KG_RELATIONS
[RUNTIME5 2026-08-12 11:05:36] [INFO] [KG_RELATIONS] Resolving relations for: zviera → zviera
[RUNTIME5 2026-08-12 11:05:36] [INFO] [KG_RELATIONS] Entity 'zviera' → 2 outgoing, 1 incoming relations.
--------------------------------------------------
{'status': 'OK', 'action': 'KG_RELATIONS', 'entity': 'zviera', 'message': "Workflow step 'KG_RELATIONS' completed", 'data': {'status': 'ok', 'action': 'KG_RELATIONS', 'entity': 'zviera', 'outgoing_relations': [{'source': 'zviera', 'relation': 'je', 'target': 'entita'}, {'source': 'zviera', 'relation': 'ma_vlastnost', 'target': 'chlpaty'}], 'incoming_relations': [{'source': 'entita', 'relation': 'je', 'target': 'zviera'}], 'outgoing_count': 2, 'incoming_count': 1, 'message': "Relations for 'zviera': 2 outgoing, 1 incoming."}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.relations entita
[RUNTIME5 2026-08-12 11:05:47] [INFO] [RuntimeCore] Processing input: {'input': 'kg.relations entita'}
[RUNTIME5 2026-08-12 11:05:47] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.relations entita
[RUNTIME5 2026-08-12 11:05:47] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.relations, entity='entita'
[RUNTIME5 2026-08-12 11:05:47] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:05:47] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:05:47] [INFO] [PolicyEngine5] MATCH intent='kg.relations' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:05:47] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:05:47] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.relations' → route='KG_RELATIONS'
[RUNTIME5 2026-08-12 11:05:47] [INFO] [WorkflowEngine5] Executing workflow step: KG_RELATIONS
[RUNTIME5 2026-08-12 11:05:47] [INFO] [KG_RELATIONS] Resolving relations for: entita → entita
[RUNTIME5 2026-08-12 11:05:47] [INFO] [KG_RELATIONS] Entity 'entita' → 5 outgoing, 3 incoming relations.
--------------------------------------------------
{'status': 'OK', 'action': 'KG_RELATIONS', 'entity': 'entita', 'message': "Workflow step 'KG_RELATIONS' completed", 'data': {'status': 'ok', 'action': 'KG_RELATIONS', 'entity': 'entita', 'outgoing_relations': [{'source': 'entita', 'relation': 'ma_vlastnost', 'target': 'existuje'}, {'source': 'entita', 'relation': 'ma_vlastnost', 'target': 'fyzicka'}, {'source': 'entita', 'relation': 'je', 'target': 'zviera'}, {'source': 'entita', 'relation': 'je', 'target': 'entita'}, {'source': 'entita', 'relation': 'orbits', 'target': 'entita'}], 'incoming_relations': [{'source': 'zviera', 'relation': 'je', 'target': 'entita'}, {'source': 'entita', 'relation': 'je', 'target': 'entita'}, {'source': 'entita', 'relation': 'orbits', 'target': 'entita'}], 'outgoing_count': 5, 'incoming_count': 3, 'message': "Relations for 'entita': 5 outgoing, 3 incoming."}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.path entita zviera
[RUNTIME5 2026-08-12 11:05:56] [INFO] [RuntimeCore] Processing input: {'input': 'kg.path entita zviera'}
[RUNTIME5 2026-08-12 11:05:56] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.path entita zviera
[RUNTIME5 2026-08-12 11:05:56] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.path, entity='entita'
[RUNTIME5 2026-08-12 11:05:56] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:05:56] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:05:56] [INFO] [PolicyEngine5] MATCH intent='kg.path' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:05:56] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:05:56] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.path' → route='KG_PATH'
[RUNTIME5 2026-08-12 11:05:56] [INFO] [WorkflowEngine5] Executing workflow step: KG_PATH
[RUNTIME5 2026-08-12 11:05:56] [INFO] [KG_PATH] Searching shortest path: entita → zviera
[RUNTIME5 2026-08-12 11:05:56] [INFO] [KGQuery] Related entities for 'entita': 8 found
[RUNTIME5 2026-08-12 11:05:56] [INFO] [KGQuery] Related entities for 'existuje': 1 found
[RUNTIME5 2026-08-12 11:05:56] [INFO] [KGQuery] Related entities for 'fyzicka': 2 found
[RUNTIME5 2026-08-12 11:05:56] [INFO] [KGQuery] Shortest path found: ['entita', 'zviera']
[RUNTIME5 2026-08-12 11:05:56] [INFO] [KG_PATH] Path found: ['entita', 'zviera']
--------------------------------------------------
{'status': 'OK', 'action': 'KG_PATH', 'entity': 'entita', 'message': "Workflow step 'KG_PATH' completed", 'data': {'status': 'ok', 'action': 'KG_PATH', 'source': 'entita', 'target': 'zviera', 'path': ['entita', 'zviera'], 'length': 2, 'message': "Shortest path from 'entita' to 'zviera'."}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.delete entita
[RUNTIME5 2026-08-12 11:06:09] [INFO] [RuntimeCore] Processing input: {'input': 'kg.delete entita'}
[RUNTIME5 2026-08-12 11:06:09] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.delete entita
[RUNTIME5 2026-08-12 11:06:09] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.delete, entity='entita'
[RUNTIME5 2026-08-12 11:06:09] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:06:09] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:06:09] [INFO] [PolicyEngine5] MATCH intent='kg.delete' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:06:09] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:06:09] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.delete' → route='KG_DELETE'
[RUNTIME5 2026-08-12 11:06:09] [INFO] [WorkflowEngine5] Executing workflow step: KG_DELETE
[RUNTIME5 2026-08-12 11:06:09] [INFO] [KG_DELETE] RAW DATA = {'intent': 'kg.delete', 'entity': 'entita', 'args': {'entity': 'entita', 'mode': 'developer', 'raw_input': 'kg.delete entita', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'reasoning_output': {'intent': 'kg.delete', 'entity': 'entita', 'args': {'entity': 'entita', 'mode': 'developer', 'raw_input': 'kg.delete entita', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'route': 'KG_DELETE', 'mode': 'developer', 'degraded': False}}
[RUNTIME5 2026-08-12 11:06:09] [INFO] [KG] Removed relation: zviera -[je]-> entita
[RUNTIME5 2026-08-12 11:06:09] [INFO] [KG] Removed relation: entita -[ma_vlastnost]-> existuje
[RUNTIME5 2026-08-12 11:06:09] [INFO] [KG] Removed relation: entita -[ma_vlastnost]-> fyzicka
[RUNTIME5 2026-08-12 11:06:09] [INFO] [KG] Removed relation: entita -[je]-> zviera
[RUNTIME5 2026-08-12 11:06:09] [INFO] [KG] Removed relation: entita -[je]-> entita
[RUNTIME5 2026-08-12 11:06:09] [INFO] [KG] Removed relation: entita -[orbits]-> entita
[RUNTIME5 2026-08-12 11:06:09] [INFO] [KG_DELETE] Deleted entity: entita
--------------------------------------------------
{'status': 'OK', 'action': 'KG_DELETE', 'entity': 'entita', 'message': "Workflow step 'KG_DELETE' completed", 'data': {'status': 'ok', 'action': 'KG_DELETE', 'entity': 'entita', 'deleted': True, 'removed_relations': 6, 'message': "Entity 'entita' deleted. Removed 6 relations."}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.set entita color modra
[RUNTIME5 2026-08-12 11:06:19] [INFO] [RuntimeCore] Processing input: {'input': 'kg.set entita color modra'}
[RUNTIME5 2026-08-12 11:06:19] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.set entita color modra
[RUNTIME5 2026-08-12 11:06:19] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.set, entity='entita'
[RUNTIME5 2026-08-12 11:06:19] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:06:19] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:06:19] [INFO] [PolicyEngine5] MATCH intent='kg.set' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:06:19] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:06:19] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.set' → route='KG_SET'
[RUNTIME5 2026-08-12 11:06:19] [INFO] [WorkflowEngine5] Executing workflow step: KG_SET
[RUNTIME5 2026-08-12 11:06:19] [INFO] [KG_SET] Setting attribute: entita.color = modra
[RUNTIME5 2026-08-12 11:06:19] [INFO] [KG_SET] Entity 'entita' not found → creating it
[RUNTIME5 2026-08-12 11:06:19] [INFO] [KG] Added entity: entita
[RUNTIME5 2026-08-12 11:06:19] [INFO] [KG] Set attribute: entita.color = modra
[RUNTIME5 2026-08-12 11:06:19] [INFO] [KG_SET] entita.color = modra
--------------------------------------------------
{'status': 'OK', 'action': 'KG_SET', 'entity': 'entita', 'message': "Workflow step 'KG_SET' completed", 'data': {'status': 'ok', 'action': 'KG_SET', 'entity': 'entita', 'key': 'color', 'value': 'modra', 'message': 'Set entita.color = modra'}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.get entita color
[RUNTIME5 2026-08-12 11:06:28] [INFO] [RuntimeCore] Processing input: {'input': 'kg.get entita color'}
[RUNTIME5 2026-08-12 11:06:28] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.get entita color
[RUNTIME5 2026-08-12 11:06:28] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.get, entity='entita'
[RUNTIME5 2026-08-12 11:06:28] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:06:28] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:06:28] [INFO] [PolicyEngine5] MATCH intent='kg.get' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:06:28] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:06:28] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.get' → route='KG_GET'
[RUNTIME5 2026-08-12 11:06:28] [INFO] [WorkflowEngine5] Executing workflow step: KG_GET
[RUNTIME5 2026-08-12 11:06:28] [INFO] [KG_GET] DEBUG → entity=entita, key=color
[RUNTIME5 2026-08-12 11:06:28] [INFO] [KG_GET] RESULT → entita.color = modra
--------------------------------------------------
{'status': 'OK', 'action': 'KG_GET', 'entity': 'entita', 'message': "Workflow step 'KG_GET' completed", 'data': {'status': 'ok', 'entity': 'entita', 'key': 'color', 'value': 'modra', 'message': 'entita.color = modra'}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.unset entita color
[RUNTIME5 2026-08-12 11:06:36] [INFO] [RuntimeCore] Processing input: {'input': 'kg.unset entita color'}
[RUNTIME5 2026-08-12 11:06:36] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.unset entita color
[RUNTIME5 2026-08-12 11:06:36] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.unset, entity='entita'
[RUNTIME5 2026-08-12 11:06:36] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:06:36] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:06:36] [INFO] [PolicyEngine5] MATCH intent='kg.unset' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:06:36] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:06:36] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.unset' → route='KG_UNSET'
[RUNTIME5 2026-08-12 11:06:36] [INFO] [WorkflowEngine5] Executing workflow step: KG_UNSET
[RUNTIME5 2026-08-12 11:06:36] [INFO] [KG_UNSET] RAW DATA = {'intent': 'kg.unset', 'entity': 'entita', 'args': {'entity': 'entita', 'attribute': 'color', 'key': 'color', 'mode': 'developer', 'raw_input': 'kg.unset entita color', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'reasoning_output': {'intent': 'kg.unset', 'entity': 'entita', 'args': {'entity': 'entita', 'attribute': 'color', 'key': 'color', 'mode': 'developer', 'raw_input': 'kg.unset entita color', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}}, 'route': 'KG_UNSET', 'mode': 'developer', 'degraded': False}}
[RUNTIME5 2026-08-12 11:06:36] [INFO] [KG] Unset attribute: entita.color
[RUNTIME5 2026-08-12 11:06:36] [INFO] [KG_UNSET] Attribute 'color' removed from 'entita'
--------------------------------------------------
{'status': 'OK', 'action': 'KG_UNSET', 'entity': 'entita', 'message': "Workflow step 'KG_UNSET' completed", 'data': {'status': 'ok', 'action': 'KG_UNSET', 'entity': 'entita', 'attribute': 'color', 'message': "Attribute 'color' removed from 'entita'."}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.relate entita ma_vlastnost existuje
[RUNTIME5 2026-08-12 11:06:48] [INFO] [RuntimeCore] Processing input: {'input': 'kg.relate entita ma_vlastnost existuje'}
[RUNTIME5 2026-08-12 11:06:48] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.relate entita ma_vlastnost existuje
[RUNTIME5 2026-08-12 11:06:48] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.relate, entity='entita'
[RUNTIME5 2026-08-12 11:06:48] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:06:48] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:06:48] [INFO] [PolicyEngine5] MATCH intent='kg.relate' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:06:48] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:06:48] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.relate' → route='KG_RELATE'
[RUNTIME5 2026-08-12 11:06:48] [INFO] [WorkflowEngine5] Executing workflow step: KG_RELATE
[RUNTIME5 2026-08-12 11:06:48] [INFO] [KG_RELATE] RAW DATA = {'intent': 'kg.relate', 'entity': 'entita', 'args': {'source': 'entita', 'relation': 'ma_vlastnost', 'target': 'existuje', 'mode': 'developer', 'raw_input': 'kg.relate entita ma_vlastnost existuje', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'entity': 'entita'}, 'reasoning_output': {'intent': 'kg.relate', 'entity': 'entita', 'args': {'source': 'entita', 'relation': 'ma_vlastnost', 'target': 'existuje', 'mode': 'developer', 'raw_input': 'kg.relate entita ma_vlastnost existuje', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'entity': 'entita'}, 'route': 'KG_RELATE', 'mode': 'developer', 'degraded': False}}
[RUNTIME5 2026-08-12 11:06:48] [INFO] [KG_RELATE] Adding relation: entita -[ma_vlastnost]-> existuje
[RUNTIME5 2026-08-12 11:06:48] [INFO] [KG] Added relation: entita -[ma_vlastnost]-> existuje
--------------------------------------------------
{'status': 'OK', 'action': 'KG_RELATE', 'entity': 'entita', 'message': "Workflow step 'KG_RELATE' completed", 'data': {'status': 'ok', 'action': 'KG_RELATE', 'source': 'entita', 'relation': 'ma_vlastnost', 'target': 'existuje', 'message': 'Relation added: entita -[ma_vlastnost]-> existuje'}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.remove_relation entita ma_vlastnost existuje
[RUNTIME5 2026-08-12 11:07:00] [INFO] [RuntimeCore] Processing input: {'input': 'kg.remove_relation entita ma_vlastnost existuje'}
[RUNTIME5 2026-08-12 11:07:00] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.remove_relation entita ma_vlastnost existuje
[RUNTIME5 2026-08-12 11:07:00] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.remove_relation, entity='entita'
[RUNTIME5 2026-08-12 11:07:00] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:07:00] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:07:00] [INFO] [PolicyEngine5] MATCH intent='kg.remove_relation' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:07:00] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:07:00] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.remove_relation' → route='KG_REMOVE_RELATION'
[RUNTIME5 2026-08-12 11:07:00] [INFO] [WorkflowEngine5] Executing workflow step: KG_REMOVE_RELATION
[RUNTIME5 2026-08-12 11:07:00] [INFO] [KG_REMOVE_RELATION] Removing relation: entita -[ma_vlastnost]-> existuje
[RUNTIME5 2026-08-12 11:07:00] [INFO] [KG] Removed relation: entita -[ma_vlastnost]-> existuje
[RUNTIME5 2026-08-12 11:07:00] [INFO] [KG_REMOVE_RELATION] Relation removed: entita -[ma_vlastnost]-> existuje
--------------------------------------------------
{'status': 'OK', 'action': 'KG_REMOVE_RELATION', 'entity': 'entita', 'message': "Workflow step 'KG_REMOVE_RELATION' completed", 'data': {'status': 'ok', 'action': 'KG_REMOVE_RELATION', 'source': 'entita', 'relation': 'ma_vlastnost', 'target': 'existuje', 'message': 'Relation removed.'}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.explain entita
[RUNTIME5 2026-08-12 11:07:16] [INFO] [RuntimeCore] Processing input: {'input': 'kg.explain entita'}
[RUNTIME5 2026-08-12 11:07:16] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.explain entita
[RUNTIME5 2026-08-12 11:07:16] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.explain, entity='entita'
[RUNTIME5 2026-08-12 11:07:16] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'entita'
[RUNTIME5 2026-08-12 11:07:16] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:07:16] [INFO] [PolicyEngine5] MATCH intent='kg.explain' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:07:16] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:07:16] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.explain' → route='KG_EXPLAIN'
[RUNTIME5 2026-08-12 11:07:16] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXPLAIN
[RUNTIME5 2026-08-12 11:07:16] [INFO] [KG_EXPLAIN] Explaining entity: entita → resolved: entita
[RUNTIME5 2026-08-12 11:07:16] [INFO] [WHY] Hypothesis not provided → auto-detecting
--------------------------------------------------



--------------------------------------------------
{'status': 'OK', 'action': 'KG_EXPLAIN', 'entity': 'entita', 'message': "Workflow step 'KG_EXPLAIN' completed", 'data': {'status': 'ok', 'entity': 'entita', 'explanation': {'human': "No information about 'entita' is available to explain.", 'evidence': [], 'rule': None, 'confidence': 0.0}, 'tree': "\x1b[1;36mentita\x1b[0m\n ├─ \x1b[0;33mattributes\x1b[0m: (none)\n ├─ \x1b[0;35mrelations\x1b[0m\n │   ├─ (none)\n └─ \x1b[0;32mexplanation\x1b[0m\n     ├─ \x1b[0;32mhuman\x1b[0m: No information about 'entita' is available to explain.\n     ├─ \x1b[0;32mrule\x1b[0m: None\n     ├─ \x1b[0;32mconfidence\x1b[0m: 0.0\n     └─ \x1b[0;32mevidence\x1b[0m:", 'attributes': {}, 'relations': [], 'counts': {'attributes': 0, 'relations': 0, 'evidence': 0}}, 'counts': {'attributes': 0, 'relations': 0, 'neighbors': None}}
--------------------------------------------------
>>> kg.explain zviera
[RUNTIME5 2026-08-12 11:07:25] [INFO] [RuntimeCore] Processing input: {'input': 'kg.explain zviera'}
[RUNTIME5 2026-08-12 11:07:25] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.explain zviera
[RUNTIME5 2026-08-12 11:07:25] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.explain, entity='zviera'
[RUNTIME5 2026-08-12 11:07:25] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'zviera'
[RUNTIME5 2026-08-12 11:07:25] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:07:25] [INFO] [PolicyEngine5] MATCH intent='kg.explain' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:07:25] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:07:25] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.explain' → route='KG_EXPLAIN'
[RUNTIME5 2026-08-12 11:07:25] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXPLAIN
[RUNTIME5 2026-08-12 11:07:25] [INFO] [KG_EXPLAIN] Explaining entity: zviera → resolved: zviera
[RUNTIME5 2026-08-12 11:07:25] [INFO] [WHY] Hypothesis not provided → auto-detecting
[RUNTIME5 2026-08-12 11:07:25] [INFO] [WHY] Auto hypothesis (relation): zviera ma_vlastnost chlpaty
--------------------------------------------------



--------------------------------------------------
{'status': 'OK', 'action': 'KG_EXPLAIN', 'entity': 'zviera', 'message': "Workflow step 'KG_EXPLAIN' completed", 'data': {'status': 'ok', 'entity': 'zviera', 'explanation': {'human': 'Zviera -[ma_vlastnost]-> chlpaty. Therefore, zviera -[ma_vlastnost]-> chlpaty.', 'evidence': ['zviera -[ma_vlastnost]-> chlpaty'], 'rule': 'DirectFact', 'confidence': 1.0}, 'tree': '\x1b[1;36mzviera\x1b[0m\n ├─ \x1b[0;33mattributes\x1b[0m\n │   ├─ \x1b[0;33mtype\x1b[0m = zviera\n ├─ \x1b[0;35mrelations\x1b[0m\n │   ├─ \x1b[1;36mzviera\x1b[0m -[\x1b[0;35mma_vlastnost\x1b[0m]-> \x1b[1;36mchlpaty\x1b[0m\n └─ \x1b[0;32mexplanation\x1b[0m\n     ├─ \x1b[0;32mhuman\x1b[0m: Zviera -[ma_vlastnost]-> chlpaty. Therefore, zviera -[ma_vlastnost]-> chlpaty.\n     ├─ \x1b[0;32mrule\x1b[0m: DirectFact\n     ├─ \x1b[0;32mconfidence\x1b[0m: 1.0\n     └─ \x1b[0;32mevidence\x1b[0m:\n         ├─ zviera -[ma_vlastnost]-> chlpaty', 'attributes': {'type': 'zviera'}, 'relations': [{'source': 'zviera', 'relation': 'ma_vlastnost', 'target': 'chlpaty'}], 'counts': {'attributes': 1, 'relations': 1, 'evidence': 1}}, 'counts': {'attributes': 1, 'relations': 1, 'neighbors': None}}
--------------------------------------------------
>>> kg.infer entita
[RUNTIME5 2026-08-12 11:07:32] [INFO] [RuntimeCore] Processing input: {'input': 'kg.infer entita'}
[RUNTIME5 2026-08-12 11:07:32] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.infer entita
[RUNTIME5 2026-08-12 11:07:32] [INFO] [ReasoningEngine5] Starting reasoning for intent=UNKNOWN, entity='None'
[RUNTIME5 2026-08-12 11:07:32] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:07:32] [INFO] [PolicyEngine5] MATCH intent='UNKNOWN' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:07:32] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:07:32] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='UNKNOWN' → route='None'
[RUNTIME5 2026-08-12 11:07:32] [INFO] [WorkflowStepContinue5] Executing WORKFLOW_CONTINUE step
--------------------------------------------------
{'status': 'OK', 'action': 'WORKFLOW_CONTINUE', 'entity': None, 'message': 'Default workflow route', 'data': {'status': 'ok', 'reasoning': {'intent': 'UNKNOWN', 'entity': None, 'args': {'raw_input': 'kg.infer entita', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'mode': 'developer'}, 'reasoning_output': {'intent': 'UNKNOWN', 'entity': None, 'args': {'raw_input': 'kg.infer entita', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'mode': 'developer'}, 'route': 'DEFAULT', 'mode': 'developer', 'notes': 'Non-KG reasoning path.', 'degraded': False}}, 'notes': 'No workflow action required.'}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.stats
[RUNTIME5 2026-08-12 11:07:42] [INFO] [RuntimeCore] Processing input: {'input': 'kg.stats'}
[RUNTIME5 2026-08-12 11:07:42] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.stats
[RUNTIME5 2026-08-12 11:07:42] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.stats, entity='None'
[RUNTIME5 2026-08-12 11:07:42] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'None'
[RUNTIME5 2026-08-12 11:07:42] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:07:42] [INFO] [PolicyEngine5] MATCH intent='kg.stats' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:07:42] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:07:42] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.stats' → route='KG_STATS'
[RUNTIME5 2026-08-12 11:07:42] [INFO] [WorkflowEngine5] Executing workflow step: KG_STATS
[RUNTIME5 2026-08-12 11:07:42] [INFO] [KG_STATS] RAW DATA = {'intent': 'kg.stats', 'entity': None, 'args': {'mode': 'developer', 'raw_input': 'kg.stats', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'entity': None}, 'reasoning_output': {'intent': 'kg.stats', 'entity': None, 'args': {'mode': 'developer', 'raw_input': 'kg.stats', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'entity': None}, 'route': 'KG_STATS', 'mode': 'developer', 'degraded': False}}
[RUNTIME5 2026-08-12 11:07:42] [INFO] [KG_STATS] entities=11, relations=4, attributes=1, orphans=4
--------------------------------------------------
{'status': 'ok', 'action': 'KG_STATS', 'entities': 11, 'relations': 4, 'attributes': 1, 'orphans': 4, 'message': 'KG stats → entities=11, relations=4, attributes=1, orphans=4'}
--------------------------------------------------
>>> kg.export
[RUNTIME5 2026-08-12 11:07:55] [INFO] [RuntimeCore] Processing input: {'input': 'kg.export'}
[RUNTIME5 2026-08-12 11:07:55] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.export
[RUNTIME5 2026-08-12 11:07:55] [INFO] [ReasoningEngine5] Starting reasoning for intent=UNKNOWN, entity='None'
[RUNTIME5 2026-08-12 11:07:55] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:07:55] [INFO] [PolicyEngine5] MATCH intent='UNKNOWN' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:07:55] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:07:55] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='UNKNOWN' → route='None'
[RUNTIME5 2026-08-12 11:07:55] [INFO] [WorkflowStepContinue5] Executing WORKFLOW_CONTINUE step
--------------------------------------------------
{'status': 'OK', 'action': 'WORKFLOW_CONTINUE', 'entity': None, 'message': 'Default workflow route', 'data': {'status': 'ok', 'reasoning': {'intent': 'UNKNOWN', 'entity': None, 'args': {'raw_input': 'kg.export', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'mode': 'developer'}, 'reasoning_output': {'intent': 'UNKNOWN', 'entity': None, 'args': {'raw_input': 'kg.export', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'mode': 'developer'}, 'route': 'DEFAULT', 'mode': 'developer', 'notes': 'Non-KG reasoning path.', 'degraded': False}}, 'notes': 'No workflow action required.'}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> kg.import autosave_kg.json
[RUNTIME5 2026-08-12 11:08:04] [INFO] [RuntimeCore] Processing input: {'input': 'kg.import autosave_kg.json'}
[RUNTIME5 2026-08-12 11:08:04] [INFO] [RuntimeCore] Normalized input (KG-safe): kg.import autosave_kg.json
[RUNTIME5 2026-08-12 11:08:04] [INFO] [ReasoningEngine5] Starting reasoning for intent=UNKNOWN, entity='None'
[RUNTIME5 2026-08-12 11:08:04] [INFO] [RuntimeCore] COLNIK identity=OWNER
[RUNTIME5 2026-08-12 11:08:04] [INFO] [PolicyEngine5] MATCH intent='UNKNOWN' → effect=ALLOW (Default allow.)
[RUNTIME5 2026-08-12 11:08:04] [INFO] [BehaviorFilter5] OWNER_BYPASS_BEHAVIOR – OWNER má plný prístup
[RUNTIME5 2026-08-12 11:08:04] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='UNKNOWN' → route='None'
[RUNTIME5 2026-08-12 11:08:04] [INFO] [WorkflowStepContinue5] Executing WORKFLOW_CONTINUE step
--------------------------------------------------
{'status': 'OK', 'action': 'WORKFLOW_CONTINUE', 'entity': None, 'message': 'Default workflow route', 'data': {'status': 'ok', 'reasoning': {'intent': 'UNKNOWN', 'entity': None, 'args': {'raw_input': 'kg.import autosave_kg.json', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'mode': 'developer'}, 'reasoning_output': {'intent': 'UNKNOWN', 'entity': None, 'args': {'raw_input': 'kg.import autosave_kg.json', 'anchor': {'source': None, 'relation': None, 'target': None, 'error': 'Missing relation'}, 'mode': 'developer'}, 'route': 'DEFAULT', 'mode': 'developer', 'notes': 'Non-KG reasoning path.', 'degraded': False}}, 'notes': 'No workflow action required.'}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> ^Z

Exiting Runtime5 CLI.
[RUNTIME5 2026-08-12 11:11:33] [INFO] [KGExportImport5] EXPORT OK → autosave_kg.json
[RUNTIME5 2026-08-12 11:11:33] [INFO] [RuntimeCore] AUTOSAVE completed → autosave_kg.json (entities=11, relations=4)
[RUNTIME5 2026-08-12 11:11:34] [INFO] [KGExportImport5] EXPORT OK → autosave_kg.json
[RUNTIME5 2026-08-12 11:11:34] [INFO] [SystemHooks5] AUTOSAVE completed → autosave_kg.json (11 entities, 4 relations)
[RUNTIME5 2026-08-12 11:11:34] [INFO] [RuntimeCore] Shutdown complete.
