"""
SIRIUS LOCAL AI – Email Package 4.3
-----------------------------------
This package contains all email‑related modules used by the SIRIUS Runtime 4.x.

The email subsystem provides:
- profile management
- validation and safety checks
- message rendering
- storage and metadata handling
- integration with the command layer
- deterministic behavior for Runtime4
- Self‑Repair 4.4 compatibility

Notes:
- Modules inside this package are dynamically loaded by the runtime.
- No imports are performed here to avoid side‑effects during initialization.
- This package is part of the SIRIUS LOCAL AI modular architecture.
"""

__all__ = [
    "email_storage",
    "email_validator",
    "email_renderer",
    "email_profile_manager",
    "email_manager",
]
