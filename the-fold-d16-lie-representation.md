# UF-029 — The D16 representation on the nonlinear automorphism Lie algebra

## Setup

Let U=Aut₁(C), C=k[x,y]/(y²+x²,x⁴), over a characteristic-zero field containing √2. Let u=Lie(U), with coordinates (a,b,c,d,e,u,v) as in UF-028. Let r be the graded automorphism
\[
r(x)=(x-y)/\sqrt2,\qquad r(y)=(x+y)/\sqrt2,
\]
and let s(x)=x, s(y)=−y. These generate the orthogonal dihedral subgroup D16 of order 16 in UF-025.

The action on u is conjugation by graded automorphisms. With the convention r⋅D=rDr⁻¹, direct substitution gives the following.

## Theorem 1 — Generator matrices

For r:
\[
\begin{aligned}
a'&=(a+b)/\sqrt2,&b'&=(-a+b)/\sqrt2,\\
c'&=-c/2+d+e/2,&d'&=-(c+e)/2,\\
e'&=c/2+d-e/2,\\
u'&=-(u+v)/\sqrt2,&v'&=(u-v)/\sqrt2.
\end{aligned}
\]
For s:
\[
(a,b,c,d,e,u,v)\mapsto(a,-b,c,-d,e,-u,v).
\]
The matrices satisfy r⁸=s²=I and srs=r⁻¹.

## Theorem 2 — Irreducible decomposition

Let E_j denote the real/characteristic-zero two-dimensional irreducible representation of D16 in which a generator of order eight acts as rotation through jπ/4 (up to equivalence), for j=1,2,3. Let χ be the one-dimensional representation with r↦−1 and s↦+1. Then
\[
\boxed{u\cong E_1\oplus E_2\oplus\chi\oplus E_3.}
\]

**Proof.** The (a,b)-plane is invariant and has rotation angle −π/4, hence is E₁. In the cubic parameter space, the line spanned by (c,d,e)=(-1,0,1) is fixed by s and negated by r, hence is χ. The complementary plane e=c is invariant; in coordinates (c,d) its rotation is (c,d)↦(d,−c) and its reflection is (c,d)↦(c,−d), hence E₂. Finally, the center spanned by the two socle derivations U(x)=x³y,U(y)=0 and V(x)=0,V(y)=x³y has rotation matrix
\[
\frac1{\sqrt2}\begin{pmatrix}-1&-1\\1&-1\end{pmatrix}
\]
and reflection matrix diag(−1,1), hence is E₃. The four invariant summands have dimensions 2+2+1+2=7. ∎

## Theorem 3 — Equivariance of the commutator pairing

The bracket
\[
[-,-]:\Lambda²u\longrightarrow Z(u)
\]
is D16-equivariant:
\[
[r⋅D_1,r⋅D_2]=r⋅[D_1,D_2],\qquad
[s⋅D_1,s⋅D_2]=s⋅[D_1,D_2].
\]
This follows abstractly because the action is by conjugation by algebra automorphisms, and conjugation preserves commutators. The explicit matrices and UF-028 bracket formulas also verify these identities symbolically.

The pairing is surjective and has target E₃. Its restriction to the five-dimensional quotient u/Z(u) is the central commutator form. Thus the D16 action on the center is exactly the E₃ representation, not E₁ or E₂.

## Implications

1. The nonlinear Lie algebra is multiplicity-free as a D16-module: it contains E₁, E₂, χ, and E₃ once each.
2. The center is intrinsically distinguished as [u,u], and its D16 type is E₃.
3. The quotient u/Z(u) decomposes as E₁⊕E₂⊕χ.
4. The bracket couples these components equivariantly into E₃. This is a representation-theoretic constraint on the nonlinear symmetry group, not merely a choice of coordinates.
5. The original D4 subgroup is index two in D16; restricting these representations to D4 may cause some irreducibles to become equivalent. This restriction should be analyzed separately before making claims about D4-intrinsic recovery.

## Reproducibility

Run `python3 tools/fold_d16_lie_representation.py`. It checks the dihedral relations, the invariant decomposition, and equivariance of the UF-028 bracket under both generators.

## Open problem UF-029-A

Restrict E₁,E₂,χ,E₃ to the original D4 subgroup and determine the resulting multiplicities. Then study reduction modulo odd primes, including primes where the characteristic divides 16 or the representation ceases to be semisimple. In particular, determine which primes change the isotypic decomposition of this specific Lie algebra module.
