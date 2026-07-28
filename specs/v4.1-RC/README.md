# LFAS v4.1-RC Specification Files

| File | Role | Canonical? |
|------|------|------------|
| `blueprint.json` | Master Knowledge Graph: phases, layers, gates, detectors (D1-D8), failure modes (FM#), enforcement edges, rules | **Yes — machine-readable source of truth** |
| `blueprint.schema.json` | JSON Schema (draft-07) that `blueprint.json` must validate against | Yes — schema of record |
| `kg_generation_guide.md` | How to instantiate a scenario-specific KG from the master graph (steps, enforcement edge rules, output schema) | Human-readable |
| `generation_rules.md` | Additional generation rules: Meta-Listen (Phase 0), constraint proof, fail-closed, provenance, new discovery, trajectory overlay | Human-readable |

## For implementers

1. Consume `blueprint.json` — never parse the Markdown documents to build a graph.
2. Read `kg_generation_guide.md` and `generation_rules.md` for the rules that generated graphs must satisfy.
3. Every node and edge you emit must carry `provenance_ref` pointing back at a master graph id, transcript or file.
4. `fail_closed` nodes (`D7_EVIDENCE_PRESENCE_CHECKER`, all `Gate` nodes) must block the phase transition when their condition is unmet — never fail open.

## Validate locally

```bash
python -m pip install jsonschema
python tools/validate_blueprint.py specs/v4.1-RC/blueprint.json
```

The validator checks the schema plus referential integrity: every edge endpoint, gate, detector and failure mode referenced in the graph must exist in the graph.

## Versioning

A new protocol version gets a new `specs/<version>/` directory containing its own `blueprint.json` and `blueprint.schema.json`. `specs/v4.1-RC/` is frozen once v4.1 Stable is cut; see `/IMPLEMENTATION_CHECKLIST.md`.
