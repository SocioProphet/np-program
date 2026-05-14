# A2 Theorem Roadmap

Status: roadmap / theorem-track scoping / not a theorem / not a Clay claim.

Depends on:

```text
docs/conventions/a2-target-split.md
docs/conventions/a2-local-cuberoot-normalization-v0.md
docs/conventions/a2-gate-convention-corrections.md
docs/proofs/c3-cohomological-obstruction.md
docs/proofs/c3-layer1-a2-group-identification.md
docs/proofs/c3-layer2-a2-polarization-candidates.md
docs/proofs/a2-stage2-attestation.md
specs/a2-local-cuberoot-test-vectors.md
```

Related issues:

```text
#20 — A2 Gate Convention: SU2 representation branch vs SU3 ADE branch
#16 — Implement A2 local cube-root Stage-1 harness
```

## 0. Purpose

This roadmap records what the A2 theorem track is trying to specify before any Stage-2 harness implementation is extended.

The sequencing rule is:

```text
roadmap before Stage-2 harness extension
```

A Stage-2 harness should not produce theorem-facing output until the roadmap names the objects whose theorem-context status is being attested.

## 1. Current state

The A2 stack currently has:

```text
1. target split: pure local A2 cube-root is separated from order-3 Fuss-Catalan;
2. local normalization: u^3 = t with C3 / mu3 monodromy;
3. Stage-1 test vectors and harness expectations;
4. Stage-2 attestation scaffold;
5. A2 gate-convention corrections;
6. C-3' cohomological capstone showing A1 obstruction does not automatically inherit into A2/Ak.
```

This is enough for fixture execution and roadmap scoping.

It is not enough for an A2 gate-minimality theorem.

## 2. Roadmap target

The target is not:

```text
show the local cube-root harness passes
```

That is Stage 1.

The roadmap target is:

```text
specify what additional theorem-context facts would make a passing A2 fixture
count as evidence for an A2 gate-minimality statement.
```

The central result of the current review is that this cannot be answered without a convention choice for `V_A^(2)` and its invariant data.

## 3. Attachment question

The C-3' cohomological note makes the attachment question explicit.

For the A1 faithful branch:

```text
SO(3) projective obstruction -> auxiliary Spin(3) realization -> -I on V_A
```

For A2, this does not automatically generalize.

The A2 attachment question is:

```text
Given the A2 source monodromy, active space V_A^(2), invariant data,
transport E_phi^(2), and active monodromy M_A^(2), what attaches the local
mu3 / C3 fixture data to theorem-context active data?
```

This question is in scope for the roadmap as a long-horizon theorem target. It is not a harness-only question.

## 4. Convention fork

Issue #20 records the fork.

### Path alpha: SU2 representation branch

Under path alpha:

```text
carrier remains SU(2) / Spin(3)-controlled
central datum remains Z/2
A2 distinction enters through representation type and Frobenius-Schur behavior
```

Stage-2 target under path alpha:

```text
identify the exact SU(2) representation on V_A^(2), its form type,
and the way the A2 local cube-root / mu3 fixture maps into that representation.
```

Risk:

```text
A2 may not be distinguished at the group level.
```

### Path beta: SU3 ADE branch

Under path beta:

```text
G_aux = SU(3)
V_A^(2) = C^3
zeta = omega I_3
omega = exp(2*pi*i/3)
invariant data = Hermitian form + determinant / volume form
```

Stage-2 target under path beta:

```text
justify C^3 as theorem-context V_A^(2), justify Hermitian-volume
compatibility, and prove the local mu3 fixture is the intended theorem-context
readout rather than only a local model.
```

Risk:

```text
A2 Step 4 is not an A1 projective-obstruction lift. At the simply connected
SU3 carrier level there is no A1-style projective obstruction, so the proof
structure must change.
```

## 5. Stage-2 attestation targets

A future Stage-2 implementation must attest these objects, not merely output numerical residuals.

