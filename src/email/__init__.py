"""
SIRIUS LOCAL AI – Email Package 4.5
-----------------------------------
This package contains all email‑related modules used by the SIRIUS Runtime 4.x.

The email subsystem provides:
- profile management
- validation and safety checks
- message rendering
- storage and metadata handling
- integration with the command layer
- deterministic behavior for Runtime4.5
- Self‑Repair Layer 4.5 compatibility
- stable metadata contract for NL Router 4.5

Notes:
- Modules inside this package are dynamically loaded by the runtime.
- No imports are performed here to avoid side‑effects during initialization.
- This package is part of the SIRIUS LOCAL AI modular architecture.
- All modules must follow the Runtime4.5 deterministic execution model.
"""

__all__ = [
    "email_storage",
    "email_validator",
    "email_renderer",
    "email_profile_manager",
    "email_manager",
]
