#!/usr/bin/env python3
"""Check documentation cross-references.

Two checks run over every tracked Markdown file:
  1. Legacy names retired by the spec cleanup must not reappear.
  2. Repo-absolute references written as `/path/inside/repo.ext` must resolve,
     as must relative Markdown links such as [text](specs/v4.1-RC/blueprint.json).

Usage:
    python tools/check_references.py [root]

Exits 0 when all references resolve, 1 otherwise.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# (pattern, replacement) - patterns are matched per line, skipping heading lines so that
# document titles containing a retired filename are not flagged.
LEGACY_PATTERNS = [
    (re.compile(r"Roaadmap"), "ROADMAP.md"),
    (
        re.compile(r"v4\.1 Stable\s+—\s+Implementation Validation Checklist"),
        "IMPLEMENTATION_CHECKLIST.md",
    ),
    (
        re.compile(r"lfas_v4\.1-rc_knowledge_graph_blueprint\.json"),
        "specs/v4.1-RC/blueprint.json",
    ),
    (re.compile(r"path/to/your/documentation"), "(removed placeholder path)"),
]
EXTENSIONS = "md|json|yml|yaml|py|txt"
ABSOLUTE_REF = re.compile(rf"`(/[A-Za-z0-9_./-]+\.(?:{EXTENSIONS}))`")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\((?!https?:|mailto:|#)([^)#]+)")
SELF_REFERENTIAL = {"tools/check_references.py"}


def tracked_markdown(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "*.md"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(entry) for entry in result.stdout.split("\0") if entry]


def check_file(root: Path, rel_path: Path) -> list[str]:
    problems: list[str] = []
    text = (root / rel_path).read_text(encoding="utf-8")

    if rel_path.as_posix() not in SELF_REFERENTIAL:
        for lineno, line in enumerate(text.splitlines(), start=1):
            if line.lstrip().startswith("#"):
                continue
            for pattern, replacement in LEGACY_PATTERNS:
                match = pattern.search(line)
                if match:
                    problems.append(
                        f"line {lineno}: references retired name "
                        f"'{match.group(0)}' (use {replacement})"
                    )

    for match in ABSOLUTE_REF.finditer(text):
        target = match.group(1).lstrip("/")
        if not (root / target).exists():
            problems.append(f"reference '/{target}' does not exist")

    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip()
        candidate = (root / rel_path).parent / target
        if not candidate.exists() and not (root / target.lstrip("/")).exists():
            problems.append(f"link '{target}' does not exist")

    return problems


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
    root = args.root.resolve()

    failed = False
    for rel_path in tracked_markdown(root):
        problems = check_file(root, rel_path)
        if problems:
            failed = True
            print(f"FAIL {rel_path}", file=sys.stderr)
            for problem in problems:
                print(f"  - {problem}", file=sys.stderr)

    if failed:
        return 1
    print("OK   all documentation cross-references resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
