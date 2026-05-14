# C-3' Layer 2: A2 Polarization Candidates and Readout Contract

Status: **C-3' Layer 2 draft / theorem-input scoping note / not a Clay claim**.  
Depends on: `docs/proofs/c3-layer1-a2-group-identification.md`, `docs/proofs/a1-gate-minimality-assuming-polarization.md`, `docs/foundations/polarization.md`.  
Related issue: `#7` — C-3' cohomological projective-representation obstruction.

## 0. Purpose

Layer 1 established the immediate constraint for A2:

```text
C3 / mu3 is the natural local/ADE candidate at A2.
H^2(C3; U(1)) = 0.
```

Therefore A2 does not have the same projective-obstruction story as the A1 faithful branch. The A1 contract says polarization makes the `-1` eigendirection readout-compatible. A2 needs a different contract.

This note enumerates Layer 2 candidates for what A2 polarization compatibility could mean and selects a development default for the A2/Fuss-Catalan harness.

## 1. Restatement of the Layer 1 constraint

The A1 faithful branch uses:

```text
SO(3) projective action
H^2(SO(3); U(1)) = Z/2
auxiliary Spin(3)
-1 endpoint on V_A
```

A2 cannot inherit that structure by index substitution.

At the `C3` level:

```text
H^2(C3; U(1)) = 0.
```

But `C3` still has nontrivial character data:

```text
Hom(C3, U(1)) ~= mu3.
```

Thus the primary A2 signal available to a Stage-1 harness is likely root-of-unity sheet monodromy, not a projective obstruction class.

## 2. Candidate A — mu3 sheet grading without obstruction

### 2.1 Description

Candidate A treats A2 polarization as preservation of a predeclared `mu3` sheet grading.

The A2 source space decomposes into sheet/eigen channels:

```text
H_phi^(2) = H_0 ⊕ H_1 ⊕ H_2
```

with source monodromy acting by:

```text
M_phi^(2)|H_j = omega^j
```

where:

```text
omega = exp(2*pi*i/3).
```

The active space has a corresponding decomposition:

```text
V_A^(2) = V_0 ⊕ V_1 ⊕ V_2
```

and the transport map is block-compatible:

```text
E_phi^(2)(H_j) subset V_j.
```

The pairing must preserve the declared grading. Depending on the chosen form, the pairing may be diagonal by sheet or may pair conjugate sheets:

```text
Q_A^(2)(V_i, V_j) = 0 unless i + j ≡ 0 mod 3
```

or another explicitly declared rule.

### 2.2 What this candidate preserves

Candidate A preserves:

```text
sheet identity
mu3 character channel
no-mixing between readout sheets
predeclared readout sheet or sheet-pairing rule
```

It does not preserve a nontrivial Schur-multiplier obstruction, because Layer 1 found none at `C3`.

### 2.3 Required data

Candidate A requires:

```text
1. H_phi^(2) sheet/eigen decomposition.
2. V_A^(2) active sheet/eigen decomposition.
3. E_phi^(2) declared before harness evaluation.
4. M_phi^(2) with eigenvalues {1, omega, omega^2}.
5. M_A^(2) with matching active eigenvalues.
6. Pairing rule Q_A^(2) compatible with the grading.
7. No-mixing check: projection of E_phi^(2)(H_j) outside V_j is zero within tolerance.
8. Lateral-value schema with three sheet slots.
```

### 2.4 Readout contract

The A2 analog of the A1 bridge lemma becomes:

```text
If E_phi^(2) predeclares the A2 source sheet decomposition and preserves the mu3 grading, then the active sheet/readout channel used by the A2 harness is readout-compatible, not a post-hoc sheet selection.
```

This is a no-mixing/readout-sheet contract, not an obstruction-preservation contract.

### 2.5 Status

Candidate A is the development default because it is the closest structure to what the A2/Fuss-Catalan harness can directly measure: sheet structure, lateral values, Stokes multipliers, and additive jumps.

## 3. Candidate B — higher, twisted, or equivariant cohomology

### 3.1 Description

Candidate B asks whether A2 has nontrivial structure outside ordinary Schur-multiplier cohomology:

```text
H^3(C3; U(1))
twisted cohomology
equivariant cohomology
cohomology with nontrivial coefficient module
derived or categorical obstruction data
```

### 3.2 What would be required

Candidate B requires a precise coefficient system or higher-categorical object. It is not enough to say that higher cohomology may be nontrivial.

Required data:

```text
1. declared coefficient module or category;
2. group action on that coefficient object;
3. obstruction class definition;
4. relation between that class and V_A^(2), Q_A^(2), and E_phi^(2);
5. harness-observable consequence.
```

### 3.3 Status

Candidate B is held as a research branch. It is not the default harness contract because the current A2 harness proposal does not measure higher/twisted/equivariant cohomology.

## 4. Candidate C — S3 Weyl or full sheet-permutation reattachment

### 4.1 Description

Candidate C replaces the cyclic `C3` branch role with a larger sheet-permutation or Weyl-group role:

```text
S3
```

This may become relevant if the A2 object tracks all root permutations, discriminant loops, or Weyl reflections rather than only cyclic local monodromy.

### 4.2 Why this matters

The Weyl group of type A2 is `S3`. If a principled construction identifies the relevant A2 carrier as the Weyl/sheet-permutation group, then the cohomology and extension problem must be recalculated for `S3` and for the actual representation/polarization data used.

This may reintroduce nontrivial extension phenomena not visible at the `C3` level.

### 4.3 Required data

Candidate C requires:

