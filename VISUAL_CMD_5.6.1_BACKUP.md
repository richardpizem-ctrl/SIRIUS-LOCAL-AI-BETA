STATUS: This release 5.6.1 will be available soon on GitHub as a ZIP package in the Releases section once the compilation is complete.
C:\Users\richa\SIRIUS-LOCAL-AI-BETA>python -m runtime5.runtime5_cli
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RuntimeCore] Initializing Runtime 5.x
[RUNTIME5 2026-07-17 16:49:00] [INFO] [PermissionLayer5] Initialized ENVOY Permission Layer 5.x
[RUNTIME5 2026-07-17 16:49:00] [INFO] [PolicyEngine5] Loaded 4 rules.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [PermissionLayer5] PolicyEngine5 loaded.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KnowledgeGraph] Initialized KG Core
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_BOOTSTRAP] Loading default ontology
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Added class: animal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Added class: mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Added class: bird
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Added class: reptile
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Added class: planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Added class: star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Instance: dog : mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: dog.type = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: dog.instance_of = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Instance: cat : mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: cat.type = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: cat.instance_of = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Instance: lion : mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: lion.type = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: lion.instance_of = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Instance: earth : planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: earth.type = planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: earth.instance_of = planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Instance: sun : star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: sun.type = star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: sun.instance_of = star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Property: alive, domains=['animal']
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Property: mobile, domains=['animal']
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Property: biological, domains=['animal']
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Property: warm_blooded, domains=['mammal', 'bird']
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Property: carnivore, domains=['animal']
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG_ONTOLOGY] Property: herbivore, domains=['animal']
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Updated entity: dog
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: dog.type = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: dog.instance_of = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Updated entity: cat
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: cat.type = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: cat.instance_of = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Updated entity: lion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: lion.type = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: lion.instance_of = mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Updated entity: earth
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: earth.type = planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: earth.instance_of = planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: earth.mass = 5.97e24
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: earth.radius = 6371km
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: earth.inferred_type = planet_orbiting_star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Updated entity: sun
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: sun.type = star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: sun.instance_of = star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: moon
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: moon.type = natural_satellite
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: moon.inferred_root = sun
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: moon.instance_of = natural_satellite
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: hairy
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: physical_property
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: mammal.type = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: mammal.description = Animal that is warm-blooded, has hair, and produces milk.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: mammal.instance_of = animal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: animal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.type = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.description = Organism capable of movement, feeding, and sensory perception.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.instance_of = organism
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.alive = true
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.mobile = true
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.biological = true
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.warm_blooded = true
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.vertebrate = true
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.mammal = true
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: animal.carnivore = true
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: organism
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: organism.type = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: organism.description = Living biological entity.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: organism.instance_of = living_thing
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: living_thing
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: living_thing.type = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: living_thing.description = Entity that exhibits life processes.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: living_thing.instance_of = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: planet.type = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: planet.description = Celestial body orbititing a star, without its own fusion.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: planet.instance_of = astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: mars
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: mars.type = planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: mars.inferred_type = planet_orbiting_star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: mars.instance_of = planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: spherical
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: massive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: no_fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: star.type = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: star.description = Self-luminous celestial body producing energy through nuclear fusion.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: star.instance_of = astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: luminous
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: natural_satellite
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: natural_satellite.type = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: natural_satellite.description = Celestial body orbiting a planet.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: natural_satellite.instance_of = astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: warm_blooded
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: hair
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: milk_production
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: alive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: mobile
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: biological
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: astronomical_body.type = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: astronomical_body.description = General category for celestial objects.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Set attribute: astronomical_body.instance_of = category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: car
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added entity: engine
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: earth -[orbits]-> sun
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mars -[orbits]-> sun
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: planet -[has_property]-> spherical
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: planet -[has_property]-> massive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: planet -[has_property]-> no_fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: star -[has_property]-> luminous
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: star -[has_property]-> fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: star -[has_property]-> massive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: natural_satellite -[orbits]-> planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: natural_satellite -[has_property]-> no_fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: moon -[orbits]-> planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: moon -[has_property]-> spherical
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: moon -[has_property]-> massive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: moon -[has_property]-> no_fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: natural_satellite -[category]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: moon -[category]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: animal -[has_property]-> alive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: animal -[has_property]-> mobile
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: animal -[has_property]-> biological
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[has_property]-> warm_blooded
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[has_property]-> hair
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[has_property]-> milk_production
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: earth -[has_property]-> spherical
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: earth -[has_property]-> massive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: earth -[has_property]-> no_fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: sun -[has_property]-> luminous
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: sun -[has_property]-> fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: sun -[has_property]-> massive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[has_property]-> alive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[has_property]-> mobile
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[has_property]-> biological
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[has_property]-> alive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[has_property]-> mobile
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[has_property]-> biological
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mars -[has_property]-> spherical
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mars -[has_property]-> massive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mars -[has_property]-> no_fusion
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[is_a]-> animal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: earth -[is_a]-> planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mars -[is_a]-> planet
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: moon -[is_a]-> natural_satellite
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: sun -[is_a]-> star
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[is_a]-> mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: animal -[is_a]-> organism
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: organism -[is_a]-> living_thing
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: living_thing -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: planet -[is_a]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: star -[is_a]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: natural_satellite -[is_a]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[is_a]-> mammal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[is_a]-> animal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: car -[has_part]-> engine
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[is_a]-> animal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[has_property]-> warm_blooded
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[has_property]-> hair
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[has_property]-> milk_production
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[has_property]-> warm_blooded
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[has_property]-> hair
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[has_property]-> milk_production
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[has_property]-> alive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[has_property]-> mobile
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[has_property]-> biological
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[has_property]-> warm_blooded
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[has_property]-> hair
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[has_property]-> milk_production
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[has_property]-> alive
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[has_property]-> mobile
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[has_property]-> biological
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[is_a]-> animal
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: earth -[is_a]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: sun -[is_a]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: moon -[is_a]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[is_a]-> organism
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: animal -[is_a]-> living_thing
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: organism -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mars -[is_a]-> astronomical_body
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[is_a]-> organism
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[is_a]-> organism
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[is_a]-> organism
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[is_a]-> living_thing
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: animal -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: dog -[is_a]-> living_thing
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: cat -[is_a]-> living_thing
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: lion -[is_a]-> living_thing
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KG] Added relation: mammal -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KGExportImport5] AUTOLOAD completed: entities=31, relations=85
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RuntimeCore] AUTOLOAD completed → autosave_kg.json
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KGQuery] Initialized query engine (Unified Schema).
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KGReasoner] Initialized reasoning engine.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KGRouter] Initialized KG router 5.x (ReasoningEngine5 enabled)
[RUNTIME5 2026-07-17 16:49:00] [INFO] [KGLight5] Initialized KG Light module
[RUNTIME5 2026-07-17 16:49:00] [INFO] [EnvoyQuarantine5] Initialized minimal quarantine store
[RUNTIME5 2026-07-17 16:49:00] [INFO] [EnvoyNormalizer5] Initialized normalizer 5.x
[RUNTIME5 2026-07-17 16:49:00] [INFO] [EnvoyExecutionLayer5] Initialized ENVOY Execution Layer 5.x (shared runtime)
[RUNTIME5 2026-07-17 16:49:00] [INFO] [WorkflowEngine5] Initialized workflow engine 5.x
[RUNTIME5 2026-07-17 16:49:00] [INFO] [SelfRepair5] Initialized self-repair layer 5.4
[RUNTIME5 2026-07-17 16:49:00] [INFO] [SystemAgent5] Initializing system agent
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Initialized reasoning engine.
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RRE] Registered rule: OrbitTypeInferenceRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Registered rule: OrbitTypeInferenceRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RRE] Registered rule: AutoTypeInferenceRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Registered rule: AutoTypeInferenceRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RRE] Registered rule: MultiHopOrbitInferenceRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Registered rule: MultiHopOrbitInferenceRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RRE] Registered rule: PropertyInheritanceRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Registered rule: PropertyInheritanceRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RRE] Registered rule: TransitiveRelationsRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Registered rule: TransitiveRelationsRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RRE] Registered rule: InheritanceCategoryRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Registered rule: InheritanceCategoryRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RRE] Registered rule: InheritancePropertiesRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Registered rule: InheritancePropertiesRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RRE] Registered rule: InheritanceRelationsRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ReasoningEngine5] Registered rule: InheritanceRelationsRule
[RUNTIME5 2026-07-17 16:49:00] [INFO] [IntentResolver5] Initialized intent resolver 5.x
[RUNTIME5 2026-07-17 16:49:00] [INFO] [FamilySafetyRules5_x] Initialized Family Safety Rules 5.x
[RUNTIME5 2026-07-17 16:49:00] [INFO] [BehaviorFilter5] Initialized behavior filter 5.x
[RUNTIME5 2026-07-17 16:49:00] [INFO] [ContextualBehaviorEngine5] Initialized
[RUNTIME5 2026-07-17 16:49:00] [INFO] [RuntimeCore] Initialization complete
[RUNTIME5 2026-07-17 16:49:00] [INFO] [BehaviorFilter5] Initialized behavior filter 5.x
[RUNTIME5 2026-07-17 16:49:00] [INFO] [Runtime5CLI] Initialized (v5.3.0)
Runtime5 CLI ready.
>>> KG_EXPLAIN moon
[RUNTIME5 2026-07-17 16:49:07] [INFO] [RuntimeCore] Processing input: KG_EXPLAIN moon
[RUNTIME5 2026-07-17 16:49:07] [INFO] [RuntimeCore] Normalized input: kg_explain moon
[RUNTIME5 2026-07-17 16:49:07] [INFO] [IntentResolver5] Resolving intent for input: 'kg_explain moon'
[RUNTIME5 2026-07-17 16:49:07] [INFO] [WorkflowEngine5] ROUTE RESOLVE intent='KG_EXPLAIN' → route='None'
[RUNTIME5 2026-07-17 16:49:07] [INFO] [KG_EXPLAIN] Explaining entity: moon → resolved: moon
[RUNTIME5 2026-07-17 16:49:07] [INFO] [KG] Set attribute: earth.inferred_type = planet_orbiting_star
[RUNTIME5 2026-07-17 16:49:07] [INFO] [OrbitTypeInferenceRule] Inferred: earth.inferred_type = planet_orbiting_star
[RUNTIME5 2026-07-17 16:49:07] [INFO] [KG] Set attribute: mars.inferred_type = planet_orbiting_star
[RUNTIME5 2026-07-17 16:49:07] [INFO] [OrbitTypeInferenceRule] Inferred: mars.inferred_type = planet_orbiting_star
[RUNTIME5 2026-07-17 16:49:07] [INFO] [TransitiveRelationsRule] Inferred (safe): dog -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [TransitiveRelationsRule] Inferred (safe): cat -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [TransitiveRelationsRule] Inferred (safe): lion -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [InheritanceCategoryRule] Inferred (safe): living_thing.instance_of = category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [InheritanceCategoryRule] Inferred (safe): astronomical_body.instance_of = category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [InheritanceCategoryRule] Inferred (safe): living_thing.instance_of = category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [InheritanceCategoryRule] Inferred (safe): living_thing.instance_of = category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [KG] Added relation: dog -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [InheritanceRelationsRule] dog inherited relation is_a -> category (from mammal)
[RUNTIME5 2026-07-17 16:49:07] [INFO] [KG] Added relation: cat -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [InheritanceRelationsRule] cat inherited relation is_a -> category (from mammal)
[RUNTIME5 2026-07-17 16:49:07] [INFO] [KG] Added relation: lion -[is_a]-> category
[RUNTIME5 2026-07-17 16:49:07] [INFO] [InheritanceRelationsRule] lion inherited relation is_a -> category (from mammal)
[RUNTIME5 2026-07-17 16:49:07] [INFO] [KG_EXPLAIN] Inferred 12 facts.
[RUNTIME5 2026-07-17 16:49:07] [INFO] [HealthMonitor5] OK: Runtime cycle completed.
--------------------------------------------------
{'status': 'ok', 'entity': 'moon', 'tree': '\x1b[1;36mmoon\x1b[0m\n ├─ \x1b[0;33mattributes\x1b[0m\n │   └─ \x1b[0;33mtype\x1b[0m = natural_satellite\n │   └─ \x1b[0;33minferred_root\x1b[0m = sun\n │   └─ \x1b[0;33minstance_of\x1b[0m = natural_satellite\n ├─ \x1b[0;35moutbound\x1b[0m\n │   └─ \x1b[1;36mmoon\x1b[0m -[\x1b[0;35morbits\x1b[0m]-> \x1b[1;36mplanet\x1b[0m\n │   └─ \x1b[1;36mmoon\x1b[0m -[\x1b[0;35mhas_property\x1b[0m]-> \x1b[1;36mspherical\x1b[0m\n │   └─ \x1b[1;36mmoon\x1b[0m -[\x1b[0;35mhas_property\x1b[0m]-> \x1b[1;36mmassive\x1b[0m\n │   └─ \x1b[1;36mmoon\x1b[0m -[\x1b[0;35mhas_property\x1b[0m]-> \x1b[1;36mno_fusion\x1b[0m\n │   └─ \x1b[1;36mmoon\x1b[0m -[\x1b[0;35mcategory\x1b[0m]-> \x1b[1;36mastronomical_body\x1b[0m\n │   └─ \x1b[1;36mmoon\x1b[0m -[\x1b[0;35mis_a\x1b[0m]-> \x1b[1;36mnatural_satellite\x1b[0m\n │   └─ \x1b[1;36mmoon\x1b[0m -[\x1b[0;35mis_a\x1b[0m]-> \x1b[1;36mastronomical_body\x1b[0m\n ├─ \x1b[0;35minbound\x1b[0m\n │   └─ (none)\n └─ \x1b[0;32mreasoning\x1b[0m\n     └─ (none)', 'attributes': {'name': 'moon', 'attributes': {'type': 'natural_satellite', 'inferred_root': 'sun', 'instance_of': 'natural_satellite'}}, 'outbound': [{'source': 'moon', 'relation': 'orbits', 'target': 'planet'}, {'source': 'moon', 'relation': 'has_property', 'target': 'spherical'}, {'source': 'moon', 'relation': 'has_property', 'target': 'massive'}, {'source': 'moon', 'relation': 'has_property', 'target': 'no_fusion'}, {'source': 'moon', 'relation': 'category', 'target': 'astronomical_body'}, {'source': 'moon', 'relation': 'is_a', 'target': 'natural_satellite'}, {'source': 'moon', 'relation': 'is_a', 'target': 'astronomical_body'}], 'inbound': [], 'reasoning': [], 'reasoning_count': 0}
--------------------------------------------------
>>> ^Z

Exiting Runtime5 CLI.
[RUNTIME5 2026-07-17 17:41:30] [INFO] [KGExportImport5] EXPORT OK → autosave_kg.json
[RUNTIME5 2026-07-17 17:41:30] [INFO] [RuntimeCore] AUTOSAVE completed → autosave_kg.json
[RUNTIME5 2026-07-17 17:41:30] [INFO] [KGExportImport5] EXPORT OK → autosave_kg.json
[RUNTIME5 2026-07-17 17:41:30] [INFO] [SystemHooks5] AUTOSAVE completed → autosave_kg.json (31 entities, 88 relations)
[RUNTIME5 2026-07-17 17:41:30] [INFO] [RuntimeCore] Shutdown complete. STATUS: This release 5.6.1 will be available soon on GitHub as a ZIP package in the Releases section once the compilation is complete.
