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
