# LFAS Component Continuity Matrix (Corrected v2.1 → v4.1-RC)

**Purpose:** Trace which protocol components persisted, evolved, or were newly introduced across all versions. Confirms that the Core Loop and Five Pillars have never changed.

---

## Legend

- 🟩 **Implemented** — Feature is fully present and active in this version  
- 🟨 **Partial** — Feature is present but implicit, conditional, or incomplete  
- 🟧 **Reconstructed** — Feature inferred from internal references (v3.8 only; not directly documented)  
- ⬜ **Absent** — Feature not yet introduced in this version  

---

## Component Evolution Matrix (Corrected)

| Component / Feature | v2.1 | v3.4 | v3.5 | v3.6 | v3.8* | v4.0 | v4.1-RC |
|---|---|---|---|---|---|---|---|
| **Core Loop (L→R→W→A→Ack)** | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Five Pillars (procedural)** | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Core Guarantee** | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Breach Reset Protocol** | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Failure Modes (FM#)** | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Cultural Intent Layer (CIL)** | 🟨 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Transparency Tiers (TTS)** | ⬜ | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **High-Stakes Mode (HSM)** | ⬜ | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Defensive Architecture (11 locks)** | ⬜ | 🟨 | 🟨 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Softening Layer / Norm. Kernel** | ⬜ | 🟨 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| **Verification Requirements (VR)** | ⬜ | ⬜ | 🟨 | 🟩 | 🟧 | 🟩 | 🟩 |
| **Oversight Ledger / Logging** | ⬜ | ⬜ | ⬜ | 🟩 | 🟧 | 🟩 | 🟩 |
| **Meta-State Layer (MSL)** | ⬜ | ⬜ | ⬜ | ⬜ | 🟧 | 🟩 | 🟩 |
| **Detectors D1–D7 (conceptual → executable)** | ⬜ | ⬜ | ⬜ | ⬜ | 🟧 | 🟩 | 🟩 |
| **Detector D8 (Notability)** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 🟩 |
| **Normalization Balancing Layer (NBL)** | ⬜ | ⬜ | ⬜ | 🟨 | ⬜ | 🟩 | 🟩 |
| **Cost-Control & Fidelity Layer (CCFL)** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 🟩 | 🟩 |
| **L42 Grounding Evidence Node (GEN)** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 🟩 |
| **V9 State-Proof Metadata** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 🟩 |
| **NCWA / SLTP Rules** | ⬜ | ⬜ | 🟨 | 🟩 | 🟧 | 🟩 | 🟩 |
| **JSON Knowledge Graph** | ⬜ | ⬜ | ⬜ | ⬜ | 🟧 | 🟩 | 🟩 |
| **Generation Rules** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | 🟩 |

---

\* v3.8 = inferred / internal bridge (non-released)
