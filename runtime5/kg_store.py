# runtime5/kg_store.py

import json
import os

from runtime5.kg_core import KnowledgeGraph
from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class KGStore:
    """
    Persistent storage for KnowledgeGraph (Runtime 5.x).
    Provides:
    - safe save/load
    - diagnostics
    - degraded mode awareness
    - Self‑Repair Layer compatibility
    """

    def __init__(self, path="kg_data.json"):
        self.path = path
        log5(f"[KGStore] Initialized store at: {path}")

    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------
    def save(self, kg: KnowledgeGraph):
        """
        Saves the KnowledgeGraph to disk safely.
        """
        def _exec():
            data = {
                "entities": {
                    name: entity.attributes
                    for name, entity in kg.entities.items()
                },
                "relations": [
                    {
                        "source": r.source,
                        "relation": r.relation,
                        "target": r.target
                    }
                    for r in kg.relations
                ],
                "degraded": HealthMonitor5.is_degraded()
            }

            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            log5(f"[KGStore] Saved KG to {self.path}")

        return ErrorHandler5.safe_execute(
            _exec,
            context={"path": self.path},
            fallback=None
        )

    # --------------------------------------------------------
    # LOAD
    # --------------------------------------------------------
    def load(self) -> KnowledgeGraph:
        """
        Loads the KnowledgeGraph from disk safely.
        Returns an empty KG if file missing or corrupted.
        """
        def _exec():
            kg = KnowledgeGraph()

            if not os.path.exists(self.path):
                log5(f"[KGStore] No KG file found at {self.path}, returning empty KG.")
                return kg

            log5(f"[KGStore] Loading KG from {self.path}")

            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as exc:
                log5(f"[KGStore] ERROR loading JSON: {exc}")
                SystemHooks5.on_error(str(exc))
                return kg  # fallback empty KG

            # Load entities
            for name, attributes in data.get("entities", {}).items():
                kg.add_entity(name, attributes)

            # Load relations
            for rel in data.get("relations", []):
                try:
                    kg.add_relation(rel["source"], rel["relation"], rel["target"])
                except Exception as exc:
                    log5(f"[KGStore] Invalid relation skipped: {exc}")

            log5(f"[KGStore] KG loaded successfully from {self.path}")
            return kg

        return ErrorHandler5.safe_execute(
            _exec,
            context={"path": self.path},
            fallback=KnowledgeGraph()
        )
