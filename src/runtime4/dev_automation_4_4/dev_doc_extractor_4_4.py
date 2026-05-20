dev_automation_4_4/dev_doc_extractor_4_4.py
"""
SIRIUS LOCAL AI – Developer Documentation Extractor 4.4.0

This module provides deterministic, offline‑safe documentation extraction
for Developer Automation 4.4. It supports:

- Extracting docstrings from Python modules
- Extracting inline comments
- Building structured documentation trees
- Generating summaries and metadata
- Security‑aware extraction (Security Family 4.4)

All logic is deterministic, offline, and fully isolated.

Security Notes:
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- No execution of source code; only static parsing.
- Fully compatible with Security Family 4.4.
"""

from typing import Dict, Any, List, Optional


class DevDocExtractor44:
    """
    Deterministic documentation extractor for Runtime 4.4.
    """

    def __init__(self, analyzer=None, security_policy=None):
        self.analyzer = analyzer
        self.security_policy = security_policy

        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.analyzer:
                self.analyzer.initialize()

            if self.security_policy:
                self.security_policy.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # PUBLIC API – EXTRACT DOCUMENTATION
    # ------------------------------------------------------------------
    def extract(self, source_code: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extracts documentation from Python source code.

        Supported extraction:
        - module docstring
        - class docstrings
        - function docstrings
        - inline comments (# ...)
        - metadata summary

        Returns:
        {
            "status": "ok",
            "documentation": {...},
        }
        """
        if not self.initialized:
            init_result = self.initialize()
            if init_result.get("status") not in ("initialized", "already_initialized"):
                return {"status": "error", "reason": "extractor_not_initialized", "details": init_result}

        # 1. Security policy check
        if self.security_policy:
            sec = self.security_policy.check_doc_extraction(options)
            if sec.get("status") != "allowed":
                return {"status": "blocked", "policy": sec}

        try:
            doc = {
                "module_doc": self._extract_module_doc(source_code),
                "classes": self._extract_class_docs(source_code),
                "functions": self._extract_function_docs(source_code),
                "comments": self._extract_inline_comments(source_code),
            }

            return {"status": "ok", "documentation": doc}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # INTERNAL – MODULE DOCSTRING
    # ------------------------------------------------------------------
    def _extract_module_doc(self, code: str) -> Optional[str]:
        lines = code.strip().splitlines()
        if not lines:
            return None

        if lines[0].startswith('"""') or lines[0].startswith("'''"):
            doc = []
            quote = lines[0][:3]
            for line in lines[1:]:
                if line.startswith(quote):
                    break
                doc.append(line)
            return "\n".join(doc).strip()

        return None

    # ------------------------------------------------------------------
    # INTERNAL – CLASS DOCSTRINGS
    # ------------------------------------------------------------------
    def _extract_class_docs(self, code: str) -> List[Dict[str, Any]]:
        classes = []
        lines = code.splitlines()

        for i, line in enumerate(lines):
            if line.strip().startswith("class "):
                name = line.strip().split()[1].split("(")[0].replace(":", "")
                doc = self._extract_following_docstring(lines, i + 1)
                classes.append({"name": name, "doc": doc})

        return classes

    # ------------------------------------------------------------------
    # INTERNAL – FUNCTION DOCSTRINGS
    # ------------------------------------------------------------------
    def _extract_function_docs(self, code: str) -> List[Dict[str, Any]]:
        funcs = []
        lines = code.splitlines()

        for i, line in enumerate(lines):
            if line.strip().startswith("def "):
                name = line.strip().split()[1].split("(")[0]
                doc = self._extract_following_docstring(lines, i + 1)
                funcs.append({"name": name, "doc": doc})

        return funcs

    # ------------------------------------------------------------------
    # INTERNAL – INLINE COMMENTS
    # ------------------------------------------------------------------
    def _extract_inline_comments(self, code: str) -> List[str]:
        comments = []
        for line in code.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                comments.append(stripped[1:].strip())
        return comments

    # ------------------------------------------------------------------
    # INTERNAL – DOCSTRING AFTER CLASS/FUNCTION
    # ------------------------------------------------------------------
    def _extract_following_docstring(self, lines: List[str], start: int) -> Optional[str]:
        if start >= len(lines):
            return None

        line = lines[start].strip()
        if line.startswith('"""') or line.startswith("'''"):
            doc = []
            quote = line[:3]
            for l in lines[start + 1:]:
                if l.strip().startswith(quote):
                    break
                doc.append(l.strip())
            return "\n".join(doc).strip()

        return None
