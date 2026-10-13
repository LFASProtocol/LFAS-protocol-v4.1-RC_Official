#!/usr/bin/env python3
"""Validate an LFAS master blueprint against blueprint.schema.json plus referential checks.

Usage:
    python tools/validate_blueprint.py [specs/v4.1-RC/blueprint.json ...]

Exits 0 when every file is valid, 1 otherwise. Diagnostics go to stderr.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BLUEPRINTS = [REPO_ROOT / "specs" / "v4.1-RC" / "blueprint.json"]
SCHEMA_FILENAME = "blueprint.schema.json"

CONTROL_NODE_TYPES = {"Gate", "Layer", "Mode", "Phase"}


def load_json(path: Path) -> tuple[dict | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except FileNotFoundError:
        return None, [f"{path}: file not found"]
    except json.JSONDecodeError as exc:
        return None, [f"{path}:{exc.lineno}:{exc.colno}: invalid JSON: {exc.msg}"]


def schema_errors(blueprint: dict, schema: dict) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return [
            "jsonschema is not installed; run 'python -m pip install jsonschema' "
            "to enable schema validation"
        ]

    validator = jsonschema.Draft7Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(blueprint), key=lambda e: list(e.absolute_path)):
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"schema: {location}: {error.message}")
    return errors


def _as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def reference_errors(blueprint: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    nodes = blueprint.get("nodes", [])
    ids = [node.get("id") for node in nodes]
    names = {node.get("name") for node in nodes}
    name_to_node = {node.get("name"): node for node in nodes if node.get("name") is not None}

    duplicates = {node_id for node_id in ids if ids.count(node_id) > 1}
    for node_id in sorted(duplicates):
        errors.append(f"nodes: duplicate node id '{node_id}'")

    known_ids = set(ids)
    for index, edge in enumerate(blueprint.get("edges", [])):
        for side in ("from", "to"):
            endpoint = edge.get(side)
            if endpoint not in known_ids:
                errors.append(f"edges/{index}: '{side}' references unknown node id '{endpoint}'")

    failure_mode_ids = {fm.get("id") for fm in blueprint.get("failure_modes", [])}

    detector_to_fms: dict[str, set[str]] = {}
    for node in nodes:
        node_id = node.get("id")
        node_type = node.get("type")
        node_name = node.get("name")

        for gate in node.get("gates", []):
            if gate not in names:
                errors.append(f"nodes/{node_id}: gate '{gate}' is not a node in this graph")
            elif name_to_node.get(gate, {}).get("type") not in CONTROL_NODE_TYPES:
                errors.append(f"nodes/{node_id}: gate '{gate}' is not a control node")

        related_fms = _as_list(node.get("related_failure_modes"))
        for fm_id in related_fms:
            if fm_id not in failure_mode_ids:
                errors.append(
                    f"nodes/{node_id}: related_failure_modes contains unknown failure mode '{fm_id}'"
                )

        if node_type == "Detector" and node_name:
            detector_to_fms[node_name] = set(related_fms)

    fm_to_detectors: dict[str, set[str]] = {}
    for fm in blueprint.get("failure_modes", []):
        fm_id = fm.get("id")
        related_detectors = _as_list(fm.get("related_detectors"))

        for det_name in related_detectors:
            if det_name not in names:
                errors.append(
                    f"failure_modes/{fm_id}: related_detectors entry '{det_name}' is not a node in this graph"
                )
            elif name_to_node.get(det_name, {}).get("type") != "Detector":
                errors.append(
                    f"failure_modes/{fm_id}: related_detectors entry '{det_name}' is not a Detector node"
                )

        fm_to_detectors[fm_id] = set(related_detectors)

        prevention_gate = fm.get("prevention_gate")
        if prevention_gate not in names:
            errors.append(
                f"failure_modes/{fm_id}: prevention_gate '{prevention_gate}' is not a node in this graph"
            )
        elif name_to_node.get(prevention_gate, {}).get("type") != "Gate":
            errors.append(
                f"failure_modes/{fm_id}: prevention_gate '{prevention_gate}' is not a Gate node"
            )

    for det_name, fm_set in detector_to_fms.items():
        for fm_id in fm_set:
            if fm_id in fm_to_detectors and det_name not in fm_to_detectors[fm_id]:
                warnings.append(
                    f"asymmetry: detector '{det_name}' lists '{fm_id}' "
                    f"but failure_mode '{fm_id}' does not list '{det_name}'"
                )
    for fm_id, det_set in fm_to_detectors.items():
        for det_name in det_set:
            if det_name in detector_to_fms and fm_id not in detector_to_fms[det_name]:
                warnings.append(
                    f"asymmetry: failure_mode '{fm_id}' lists '{det_name}' "
                    f"but detector '{det_name}' does not list '{fm_id}'"
                )

    for phase in blueprint.get("phases", []):
        if phase not in names:
            errors.append(f"phases: '{phase}' has no corresponding node")
        elif name_to_node.get(phase, {}).get("type") != "Phase":
            errors.append(f"phases: '{phase}' is not a Phase node")

    for index, transition in enumerate(blueprint.get("state_transition_proof", [])):
        for side in ("current_phase", "next_phase"):
            if transition.get(side) not in names:
                errors.append(
                    f"state_transition_proof/{index}: {side} "
                    f"'{transition.get(side)}' has no corresponding node"
                )
            elif name_to_node.get(transition.get(side), {}).get("type") != "Phase":
                errors.append(
                    f"state_transition_proof/{index}: {side} "
                    f"'{transition.get(side)}' is not a Phase node"
                )

    return errors, warnings


def provenance_errors(blueprint: dict) -> list[str]:
    errors: list[str] = []

    def check_ref(label: str, ref: object) -> None:
        if not isinstance(ref, str):
            errors.append(f"{label}: provenance_ref is missing or not a string")
            return
        if not ref or ref.startswith(("http://", "https://")):
            return
        if ref.startswith("#"):
            return

        path = ref.split("#", 1)[0].strip()
        if not path:
            errors.append(f"{label}: provenance_ref '{ref}' has no file path")
            return
        if path.startswith("/"):
            errors.append(f"{label}: provenance_ref '{ref}' must be repo-relative, not absolute")
            return

        resolved = (REPO_ROOT / path).resolve()
        if not resolved.exists():
            errors.append(f"{label}: provenance_ref '{ref}' points to missing file '{path}'")

    for index, node in enumerate(blueprint.get("nodes", [])):
        check_ref(f"nodes/{node.get('id', index)}", node.get("provenance_ref"))

    for index, edge in enumerate(blueprint.get("edges", [])):
        check_ref(f"edges/{index}", edge.get("provenance_ref"))

    for fm in blueprint.get("failure_modes", []):
        check_ref(f"failure_modes/{fm.get('id')}", fm.get("provenance_ref"))

    for index, rule in enumerate(blueprint.get("rules", [])):
        check_ref(f"rules/{index}", rule.get("provenance_ref"))

    return errors


def validate(path: Path) -> tuple[list[str], list[str]]:
    blueprint, errors = load_json(path)
    if blueprint is None:
        return errors, []

    schema_path = path.parent / SCHEMA_FILENAME
    schema, schema_load_errors = load_json(schema_path)
    if schema is None:
        return schema_load_errors, []

    ref_errs, warnings = reference_errors(blueprint)
    all_errors = schema_errors(blueprint, schema) + ref_errs + provenance_errors(blueprint)
    return all_errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "blueprints",
        nargs="*",
        type=Path,
        help="blueprint.json files to validate (default: specs/v4.1-RC/blueprint.json)",
    )
    args = parser.parse_args(argv)
    paths = args.blueprints or DEFAULT_BLUEPRINTS

    failed = False
    for path in paths:
        errors, warnings = validate(path)
        if errors:
            failed = True
            print(f"FAIL {path}", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
        else:
            print(f"OK   {path}")
        for warning in warnings:
            print(f"WARN {warning}", file=sys.stderr)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
