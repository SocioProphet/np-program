# Five-Layer Falsification Specification

Status: **falsification design / pre-run criteria / no claim promotion**.  
Issue: `#29`.  
Scope: current `np-program` steelman after PR #28.

## 0. Purpose

This document fixes falsification criteria before further proof notes, harness outputs, or attestation receipts are used as evidence.

The goal is not to make the program harder to refute. The goal is to make refutation precise. Each layer below states what would count as failure by observation, by construction, or by scope violation.

A passed fixture, proof note, or attestation cannot be interpreted beyond the layer it belongs to.

## 1. Global claim boundary

This falsification document does not claim:

```text
- P = NP;
- P != NP;
- NP != coNP;
- a Boolean circuit lower bound;
- a proof-system lower bound;
- A2 gate minimality;
- A2 theorem-context naturality;
- I-12 promotion;
- any Clay-prize result.
```

It only records what would refute the current layered steelman.

## 2. Layer map

The current program has five falsifiable layers.

```text
Layer 1: A1 admissible gate-minimality contract
Layer 2: A1 Catalan Stokes convention / harness target
Layer 3: A1 polarization compatibility bottleneck
Layer 4: A2 Candidate-A Stage-1 local cube-root realizability
Layer 5: A2 Stage-2 fixture-only five-object attestation
```

These layers are ordered by dependency but not by promotion. Passing a lower layer does not automatically promote a higher layer.

## 3. Layer 1 — A1 admissible gate-minimality contract

### Claim being tested

For the `A1` / Catalan square-root case, the minimal gate realization is not merely a group capable of displaying a sign. The corrected claim is relative to an admissibility class requiring:

```text
1. spatial-triad action;
2. non-abelian active-set action;
3. compact connected Lie regularity;
4. nontrivial Z/2 loop class;
5. polarization-compatible readout contract.
```

Within that admissibility class, the A1 target is `SO(3)` with the `Spin(3)=SU(2)` lift carrying the half-integer sign.

### Evidence class

```text
theorem-target / proof-note pending
```

The layer is proof-shaped but not promoted until the proof note closes the admissibility conditions without hidden assumptions.

### Refutation by observation / proof result

Layer 1 fails if the proof note cannot show that all five admissibility conditions jointly force the declared minimal gate object.

Concrete failures include:

```text
- the proof uses sign-realization alone;
- the proof excludes U(1) for the wrong reason;
- the proof assumes non-abelian active-set action without defining it;
- the proof silently post-selects the active -1 eigendirection;
- the proof treats polarization compatibility as decorative rather than load-bearing;
- the proof cannot distinguish triad image minimality from arbitrary representation minimality.
```

### Refutation by construction

A counter-construction refutes Layer 1 if it supplies an admissible gate object satisfying all five conditions while being strictly smaller than or not factoring through the declared `SO(3)` / `Spin(3)` structure.

The counter-construction must satisfy the actual admissibility class, not a weakened one. In particular, an abelian sign carrier such as `U(1)` is not a counterexample unless it also satisfies non-abelian active-set action and the polarization-compatible readout contract.

### Refutation by scope violation

Layer 1 fails by scope if the proof depends on a hidden condition not listed in the admissibility class.

Examples:

```text
- importing an undeclared auxiliary group;
- requiring a global theorem-context object while claiming only local A1 data;
- using Lawful Learning geometry beyond the declared spatial-triad condition;
- replacing compact connected Lie regularity with a stronger unstated hypothesis.
```

### Vacuity / under-constraint risk

If the admissibility class is so restrictive that `SO(3)` is effectively inserted by definition, then the theorem is vacuous.

The proof note must therefore show which hypotheses do real work and why each competitor is excluded:

```text
U(1) / SO(2): excluded by non-abelian active-set action.
Disconnected finite sign carriers: excluded by compact connected Lie regularity.
Larger covers or redundant groups: not minimal in the declared faithful triad image.
Post-hoc basis flips: excluded by polarization-compatible predeclaration of E_phi.
```

### Nonclaims

Passing Layer 1 does not prove a circuit lower bound, A2 behavior, an A_n pattern, P vs NP, or Clay progress.

## 4. Layer 2 — A1 Catalan Stokes convention / harness target

### Claim being tested

Under `A1-sauzin-normalization-v0`, with `t = 1 - 4x` and the positive real `t`-ray as canonical wall, the Catalan generating function has:

```text
Stokes multiplier: -1
Catalan additive jump coefficient: 4
```

### Evidence class

```text
analytic convention fixture / harness target
```

This is convention-pinned and directly checkable.

### Refutation by observation / harness result

Layer 2 fails if the Catalan harness, using the pinned convention without changing branch or wall choices, returns:

```text
stokes_multiplier_observed != -1
abs(catalan_jump_coefficient_observed - 4) > tolerance
coefficient enumeration mismatch
branch coordinate mismatch
hash/provenance mismatch
```

### Refutation by construction

A construction refutes Layer 2 if it shows that under the pinned convention the declared lateral values are wrong.

Changing the convention does not refute Layer 2. It defines a different fixture.

