#!/usr/bin/env python3
"""Enforce the repository filename policy.

Policy (see CONTRIBUTING.md):
  * ASCII only - no spaces, em dashes or other non-ASCII characters
  * Allowed characters: letters, digits, '.', '_', '-'
  * Every file has a known extension (.md, .json, .yml, .yaml, .py, .txt)
  * No placeholder paths such as path/to/your/...

Usage:
    python tools/check_filenames.py [root]

Exits 0 when every tracked path complies, 1 otherwise.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ALLOWED_NAME = re.compile(r"^[A-Za-z0-9._-]+$")
ALLOWED_EXTENSIONS = {".md", ".json", ".yml", ".yaml", ".py", ".txt"}
EXEMPT_NAMES = {".gitignore", ".gitattributes", "LICENSE"}
PLACEHOLDER_SEGMENTS = {"path", "to", "your"}


def tracked_paths(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(entry) for entry in result.stdout.split("\0") if entry]


def path_violations(path: Path) -> list[str]:
    violations = []
    for segment in path.parts:
        if not ALLOWED_NAME.match(segment):
            violations.append(
                f"'{segment}' contains characters outside [A-Za-z0-9._-] (spaces and non-ASCII are banned)"
            )
    if path.name not in EXEMPT_NAMES and path.suffix.lower() not in ALLOWED_EXTENSIONS:
        allowed = ", ".join(sorted(ALLOWED_EXTENSIONS))
        violations.append(f"extension '{path.suffix or '(none)'}' is not one of: {allowed}")
    if set(path.parts[:-1]) & PLACEHOLDER_SEGMENTS:
        violations.append("looks like a placeholder path (path/to/your/...)")
    return violations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (default: the repository containing this script)",
    )
    args = parser.parse_args(argv)

    failed = False
    for path in tracked_paths(args.root):
        violations = path_violations(path)
        if violations:
            failed = True
            print(f"FAIL {path}", file=sys.stderr)
            for violation in violations:
                print(f"  - {violation}", file=sys.stderr)

    if failed:
        return 1
    print("OK   all tracked filenames comply with the filename policy")
    return 0


if __name__ == "__main__":
    sys.exit(main())
