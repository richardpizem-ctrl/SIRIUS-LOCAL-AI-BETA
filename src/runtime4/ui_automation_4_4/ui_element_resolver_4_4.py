"""
SIRIUS LOCAL AI – UI Element Resolver 4.4.0

This module provides semantic + structural UI element resolution
for the UI Automation Engine 4.4. It is responsible for:

- Interpreting high‑level semantic queries (role, label, intent)
- Combining semantic filters with structural hints (window, region, hierarchy)
- Ranking candidate elements deterministically
- Producing a stable element reference for downstream actions

All logic is deterministic, offline, and fully isolated.

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- All OS access must go through the OS bridge / capability layer.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any, List, Optional


class UIElementResolver44:
    """
    Semantic + structural UI element resolver for Runtime 4.4.

    It does NOT talk to the OS directly.
    It only uses the provided `os_bridge` abstraction.
    """

    def __init__(self, os_bridge):
        self.os_bridge = os_bridge
        self.initialized = False
        self.degraded_mode = False

    # ---------------------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        if not self.os_bridge:
            self.degraded_mode = True
            return {"status": "error", "reason": "no_os_bridge"}

        result = self.os_bridge.initialize()
        if result.get("status") != "initialized" and result.get("status") != "already_initialized":
            self.degraded_mode = True
            return {"status": "error", "reason": "os_bridge_init_failed", "details": result}

        self.initialized = True
        return {"status": "initialized"}

    # ---------------------------------------------------------------------
    # PUBLIC API – RESOLVE ELEMENT
    # ---------------------------------------------------------------------
    def resolve(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolves a UI element based on a semantic + structural query.

        Expected query fields (all optional, but at least one should be present):
        - "role": semantic role (e.g., "button", "textbox", "menu_item")
        - "label": visible text or accessibility name
        - "window_title": target window title
        - "app_hint": application name hint
        - "region": {"x": ..., "y": ..., "width": ..., "height": ...}
        - "priority": list of fields to prioritize when ranking

        Returns:
        {
            "status": "ok" | "error",
            "element": {...} | None,
            "candidates": [...],  # optional, for debugging / explanation
        }
        """
        if not self.initialized:
            init_result = self.initialize()
            if init_result.get("status") != "initialized" and init_result.get("status") != "already_initialized":
                return {"status": "error", "reason": "resolver_not_initialized", "details": init_result}

        try:
            # 1. Ask OS bridge for raw candidates
            raw_query = self._build_raw_query(query)
            bridge_result = self.os_bridge.query_element(raw_query)

            if bridge_result.get("status") != "ok":
                self.degraded_mode = True
                return {"status": "error", "reason": "os_bridge_query_failed", "details": bridge_result}

            candidates = bridge_result.get("element") or []
            if not isinstance(candidates, list):
                candidates = [candidates] if candidates else []

            if not candidates:
                return {"status": "ok", "element": None, "candidates": []}

            # 2. Rank candidates deterministically
            ranked = self._rank_candidates(query, candidates)
            best = ranked[0] if ranked else None

            return {
                "status": "ok",
                "element": best,
                "candidates": ranked,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # INTERNAL – BUILD RAW QUERY FOR OS BRIDGE
    # ---------------------------------------------------------------------
    def _build_raw_query(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converts high‑level semantic query into a raw OS bridge query.
        This is still deterministic and purely data‑driven.
        """
        raw: Dict[str, Any] = {}

        # Pass through known fields
        for key in ("role", "label", "window_title", "app_hint", "region"):
            if key in query:
                raw[key] = query[key]

        # Add default constraints if missing
        if "max_results" not in raw:
            raw["max_results"] = 32

        return raw

    # ---------------------------------------------------------------------
    # INTERNAL – RANKING LOGIC
    # ---------------------------------------------------------------------
    def _rank_candidates(self, query: Dict[str, Any], candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Deterministically ranks candidates based on:
        - label similarity
        - role match
        - window/app match
        - region proximity

        No randomness, no non‑deterministic ordering.
        """
        priority = query.get("priority") or ["role", "label", "window_title", "app_hint", "region"]

        def score(candidate: Dict[str, Any]) -> int:
            s = 0

            if "role" in priority and "role" in query:
                if candidate.get("role") == query.get("role"):
                    s += 10

            if "label" in priority and "label" in query:
                if candidate.get("label") == query.get("label"):
                    s += 10
                elif self._soft_match(candidate.get("label"), query.get("label")):
                    s += 6

            if "window_title" in priority and "window_title" in query:
                if candidate.get("window_title") == query.get("window_title"):
                    s += 5

            if "app_hint" in priority and "app_hint" in query:
                if candidate.get("app_hint") == query.get("app_hint"):
                    s += 4

            if "region" in priority and "region" in query:
                if self._region_overlap(candidate.get("region"), query.get("region")):
                    s += 3

            return s

        # Deterministic sort: by score desc, then by stable key (e.g., id or label)
        ranked = sorted(
            candidates,
            key=lambda c: (-score(c), str(c.get("id") or c.get("label") or "")),
        )
        return ranked

    # ---------------------------------------------------------------------
    # INTERNAL – SOFT LABEL MATCH
    # ---------------------------------------------------------------------
    def _soft_match(self, a: Optional[str], b: Optional[str]) -> bool:
        if not a or not b:
            return False
        a_norm = a.strip().lower()
        b_norm = b.strip().lower()
        return a_norm == b_norm or a_norm.startswith(b_norm) or b_norm.startswith(a_norm)

    # ---------------------------------------------------------------------
    # INTERNAL – REGION OVERLAP
    # ---------------------------------------------------------------------
    def _region_overlap(self, a: Optional[Dict[str, Any]], b: Optional[Dict[str, Any]]) -> bool:
        if not a or not b:
            return False

        try:
            ax, ay = int(a.get("x", 0)), int(a.get("y", 0))
            aw, ah = int(a.get("width", 0)), int(a.get("height", 0))
            bx, by = int(b.get("x", 0)), int(b.get("y", 0))
            bw, bh = int(b.get("width", 0)), int(b.get("height", 0))

            if aw <= 0 or ah <= 0 or bw <= 0 or bh <= 0:
                return False

            ax2, ay2 = ax + aw, ay + ah
            bx2, by2 = bx + bw, by + bh

            overlap_x = max(0, min(ax2, bx2) - max(ax, bx))
            overlap_y = max(0, min(ay2, by2) - max(ay, by))

            return overlap_x > 0 and overlap_y > 0
        except Exception:
            return False
