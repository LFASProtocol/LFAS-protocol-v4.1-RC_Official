# LFAS Interaction Autopsy Module - Usage Guide

**Version:** 1.0  
**Audience:** Researchers, AI Safety Engineers, Conversation Designers  
**Prerequisites:** Familiarity with LFAS Protocol v4.1-RC basics

---

## Quick Start

### 1. Understand the Purpose

The Interaction Autopsy Module helps you answer:

- **"What went wrong?"** → Identify specific failure modes
- **"Why did it go wrong?"** → Trace user signals → AI biases → failures
- **"How could it be prevented?"** → LFAS counterfactual paths
- **"Is this a new pattern?"** → Discovery mode for unknown failures

### 2. Required Knowledge (Layer 1 - Clean Reference Data)

Before analyzing any transcript, familiarize yourself with:

1. **Core Files:**
   - `failure_modes.json` - Dictionary of known failures with dual labels
   - `detectors.json` - 8 detectors (D1-D8) and interaction causality chains
   - `schemas/audit_artifact.json` - Output format specification

2. **LFAS Protocol Basics:**
   - **5 Phases:** LISTEN → REFLECT → WAIT → ACT → ACKNOWLEDGE
   - **8 Detectors:** D1-D8 (see detectors.json)
   - **Key Gates:** L2 (Input Analysis), L3 (Understanding Verification), L37 (Scope Confirmation), L41 (Deliverable Check)

3. **Critical Concepts:**
   - **Dual-Labeling:** Technical labels (engineering) + Critical labels (user-facing)
   - **Interaction Causality:** User Signal → AI Bias → Failure Mode
   - **Counterfactual Path:** What LFAS would have done instead

---

## Step-by-Step Workflow

### Step 1: Prepare Your Transcript

**Input Formats Accepted:**

**Format A: Plain Text**

```
User: I need help with my project
AI: Sure! Let me give you a comprehensive plan...
User: ok
AI: [continues with detailed plan]
User: Wait, that's too much detail
```

**Format B: Structured JSON**

```json
{
  "turns": [
    {"turn": 1, "role": "user", "message": "I need help with my project"},
    {"turn": 1, "role": "ai", "message": "Sure! Let me give you..."}
  ]
}
```

**Format C: Chat Export**

- Most chat platforms allow export - just paste the content

### Step 2: Run the Analysis

**Using the Methodology (Manual Analysis):**

1. Load `autopsy_analyzer.md`
2. Follow the 5 phases:
   - **LISTEN:** Structure the transcript, assign turn IDs
   - **REFLECT:** Fire detectors for each turn
   - **WAIT:** Trace objectives, detect drift
   - **ACT:** Build counterfactual paths
   - **ACKNOWLEDGE:** Generate audit artifact

**Using Automation (If Available):**

```bash
# Future: Automated analyzer tool
./analyze_transcript.py --input transcript.txt --output audit.json
```

### Step 3: Interpret the Results

Your audit artifact will contain:

1. **Turn-by-Turn Analysis:**
   - Which detectors fired
   - Which failures occurred
   - What LFAS would have done instead

2. **Session Summary:**
   - LFAS compliance score (0-1, where 1 = perfect)
   - Primary failure mode
   - Recommendations for users, AI, and protocol

3. **Knowledge Graph:**
   - Visual representation of failure paths
   - Critical interaction chains

---

## Common Use Cases

### Use Case 1: Post-Mortem Analysis

**Scenario:** You had a frustrating conversation with an AI assistant and want to understand what went wrong.

**Process:**

1. Export your conversation
2. Run autopsy analysis
3. Look for:
   - Which failure modes occurred
   - Where LFAS gates would have helped
   - What you could do differently as a user

**Example Output:**

```
Primary Failure: FM#34 (The Silence-Trap)
Trigger: Your "ok" in Turn 3 was interpreted as consent
LFAS Fix: AI should have confirmed scope before proceeding
User Tip: Next time, use "Yes, that's exactly what I need" instead of "ok"
```

### Use Case 2: AI System Validation

**Scenario:** You're testing whether your AI system follows LFAS protocol.

