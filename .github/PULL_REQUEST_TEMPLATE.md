## What

<!-- What changed in the specification or docs? -->

## Why

<!-- Why is this change needed? Link the issue or discussion if there is one. -->

## Checklist

- [ ] `python tools/validate_blueprint.py specs/v4.1-RC/blueprint.json` passes
- [ ] `python tools/check_filenames.py` passes
- [ ] `python tools/check_references.py` passes
- [ ] `markdownlint --config .markdownlint.json '**/*.md'` passes
- [ ] Files renamed with `git mv` and all references updated, including `MANIFEST.md`
- [ ] `blueprint.schema.json` updated if `blueprint.json` gained new fields, node types or relations
- [ ] `CHANGELOG.md` updated for protocol behaviour changes (and `VERSION_MATRIX.md` if a component was added or removed)
- [ ] No change opens a path to `L5_ACT` that bypasses `L37_SCOPE_CONFIRMATION_GATE`

## Migration notes

<!-- External links to update, consumers affected, or "none". -->
