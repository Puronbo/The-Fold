# UF-024 — Multiplication tensor in the D4-isotypic basis

## Explicit representation basis

Work over a field k of characteristic different from 2. In
\[
C=k[x,y]/(x²+y²,x²y²)
\]
put
\[
a=1,\quad c=x²,\quad b=xy,\quad d=x³y,
\]
and define two copies of the two-dimensional D4 representation:
\[
E_1=\operatorname{span}\{x,y\},\qquad
E_2=\operatorname{span}\{u=x³,v=-x²y\}.
\]
The ordered list (a,c,b,d,x,y,u,v) is a basis of C.

For r(x,y)=(-y,x), s(x,y)=(x,-y), the four lines have characters
\[
a:\chi_{++},\quad c:\chi_{-+},\quad
b:\chi_{--},\quad d:\chi_{+-}.
\]
Both ordered pairs (x,y) and (u,v) carry the same E matrices:
\[
R_E=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
S_E=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Thus this basis realizes the decomposition from UF-023 without needing abstract projectors.

## Theorem 1 — Complete multiplication table

All products are determined by the unit a and the following nonzero products, together with commutativity:
\[
b c=d,
\]
\[
x²=c,\qquad xy=b,\qquad y²=-c,
\]
\[
xv=-d,\qquad yu=d.
\]
Every other product among the seven non-unit basis vectors is zero.

**Proof.** Reduce monomials using y²=−x² and x⁴=0. The listed products are immediate. Every omitted product either contains x⁴ after reduction or has degree too high to survive; direct reduction verifies it is zero. Since the list has eight basis elements and the reductions preserve the defining ideal, this determines the algebra. ∎

## Theorem 2 — Equivariant selection rules

The multiplication map μ:Sym²(C)→C is D4-equivariant. The explicit table gives the following rules.

1. Products of character lines obey χ·χ'=χχ'. In this algebra the only nonzero product among nontrivial character lines is χ_{--}·χ_{-+}→χ_{+-}, represented by bc=d.
2. The symmetric square of E1 maps to the χ_{-+} and χ_{--} lines: x²=c, xy=b, y²=−c.
3. The symmetric square of E2 is zero.
4. The mixed product E1·E2 maps through the alternating determinant pairing to χ_{+-}: xv=−d and yu=d, while xu=yv=0.
5. Multiplication by b and c sends E1 into E2:
\[
b x=-v,\quad b y=-u,\qquad c x=u,\quad c y=-v.
\]
Both b and c annihilate E2, and d annihilates the maximal ideal.

These are concrete structure constants, not merely representation-theoretic possibilities. The appearance of the determinant character in E1·E2 is forced by the alternating pairing between the two multiplicity copies.

## Consequence: the algebra is not a direct product of its isotypic pieces

The character lines and E-isotypic part are vector-space summands, but multiplication couples them: for example bc=d and cx=u. Hence the D4 decomposition is not a decomposition into subalgebras or ideals. The multiplication tensor, rather than the representation alone, is the full object.

## Relation to the prime 2

The chosen integral basis and multiplication table have coefficients 0, ±1, so the algebra structure itself reduces without denominators modulo 2. What fails at 2 is the semisimple D4 character decomposition and the ability to normalize the two-dimensional projectors. Thus the table survives as an integral algebra statement even when the representation-theoretic splitting collapses.

## Open problem UF-024-A

Determine the stabilizer of this multiplication tensor inside GL(C), and compare it with the original D4 automorphism group. In particular, decide whether the signed-permutation D4 action is intrinsically recoverable from the algebra together with the chosen grading/socle data, or whether additional automorphisms enlarge the stabilizer.

## Reproducibility

Run `python3 tools/fold_d4_multiplication_tensor.py`. The standard-library verifier reduces all basis products, checks the displayed table, and verifies that the two E copies have matching generator matrices.
