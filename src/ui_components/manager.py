# manager.py
# SIRIUS LOCAL AI – UI Manager 4.3.x
# Phase‑4 deterministic UI component orchestrator

from typing import Dict, Type, Optional
from .pixel_layout_engine import PixelLayoutEngine


class UIComponent:
    """
    Base class for all UI components.

    Phase‑4 requirements:
        - mount()
        - unmount()
        - render() → returns layout blocks
        - safe-mode compatible
        - degraded-mode compatible
    """

    safe_mode: bool = False
    degraded_mode: bool = False

    def mount(self):
        raise NotImplementedError

    def unmount(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError


class UIManager:
    """
    UIManager 4.3.x

    Responsibilities:
        - Component registration
        - Component lifecycle (mount/unmount)
        - Active component switching
        - Safe-mode and degraded-mode behavior
        - Integration with PixelLayoutEngine Phase‑4
        - Deterministic, offline-only behavior
        - Error-safe rendering
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

        self._registry: Dict[str, Type[UIComponent]] = {}
        self._instances: Dict[str, UIComponent] = {}
        self._active: Optional[str] = None
        self._layout_engine: Optional[PixelLayoutEngine] = None

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------

    def register(self, name: str, component_cls: Type[UIComponent]):
        """Register a UI component class under a unique name."""
        if name in self._registry:
            raise ValueError(f"UI component '{name}' already registered")

        self._registry[name] = component_cls

    def unregister(self, name: str):
        """Remove a component from registry."""
        if name in self._instances:
            try:
                self._instances[name].unmount()
            except Exception:
                pass
            del self._instances[name]

        self._registry.pop(name, None)

    # ---------------------------------------------------------
    # COMPONENT ACCESS
    # ---------------------------------------------------------

    def get(self, name: str) -> UIComponent:
        """Return an instance of a component, creating it if needed."""
        if name not in self._registry:
            raise KeyError(f"UI component '{name}' not found")

        if name not in self._instances:
            try:
                self._instances[name] = self._registry[name]()
            except Exception:
                self.degraded_mode = True
                raise

        return self._instances[name]

    # ---------------------------------------------------------
    # LIFECYCLE CONTROL
    # ---------------------------------------------------------

    def activate(self, name: str):
        """Activate a component and deactivate the previous one."""
        if self.safe_mode:
            return {"status": "safe_mode", "component": None}

        if name not in self._registry:
            raise KeyError(f"UI component '{name}' not found")

        # Unmount previous
        if self._active and self._active in self._instances:
            try:
                self._instances[self._active].unmount()
            except Exception:
                self.degraded_mode = True

        # Mount new
        try:
            instance = self.get(name)
            instance.mount()
            self._active = name
            return {"status": "ok", "component": name}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "component": name,
                "exception": str(exc),
                "degraded_mode": True,
            }

    def deactivate(self):
        """Deactivate the currently active component."""
        if self._active and self._active in self._instances:
            try:
                self._instances[self._active].unmount()
            except Exception:
                self.degraded_mode = True

        self._active = None

    # ---------------------------------------------------------
    # LAYOUT ENGINE INTEGRATION
    # ---------------------------------------------------------

    def connect_layout_engine(self, engine: PixelLayoutEngine):
        """Attach PixelLayoutEngine instance."""
        self._layout_engine = engine

    # ---------------------------------------------------------
    # RENDERING
    # ---------------------------------------------------------

    def render_active(self):
        """
        Render the currently active component and forward to PixelLayoutEngine.
        Deterministic, safe-mode aware, error-safe.
        """

        if self.safe_mode:
            return {"status": "safe_mode", "layout": None}

        if not self._active:
            return {"status": "no_active_component", "layout": None}

        instance = self._instances.get(self._active)
        if not instance:
            return {"status": "missing_instance", "layout": None}

        try:
            layout = instance.render()

            if self._layout_engine:
                try:
                    self._layout_engine.render_blocks(layout)
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "layout": layout}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "layout": None,
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # DEBUG / INTROSPECTION
    # ---------------------------------------------------------

    def list_components(self):
        return list(self._registry.keys())

    def active_component(self):
        return self._active

    # ---------------------------------------------------------
    # SAFE-MODE
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True
        if self._active and self._active in self._instances:
            try:
                self._instances[self._active].unmount()
            except Exception:
                pass

    def exit_safe_mode(self):
        self.safe_mode = False

    def is_safe_mode(self):
        return self.safe_mode

    def is_degraded_mode(self):
        return self.degraded_mode
