"""
SIRIUS LOCAL AI – Knowledge Packs Linker 4.5.0 (PRO)

Responsible for:
- linking validated packs into a unified structure
- resolving dependencies using PackGraph45
- merging pack data and metadata
- preparing packs for runtime reasoning
- enforcing Security Family 4.5 rules
- supporting Self‑Repair 4.5 diagnostics

This is the linking layer of Knowledge Packs 4.5.
"""

from typing import Dict, Any, Optional


class PackLinker45:
    """
    Deterministic linker for Knowledge Packs 4.5.
    """

    def __init__(self, graph):
        if graph is None or not hasattr(graph, "resolve_order"):
            raise ValueError("Invalid graph: missing resolve_order() method.")

        self.graph = graph
        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INTERNAL HELPERS
    # ------------------------------------------------------------------
    def _validate_pack_dict(self, pack: Any) -> bool:
        if not isinstance(pack, dict):
            return False
        if "data" not in pack or "metadata" not in pack:
            return False
        if not isinstance(pack["data"], dict):
            return False
        if not isinstance(pack["metadata"], dict):
            return False
        return True

    # ------------------------------------------------------------------
    # LINKING
    # ------------------------------------------------------------------
    def link(self, packs: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Links all packs according to dependency order.
        Returns a merged structure with full Runtime 4.5 validation.
        """

        # SAFE MODE
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Pack linking disabled in safe-mode.",
                "version": "4.5",
            }

        # Validate packs container
        if not isinstance(packs, dict):
            return {"status": "error", "code": "invalid_packs_type", "version": "4.5"}

        # Resolve dependency order
        order_result = self.graph.resolve_order()

        if not isinstance(order_result, dict) or order_result.get("status") != "ok":
            return {
                "status": "error",
                "code": "graph_resolution_failed",
                "details": order_result,
                "version": "4.5",
            }

        order = order_result["order"]

        merged = {
            "packs": {},
            "merged_data": {},
            "merged_metadata": {},
            "order": order,
        }

        try:
            for pack_name in order:

                # Validate pack name
                if not isinstance(pack_name, str) or not pack_name.strip():
                    return {
                        "status": "error",
                        "code": "invalid_pack_name",
                        "pack": pack_name,
                        "version": "4.5",
                    }

                pack = packs.get(pack_name)

                # Skip missing packs (optional packs allowed)
                if not pack:
                    continue

                # Validate pack structure
                if not self._validate_pack_dict(pack):
                    return {
                        "status": "error",
                        "code": "invalid_pack_structure",
                        "pack": pack_name,
                        "version": "4.5",
                    }

                data = pack["data"]
                meta = pack["metadata"]

                # Store pack
                merged["packs"][pack_name] = pack

                # Merge data
                merged["merged_data"][pack_name] = data

                # Merge metadata
                merged["merged_metadata"][pack_name] = meta

            return {
                "status": "ok",
                "merged": merged,
                "degraded_mode": self.degraded_mode,
                "version": "4.5",
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "linking_failed",
                "exception": str(exc),
                "version": "4.5",
            }
