# pixel_layout_engine.py
# PixelLayoutEngine – central renderer for UI layout blocks
# SIRIUS LOCAL AI – ui_components (Phase 4)

from typing import List, Dict, Any

class PixelLayoutEngine:
    """
    PixelLayoutEngine receives layout blocks from UI components
    and renders them into the target output (terminal, canvas, GUI, etc.)

    In this phase (Phase 4) it is a stable skeleton:
        - render_blocks() accepts a list of blocks
        - validate_block() checks block format correctness
        - render() performs the actual rendering (placeholder)
        - clear() resets the buffer
        - get_last_frame() returns the last rendered frame
    """

    def __init__(self):
        self._last_frame = None

    # ---------------------------------------------------------
    # Buffer management
    # ---------------------------------------------------------

    def clear(self):
        """Clear the current frame buffer."""
        self._last_frame = None
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

    # ---------------------------------------------------------
    # Rendering pipeline
    # ---------------------------------------------------------

    def render_blocks(self, blocks: List[Dict[str, Any]]):
        """
        Main method – receives layout blocks from a UI component.
        In Phase 4 it performs only safe logging and validation.
        """
        if not isinstance(blocks, list):
            raise ValueError("render_blocks() expects a list of blocks")

        validated = []
        for block in blocks:
            if self.validate_block(block):
                validated.append(block)
            else:
                print(f"[PixelLayoutEngine] Ignoring invalid block: {block}")

        self._last_frame = validated
        self.render(validated)

    def render(self, blocks: List[Dict[str, Any]]):
        """
        Placeholder renderer.
        In the future this will connect to:
            - terminal renderer
            - GUI renderer
            - canvas renderer
            - animations
        """
        print("\n[PixelLayoutEngine] Rendering layout:")
        for block in blocks:
            print(f"  → {block}")
