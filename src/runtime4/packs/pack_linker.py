"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Linker

Responsible for:
- linking validated packs into a unified structure
- resolving dependencies using PackGraph4
- merging pack data
- preparing packs for runtime reasoning

This is the linking layer of Knowledge Packs 2.0.
"""

from typing import Dict, Any, List


class PackLinker4:
    """
    Links Knowledge Packs 2.0 into a final runtime structure.
    """

    def __init__(self, graph):
        # Validate graph object
        if graph is None or not hasattr(graph, "resolve_order"):
            raise ValueError("Invalid graph: missing resolve_order() method.")

        self.graph = graph

    # ---------------------------------------------------------
    # LINKING
    # ---------------------------------------------------------

    def link(self, packs: Dict[str, Dict[str, Any]]):
        """
        Links all packs according to dependency order.
        Returns a merged structure with full safety validation.
        """

        # Validate packs structure
        if not isinstance(packs, dict):
            return {"error": "invalid_packs_type"}

        # Resolve dependency order
        try:
            order = self.graph.resolve_order()
        except Exception:
            return {"error": "graph_resolution_failed"}

        if not isinstance(order, list):
            return {"error": "invalid_graph_order"}

        merged = {
            "packs": {},
            "merged_data": {},
            "meta": {}
        }

        for pack_name in order:

            # Validate pack name
            if not isinstance(pack_name, str) or not pack_name.strip():
                return {"error": "invalid_pack_name", "pack": pack_name}

            pack = packs.get(pack_name)

            # Skip missing packs silently (graph may reference optional packs)
            if not pack:
                continue

            # Validate pack structure
            if not isinstance(pack, dict):
                return {"error": "invalid_pack_structure", "pack": pack_name}

            data = pack.get("data")
            meta = pack.get("meta")

            # Validate data
            if data is not None and not isinstance(data, dict):
                return {"error": "invalid_pack_data", "pack": pack_name}

            # Validate meta
            if meta is not None and not isinstance(meta, dict):
                return {"error": "invalid_pack_meta", "pack": pack_name}

            # Store pack
            merged["packs"][pack_name] = pack

            # Merge data
            if isinstance(data, dict):
                merged["merged_data"][pack_name] = data

            # Merge metadata
            if isinstance(meta, dict):
                merged["meta"][pack_name] = meta

        return merged
