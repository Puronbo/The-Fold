# G-EP151: Characteristic polynomial, minimal polynomial, and cyclic vectors in dimension two

This milestone tests the distinction between characteristic-polynomial agreement and operator similarity over F₂, F₃, and F₅.

For the negative control, compare the identity and the size-two Jordan block at eigenvalue one:
\[
A=I_2,\qquad B=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
They have the same characteristic polynomial \((t-1)^2\), but different rational-canonical invariant factors. The identity has two linear invariant factors \((t-1),(t-1)\); the Jordan block has the single invariant factor \((t-1)^2\). Their minimal-polynomial degrees are therefore one and two. The production rational-canonical similarity routine reports a complete negative decision.

The test independently enumerates all vectors \(v\) and checks whether the two columns \([v,Av]\) are linearly independent. No vector is cyclic for the identity, while the Jordan block has cyclic vectors. This agrees with the invariant-factor distinction and does not rely on a guessed vector.

A positive control starts with \(D=\operatorname{diag}(1,2)\) and applies a nonidentity invertible shear by conjugation. The production operator-similarity routine constructs an invertible intertwiner and verifies \(PA=BP\); both operators have matching invariant factors and explicit cyclic vectors.

The tests establish these facts for the stated 2×2 examples over the three finite fields. They do not assert that characteristic-polynomial equality alone decides similarity, nor add a new similarity algorithm; they exercise the existing rational-canonical profile and witness APIs.
