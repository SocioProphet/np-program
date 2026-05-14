# A2 Local Cube-Root Normalization v0

Status: **committed local convention v0 / pure A2 target / Stage-1 harness contract**.  
Convention ID:

```text
A2-local-cuberoot-normalization-v0
```

Depends on:

```text
docs/conventions/a2-target-split.md
docs/proofs/c3-layer1-a2-group-identification.md
docs/proofs/c3-layer2-a2-polarization-candidates.md
docs/foundations/polarization.md
```

## 0. Scope

This convention covers the pure local A2 cube-root target:

```text
u^3 = t.
```

It does not cover the order-3 Fuss-Catalan critical branch:

```text
y = 1 + x y^3, x0 = 4/27, y0 = 3/2.
```

That target is square-root critical and requires a separate convention such as:

```text
fusscatalan-order3-critical-normalization-v0
```

This A2 local convention is a Stage-1 analytic normalization and Candidate-A readout-contract instrument. Stage-2 promotion still requires the Layer 2 attestation defined in `docs/proofs/c3-layer2-a2-polarization-candidates.md`.

## 1. Local model

The local model is:

```text
u^3 = t.
```

The singularity is at:

```text
t = 0.
```

The canonical wall is the positive real `t`-ray. The local coordinate is already the branch coordinate; no Fuss-Catalan generating-function coordinate is used.

## 2. Root of unity convention

Set:

```text
omega = exp(2*pi*i/3) = -1/2 + i*sqrt(3)/2.
```

The three local branches are indexed by:

```text
S_0, S_1, S_2.
```

For `t = r exp(i theta)` with `r > 0` and `0 < theta < 2*pi`, define:

```text
u_k(t) = r^(1/3) exp(i*(theta + 2*pi*k)/3),  k in {0,1,2}.
```

The principal sheet is:

```text
S_0: u_0(r) = r^(1/3) > 0 for t = r > 0.
```

This principal-sheet rule is declared before evaluation and must be included in all run ledgers.

## 3. Lateral values on the canonical wall

Let the plus side of the positive real `t`-ray mean:

```text
t = r exp(i*0+), r > 0.
```

Let the minus side mean:

```text
t = r exp(i*2*pi-), r > 0.
```

Then the plus lateral values are:

```text
u_0^+(r) = r^(1/3)
u_1^+(r) = omega * r^(1/3)
u_2^+(r) = omega^2 * r^(1/3)
```

and the minus lateral values are:

```text
u_0^-(r) = omega * r^(1/3)
u_1^-(r) = omega^2 * r^(1/3)
u_2^-(r) = r^(1/3)
```

Equivalently:

```text
u_k^-(r) = omega * nu_k^+(r).
```

The harness must emit three lateral-value slots on each side:

```yaml
lateral_values_plus:
  sheet_0: complex
  sheet_1: complex
  sheet_2: complex
lateral_values_minus:
  sheet_0: complex
  sheet_1: complex
  sheet_2: complex
```

## 4. Monodromy and continuation matrices

### 4.1 Sheet basis

In the ordered sheet basis:

```text
[S_0, S_1, S_2]
```

a positive loop around `t = 0` sends:

```text
S_0 -> S_1 -> S_2 -> S_0.
```

The sheet-basis continuation matrix is the cyclic permutation matrix:

```text
P = [[0, 0, 1],
     [1, 0, 0],
     [0, 1, 0]].
```

It satisfies:

```text
P^3 = I.
```

Its eigenvalues are:

```text
{1, omega, omega^2}.
```

### 4.2 Character basis

In the `mu3` character basis, the same continuation action is diagonal:

```text
D = diag(1, omega, omega^2)
```

up to the declared ordering of characters.

Therefore the no-mixing check is not performed in the sheet basis. It is performed in the declared character basis.

This is load-bearing: the harness must not require a sheet-basis cyclic permutation matrix to be diagonal. That would conflate sheet permutation with character decomposition.

## 5. Stokes / continuation multiplier checks

The hard multiplier checks for this convention are:

```text
P^3 = I
spec(P) = {1, omega, omega^2}
D = diag(1, omega, omega^2) in character basis
```

The harness must report:

```yaml
sheet_basis_matrix: matrix
sheet_basis_cubic_error: number
sheet_basis_eigenvalues: list[complex]
character_basis_matrix: matrix
character_basis_offdiag_ratio: number
character_basis_diag_errors: list[number]
```

Required tolerances:

```yaml
sheet_basis_cubic_tolerance: 1.0e-12
eigenvalue_tolerance: 1.0e-12
character_basis_offdiag_tolerance: 1.0e-12
character_basis_diag_tolerance: 1.0e-12
```

The harness may use exact symbolic arithmetic or arbitrary-precision complex arithmetic. If double precision is used, the implementation must report the numerical precision and the observed residuals.

## 6. Additive jump vector

For the normalized generator `u = t^(1/3)`, the additive jumps across the canonical wall are sheet-indexed:

```text
Delta_k(r) = u_k^-(r) - u_k^+(r)
           = omega^k * (omega - 1) * r^(1/3).
```

Thus the normalized additive-jump coefficient vector is:

```text
J_expected = [omega - 1,
              omega^2 - omega,
              1 - omega^2].
```