### Refutation by scope violation

Layer 2 is scoped only to the Catalan square-root singularity under `A1-sauzin-normalization-v0`.

Layer 2 fails by scope if a harness:

```text
- imports a different Stokes normalization;
- uses a different branch coordinate without declaring an extension;
- compares against a Fuss-Catalan or A2 cube-root branch;
- treats the A1 result as evidence for A2 or higher A_n.
```

### Vacuity / under-constraint risk

The Catalan harness becomes vacuous if it simply hardcodes `(-1, 4)` without recomputing coefficient enumeration, branch behavior, and wall-crossing data from the declared fixture.

The harness must therefore emit enough receipt data to show that the observed values came from the declared fixture and not from expected-output replay alone.

### Nonclaims

Passing Layer 2 does not prove A1 gate minimality, polarization compatibility, A2 behavior, or P vs NP progress.

## 5. Layer 3 — A1 polarization compatibility bottleneck

### Claim being tested

The A1 polarization contract says the singular-germ source data and active-side readout data are connected by a predeclared transport map:

```text
E_phi: H_phi^bridge -> V_A
```

with:

```text
Q_A(E_phi(u), E_phi(v)) = Q_phi(u,v)
M_A E_phi = E_phi M_phi
pairing preservation under active monodromy
filtration preservation
```

### Evidence class

```text
structural contract / fixture-attestation target
```

This layer is mechanical. It is not a theorem by itself.

### Refutation by observation / harness result

Layer 3 fails if an A1 fixture receipt shows:

```text
E_phi not declared before monodromy evaluation;
rank(E_phi) below expected rank;
source pairing zero or undeclared;
pairing transport error > tolerance;
pairing preservation error > tolerance;
commutator_norm or monodromy compatibility residual > tolerance;
filtration_preservation_report != pass;
hash-chain or provenance mismatch.
```

### Refutation by construction

A construction refutes Layer 3 if it shows a valid-looking A1 run can pass while using post-hoc eigendirection selection, undeclared pairing extension, or basis manipulation that the receipt does not detect.

This is the main adversarial target: produce a fake or mutated fixture that should fail but passes.

### Refutation by scope violation

Layer 3 fails by scope if it is used to claim theorem-context canonicity for an object whose source pairing, active pairing, or encoding map was not declared in the contract.

Layer 3 also fails by scope if it is used as evidence outside algebraic isolated singularities without a declared extension theory.

### Vacuity / under-constraint risk

The contract is under-constrained if any sign-carrying active space can be made to pass by choosing `E_phi` after the fact.

Required anti-vacuity tests:

```text
- post-selected eigendirection must fail;
- missing source pairing must fail;
- wrong monodromy sign must fail;
- wrong active pairing extension must fail;
- failed filtration must fail.
```

### Nonclaims

Passing Layer 3 does not prove A1 gate minimality. It only supplies a valid input to the A1 proof note.

## 6. Layer 4 — A2 Candidate-A Stage-1 local cube-root realizability

### Claim being tested

For the pure local A2 cube-root model:

```text
u^3 = t
```

under `A2-local-cuberoot-normalization-v0`, Candidate A is realizable as a fixture with:

```text
closed-form omega and omega^2;
sample radii 1e-3, 1e-6, 1e-9;
cyclic sheet-basis continuation P;
closed-form DFT-3 character basis F;
F^{-1} P F = diag(1, omega, omega^2);
conjugate-character pairing Q;
intertwining M_A E_phi = E_phi M_phi.
```

### Evidence class

```text
Stage-1 computational fixture realization
```

This layer tests realizability of the pinned local fixture, not theorem-context naturality.

### Refutation by observation / harness result

Layer 4 fails if the canonical Stage-1 harness returns any of:

```text
lateral_value_max_error > tolerance;
additive_jump_max_error > tolerance;
sheet_basis_cubic_error > tolerance;
eigenvalue_max_error > tolerance;
character_basis_offdiag_ratio > tolerance;
character_basis_diag_max_error > tolerance;
pairing_transport_error > tolerance;
monodromy_compatibility_error > tolerance;
stage1_pass != true;
stage2_claimed != false.
```

### Refutation by construction

A construction refutes Layer 4 if it supplies a mutated or adversarial fixture that should fail but passes, for example:

```text
F constructed by eigendecomposition rather than the closed-form DFT-3 convention;
Q-dependent residual norm disguised as normalization;
wrong omega ordering passing as correct;
post-hoc sheet/channel reordering passing as predeclared basis;
E_phi treated as determinant/nondegenerate-energy object rather than transport map;
wrong monodromy matrix passing the intertwining check.
```

### Refutation by scope violation

Layer 4 fails by scope if its pass is interpreted as any of:

```text
A2 theorem-context naturality;
A2 gate minimality;
McKay-context A2 result;
A3 or higher A_n result;
C-6' general template completion;
I-12 promotion;
P vs NP or Clay progress.
```

### Vacuity / under-constraint risk

Layer 4 is vacuous if any `mu3`-labeled fixture can pass after basis relabeling.

