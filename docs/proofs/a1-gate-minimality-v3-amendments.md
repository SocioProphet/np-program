# A1 Gate Minimality — v3 Amendments

Status: amendment note / Track A1 / not a Clay claim.

This note captures the v3 mechanical refinements for the non-faithful A1 gate-minimality branch. It is intentionally narrow: it does not restate the theorem, does not alter the faithful `T2'` branch, and does not promote any A2 result.

## Amendment 1: closed-embedding justification

Replace any Step-1 wording of the form:

```text
Since G is compact and rho_spatial is continuous and injective, rho_spatial is a closed embedding...
```

with:

```text
Because G is compact and SU(2) is Hausdorff, any continuous injective
homomorphism rho_spatial: G -> SU(2) is a homeomorphism onto its image.
The image is compact, hence closed in SU(2). Thus rho_spatial identifies
G with a closed connected Lie subgroup of SU(2).
```

Cartan's theorem on closed subgroups may be cited as an equivalent structural framing, but the compact-to-Hausdorff argument is sufficient for the proof step.

## Amendment 2: terminal-object dependency fix

The endomorphism argument alone proves only that `(SU(2), rho_def)` has trivial automorphism group. It does not by itself prove terminality.

Terminality requires that every admissible object admit a unique morphism into `(SU(2), rho_def)`.

Correct replacement text:

```text
By Steps 1-5, every object of A is canonically isomorphic to
(SU(2), rho_def). It follows that (SU(2), rho_def) is terminal: for any
object X, the canonical isomorphism X -> (SU(2), rho_def) is the unique
morphism, since any morphism must intertwine the spatial representations
and is therefore the canonical isomorphism. Triviality of the endomorphism
group confirms this uniqueness.
```

Logical dependency:

```text
classification/minimality proof first;
terminality as corollary second;
trivial endomorphism group as confirmation, not primary proof.
```

This prevents the common error:

```text
trivial automorphism group => terminal object
```

which is false in general.

## Amendment 3: Spin^c extension remains open

The Spin^c extension should remain an open subclaim, not a theorem.

Recommended wording:

```text
C-4 (Spin^c extension). The complexified extension replaces Spin(3)
with Spin^c(3) = U(2), where U(2) = (SU(2) x U(1)) / Z/2 with the
diagonal Z/2 quotient. The center of U(2) is U(1); its relation to the
A1 central order-2 lift must be tracked through the diagonal quotient and
the chosen Spin^c connection. The target group for the minimal-G theorem
under a faithful map into Spin^c(3) is U(2), and a candidate minimal object
would use the defining U(2) representation twisted by an appropriate
character.
```

Required work before theorem status:

1. extend the central `Z/2` condition to the relevant `U(1)` central family;
2. reformulate polarization compatibility to track the Spin^c connection and curvature against the active pairing data;
3. state the exact morphism category before asserting any universal property.

## Nonclaims

This amendment note does not claim:

- P vs NP progress;
- a lower bound;
- any Clay result;
- an A2 theorem;
- a Spin^c minimality theorem.

It only records mechanical proof hygiene for the A1 non-faithful branch and preserves the Spin^c extension as open.