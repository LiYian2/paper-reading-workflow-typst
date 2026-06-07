#!/usr/bin/env python3
"""Create a Typst paper-reading scaffold from metadata JSON."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PLACEHOLDERS = {
    "TITLE": "Unknown Title",
    "AUTHORS": "Unknown",
    "AFFILIATIONS": "Unknown",
    "VENUE": "Unknown",
    "YEAR": "Unknown",
    "PAPER_URL": "Unknown",
    "ARXIV_URL": "Unknown",
    "OPENREVIEW_URL": "Unknown",
    "CODE_URL": "Unknown",
    "PROJECT_URL": "Unknown",
    "SCOPE_SUBFIELD": "Unknown",
    "TASK": "Unknown",
    "METHOD_FAMILY": "Unknown",
    "DATA_SOURCES": "Unknown",
    "ARTIFACT_STATUS": "Unknown",
    "THESIS": "[Missing] Fill after reading the full paper.",
    "RESEARCH_QUESTION": "[Missing]",
    "PREVIOUS_GAPS_ROOT_CAUSE": "[Missing]",
    "PROPOSED_SOLUTION_OVERVIEW": "[Missing]",
    "MODEL_ARCHITECTURE_DESIGN": "[Missing]",
    "MATH_ALGO_CORE": "[Missing]",
    "CLAIMS_EVIDENCE_MAP": "[Missing]",
    "DATA_EVALUATION": "[Missing]",
    "EXPERIMENTAL_VALIDATION": "[Missing]",
    "UNSUPPORTED_WEAK_CLAIMS": "[Missing]",
    "FIELD_RELATIONSHIP": "[Missing]",
    "CORE_ASSUMPTIONS": "[Missing]",
    "LIMITATIONS": "[Missing]",
    "REVIEWER_REJECT_CASE": "[Missing]",
    "REVIEWER_ACCEPT_CASE": "[Missing]",
    "OVERALL_EVALUATION": "[Missing]",
    "RED_TEAM": "[Missing]",
    "KG_HOOKS": "[Missing]",
    "OPEN_QUESTIONS": "[Missing]",
    "REFERENCES_CHECKED": "[Missing]",
}


def normalize_key(key: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "_", key.upper()).strip("_")


def stringify(value: object) -> str:
    if value is None or value == "":
        return "Unknown"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) if value else "Unknown"
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("metadata_json", type=Path)
    parser.add_argument("output_typ", type=Path)
    parser.add_argument(
        "--template",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "paper_reading_template.typ",
    )
    args = parser.parse_args()

    metadata = json.loads(args.metadata_json.read_text(encoding="utf-8"))
    values = dict(PLACEHOLDERS)
    for key, value in metadata.items():
        values[normalize_key(key)] = stringify(value)

    content = args.template.read_text(encoding="utf-8")
    for key, value in values.items():
        content = content.replace("{{" + key + "}}", value)

    args.output_typ.parent.mkdir(parents=True, exist_ok=True)
    args.output_typ.write_text(content, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