**Process:**

1. Create test scenarios with known edge cases
2. Run conversations through your system
3. Autopsy the results
4. Measure LFAS compliance score
5. Identify gate enforcement gaps

**Example:**

```
Test: User gives vague request
Expected: AI asks clarifying questions (L2 gate)
Actual: AI assumed details (FM#29 violation)
Compliance Score: 0.2
Action: Strengthen L2_INPUT_ANALYSIS_GATE
```

### Use Case 3: Research on Interaction Dynamics

**Scenario:** You're studying how user fatigue affects AI conversations.

**Process:**

1. Collect transcripts where users showed fatigue signs
2. Run autopsy on all transcripts
3. Aggregate detector activations:
   - How often did D2 (Vulnerability Detector) fire?
   - What failures correlated with short replies?
4. Publish findings with anonymized data

**Research Questions:**

- Does reply length correlate with failure modes?
- What percentage of "ok" replies led to consent mismatch?
- How effective is D2 at detecting user fatigue?

### Use Case 4: Training Data Generation

**Scenario:** You want to train an AI to follow LFAS protocol.

**Process:**

1. Collect diverse conversation transcripts
2. Run autopsy on all
3. Extract counterfactual LFAS paths
4. Use as training examples:
   - **Negative Examples:** Actual AI responses that failed
   - **Positive Examples:** LFAS counterfactual responses

**Training Pair:**

```
Context: User said "ok"
Bad Response: [Proceeds with assumption]
Good Response: "To confirm - you want me to proceed with [action]? Please reply YES."
Label: FM#34 prevention via L37 gate
```

---

## Understanding Detector Activations

### Detector Quick Reference

| Detector | Fires When | Example |
|----------|-----------|---------|
| **D1** | Uncertainty masked | AI says "definitely" without probability |
| **D2** | User vulnerability | Short replies, fatigue signs |
| **D3** | Crisis/urgency | "Urgent", "emergency" language |
| **D4** | Needs escalation | Request exceeds AI capability |
| **D5** | Risk threshold | Aggregate from D2+D3 |
| **D6** | Contradiction | Objective drifted from stated goal |
| **D7** | Missing evidence | AI assumes instead of asking |
| **D8** | Unusual request | Rare or specific constraint |

### Reading Detector Output

Example from audit artifact:

```json
{
  "detector_triggered": "D2_VULNERABILITY_DETECTOR",
  "failure_mode_id": "FM#34",
  "lfas_violation": "L37_SCOPE_CONFIRMATION_GATE_BYPASSED"
}
```

**Interpretation:**

- **D2 fired** because user showed fatigue (short reply)
- This led to **FM#34** (The Silence-Trap) where silence was treated as consent
- **L37 gate** should have prevented this by requiring explicit confirmation

---

## Understanding Failure Modes

### The 8 Core Failure Modes

**From LFAS v4.1-RC Protocol:**

- **FM#29** - Autopilot Prioritization ("The Assumption Express")
- **FM#34** - Signal Consent Mismatch ("The Silence-Trap") ⚠️ High Severity
- **FM#35** - Premature Closure ("The Polite Walk-Away")
- **FM#42** - Inference Without Grounding ("Ice Cream Shop Reflex") ⚠️ Critical

**New Discoveries:**

- **FM#NEW_01** - Objective Drift ("Helper-Mode Reversion")
- **FM#NEW_02** - State Proof Failure ("Hallucinated Compliance") ⚠️ Critical
- **FM#NEW_03** - Uncertainty Dampening ("Defensive Hedging")
- **FM#NEW_04** - Instruction Stripping ("Normalization Bias")

### Severity Levels

- **Low:** Minor inefficiency, easy to recover
- **Medium:** Noticeable problem, requires correction
- **High:** Significant issue, user frustration
- **Critical:** Potential harm, trust violation, safety concern

---

## Interpreting Counterfactual Paths

Every failure includes a counterfactual showing **what LFAS would have done**.

### Example Counterfactual

