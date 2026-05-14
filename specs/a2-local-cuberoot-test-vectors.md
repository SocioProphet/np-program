# A2 Local Cube-Root Harness Test Vectors

Status: **implementation fixture spec / Stage-1 harness target / not theorem content**.  
Depends on: `docs/conventions/a2-local-cuberoot-normalization-v0.md`.  
Convention ID:

```text
A2-local-cuberoot-normalization-v0
```

## 0. Purpose

This file turns the A2 local cube-root convention into fixed test vectors for implementation.

It supplies:

```text
- exact omega values;
- sheet-basis continuation matrix;
- character-basis diagonalization matrix;
- pairing matrix;
- sample radii;
- expected plus/minus lateral values;
- expected additive-jump coefficients;
- pass/fail tolerances;
- pseudocode for the Stage-1 harness.
```

The fixture tests the pure local model:

```text
u^3 = t.
```

It does not test the order-3 Fuss-Catalan critical branch.

## 1. Constants

Use exact symbolic constants when possible.

```text
omega = exp(2*pi*i/3) = -1/2 + i*sqrt(3)/2
omega2 = omega^2 = -1/2 - i*sqrt(3)/2
```

Decimal values for numerical fixtures:

```yaml
omega:
  re: -0.5
  im:  0.86602540378443864676
omega2:
  re: -0.5
  im: -0.86602540378443864676
```

Expected additive-jump coefficients:

```text
J0 = omega - 1       = -3/2 + i*sqrt(3)/2
J1 = omega2 - omega  = -i*sqrt(3)
J2 = 1 - omega2      =  3/2 + i*sqrt(3)/2
```

Decimal form:

```yaml
additive_jump_coefficients_expected:
  sheet_0: {re: -1.5, im:  0.86602540378443864676}
  sheet_1: {re:  0.0, im: -1.73205080756887729353}
  sheet_2: {re:  1.5, im:  0.86602540378443864676}
```

## 2. Sample radii

Use exactly these sample radii for the v0 fixture:

```yaml
sample_radii:
  - 1.0e-3
  - 1.0e-6
  - 1.0e-9
```

Their real cube roots are:

```yaml
cube_roots:
  1.0e-3: 0.1
  1.0e-6: 0.01
  1.0e-9: 0.001
```

## 3. Expected lateral values

For `a = r^(1/3)`, plus-side values are:

```text
u_0^+(r) = a
u_1^+(r) = omega * a
u_2^+(r) = omega2 * a
```

Minus-side values are:

```text
u_0^-(r) = omega * a
u_1^-(r) = omega2 * a
u_2^-(r) = a
```

### 3.1 r = 1.0e-3

```yaml
r: 1.0e-3
a: 0.1
lateral_values_plus:
  sheet_0: {re:  0.1,  im:  0.0}
  sheet_1: {re: -0.05, im:  0.08660254037844386468}
  sheet_2: {re: -0.05, im: -0.08660254037844386468}
lateral_values_minus:
  sheet_0: {re: -0.05, im:  0.08660254037844386468}
  sheet_1: {re: -0.05, im: -0.08660254037844386468}
  sheet_2: {re:  0.1,  im:  0.0}
```

### 3.2 r = 1.0e-6

```yaml
r: 1.0e-6
a: 0.01
lateral_values_plus:
  sheet_0: {re:  0.01,  im:  0.0}
  sheet_1: {re: -0.005, im:  0.00866025403784438647}
  sheet_2: {re: -0.005, im: -0.00866025403784438647}
lateral_values_minus:
  sheet_0: {re: -0.005, im:  0.00866025403784438647}
  sheet_1: {re: -0.005, im: -0.00866025403784438647}
  sheet_2: {re:  0.01,  im:  0.0}
```

### 3.3 r = 1.0e-9

```yaml
r: 1.0e-9
a: 0.001
lateral_values_plus:
  sheet_0: {re:  0.001,  im:  0.0}
  sheet_1: {re: -0.0005, im:  0.00086602540378443865}
  sheet_2: {re: -0.0005, im: -0.00086602540378443865}
lateral_values_minus:
  sheet_0: {re: -0.0005, im:  0.00086602540378443865}
  sheet_1: {re: -0.0005, im: -0.00086602540378443865}
  sheet_2: {re:  0.001,  im:  0.0}
```

