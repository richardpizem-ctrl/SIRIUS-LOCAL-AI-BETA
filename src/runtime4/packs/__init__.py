"""
SIRIUS LOCAL AI – PACKS 4.3 Package

Provides:
- PackGraph4
- PackLinker4
- PackLoader4
- PackValidator4

This package manages:
- knowledge pack structure
- dependency linking
- validation
- loading and registration into Runtime 4.3

Security Notes (Runtime 4.3):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
- Compatible with Security Family 4.4.
"""

from .pack_graph import PackGraph4
from .pack_linker import PackLinker4
from .pack_loader import PackLoader4
from .pack_validator import PackValidator4

PACKS_VERSION = "4.3"
SECURITY_FAMILY_COMPAT = "4.4"

__all__ = [
    "PackGraph4",
    "PackLinker4",
    "PackLoader4",
    "PackValidator4",
    "PACKS_VERSION",
    "SECURITY_FAMILY_COMPAT",
]
