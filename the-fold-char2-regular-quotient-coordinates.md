# UF-045 — Regular quotient coordinates on the full automorphism chart

## Setup

Let k have characteristic two and let
\[
C=k[x,z]/(x^4,z^2).
\]
Write a substitution on the open automorphism scheme as
\[
\begin{aligned}
X&=a x+bz+\alpha x^2+\gamma xz+\text{terms of degree at least three},\\
Z&=h x+d z+\phi x^2+\eta xz+\text{terms of degree at least three}.
\end{aligned}
\]
The linear determinant condition is that \(ad-bh\) is invertible. On the reduced subgroup, \(h=0\), and \(a,d\) are units. The formulas below are first derived on that reduced chart.

Let \(g\) be the graded linear substitution
\[
g(x)=ax+bz,\qquad g(z)=dz.
\]
Composition is read right to left. Its inverse is
\[
g^{-1}(x)=a^{-1}x+\frac{b}{ad}z,
\qquad
g^{-1}(z)=d^{-1}z.
\]
For a reduced automorphism \(\varphi\), define its identity-linear factor by
\(\theta=\varphi\circ g^{-1}\). Thus \(\varphi=\theta\circ g\).

## Coordinate extraction

Substitution into the displayed degree-two terms gives
\[
\begin{aligned}
\theta(x)&=x+
\left(\frac{\alpha}{a}+\frac{b\phi}{ad}\right)x^2
+\left(\frac{\gamma}{a}+\frac{b\eta}{ad}\right)xz
+\cdots,\\
\theta(z)&=z+\frac{\phi}{d}x^2+\frac{\eta}{d}xz+\cdots.
\end{aligned}
\]
In the notation of the reduced identity-linear kernel, the coefficient of \(x^2\) in \(\theta(z)\) is \(F\), the coefficient of \(xz\) in \(\theta(z)\) is \(H\), and the coefficient of \(x^2\) in \(\theta(x)\) is \(A\). The quotient coordinates are \((F,R)=(F,H+A)\). Therefore
\[
\boxed{
F=\frac{\phi}{d},\qquad
R=\frac{\alpha}{a}+\frac{b\phi}{ad}+\frac{\eta}{d}.
}
\]
These are regular functions on the reduced chart because \(a,d\) are invertible.

## Consequence for the Frobenius construction

The second relative Frobenius on the full automorphism scheme factors through its reduction. Consequently the pullbacks of the five quotient coordinate functions on \(Q^{(2)}\) are fourth powers of their reduced-chart representatives. In particular, on this chart they are represented by
\[
a^4-1,\quad b^4,\quad d^4-1,\quad
\left(\frac{\phi}{d}\right)^4,\quad
\left(\frac{\alpha}{a}+\frac{b\phi}{ad}+\frac{\eta}{d}\right)^4.
\]
This describes the quotient-side equations in terms of substitution coefficients; it does not assert that these five displayed expressions alone generate the full ideal in the ambient coordinate ring. The ambient defining relations, determinant localization, and the nilpotent linear coefficient must still be included.

## What this resolves and what remains open

This calculation resolves a concrete part of UF-045: the quotient functions \(F,R\) are not mysterious abstract coordinates. They are explicitly recoverable from the degree-two coefficients after normalizing by the graded linear part.

It does **not** yet compute the full conjugation coaction on the ambient coordinate algebra. In particular, the coefficient \(h\), the higher-degree coefficients, and the relations among all coefficients must be retained when extending the coaction across the non-reduced directions. Nor does this calculation identify the largest conjugation-stable Hopf ideal inside the ideal of \(U\). Thus it gives an explicit chart-level input to the universal Hopf-ideal computation, not a proof that the minimal normal closure equals the second-Frobenius candidate.

## Next calculation

Write the universal substitution and its inverse in the localized coordinate algebra, then compute the pullback under
\[
(g,u)\longmapsto gug^{-1}.
\]
The target is an explicit coaction matrix on the generators of the ideal of \(U\), reduced modulo the defining relations of the full automorphism scheme. Its stable Hopf-ideal core can then be compared with the five fourth-power quotient equations.