## 4. Additive jump checks

For each radius `r`, compute:

```text
Delta_k(r) = u_k^-(r) - u_k^+(r).
```

Normalize by:

```text
a = r^(1/3)
J_k_observed = Delta_k(r) / a.
```

Expected:

```text
[J_0, J_1, J_2] = [omega - 1, omega2 - omega, 1 - omega2].
```

The normalized coefficients must match the expected values at every sample radius.

Required tolerance:

```yaml
additive_jump_coefficient_tolerance: 1.0e-12
```

No scalar `27` appears in this fixture.

## 5. Sheet-basis continuation matrix

Use ordered sheet basis:

```text
[S_0, S_1, S_2].
```

The positive continuation matrix is:

```text
P = [[0, 0, 1],
     [1, 0, 0],
     [0, 1, 0]].
```

Expected checks:

```text
P^3 = I
spec(P) = {1, omega, omega2}
```

Required tolerances:

```yaml
sheet_basis_cubic_tolerance: 1.0e-12
eigenvalue_tolerance: 1.0e-12
```

## 6. Character-basis diagonalization

Use the character basis matrix `F` whose columns are eigenvectors of `P` ordered to give diagonal entries `[1, omega, omega2]`:

```text
F = [[1, 1,      1],
     [1, omega2, omega],
     [1, omega,  omega2]].
```

Then:

```text
F^{-1} P F = D
D = diag(1, omega, omega2).
```

The harness must report the character-basis matrix:

```text
D_observed = F^{-1} P F.
```

No-mixing check:

```text
offdiag(D_observed) == 0
```

with tolerance:

```yaml
character_basis_offdiag_tolerance: 1.0e-12
character_basis_diag_tolerance: 1.0e-12
```

This is the only valid no-mixing check in v0. The sheet basis is allowed to be cyclic-permutation, not diagonal.

### 6.1 Reference implementation precision policy

The reference harness must construct `F` from the exact closed-form DFT-of-3 matrix above. It must not construct `F` through floating-point eigendecomposition of `P`.

The no-mixing residual:

```text
F^{-1} P F - diag(1, omega, omega2)
```

is a structural basis-change residual. It is independent of the sample radius `epsilon` and must not inherit tolerances from lateral-value checks at `1.0e-3`, `1.0e-6`, or `1.0e-9`.

The reference implementation should report the policy explicitly:

```yaml
precision_policy:
  omega_source: closed_form_-1/2_plus_minus_i_sqrt3_over_2
  character_basis_F_source: closed_form_DFT3_from_spec
  eigendecomposition_used: false
  no_mixing_residual_epsilon_independent: true
  no_mixing_tolerance_is_not_inherited_from_lateral_values: true
```

A stricter reference no-mixing tolerance is allowed and recommended:

```yaml
reference_character_basis_offdiag_tolerance: 1.0e-14
```

This keeps the no-mixing check a test of structural correctness rather than a mixed test of structural correctness and numerical conditioning.

## 7. Pairing fixture

Use character basis `[v_0, v_1, v_2]` with pairing:

```text
Q(v_i, v_j) = 1 if i + j ≡ 0 mod 3
Q(v_i, v_j) = 0 otherwise.
```

Matrix:

```text
Q = [[1, 0, 0],
     [0, 0, 1],
     [0, 1, 0]].
```

This matrix is nondegenerate:

```text
det(Q) = -1.
```

It is not positive-definite, and the harness must not use a Q-induced positive norm. All residuals should be computed in a Q-independent norm such as Frobenius norm or max-entry norm.

Pairing preservation check:

```text
D^T Q D = Q.
```

Required tolerance:

```yaml
pairing_transport_tolerance: 1.0e-12
```

## 8. Intertwining fixture

Use:

```text
H_phi^(2) = C e_0 ⊕ C e_1 ⊕ C e_2
V_A^(2)   = C v_0 ⊕ C v_1 ⊕ C v_2
E_phi^(2)(e_j) = v_j
```

In the declared character bases:

```text
M_phi^(2) = diag(1, omega, omega2)
M_A^(2)   = diag(1, omega, omega2)
E_phi^(2) = I_3
```

Required check:

```text
M_A^(2) E_phi^(2) = E_phi^(2) M_phi^(2).
```

Required tolerance:

