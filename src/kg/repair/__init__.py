"""
SIRIUS Runtime 5.1.0 – Knowledge Graph Repair Layer 1.0
Package Initializer

Tento modul poskytuje jednotné API pre všetky opravné komponenty KG:

- KGIntegrityRepair      (hlavný opravný modul)
- KGRepairPlanner        (výber stratégie opravy)
- KGRepairSandbox        (izolované vykonávanie opráv)
- KGRepairValidator      (validácia integrity pred/po oprave)
- KGRepairFallback       (fallback minimálneho balíka KG)

Používa sa v:
- Self‑Repair Layer 1.0
- Runtime Integrity Engine 1.0
- Workflow Engine 5.1
- System Agent 5.1
"""

from .kg_integrity_repair import KGIntegrityRepair
from .kg_repair_planner import KGRepairPlanner
from .kg_repair_sandbox import KGRepairSandbox
from .kg_repair_validator import KGRepairValidator
from .kg_repair_fallback import KGRepairFallback

__all__ = [
    "KGIntegrityRepair",
    "KGRepairPlanner",
    "KGRepairSandbox",
    "KGRepairValidator",
    "KGRepairFallback",
]
