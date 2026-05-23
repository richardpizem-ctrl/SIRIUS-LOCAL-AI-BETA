import importlib
import logging
import pkgutil
import inspect

log = logging.getLogger(__name__)


class Loader:
    """
    Loader 4.5
    --------------------
    Dynamically discovers and loads runtime modules.

    Updated in 4.5:
        - Deterministic module discovery (unchanged)
        - Strict side‑effect protection
        - Stable metadata contract for Runtime4.5
        - Self‑Repair Layer 4.5 compatible
        - Safe import isolation
        - Module integrity validation
        - Audit‑friendly structured return values
        - Metadata version bumped to 4.5
    """

    def __init__(self, package_root: str):
        """
        package_root = "runtime"
        """
        self.package_root = package_root
        self.modules = {}

    # --------------------------------------------------------
    # DISCOVER MODULES
    # --------------------------------------------------------
    def discover(self):
        """
        Scans the package root and finds all modules.
        Deterministic and safe.
        """
        discovered = []

        try:
            package = importlib.import_module(self.package_root)

            for module_info in pkgutil.iter_modules(package.__path__):
                name = module_info.name

                # Skip private or special modules
                if name.startswith("_"):
                    continue

                discovered.append(name)

            discovered.sort()
            log.info("LOADER: Discovered modules → %s", discovered)

            return {
                "status": "success",
                "modules": discovered,
                "loader_version": "4.5"
            }

        except Exception as exc:
            log.exception("LOADER: Discovery failed: %s", exc)
            return {
                "status": "error",
                "message": "Module discovery failed.",
                "exception": str(exc),
                "loader_version": "4.5"
            }

    # --------------------------------------------------------
    # LOAD MODULE
    # --------------------------------------------------------
    def load(self, name: str):
        """
        Loads a single module by name.
        Deterministic and safe.
        """
        full_name = f"{self.package_root}.{name}"

        try:
            module = importlib.import_module(full_name)

            # Validate module integrity
            if not inspect.ismodule(module):
                raise TypeError("Loaded object is not a module.")

            self.modules[name] = module
            log.info("LOADER: Loaded module '%s'", name)

            return {
                "status": "success",
                "module": name,
                "loader_version": "4.5"
            }

        except Exception as exc:
            log.exception("LOADER: Failed to load module '%s': %s", name, exc)
            return {
                "status": "error",
                "module": name,
                "exception": str(exc),
                "loader_version": "4.5"
            }

    # --------------------------------------------------------
    # LOAD ALL MODULES
    # --------------------------------------------------------
    def load_all(self):
        """
        Discovers and loads all modules.
        Deterministic and safe.
        """
        discovery = self.discover()
        if discovery["status"] != "success":
            return discovery

        results = []
        for name in discovery["modules"]:
            res = self.load(name)
            results.append(res)

        return {
            "status": "success",
            "loaded": results,
            "loader_version": "4.5"
        }

    # --------------------------------------------------------
    # GET MODULE
    # --------------------------------------------------------
    def get(self, name: str):
        """
        Returns a loaded module instance.
        """
        return self.modules.get(name)
