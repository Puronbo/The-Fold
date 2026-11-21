# UF-023 — Explicit D4 character projectors on the Fold coinvariant algebra

## Setup and conventions

Let
\[
C=k[x,y]/(x²+y²,x²y²)
\]
with ordered basis
\[
\mathcal B=(1,x,y,xy,x²,x²y,x³,x³y).
\]
Let D4=<r,s | r⁴=s²=1, srs=r⁻¹> act by algebra automorphisms
\[
r(x,y)=(-y,x),\qquad s(x,y)=(x,-y).
\]
Write R,S for the induced linear operators on C. The action convention is substitution on the displayed generators; the matrices satisfy R⁴=S²=I and SRS=R⁻¹.

## Theorem 1 — Four explicit one-dimensional projectors

For ε,δ∈{+1,−1}, define
\[
P_{ε,δ}=\frac18
(I+εR+R²+εR³)(I+δS).
\]
These are pairwise orthogonal idempotents in End_k(C), provided char(k) is odd. Their images are the four one-dimensional character spaces with r acting by ε and s acting by δ.

**Proof.** The group-algebra element
\[
e_{ε,δ}=\frac18\sum_{a=0}^3\sum_{b=0}^1
ε^aδ^b r^a s^b
\]
is the standard primitive central idempotent for the one-dimensional character χ_{ε,δ}(r^a s^b)=ε^aδ^b. The representation map k[D4]→End_k(C) sends it to P_{ε,δ}. The standard character orthogonality relations give idempotence and pairwise orthogonality. The regular-representation decomposition of the coinvariant algebra in nonmodular characteristic (UF-022) shows each image has dimension one. ∎

## Theorem 2 — Explicit two-dimensional isotypic projector

The unique two-dimensional irreducible character has values 2 on 1, −2 on r², and 0 on the other six group elements. Its central idempotent is
\[
P_E=\frac14(2I-2R²)=\frac12(I-R²).
\]
It is an idempotent of rank four. Moreover,
\[
P_E+\sum_{ε,δ=±1}P_{ε,δ}=I,
\]
and all five projectors are pairwise orthogonal.

Thus
\[
C=\bigoplus_{ε,δ=±1}\operatorname{im}P_{ε,δ}
\;\oplus\;\operatorname{im}P_E
\]
has dimensions 1+1+1+1+4. The final summand is two copies of the irreducible E.

## Theorem 3 — What changes in characteristic two

In characteristic two, r acts by coordinate swap (x,y)↦(y,x), while s acts trivially. Hence the D4 action factors through C2. On the ordered basis B, r swaps x with y and x²y with x³, while fixing 1,xy,x²,x³y. Consequently
\[
C^{D4}=\ker(R-I)
\]
has dimension six, and R−I has rank two. As a module for the effective C2, C is the direct sum of four trivial one-dimensional modules and two copies of the two-dimensional indecomposable regular module k[C2]. It is not semisimple.

The formulas for P_{ε,δ} and P_E cannot be reduced modulo two because their denominators 8 and 2 are not invertible. This is the concrete failure of the character-projector decomposition, not a failure of the underlying eight-dimensional algebra or its Frobenius pairing.

## Interaction with multiplication

The projectors act on the vector space C, not as algebra projections in general. The D4 action is by algebra automorphisms, so multiplication is equivariant:
\[
g(ab)=(ga)(gb).
\]
Equivalently, the multiplication operators transform covariantly under conjugation; for example, R M_x R⁻¹=M_{-y} and R M_y R⁻¹=M_x. Therefore the isotypic decomposition is compatible with the multiplication tensor, but its summands need not be ideals and the projectors need not commute with Mx or My.

This distinction prevents a common overclaim: the D4 decomposition is a decomposition of the representation, not a direct-product decomposition of the algebra.

## Reproducibility and scope

Run `python3 tools/fold_d4_character_projectors.py`. The standard-library verifier constructs R,S from monomial substitution and the reduction y²=−x², x⁴=0; checks the D4 relations; builds all five projectors over exact rational arithmetic; verifies orthogonality, idempotence, completeness, and ranks; and checks the characteristic-two swap action and fixed-space dimension.

The proof that the odd-characteristic representation is regular uses the nonmodular reflection-group coinvariant theorem, as stated in UF-022. The script verifies the explicit matrices and projector identities, not that general theorem.

## Open problem UF-023-A

Construct integral matrix units for the two E copies and determine whether the multiplication tensor has a canonical normal form relative to the four one-dimensional character lines and the E-isotypic component. In particular, determine which structure constants are forced to vanish by D4 character multiplication and which couple the two E copies.
