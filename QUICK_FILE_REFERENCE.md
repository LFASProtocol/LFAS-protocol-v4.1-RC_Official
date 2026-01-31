# Quick File Reference: Which Files to Use from LFAS-protocol-v4

## TL;DR - Fast Decision Tree

```
Is it code (.py, .xml specs, setup.py)?
  └─ NO → Don't copy it

Is it community infrastructure (CODE_OF_CONDUCT, SECURITY, .github/)?
  └─ YES → ✅ Copy it directly

Is it documentation (markdown files)?
  └─ Check: Does it reference v4.0 specifically?
      ├─ NO (version-agnostic) → ✅ Copy or adapt
      └─ YES (v4.0-specific) → ⚠️ Use as reference only

Is it a build/package file (Makefile, pyproject.toml)?
  └─ YES → ❌ Don't copy it
```

---

## ✅ COPY THESE (Recommended)

### Community Files
```
CODE_OF_CONDUCT.md              → Establish community standards
CONTRIBUTING.md                 → Guide contributors (adapt to spec repo)
SECURITY.md                     → Security policy & vulnerability reporting
```

### GitHub Infrastructure
```
.github/ISSUE_TEMPLATE/         → Bug reports, feature requests, security
.github/PULL_REQUEST_TEMPLATE/  → PR template
```

### Documentation Tools
```
.editorconfig                   → Editor settings
.gitignore                      → Git ignore rules (review first)
.markdownlint.json              → Markdown linting
```

---

## ⚠️ ADAPT THESE (Modify Before Using)

### Documentation (Remove v4.0-specific content)
```
FAQ.md                → FAQ_v4.1-RC.md (rewrite for v4.1-RC context)
README.md             → Adapt overview for specification repo
IMPLEMENTATION.md     → Create IMPLEMENTATION_GUIDE_v4.1-RC.md
```

### Project Files (Update version references)
```
PROJECT_STATUS.md     → Adapt for v4.1-RC milestones
REPOSITORY-STRUCTURE-GUIDE.md → Update for spec repo structure
```

---

## 📖 REFERENCE ONLY (Don't Copy)

### Historical Context
```
CHANGELOG.md          → Read for v4.0 context (keep YOUR changelog as primary)
Evolution/            → Understand evolution from v4.0 perspective
history of the project/ → Project history reference
```

### Research & Analysis
```
research/             → Research evidence and studies (useful reference)
ANALYSIS-IMPLEMENTATION-OPTIONS.md → Implementation considerations
```

### Documentation Examples
```
documentation/        → Structure and organization ideas
docs/                 → Documentation site structure
```

---

## ❌ DO NOT COPY

### Code Files
```
src/                  → Python implementation (v4.0, incompatible)
lfas/                 → Package code (v4.0)
lfas_protocol/        → Alternative package (v4.0)
tests/                → Test suite for v4.0 code
tests_v41/            → Outdated tests
examples/*.py         → Python examples (v4.0)
demo.py               → v4.0 demo
*.py                  → All Python files
```

### Build & Package Files
```
setup.py              → Python package setup
pyproject.toml        → Python project config
MANIFEST.in           → Package manifest
Makefile              → Build automation for v4.0
requirements*.txt     → Python dependencies
```

### Protocol Specifications
```
protocol/lfas-v4-specification.xml           → v4.0 XML (you have v4.1-RC JSON)
protocol/lfas-v4-specification-enhanced.xml  → v4.0 enhanced XML
```

### Development Tools (Code-specific)
```
.pre-commit-config.yaml → Pre-commit hooks for Python code
```

---

## File Compatibility at a Glance

| File Type | Copy? | Reason |
|-----------|-------|--------|
| `.md` (generic) | ✅ YES | Version-agnostic documentation |
| `.md` (v4.0-specific) | ⚠️ ADAPT | Needs version update |
| `.py` | ❌ NO | v4.0 code, incompatible |
| `.xml` (specs) | ❌ NO | v4.0 XML → v4.1-RC uses JSON |
| `.json` (config) | ⚠️ REVIEW | Check compatibility |
| `.github/` | ✅ YES | GitHub infrastructure |
| `CODE_OF_CONDUCT` | ✅ YES | Community standards |
| `SECURITY` | ✅ YES | Security policy |
| `LICENSE` | ⚠️ REVIEW | Check license alignment |
| `requirements.txt` | ❌ NO | Python dependencies |
| `setup.py` | ❌ NO | Package setup |

