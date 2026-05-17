import json
import hashlib
from typing import Any, Dict, List, Optional


class ContextManager:
    """
    ContextManager 4.1
    Manages the internal AI context for SIRIUS LOCAL AI.

    Features:
    - short‑term memory (session)
    - long‑term memory (persistent)
    - system state
    - snapshot history with capacity limit
    - validation & integrity seal
    - rollback
    - diff and merge utilities
    - safe deep-copy operations
    - export / import
    - clear operations
    - profile support (simple)
    """

    def __init__(self):
        # ---------------------------------------------------------
        # MEMORY STRUCTURES
        # ---------------------------------------------------------
        self.session_memory: List[str] = []
        self.persistent_memory: Dict[str, str] = {}
        self.state: Dict[str, Any] = {}

        # ---------------------------------------------------------
        # SNAPSHOT HISTORY
        # ---------------------------------------------------------
        self.history: List[Dict[str, Any]] = []
        self.max_history: int = 20

        # ---------------------------------------------------------
        # PROFILES (simple key → state mapping)
        # ---------------------------------------------------------
        self.profiles: Dict[str, Dict[str, Any]] = {}
        self.active_profile: Optional[str] = None

        # ---------------------------------------------------------
        # INTEGRITY
        # ---------------------------------------------------------
        self.last_integrity_hash: Optional[str] = None

    # ============================================================
    #  SHORT‑TERM MEMORY
    # ============================================================
    def remember(self, text: str):
        """Append a new item to session memory."""
        self.session_memory.append(text)

    def get_recent(self, limit: int = 5) -> List[str]:
        """Return the last N items from session memory."""
        if limit <= 0:
            return []
        return self.session_memory[-limit:]

    def clear_session(self):
        """Clear short‑term memory."""
        self.session_memory = []

    # ============================================================
    #  LONG‑TERM MEMORY
    # ============================================================
    def store(self, key: str, value: str):
        """Store a key-value pair in persistent memory."""
        self.persistent_memory[key] = value

    def recall(self, key: str) -> Optional[str]:
        """Retrieve a value from persistent memory."""
        return self.persistent_memory.get(key)

    def clear_persistent(self):
        """Clear long‑term memory (in‑memory representation)."""
        self.persistent_memory = {}

    # ============================================================
    #  TRANSLATION (placeholder)
    # ============================================================
    def translate(self, text: str, target_lang: str = "en") -> str:
        """Placeholder translation method."""
        return f"[translate → {target_lang}] {text}"

    # ============================================================
    #  STATE MANAGEMENT
    # ============================================================
    def set_state(self, key: str, value: Any):
        """Set a state variable."""
        self.state[key] = value

    def get_state(self, key: str) -> Any:
        """Retrieve a state variable."""
        return self.state.get(key)

    def clear_state(self):
        """Clear all state variables."""
        self.state = {}

    # ============================================================
    #  VALIDATION & INTEGRITY
    # ============================================================
    def _compute_integrity_hash(self) -> str:
        """
        Compute a deterministic hash of the current context.
        Used for integrity checks and self‑repair diagnostics.
        """
        payload = {
            "session": self.session_memory,
            "persistent": self.persistent_memory,
            "state": self.state,
        }
        serialized = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    def validate(self) -> bool:
        """Validate internal structures and snapshot integrity."""
        if not isinstance(self.session_memory, list):
            return False
        if not isinstance(self.persistent_memory, dict):
            return False
        if not isinstance(self.state, dict):
            return False
        if not isinstance(self.history, list):
            return False

        # Validate snapshots
        for snap in self.history:
            if not isinstance(snap, dict):
                return False
            if "session" not in snap or "persistent" not in snap or "state" not in snap:
                return False

        return True

    def seal_integrity(self):
        """
        Store the current integrity hash.
        Self‑Repair 4.4 can compare this later.
        """
        self.last_integrity_hash = self._compute_integrity_hash()

    def is_integrity_unchanged(self) -> bool:
        """
        Check if the current context matches the last sealed hash.
        Returns False if no seal exists.
        """
        if self.last_integrity_hash is None:
            return False
        return self.last_integrity_hash == self._compute_integrity_hash()

    # ============================================================
    #  SNAPSHOT
    # ============================================================
    def snapshot(self):
        """Create a snapshot of the current context."""
        snap = {
            "session": list(self.session_memory),
            "persistent": dict(self.persistent_memory),
            "state": dict(self.state),
        }
        self.history.append(snap)

        # Enforce capacity
        if len(self.history) > self.max_history:
            self.history.pop(0)

    # ============================================================
    #  ROLLBACK
    # ============================================================
    def rollback(self, steps: int = 1) -> bool:
        """
        Roll back the context by N snapshots.
        Returns True on success, False on invalid request.
        """
        if steps <= 0 or steps > len(self.history):
            return False

        snap = self.history[-steps]

        self.session_memory = list(snap["session"])
        self.persistent_memory = dict(snap["persistent"])
        self.state = dict(snap["state"])

        # Remove snapshots after rollback point
        del self.history[-steps + 1 :]

        return True

    # ============================================================
    #  DIFF
    # ============================================================
    def diff(self, other_state: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """
        Compare current state with another state dictionary.
        Returns a dict of differences.
        """
        differences: Dict[str, Dict[str, Any]] = {}

        # Keys in other_state
        for key, value in other_state.items():
            if self.state.get(key) != value:
                differences[key] = {
                    "current": self.state.get(key),
                    "incoming": value,
                }

        # Keys missing in other_state
        for key in self.state:
            if key not in other_state:
                differences[key] = {
                    "current": self.state[key],
                    "incoming": None,
                }

        return differences

    # ============================================================
    #  MERGE
    # ============================================================
    def merge(self, new_state: Dict[str, Any]):
        """
        Safely merge new state values into the current state.
        """
        for key, value in new_state.items():
            if isinstance(key, str):
                self.state[key] = value

    # ============================================================
    #  EXPORT / IMPORT
    # ============================================================
    def export_context(self) -> Dict[str, Any]:
        """
        Export the entire context as a serializable dictionary.
        """
        return {
            "session": list(self.session_memory),
            "persistent": dict(self.persistent_memory),
            "state": dict(self.state),
            "history": list(self.history),
            "profiles": dict(self.profiles),
            "active_profile": self.active_profile,
        }

    def import_context(self, data: Dict[str, Any]):
        """
        Import context from a dictionary.
        Unsafe input should be validated before calling this.
        """
        self.session_memory = list(data.get("session", []))
        self.persistent_memory = dict(data.get("persistent", {}))
        self.state = dict(data.get("state", {}))
        self.history = list(data.get("history", []))
        self.profiles = dict(data.get("profiles", {}))
        self.active_profile = data.get("active_profile")

    # ============================================================
    #  CLEAR OPERATIONS
    # ============================================================
    def clear_all(self):
        """Clear all context data (session, persistent, state, history)."""
        self.session_memory = []
        self.persistent_memory = {}
        self.state = {}
        self.history = []
        self.profiles = {}
        self.active_profile = None
        self.last_integrity_hash = None

    # ============================================================
    #  PROFILES (SIMPLE)
    # ============================================================
    def save_profile(self, name: str):
        """
        Save current state as a named profile.
        Only state is stored (not full memory).
        """
        if not isinstance(name, str) or not name:
            return
        self.profiles[name] = {
            "state": dict(self.state),
        }

    def load_profile(self, name: str) -> bool:
        """
        Load a named profile into current state.
        Returns True on success.
        """
        profile = self.profiles.get(name)
        if not profile:
            return False

        self.state = dict(profile.get("state", {}))
        self.active_profile = name
        return True

    def list_profiles(self) -> List[str]:
        """Return a list of available profile names."""
        return sorted(self.profiles.keys())
