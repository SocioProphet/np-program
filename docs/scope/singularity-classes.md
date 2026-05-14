# Singularity Class Scope Taxonomy

Status: **scope boundary / tracked risk**.

The singular-germ framework is currently strongest for algebraic isolated singularities. This document prevents overclaiming by declaring which singularity classes are in the base theory, which require extensions, and which are out of scope until further machinery is built.

## 1. Base claim boundary

The base framework covers proof-class generating functions whose local behavior is governed by an isolated algebraic singularity, especially square-root / `A_1` germs such as the Catalan generating function.

The base framework does **not** claim to cover all analytic combinatorics, all D-finite functions, all transcendental generating functions, or all essential/irregular singular points.

## 2. Taxonomy

| Singularity type | Milnor fiber | Monodromy | Resurgence / Stokes | Framework status |
|---|---|---|---|---|
| Algebraic, isolated (`A_k`, `D_k`, `E_k`, etc.) | classical | quasi-unipotent; eigenvalues roots of unity | standard local branch/Stokes data | **Base scope. Catalan lives here.** |
| Algebraic with logarithmic factors | classical plus unipotent tracking | semisimple plus unipotent part `T = T_s T_u` | standard, with logarithmic terms | **In scope after `T_u` register is implemented.** |
| D-finite with regular singularities | partial, case-dependent | controlled by local system / regular singular monodromy | often available | **Boundary scope; case-by-case.** |
| D-finite with irregular singularities | no classical Milnor fiber in the same sense | Stokes matrices replace ordinary monodromy as primary data | primary, not auxiliary | **Extension scope; Stokes regime becomes central.** |
| Rational functions with poles only | trivial local Milnor picture | residue / pole-order data | finite-part diagnostics | **In scope for finite-defect diagnostics, not for `mu_2` bridge unless branching exists.** |
| Transcendental / essential singularities | no classical Milnor fiber | wild or non-finite branch behavior | resurgent algebra only if available | **Out of base scope. Requires separate extension.** |
| Natural-boundary behavior | no isolated singular germ | no single local monodromy object | global boundary analysis required | **Out of base scope.** |

## 3. Consequences for claims

Permitted base claim:

```text
For algebraic isolated singular germs, the regime decomposition into scale, monodromy, finite part, and Stokes/wall-crossing data is the correct organizing stack for the NP Program's proof-dynamics bridge.
```

Forbidden general claim:

```text
All proof-class generating functions admit the same Milnor-fiber / mixed-Hodge / monodromy analysis.
```

The latter is false without additional assumptions.

## 4. Tracking requirements

Every future bridge document must declare:

```text
singularity_class
local_coordinate
is_isolated
is_algebraic
has_branching
has_log_terms
has_irregular_terms
monodromy_model
stokes_model
finite_part_model
scope_status
```

A missing `singularity_class` declaration blocks promotion past candidate stage.

## 5. Catalan placement

The Catalan generating function:

```math
C(x)=\frac{1-\sqrt{1-4x}}{2x}
```

has an isolated algebraic square-root singularity at `x = 1/4`. It is therefore base-scope and is the correct first implementation target for the `mu_2` bridge.

## 6. A1 gate-minimality scope declaration

Any document invoking `A_1` gate minimality must declare which theorem branch it uses.

The default branch for faithful triad semantics is now:

```text
T2' / faithful triad action:
G = SO(3)
central sign location = auxiliary Spin(3)-structure on V_A
proof reference = docs/proofs/a1-gate-minimality-faithful.md
```

Under this branch, the central element `-I` is not an element of `G`. It is the endpoint of the lifted nontrivial loop in the auxiliary `Spin(3)` frame, evaluated through the spinor representation:

```text
zeta = sigma(gamma_tilde(1)) = -I.
```

Documents relying on the non-faithful branch must instead declare:

```text
T2 / non-faithful triad action:
G = SU(2)
central sign location = central element of G
proof reference = docs/proofs/a1-gate-minimality.md
```

Documents that are version-agnostic must declare which shared fragment they use, such as abstract `Z/2` monodromy, symplectic preservation on `V_A`, or the Catalan square-root branch convention.

## 7. Higher-Ak auxiliary-structure barrier

The faithful branch deliberately separates spatial symmetry from auxiliary spin data. This prevents a false generalization.

For `A_1`, the auxiliary `Spin(3)` structure happens to be isomorphic to the universal cover of `SO(3)`. That coincidence is not part of the general theorem template.

For `A_k` with `k > 1`, the auxiliary group must be derived from the relevant polarization space, form, and central monodromy structure. It must not be obtained by blindly taking a universal cover of the spatial symmetry group.

This is a scope barrier for `A_2` and beyond.

## 8. Primary risk

The main risk is that future proof-class generating functions will not be algebraic. If they are D-finite, irregular, transcendental, or natural-boundary objects, the framework must switch from Milnor-fiber-first analysis to Stokes/resurgence-first or another declared local/global analytic framework.

A second risk is branch ambiguity in gate-minimality semantics. A document that uses `zeta = -I` without declaring whether the sign is internal to `G` (`T2`) or auxiliary to `G` (`T2'`) is under-specified and cannot be promoted past candidate stage.

These risks are tracked as scope conditions, not as refutations of the base theory.
