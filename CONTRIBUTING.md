# Contributing to the LFAS Protocol specification

This is a specification repository: there is no application runtime. Contributions are documentation and machine-readable spec changes, and CI enforces that both stay valid and consistent.

## Repository layout

| Path | Contents |
|------|----------|
| `/specs/<version>/blueprint.json` | Canonical machine-readable master graph for that protocol version |
| `/specs/<version>/blueprint.schema.json` | Schema the blueprint must validate against |
| `/specs/<version>/*.md` | Generation rules and guides |
| `/interaction-autopsy/` | Interaction Autopsy module (detectors, failure modes, audit artifact schema, examples) |
| `/tools/` | Validation scripts run locally and in CI |
| Root `*.md` | Manifest, changelog, version matrix, roadmap, checklist, visual summary |

`MANIFEST.md` is the index of artifacts — update it whenever you add, rename or remove a tracked artifact.

## Filename policy

Enforced by `tools/check_filenames.py`:

- ASCII only. No spaces, em dashes or other non-ASCII characters in any path segment.
- Allowed characters: `A-Z a-z 0-9 . _ -`.
- Every file carries a known extension: `.md`, `.json`, `.yml`, `.yaml`, `.py`, `.txt` (exceptions: `LICENSE`, `.gitignore`, `.gitattributes`).
- No placeholder paths such as `path/to/your/...`.

When you rename a file, use `git mv` (preserves history) and update every reference to it, including `MANIFEST.md`.

## Blueprint changes

- `blueprint.json` is the source of truth. Do not describe protocol structure only in Markdown.
- Add new node types, relations or fields to `blueprint.schema.json` in the same commit.
- Every node and edge needs a `provenance_ref`.
- Detector ids match `D[1-8]`; layer, gate, phase and mode ids match `L<number>`; failure modes match `FM#<nn>` or `FM#NEW_<nn>`.
- Gates and `D7_EVIDENCE_PRESENCE_CHECKER` are fail-closed: changes must not create a path that reaches `L5_ACT` without `L37_SCOPE_CONFIRMATION_GATE`.

## Run the checks locally

```bash
python -m pip install jsonschema
npm install -g markdownlint-cli               # optional, matches the CI lint step

python tools/validate_blueprint.py specs/v4.1-RC/blueprint.json
python tools/check_filenames.py
python tools/check_references.py
markdownlint --config .markdownlint.json '**/*.md'
```

All four checks also run on every pull request via `.github/workflows/validate-spec.yml`. A pull request needs green CI before review.

## Commits and pull requests

- Branch naming: `feature/<area>/<short-description>` or `fix/<area>/<short-description>`.
- One logical change per pull request; fill in `.github/PULL_REQUEST_TEMPLATE.md`.
- Protocol behaviour changes must also update `CHANGELOG.md` and, when a component is added or removed, `VERSION_MATRIX.md`.
