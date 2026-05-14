# A1 Gate Minimality: Faithful Triad Action Version

Status: **Draft v1 / parallel faithful branch / not a Clay claim**.  
Track: A1 gate minimality.  
Theorem version: `T2_prime`.  
Relationship to non-faithful version: this is an alternative branch, not a contradiction.

This proof note holds when the triad-action condition is strengthened from:

```text
induces a nontrivial action on the triad
```

to:

```text
acts faithfully on the triad.
```

Under that strengthening, the minimal spatial group changes from `SU(2)` acting through the double cover of `SO(3)` to `SO(3)` equipped with auxiliary `Spin(3)` data on `V_A`. The two versions answer different questions about where the `-I` lives.

- Non-faithful branch `T2`: the sign lives inside `G = SU(2)`.
- Faithful branch `T2'`: the sign lives in the auxiliary `Spin(3)`-structure on `V_A`, not in `G = SO(3)`.

## 0. Categorical setup

Let `A'` denote the category whose objects are tuples

```text
(G, rho_spatial, V_A, Q_A, S, gamma)
```

where:

1. `G` is a connected compact Lie group.
2. `rho_spatial: G -> SO(3)` is faithful and nontrivial; equivalently, after identifying the image, `G` is a closed connected subgroup of `SO(3)` acting faithfully on the spatial triad.
3. `V_A` is a two-dimensional complex vector space carrying a nondegenerate symplectic form `Q_A`.
4. `S` is an auxiliary `Spin(3)`-structure on `V_A`: a homomorphism

   ```text
   sigma: Spin(3) -> Sp(V_A, Q_A) = SL(2, C)
   ```

   lifting the `SO(3)` action on orthonormal frames of the triad to a `Spin(3)` action on `V_A`.
5. `gamma in pi_1(SO(3)) = Z/2` is the distinguished nontrivial loop class.

The compatibility condition is that the `G` action on the triad, pulled back through `rho_spatial` and lifted through `sigma`, gives a well-defined projective action of `G` on `V_A` that becomes a linear action when the path is lifted to the appropriate `Spin(3)` frame.

Morphisms in `A'` are pairs `(phi, phi_tilde)` with `phi: G_1 -> G_2` intertwining the spatial representations and `phi_tilde` a compatible map of the auxiliary `Spin(3)` structures preserving `Q_A` and `gamma`.

The key ontological move relative to the non-faithful version is that `V_A` and its symplectic action are not ordinary representations of `G` inside `A'`. They are auxiliary spinor data compatible with the faithful spatial action. Under faithfulness, `G` cannot itself carry the `±I` structure; that structure must come from the auxiliary spin frame.

## 1. Theorem statements

### T1' — admissibility under faithfulness

An object

```text
(G, rho_spatial, V_A, Q_A, S, gamma) in A'
```

realizes the A1 gate semantics iff the following conditions hold.

1. **Lie regularity.** `G` is a connected compact Lie group.
2. **Faithful triad action.** `rho_spatial: G -> SO(3)` is faithful and nontrivial.
3. **Nonabelian active set.** The induced projective action on `V_A`, obtained through `rho_spatial` and the auxiliary spin structure `sigma`, is nonabelian.
4. **Coherent loop class.** The distinguished loop class `gamma in pi_1(SO(3)) = Z/2` lifts under the auxiliary spin structure to the central element `-I in Spin(3) = SU(2)`, and hence to `-I in SL(V_A)` under `sigma`.
5. **Polarization compatibility through auxiliary spin.** The form `Q_A` is preserved: `sigma(g)` is symplectic for all `g in Spin(3)`, and the induced `G` action on `P(V_A)` factors through the projective projection

   ```text
   SL(2, C) -> PSL(2, C).
   ```

### T2' — minimality under faithfulness

The class `A'` has a unique minimal object up to isomorphism:

```text
(SO(3), id_SO(3), C^2, epsilon^{ab}, sigma_spinor, gamma_can)
```

where `sigma_spinor: Spin(3) -> SL(2, C)` is the canonical spinor representation and `gamma_can` generates

```text
pi_1(SO(3)) = Z/2.
```

