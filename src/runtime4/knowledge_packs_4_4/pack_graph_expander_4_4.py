knowledge_packs_4_4/pack_graph_expander_4_4.py
"""
SIRIUS LOCAL AI – Pack Graph Expander 4.4.0

This module builds deterministic knowledge graphs from Knowledge Packs 4.4.

It supports:
- Node extraction
- Edge extraction
- Cross-pack graph linking
- Graph expansion rules
- Deterministic offline graph generation
- Integration with KP Registry 4.4 and Pack Linker 4.4

Security Notes:
- No dynamic imports, no eval, no reflection.
- Only JSON/dict structures are processed.
- Graphs contain no executable code.
"""

from typing import Dict, Any, List


class PackGraphExpander44:
    """
    Deterministic graph builder for Knowledge Packs 4.4.
    """

    def __init__(self, registry=None, linker=None):
        self.registry = registry
        self.linker = linker

        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.registry:
                self.registry.initialize()
            if self.linker:
                self.linker.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # EXTRACT NODES
    # ------------------------------------------------------------------
    def extract_nodes(self, pack: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extracts graph nodes from a pack.
        Nodes are defined as:
        {
            "id": key,
            "value": value
        }
        """

        nodes = []
        for key, value in pack.items():
            nodes.append({
                "id": key,
                "value": value,
            })

        return nodes

    # ------------------------------------------------------------------
    # EXTRACT EDGES
    # ------------------------------------------------------------------
    def extract_edges(self, pack: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extracts edges based on reference fields:
        {
            "ref": "pack:key"
        }
        """

        edges = []

        for key, value in pack.items():
            if isinstance(value, dict) and "ref" in value:
                ref = value["ref"]

                if ":" not in ref:
                    continue

                pack_name, ref_key = ref.split(":", 1)

                edges.append({
                    "from": key,
                    "to_pack": pack_name,
                    "to_key": ref_key,
                })

        return edges

    # ------------------------------------------------------------------
    # BUILD GRAPH FOR ONE PACK
    # ------------------------------------------------------------------
    def build_graph(self, pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Builds a graph structure for a single pack.
        """

        nodes = self.extract_nodes(pack)
        edges = self.extract_edges(pack)

        return {
            "nodes": nodes,
            "edges": edges,
        }

    # ------------------------------------------------------------------
    # BUILD FULL GRAPH FOR ALL PACKS
    # ------------------------------------------------------------------
    def build_full_graph(self) -> Dict[str, Any]:
        """
        Builds a combined graph from all registered packs.
        """

        if not self.registry:
            return {"status": "error", "reason": "no_registry"}

        full_graph = {
            "nodes": [],
            "edges": [],
        }

        for name, pack in self.registry.get_all().items():
            graph = self.build_graph(pack)

            # Tag nodes with pack name
            for node in graph["nodes"]:
                node["pack"] = name

            # Tag edges with pack name
            for edge in graph["edges"]:
                edge["from_pack"] = name

            full_graph["nodes"].extend(graph["nodes"])
            full_graph["edges"].extend(graph["edges"])

        return {
            "status": "ok",
            "graph": full_graph,
        }

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
