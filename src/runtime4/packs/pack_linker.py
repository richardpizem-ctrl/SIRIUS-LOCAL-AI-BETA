"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Linker (Runtime 4.3)

Responsible for:
- linking validated packs into a unified structure
- resolving dependencies using PackGraph4
- merging pack data and metadata
- preparing packs for runtime reasoning
- enforcing Security Family 4.4 rules
- supporting Self‑Repair 4.4 diagnostics

This is the linking layer of Knowledge Packs 2.0 (Runtime 4.3).
"""

from typing import Dict, Any


class PackLinker4:
    """
    Links Knowledge Packs 2.0 into a final runtime structure.
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, graph):
        if graph is None or not hasattr(graph, "resolve_order"):
            raise ValueError("Invalid graph: missing resolve_order() method.")

        self.graph = graph
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # LINKING
    # ---------------------------------------------------------

    def link(self, packs: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Links all packs according to dependency order.
        Returns a merged structure with full Runtime 4.3 validation.
        """

        # SAFE MODE
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Pack linking disabled in safe-mode."
            }

        # Validate packs container
        if not isinstance(packs, dict):
            return {"status": "error", "code": "invalid_packs_type"}

        # Resolve dependency order
        order_result = self.graph.resolve_order()

        if not isinstance(order_result, dict) or order_result.get("status") != "success":
            return {
                "status": "error",
                "code": "graph_resolution_failed",
                "details": order_result
            }

        order = order_result["order"]

        merged = {
            "packs": {},
            "merged_data": {},
            "meta": {},
            "order": order,
        }

        try:
            for pack_name in order:

                # Validate pack name
                if not isinstance(pack_name, str) or not pack_name.strip():
                    return {"status": "error", "code": "invalid_pack_name", "pack": pack_name}

                pack = packs.get(pack_name)

                # Skip missing packs (optional packs allowed)
                if not pack:
                    continue

                # Validate pack structure
                if not isinstance(pack, dict):
                    return {"status": "error", "code": "invalid_pack_structure", "pack": pack_name}

                data = pack.get("data")
                meta = pack.get("meta")

                # Validate data
                if data is not None and not isinstance(data, dict):
                    return {"status": "error", "code": "invalid_pack_data", "pack": pack_name}

                # Validate metadata
                if meta is not None and not isinstance(meta, dict):
                    return {"status": "error", "code": "invalid_pack_meta", "pack": pack_name}

                # Store pack
                merged["packs"][pack_name] = pack

                # Merge data
                if isinstance(data, dict):
                    merged["merged_data"][pack_name] = data

                # Merge metadata
                if isinstance(meta, dict):
                    merged["meta"][pack_name] = meta

            return {
                "status": "success",
                "merged": merged,
                "degraded_mode": self.degraded_mode
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "linking_failed",
                "exception": str(exc)
            }
