# UF-049 — Nilradical length and associated-graded structure

## Setup

In characteristic two, the full automorphism coordinate ring has nilpotent parameters
\[
c^4=0,\qquad d_0^2=0,\qquad h^2=0.
\]
Let \(\mathfrak n=(c,d_0,h)\) be the nilradical ideal. The other coefficient variables and the invertible determinant \(\Delta=ai-bh\) form the reduced base.

## Theorem UF-049.1 — Nilpotence order and associated graded ranks

As a module over the reduced coordinate ring, the nilpotent coefficient algebra is free with basis
\[
c^r d_0^s h^t,
\qquad 0\le r\le3,\quad 0\le s,t\le1.
\]
There are \(4\cdot2\cdot2=16\) such monomials. Their ordinary total degrees give
\[
\operatorname{Hilb}(\operatorname{gr}_{\mathfrak n}A;T)
=(1+T+T^2+T^3)(1+T)^2
=1+3T+4T^2+4T^3+3T^4+T^5.
\]
Therefore
\[
\operatorname{rank}(\mathfrak n^r/\mathfrak n^{r+1})
=(3,4,4,3,1),\qquad r=1,2,3,4,5,
\]
and
\[
\mathfrak n^5\ne0,\qquad \mathfrak n^6=0.
\]
In particular, \(c^3d_0h\) is a nonzero generator of the top graded piece.

**Proof.** The coordinate ring before determinant localization is the polynomial coefficient ring modulo the monomial ideal \((c^4,d_0^2,h^2)\). The surviving monomials in c,d₀,h are exactly those in the displayed ranges. Localization at \(\Delta\) does not annihilate any of these monomials: the determinant has nonzero reduction and is a unit on the automorphism scheme. The monomial basis and Hilbert series follow. The maximum possible total degree is \(3+1+1=5\), proving the nilpotence index statement. \(\square\)

## Crucial distinction: elementwise fourth powers versus ideal powers

For every \(r\in\mathfrak n\), characteristic-two additivity of the fourth-power map gives
\[
r^4=0.
\]
This does **not** imply \(\mathfrak n^4=0\). Products of four or five possibly distinct nilpotent factors can be nonzero; in particular \(c^3d_0h\in\mathfrak n^5\) is nonzero.

The second relative Frobenius kills the nilpotent ideal elementwise, while the ordinary ideal filtration has five nonzero positive graded pieces.

## Relation to tangent dimension

The first graded piece \(\mathfrak n/\mathfrak n^2\) has rank three, corresponding to the three extra tangent directions represented by c,d₀,h. The total rank 16 is the length of the nilpotent coefficient algebra over the reduced base; it is not the tangent dimension. The tangent dimension is obtained from the cotangent space at the identity, and its value 16 is a separate established result (UF-033).

## Consequence for the normal-closure comparison

Any comparison of the normal-closure Hopf ideal with the second-Frobenius kernel must track the full filtration
\[
A\supset\mathfrak n\supset\mathfrak n^2\supset\mathfrak n^3
\supset\mathfrak n^4\supset\mathfrak n^5\supset\mathfrak n^6=0.
\]
It is insufficient to compare only the first-order tangent space or to truncate at \(\mathfrak n^4\).

**Open UF-050:** compute the induced normal-closure and Frobenius-kernel ideals on each associated-graded piece and determine the first degree at which they differ, if any.
