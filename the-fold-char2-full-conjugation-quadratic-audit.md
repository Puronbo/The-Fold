# UF-054 — Full target-coordinate audit of quadratic conjugation

## 1. Motivation and scope

UF-053 computed the degree-two coefficient module arising from the three nilpotent target coordinates (c,d_0,h) under the universal conjugation family. It found
\[
M_2^{(c,d_0,h)}=\langle c^2,cd_0,d_0h\rangle
\subset \operatorname{gr}^2_{\mathfrak n} A.
\]
This is a statement about those three coordinate functions only. It is not the coefficient module of the full conjugation morphism, and it does not determine the scheme-theoretic image ideal or its Hopf core.

The remaining target coordinates must be included before making any claim about the full degree-two image.

## 2. Why cubic terms matter

Write the identity-linear subgroup (H) in characteristic two as
\[
\begin{aligned}
u(x)&=x+A x^2+B x^3+C xz+D x^2z+E x^3z,\\
u(z)&=z+F x^2+G x^3+H_1 xz+I x^2z+J x^3z.
\end{aligned}
\]
The seven-dimensional subgroup (U\) is cut out by
\[
F=0,\qquad H_1=A,\qquad B+G+I=0.
\]
In particular, (B,G,D,E,J) are not all absent: cubic and higher terms remain among the free parameters of (U).

For a nilpotent constant (c) with (c^4=0), characteristic two gives
\[
(x+c)^3=x^3+cx^2+c^2x+c^3.
\]
Thus a cubic term evaluated at an inverse constant has order three, but its coefficient of (x) has order two. Filtering only the constant coefficient therefore does not justify discarding cubic terms when computing the other target coefficients.

A concrete test is the valid automorphism
\[
g(x)=x+c,\qquad g(z)=z,
\]
with inverse (g^{-1}=g). Under substitution, a cubic perturbation (B x^3) produces the term (B(x+c)^3), whose linear coefficient contains (Bc^2). This demonstrates the filtration issue without relying on a general inverse expansion.

## 3. What remains valid from UF-053

The previously computed formulas for the three nilpotent coordinate outputs remain statements about those outputs:
\[
[c']_2=\frac A a c^2+
\left(\frac C i+\frac{bA}{ai}\right)cd_0,
\]
\[
[d_0']_2=\frac A a cd_0,
\]
and the corrected (h')-formula in the UF-052 paper. Their coefficient module is not, by itself, the full target-coordinate coefficient module.

No conclusion is drawn here that the missing class (ch) is or is not detected by the remaining coordinates. Nor does the calculation identify the kernel of the full conjugation pullback.

## 4. Exact next calculation

For every target coefficient
\[
a,b,\alpha,\beta,\gamma,\delta,\epsilon,
\quad
i,\phi,\psi,\eta,\theta,\kappa,
\]
compute the coefficient of each basis monomial in
\[
g\circ u\circ g^{-1}
\]
through nilradical degree two, retaining all seven free parameters of (U) and the non-reduced ambient coefficients (c,d_0,h).

The calculation should be organized as follows:

1. Use the exact (U)-parameterization, including its cubic terms and the relation (B+G+I=0).
2. Compute (g\circ u-g) as polynomial maps, not merely their constant coefficients.
3. Substitute the full inverse (g^{-1}), keeping terms whose *target-coordinate coefficients* have nilradical degree at most two.
4. Extract the coefficient module in (\operatorname{gr}^2_{\mathfrak n}A) for all target coordinates.
5. Only then compute the annihilator and distinguish it from the kernel ideal of the conjugation pullback.
6. Finally determine the largest Hopf ideal contained in that kernel; this is the normal-closure problem.

## 5. Status

**Established:** cubic terms can contribute to degree-two coefficients of nonconstant target coordinates. The rank-three result of UF-053 remains a valid restricted calculation for (c,d_0,h), but is insufficient to describe the full conjugation family.

**Open:** the full degree-two target-coordinate coefficient module, its annihilator, the scheme-theoretic conjugacy-image ideal, and its Hopf core.

The second-relative-Frobenius candidate remains an upper bound for the minimal normal closure; equality is not established.
