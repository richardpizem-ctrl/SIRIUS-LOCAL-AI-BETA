# pack_loader.py
"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Loader

Responsible for:
- loading knowledge packs from disk
- validating basic structure
- registering packs into runtime
- preparing packs for graph/linker stages

This is the entry point for Knowledge Packs 2.0.
"""

from typing import Optional


class PackLoader4:
    """
    Loads and registers Knowledge Packs 2.0.
    """

    def __init__(self):
        # Loaded packs stored as:
        # { "pack_name": { "data": ..., "meta": ... } }
        self.packs = {}

    # ---------------------------------------------------------
    # LOADING
    # ---------------------------------------------------------

    def load_pack(self, name: str, data: dict, meta: Optional[dict] = None):
        """
        Loads a pack into memory.
        In real implementation, this will load from disk.
        """
        self.packs[name] = {
            "data": data,
            "meta": meta or {}
        }

    # ---------------------------------------------------------
    # ACCESS
    # ---------------------------------------------------------

    def get_pack(self, name: str):
        """Returns a loaded pack."""
        return self.packs.get(name)

    def list_packs(self):
        """Returns a list of all loaded pack names."""
        return list(self.packs.keys())
