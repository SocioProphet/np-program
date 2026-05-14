# Catalan `mu_2` Reference Implementation Spec

Status: **first falsifiable toy protocol / implementation target**.

This spec defines the first concrete test case for the singular-germ regime framework. It uses the Catalan generating function because its square-root singularity forces the half-integer / `A_1` branch structure.

The default theorem interpretation is now the faithful-triad branch `T2'`: `G = SO(3)` acts faithfully on the spatial triad, while the concrete `-I` sign lives in the auxiliary `Spin(3)`-structure on `V_A`. The numerical fixture is unchanged; the interpretation of the `zeta = -I` witness is sharpened.

## 1. Purpose

A run claiming to encode the Catalan species must produce enough ledgered data to recompute:

1. the Catalan coefficient enumeration;
2. the branch / monodromy sign;
3. the gate-loop lift through the auxiliary `Spin(3)` structure over the `SO(3)` loop;
4. the chamber / Stokes signature under the committed `A_1` convention.

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
theorem_branch
series_truncation_N
coefficients[0..N]
branch_coordinate_t
monodromy_matrix
milnor_generator_id
gate_trajectory_SO3
gate_lift_Spin3
auxiliary_spin_structure_id
zeta_interpretation
stokes_normalization_id
stokes_multiplier_observed
catalan_jump_coefficient_observed
stokes_error
hash_chain
provenance_graph
```

For `T2'`, the ledger must state:

```text
theorem_branch = T2_prime
zeta_interpretation = auxiliary_spin_structure_on_V_A
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

## 6. Pass condition 3: auxiliary Spin lift under T2'

The ledgered `SO(3)` loop must lift through the auxiliary spin frame:

```text
Spin(3) = SU(2) -> SO(3)
```

Required check:

```text
lift_start == I
lift_end == -I
sigma(lift_end) == -I on V_A
```

This confirms that the gate trajectory represents the nontrivial element of:

```text
pi_1(SO(3)) = Z/2
```

and that the concrete `-I` is carried by the auxiliary `Spin(3)`-structure on `V_A`, not by an element of `G = SO(3)`.

Under the non-faithful `T2` branch, the same numerical predicate may be read as a central element of `G = SU(2)`. Under `T2'`, that reading is forbidden.

## 7. Pass condition 4: Stokes / wall-crossing signature

The committed Stokes convention is:

```text
A1-sauzin-normalization-v0
```

defined in:

```text
docs/conventions/stokes.md
```

Under this convention, for `t = r > 0`:

```math
\sqrt{t}_{+}=+\sqrt{r}, \quad \sqrt{t}_{-}=-\sqrt{r}
```

The hard Stokes / wall-crossing invariant on the `A_1` sign line is:

```math
S^{mult}_{A_1}=-1
```

For the Catalan singular part `C_sing(t) = -2 sqrt(t)`, the additive jump is:

```math
C_{sing,-}-C_{sing,+}=4\sqrt{r}
```

Required check:

```text
stokes_normalization_id == A1-sauzin-normalization-v0
stokes_multiplier_observed == -1
abs(catalan_jump_coefficient_observed - 4) <= tolerance
```

This is now a hard pass condition for the `A_1` Catalan test. Higher singularities require their own convention IDs before hard CI checks are enabled.

## 8. Failure taxonomy

| Failure | Interpretation |
|---|---|
| coefficient mismatch | enumeration or basis error |
| missing eigendirection | `E_phi` incomplete |
| eigenvalue not `-1` | branch/monodromy encoding drift |
| lift does not end at `-I` | gate trajectory not the nontrivial `SO(3)` loop |
| `zeta = -I` recorded as element of `SO(3)` under `T2'` | theorem-branch interpretation error |
| Stokes multiplier not `-1` | wall-crossing convention or branch encoding failure |
| Catalan jump coefficient not `4` | singular-part normalization error |
| hash-chain mismatch | provenance failure |

## 9. Minimal CI target

The first CI target should implement deterministic checks:

1. coefficient check;
2. explicit symbolic monodromy for `sqrt(t)`;
3. synthetic `SO(3)` loop with known auxiliary `Spin(3)` lift;
4. `A1-sauzin-normalization-v0` Stokes / wall-crossing check;
5. theorem-branch metadata check;
6. hash-chain integrity.

## 10. Nonclaims

Passing this test does not prove P vs NP, validate Lawful Learning, or establish the full bridge. It shows that one forced singular-germ instance can be transported through the declared morphology pipeline without losing its `mu_2` sign or its declared `A_1` wall-crossing signature.

Under `T2'`, passing this test does not show that `-I` is an element of `G = SO(3)`. It shows that the nontrivial `SO(3)` loop has the declared auxiliary `Spin(3)` endpoint on `V_A`.
