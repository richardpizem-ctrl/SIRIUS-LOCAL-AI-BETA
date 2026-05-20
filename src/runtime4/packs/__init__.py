"""
SIRIUS LOCAL AI – PACKS 4.4 Package (PRO)

Provides:
- PackGraphExpander44
- PackLinker44
- KnowledgePackLoader44
- KnowledgePackValidator44
- PackDeltaUpdater44
- PackDynamicLoader44

This package manages:
- Knowledge Pack structure
- Dependency linking
- Validation
- Loading and registration into Runtime 4.4
- Deterministic graph expansion
- Safe delta updates
- Dynamic (non-executing) pack loading

Security Notes (Runtime 4.4 PRO):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
- All modules must be deterministic, offline, and isolated.
- Fully compatible with Security Family 4.4.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA
# -------------------------------------------------------------------------

PACKS_VERSION = "4.4"
SECURITY_FAMILY_COMPAT = "4.4"

# -------------------------------------------------------------------------
# SAFE STATIC IMPORTS
# -------------------------------------------------------------------------

from .pack_graph_expander_4_4 import PackGraphExpander44
from .pack_linker_4_4 import PackLinker44
from .kp_loader_4_4 import KnowledgePackLoader44
from .kp_validator_4_4 import KnowledgePackValidator44
from .pack_delta_updater_4_4 import PackDeltaUpdater44
from .pack_dynamic_loader_4_4 import PackDynamicLoader44

# -------------------------------------------------------------------------
# SAFE EXPORT LIST
# -------------------------------------------------------------------------

__all__ = [
    "PackGraphExpander44",
    "PackLinker44",
    "KnowledgePackLoader44",
    "KnowledgePackValidator44",
    "PackDeltaUpdater44",
    "PackDynamicLoader44",
    "PACKS_VERSION",
    "SECURITY_FAMILY_COMPAT",
]
