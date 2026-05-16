"""
WinCapabilities Module – Runtime 4.3.0

Responsible for:
- providing an OS UI control interface for UIActions
- abstracting real OS automation (click, write, select, semantic)
- keeping Runtime 4.x deterministic and testable

In 4.3.0 this module is a SAFE ADAPTER:
- no real OS integration yet
- all methods are deterministic
- ready for future Win32/UIA/WinRT bindings in 4.4.0+
"""

class WinCapabilities:
    def __init__(self, dry_run=True):
        """
        dry_run:
            True  = do not touch real OS, only simulate success
            False = future flag for real OS integration (4.4.0+)
        """
        self.dry_run = dry_run
        self.last_calls = []

    # ------------------------------------------------------------
    # INTERNAL LOGGING
    # ------------------------------------------------------------
    def _log(self, action_type, element=None, value=None, result=True):
        entry = {
            "action": action_type,
            "element": getattr(element, "name", element),
            "value": value,
            "result": result,
        }
        self.last_calls.append(entry)
        return entry

    # ------------------------------------------------------------
    # OS-LEVEL ACTIONS (INTERFACE ONLY IN 4.3.0)
    # ------------------------------------------------------------
    def click(self, element):
        """
        OS-level click on a UI element.
        In 4.3.0 this is a deterministic stub.
        """
        # Future: real OS click via Win32/UIA/WinRT
        self._log("click", element, result=True)
        return True

    def write(self, element, text):
        """
        OS-level text input.
        """
        # Future: real OS text input
        self._log("write", element, value=text, result=True)
        return True

    def select(self, element, option):
        """
        OS-level selection in menus/lists.
        """
        # Future: real OS selection
        self._log("select", element, value=option, result=True)
        return True

    def semantic(self, action_name, context=None):
        """
        OS-level semantic actions:
        - open_settings
        - confirm
        - cancel
        - open_window
        - close_window
        """
        # Future: map semantic actions to real OS operations
        self._log("semantic", action_name, value=context, result=True)
        return True