```yaml
monodromy_compatibility_tolerance: 1.0e-12
```

Do not replace this with a commutator between unrelated source and active matrices. It is an intertwining relation through the transport map.

## 9. Stage-1 pass conditions

A fixture run passes Stage 1 iff:

```text
1. all lateral values match Section 3 within 1.0e-12;
2. all normalized additive-jump coefficients match Section 1 within 1.0e-12;
3. ||P^3 - I|| <= 1.0e-12;
4. spec(P) matches {1, omega, omega2} within 1.0e-12;
5. F^{-1} P F matches diag(1, omega, omega2) within 1.0e-12;
6. character-basis off-diagonal ratio <= 1.0e-12;
7. D^T Q D - Q has residual <= 1.0e-12;
8. M_A E - E M_phi has residual <= 1.0e-12;
9. all residual norms are Q-independent.
```

Reference implementations using the closed-form DFT-of-3 matrix should additionally satisfy:

```text
character-basis off-diagonal ratio <= 1.0e-14.
```

## 10. Expected output skeleton

```yaml
convention_id: A2-local-cuberoot-normalization-v0
fixture_id: A2-LOCAL-CUBEROOT-TV-001
test_vectors_id: sha256(specs/a2-local-cuberoot-test-vectors.md)
harness_implementation_hash: git commit hash or source-file hash
stage: "1"
target: A2_local_cuberoot
omega: {re: -0.5, im: 0.86602540378443864676}
omega2: {re: -0.5, im: -0.86602540378443864676}
sample_radii: [1.0e-3, 1.0e-6, 1.0e-9]
lateral_values_plus: object
lateral_values_minus: object
additive_jump_coefficients: object
sheet_basis_matrix: [[0,0,1],[1,0,0],[0,1,0]]
character_basis_matrix_F: object
character_basis_matrix_D: object
pairing_matrix_Q: [[1,0,0],[0,0,1],[0,1,0]]
monodromy_source_M_phi: diag(1, omega, omega2)
monodromy_active_M_A: diag(1, omega, omega2)
encoding_E_phi: identity_3
residuals:
  lateral_value_max_error: number
  additive_jump_max_error: number
  sheet_basis_cubic_error: number
  eigenvalue_max_error: number
  character_basis_offdiag_ratio: number
  character_basis_diag_max_error: number
  pairing_transport_error: number
  monodromy_compatibility_error: number
precision_policy:
  omega_source: closed_form_-1/2_plus_minus_i_sqrt3_over_2
  character_basis_F_source: closed_form_DFT3_from_spec
  eigendecomposition_used: false
  no_mixing_residual_epsilon_independent: true
  no_mixing_tolerance_is_not_inherited_from_lateral_values: true
norm_policy: Q_independent
pass: boolean
provenance:
  convention_id: A2-local-cuberoot-normalization-v0
  test_vectors_id: sha256(specs/a2-local-cuberoot-test-vectors.md)
  harness_implementation_hash: git commit hash or source-file hash
  convention_hash: string
  fixture_spec_hash: string
  harness_version: string
  generated_at: string
  output_hash: string
```

The triplet:

```text
convention_id
test_vectors_id
harness_implementation_hash
```

is mandatory. It anchors which convention was used, which fixture was run, and which implementation produced the receipt.

## 11. Stage-2 nonclaim

Passing this fixture establishes only that the Candidate-A reference fixture for the pure local A2 cube-root model is implemented correctly.

More mechanically: a passing Stage-1 run establishes that the Candidate-A readout contract is realizable on the bare local cube-root model with the fixture specified in `A2-local-cuberoot-normalization-v0` and the test vectors in `specs/a2-local-cuberoot-test-vectors.md`.

It does not establish:

```text
- that this fixture is the canonical or unique natural choice for A2;
- that the cube-root readout extends to A2 singularities appearing in larger algebraic-geometry contexts, including resolution settings or McKay correspondence with C3 subset SU(2) acting on C^2;
- that the Candidate-A picture survives at higher An for n >= 3, where the natural finite group is C_(n+1) and cohomological structure may differ;
- any I-12 template promotion;
- a P vs NP result;
- a Clay result;
- anything about the order-3 Fuss-Catalan critical branch.
```

Stage-2 attestation is required for the canonicity/naturality question and is out of scope for the Stage-1 harness.
