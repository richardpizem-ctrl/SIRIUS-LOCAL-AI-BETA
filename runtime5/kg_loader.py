# runtime5/kg_loader.py

import json
import os

from runtime5.kg_core import KnowledgeGraph
from runtime5.kg_integrity import KGIntegrity
from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class KGLoader:
    """
    Knowledge Pack Loader for Runtime 5.x.
    Provides:
    - safe JSON loading
    - validation
    - diagnostics
    - degraded mode awareness
    - Self‑Repair Layer compatibility
    """

    def __init__(self, base_path="knowledge_packs"):
        self.base_path = base_path
        log5(f"[KGLoader] Initialized loader at: {base_path}")

    # --------------------------------------------------------
    # LOAD SINGLE PACK
    # --------------------------------------------------------
    def load_pack(self, filename: str) -> KnowledgeGraph:
        """
        Loads a single knowledge pack JSON file into a KnowledgeGraph.
        Includes:
        - safe file access
        - JSON validation
        - KG integrity validation
        - diagnostics
        """
        def _exec():
            path = os.path.join(self.base_path, filename)

            if not os.path.exists(path):
                raise FileNotFoundError(f"Knowledge pack not found: {path}")

            log5(f"[KGLoader] Loading pack: {path}")

            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except Exception as exc:
                    raise ValueError(f"Invalid JSON in pack '{filename}': {exc}")

            kg = KnowledgeGraph()

            # Load entities
            for name, attrs in data.get("entities", {}).items():
                kg.add_entity(name, attrs)

            # Load relations
            for src, rel, tgt in data.get("relations", []):
                kg.add_relation(src, rel, tgt)

            # Validate integrity
            integrity = KGIntegrity(kg).validate()

            if integrity.get("missing_entities") or integrity.get("cycles"):
                log5(f"[KGLoader] Integrity issues detected in pack '{filename}'")
                SystemHooks5.on_error("KG integrity validation failed.")

            log5(f"[KGLoader] Pack '{filename}' loaded successfully.")
            return kg

        return ErrorHandler5.safe_execute(
            _exec,
            context={"filename": filename},
            fallback=KnowledgeGraph()
        )

    # --------------------------------------------------------
    # LOAD ALL PACKS IN DIRECTORY
    # --------------------------------------------------------
    def load_all(self):
        """
        Loads all JSON packs in the base directory.
        Returns dict: { filename: KnowledgeGraph }
        """
        def _exec():
            packs = {}

            if not os.path.exists(self.base_path):
                raise FileNotFoundError(f"Knowledge pack directory missing: {self.base_path}")

            for file in os.listdir(self.base_path):
                if file.endswith(".json"):
                    packs[file] = self.load_pack(file)

            log5(f"[KGLoader] Loaded {len(packs)} packs.")
            return packs

        return ErrorHandler5.safe_execute(
            _exec,
            context={"path": self.base_path},
            fallback={}
        )