In particular, the central element `-I in Spin(3)` is the lift of `gamma_can`; the `-1` of the A1 gate semantics resides in the auxiliary spin structure rather than in `G` itself; and `G = SO(3)` is the smallest connected compact Lie group satisfying T1' under faithful triad action.

## 2. Proof of T2'

### Step 1 — reduce to connected compact subgroups of SO(3)

By faithfulness, `G` embeds into `SO(3)`. The connected compact subgroups of `SO(3)`, up to conjugacy, are:

```text
{e}, SO(2), SO(3).
```

The trivial group is excluded by nontriviality of the triad action. Thus the only candidates are:

```text
SO(2), SO(3).
```

### Step 2 — eliminate SO(2)

`SO(2)` is abelian. Any homomorphic image of `SO(2)` is abelian, and the induced projective action obtained through the auxiliary spin structure remains abelian. Condition (iii) requires a nonabelian active-set action. Therefore `SO(2)` is inadmissible.

The only remaining candidate is:

```text
G = SO(3).
```

### Step 3 — verify admissibility of SO(3)

Take `G = SO(3)` and `rho_spatial = id_SO(3)`.

1. `SO(3)` is connected, compact, and Lie.
2. The defining spatial representation is faithful.
3. The lifted action on `V_A` is the spinor representation of `Spin(3) = SU(2)` on `C^2`; its projective action on `P(C^2) = CP^1` is the standard nonabelian rotation action.
4. `pi_1(SO(3)) = Z/2`; the nontrivial loop lifts to the nontrivial central endpoint `-I in Spin(3)`.
5. The spinor representation preserves the canonical symplectic form `epsilon^{ab}`. In dimension two, `Sp(V_A, Q_A) = SL(2, C)`, so `sigma` takes values in the required symplectic group.

Thus `SO(3)` with the canonical auxiliary `Spin(3)` structure is admissible.

### Step 4 — the auxiliary Spin(3)-structure is necessary and unique up to the central Z/2

#### 4a. Necessity

`SO(3)` has no faithful two-dimensional complex representation.

The irreducible complex representations of `SO(3)` are indexed by integer spin `ell = 0, 1, 2, ...`, with dimensions

```text
dim V_ell = 2ell + 1.
```

All such dimensions are odd. Hence `SO(3)` has no irreducible two-dimensional complex representation. A reducible two-dimensional complex representation would be a sum of two one-dimensional representations. Since `SO(3)` is connected semisimple, those one-dimensional representations are trivial, so the reducible two-dimensional representation is not faithful.

Equivalently, in Frobenius-Schur language, the integer-spin representations of `SO(3)` are real/orthogonal type, not two-dimensional complex symplectic type.

Therefore, a faithful spatial `SO(3)` action cannot also be a faithful linear two-dimensional symplectic action on `V_A`. The action on `V_A` must instead be projective:

```text
SO(3) -> PSL(2, C),
```

and the lift to a linear symplectic action is supplied by

```text
Spin(3) = SU(2) -> SL(2, C).
```

The obstruction to such a lift is the nontrivial class in

```text
H^2(SO(3); U(1)) = Z/2.
```

The auxiliary `Spin(3)` structure resolves precisely this projective-representation obstruction.

#### 4b. Uniqueness up to ±I

Let `sigma_1` and `sigma_2` be two auxiliary `Spin(3)` structures on `(V_A, Q_A)` inducing the same projective action of `SO(3)` on `P(V_A)`. The spinor representation is irreducible, so by Schur's lemma any automorphism relating the two is scalar:

```text
sigma_2 = lambda sigma_1
```

for some `lambda in C^*`. Preservation of the symplectic form forces

```text
lambda^2 = 1,
```

so `lambda = ±1`.

