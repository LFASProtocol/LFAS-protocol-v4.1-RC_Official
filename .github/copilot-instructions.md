# GitHub Copilot Instructions for LFAS Protocol v4.1-RC

## Repository Overview

This repository contains the **LFAS (Listen First, Act Second) Protocol v4.1-RC** specification - an AI safety protocol that enforces structured decision-making through automated risk detection and mandatory confirmation gates.

**Repository Type:** Specification and Documentation  
**Status:** Release Candidate (RC)  
**Version:** 4.1-RC (December 2024)  
**Purpose:** Authoritative specification for LFAS safety protocol implementation

## Core Principle

**"Never ACT before understanding and authorization."**

The LFAS protocol enforces AI safety through structured phases (LISTEN → REFLECT → WAIT → ACT → ACKNOWLEDGE), automated risk detection (8 detectors), and mandatory confirmation gates.

## Repository Structure

```
LFAS-protocol-v4.1-RC_Official/
├── .github/
│   ├── copilot-instructions.md          # This file
│   ├── PULL_REQUEST_TEMPLATE.md         # Contributor checklist
│   └── workflows/
│       └── validate-spec.yml            # CI: schema, filename policy, references, markdownlint
├── specs/
│   └── v4.1-RC/
│       ├── README.md                     # Which spec file is canonical
│       ├── blueprint.json                # Master Knowledge Graph (machine-readable, canonical)
│       ├── blueprint.schema.json         # Schema blueprint.json is validated against
│       ├── kg_generation_guide.md        # How to instantiate scenario graphs
│       └── generation_rules.md           # Scenario graph generation rules
├── tools/                                # Validation scripts (also run in CI)
├── MANIFEST.md                           # Repository overview and structure
├── CHANGELOG.md                          # Version history (v2.1 → v4.1-RC)
├── VERSION_MATRIX.md                     # Component continuity heatmap
├── ROADMAP.md                            # Development timeline and next steps
├── CONTRIBUTING.md                       # Filename policy, blueprint rules, local checks
├── Visual_Summary.md                     # Human-readable protocol overview with diagrams
└── IMPLEMENTATION_CHECKLIST.md           # Validation gates for stable release
```

## Key Artifacts

