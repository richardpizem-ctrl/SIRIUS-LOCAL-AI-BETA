C:\Users\richa\SIRIUS-LOCAL-AI-5.6.0-CLEAN>python runtime5_cli.py
[RUNTIME5 2026-07-29 05:39:07] [INFO] [RuntimeCore] Initializing Runtime 5.x
[RUNTIME5 2026-07-29 05:39:07] [INFO] [PermissionLayer5] Initialized ENVOY Permission Layer 5.x
[RUNTIME5 2026-07-29 05:39:07] [INFO] [PolicyEngine5] Loaded 4 rules.
[RUNTIME5 2026-07-29 05:39:07] [INFO] [PermissionLayer5] PolicyEngine5 loaded.
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KnowledgeGraph] Initialized KG Core (Unified Schema)
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added entity: auto
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Set attribute: auto.color = red
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added entity: osoba
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added entity: zviera
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added entity: organizmus
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added entity: entita
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added entity: chlpaty
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added entity: pes
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Set attribute: pes.type = zviera
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added entity: je
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: osoba -[owns]-> auto
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: zviera -[je]-> organizmus
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: organizmus -[je]-> entita
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: pes -[je]-> organizmus
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: zviera -[je]-> entita
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: pes -[je]-> zviera
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: pes -[je]-> entita
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: pes -[orbits]-> entita
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: entita -[orbits]-> organizmus
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: pes -[orbits]-> organizmus
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG] Added relation: zviera -[ma_vlastnost]-> chlpaty
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KGExportImport5] AUTOLOAD completed: entities=8, relations=11
[RUNTIME5 2026-07-29 05:39:07] [INFO] [RuntimeCore] AUTOLOAD completed → autosave_kg.json (entities=8, relations=11)
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KGQuery] Initialized query engine (Unified Schema).
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KGReasoner] Initialized reasoning engine.
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KGReasoner] Linked to ReasoningRulesEngine5.
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KGRouter] Initialized KG router 5.x
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KGLight5] Initialized KG Light module
[RUNTIME5 2026-07-29 05:39:07] [INFO] [EnvoyQuarantine5] Initialized minimal quarantine store
[RUNTIME5 2026-07-29 05:39:07] [INFO] [EnvoyNormalizer5] Initialized normalizer 5.x
[RUNTIME5 2026-07-29 05:39:07] [INFO] [EnvoyExecutionLayer5] Initialized ENVOY Execution Layer 5.x (shared runtime)
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: WORKFLOW_CONTINUE
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: ENVOY_LEVEL1
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: COMPARE
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_LIGHT
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_ADD
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_REMOVE
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_RELATE
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_RELATIONS
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_VIEW
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_PATH
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_QUERY
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPORT
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_IMPORT
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_BACKUP
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_RESTORE
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_SET
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_GET
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG_UNSET] Initialized KG_UNSET step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_UNSET
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG_LIST] Initialized KG_LIST step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_LIST
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG_SEARCH] Initialized KG_SEARCH step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_SEARCH
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG_RENAME] Initialized KG_RENAME step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_RENAME
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG_EXISTS] Initialized KG_EXISTS step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXISTS
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG_STATS] Initialized KG_STATS step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_STATS
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG_DELETE] Initialized KG_DELETE step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_DELETE
[RUNTIME5 2026-07-29 05:39:07] [INFO] [KG_MERGE] Initialized KG_MERGE step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_MERGE
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_ATTRIBUTES
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: REASON_ORBITS
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepReasonInfer5] Initialized REASON_INFER step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: REASON_INFER
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_INFER
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLAIN
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLAIN_DEEP
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_REMOVE_RELATION
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: KG_EXPLORE
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepReasonWhy5] Initialized REASON_WHY step
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Registered step: REASON_WHY
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowStepRegistry5] Default steps initialized
[RUNTIME5 2026-07-29 05:39:07] [INFO] [WorkflowEngine5] Initialized workflow engine.
[RUNTIME5 2026-07-29 05:39:07] [INFO] [SelfRepair5] Initialized self-repair layer 5.4
[RUNTIME5 2026-07-29 05:39:07] [INFO] [SystemAgent5] Initializing system agent
[RUNTIME5 2026-07-29 05:39:07] [INFO] [ReasoningEngine5] Initialized reasoning engine.
[RUNTIME5 2026-07-29 05:39:07] [INFO] [RRE] Registered rule: OrbitTypeInferenceRule
[RUNTIME5 2026-07-29 05:39:07] [INFO] [RRE] Registered rule: AutoTypeInferenceRule
[RUNTIME5 2026-07-29 05:39:07] [INFO] [RRE] Registered rule: MultiHopOrbitInferenceRule
[RUNTIME5 2026-07-29 05:39:07] [INFO] [RRE] Registered rule: DedicsnostVlastnostiRule
[RUNTIME5 2026-07-29 05:39:07] [INFO] [RRE] Registered rule: TranzitivneRelacieRule
[RUNTIME5 2026-07-29 05:39:07] [INFO] [InputParser5] Initialized Input Parser 5.x
[RUNTIME5 2026-07-29 05:39:07] [INFO] [BehaviorFilter5] Initialized behavior filter 5.x
[RUNTIME5 2026-07-29 05:39:07] [INFO] [FamilySafetyRules5_x] Initialized Family Safety Rules 5.x
[RUNTIME5 2026-07-29 05:39:07] [INFO] [ContextualBehaviorEngine5] Initialized
[RUNTIME5 2026-07-29 05:39:07] [INFO] [RuntimeCore] Initialization complete
[RUNTIME5 2026-07-29 05:39:07] [INFO] [BehaviorFilter5] Initialized behavior filter 5.x
[RUNTIME5 2026-07-29 05:39:07] [INFO] [Runtime5CLI] Initialized (v5.3.0)
Runtime5 CLI ready.
>>> kg explore pes
[RUNTIME5 2026-07-29 05:40:03] [INFO] [RuntimeCore] Processing input: {'input': 'kg explore pes'}
[RUNTIME5 2026-07-29 05:40:03] [INFO] [RuntimeCore] Normalized input (KG-safe): kg explore pes
[RUNTIME5 2026-07-29 05:40:03] [INFO] [ReasoningEngine5] Starting reasoning for intent=kg.explore, entity='pes'
[RUNTIME5 2026-07-29 05:40:03] [INFO] [ReasoningEngine5] FIXED KG ENTITY → 'pes'
[RUNTIME5 2026-07-29 05:40:03] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='kg.explore' → route='KG_EXPLORE'
[RUNTIME5 2026-07-29 05:40:03] [INFO] [WorkflowEngine5] Executing workflow step: KG_EXPLORE
[RUNTIME5 2026-07-29 05:40:03] [INFO] [KG_EXPLORE] Exploring graph around: pes
[RUNTIME5 2026-07-29 05:40:03] [INFO] [KGQuery] Multi-hop traversal from 'pes' completed (depth=2).
--------------------------------------------------
{'status': 'OK', 'action': 'KG_EXPLORE', 'entity': 'pes', 'message': "Workflow step 'KG_EXPLORE' completed", 'data': {'status': 'ok', 'action': 'KG_EXPLORE', 'entity': 'pes', 'tree': {'entity': 'pes', 'outbound': [{'source': 'pes', 'relation': 'je', 'target': 'organizmus'}, {'source': 'pes', 'relation': 'je', 'target': 'zviera'}, {'source': 'pes', 'relation': 'je', 'target': 'entita'}, {'source': 'pes', 'relation': 'orbits', 'target': 'entita'}, {'source': 'pes', 'relation': 'orbits', 'target': 'organizmus'}], 'inbound': [], 'neighbors': {'start': 'pes', 'levels': [{'depth': 0, 'nodes': ['pes'], 'edges': [{'source': 'pes', 'relation': 'je', 'target': 'organizmus'}, {'source': 'pes', 'relation': 'je', 'target': 'zviera'}, {'source': 'pes', 'relation': 'je', 'target': 'entita'}, {'source': 'pes', 'relation': 'orbits', 'target': 'entita'}, {'source': 'pes', 'relation': 'orbits', 'target': 'organizmus'}]}, {'depth': 1, 'nodes': ['organizmus', 'zviera', 'entita'], 'edges': [{'source': 'zviera', 'relation': 'je', 'target': 'organizmus'}, {'source': 'organizmus', 'relation': 'je', 'target': 'entita'}, {'source': 'pes', 'relation': 'je', 'target': 'organizmus'}, {'source': 'entita', 'relation': 'orbits', 'target': 'organizmus'}, {'source': 'pes', 'relation': 'orbits', 'target': 'organizmus'}, {'source': 'zviera', 'relation': 'je', 'target': 'organizmus'}, {'source': 'zviera', 'relation': 'je', 'target': 'entita'}, {'source': 'pes', 'relation': 'je', 'target': 'zviera'}, {'source': 'zviera', 'relation': 'ma_vlastnost', 'target': 'chlpaty'}, {'source': 'organizmus', 'relation': 'je', 'target': 'entita'}, {'source': 'zviera', 'relation': 'je', 'target': 'entita'}, {'source': 'pes', 'relation': 'je', 'target': 'entita'}, {'source': 'pes', 'relation': 'orbits', 'target': 'entita'}, {'source': 'entita', 'relation': 'orbits', 'target': 'organizmus'}]}]}, 'ascii': '\x1b[1;36mpes\x1b[0m\n ├─ \x1b[0;33mattributes\x1b[0m\n │   └─ \x1b[0;33mtype\x1b[0m = zviera\n ├─ \x1b[0;35moutbound\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35mje\x1b[0m]-> \x1b[1;36morganizmus\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35mje\x1b[0m]-> \x1b[1;36mzviera\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35mje\x1b[0m]-> \x1b[1;36mentita\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35morbits\x1b[0m]-> \x1b[1;36mentita\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35morbits\x1b[0m]-> \x1b[1;36morganizmus\x1b[0m\n ├─ \x1b[0;35minbound\x1b[0m\n │   └─ (none)\n └─ \x1b[0;32mneighbors\x1b[0m\n     depth 0:\n       \x1b[1;36mpes\x1b[0m\n     depth 1:\n       \x1b[1;36morganizmus\x1b[0m\n       \x1b[1;36mzviera\x1b[0m\n       \x1b[1;36mentita\x1b[0m'}, 'ascii': '\x1b[1;36mpes\x1b[0m\n ├─ \x1b[0;33mattributes\x1b[0m\n │   └─ \x1b[0;33mtype\x1b[0m = zviera\n ├─ \x1b[0;35moutbound\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35mje\x1b[0m]-> \x1b[1;36morganizmus\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35mje\x1b[0m]-> \x1b[1;36mzviera\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35mje\x1b[0m]-> \x1b[1;36mentita\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35morbits\x1b[0m]-> \x1b[1;36mentita\x1b[0m\n │   └─ \x1b[1;36mpes\x1b[0m -[\x1b[0;35morbits\x1b[0m]-> \x1b[1;36morganizmus\x1b[0m\n ├─ \x1b[0;35minbound\x1b[0m\n │   └─ (none)\n └─ \x1b[0;32mneighbors\x1b[0m\n     depth 0:\n       \x1b[1;36mpes\x1b[0m\n     depth 1:\n       \x1b[1;36morganizmus\x1b[0m\n       \x1b[1;36mzviera\x1b[0m\n       \x1b[1;36mentita\x1b[0m', 'message': "Graph exploration for 'pes' completed."}, 'counts': {'attributes': None, 'relations': None, 'neighbors': None}}
--------------------------------------------------
>>> ^Z

Exiting Runtime5 CLI.
[RUNTIME5 2026-07-29 05:41:41] [INFO] [KGExportImport5] EXPORT OK → autosave_kg.json
[RUNTIME5 2026-07-29 05:41:41] [INFO] [RuntimeCore] AUTOSAVE completed → autosave_kg.json (entities=8, relations=11)
[RUNTIME5 2026-07-29 05:41:41] [INFO] [KGExportImport5] EXPORT OK → autosave_kg.json
[RUNTIME5 2026-07-29 05:41:41] [INFO] [SystemHooks5] AUTOSAVE completed → autosave_kg.json (8 entities, 11 relations)
[RUNTIME5 2026-07-29 05:41:41] [INFO] [RuntimeCore] Shutdown complete.
