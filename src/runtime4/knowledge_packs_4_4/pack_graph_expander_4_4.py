"""
SIRIUS LOCAL AI – Pack Graph Expander 4.4.0 (PRO)

This module builds deterministic knowledge graphs from Knowledge Packs 4.4.

It supports:
- Node extraction
- Edge extraction
- Cross-pack graph linking
- Graph expansion rules
- Deterministic offline graph generation
- Integration with KP Registry 4.4 and Pack Linker 4.4

Security Notes (PRO):
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
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL HELPERS
    # ------------------------------------------------------------------
    def _get_pack_data(self, pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registry stores full pack dict:
        { name, version, pack_type, data, metadata }
        Graph must operate ONLY on pack["data"].
        """
        if not isinstance(pack, dict):
            return {}
        data = pack.get("data", {})
        return data if isinstance(data, dict) else {}

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.registry:
                res = self.registry.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "registry_init_failed", "details": res}

            if self.linker:
                res = self.linker.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {"status": "error", "code": "linker_init_failed", "details": res}

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "init_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # EXTRACT NODES
    # ------------------------------------------------------------------
    def extract_nodes(self, pack: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extracts graph nodes from a pack's data section.
        Nodes are defined as:
        {
            "id": key,
            "value": value
        }
        """

        if self.safe_mode:
            return []

        data = self._get_pack_data(pack)
        nodes: List[Dict[str, Any]] = []

        for key, value in data.items():
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
        Extracts edges based on reference fields in data:
        {
            "ref": "pack_name:key"
        }
        """

        if self.safe_mode:
            return []

        data = self._get_pack_data(pack)
        edges: List[Dict[str, Any]] = []

        for key, value in data.items():
            if isinstance(value, dict) and "ref" in value:
                ref = value["ref"]
                if not isinstance(ref, str):
                    continue

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

        if self.safe_mode:
            return {"status": "safe_mode", "graph": {"nodes": [], "edges": []}}

        try:
            nodes = self.extract_nodes(pack)
            edges = self.extract_edges(pack)

            return {
                "status": "ok",
                "graph": {
                    "nodes": nodes,
                    "edges": edges,
                },
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "build_graph_failed",
                "exception": str(exc),
            }

    # ------------------------------------------------------------------
    # BUILD FULL GRAPH FOR ALL PACKS
    # ------------------------------------------------------------------
    def build_full_graph(self) -> Dict[str, Any]:
        """
        Builds a combined graph from all registered packs.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "graph": {"nodes": [], "edges": []},
            }

        if not self.registry:
            return {"status": "error", "code": "no_registry"}

        try:
            full_graph = {
                "nodes": [],
                "edges": [],
            }

            for name, pack in self.registry.get_all().items():
                single = self.build_graph(pack)
                if single.get("status") != "ok":
                    # Non-fatal: skip broken pack, keep graph deterministic
                    continue

                graph = single["graph"]

                # Tag nodes with pack name
                for node in graph["nodes"]:
                    node["pack"] = name

                # Tag edges with source pack name
                for edge in graph["edges"]:
                    edge["from_pack"] = name

                full_graph["nodes"].extend(graph["nodes"])
                full_graph["edges"].extend(graph["edges"])

            return {
                "status": "ok",
                "graph": full_graph,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "build_full_graph_failed",
                "exception": str(exc),
            }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
        }
