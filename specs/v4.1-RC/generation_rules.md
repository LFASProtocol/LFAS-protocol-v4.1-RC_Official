# Generation Rules

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