```text
1. a declared reason that S3, not C3, is the relevant group role;
2. a root/sheet-permutation action on H_phi^(2);
3. an active S3 action on V_A^(2);
4. pairing compatibility for reflections and 3-cycles;
5. a predeclared readout sheet or orbit rule;
6. proof that the harness is testing S3 structure rather than only cyclic mu3 monodromy.
```

### 4.4 Status

Candidate C is conditional. The Layer 1 note intentionally did not assume it. The A2 harness must not switch from `C3` to `S3` after observing output.

## 5. Candidate D — no Stage-2 obstruction analog

### 5.1 Description

Candidate D is the honest null possibility:

```text
A2 has no A1-style obstruction-attachment story.
```

In this case, A2/Fuss-Catalan harness outputs remain analytic normalization evidence:

```text
coefficient enumeration
sheet structure
Stokes multipliers
additive jumps
lateral values
```

but they do not promote to A2 gate-minimality in the A1 sense.

### 5.2 Consequence for the template

If Candidate D is correct, the template generalization changes form.

The unifying structure would not be:

```text
the same obstruction-attachment frame at each prime/singularity type.
```

It would be:

```text
a moment / sheet / normalization hierarchy with prime-specific structural attachments.
```

This is a weaker but more honest conjecture. It may be more mathematically interesting, because it allows p=2 to be exceptional.

### 5.3 Status

Candidate D is the fallback if Candidate A fails to produce a coherent A2 readout-basis contract and no principled Candidate B or C attachment is supplied.

## 6. Selected development default

The selected development default is:

```text
Candidate A — mu3 sheet grading without obstruction.
```

Reason:

```text
1. It matches the Stage-1 data the A2/Fuss-Catalan harness can plausibly emit.
2. It respects Layer 1's trivial H^2(C3; U(1)) result.
3. It avoids falsely importing the A1 Spin(3) obstruction story.
4. It supplies a concrete no-mixing/readout-sheet contract.
```

Fallback:

```text
Candidate D — no Stage-2 obstruction analog.
```

Conditional research branches:

```text
Candidate B — higher/twisted/equivariant cohomology.
Candidate C — S3/Weyl/full sheet-permutation reattachment.
```

## 7. A2 readout-basis contract v0

Under Candidate A, the A2 harness may claim readout compatibility only if it emits and passes the following checks.

### 7.1 Declared sheet structure

```yaml
source_sheet_structure:
  group_role: C3_branch_monodromy
  sheets: [0, 1, 2]
  eigenvalues: [1, omega, omega^2]
  principal_sheet_rule: declared_before_evaluation
```

### 7.2 Active decomposition

```yaml
active_decomposition:
  V_A_2: declared
  V_0: declared
  V_1: declared
  V_2: declared
  direct_sum_verified: true
```

### 7.3 Transport map

```yaml
encoding:
  E_phi_2: declared_before_evaluation
  block_compatibility:
    H_0_to_V_0: pass
    H_1_to_V_1: pass
    H_2_to_V_2: pass
  no_posthoc_sheet_selection: true
```

### 7.4 Monodromy compatibility

```text
M_A^(2) E_phi^(2) = E_phi^(2) M_phi^(2)
```

with reported error:

```yaml
monodromy_compatibility_error: number
monodromy_compatibility_tolerance: number
```

### 7.5 Pairing compatibility

The pairing rule must be declared before evaluation:

```yaml
pairing_rule:
  type: diagonal_by_sheet | conjugate_sheet_pairing | explicitly_declared_other
  allowed_pairs: list
```

The harness must report:

```yaml
pairing_transport_error: number
pairing_transport_tolerance: number
```

### 7.6 Lateral values

A2 has three sheet/lateral slots, not two:

```yaml
lateral_values:
  sheet_0: value
  sheet_1: value
  sheet_2: value
```

The principal sheet must be selected by a rule declared before extraction.

## 8. Tolerance and depth placeholders

The A2 harness must pin its own tolerances and enumeration depth before execution.

Required fields:

```yaml
coefficient_enumeration_depth_N: integer
coefficient_tolerance: number
stokes_multiplier_tolerance: number
additive_jump_tolerance: number
monodromy_compatibility_tolerance: number
pairing_transport_tolerance: number
no_mixing_tolerance: number
```

These values are not supplied by this note. They belong in the future `A2-fusscatalan-normalization-v0` spec. The tolerance must account for cube-root numerical sensitivity and cannot be inherited blindly from `A1-sauzin-normalization-v0`.

## 9. Promotion rule

An A2 harness result may be promoted from Stage 1 to Stage 2 only if:

```text
1. Candidate A, B, C, or D status is declared before evaluation.
2. If Candidate A is used, the mu3 sheet-grading contract passes.
3. If Candidate B is used, the higher/twisted/equivariant cohomology object is defined and attached to V_A^(2).
4. If Candidate C is used, the S3/Weyl reattachment is justified before measurement.
5. If Candidate D is selected, no Stage-2 obstruction claim is made.
6. Nonclaim boundaries remain intact.
```

## 10. Nonclaims

This note does not claim:

- an A2 gate-minimality theorem;
- a P vs NP result;
- a lower bound;
- that Candidate A is true;
- that Candidate D is false;
- that higher cohomology supplies the missing obstruction;
- that S3 is the correct A2 group;
- that SU(3) is justified;
- that the A2/Fuss-Catalan harness can promote without Layer 2 data.

It is a Layer 2 candidate and contract note. Its purpose is to make the next A2 harness measurable without overclaiming.