| Object | Stage-2 question | Status before implementation |
|---|---|---|
| `V_A^(2)` | Is the fixture space `C^3` theorem-context active space, sheet/character readout space, or only local model? | unresolved |
| invariant data | Is the invariant symplectic, orthogonal, Hermitian, Hermitian-volume, doubled symplectic, or adjoint cubic? | unresolved |
| `E_phi^(2)` | Is the map a predeclared transport/encoding map from source data to active data? | scaffolded, not attested |
| `M_phi^(2)` | Is the source monodromy theorem-context monodromy or local cube-root monodromy only? | scaffolded, not attested |
| `M_A^(2)` | Is the active monodromy theorem-context action or fixture action only? | scaffolded, not attested |
| central datum | Is the central datum `Z/2`, `Z/3`, `mu3`, Weyl/S3, or another declared object? | unresolved |
| subgroup elimination | If path beta claims SU3 minimality, what exact subgroup/embedding elimination is used? | unresolved |

The Stage-2 harness may validate these attestations only after the roadmap chooses which branch each object belongs to.

## 6. Stage-2 receipt shape

A future Stage-2 receipt should include fields like:

```yaml
stage: A2-stage2
stage1_receipt_ref: string
roadmap_ref: docs/roadmap/a2-theorem-roadmap.md
convention_issue_ref: issue-20
branch_choice: path_alpha | path_beta | unresolved
V_A_status: committed | open
invariant_status: committed | open
E_phi_status: committed | open
M_phi_status: committed | open
M_A_status: committed | open
central_datum_status: committed | open
subgroup_elimination_status: committed | open
claim_status: fixture_only | theorem_context_partial | theorem_context_ready
stage2_claimed: false | true
nonclaims:
  - no_A2_theorem_claim_unless_theorem_context_ready
  - no_Clay_claim
```

Until the branch choice is committed, `claim_status` must remain `fixture_only` or `theorem_context_partial`.

## 7. Roadmap milestones

### Milestone R1: convention decision

Resolve Issue #20 by choosing one of:

```text
path_alpha
path_beta
explicitly_unresolved_with_A2_remaining_stage1
```

Acceptance criterion:

```text
A repo note states what V_A^(2) means and what invariant data it carries.
```

### Milestone R2: Stage-2 target specification

Patch `docs/proofs/a2-stage2-attestation.md` or add a companion spec to name the exact Stage-2 receipt fields and pass/fail conditions for the chosen branch.

Acceptance criterion:

```text
A Stage-2 implementation can know what it is attesting before it computes.
```

### Milestone R3: Stage-2 implementation

Only after R1 and R2, implement the Stage-2 receipt generator / validator.

Acceptance criterion:

```text
Stage-2 output says whether theorem-context objects are committed or open;
it does not silently promote fixture data.
```

### Milestone R4: theorem sketch

Only after Stage-2 has committed enough theorem-context objects, write the A2 theorem sketch or record why the theorem remains blocked.

Acceptance criterion:

```text
The sketch cites committed Stage-2 attestations and explicitly lists remaining open objects.
```

## 8. Relationship to systems-learning-loops Issue #3

The centroid/readout-basis cipher experiment in `systems-learning-loops` Issue #3 remains independent but related in discipline.

It should not block A2 roadmap work, but it should not drift indefinitely because it is another convention-pinned readout-basis experiment. The same failure mode applies:

```text
fixtures without a declared readout convention become uninterpretable claim material.
```

## 9. Nonclaims

This roadmap does not claim:

```text
- A2 gate minimality;
- correctness of path alpha;
- correctness of path beta;
- that the A2 local cube-root fixture is theorem-facing evidence;
- that Stage-2 is implemented;
- that any A2 theorem is ready to state;
- P = NP;
- P != NP;
- a lower bound;
- any Clay result.
```

It only orders the next work: convention decision and Stage-2 target specification before Stage-2 harness extension.