```json
{
  "actual_action": "AI proceeded with assumption about X",
  "lfas_action": "AI should have asked 'Did you mean X or Y?'",
  "gate_that_would_prevent": "L2_INPUT_ANALYSIS_GATE",
  "cost_of_deviation": "3 wasted turns, user frustration",
  "cost_of_lfas_compliance": "1 clarification turn"
}
```

### Cost-Benefit Analysis

**Cost of Deviation:**

- Wasted turns (inefficiency)
- User frustration (trust erosion)
- Incorrect output (safety concern)
- Scope creep (resource waste)

**Cost of LFAS Compliance:**

- Usually 1-2 extra turns for verification
- Slightly longer conversation
- **BUT:** Higher accuracy, user satisfaction, trust

**Key Insight:** LFAS trades minimal upfront cost (verification) for major savings (preventing failures)

---

## Using Recommendations

Each autopsy generates three types of recommendations:

### For Users (Interaction Hygiene)

**Bad Habits → Better Habits:**

| Don't Say | Say Instead | Why |
|-----------|-------------|-----|
| "ok" | "Yes, that's correct" | Explicit confirmation |
| [silence] | "I need time to think" | Absence is not consent |
| [long emotional rant] | "First, confirm you understood my main point" | Reduce misinterpretation |
| "urgent!" | "This is urgent - please confirm understanding first" | Urgency should increase verification |

### For AI Systems (Bias Recalibration)

**Pattern → Fix:**

| Bias | Correction |
|------|------------|
| Silence Reinforcement | Treat short replies as possible fatigue, not consent |
| Autopilot Prioritization | Ask clarifying questions instead of assuming |
| Ice Cream Shop Reflex | Urgency activates High-Stakes Mode, increases verification |
| Implicit Reward Loop | Praise ≠ correctness; verify objective hasn't drifted |

### For Protocol (LFAS Enhancement)

**Discovery → Integration:**

New failure patterns found in autopsies should be:

1. Documented with dual labels
2. Added to `failure_modes.json`
3. Mapped to detector logic
4. Incorporated into next LFAS version

---

## Advanced: Knowledge Graph Construction

Each autopsy generates a scenario-specific KG following LFAS schema.

### KG Components

**Nodes:**

- User requests
- AI responses
- Detector activations
- Failure modes
- Gate violations

**Edges:**

- `triggered` - User signal → Detector
- `detected` - Detector → Failure
- `violated` - Failure → Gate
- `prevented_by` - Failure → Counterfactual LFAS path

### Visualizing KGs

Example critical path:

```
USER_REQUEST_T3 
  → (vague language) → 
D7_EVIDENCE_CHECKER_FIRED 
  → (detected) → 
FM#29_ASSUMPTION_EXPRESS 
  → (violated) → 
L2_INPUT_GATE_BYPASSED

COUNTERFACTUAL:
L2_INPUT_GATE 
  → (should have enforced) → 
CLARIFYING_QUESTION 
  → (prevented) → 
FM#29
```

---

## Quality Assurance

### Before Finalizing an Autopsy

✅ **Checklist:**

