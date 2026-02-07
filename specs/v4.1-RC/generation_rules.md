# Generation Rules

## Phase 0: Meta-Listen (Asker Profiling)

**Purpose:** Before analyzing the question content, profile the asker to determine the optimal response structure.

### The Universal Meta-Rule
**Never answer a question until you have profiled the Asker.**

### 5W1H on the Question Itself

Before applying detectors to the user's *content*, apply 5W1H to the user's *context*:

| Dimension | Questions to Ask |
|-----------|------------------|
| **WHO** | Who is asking? (Role: Regulator, Developer, Customer, Executive, Researcher) |
| **WHY** | Why are they asking? (Intent: Blame assignment, bug fix, cost savings, trust restoration, understanding) |
| **WHERE** | Where will the answer go? (Destination: Courtroom, GitHub issue, Email, Dashboard, Report) |
| **WHEN** | When do they need it? (Urgency: Crisis/Now vs Strategy/Later) |
| **WHAT** | What are they really looking for? (Outcome: Peace of mind, code patch, liability proof, safety assurance) |
| **HOW** | How do they process info? (Format: Legalese, Python code, bullet points, diagrams, narrative) |

### Dominant W Selection

Based on the profile, identify the **Dominant W** — the dimension that should lead the response:

| User Profile | Dominant W | Response Order Example |
|--------------|------------|------------------------|
| **Regulator/Legal** | WHO | Start with attribution → Why it happened → How to prove it |
| **Developer/Engineer** | HOW | Start with mechanics → Where is the log → What is the fix |
| **CEO/Executive** | WHAT | Start with impact → When is it fixed → Who is on it |
| **Customer/End-User** | WHAT | Start with safety assurance → Why it matters → What's next |
| **Researcher/Analyst** | WHY | Start with root cause → How it works → What are implications |

### Example: "The AI Crashed" (Same Question, Three Different Askers)

**Regulator asks:**
- Meta-Listen Profile: WHO=Enforcer, WHY=Liability, WHERE=Court, Dominant W=WHO
- Response Order: **WHO** (attribution) → **WHY** (cause) → **HOW** (proof)
- Output: "The System Controller (Human) authorized the action. Safety Gate blocked it. No consumer harm occurred."

**Engineer asks:**
- Meta-Listen Profile: WHO=Builder, WHY=Repair, WHERE=Jira, Dominant W=HOW
- Response Order: **HOW** (mechanics) → **WHERE** (logs) → **WHAT** (fix)
- Output: "JSON parser failed at Line 42 due to null value in 'User Emotion' field. See logs at /var/log/system.log."

**Customer asks:**
- Meta-Listen Profile: WHO=User, WHY=Trust/Fear, WHERE=Email, Dominant W=WHAT
- Response Order: **WHAT** (impact) → **WHY** (reason) → **HOW** (resolution)
- Output: "Your money is safe. Protective system paused transaction to ensure security. You can retry now."

### Integration with LISTEN Phase

1. **Meta-Listen fires FIRST** (before D1-D8)
2. **Output:** Asker profile + Dominant W
3. **Input to REFLECT:** Response structure template based on Dominant W
4. **Result:** Same facts, optimal ordering for the specific asker

### Detector Integration

| Detector | Feeds Meta-Listen | Influenced by Meta-Listen |
|----------|-------------------|---------------------------|
| **D2 (Vulnerability)** | Detects emotional state → Informs WHY dimension | Meta-Listen adjusts tone for vulnerable users |
| **D8 (Notability)** | Context significance → Informs WHEN dimension | Meta-Listen adjusts urgency framing |
| **D3 (Crisis)** | Emergency signals → Triggers immediate Dominant W=WHAT | Meta-Listen forces impact-first response |

### LFAS-Compliant Implementation

- **LISTEN Phase Extension:** Meta-Listen runs as first sub-phase
- **No ACT until WAIT:** Asker profiling doesn't bypass authorization gates
- **Transparent:** System states detected profile in REFLECT phase
- **Auditable:** Logs Dominant W selection in V9 proof metadata

---

## Constraint Proof
- Each scenario Knowledge Graph (KG) logs both copied and missing edges from the Master Graph. The structure should include a `constraint_proof` entry with `copied_edges` and reasons for any missing edges.

## Fail-Closed Rule for D7_EVIDENCE_PRESENCE_CHECKER
- Scenario KGs must block actions (WAIT/VERIFY) if evidence is missing. This ensures that only valid scenarios proceed, thereby maintaining the integrity of the process.

## State Transition Proof
- It is necessary to document permitted phase transitions. Implement a metadata field `STATE_TRANSITION_PROOF` which outlines the `current_phase`, `next_phase`, and the conditions required for the transition to occur.

## Provenance Fields
- Nodes and edges must include `provenance_ref` for traceability. This field should link back to master graph IDs, transcripts, or files, ensuring stakeholders can easily track the origins of each element.

## New Discovery Rule
- Introduce `NEW_DISCOVERY_*` nodes to manage unknown behaviors. These nodes must be marked for review and include safer gating mechanisms to mitigate risks associated with unforeseen circumstances.

## Trajectory Overlay
- As an optional structure for repeated fatigue scenarios, utilize nodes such as `AI_COMMITMENT_LEVEL` and `USER_LOAD_LEVEL`. This framework can help assess the impact over time and facilitate better decision-making based on historical data.

## Schema Examples Revision
- Revise existing schema examples to encompass new fields including but not limited to `schema_locked`, `provenance_ref`, `constraint_proof`, and `fail_closed`, ensuring compliance verifiability and enhancing data integrity.

This document outlines critical rules governing the scenario generation processes within the LFAS Protocol, aimed at maintaining rigorous standards and ensuring clarity in execution.