---

## Common Questions

**Q: Can I copy the Python code to implement v4.1-RC?**  
A: ❌ No. The v4.0 code uses XML specifications. You need to build new code based on `blueprint.json`.

**Q: Should I copy the CHANGELOG.md?**  
A: ⚠️ No, keep yours. Your CHANGELOG has complete history (v2.1 → v4.1-RC). Use theirs for additional v4.0 context only.

**Q: What about the test files?**  
A: ❌ No. They test v4.0 Python code. You'll need to create new tests for v4.1-RC implementations.

**Q: Can I use the documentation structure?**  
A: ✅ Yes. Use their documentation organization as inspiration, but create v4.1-RC-specific content.

**Q: Is the LICENSE compatible?**  
A: ⚠️ Review it. Both repos should have aligned licenses, but verify before copying.

**Q: What about the XML protocol specifications?**  
A: ❌ No. v4.1-RC uses JSON Knowledge Graph (`blueprint.json`), not XML.

**Q: Can I copy the GitHub issue templates?**  
A: ✅ Yes. These are version-agnostic and improve community engagement.

**Q: Should I copy the .gitignore?**  
A: ⚠️ Review first. The v4.0 .gitignore is for Python projects. Adapt for your needs.

---

## Priority Actions

### **High Priority: Add These Now**
1. `CODE_OF_CONDUCT.md` - Establish community standards
2. `SECURITY.md` - Enable security vulnerability reporting
3. `.github/ISSUE_TEMPLATE/` - Better issue tracking

### **Medium Priority: Consider These**
1. `CONTRIBUTING.md` (adapted) - Guide contributors
2. `FAQ.md` (rewritten for v4.1-RC) - Answer common questions
3. `.gitignore` (reviewed) - Better git management

### **Low Priority: Optional**
1. `PROJECT_STATUS.md` (adapted) - Track project status
2. `IMPLEMENTATION.md` (rewritten) - Future implementation guide
3. Research documents (reference) - Additional context

---

## One-Line Decisions

| File | Decision | Action |
|------|----------|--------|
| `CODE_OF_CONDUCT.md` | ✅ COPY | Community standards |
| `SECURITY.md` | ✅ COPY | Security policy |
| `.github/ISSUE_TEMPLATE/` | ✅ COPY | Issue templates |
| `CONTRIBUTING.md` | ⚠️ ADAPT | Update for spec repo |
| `FAQ.md` | ⚠️ ADAPT | Rewrite for v4.1-RC |
| `src/*.py` | ❌ SKIP | v4.0 code |
| `protocol/*.xml` | ❌ SKIP | v4.0 specs |
| `setup.py` | ❌ SKIP | Package setup |
| `tests/` | ❌ SKIP | v4.0 tests |
| `CHANGELOG.md` | 📖 REFERENCE | Keep yours |
| `research/` | 📖 REFERENCE | Context only |

---

## Summary

**Safe to Copy (9 files/folders):**
- CODE_OF_CONDUCT.md
- SECURITY.md
- .github/ISSUE_TEMPLATE/
- .github/PULL_REQUEST_TEMPLATE/
- .editorconfig
- .markdownlint.json
- .gitignore (review first)

**Adapt Before Using (5 files):**
- CONTRIBUTING.md
- FAQ.md
- README.md
- IMPLEMENTATION.md
- PROJECT_STATUS.md

**Reference Only (Don't Copy) (15+ files/folders):**
- CHANGELOG.md (use yours)
- research/
- Evolution/
- documentation/
- docs/

**Never Copy (20+ files/folders):**
- src/
- lfas/
- lfas_protocol/
- tests/
- examples/*.py
- protocol/*.xml
- setup.py, pyproject.toml, requirements.txt
- All .py files

---

**Golden Rule:** When in doubt, **DON'T COPY CODE**. Only copy **documentation** and **community files**.

**Last Updated:** January 31, 2026
