# A2 Track Archival Status

Status: **archival boundary / closed slice / not a theorem claim**.  
Repository: `SocioProphet/np-program`.  
Snapshot date: 2026-05-14.  
Purpose: record the closed state of the A2 track so future work does not silently reinterpret merged fixture, convention, or theorem-input artifacts.

## 0. Summary

The A2 track is at a clean archival boundary.

The merged material establishes:

```text
1. A1 theorem-input structure and polarization bridge are documented.
2. A2 group/cohomology scoping is documented.
3. A2 local cube-root fixture, normalization, test vectors, and Stage-1 harness are implemented.
4. Stage-2 theorem-context attestation is scaffolded but not satisfied.
5. A2/Ak attachment is future theorem work, not unresolved cleanup.
```

The current A2 material is internally consistent and does not depend on resolving the future A2/Ak theorem question.

## 1. Merged stack

### A1 foundation and faithful branch

- `docs/proofs/a1-gate-minimality-faithful.md`
- `docs/proofs/a1-gate-minimality-assuming-polarization.md`
- `docs/foundations/polarization.md`

These files lock the faithful A1 branch:

```text
G = SO(3)
-I lives in auxiliary Spin(3) on V_A, not in G
zeta = sigma(gamma_tilde(1)) = -I on V_A
```

The bridge lemma states that, assuming polarization compatibility, the transported A1 sign line is readout-compatible and not a post-hoc coordinate-basis sign flip.

### C-3' A2 scoping

- `docs/proofs/c3-layer1-a2-group-identification.md`
- `docs/proofs/c3-layer2-a2-polarization-candidates.md`
- `docs/proofs/c3-cohomological-obstruction.md`

These files separate:

```text
1. C3 / mu3 as the natural local/ADE A2 candidate;
2. H^2(C3; U(1)) = 0 at the C3 level;
3. Candidate A: mu3 sheet grading without obstruction;
4. Candidate D: no Stage-2 obstruction analog;
5. the SO(3) projective obstruction used in A1;
6. the open A2/Ak attachment question.
```

### Target split

- `docs/conventions/a2-target-split.md`

This file blocks the false identification:

```text
order-3 Fuss-Catalan critical branch != pure local A2 cube-root branch
```

It splits:

```text
Target F:
  y = 1 + x y^3
  x0 = 4/27, y0 = 3/2
  generic square-root critical branch

Target A2:
  u^3 = t
  C3 / mu3 monodromy
  pure local cube-root branch
```

### A2 local cube-root computational layer

- `docs/conventions/a2-local-cuberoot-normalization-v0.md`
- `specs/a2-local-cuberoot-test-vectors.md`
- `experiments/a2_local_cuberoot_harness.py`
- `tests/test_a2_local_cuberoot_harness.py`

These files implement the Stage-1 local fixture:

```text
u^3 = t
omega = exp(2*pi*i/3)
principal sheet S0 is real positive for t > 0
sheet-basis continuation is cyclic permutation P
character-basis continuation is diag(1, omega, omega^2)
additive jump vector is [omega - 1, omega^2 - omega, 1 - omega^2]
```

The Stage-1 harness passes only fixture-level predicates and emits `stage2_claimed: false`.

### Stage-2 scaffold

- `docs/proofs/a2-stage2-attestation.md`

This file records what a Stage-1 pass does not establish and what Stage 2 must additionally attest.

## 2. Locked conventions

The A2 track currently depends on the following conventions.

### A1 faithful convention

```text
A1 faithful branch: T2'
G = SO(3)
auxiliary group = Spin(3)
V_A = C^2
zeta = sigma(gamma_tilde(1)) = -I on V_A
```

### Projective-representation obstruction convention

```text
H^2_proj(SO(3); U(1)) ~= Z/2
```

Here `H^2_proj` names the projective-representation / continuous-central-extension convention used in the repo. It is not ordinary singular cohomology of the topological space `SO(3)`.

### A2 local convention

```text
A2-local-cuberoot-normalization-v0
model: u^3 = t
target: pure local A2 cube-root
```

### Target split convention

```text
fusscatalan-order3-critical-normalization-v0  # future Target F convention
A2-local-cuberoot-normalization-v0            # current Target A2 convention
```

Do not use the label `A2-fusscatalan-normalization-v0` without explicitly resolving the target split.

## 3. Current evidence classes

| Artifact | Evidence class | What it establishes | What it does not establish |
|---|---|---|---|
| A1 faithful proof note | theorem-input | faithful A1 structure under declared hypotheses | P vs NP, lower bound, A2 inheritance |
| A1 polarization bridge lemma | theorem-input bridge | transported A1 sign line is readout-compatible under polarization assumption | universal readout principle |
| C-3' Layer 1/2 notes | structural scoping | A2 candidate structure and non-inheritance of A1 obstruction | A2 theorem |
| A2 target split | convention / guardrail | Fuss-Catalan order-3 and pure A2 local target are distinct | either harness passes |
| A2 local convention | local normalization | declared local cube-root convention | theorem-context naturality |
| A2 test vectors | fixture | expected local computational values | canonicality |
| A2 harness | computational diagnostic | Stage-1 fixture implementation correctness | Stage-2, I-12, Clay |
| A2 Stage-2 scaffold | attestation schema | what future theorem-context attestation must close | theorem-context attestation itself |

## 4. Open future theorem question

The A2/Ak attachment problem is open as future theorem work.

It is not an unresolved cleanup item.

It is not a gap in the merged C-3' Layer 1 / Layer 2 / cohomological scoping stack.

The future question is:

```text
Given A_k source monodromy, V_A^(k), Q_A^(k), E_phi^(k), active monodromy, and auxiliary data, is there an obstruction or character attachment that plays a theorem-facing role analogous to A1's Spin(3) realization?
```

For A2 specifically, possible answers remain:

```text
Candidate A: mu3 sheet grading is theorem-context data.
Candidate B: higher/twisted/equivariant cohomology supplies structure.
Candidate C: S3/Weyl reattachment is justified.
Candidate D: no Stage-2 obstruction analog exists.
```

No current merged artifact chooses among these as a theorem result.

## 5. What future work must not do

Future work must not:

```text
- treat the A2 Stage-1 harness pass as theorem-facing evidence;
- claim I-12 template promotion from the Stage-1 harness;
- identify order-3 Fuss-Catalan with pure local A2 cube-root;
- inherit A1 Spin(3) data into A2/Ak without rederiving auxiliary data;
- cite H^2_proj(SO(3); U(1)) ~= Z/2 as an A2 obstruction;
- silently compose fixture-level evidence into theorem support.
```

Any composition of multiple fixture-level attestations into a higher-level claim must carry an explicit composition warrant.

## 6. Restart protocol

When reopening A2/Ak theorem work, start from:

```text
1. docs/proofs/a2-stage2-attestation.md
2. docs/proofs/c3-cohomological-obstruction.md
3. docs/proofs/c3-layer2-a2-polarization-candidates.md
4. docs/conventions/a2-target-split.md
```

Then choose one of:

```text
A. theorem-context attestation for the current pure A2 local fixture;
B. a separate Target F / order-3 Fuss-Catalan square-root critical harness;
C. a higher-Ak target with a new target-split convention and new normalization;
D. Candidate D, explicitly recording that no Stage-2 obstruction analog is claimed.
```

## 7. Nonclaims

This archival status document does not claim:

```text
- A2 gate minimality;
- A2 theorem-context naturality;
- A2/Ak obstruction existence;
- I-12 template promotion;
- P vs NP progress;
- any Clay result.
```

It freezes the current methodological state so future work can resume without silent inheritance or doctrinal drift.