### 1. Master Blueprint (`specs/v4.1-RC/blueprint.json`)
- **The authoritative specification**: valid JSON, validated in CI against `specs/v4.1-RC/blueprint.schema.json`
- Contains: Phases (L2-L6), Safety Layers, Gates, Modes, Detectors (D1-D8), Failure Modes (FM#), enforcement edges, rules
- **Version-locked at 4.1-RC**
- Status: Engine-ready; run `python tools/validate_blueprint.py specs/v4.1-RC/blueprint.json` after any edit
- **Do not modify** without understanding full protocol impact

### 2. Generation Rules (`specs/v4.1-RC/generation_rules.md`)
- Instructions for building scenario-specific enforcement graphs from the master blueprint
- Includes templates for: financial crisis, medical emergency, legal analysis
- Cross-references blueprint nodes and detectors
- **Note**: `kg_generation_guide.md` holds the step-by-step KG instantiation procedure; `generation_rules.md` holds Meta-Listen and the proof/provenance rules

### 3. Documentation Files
- **MANIFEST.md**: Repository overview and artifact descriptions
- **CHANGELOG.md**: Complete version evolution with rationale for all changes
- **VERSION_MATRIX.md**: Component continuity across versions
- **Visual_Summary.md**: Non-technical overview with Mermaid diagrams
- **ROADMAP.md**: Timeline for v4.1 Stable and v4.2+ features
- **CONTRIBUTING.md**: Filename policy, blueprint change rules, local validation commands

## Protocol Components

### Five Phases (Core Loop - Immutable since v2.1)
1. **LISTEN (L2)**: Ingest input, fire detectors (D1-D8)
2. **REFLECT (L3)**: Confirm understanding, no action yet
3. **WAIT (L4)**: Mandatory scope confirmation gate (L37)
4. **ACT (L5)**: Execute with safety layers active
5. **ACKNOWLEDGE (L6)**: Validate deliverable (L41), close with logging

### Eight Detectors
- **D1**: Probability Classifier (uncertainty detection)
- **D2**: Vulnerability Detector (user risk context)
- **D3**: Crisis Detector (immediate harm triggers)
- **D4**: Escalation Router (safe-handoff routing)
- **D5**: User Safety Scorer (risk scoring & mode activation)
- **D6**: Logic Consistency Checker (contradiction detection)
- **D7**: Evidence Presence Checker (missing data detection)
- **D8**: Notability Detector (rare, salient issues requiring emphasis)

### Key Safety Layers
- **L9**: Ambiguity Absorption Layer (AAL) - handles vague requests
- **L16**: Normalization Balancing Layer (NBL) - tone/factual balance
- **L31**: High-Stakes Mode - activated by D3 crisis detection
- **L37**: Scope Confirmation Gate - mandatory WAIT phase checkpoint
- **L41**: Deliverable Check - validates output before acknowledgment
- **L42**: Grounding Evidence Node (GEN) - source token provenance

## Version Lineage

```
v2.1 (March 2024) → Philosophical foundation, core loop established
v3.4 (June 2024) → Policy + Defensive Architecture
v3.6 (August 2024) → Calibration + Oversight, Softening Layer
v4.0 (October 2024) → Text → JSON Schema transition
v4.1-RC (December 2024) → Detectors + Grounding + Proof ← CURRENT
v4.1 Stable (TBD) → Validation complete
v4.2 (Q1 2025) → KG Builder tool + multi-platform integration
```

## Documentation Standards

### Format Conventions
- **Markdown** for all human-readable documentation
- **JSON** for machine-readable specifications (blueprint.json)
- Node identifiers use format: `L##` (layers), `D#` (detectors), `FM#` (failure modes)
- Version identifiers: `v#.#` for releases, `v#.#-RC` for release candidates

### Consistency Requirements
- The **core loop** (5 phases) is immutable and version-locked since v2.1
- The **five pillars** (Ethical Decision-Making, Transparency, Accountability, Contextual Understanding, Collaboration) are unchangeable
- The **core guarantee** ("Never ACT before understanding and authorization") cannot be compromised
- All changes must preserve backward compatibility with core principles

### Documentation Updates
When updating documentation:
1. Maintain consistency with MANIFEST file
2. Update CHANGELOG if adding/modifying features
3. Preserve version lineage information
4. Keep cross-references accurate (e.g., node IDs, detector numbers)
5. Ensure Mermaid diagrams remain valid and render correctly

## File Naming Conventions
- Use underscores for multi-word files: `Visual_Summary.md`
- Version indicators in filenames: `v4.1-RC` format
- Specifications in `specs/` with version subdirectories
- No spaces or non-ASCII characters in any path; see the filename policy in `CONTRIBUTING.md` (enforced by `tools/check_filenames.py`)

## Important Notes for Contributors

### What NOT to Change
- Core loop structure (LISTEN → REFLECT → WAIT → ACT → ACKNOWLEDGE)
- Five pillars definitions
- Core guarantee statement
- Version history in CHANGELOG (only append, never modify past entries)
- Master blueprint structure without full protocol review

### What CAN Be Modified
- Documentation clarity and formatting
- Example scenarios in generation_rules.md
- Visual diagrams for better explanation
- Implementation guidance and best practices
- Roadmap timelines (with rationale)

### When Adding New Content
- Cross-reference existing components in MANIFEST
- Document in CHANGELOG with clear rationale
- Maintain version matrix if adding new features
- Follow existing documentation style and structure
- Ensure JSON schemas remain valid and parseable

## Validation and Testing

This is a **specification repository** with no executable code. Validation focuses on:
- Markdown rendering correctness
- Cross-reference accuracy (node IDs, detector numbers, file paths)
- Diagram rendering (Mermaid syntax)
- Version continuity (CHANGELOG and VERSION_MATRIX alignment)
- Future: JSON schema validity when blueprint.json is implemented as actual JSON

### Before Committing
1. Check markdown formatting renders correctly
2. Verify all cross-references are accurate (node IDs, detector numbers, file paths)
3. Ensure MANIFEST is updated if structure changed
4. Update CHANGELOG if functional changes made
5. If blueprint.json is converted to actual JSON, validate with: `jq . specs/v4.1-RC/blueprint.json`

## Build/Test Instructions

**No build process required** - this is a documentation-only repository.

To preview Markdown locally:
```bash
# Use any markdown previewer or GitHub preview
# GitHub rendering is canonical
```

Note: `blueprint.json` is currently markdown documentation, not JSON. Future versions may implement it as actual JSON schema.

## Next Phase: v4.1 Stable

Current focus is on validation for stable release promotion:
- Graph integrity verification
- Functional testing with scenario graphs
- Cross-reference validation
- External review sign-offs

See `IMPLEMENTATION_CHECKLIST.md` for detailed gates.

## Questions and Support

- **Technical specifications**: See `specs/v4.1-RC/blueprint.json` and `generation_rules.md`
- **Version history**: See `CHANGELOG`
- **Component evolution**: See `VERSION_MATRIX`
- **Implementation timeline**: See `ROADMAP.md`
- **Non-technical overview**: See `Visual_Summary.md`

## License & Attribution

LFAS Protocol v4.1-RC - Authoritative specification, version-locked, audit-ready.  
See CHANGELOG for full attribution and evolution history.