- [ ] All turns have turn_id and are analyzed
- [ ] Detector activations justified with evidence from transcript
- [ ] Each failure has clear failure_mode_id (FM#XX or FM#NEW_XX)
- [ ] Every failure includes counterfactual LFAS path
- [ ] Objective trace tracked throughout (correct vs. active)
- [ ] LFAS compliance score calculated: `(turns_without_failure / total_turns)`
- [ ] Recommendations are specific and actionable
- [ ] JSON validates against `schemas/audit_artifact.json`
- [ ] New discoveries have dual labels and are documented
- [ ] Knowledge graph nodes and edges are complete

### Validation

**Test your audit artifact:**

```bash
# Validate JSON schema
jsonschema -i your_audit.json schemas/audit_artifact.json
```

**Human Review:**

- Have another person read the autopsy
- Can they understand what went wrong?
- Are recommendations clear and actionable?

---

## Frequently Asked Questions

### Q: How long does an autopsy take?

**A:**

- **Simple (5 turns):** 10-15 minutes
- **Medium (15 turns):** 30-45 minutes  
- **Complex (30+ turns):** 1-2 hours
- **Automated (future):** Seconds to minutes

### Q: What if I find a failure not in the catalog?

**A:** Flag it as `[NEW DISCOVERY]`, create dual labels, document detection criteria, and log for protocol review. See `autopsy_analyzer.md` section on "Handling New Discoveries".

### Q: Can I use this on conversations with non-LFAS AI systems?

**A:** Yes! The autopsy shows where LFAS would have prevented failures, even if the original system didn't use LFAS. This helps validate LFAS effectiveness.

### Q: How do I know which detector should fire?

**A:** Match user signals to detector descriptions in `detectors.json`. Multiple detectors can fire on the same turn.

### Q: What's a good LFAS compliance score?

**A:**

- **0.0-0.3:** Major problems, multiple gate failures
- **0.4-0.6:** Moderate issues, some gates working
- **0.7-0.8:** Good compliance, minor violations
- **0.9-1.0:** Excellent, LFAS protocol well-enforced

### Q: Should every "ok" be flagged as FM#34?

**A:** No. Context matters. If "ok" follows explicit scope confirmation request ("Do you want me to proceed? Reply YES"), it's safer. If "ok" is unprompted or vague, then D2 should fire and check for consent mismatch.

---

## Example Workflow: Complete Autopsy

**Input:** 4-turn conversation where user got frustrated

**Step 1: LISTEN - Structure Data**

```
Turn 1: User asks vague question
Turn 2: AI provides detailed answer, user says "yes"
Turn 3: User says "ok"  
Turn 4: User: "Wait, that's not what I wanted"
```

**Step 2: REFLECT - Fire Detectors**

```
Turn 1: D7 fires (vague question, no clarification asked)
Turn 2: D6 fires (objective may have drifted, "yes" is vague)
Turn 3: D2 fires (short reply "ok" = fatigue indicator)
```

**Step 3: WAIT - Trace Objectives**

```
Correct objective: User wanted simple overview
Active objective: AI providing detailed implementation
Drift: Yes, started Turn 2, compounded Turn 3
```

**Step 4: ACT - Build Counterfactuals**

```
Turn 1: L2 gate should have triggered clarification
Turn 2: L3 gate should have verified objective
Turn 3: L37 gate should have required explicit confirmation
```

**Step 5: ACKNOWLEDGE - Generate Artifact**

```json
{
  "session_id": "example_001",
  "total_failures": 3,
  "lfas_compliance_score": 0.25,
  "primary_failure_mode": "FM#34 - The Silence-Trap",
  "recommendations": {...}
}
```

---

## Integration with Research

### Publishing Findings

When using autopsy data in research:

1. **Anonymize:** Remove identifying information
2. **Aggregate:** Report statistics across multiple sessions
3. **Cite Protocol:** Reference LFAS v4.1-RC specification
4. **Share Artifacts:** Include audit JSONs as supplementary material
5. **Contribute Back:** Submit new discoveries to LFAS protocol team

### Metrics for Research

Useful aggregate metrics:

- **Failure Mode Distribution:** Which FM# most common?
- **Detector Sensitivity:** How often does each detector fire?
- **Compliance Scores:** Average across sessions, by domain
- **Cost Analysis:** Aggregate cost_of_deviation vs. cost_of_lfas_compliance

---

## Next Steps

1. **Try it:** Analyze one of your own AI conversations
2. **Study examples:** Review `examples/example_silence_trap_analysis.json`
3. **Learn methodology:** Read `autopsy_analyzer.md` in full
4. **Contribute:** Share new failure discoveries with protocol team
5. **Automate:** Build tools to streamline the process

---

## Support & Resources

- **Core Methodology:** `autopsy_analyzer.md`
- **Failure Catalog:** `failure_modes.json`
- **Detector Specs:** `detectors.json`
- **Schema:** `schemas/audit_artifact.json`
- **Examples:** `examples/` directory
- **LFAS Protocol:** See main repository `specs/v4.1-RC/`

---

## License

Part of **LFAS Protocol v4.1-RC**  
Interaction Autopsy Module v1.0  
See main repository for full license and attribution
