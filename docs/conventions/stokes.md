# Stokes / Wall-Crossing Convention

Status: **committed convention v0 / scoped to the `A_1` Catalan test**.

Convention ID:

```text
A1-sauzin-normalization-v0
```

This document fixes the Stokes / wall-crossing normalization used by the Catalan `mu_2` reference implementation. The convention is deliberately narrow: it covers the square-root / `A_1` algebraic branch point used by the first test. It does not claim to settle all resurgence-normalization conventions for arbitrary singularities.

## 1. Reference spine

The notation and lateral-continuation discipline follow the Borel-Laplace / resurgence orientation used in the Mitschi-Sauzin and Sauzin reference line:

- Claude Mitschi and David Sauzin, *Divergent Series, Summability and Resurgence I: Monodromy and Resurgence*, Lecture Notes in Mathematics 2153, Springer, 2016.
- David Sauzin, *Resurgent functions and splitting problems*, RIMS Kokyuroku 1493, 2006.

The implementation convention below is a local algebraic specialization of that analytic-continuation discipline.

## 2. Local coordinate

For the Catalan germ:

```math
C(x)=\frac{1-\sqrt{1-4x}}{2x}
```

use the local coordinate:

```math
t = 1 - 4x
```

The branch point is `t = 0`. The canonical wall is the positive real `t`-ray. Lateral values are denoted by `+` and `-` sides of that ray.

## 3. Square-root normalization

The normalized square-root branch is fixed by:

```math
\sqrt{t}_{+}=+\sqrt{r}, \quad t=r>0
```

Crossing the canonical wall to the other sheet gives:

```math
\sqrt{t}_{-}=-\sqrt{r}
```

Thus the multiplicative wall-crossing invariant on the `A_1` sign line is:

```math
S^{mult}_{A_1}=-1
```

and the additive jump for the normalized generator `sqrt(t)` is:

```math
\Delta_{A_1}(\sqrt{t})=\sqrt{t}_{-}-\sqrt{t}_{+}=-2\sqrt{r}
```

The program treats `S^{mult}_{A_1}` as the hard Stokes / wall-crossing invariant for the first implementation. The additive coefficient is recorded as a secondary diagnostic.

## 4. Catalan singular part

Near `t=0`,

```math
C(x)=2-2\sqrt{t}+O(t)
```

so the singular part is:

```math
C_{sing}(t)=-2\sqrt{t}
```

Under the convention above:

```math
C_{sing,+}=-2\sqrt{r}, \quad C_{sing,-}=+2\sqrt{r}
```

and therefore:

```math
\Delta C_{sing}=C_{sing,-}-C_{sing,+}=4\sqrt{r}
```

The hard invariant remains the sheet multiplier `-1`; the Catalan-specific additive jump coefficient is `4` relative to `sqrt(r)`.

## 5. Required ledger fields

A run using this convention must record:

```text
stokes_normalization_id = A1-sauzin-normalization-v0
wall_coordinate = t = 1 - 4x
canonical_wall = positive_real_t_ray
sqrt_branch_plus = +sqrt(r)
sqrt_branch_minus = -sqrt(r)
stokes_multiplier_expected = -1
catalan_jump_coefficient_expected = 4
stokes_multiplier_observed
catalan_jump_coefficient_observed
stokes_error
```

## 6. Pass conditions

For the Catalan reference implementation:

```text
stokes_normalization_id == A1-sauzin-normalization-v0
stokes_multiplier_observed == -1
abs(catalan_jump_coefficient_observed - 4) <= tolerance
```

This removes the earlier experimental flag for the `A_1` case. Higher singularity classes require their own convention IDs before CI can treat their Stokes checks as hard pass/fail.

## 7. Scope limit

This convention does not assert a universal numerical normalization for arbitrary resurgent transseries, irregular singular points, or essential singularities. It fixes only the algebraic `A_1` wall-crossing data needed by the first `mu_2` implementation.
