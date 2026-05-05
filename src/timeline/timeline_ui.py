# timeline_ui.py
# Core Timeline UI logic – generates layout blocks for PixelLayoutEngine
# SIRIUS LOCAL AI – timeline (Phase 4+)

from typing import List, Dict, Any, Optional


class TimelineUI:
    """
    TimelineUI is the logical layer of the timeline.
    It knows nothing about the concrete renderer – it only generates layout blocks.

    In Phase 4 it provides:
        - base grid (C4 adaptive)
        - header
        - placeholder events
        - snapping overlay (C1)
        - ghost dragging overlay (C2)
        - selection overlay (C3)
        - marker types (C5)
        - marker lane (C6)
        - marker dragging overlay (C7)
        - event dragging overlay (C8)
        - event resize overlay (C9)
        - hover overlay (C10)
        - grid hover overlay (C11)
        - event overlap overlay (C12)
        - playhead overlay (C13)

    Extended API (Phase 4+):
        - public setters for events, markers, zoom, playhead
        - state update helpers for hover, drag, resize, overlap
        - simple reset helpers for overlays
    """

    def __init__(self):
        # Base timeline dimensions
        self.width: int = 120
        self.height: int = 20
        self.grid_step: int = 10
        self.zoom: float = 1.0  # C4 – placeholder zoom level

        # Marker lane height (C6)
        self.marker_lane_y: int = 2
        self.marker_lane_height: int = 1

        # Placeholder events
        self._events: List[Dict[str, Any]] = [
            {"x": 5, "y": 4, "width": 15, "height": 3, "label": "Demo event"}
        ]

        # Placeholder selected event (C3)
        self._selected_event: Optional[Dict[str, Any]] = {
            "x": 5,
            "y": 4,
            "width": 15,
            "height": 3,
        }

        # C5 – Marker types
        self._markers: List[Dict[str, Any]] = [
            {"x": 10, "icon": "🔵", "label": "Section Start", "color": "blue"},
            {"x": 40, "icon": "🟢", "label": "Loop Start", "color": "green"},
            {"x": 80, "icon": "🔴", "label": "Error", "color": "red"},
        ]

        # C7 – Marker dragging placeholder
        self._dragging_marker: Dict[str, Any] = {
            "active": True,
            "x": 55,
            "icon": "🟢",
            "label": "Loop Start",
            "color": "green",
        }

        # C8 – Event dragging placeholder
        self._dragging_event: Dict[str, Any] = {
            "active": True,
            "x": 35,
            "y": 4,
            "width": 15,
            "height": 3,
            "label": "Dragging Event",
        }

        # C9 – Event resize placeholder
        self._resizing_event: Dict[str, Any] = {
            "active": True,
            "x": 5,
            "y": 4,
            "width": 20,
            "height": 3,
            "label": "Resizing Event",
            "handle": "right",  # "left" or "right"
        }

        # C10 – Hover overlay placeholder
        self._hover: Dict[str, Any] = {
            "active": True,
            "x": 5,
            "y": 4,
            "width": 15,
            "height": 3,
            "color": "white",
        }

        # C11 – Grid hover placeholder
        self._grid_hover: Dict[str, Any] = {
            "active": True,
            "x": 30,
            "width": 10,
            "color": "lightblue",
        }

        # C12 – Event overlap placeholder
        self._event_overlap: Dict[str, Any] = {
            "active": True,
            "x": 8,
            "y": 4,
            "width": 10,
            "height": 3,
            "color": "red",
        }

        # ---------------------------------------------------------
        # C13 – Playhead placeholder
        # ---------------------------------------------------------
        self._playhead: Dict[str, Any] = {
            "active": True,
            "x": 60,
            "color": "red",
        }

    # ---------------------------------------------------------
    # Public API – layout generation
    # ---------------------------------------------------------

    def render(self) -> List[Dict[str, Any]]:
        """
        Build a flat list of layout blocks representing the current timeline state.
        This is the only method the renderer needs to call.
        """
        layout: List[Dict[str, Any]] = []

        layout.extend(self._build_header())
        layout.extend(self._build_marker_lane())            # C6
        layout.extend(self._build_grid())                   # C4
        layout.extend(self._build_grid_hover_overlay())     # C11
        layout.extend(self._build_playhead_overlay())       # C13
        layout.extend(self._build_events())
        layout.extend(self._build_event_drag_overlay())     # C8
        layout.extend(self._build_event_resize_overlay())   # C9
        layout.extend(self._build_event_overlap_overlay())  # C12
        layout.extend(self._build_hover_overlay())          # C10
        layout.extend(self._build_markers())                # C5
        layout.extend(self._build_marker_drag_overlay())    # C7
        layout.extend(self._build_snapping_overlay())       # C1
        layout.extend(self._build_ghost_overlay())          # C2
        layout.extend(self._build_selection_overlay())      # C3

        return layout

    # ---------------------------------------------------------
    # Public API – state setters / helpers (Phase 4+)
    # ---------------------------------------------------------

    def set_size(self, width: int, height: int) -> None:
        """Set the logical size of the timeline."""
        self.width = max(1, width)
        self.height = max(1, height)

    def set_zoom(self, zoom: float) -> None:
        """Set zoom level used by the adaptive grid."""
        self.zoom = max(0.1, zoom)

    def set_events(self, events: List[Dict[str, Any]]) -> None:
        """
        Replace the current event list.

        Expected event keys:
            - x, y, width, height
            - label (optional)
        """
        self._events = list(events)

    def set_markers(self, markers: List[Dict[str, Any]]) -> None:
        """
        Replace the current marker list.

        Expected marker keys:
            - x
            - icon
            - label
            - color
        """
        self._markers = list(markers)

    def set_selected_event(self, event: Optional[Dict[str, Any]]) -> None:
        """Set or clear the selected event box (C3)."""
        self._selected_event = event

    def set_playhead(self, x: Optional[int], active: Optional[bool] = None) -> None:
        """
        Update playhead position and/or active state.

        If x is None, position is not changed.
        If active is None, active flag is not changed.
        """
        if x is not None:
            self._playhead["x"] = x
        if active is not None:
            self._playhead["active"] = bool(active)

    def set_hover_box(
        self,
        active: bool,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        color: Optional[str] = None,
    ) -> None:
        """Update hover overlay (C10)."""
        self._hover["active"] = active
        if x is not None:
            self._hover["x"] = x
        if y is not None:
            self._hover["y"] = y
        if width is not None:
            self._hover["width"] = width
        if height is not None:
            self._hover["height"] = height
        if color is not None:
            self._hover["color"] = color

    def set_grid_hover(
        self,
        active: bool,
        x: Optional[int] = None,
        width: Optional[int] = None,
        color: Optional[str] = None,
    ) -> None:
        """Update grid hover overlay (C11)."""
        self._grid_hover["active"] = active
        if x is not None:
            self._grid_hover["x"] = x
        if width is not None:
            self._grid_hover["width"] = width
        if color is not None:
            self._grid_hover["color"] = color

    def set_dragging_event(
        self,
        active: bool,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        label: Optional[str] = None,
    ) -> None:
        """Update event dragging ghost (C8)."""
        self._dragging_event["active"] = active
        if x is not None:
            self._dragging_event["x"] = x
        if y is not None:
            self._dragging_event["y"] = y
        if width is not None:
            self._dragging_event["width"] = width
        if height is not None:
            self._dragging_event["height"] = height
        if label is not None:
            self._dragging_event["label"] = label

    def set_resizing_event(
        self,
        active: bool,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        label: Optional[str] = None,
        handle: Optional[str] = None,
    ) -> None:
        """Update event resize ghost (C9)."""
        self._resizing_event["active"] = active
        if x is not None:
            self._resizing_event["x"] = x
        if y is not None:
            self._resizing_event["y"] = y
        if width is not None:
            self._resizing_event["width"] = width
        if height is not None:
            self._resizing_event["height"] = height
        if label is not None:
            self._resizing_event["label"] = label
        if handle in ("left", "right"):
            self._resizing_event["handle"] = handle

    def set_event_overlap(
        self,
        active: bool,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        color: Optional[str] = None,
    ) -> None:
        """Update event overlap overlay (C12)."""
        self._event_overlap["active"] = active
        if x is not None:
            self._event_overlap["x"] = x
        if y is not None:
            self._event_overlap["y"] = y
        if width is not None:
            self._event_overlap["width"] = width
        if height is not None:
            self._event_overlap["height"] = height
        if color is not None:
            self._event_overlap["color"] = color

    def set_dragging_marker(
        self,
        active: bool,
        x: Optional[int] = None,
        icon: Optional[str] = None,
        label: Optional[str] = None,
        color: Optional[str] = None,
    ) -> None:
        """Update marker dragging ghost (C7)."""
        self._dragging_marker["active"] = active
        if x is not None:
            self._dragging_marker["x"] = x
        if icon is not None:
            self._dragging_marker["icon"] = icon
        if label is not None:
            self._dragging_marker["label"] = label
        if color is not None:
            self._dragging_marker["color"] = color

    def reset_overlays(self) -> None:
        """
        Simple helper to disable all transient overlays at once.
        Does not touch events or markers themselves.
        """
        self._hover["active"] = False
        self._grid_hover["active"] = False
        self._dragging_event["active"] = False
        self._resizing_event["active"] = False
        self._event_overlap["active"] = False
        self._dragging_marker["active"] = False

    # ---------------------------------------------------------
    # Internal layout builders
    # ---------------------------------------------------------

    def _build_header(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = [
            {"type": "text", "x": 0, "y": 0, "content": "Timeline"}
        ]

        for x in range(0, self.width, self.grid_step):
            blocks.append({"type": "text", "x": x, "y": 1, "content": f"{x}"})

        return blocks

    # C6 – Marker lane
    def _build_marker_lane(self) -> List[Dict[str, Any]]:
        return [{
            "type": "marker_lane",
            "x": 0,
            "y": self.marker_lane_y,
            "width": self.width,
            "height": self.marker_lane_height,
            "color": "darkgray",
        }]

    # C4 – Adaptive grid
    def _build_grid(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

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

    # C11 – Grid hover overlay
    def _build_grid_hover_overlay(self) -> List[Dict[str, Any]]:
        if not self._grid_hover["active"]:
            return []

        gh = self._grid_hover

        return [{
            "type": "grid_hover",
            "x": gh["x"],
            "y": self.marker_lane_y + self.marker_lane_height,
            "width": gh["width"],
            "height": self.height - (self.marker_lane_y + self.marker_lane_height),
            "color": gh["color"],
            "opacity": 0.2,
        }]

    # ---------------------------------------------------------
    # C13 – Playhead overlay
    # ---------------------------------------------------------

    def _build_playhead_overlay(self) -> List[Dict[str, Any]]:
        if not self._playhead["active"]:
            return []

        ph = self._playhead

        return [{
            "type": "playhead",
            "x": ph["x"],
            "y": 0,
            "height": self.height,
            "color": ph["color"],
            "opacity": 1.0,
        }]

    # Events
    def _build_events(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        for ev in self._events:
            blocks.append({
                "type": "event",
                "x": ev["x"],
                "y": ev["y"],
                "width": ev["width"],
                "height": ev["height"],
                "label": ev.get("label", ""),
            })

        return blocks

    # C8 – Event dragging overlay
    def _build_event_drag_overlay(self) -> List[Dict[str, Any]]:
        if not self._dragging_event["active"]:
            return []

        de = self._dragging_event

        return [{
            "type": "event_drag_ghost",
            "x": de["x"],
            "y": de["y"],
            "width": de["width"],
            "height": de["height"],
            "opacity": 0.5,
            "label": de["label"],
        }]

    # C9 – Event resize overlay
    def _build_event_resize_overlay(self) -> List[Dict[str, Any]]:
        if not self._resizing_event["active"]:
            return []

        re = self._resizing_event

        blocks: List[Dict[str, Any]] = [{
            "type": "event_resize_ghost",
            "x": re["x"],
            "y": re["y"],
            "width": re["width"],
            "height": re["height"],
            "opacity": 0.5,
            "label": re["label"],
        }]

        handle_x = re["x"] + re["width"] if re["handle"] == "right" else re["x"]

        blocks.append({
            "type": "resize_handle",
            "x": handle_x,
            "y": re["y"],
            "height": re["height"],
            "color": "orange",
        })

        return blocks

    # C12 – Event overlap overlay
    def _build_event_overlap_overlay(self) -> List[Dict[str, Any]]:
        if not self._event_overlap["active"]:
            return []

        eo = self._event_overlap

        return [{
            "type": "event_overlap",
            "x": eo["x"],
            "y": eo["y"],
            "width": eo["width"],
            "height": eo["height"],
            "color": eo["color"],
            "opacity": 0.3,
        }]

    # C10 – Hover overlay
    def _build_hover_overlay(self) -> List[Dict[str, Any]]:
        if not self._hover["active"]:
            return []

        h = self._hover

        return [{
            "type": "hover_box",
            "x": h["x"],
            "y": h["y"],
            "width": h["width"],
            "height": h["height"],
            "color": h["color"],
            "opacity": 0.3,
        }]

    # C5 – Marker types
    def _build_markers(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        for m in self._markers:
            blocks.append({
                "type": "marker",
                "x": m["x"],
                "y": self.marker_lane_y,
                "icon": m["icon"],
                "label": m["label"],
                "color": m["color"],
            })

        return blocks

    # C7 – Marker dragging overlay
    def _build_marker_drag_overlay(self) -> List[Dict[str, Any]]:
        if not self._dragging_marker["active"]:
            return []

        dm = self._dragging_marker

        return [{
            "type": "marker_drag_ghost",
            "x": dm["x"],
            "y": self.marker_lane_y,
            "icon": dm["icon"],
            "label": dm["label"],
            "color": dm["color"],
            "opacity": 0.5,
        }]

    # C1 – Snapping overlay
    def _build_snapping_overlay(self) -> List[Dict[str, Any]]:
        return [{
            "type": "snapping_line",
            "x": 30,
            "y": 2,
            "height": self.height - 2,
            "color": "cyan",
        }]

    # C2 – Ghost dragging overlay
    def _build_ghost_overlay(self) -> List[Dict[str, Any]]:
        return [{
            "type": "ghost_event",
            "x": 25,
            "y": 4,
            "width": 15,
            "height": 3,
            "opacity": 0.5,
            "label": "Ghost",
        }]

    # C3 – Selection overlay
    def _build_selection_overlay(self) -> List[Dict[str, Any]]:
        if not self._selected_event:
            return []

        sel = self._selected_event

        return [{
            "type": "selection_box",
            "x": sel["x"],
            "y": sel["y"],
            "width": sel["width"],
            "height": sel["height"],
            "color": "yellow",
            "thickness": 1,
        }]
