C:\Users\richa\SIRIUS-LOCAL-AI-BETA>python -m runtime5.runtime5_cli
[RUNTIME5 2026-07-11 08:39:05] [INFO] [RuntimeCore] Initializing Runtime 5.x
[RUNTIME5 2026-07-11 08:39:05] [INFO] [PermissionLayer5] Initialized ENVOY Permission Layer 5.x
[RUNTIME5 2026-07-11 08:39:05] [INFO] [PolicyEngine5] Loaded 4 rules.
[RUNTIME5 2026-07-11 08:39:05] [INFO] [PermissionLayer5] PolicyEngine5 loaded.
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KnowledgeGraph] Initialized KG Core (Unified Schema)
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: earth
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: earth.type = planet
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: earth.mass = 5.97e24
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: earth.radius = 6371km
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: earth.inferred_type = planet_orbiting_star
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: sun
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: sun.type = star
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: moon
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: moon.type = planet
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: moon.orbits_star = True
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: moon.inferred_root = sun
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: moon.inferred_type = planet_orbiting_star
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: pes
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: pes.type = zviera
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: pes.ma_fyzicka_vlastnost = True
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: chlpaty
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: fyzicka_vlastnost
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: cicavec
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: zviera
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: co
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: planet
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added entity: mars
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Set attribute: mars.type = planet
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: earth -[orbits]-> sun
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: moon -[orbits]-> earth
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: pes -[ma_vlastnost]-> chlpaty
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: chlpaty -[dedicnost]-> fyzicka_vlastnost
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: pes -[je_v]-> cicavec
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: cicavec -[je_v]-> zviera
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: moon -[orbits]-> sun
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: co -[je]-> zviera
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KG] Added relation: mars -[orbits]-> sun
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KGExportImport5] AUTOLOAD completed: entities=11, relations=9
[RUNTIME5 2026-07-11 08:39:05] [INFO] [RuntimeCore] AUTOLOAD completed → autosave_kg.json (entities=11, relations=9)
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KGQuery] Initialized query engine (Unified Schema).
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KGReasoner] Initialized reasoning engine.
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KGRouter] Initialized KG router 5.x
[RUNTIME5 2026-07-11 08:39:05] [INFO] [KGLight5] Initialized KG Light module
[RUNTIME5 2026-07-11 08:39:05] [INFO] [EnvoyQuarantine5] Initialized minimal quarantine store
[RUNTIME5 2026-07-11 08:39:05] [INFO] [EnvoyNormalizer5] Initialized normalizer 5.x
[RUNTIME5 2026-07-11 08:39:05] [INFO] [EnvoyExecutionLayer5] Initialized ENVOY Execution Layer 5.x (shared runtime)
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: WORKFLOW_CONTINUE
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: ENVOY_LEVEL1
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: COMPARE
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_LIGHT
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_ADD
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_REMOVE
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_RELATE
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_RELATIONS
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_VIEW
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_PATH
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_QUERY
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPORT
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_IMPORT
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_BACKUP
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_RESTORE
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_SET
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_GET
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_LIST
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_SEARCH
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_ATTRIBUTES
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: REASON_ORBITS
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_UNSET
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_RENAME
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXISTS
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_STATS
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_DELETE
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: REASON_INFER
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLAIN
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLAIN_DEEP
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_REMOVE_RELATION
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLORE
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowStepRegistry5] Default steps initialized
[RUNTIME5 2026-07-11 08:39:05] [INFO] [WorkflowEngine5] Initialized workflow engine.
[RUNTIME5 2026-07-11 08:39:05] [INFO] [SelfRepair5] Initialized self-repair layer 5.4
[RUNTIME5 2026-07-11 08:39:05] [INFO] [SystemAgent5] Initializing system agent
[RUNTIME5 2026-07-11 08:39:05] [INFO] [ReasoningEngine5] Initialized reasoning engine.
[RUNTIME5 2026-07-11 08:39:05] [INFO] [RRE] Registered rule: OrbitTypeInferenceRule
[RUNTIME5 2026-07-11 08:39:05] [INFO] [RRE] Registered rule: AutoTypeInferenceRule
[RUNTIME5 2026-07-11 08:39:05] [INFO] [RRE] Registered rule: MultiHopOrbitInferenceRule
[RUNTIME5 2026-07-11 08:39:05] [INFO] [RRE] Registered rule: DedicsnostVlastnostiRule
[RUNTIME5 2026-07-11 08:39:05] [INFO] [RRE] Registered rule: TranzitivneRelacieRule
[RUNTIME5 2026-07-11 08:39:05] [INFO] [InputParser5] Initialized Input Parser 5.x
[RUNTIME5 2026-07-11 08:39:05] [INFO] [BehaviorFilter5] Initialized behavior filter 5.x
[RUNTIME5 2026-07-11 08:39:05] [INFO] [FamilySafetyRules5_x] Initialized Family Safety Rules 5.x
[RUNTIME5 2026-07-11 08:39:05] [INFO] [ContextualBehaviorEngine5] Initialized
[RUNTIME5 2026-07-11 08:39:05] [INFO] [RuntimeCore] Initialization complete
[RUNTIME5 2026-07-11 08:39:05] [INFO] [BehaviorFilter5] Initialized behavior filter 5.x
[RUNTIME5 2026-07-11 08:39:05] [INFO] [Runtime5CLI] Initialized (v5.3.0)
Runtime5 CLI ready.
>>> kg explore mars
[RUNTIME5 2026-07-11 08:39:18] [INFO] [RuntimeCore] Processing input: kg explore mars
[RUNTIME5 2026-07-11 08:39:18] [INFO] [RuntimeCore] Normalized input: kg explore mars
[RUNTIME5 2026-07-11 08:39:18] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.explore, entity='mars'
[RUNTIME5 2026-07-11 08:39:18] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.explore' → route='KG_EXPLORE'
[RUNTIME5 2026-07-11 08:39:18] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXPLORE
[RUNTIME5 2026-07-11 08:39:18] [INFO] [KG_EXPLORE] Exploring graph around: mars
[RUNTIME5 2026-07-11 08:39:18] [INFO] [KGQuery] Multi-hop traversal from 'mars' completed (depth=2).
--------------------------------------------------
{'status': 'ok', 'action': 'KG_EXPLORE', 'entity': 'mars', 'tree': {'entity': 'mars', 'outbound': [{'source': 'mars', 'relation': 'orbits', 'target': 'sun'}], 'inbound': [], 'neighbors': {'start': 'mars', 'levels': [{'depth': 0, 'nodes': ['mars'], 'edges': [{'source': 'mars', 'relation': 'orbits', 'target': 'sun'}]}, {'depth': 1, 'nodes': ['sun'], 'edges': [{'source': 'earth', 'relation': 'orbits', 'target': 'sun'}, {'source': 'moon', 'relation': 'orbits', 'target': 'sun'}, {'source': 'mars', 'relation': 'orbits', 'target': 'sun'}]}]}, 'ascii': '\x1b[1;36mmars\x1b[0m\n ├─ \x1b[0;33mattributes\x1b[0m\n │   └─ \x1b[0;33mtype\x1b[0m = planet\n ├─ \x1b[0;35moutbound\x1b[0m\n │   └─ \x1b[1;36mmars\x1b[0m -[\x1b[0;35morbits\x1b[0m]-> \x1b[1;36msun\x1b[0m\n ├─ \x1b[0;35minbound\x1b[0m\n │   └─ (none)\n └─ \x1b[0;32mneighbors\x1b[0m\n     depth 0:\n       \x1b[1;36mmars\x1b[0m\n     depth 1:\n       \x1b[1;36msun\x1b[0m'}, 'ascii': '\x1b[1;36mmars\x1b[0m\n ├─ \x1b[0;33mattributes\x1b[0m\n │   └─ \x1b[0;33mtype\x1b[0m = planet\n ├─ \x1b[0;35moutbound\x1b[0m\n │   └─ \x1b[1;36mmars\x1b[0m -[\x1b[0;35morbits\x1b[0m]-> \x1b[1;36msun\x1b[0m\n ├─ \x1b[0;35minbound\x1b[0m\n │   └─ (none)\n └─ \x1b[0;32mneighbors\x1b[0m\n     depth 0:\n       \x1b[1;36mmars\x1b[0m\n     depth 1:\n       \x1b[1;36msun\x1b[0m', 'message': "Graph exploration for 'mars' completed."}
--------------------------------------------------
>>> kg explain mars
[RUNTIME5 2026-07-11 08:40:36] [INFO] [RuntimeCore] Processing input: kg explain mars
[RUNTIME5 2026-07-11 08:40:36] [INFO] [RuntimeCore] Normalized input: kg explain mars
[RUNTIME5 2026-07-11 08:40:36] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.explain, entity='mars'
[RUNTIME5 2026-07-11 08:40:36] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.explain' → route='KG_EXPLAIN'
[RUNTIME5 2026-07-11 08:40:36] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXPLAIN
[RUNTIME5 2026-07-11 08:40:36] [INFO] [KG_EXPLAIN] Explaining entity: mars → resolved: mars
--------------------------------------------------
{'status': 'ok', 'entity': 'mars', 'tree': 'mars\n ├─ attributes\n │   └─ type = planet\n └─ relations\n     └─ mars -[orbits]-> sun', 'attributes': {'name': 'mars', 'attributes': {'type': 'planet'}}, 'relations': [{'source': 'mars', 'relation': 'orbits', 'target': 'sun'}], 'attributes_count': 1, 'relations_count': 1}
--------------------------------------------------
>>> kg explain deep mars
[RUNTIME5 2026-07-11 08:40:49] [INFO] [RuntimeCore] Processing input: kg explain deep mars
[RUNTIME5 2026-07-11 08:40:49] [INFO] [RuntimeCore] Normalized input: kg explain deep mars
[RUNTIME5 2026-07-11 08:40:49] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.explain_deep, entity='mars'
[RUNTIME5 2026-07-11 08:40:49] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.explain_deep' → route='KG_EXPLAIN_DEEP'
[RUNTIME5 2026-07-11 08:40:49] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXPLAIN_DEEP
[RUNTIME5 2026-07-11 08:40:49] [INFO] [KG_EXPLAIN_DEEP] Deep explanation for: mars → mars
--------------------------------------------------
{'status': 'ok', 'entity': 'mars', 'tree': '\x1b[1;36mmars\x1b[0m\n ├─ \x1b[0;33mattributes\x1b[0m\n │   └─ \x1b[0;33mtype\x1b[0m = planet\n ├─ \x1b[0;35mrelations\x1b[0m\n │   └─ \x1b[1;36mmars\x1b[0m -[\x1b[0;35morbits\x1b[0m]-> \x1b[1;36msun\x1b[0m\n ├─ \x1b[0;32mreasoning\x1b[0m\n │   ├─ \x1b[0;32mAutoTypeInferenceRule → mars.type = planet\x1b[0m\n │   └─ \x1b[0;32mMultiHopOrbitInferenceRule → mars orbits sun\x1b[0m\n └─ \x1b[1;36mdeep_traversal\x1b[0m\n     mars\n       mars -[orbits]-> sun\n       sun\n         earth -[orbits]-> sun\n         moon -[orbits]-> sun\n         mars -[orbits]-> sun', 'root_attributes': {'name': 'mars', 'attributes': {'type': 'planet'}}, 'root_relations': [{'source': 'mars', 'relation': 'orbits', 'target': 'sun'}], 'reasoning': {'entity': 'mars', 'steps': ['AutoTypeInferenceRule → mars.type = planet', 'MultiHopOrbitInferenceRule → mars orbits sun']}, 'deep_traversal': ['mars', '  mars -[orbits]-> sun', '  sun', '    earth -[orbits]-> sun', '    moon -[orbits]-> sun', '    mars -[orbits]-> sun'], 'deep_nodes_count': 2}
--------------------------------------------------
>>> ^Z

Exiting Runtime5 CLI.
[RUNTIME5 2026-07-11 09:35:55] [INFO] [KGExportImport5] EXPORT OK → autosave_kg.json
[RUNTIME5 2026-07-11 09:35:55] [INFO] [RuntimeCore] AUTOSAVE completed → autosave_kg.json (entities=11, relations=9)
[RUNTIME5 2026-07-11 09:35:55] [INFO] [KGExportImport5] EXPORT OK → autosave_kg.json
[RUNTIME5 2026-07-11 09:35:55] [INFO] [SystemHooks5] AUTOSAVE completed → autosave_kg.json (11 entities, 9 relations)
[RUNTIME5 2026-07-11 09:35:55] [INFO] [RuntimeCore] Shutdown complete.
