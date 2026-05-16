# Dependencies

## Upstream

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `b1502373532ca1b782aafd451ecb98dfacd067b8` | Framework objects (`HG-*`) from `docs/framework-core/`; PFK operational substrate from `proof_fabric_kernel/` |

## Cited objects

### Framework-grade (HG-*)

| Identifier | Role | Notes |
|---|---|---|
| `HG-FND-*` | Foundational vocabulary | typing for lawful-morphology doctrine, polarization, singular-germ regime decomposition |
| `HG-EX-001` | Catalan / mu_2 fixture | replaces self-anchored Catalan / mu_2 work in `ledgers/catalan_mu2/` and `specs/catalan-mu2-reference-implementation.md` |
| `HG-MTH-005` | Universal Bridge formal specification | parent / general bridge axiom; does not transfer proofs |
| `HG-MTH-008` | Universal Bridge: P vs NP / complexity domain extension | canonical NP bridge spec; np-program is the primary consumer |

### PFK operational substrate (canonical IDs)

| Identifier | Role | np-program use |
|---|---|---|
| `PFK-OP-001` | Event ingestion family | required for any future receipt emission |
| `PFK-OP-002` | pi(x) prime-counting | available for any density-related calibration |
| `PFK-OP-005` | Li(x) logarithmic integral | available for any mean-field calibration |
| `PFK-OP-010` | Phase-map operator family | available for proof-character generating-function phase analysis |
| `PFK-OP-020` | Null-model operator family | required for any descriptive-grade empirical claim |
| `PFK-OP-030` | Calibration operator family | required for numerical-baseline checks |
| `PFK-OP-031` | log-phase embedding | available for proof-character generating-function singular-germ work |
| `PFK-OP-032` | mean resultant length R | available for phase-statistic computation |
| `PFK-OP-040` | Catalan / mu_2 fixture operator | load-bearing for the Catalan p=2 toy protocol |
| `PFK-OP-050` | PrimeStatsProtocol operator family | required for descriptive-grade empirical claims |
| `PFK-OP-051..055` | N1/N2/S1/S2/S3 granular operators | required for full protocol compliance |

### PFK schemas

| Identifier | Canonical path | np-program use |
|---|---|---|
| `PFK-SCHEMA-001` | `proof_fabric_kernel/schemas/claim_ledger_row.schema.json` | claim-ledger row schema |
| `PFK-SCHEMA-002` | `proof_fabric_kernel/schemas/event_ir.schema.json` | Event-IR receipts |
| `PFK-SCHEMA-003` | `proof_fabric_kernel/schemas/proof_artifact.schema.json` | proof-step envelopes |
| `PFK-SCHEMA-004` | `proof_fabric_kernel/schemas/calibration_bundle.schema.json` | numerical-baseline checks |

### PFK anti-seed

| Identifier | Applies to np-program because |
|---|---|
| `A-PFK-OP-001` | operator invocation is not evidence; Catalan / mu_2 numerical recomputation is not P-vs-NP progress |
| `A-PFK-PROTOCOL-001` | null-test passage is not theorem-grade |
| `A-PFK-PROTOCOL-002` | window-shopping prevention |
| `A-PFK-SCHEMA-001` | schema validity is not content validity |
| `A-PFK-SCHEMA-002` | schema-version drift; this pin is not floating |
| `A-PFK-VAL-001` | validator green status is not audit completion |

### Framework anti-seed

| Identifier | Applies to np-program because |
|---|---|
| `A-HG-MTH-001` | Universal Bridge does not transfer proofs |
| `A-HG-MTH-002` | Catalan / mu_2 fixture is not Clay progress |
| `A-HG-MTH-003` | fixture-grade and theorem-grade citations must not be mixed |
| `A-HG-MTH-005` | triple barrier diagnosis is not a circumvention recipe |

## Citation form

```text
[HG-MTH-005 @ b1502373532ca1b782aafd451ecb98dfacd067b8]
[HG-MTH-008 @ b1502373532ca1b782aafd451ecb98dfacd067b8]
[PFK-OP-040 @ b1502373532ca1b782aafd451ecb98dfacd067b8]
[PFK-SCHEMA-001 @ b1502373532ca1b782aafd451ecb98dfacd067b8]
[A-HG-MTH-005 @ b1502373532ca1b782aafd451ecb98dfacd067b8]
[A-PFK-OP-001 @ b1502373532ca1b782aafd451ecb98dfacd067b8]
```

The commit SHA is the merged Heller-Godel HG-MTH-008 commit. Pinning is required; floating `main` references are forbidden per `A-PFK-SCHEMA-002`.

## Forbidden edges

- `np-program` -> any other Clay-program repo (no horizontal dependencies)
- `np-program` -> Heller-Godel-other-than-pinned-commit (no floating references)
- `np-program` -> automorphic / number-theoretic methodology from RH or Hodge programs except through the Universal Bridge method-grade analogy (`HG-MTH-005`, `HG-MTH-008`)
- `np-program` -> proof-character generating-function results as if they were complexity-theoretic results

## Scope discipline (unchanged by this pin advance)

Permitted:

- measuring proof and certificate morphologies;
- separating verifier cost from generator cost;
- defining basis-relative generating functions;
- building tranche-conditioned empirical registries;
- treating singular germs as the organizing object for the four-regime decomposition inside declared scope;
- implementing falsifiable toy protocols such as the Catalan `p = 2` monodromy test.

Forbidden:

- claiming P vs NP movement without a formal separation or algorithm;
- claiming agentic search bypasses complexity barriers;
- claiming full canonicity of the `SO(3)` gate target before the gate-minimality theorem is proved;
- comparing proof lengths across bases without a translation cost;
- reporting empirical solver performance without input distribution and tranche;
- treating cryptographic hardness as metaphysical;
- treating convention-dependent Stokes constants as intrinsic outside a committed normalization;
- extending the Milnor-fiber argument beyond algebraic isolated singularities without declaring an extension theory;
- claiming any lane circumvents relativization, natural-proofs, or algebrization by citing `HG-MTH-008`.

Clay proximity remains 0-5%.

## What this pin advance does not do

- Does not change the 10-lane structure.
- Does not change the Q2/Q4/Q6 gate schedule.
- Does not change the np-program's own barrier registry.
- Does not promote any claim grade.
- Does not constitute progress on P vs NP, proof complexity, GCT, or meta-complexity.
- Does not emit receipts or alter apparatus.

## Schema source

PFK schemas live canonically at `SocioProphet/Heller-Godel/proof_fabric_kernel/schemas/` as of the pinned commit. This repository consumes schemas from `HELLER_GODEL_ROOT/proof_fabric_kernel/schemas/` in CI where needed.

## Schema-version pinning policy

Per `A-PFK-SCHEMA-002`, this pin is not floating. Re-pinning across a major schema version triggers re-validating all existing receipts and emissions against the new schemas.
