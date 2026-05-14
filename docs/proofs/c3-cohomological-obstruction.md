# C-3' Cohomological Obstruction Note

Status: **C-3' structural proof note / theorem-input scoping / not a Clay claim**.  
Related issue: `#7` — Write C-3' cohomological projective-representation obstruction.  
Depends on:

```text
docs/proofs/a1-gate-minimality-faithful.md
docs/proofs/a1-gate-minimality-assuming-polarization.md
docs/proofs/c3-layer1-a2-group-identification.md
docs/proofs/c3-layer2-a2-polarization-candidates.md
docs/proofs/a2-stage2-attestation.md
```

## 0. Purpose

This note records the cohomological obstruction statement used by the faithful A1 branch and separates it from its A1-specific realization.

It has three jobs:

```text
1. state the SO(3) projective-representation obstruction class;
2. state how the A1 faithful branch realizes/resolves it through Spin(3);
3. state the A2/Ak attachment question as open rather than inherited.
```

It does not prove an A2 theorem and does not promote any Stage-1 harness result.

## 1. The SO(3) obstruction class

In the projective-representation / continuous-central-extension convention used in this repository, projective representations of `SO(3)` have a `Z/2` obstruction class:

```text
H^2_proj(SO(3); U(1)) ~= Z/2.
```

Here `H^2_proj` denotes the group-cohomological/projective-representation classification of continuous `U(1)`-central extensions relevant to lifting projective actions to linear actions. The notation is pinned here to avoid confusing this obstruction with ordinary singular cohomology of the topological space `SO(3)` or with cohomology of a representation variety.

Equivalently, the obstruction is detected by the fundamental group:

```text
pi_1(SO(3)) ~= Z/2.
```

The nontrivial class corresponds to the double cover:

```text
Spin(3) = SU(2) -> SO(3).
```

This obstruction statement is a fact about the projective-representation setting for `SO(3)`. It is not yet a statement about A1, A2, or any proof-complexity object.

## 2. The A1-specific Spin(3) realization

The faithful A1 branch uses the preceding obstruction class in a specific way.

The faithful spatial group is:

```text
G = SO(3).
```

The active spinor data live in an auxiliary structure:

```text
sigma: Spin(3) -> Sp(V_A, Q_A) = SL(2, C).
```

The distinguished loop class:

```text
gamma in pi_1(SO(3)) = Z/2
```

lifts to a path in `Spin(3)` with endpoint:

```text
gamma_tilde(1) = -I.
```

Thus, under the auxiliary spinor representation:

```text
sigma(gamma_tilde(1)) = -I on V_A.
```

Load-bearing sentence:

```text
The nontrivial SO(3) projective-representation obstruction is resolved in the A1 faithful branch by passing to the auxiliary Spin(3) frame; the obstruction class pulls back to the trivial class along Spin(3) -> SO(3).
```

This is the A1 realization. It is not merely another name for the obstruction. The obstruction is a property of `SO(3)` projective representations; the resolution is a property of the specific extension and representation data chosen in the A1 faithful branch.

The A1 polarization bridge lemma then supplies the readout-basis condition: the transported A1 sign line is predeclared by `E_phi`, preserved by the pairing, and not selected after observing a convenient `-1` eigendirection.

## 3. The A2/Ak attachment question

For A2 and higher `A_k`, the preceding A1 realization does not automatically generalize.

The analogous question is:

```text
Given a proposed A_k source monodromy, active space V_A^(k), pairing Q_A^(k), transport E_phi^(k), and active monodromy M_A^(k), is there an obstruction class whose realization/resolution is carried by the declared auxiliary data?
```

For A2, the merged Layer 1 note established:

```text
C3 / mu3 is the natural local/ADE candidate at A2;
H^2(C3; U(1)) = 0.
```

Therefore there is no A1-style Schur-multiplier obstruction at the `C3` level.

The merged Layer 2 note then separated possible A2 paths:

```text
Candidate A: mu3 sheet grading without obstruction.
Candidate B: higher/twisted/equivariant cohomology.
Candidate C: conditional S3/Weyl/full sheet-permutation reattachment.
Candidate D: no Stage-2 obstruction analog.
```

This note does not choose among those candidates. It states the discipline:

```text
A2/Ak must rederive the obstruction or character attachment from their own V_A, Q_A, E_phi, monodromy, and auxiliary data. They do not inherit the A1 Spin(3) realization.
```

## 4. Relationship to the C-3' stack

The current C-3' stack has three distinct roles.

```text
Layer 1 — docs/proofs/c3-layer1-a2-group-identification.md
  Identifies the immediate A2 group candidates and their cohomological consequences.

Layer 2 — docs/proofs/c3-layer2-a2-polarization-candidates.md
  Enumerates possible A2 polarization/readout contracts after Layer 1.

Cohomological obstruction note — this file
  Separates the SO(3) obstruction class from the A1 Spin(3) realization and marks A2/Ak attachment as open.
```

This file is the capstone for the C-3' scoping work. It prevents the A1 obstruction class from being silently treated as a reusable template for every `A_k`.

## 5. Nonclaims

This note does not claim:

```text
- that A2 or higher A_k has a cohomological obstruction at all;
- that the A1 Spin(3) realization generalizes to A2/Ak;
- that C3/mu3 has a nontrivial Schur-multiplier obstruction;
- that S3/Weyl reattachment is justified;
- that SU(3) or any other auxiliary carrier is selected;
- that the A2 local cube-root Stage-1 harness is theorem-facing evidence;
- that I-12 is promotion-ready;
- that any P vs NP, lower-bound, or Clay claim follows.
```

It states a projective-representation obstruction for `SO(3)`, records the A1 faithful realization through `Spin(3)`, and defines the A2/Ak attachment question as open.

## 6. Closing status for Issue #7

This file satisfies Issue #7 by providing:

```text
1. the projective-representation obstruction class for SO(3);
2. the A1-specific Spin(3) realization;
3. explicit separation between the SO(3) calculation and the A1 V_A realization;
4. the A2/Ak attachment question as future work;
5. nonclaim boundaries preserving Stage-1 / Stage-2 / Clay separation.
```
