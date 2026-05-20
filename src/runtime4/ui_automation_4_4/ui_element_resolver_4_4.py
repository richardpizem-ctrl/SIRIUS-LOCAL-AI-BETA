"""
SIRIUS LOCAL AI – UI Element Resolver 4.4.0 (PRO)

Provides semantic + structural UI element resolution for Runtime 4.4.
Responsibilities:
- Interpret high‑level semantic queries (role, label, intent)
- Combine semantic filters with structural hints (window, region, hierarchy)
- Deterministically rank candidate elements
- Produce stable element references for downstream actions

Security Notes:
- Deterministic, offline‑safe
- No dynamic imports, no eval, no reflection
- All OS access must go through the OS bridge
- Fully compatible with Security Family 4.4
"""

from typing import Dict, Any, List, Optional


class UIElementResolver44:
    """
    Deterministic semantic + structural UI element resolver for Runtime 4.4 (PRO).
    """

    REQUIRED_OS_BRIDGE_METHODS = {"initialize", "query_element"}

    def __init__(self, os_bridge):
        self.os_bridge = os_bridge
        self.initialized = False
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        if not self.os_bridge:
            self.degraded_mode = True
            return {"status": "error", "code": "no_os_bridge"}

        # Validate OS bridge interface
        for method in self.REQUIRED_OS_BRIDGE_METHODS:
            if not hasattr(self.os_bridge, method):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "invalid_os_bridge_interface",
                    "missing": method,
                }

        try:
            result = self.os_bridge.initialize()
            if result.get("status") not in ("initialized", "already_initialized"):
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "os_bridge_init_failed",
                    "details": result,
                }

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "exception", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # PUBLIC API – RESOLVE ELEMENT
    # ---------------------------------------------------------------------
    def resolve(self, query: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "element": None,
                "candidates": [],
                "degraded_mode": self.degraded_mode,
            }

        if not isinstance(query, dict):
            return {"status": "error", "code": "invalid_query"}

        if not self.initialized:
            init = self.initialize()
            if init.get("status") not in ("initialized", "already_initialized"):
                return {
                    "status": "error",
                    "code": "resolver_not_initialized",
                    "details": init,
                }

        try:
            # 1. Build raw OS query
            raw_query = self._build_raw_query(query)

            # 2. Query OS bridge
            bridge_result = self.os_bridge.query_element(raw_query)
            if bridge_result.get("status") != "ok":
                self.degraded_mode = True
                return {
                    "status": "error",
                    "code": "os_bridge_query_failed",
                    "details": bridge_result,
                }

            candidates = bridge_result.get("element") or []
            if not isinstance(candidates, list):
                candidates = [candidates]

            if not candidates:
                return {"status": "ok", "element": None, "candidates": []}

            # 3. Rank candidates deterministically
            ranked = self._rank_candidates(query, candidates)
            best = ranked[0] if ranked else None

            return {
                "status": "ok",
                "element": best,
                "candidates": ranked,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "exception", "exception": str(exc)}

    # ---------------------------------------------------------------------
    # INTERNAL – BUILD RAW QUERY
    # ---------------------------------------------------------------------
    def _build_raw_query(self, query: Dict[str, Any]) -> Dict[str, Any]:
        raw: Dict[str, Any] = {}

        for key in ("role", "label", "window_title", "app_hint", "region"):
            if key in query:
                raw[key] = query[key]

        raw["max_results"] = 32
        return raw

    # ---------------------------------------------------------------------
    # INTERNAL – RANKING LOGIC
    # ---------------------------------------------------------------------
    def _rank_candidates(self, query: Dict[str, Any], candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        priority = query.get("priority") or [
            "role",
            "label",
            "window_title",
            "app_hint",
            "region",
        ]

        def score(c: Dict[str, Any]) -> int:
            s = 0

            # Role match
            if "role" in priority and "role" in query:
                if c.get("role") == query.get("role"):
                    s += 10

            # Label match
            if "label" in priority and "label" in query:
                if c.get("label") == query.get("label"):
                    s += 10
                elif self._soft_match(c.get("label"), query.get("label")):
                    s += 6

            # Window title
            if "window_title" in priority and "window_title" in query:
                if c.get("window_title") == query.get("window_title"):
                    s += 5

            # App hint
            if "app_hint" in priority and "app_hint" in query:
                if c.get("app_hint") == query.get("app_hint"):
                    s += 4

            # Region overlap
            if "region" in priority and "region" in query:
                if self._region_overlap(c.get("region"), query.get("region")):
                    s += 3

            return s

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
        return (
            a_norm == b_norm
            or a_norm.startswith(b_norm)
            or b_norm.startswith(a_norm)
        )

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
            self.degraded_mode = True
            return False
