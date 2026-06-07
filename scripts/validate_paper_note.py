#!/usr/bin/env python3
"""Lightweight structural checks for AI paper-reading Typst notes."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "Metadata",
    "One-Sentence Thesis",
    "Research Question",
    "Previous Gaps and Root Cause",
    "Proposed Solution Overview",
    "Model Architecture Design",
    "Mathematical and Algorithmic Core",
    "Claims and Evidence Map",
    "Data, Tasks, and Evaluation Protocol",
    "Experimental Validation by Claim",
    "Unsupported or Weakly Supported Claims",
    "Relationship to the Field",
    "Core Assumptions",
    "Limitations and Failure Modes",
    "Reviewer Case for Rejection",
    "Reviewer Case for Acceptance",
    "Overall Evaluation and Research Taste",
    "Red-Team Review",
    "Knowledge-Graph Hooks",
    "Reading Notes and Open Questions",
    "References Checked",
]

REQUIRED_METADATA = [
    "Authors:",
    "Affiliations:",
    "Venue / Journal / Conference:",
    "Year:",
    "Paper URL:",
    "OpenReview URL:",
    "Code URL:",
    "Scope / Subfield:",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("note", type=Path)
    args = parser.parse_args()

    text = args.note.read_text(encoding="utf-8")
    errors: list[str] = []

    first_section = None
    for line in text.splitlines():
        if line.startswith("== "):
            first_section = line[3:].strip()
            break

    if first_section != "Metadata":
        errors.append("first section must be 'Metadata'")

    for section in REQUIRED_SECTIONS:
        if f"== {section}" not in text:
            errors.append(f"missing section: {section}")

    for field in REQUIRED_METADATA:
        if field not in text:
            errors.append(f"missing metadata field: {field}")

    unresolved = sorted(set(part for part in text.split() if part.startswith("{{") and part.endswith("}}")))
    for token in unresolved:
        errors.append(f"unresolved placeholder: {token}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("OK: paper note structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
