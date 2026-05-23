"""
SIRIUS LOCAL AI – PACKS 4.5 Package (PRO)

Provides:
- PackGraphExpander45
- PackLinker45
- KnowledgePackLoader45
- KnowledgePackValidator45
- PackDeltaUpdater45
- PackDynamicLoader45

This package manages:
- Knowledge Pack structure
- Dependency linking
- Validation
- Loading and registration into Runtime 4.5
- Deterministic graph expansion
- Safe delta updates
- Dynamic (non-executing) pack loading

Security Notes (Runtime 4.5 PRO):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
- All modules must be deterministic, offline, and isolated.
- Fully compatible with Security Family 4.5.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA
# -------------------------------------------------------------------------

PACKS_VERSION = "4.5"
SECURITY_FAMILY_COMPAT = "4.5"

# -------------------------------------------------------------------------
# SAFE STATIC IMPORTS
# -------------------------------------------------------------------------

from .pack_graph_expander_4_5 import PackGraphExpander45
from .pack_linker_4_5 import PackLinker45
from .kp_loader_4_5 import KnowledgePackLoader45
from .kp_validator_4_5 import KnowledgePackValidator45
from .pack_delta_updater_4_5 import PackDeltaUpdater45
from .pack_dynamic_loader_4_5 import PackDynamicLoader45

# -------------------------------------------------------------------------
# SAFE EXPORT LIST
# -------------------------------------------------------------------------

__all__ = [
    "PackGraphExpander45",
    "PackLinker45",
    "KnowledgePackLoader45",
    "KnowledgePackValidator45",
    "PackDeltaUpdater45",
    "PackDynamicLoader45",
    "PACKS_VERSION",
    "SECURITY_FAMILY_COMPAT",
]