The harness must emit the raw observed vector and the normalized coefficient vector:

```yaml
additive_jump_raw:
  sheet_0: complex
  sheet_1: complex
  sheet_2: complex
additive_jump_coefficients:
  sheet_0: complex
  sheet_1: complex
  sheet_2: complex
additive_jump_errors:
  sheet_0: number
  sheet_1: number
  sheet_2: number
```

Required tolerance:

```yaml
additive_jump_coefficient_tolerance: 1.0e-12
```

No scalar coefficient such as `27` is part of this convention. The earlier `27` value belonged to a conflated Fuss-Catalan critical-target draft and is not used here.

## 7. Candidate-A readout contract fixture

This convention supplies a reference fixture for Candidate A from the C-3' Layer 2 note.

Use:

```text
H_phi^(2) = C e_0 ⊕ C e_1 ⊕ C e_2
V_A^(2)   = C v_0 ⊕ C v_1 ⊕ C v_2
E_phi^(2)(e_j) = v_j
```

In the character basis:

```text
M_phi^(2) = diag(1, omega, omega^2)
M_A^(2)   = diag(1, omega, omega^2)
```

The intertwining relation is:

```text
M_A^(2) E_phi^(2) = E_phi^(2) M_phi^(2).
```

Required tolerance:

```yaml
monodromy_compatibility_tolerance: 1.0e-12
```

The harness must report:

```yaml
monodromy_compatibility_error: number
```

## 8. Pairing convention for the reference fixture

Use the conjugate-character pairing:

```text
Q(v_i, v_j) = 1 if i + j ≡ 0 mod 3
Q(v_i, v_j) = 0 otherwise.
```

In the ordered character basis `[v_0, v_1, v_2]`, this is:

```text
Q = [[1, 0, 0],
     [0, 0, 1],
     [0, 1, 0]].
```

This pairing is preserved by the character-basis monodromy:

```text
D^T Q D = Q.
```

The harness must report:

```yaml
pairing_matrix: matrix
pairing_transport_error: number
```

Required tolerance:

```yaml
pairing_transport_tolerance: 1.0e-12
```

## 9. Sample radii

The harness must evaluate lateral values at the following radii:

```text
r in {1.0e-3, 1.0e-6, 1.0e-9}
```

For each `r`, the normalized jump coefficients must match `J_expected` within tolerance.

These radii are not used for asymptotic coefficient fitting. There is no coefficient enumeration in the pure local cube-root harness.

## 10. Output schema

Each run emits:

```yaml
convention_id: A2-local-cuberoot-normalization-v0
target: A2_local_cuberoot
local_model: u^3 = t
omega: complex
principal_sheet_rule: S_0 real positive for t > 0
canonical_wall: positive_real_t_ray
sample_radii: [1.0e-3, 1.0e-6, 1.0e-9]
lateral_values_plus: object
lateral_values_minus: object
sheet_basis_matrix: matrix
sheet_basis_cubic_error: number
sheet_basis_eigenvalues: list[complex]
character_basis_matrix: matrix
character_basis_offdiag_ratio: number
character_basis_diag_errors: list[number]
additive_jump_raw: object
additive_jump_coefficients: object
additive_jump_errors: object
monodromy_compatibility_error: number
pairing_matrix: matrix
pairing_transport_error: number
stage: "1"
precision_report: object
provenance:
  harness_version: string
  convention_hash: string
  input_hash_chain: list[string]
  output_hash: string
  generated_at: string
scope_declaration: algebraic isolated singularity, pure local A2 cube-root target, C3/mu3 monodromy, Candidate A readout contract fixture
```

## 11. Pass / fail logic

A run passes Stage 1 iff all hold:

```text
sheet_basis_cubic_error <= 1.0e-12
all sheet_basis_eigenvalues match {1, omega, omega^2} within 1.0e-12
character_basis_offdiag_ratio <= 1.0e-12
all character_basis_diag_errors <= 1.0e-12
all additive_jump_errors <= 1.0e-12
monodromy_compatibility_error <= 1.0e-12
pairing_transport_error <= 1.0e-12
```

A passing Stage-1 run does not by itself prove an A2 gate-minimality theorem.

Stage-2 promotion requires a separate attestation that the fixture is the intended `V_A^(2), Q_A^(2), E_phi^(2), M_phi^(2), M_A^(2)` data for the target theorem context and that Candidate A is the selected contract for that theorem context.

## 12. Non-goals

This convention does not:

```text
- test the order-3 Fuss-Catalan critical branch;
- enumerate Fuss-Catalan coefficients;
- use x0 = 4/27;
- use additive coefficient 27;
- test Candidate B higher/twisted/equivariant cohomology;
- test Candidate C S3/Weyl reattachment;
- prove Candidate D false;
- prove A2 gate minimality;
- prove P vs NP or any Clay claim;
- extend to non-algebraic singularities.
```

## 13. Relation to future Target F convention

The future order-3 Fuss-Catalan critical-branch convention should be written separately. It should use the target name:

```text
fusscatalan-order3-critical-normalization-v0
```

and should treat the dominant singularity as square-root critical. It may compare with `A1-sauzin-normalization-v0` structurally, but it must not cite this A2 local cube-root convention as its local branch model.