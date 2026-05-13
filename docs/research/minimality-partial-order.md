# Spin-Polarized Minimality Order

Status: **definition / proof-supporting convention**.

This note fixes what “minimal” means in the `A_1` spin-polarized gate-minimality theorem. The order is not bare subgroup inclusion. The theorem concerns a structured object consisting of a spatial quotient, a spin lift, a central sign, and a polarization-preserving active representation.

## 1. Structured gate object

An `A_1` spin-polarized gate object is a tuple:

```text
X = (G_tilde, G_sp, p, rho_sp, B_A, Q_A, rho_spin, z, E_phi)
```

where:

- `p: G_tilde -> G_sp` is a compact connected Lie cover or quotient map relevant to the bridge;
- `rho_sp: G_sp -> SO(V_sp)` is the spatial-triad representation;
- `B_A` is the lifted active branch module;
- `Q_A` is the transported spin/symplectic pairing;
- `rho_spin: G_tilde -> Sp(B_A, Q_A)` is the lifted polarization-visible action;
- `z in G_tilde` is the distinguished central sign element, expected to act as `-id` on `B_A` in the `A_1` case;
- `E_phi` is the ledgered encoding from source singular data into the active branch data.

For the canonical `A_1` target:

```text
X_A1 = (SU(2), SO(3), SU(2)->SO(3), vector triad action, C^2, standard symplectic form, standard spin action, -I, E_phi)
```

## 2. Reduction morphism

Given two spin-polarized gate objects `X` and `Y`, a reduction morphism

```text
Y -> X
```

is a pair of continuous Lie homomorphisms:

```text
pi_tilde: Y_tilde -> X_tilde
pi_sp:    Y_sp    -> X_sp
```

such that the following diagrams commute:

```text
Y_tilde ----p_Y----> Y_sp
   | pi_tilde         | pi_sp
   v                  v
X_tilde ----p_X----> X_sp
```

and

```text
Y_sp ----rho_sp,Y----> SO(V_sp)
 | pi_sp                  ||
 v                        ||
X_sp ----rho_sp,X----> SO(V_sp)
```

and the lifted action is compatible:

```text
rho_spin,Y(g) on the bridge-relevant active module
  = rho_spin,X(pi_tilde(g)) after E_phi identification.
```

The central sign must be preserved:

```text
pi_tilde(z_Y) = z_X.
```

The transported pairing must be preserved:

```math
Q_Y(u,v) = Q_X(\Pi u, \Pi v)
```

on the bridge-relevant subspace, where `Pi` is the active-module map induced by the reduction.

## 3. Minimality relation

Define:

```text
X <= Y
```

when there exists a reduction morphism `Y -> X` preserving the spatial quotient, the lifted central sign, the polarization pairing, and the `E_phi`-identified branch module.

Thus `X <= Y` means: `Y` contains no bridge-relevant structure not reducible to `X`.

A gate object `X` is **minimal** in an admissible class `C` if:

```text
for every Y in C, X <= Y.
```

## 4. Application to the `A_1` theorem

The `A_1` spin-polarized minimality theorem should be read as:

```text
X_A1 = SU(2)->SO(3) is minimal under the reduction order above.
```

Equivalently, any admissible gate object must reduce to the same bridge-relevant structure:

- spatial quotient `SO(3)`,
- spin lift `SU(2)`,
- central sign `-I`,
- standard two-dimensional lifted active module,
- transported symplectic pairing.

Larger compact connected Lie groups may contain or map onto this structure, but they are not smaller or more canonical for the `A_1` bridge.

## 5. Why subgroup inclusion is wrong

Bare subgroup inclusion would incorrectly compare objects that do not carry the same quotient/lift/polarization package. For example:

- `U(1)` is a subgroup of `SU(2)` and contains `-1`, but it is abelian and fails active-set non-abelianity.
- `SO(3)` is the spatial quotient but cannot see the central `-I` as a group element.
- a larger group may act on the triad but add irrelevant degrees of freedom.

The reduction order compares the full bridge data, not group names alone.

## 6. Nonclaim

This order is defined only for the `A_1` spin-polarized bridge target. Other singularity classes may require different structured objects and therefore different minimality relations.
