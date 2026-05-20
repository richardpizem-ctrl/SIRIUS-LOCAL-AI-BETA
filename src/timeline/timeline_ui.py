# timeline_ui_4_4.py
# SIRIUS LOCAL AI – TimelineUI 4.4.0 (Phase‑4 PRO)
# Deterministic, offline-only timeline logic for PixelLayoutEngine (Phase‑4)

from typing import List, Dict, Any, Optional


class TimelineUI44:
    """
    TimelineUI44 is the logical layer of the timeline.
    It generates layout blocks for PixelLayoutEngine (Phase‑4).

    Features (Phase‑4 PRO):
        - adaptive grid (C4)
        - header
        - events
        - markers
        - playhead (C13)
        - overlays (C1–C12)
        - snapping + ghost layers (PRO)
        - selection box
        - deterministic, offline-only behavior
        - safe-mode & degraded-mode compatible
        - Security Family 4.4 compliant
    """

    def __init__(self):
        # Base timeline dimensions
        self.width: int = 120
        self.height: int = 20
        self.grid_step: int = 10
        self.zoom: float = 1.0

        # Marker lane
        self.marker_lane_y: int = 2
        self.marker_lane_height: int = 1

        # Runtime flags
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        # Dynamic state
        self._events: List[Dict[str, Any]] = []
        self._markers: List[Dict[str, Any]] = []
        self._selected_event: Optional[Dict[str, Any]] = None

        # Overlays (all disabled by default)
        self._hover = {"active": False}
        self._grid_hover = {"active": False}
        self._dragging_event = {"active": False}
        self._resizing_event = {"active": False}
        self._event_overlap = {"active": False}
        self._dragging_marker = {"active": False}
        self._playhead = {"active": False}
        self._snapping = {"active": False}
        self._ghost = {"active": False}

    # ---------------------------------------------------------
    # Public API – layout generation
    # ---------------------------------------------------------

    def render(self) -> List[Dict[str, Any]]:
        """Build a flat list of layout blocks representing the current timeline state."""
        if self.safe_mode:
            return [{
                "type": "timeline_safe_mode",
                "x": 0,
                "y": 0,
                "width": self.width,
                "height": self.height,
                "color": "gray",
                "label": "Timeline disabled in SAFE MODE",
            }]

        try:
            layout: List[Dict[str, Any]] = []

            layout.extend(self._build_header())
            layout.extend(self._build_marker_lane())
            layout.extend(self._build_grid())
            layout.extend(self._build_grid_hover_overlay())
            layout.extend(self._build_playhead_overlay())
            layout.extend(self._build_events())
            layout.extend(self._build_event_drag_overlay())
            layout.extend(self._build_event_resize_overlay())
            layout.extend(self._build_event_overlap_overlay())
            layout.extend(self._build_hover_overlay())
            layout.extend(self._build_markers())
            layout.extend(self._build_marker_drag_overlay())
            layout.extend(self._build_snapping_overlay())
            layout.extend(self._build_ghost_overlay())
            layout.extend(self._build_selection_overlay())

            return layout

        except Exception:
            self.degraded_mode = True
            return [{
                "type": "timeline_error",
                "x": 0,
                "y": 0,
                "width": self.width,
                "height": self.height,
                "color": "red",
                "label": "Timeline rendering error (DEGRADED MODE)",
            }]

    # ---------------------------------------------------------
    # Public API – state setters
    # ---------------------------------------------------------

    def set_size(self, width: int, height: int) -> None:
        self.width = max(1, width)
        self.height = max(1, height)

    def set_zoom(self, zoom: float) -> None:
        self.zoom = max(0.1, zoom)

    def set_events(self, events: List[Dict[str, Any]]) -> None:
        self._events = list(events)

    def set_markers(self, markers: List[Dict[str, Any]]) -> None:
        self._markers = list(markers)

    def set_selected_event(self, event: Optional[Dict[str, Any]]) -> None:
        self._selected_event = event

    def set_playhead(self, x: Optional[int], active: Optional[bool] = None) -> None:
        if x is not None:
            self._playhead["x"] = x
        if active is not None:
            self._playhead["active"] = bool(active)

    def set_hover_box(self, active: bool, **kwargs) -> None:
        self._hover = {"active": active, **kwargs}

    def set_grid_hover(self, active: bool, **kwargs) -> None:
        self._grid_hover = {"active": active, **kwargs}

    def set_dragging_event(self, active: bool, **kwargs) -> None:
        self._dragging_event = {"active": active, **kwargs}

    def set_resizing_event(self, active: bool, **kwargs) -> None:
        self._resizing_event = {"active": active, **kwargs}

    def set_event_overlap(self, active: bool, **kwargs) -> None:
        self._event_overlap = {"active": active, **kwargs}

    def set_dragging_marker(self, active: bool, **kwargs) -> None:
        self._dragging_marker = {"active": active, **kwargs}

    def set_snapping(self, active: bool, **kwargs) -> None:
        self._snapping = {"active": active, **kwargs}

    def set_ghost(self, active: bool, **kwargs) -> None:
        self._ghost = {"active": active, **kwargs}

    def reset_overlays(self) -> None:
        self._hover["active"] = False
        self._grid_hover["active"] = False
        self._dragging_event["active"] = False
        self._resizing_event["active"] = False
        self._event_overlap["active"] = False
        self._dragging_marker["active"] = False
        self._snapping["active"] = False
        self._ghost["active"] = False

    # ---------------------------------------------------------
    # Internal layout builders
    # ---------------------------------------------------------

    def _build_header(self) -> List[Dict[str, Any]]:
        blocks = [{"type": "text", "x": 0, "y": 0, "content": "Timeline"}]
        for x in range(0, self.width, self.grid_step):
            blocks.append({"type": "text", "x": x, "y": 1, "content": f"{x}"})
        return blocks

    def _build_marker_lane(self) -> List[Dict[str, Any]]:
        return [{
            "type": "marker_lane",
            "x": 0,
            "y": self.marker_lane_y,
            "width": self.width,
            "height": self.marker_lane_height,
            "color": "darkgray",
        }]

    def _build_grid(self) -> List[Dict[str, Any]]:
        blocks = []
        if self.zoom < 0.75:
            step = self.grid_step * 2
        elif self.zoom > 1.5:
            step = max(2, self.grid_step // 2)
        else:
            step = self.grid_step

        for x in range(0, self.width, step):
            blocks.append({
                "type": "grid_line",
                "x": x,
                "y": self.marker_lane_y + self.marker_lane_height,
                "height": self.height - (self.marker_lane_y + self.marker_lane_height),
            })
        return blocks

    def _build_grid_hover_overlay(self) -> List[Dict[str, Any]]:
        gh = self._grid_hover
        if not gh.get("active"):
            return []
        return [{
            "type": "grid_hover",
            "x": gh.get("x", 0),
            "y": self.marker_lane_y + self.marker_lane_height,
            "width": gh.get("width", 0),
            "height": self.height - (self.marker_lane_y + self.marker_lane_height),
            "color": gh.get("color", "lightblue"),
            "opacity": 0.2,
        }]

    def _build_playhead_overlay(self) -> List[Dict[str, Any]]:
        ph = self._playhead
        if not ph.get("active"):
            return []
        return [{
            "type": "playhead",
            "x": ph.get("x", 0),
            "y": 0,
            "height": self.height,
            "color": ph.get("color", "red"),
            "opacity": 1.0,
        }]

    def _build_events(self) -> List[Dict[str, Any]]:
        return [{
            "type": "event",
            "x": ev["x"],
            "y": ev["y"],
            "width": ev["width"],
            "height": ev["height"],
            "label": ev.get("label", ""),
        } for ev in self._events]

    def _build_event_drag_overlay(self) -> List[Dict[str, Any]]:
        de = self._dragging_event
        if not de.get("active"):
            return []
        return [{
            "type": "event_drag_ghost",
            "x": de.get("x", 0),
            "y": de.get("y", 0),
            "width": de.get("width", 0),
            "height": de.get("height", 0),
            "opacity": 0.5,
            "label": de.get("label", ""),
        }]

    def _build_event_resize_overlay(self) -> List[Dict[str, Any]]:
        re = self._resizing_event
        if not re.get("active"):
            return []
        blocks = [{
            "type": "event_resize_ghost",
            "x": re.get("x", 0),
            "y": re.get("y", 0),
            "width": re.get("width", 0),
            "height": re.get("height", 0),
            "opacity": 0.5,
            "label": re.get("label", ""),
        }]
        handle_x = re.get("x", 0) + re.get("width", 0) if re.get("handle") == "right" else re.get("x", 0)
        blocks.append({
            "type": "resize_handle",
            "x": handle_x,
            "y": re.get("y", 0),
            "height": re.get("height", 0),
            "color": "orange",
        })
        return blocks

    def _build_event_overlap_overlay(self) -> List[Dict[str, Any]]:
        eo = self._event_overlap
        if not eo.get("active"):
            return []
        return [{
            "type": "event_overlap",
            "x": eo.get("x", 0),
            "y": eo.get("y", 0),
            "width": eo.get("width", 0),
            "height": eo.get("height", 0),
            "color": eo.get("color", "red"),
            "opacity": 0.3,
        }]

    def _build_hover_overlay(self) -> List[Dict[str, Any]]:
        h = self._hover
        if not h.get("active"):
            return []
        return [{
            "type": "hover_box",
            "x": h.get("x", 0),
            "y": h.get("y", 0),
            "width": h.get("width", 0),
            "height": h.get("height", 0),
            "color": h.get("color", "white"),
            "opacity": 0.3,
        }]

    def _build_markers(self) -> List[Dict[str, Any]]:
        return [{
            "type": "marker",
            "x": m["x"],
            "y": self.marker_lane_y,
            "icon": m.get("icon", ""),
            "label": m.get("label", ""),
            "color": m.get("color", "white"),
        } for m in self._markers]

    def _build_marker_drag_overlay(self) -> List[Dict[str, Any]]:
        dm = self._dragging_marker
        if not dm.get("active"):
            return []
        return [{
            "type": "marker_drag_ghost",
            "x": dm.get("x", 0),
            "y": self.marker_lane_y,
            "icon": dm.get("icon", ""),
            "label": dm.get("label", ""),
            "color": dm.get("color", "white"),
            "opacity": 0.5,
        }]

    def _build_snapping_overlay(self) -> List[Dict[str, Any]]:
        sn = self._snapping
        if not sn.get("active"):
            return []
        return [{
            "type": "snapping_line",
            "x": sn.get("x", 0),
            "y": 0,
            "height": self.height,
            "color": sn.get("color", "cyan"),
            "opacity": 0.4,
        }]

    def _build_ghost_overlay(self) -> List[Dict[str, Any]]:
        gh = self._ghost
        if not gh.get("active"):
            return []
        return [{
            "type": "ghost_block",
            "x": gh.get("x", 0),
            "y": gh.get("y", 0),
            "width": gh.get("width", 0),
            "height": gh.get("height", 0),
            "color": gh.get("color", "gray"),
            "opacity": 0.2,
        }]

    def _build_selection_overlay(self) -> List[Dict[str, Any]]:
        sel = self._selected_event
        if not sel:
            return []
        return [{
            "type": "selection_box",
            "x": sel["x"],
            "y": sel["y"],
            "width": sel["width"],
            "height": sel["height"],
            "color": "yellow",
            "thickness": 1,
        }]
