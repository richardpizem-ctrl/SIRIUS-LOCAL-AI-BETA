# pack_linker.py
"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Linker

Responsible for:
- linking validated packs into a unified structure
- resolving dependencies using PackGraph4
- merging pack data
- preparing packs for runtime reasoning

This is the linking layer of Knowledge Packs 2.0.
"""

from typing import Dict, Any


class PackLinker4:
    """
    Links Knowledge Packs 2.0 into a final runtime structure.
    """

    def __init__(self, graph):
        # graph = instance of PackGraph4
        self.graph = graph

    # ---------------------------------------------------------
    # LINKING
    # ---------------------------------------------------------

    def link(self, packs: Dict[str, Dict[str, Any]]):
        """
        Links all packs according to dependency order.
        Returns a merged structure.
        """
        order = self.graph.resolve_order()

        merged = {
            "packs": {},
            "merged_data": {},
            "meta": {}
        }

        for pack_name in order:
            pack = packs.get(pack_name)
            if not pack:
                continue

            # Store pack
            merged["packs"][pack_name] = pack

            # Merge data
            if "data" in pack:
                merged["merged_data"][pack_name] = pack["data"]

            # Merge metadata
            if "meta" in pack:
                merged["meta"][pack_name] = pack["meta"]

        return merged
