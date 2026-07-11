🚀 Overview
Version 5.6.0 represents the largest architectural leap in the SIRIUS Runtime 5.x
line since version 5.4. This release delivers a fully redesigned Knowledge Graph stack,
deep explainability (XAI), new multi-hop inference capabilities, unified traversal,
and complete integration of the reasoning engine with the workflow layer.

🧠 Unified Knowledge Graph Architecture
• Fully redesigned KG Core (stability, consistency, no cycles)
• New KG Query (multi-hop traversal, inbound/outbound, neighbors)
• New KG Explore (colored ASCII tree, multi-hop, contextual graph view)
• New KG Explain (local explanation of attributes and relations)
• New KG Explain Deep (deep explanation, reasoning, proof tree, evidence tree)
• Full integration KG → ReasoningEngine → WorkflowEngine

🔍 Deep Explainability (XAI)
• Proof trees (ASCII + HTML)
• Evidence tree (inference evidence)
• Applied rules (which rules were used)
• Reasoning metrics (depth, nodes, relations, inference cost)
• Confidence model (combined scoring)
• Multi-hop categorization and deduction

🧩 New Reasoning Rules
• MultiHopOrbitInferenceRule — multi-hop orbital inference
• DedicsnostVlastnostiRule — inheritance of physical properties
• TranzitivneRelacieRule — transitive category reasoning
• AutoTypeInferenceRule — automatic type inference

🛠 Workflow & Parser Improvements
• Full integration of KG_EXPLAIN and KG_EXPLAIN_DEEP
• Stabilized WorkflowEngine5 routing
• Clean handling of KG commands
• Unified InputParser5 for KG operations

📁 KG Export / Import
• Stabilized reasoning JSON export
• Improved KG autoload
• Autosave KG prepared (coming in next version)

🔒 System Stability
• Runtime 5.x stabilized at 98%
• KG stack stabilized at 98%
• Reasoning Engine stabilized at 98%
• WorkflowEngine5 stabilized at 100%

📦 Included in ZIP
• Complete Runtime 5.6.0
• All KG modules
• All workflow steps
• All reasoning rules
• Updated KG_EXPLAIN and KG_EXPLAIN_DEEP
• Updated KG Query and KG Explore
• Updated InputParser5
• Updated WorkflowEngine5

🏁 Summary
SIRIUS LOCAL AI 5.6.0 is the first version delivering a fully functional deep
explainability system, a unified Knowledge Graph architecture, and stable multi-hop
reasoning. This release forms the foundation for upcoming modules such as
FileManager, ProcessManager, SystemMonitor, and the autonomous mode in future versions.
