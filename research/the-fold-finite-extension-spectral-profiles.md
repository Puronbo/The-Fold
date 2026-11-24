# G-EP9 — finite extension arithmetic and Jordan profiles

## Construction

Let f(x) be a monic irreducible polynomial of degree d over F_p. The quotient
\[
\mathbb F_{p^d}=\mathbb F_p[x]/(f)
\]
is a field. Elements are represented in the polynomial basis by d coefficients
\((a_0,\ldots,a_{d-1})\), representing (a_0+a_1\alpha+\cdots+a_{d-1}\alpha^{d-1}), where (f(\alpha)=0).

The implementation adds:
- Rabin's irreducibility criterion for validating f;
- exact polynomial-remainder multiplication in the quotient;
- inversion by exponentiation to (p^d-2);
- exact Gaussian elimination over the extension field;
- kernel-growth Jordan profiles for matrices whose entries lie in the prime subfield, at a caller-supplied extension eigenvalue.

The extension API accepts the irreducible modulus in descending coefficient order and the eigenvalue in low-degree-first polynomial-basis coordinates.

## Example

Over F_3, (x^2+1) is irreducible, so
\[
\mathbb F_9=\mathbb F_3[\alpha]/(\alpha^2+1).
\]
The matrix
\[
A=\begin{pmatrix}0&2\\1&0\end{pmatrix}
\]
has characteristic polynomial (x^2+1). Its eigenvalue (\alpha) has a one-dimensional eigenspace over F_9. The extension Jordan routine returns nullities ((0,1,1)) and one Jordan block of size 1.

## Exactness and limits

All operations are finite-field operations; no floating point or external algebra package is used. The modulus is checked for irreducibility before the extension field is used.

This milestone does not yet find roots of higher-degree irreducible factors automatically. G-EP8 identifies those factors; G-EP9 provides the field arithmetic and profile routine once a root representation is supplied. It also does not extend the input matrix entries beyond the prime subfield.

## Tests

The unit suite now includes:
- Rabin irreducibility checks for (x^2+1) over F_3 and F_5, and (x^2+x+1) over F_2;
- an F_9 Jordan profile for the 2-by-2 companion matrix of (x^2+1);
- rejection of a reducible extension modulus.

The current GitHub Actions workflow runs the complete standard-library unittest suite on Python 3.11.


# G-EP10 — automatic extension eigenvalue classes

## Result

The full automatic spectral routine now combines G-EP7 through G-EP9:

1. Compute the characteristic polynomial exactly.
2. Factor it into monic irreducibles over F_p.
3. Profile degree-one factors directly over F_p.
4. For each irreducible factor q of degree d greater than one, construct F_(p^d)=F_p[x]/(q), take alpha=[x] as the canonical root of q, and compute the Jordan profile at alpha.

The output records one representative root per irreducible factor, its extension degree, its algebraic multiplicity per root, and the number d of Frobenius-conjugate roots represented by that class.

## Why one root represents the whole class

If A has entries in F_p and sigma is a Frobenius automorphism of a splitting field, then applying sigma entrywise to
\[
(A-\lambda I)^r v=0
\]
gives
\[
(A-\sigma(\lambda)I)^r\sigma(v)=0.
\]
Thus the kernel dimensions, and therefore the Jordan block partition, are identical for all Frobenius conjugates of lambda. A degree-d irreducible factor contributes d conjugate roots, so one quotient-field representative suffices to recover the common Jordan type.

This is a field-theoretic consequence, not a heuristic.

## CLI

Use `--auto-full` to request all irreducible eigenvalue classes, including extension-field profiles. The existing `--auto` remains a base-field-only mode, and `--eigenvalues` remains the manual profile mode.

## Example

For the matrix [[0,2],[1,0]] over F_3, the characteristic polynomial is x²+1, irreducible over F_3. Full mode constructs F_9=F_3[alpha]/(alpha²+1), profiles alpha, and records the two Frobenius-conjugate roots alpha and alpha³ with the same single size-one Jordan block.

The implementation still assumes the input matrix has entries in the prime field. A future generalization can accept matrix entries already represented in a common extension field.