Required anti-vacuity controls:

```text
- closed-form DFT-3 matrix, not eigendecomposition;
- no-mixing checked only in character basis;
- no-mixing residual epsilon-independent;
- Q-independent residual policy;
- E_phi rank/nullity and trivial-kernel checks;
- forbidden Stage-2 phrase guard in receipt/test surface.
```

### Nonclaims

Passing Layer 4 establishes only that the Candidate-A local cube-root readout contract is realizable on the declared fixture.

## 7. Layer 5 — A2 Stage-2 fixture-only five-object attestation

### Claim being tested

The Stage-2 fixture-only attestation says that the five declared objects from the A2 fixture are independently well-defined and structurally coherent as fixture objects:

```text
1. V_A^(2)
2. Q_A^(2)
3. E_phi^(2)
4. M_phi^(2)
5. M_A^(2)
```

Stage 2 is all-or-nothing at this attestation layer. Partial pass is not Stage 2.

### Evidence class

```text
fixture_only_reproducible_structural_attestation
```

The receipt must include:

```text
theorem_context_claimed: false
stage2_pass: true only if all five object attestations pass
partial_pass_count: integer
required_object_count: 5
```

### Refutation by observation / attestation result

Layer 5 fails if the Stage-2 receipt shows any of:

```text
object_attestations.V_A_2 != pass;
object_attestations.Q_A_2 != pass;
object_attestations.E_phi_2 != pass;
object_attestations.M_phi_2 != pass;
object_attestations.M_A_2 != pass;
protocol_validity.closed_form_DFT3 != pass;
protocol_validity.Q_independent_residuals != pass;
protocol_validity.transport_not_energy_functional != pass;
prediction_outcomes.all_five_objects_attested != pass;
stage2_pass != true;
theorem_context_claimed != false.
```

### Refutation by construction

A counter-construction refutes Layer 5 if an object mutation that should fail still passes attestation.

Minimum adversarial non-examples:

```text
wrong active-space dimension passes V_A^(2);
wrong pairing matrix passes Q_A^(2);
energy-functional leakage passes E_phi^(2);
wrong source monodromy passes M_phi^(2);
gate-minimality claim passes M_A^(2);
Q-dependent norm passes protocol_validity.Q_independent_residuals;
partial pass reports stage2_pass == true.
```

### Refutation by scope violation

Layer 5 fails by scope if a Stage-2 pass is represented as any of:

```text
theorem-context naturality;
A2 gate minimality;
canonical A2 polarization data;
McKay-context theorem result;
A3 or higher A_n result;
C-6' template completion;
I-12 promotion;
P vs NP or Clay progress.
```

### Vacuous-attestation failure mode

Layer 5 is under-constrained if adversarial non-examples that should fail the five-object attestation also pass.

This is a distinct failure from numerical mismatch. It means the attestation is not doing real work.

The key falsification test is therefore not only that the declared fixture passes, but that near-miss fixtures fail for the right reason.

A Stage-2 attestation that passes both the declared fixture and all adversarial non-examples is vacuous and must not be used as evidence.

### Nonclaims

Passing Layer 5 does not establish that the fixture is canonical theorem-context data. It only establishes reproducible structural coherence of the declared fixture.

## 8. Cross-layer non-promotion rules

The following promotions are forbidden without a separate issue, separate proof/attestation, and separate barrier entry:

```text
Layer 2 pass -> Layer 1 theorem
Layer 3 pass -> Layer 1 theorem
Layer 4 pass -> Layer 5 pass
Layer 5 pass -> theorem-context naturality
Layer 5 pass -> A2 gate minimality
A2 fixture pass -> A_n general result
A_n pattern evidence -> I-12 promotion
Any layer pass -> P vs NP / Clay progress
```

## 9. Falsification issue template

Future falsification issues should use this template:

```yaml
layer: 1 | 2 | 3 | 4 | 5
claim_id: string
attempt_type: observation | construction | scope | vacuity
expected_failure: string
artifact_under_test: string
required_inputs: list[string]
pass_condition_for_falsifier: string
if_falsifier_succeeds: demote | narrow_scope | revise_contract | reject_claim
nonclaims: list[string]
```

## 10. Immediate falsification backlog

Recommended first falsifiers:

```text
F1. A1 admissible-class counterexample search: attempt an abelian or smaller connected compact gate satisfying all five admissibility conditions.
F2. A1 polarization adversarial fixture: post-selected eigendirection must fail.
F3. A2 Stage-1 adversarial F: eigendecomposition-derived F must not be accepted as the reference closed-form fixture.
F4. A2 Stage-1 Q-norm adversary: residuals computed through Q must fail Q-independence tests.
F5. A2 Stage-2 vacuity test: mutated fixtures must fail exactly the relevant object attestation and must not report stage2_pass.
```

## 11. Done criteria for this specification

This falsification specification is complete when:

```text
- all five layers have explicit refutation criteria;
- Layer 5 includes vacuous-attestation failure mode;
- cross-layer non-promotion rules are explicit;
- no proof, harness, tolerance, or claim status is changed by this document.
```
