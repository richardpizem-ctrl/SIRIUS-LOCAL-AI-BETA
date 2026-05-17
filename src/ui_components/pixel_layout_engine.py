# pixel_layout_engine.py
# PixelLayoutEngine – deterministic Phase‑4 layout renderer
# SIRIUS LOCAL AI – ui_components (4.3.x)

from typing import List, Dict, Any


class PixelLayoutEngine:
    """
    PixelLayoutEngine 4.3.x

    Responsibilities:
        - Receive layout blocks from UI components
        - Validate and sanitize blocks
        - Provide safe-mode and degraded-mode behavior
        - Maintain deterministic last-frame buffer
        - Provide error-safe rendering pipeline
        - Offline-only, no side-effects

    Phase‑4 guarantees:
        - No crashes from invalid blocks
        - No crashes from component errors
        - Structured fallback behavior
    """

    def __init__(self):
        self._last_frame: List[Dict[str, Any]] = []
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # Buffer management
    # ---------------------------------------------------------

    def clear(self):
        """Clear the current frame buffer."""
        self._last_frame = []
        print("PixelLayoutEngine: cleared")

    def get_last_frame(self):
        """Return last rendered frame (for debugging)."""
        return self._last_frame

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate_block(self, block: Dict[str, Any]) -> bool:
        """
        Verify that a block contains at minimum:
            - type
            - x, y
        """
        required = ["type", "x", "y"]
        return all(key in block for key in required)

    def sanitize_block(self, block: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ensure block contains only safe keys.
        Phase‑4: remove unknown keys silently.
        """
        allowed = {"type", "x", "y", "value", "color", "width", "height"}
        return {k: v for k, v in block.items() if k in allowed}

    # ---------------------------------------------------------
    # Rendering pipeline
    # ---------------------------------------------------------

    def render_blocks(self, blocks: List[Dict[str, Any]]):
        """
        Main method – receives layout blocks from a UI component.
        Phase‑4:
            - safe-mode bypass
            - degraded-mode fallback
            - validation + sanitization
            - error-safe rendering
        """

        if self.safe_mode:
            self._last_frame = [
                {"type": "text", "x": 0, "y": 0, "value": "SAFE MODE – UI DISABLED"}
            ]
            self.render(self._last_frame)
            return

        if not isinstance(blocks, list):
            self.degraded_mode = True
            self._last_frame = [
                {"type": "text", "x": 0, "y": 0, "value": "INVALID BLOCK LIST"}
            ]
            self.render(self._last_frame)
            return

        validated = []
        for block in blocks:
            try:
                if self.validate_block(block):
                    validated.append(self.sanitize_block(block))
                else:
                    print(f"[PixelLayoutEngine] Ignoring invalid block: {block}")
            except Exception:
                self.degraded_mode = True

        self._last_frame = validated

        try:
            self.render(validated)
        except Exception:
            self.degraded_mode = True
            self._last_frame = [
                {"type": "text", "x": 0, "y": 0, "value": "RENDER ERROR – DEGRADED MODE"}
            ]
            self.render(self._last_frame)

    # ---------------------------------------------------------
    # Placeholder renderer
    # ---------------------------------------------------------

    def render(self, blocks: List[Dict[str, Any]]):
        """
        Placeholder renderer.
        Future versions will connect to:
            - terminal renderer
            - GUI renderer
            - canvas renderer
            - animations
        """
        print("\n[PixelLayoutEngine] Rendering layout:")
        for block in blocks:
            print(f"  → {block}")
