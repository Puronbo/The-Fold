# UF-020 — Simultaneous multiplication, Frobenius duality, and arithmetic reduction

## Scope

Let k be a field and
\[
R_0=k[x,y]/(x^2+y^2,\ x^2y^2).
\]
Unless stated otherwise, assume char(k) is not 2. The ordered basis is
\[
\mathcal B=(1,x,y,xy,x^2,x^2y,x^3,x^3y).
\]
This note separates three questions: what data determines this algebra, what its Gorenstein pairing contributes, and whether the construction singles out primes.

## Theorem 1 — based simultaneous multiplication is complete

Let V be an eight-dimensional k-vector space with commuting endomorphisms X,Y and a vector e such that the map
\[
\Phi:k[u,v]\longrightarrow V,\qquad f\longmapsto f(X,Y)e
\]
is surjective. Its kernel I is an ideal because X and Y commute. The induced map k[u,v]/I → V is an isomorphism of vector spaces and transports multiplication from the quotient to V by
\[
(f(X,Y)e)\cdot(g(X,Y)e)=(fg)(X,Y)e.
\]
It is well-defined: if f(X,Y)e=0, then for every g, (gf)(X,Y)e=g(X,Y)f(X,Y)e=0. Thus (V,X,Y,e) determines a unital algebra.

Moreover, if T:V→V' is an isomorphism satisfying TX=X'T, TY=Y'T, and T(e)=e', then T(f(X,Y)e)=f(X',Y')e' and hence T preserves products and the unit. Conversely, every unital algebra isomorphism gives such an intertwiner. Therefore based simultaneous similarity is equivalent to isomorphism of the generated based algebras.

For R0, take X=Mx, Y=My, e=1. The map is surjective because the displayed basis consists of monomials in x,y; it is an isomorphism because dim_k R0=8. This is a complete invariant, though deliberately a faithful encoding rather than a short classification.

**Caution.** The separate Jordan forms of X and Y, their spectra, the Hilbert function, and the dimension of the socle are coarser data. They are not substitutes for the simultaneous pair with its cyclic unit.

## Theorem 2 — explicit Frobenius pairing

Define λ:R0→k to extract the coefficient of x³y in the basis B. Then
\[
\langle a,b\rangle=\lambda(ab)
\]
is a nondegenerate associative symmetric bilinear form. In the ordered basis B its Gram matrix is the anti-diagonal permutation matrix:
\[
G_{ij}=\lambda(b_i b_j),\qquad
G=\begin{pmatrix}
0&0&0&0&0&0&0&1\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&1&0\\
0&0&0&0&1&0&0&0\\
0&0&0&1&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
1&0&0&0&0&0&0&0
\end{pmatrix}.
\]
Consequently det(G)=1 and the pairing is perfect over every field, including characteristic 2.

**Proof.** Reduce every monomial using y²=−x² and x⁴=0. Each basis monomial has exactly one complementary basis monomial whose product reduces to ±x³y; all other products have zero x³y coefficient. The signs occur in symmetric pairs, so the displayed Gram matrix follows. Its determinant is the determinant of the 8×8 reversal permutation, (−1)^{28}=1. Associativity and symmetry follow from commutativity and associativity of R0. ∎

The pairing identifies R0 with its k-linear dual as an R0-module. This independently certifies the Artin Gorenstein property already implied by the complete-intersection presentation. The socle generator x³y from UF-019 pairs nontrivially with 1.

## Theorem 3 — integral model and the exceptional characteristic

Set
\[
\mathcal R_{\mathbb Z}=\mathbb Z[x,y]/(x²+y²,x²y²).
\]
As a Z-module it is free with basis B: the same reductions y²=−x² and x⁴=0 give spanning, and the monic Gröbner basis (y²+x²,x⁴) gives independence. Base change therefore yields an eight-dimensional algebra over every field, and the Frobenius Gram determinant remains 1.

This means the local algebra's length, displayed basis, Hilbert function, one-dimensional socle, and perfect Frobenius pairing do **not** select any exceptional prime. In particular, there is no intrinsic sequence of “eigenprimes” in these invariants.

There is, however, an arithmetic distinction for the D4 quotient map
\[
(p,q)=(x²+y²,x²y²).
\]
Its Jacobian is J=4xy(x²−y²). In characteristic 2, J vanishes identically, and the signed-permutation reflection action is no longer faithful in the same way because −1=1. Thus 2 is exceptional for the quotient's differential/reflection geometry, not for the abstract eight-dimensional Frobenius algebra. For odd characteristics the coefficient 4 is invertible; this observation alone is not a claim that every global or specialized fiber behaves identically in all odd characteristics.

## Consequences and limits

1. The pair (Mx,My) plus the unit vector is complete; either Jordan form alone is not.
2. The Frobenius form is canonical only after choosing the coefficient functional λ (equivalently, a socle generator/normalization). Multiplying λ by a nonzero scalar rescales the form without changing the algebra.
3. The Hilbert function (1,2,2,2,1) and the socle dimension one are useful coarse invariants, but they do not provide a general classification theorem for all length-eight local algebras.
4. “Eigenprime” should be reserved for a separately defined spectral/arithmetic construction. A defensible candidate is a prime at which a specified integral family changes a specified invariant after reduction. For this fixed integral local algebra, the basic Frobenius invariants above have no bad prime; the quotient differential singles out 2.

## Open problem UF-020-A

Classify the fibers of the parameterized family
\[
R_{p,q}=k[x,y]/(x²+y²-p,x²y²-q)
\]
over residue characteristics ℓ, including the precise interaction between (i) the integral model, (ii) the D4 quotient map, and (iii) the trace discriminant. In particular, determine whether any odd ℓ produces additional exceptional strata after specialization of (p,q), rather than merely assuming characteristic-zero formulas persist.

## Reproducibility

Run `python3 tools/fold_simultaneous_frobenius.py`. The standard-library verifier constructs the reduction table, checks the eight basis elements, builds G, and verifies det(G)=1. It is a finite algebra check, not a proof of the general based-representation theorem.