Condition (iv') discriminates these two choices by requiring that the chosen lift of the loop `gamma` terminate at `-I` rather than `+I`. Thus the auxiliary spin structure is unique up to the central `Z/2`, and the A1 gate semantics choose the `-I` branch.

### Step 5 — minimality

Steps 1 and 2 force any admissible faithful spatial group to be `SO(3)`. Step 4 forces the auxiliary spin structure to be the canonical spinor representation, up to the central ambiguity fixed by condition (iv'). The remaining data are canonical: a two-dimensional complex symplectic vector space, the symplectic form `epsilon^{ab}`, and the generator of `pi_1(SO(3))`.

Therefore the minimal object of `A'` is unique up to isomorphism:

```text
(SO(3), id_SO(3), C^2, epsilon^{ab}, sigma_spinor, gamma_can).
```

This proves T2'.

## 3. Counterexamples when conditions are removed

### Remove (iii): nonabelian active set

Let `G = SO(2)` act by rotations about a fixed axis. It is faithful, connected, compact, and Lie. The auxiliary spin structure exists, but the induced action is abelian. This violates the nonabelian active-set condition.

### Remove (v'): polarization compatibility

Let `G = SO(3)` act on its standard three-dimensional real representation, with no auxiliary two-dimensional symplectic `V_A`. The abstract loop class exists, but there is no canonical concrete linear `-I` acting on `V_A`. The Stokes multiplier in the Catalan instantiation has no canonical witness.

### Remove (iv'): coherent loop class

Let `G = SO(3)` have an auxiliary spin structure that lifts the distinguished loop to `+I` rather than `-I`. Such a branch exists abstractly, but it does not realize the A1 gate semantics when the Stokes multiplier is fixed to `-1`.

A second failure mode is a stray sign: `G x U(1)` may source a `-I` from the `U(1)` factor, but that sign does not arise from the lifted spatial loop class. The sign is present but incoherent.

### Remove (ii'): faithfulness of triad action

The non-faithful version reappears. The witness is `G = SU(2)` with `rho_spatial: SU(2) -> SO(3)` the double cover, kernel `{±I}`, and `V_A` the spinor representation. This is admissible for the non-faithful branch but excluded under T2' because the triad action is not faithful.

### Remove (i): connectedness or Lie regularity

The binary icosahedral group `2I`, the preimage of `A_5 subset SO(3)` in `SU(2)`, has a central `-I` and acts nonabelianly on `V_A`. It is finite and therefore not connected. The connected Lie condition excludes it.

## 4. Structural notes

### 4.1. Where does the -I live?

In the non-faithful branch:

```text
-I in G = SU(2).
```

In the faithful branch:

```text
-I in Spin(3) auxiliary, not in G = SO(3).
```

Under T2', the `-I` is specifically

```text
sigma(gamma_tilde(1)) = -I,
```

where `gamma_tilde` is the lift of the nontrivial loop in `SO(3)` to `Spin(3)` and `sigma` is the canonical spinor representation.

Both branches are mathematically coherent. The choice is determined by what role the triad action is required to play.

### 4.2. Catalan harness contract under T2'

The five-predicate harness package

```text
Stokes = -1
Catalan jump = -4
pairing preserved
commutator = 2 sqrt(2)
zeta = -I
```

is interpreted under T2' as follows.

| Predicate | T2' interpretation |
|---|---|
| `Stokes = -1` | Tests the abstract `Z/2` monodromy in `pi_1(SO(3))`, independent of the auxiliary spin structure. |
| `Catalan jump = -4` | Quantitative witness for the same A1 sign convention; under T2' it is read through the auxiliary spin structure rather than through `G`. |
| `pairing preserved` | Tests that `sigma` takes values in `SL(V_A) = Sp(V_A, Q_A)`. |
| `commutator = 2 sqrt(2)` | Tests nonabelianness at the Lie-algebra level; `so(3)` and `spin(3)` agree infinitesimally. |
| `zeta = -I` | Tests `sigma(gamma_tilde(1)) = -I`, a statement about the auxiliary spin frame, not about an element of `G = SO(3)`. |

Thus, under T2', the harness predicates are not all internal to `G`. The `zeta` predicate is a statement about the auxiliary spin structure.

### 4.3. Comparison with the non-faithful branch

| Aspect | Non-faithful `T2` | Faithful `T2'` |
|---|---|---|
| Minimal `G` | `SU(2)` | `SO(3)` |
| Location of `-I` | central element of `G` | auxiliary `Spin(3)`, not in `G` |
| Loop class | path class in `G` | `pi_1(SO(3)) = Z/2` |
| `V_A` data | `G` representation | auxiliary `Spin(3)` representation |
| Polarization | internal to `G` | compatibility between `G` and auxiliary spin |
| Ontology | `G` knows about `-I` | `G` acts through auxiliary spin, which knows about `-I` |

The non-faithful branch asks: what is the smallest group whose own representation theory realizes the A1 semantics?

The faithful branch asks: what is the smallest group acting faithfully on the triad such that A1 semantics can be realized with auxiliary spin data?

### 4.4. Design commitment

The faithful branch is the correct default when gate semantics are phrased as:

```text
spatial symmetry group + auxiliary spinor data.
```

The non-faithful branch is the correct default when gate semantics are phrased as:

```text
one group carrying all structure internally.
```

For the current Track A roadmap, the faithful branch is the cleaner design target because it separates spatial symmetry from auxiliary spin structure and avoids falsely treating `Spin(3)` as a cover relation that generalizes automatically to higher `A_k`.

## 5. Open subclaims

### C-1' — categorical universal property under faithfulness

Under the strict morphism category above, every object is isomorphic to the minimal one, so the universal-property formulation is degenerate. A more interesting categorical statement requires a broadened category, for example allowing closed subgroups of `O(3)` and replacing auxiliary spin by pin data where appropriate.

### C-2' — Stiefel-Whitney obstruction over nontrivial bases

Over a point, the spin structure exists trivially. Over a nontrivial base, existence of spin structure is controlled by the second Stiefel-Whitney class

```text
w_2 in H^2(B; Z/2).
```

This is irrelevant for the basic algebraic A1 harness but becomes relevant for bundle, sheaf, or manifold-valued extensions.

### C-3' — cohomological projective-representation statement

The faithful version should be reformulated cohomologically: the projective representation obstruction lives in

```text
H^2(SO(3); U(1)) = Z/2.
```

The nontrivial class is resolved by passing to the auxiliary `Spin(3)` frame. This statement is required before attempting `A_2`, where the obstruction and auxiliary group will differ.

### C-4' — the ±I ambiguity

Schur uniqueness leaves a central `±I` ambiguity. The Catalan harness fixes the `-I` branch through the `Stokes = -1` convention. Future `A_k` extensions must explicitly state the analogous central-element choice rather than inheriting the A1 sign.

## 6. Load-bearing structural choices

### 6.1. Loop class location

Under T2', the loop class is genuinely

```text
gamma in pi_1(SO(3)) = Z/2.
```

The lift of this loop to `Spin(3)` is what produces `-I`.

### 6.2. Faithfulness

Faithfulness is the defining choice of the branch. If relaxed, `SU(2)` re-enters and the proof collapses back to the non-faithful theorem.

### 6.3. Representation theory of SO(3)

The proof depends on the fact that irreducible complex representations of `SO(3)` have odd dimension. If `V_A` is not two-dimensional or not complex symplectic, the elimination step changes.

### 6.4. Spin(3) is auxiliary

This is the main barrier for higher `A_k` generalization.

The `Spin(3)` appearing in T2' is an auxiliary structure on `V_A`. It happens to be isomorphic to the universal cover of `SO(3)` in the A1 case, but this coincidence is not part of the theorem statement and must not be generalized mechanically.

For `A_k` with `k > 1`, the auxiliary group may be different. The category `A'_{A_k}` must be defined from the relevant polarization space and central monodromy structure, not by blindly replacing `SO(3)` with a universal cover.

### 6.5. Morphism preservation

Morphisms in `A'` preserve all six pieces of structure:

```text
group, spatial representation, V_A, Q_A, spin structure, loop class.
```

This strictness makes the faithful category nearly singleton. A looser category may be useful for future categorical statements, but it must be declared separately.

## 7. Summary

T1' defines the admissible faithful A1 gate-semantics objects:

```text
(G, rho_spatial, V_A, Q_A, S, gamma)
```

satisfying Lie regularity, faithful triad action, nonabelian active-set action, coherent loop class, and polarization compatibility through auxiliary spin.

T2' states that the unique minimal element is:

```text
(SO(3), id_SO(3), C^2, epsilon^{ab}, sigma_spinor, gamma_can).
```

The key structural fact is:

```text
under faithfulness, -I is not an element of G; it is an element of the auxiliary Spin(3)-frame on V_A.
```

The Catalan harness's `zeta = -I` predicate tests this auxiliary structure, not the group `G` itself.

This proof does not claim P vs NP progress, a lower bound, or a Clay result. It is a theorem-input note for Track A1 gate semantics.