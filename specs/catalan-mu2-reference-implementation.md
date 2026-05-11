# Catalan `mu_2` Reference Implementation Spec

Status: **first falsifiable toy protocol / implementation target**.

This spec defines the first concrete test case for the singular-germ regime framework. It uses the Catalan generating function because its square-root singularity forces the half-integer / `A_1` branch structure.

## 1. Purpose

A run claiming to encode the Catalan species must produce enough ledgered data to recompute:

1. the Catalan coefficient enumeration;
2. the branch / monodromy sign;
3. the gate-loop lift through `Spin(3) -> SO(3)`;
4. the chamber / Stokes signature under declared normalization.

The test validates the **instance encoding**, not the whole framework. Failure is forensic evidence of encoding drift, implementation drift, or a false normalization assumption.

## 2. Catalan germ

The Catalan generating function is:

```math
C(x) = \frac{1 - \sqrt{1-4x}}{2x}
```

Let `t = 1 - 4x`. Near the dominant singularity `x = 1/4`, the singular part is square-root type:

```math
C(x) = 2 - 2\sqrt{t} + O(t)
```

The local branch datum is therefore `A_1` / two-sheeted. The distinguished monodromy around `t = 0` sends `sqrt(t)` to `-sqrt(t)`.

## 3. Required ledger artifacts

A successful run must emit a machine-readable ledger containing:

```text
run_id
basis_id
series_truncation_N
coefficients[0..N]
branch_coordinate_t
monodromy_matrix
milnor_generator_id
gate_trajectory_SO3
gate_lift_Spin3
stokes_normalization_id
stokes_estimate
hash_chain
provenance_graph
```

## 4. Pass condition 1: coefficient enumeration

The coefficient sequence must match Catalan numbers through the declared truncation `N`:

```math
C_n = \frac{1}{n+1}\binom{2n}{n}
```

Required check:

```text
for all 0 <= n <= N: ledger.coefficients[n] == Catalan(n)
```

This is the enumeration integrity check.

## 5. Pass condition 2: monodromy sign

The implementation must compute a monodromy matrix `M_gamma` on the distinguished branch / Milnor eigendirection.

For the square-root branch, analytic continuation around `t = 0` must produce:

```math
\sqrt{t} \mapsto -\sqrt{t}
```

Required check:

```text
distinguished_eigenvalue(M_gamma) == -1
```

The eigendirection must be identified by the encoding map `E_phi`, not chosen after the fact.

## 6. Pass condition 3: Spin lift

The ledgered `SO(3)` loop must lift through:

```text
Spin(3) = SU(2) -> SO(3)
```

Required check:

```text
lift_start == I
lift_end == -I
```

This confirms that the gate trajectory represents the nontrivial element of `pi_1(SO(3)) = Z/2`.

## 7. Pass condition 4: Stokes / wall-crossing signature

The run must declare a Stokes normalization before evaluation. Stokes constants are convention-dependent, so this spec does not hard-code a universal numeric value until normalization is fixed.

Required check:

```text
stokes_normalization_id is declared
stokes_estimate is reproducible from the truncated/Borel data under that normalization
stokes_error <= declared_tolerance
```

Recommended initial normalization target:

```text
A1-canonical-normalization-v0
```

A separate conventions document must define this normalization before CI treats the Stokes check as hard pass/fail.

## 8. Failure taxonomy

| Failure | Interpretation |
|---|---|
| coefficient mismatch | enumeration or basis error |
| missing eigendirection | `E_phi` incomplete |
| eigenvalue not `-1` | branch/monodromy encoding drift |
| lift does not end at `-I` | gate trajectory not the nontrivial `SO(3)` loop |
| Stokes non-reproducible | normalization, truncation, or Borel-estimation issue |
| hash-chain mismatch | provenance failure |

## 9. Minimal CI target

The first CI target should implement only deterministic checks:

1. coefficient check;
2. explicit symbolic monodromy for `sqrt(t)`;
3. synthetic `SO(3)` loop with known `Spin(3)` lift;
4. hash-chain integrity.

The Stokes check should be marked experimental until normalization is committed.

## 10. Nonclaims

Passing this test does not prove P vs NP, validate Lawful Learning, or establish the full bridge. It shows that one forced singular-germ instance can be transported through the declared morphology pipeline without losing its `mu_2` sign.
