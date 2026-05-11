# Singular Germs and the Regime Decomposition

Status: **framework spine / conditional mathematical program / not a P vs NP claim**.

This note enriches the Lawful Morphology program by placing the existing closure, monodromy, and finite-defect regimes inside a single mathematical home: the local geometry of singular germs. It also adds the missing fourth regime: Stokes / wall-crossing data.

## 1. Why the regimes are not arbitrary

The earlier framework separated lawful structure into three diagnostics:

```text
exact closure + monodromy residue + renormalized finite defect
```

That decomposition is directionally right, but it needed a structural reason. The reason is that a local singular germ carries several compatible pieces of data:

1. **Scale data.** Local exponents and algebraic branches describe the dominant scale law.
2. **Phase / monodromy data.** Analytic continuation around the singularity acts on branches and cohomology.
3. **Finite-part / defect data.** After subtracting a principal singular part or divergence, regular finite terms remain.
4. **Stokes / wall-crossing data.** Across continuation chambers, hidden or exponentially small sectors can jump; the jump constants are themselves invariants.

The working thesis becomes:

```text
lawful morphology is the transport of singular-germ data into proof, learning, search, and trust artifacts.
```

The point is not that every object in the program is literally a hypersurface singularity. The point is that the proof-character generating functions, certificate-discovery functions, and gate-dynamics observables should be analyzed by the same four projections whenever their local behavior is controlled by an isolated dominant singularity.

## 2. Local model

Let `T_phi(z)` be a proof-class generating function with isolated dominant singularity at `rho`. A schematic local expansion has the form:

```math
T_phi(z) = (z-rho)^alpha P((z-rho)^{1/N}) + Q(z-rho) + \sum_k e^{-S_k/(z-rho)^{beta_k}} R_k(z-rho)
```

where:

- `alpha` is the leading singular exponent;
- `P` is the algebraic / root expansion;
- `Q` is the analytic finite-part contribution;
- the transmonomials encode possible resurgent or exponentially small sectors;
- analytic continuation of the local branches produces monodromy.

This local object organizes the four regimes:

| Regime | Singular-germ datum | Program interpretation |
|---|---|---|
| Exact closure | algebraic scale law / local exponent | admissible morphology selected by closure |
| Phase / monodromy | branch continuation, semisimple monodromy | `chi_p`, Floquet phase, torsion sign |
| Renormalized defect | regular part after singular subtraction | finite residual, Euler/Stieltjes-style defect |
| Stokes / wall-crossing | chamber jumps, Stokes constants, alien/resurgent data | basis-change discontinuity, phase-boundary transition, topic-membrane jump |

## 3. Canonicity

The canonicity problem is the central technical risk. If the same sign or phase appears only because we manually aligned three independent constructions, the bridge is aesthetically useful but not theorem-grade.

### Definition: canonical bridge

A bridge between two regime-witnesses for `phi` is canonical if there exists a functor

```text
F: SingGerms -> BridgeData
```

such that:

1. the witnesses are images of the same germ under `F` or functors naturally derived from `F`;
2. the construction is natural under analytic continuation, rescaling, and automorphisms of the germ;
3. the construction factors through a universal object such as a local branch system, Milnor fiber, Borel transform, or resurgent algebra;
4. no auxiliary representation choice changes the resulting invariant, except by an explicitly declared natural isomorphism.

Under this definition, the current `mu_2` bridge is **nearly canonical but not fully canonical**. The `A_1` / square-root germ forces a two-sheeted branch system and a sign monodromy. The Klein-bottle and `SO(3)`/Spin representations are compatible realizations of that sign, but we still need a minimality or universality result showing why the chosen gate target is forced rather than merely convenient.

## 4. Encoding map `E_phi`

The bridge requires a functorial encoding map:

```text
E_phi: singular-germ data of T_phi -> gate / constraint data
```

A first admissible specification is:

| Source: singular germ | Target: `G = T^k x SO(3)` gate system |
|---|---|
| local exponent spectrum `{alpha_j}` | scale / phase labels on active constraints |
| branch system | active constraint sheets |
| semisimple monodromy | holonomy representation into `GL(d)` |
| unipotent/logarithmic part | counterterm or logarithmic drift register |
| finite regular part | renormalized-defect register |
| Stokes data | wall-crossing register across chambers |
| provenance of enumeration | ledger provenance of gate trajectory |

Admissibility condition:

```text
E_phi is admissible iff these correspondences commute with analytic continuation, basis change, and provenance-preserving composition.
```

This replaces informal metadata preservation with a checkable functoriality requirement.

## 5. The fourth regime: Stokes / wall-crossing closure

The previous framework missed the compatibility datum between regimes. Stokes data supplies it.

A lawful system may be stable inside a chamber but jump when an operational parameter crosses a wall: analytic continuation ray, proof-basis change, topic membrane, phase boundary, or gate-reparameterization seam. The jump itself must be ledgered.

### Stokes closure

A system has Stokes closure when chamber changes transform its regime data by discrete, reproducible jump laws.

Operational form:

```text
(chamber data before wall) --Stokes constant--> (chamber data after wall)
```

The Stokes constant or wall-crossing operator is a first-class morphological coordinate, not diagnostic noise.

## 6. Augmented proof-character generating function

The earlier proof-character generating function should be augmented with a chamber / Stokes signature variable:

```math
P_B(x,y,z,w;\zeta) = \sum_{\pi \in \Pi_B} x^{\ell(\pi)} y^{d(\pi)} z^{c(\pi)} w^{|prov(\pi)|} \zeta^{\sigma(\pi)}
```

where `sigma(pi)` records the Stokes or chamber signature of the proof artifact under declared continuation / basis-change operations.

This is the empirical object the NP Program should compute over real corpora once proof traces and basis-change morphisms are available.

## 7. Claim discipline

Permitted now:

- singular germs provide the organizing language for the four-regime decomposition;
- the `A_1` / Catalan case is the first forced test object for `mu_2` monodromy;
- `E_phi` is the central formal object to construct;
- Stokes / wall-crossing data must be added to the morphology record.

Not permitted yet:

- claiming full canonicity of the `SO(3)` gate target;
- claiming a universal theorem across all proof-class generating functions;
- claiming P vs NP movement;
- treating a convention-dependent Stokes normalization as intrinsic before conventions are fixed.

## 8. Next theorem target

The first theorem target is a gate-minimality or gate-universality statement for half-integer singularities.

Informal form:

```text
Among compact-Lie gate manifolds of the selected admissible class, SO(3) is minimal for faithful equivariant realization of the half-integer/A_1 monodromy sign on the spatial triad.
```

This statement must be sharpened: without the spatial-triad and equivariance requirements, smaller targets such as `U(1)` can represent a sign. The theorem is only plausible after the admissible class is constrained by the Lawful Learning geometry.
