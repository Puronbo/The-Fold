# UF-052 — Quadratic conjugation coaction

## 1. The subgroup parameters

For u in U, write its terms through degree two as
\[
u(x)=x+A x^2+C xz+\text{terms of degree three},
\qquad
u(z)=z+A xz+\text{terms of degree three}.
\]
The zero x² coefficient in u(z), and equality of its xz coefficient with A, are defining equations of U.

For a general g in G use
\[
X=c+ax+bz+\alpha x^2+\gamma xz+\cdots,
\qquad
Z=d_0+hx+iz+\phi x^2+\eta xz+\cdots,
\]
with \(\Delta=ai-bh\) invertible and \(c^4=d_0^2=h^2=0\).

## 2. Inverse constants to first nilpotent order

Let \(g^{-1}\) have constant coefficients \(c_-,d_-\), and linear x-coefficient of its first image \(a_-\). The identity \(g\circ g^{-1}=1\), using the constant-term coproducts from UF-051, gives
\[
c_-\equiv\frac{ic+bd_0}{\Delta},\qquad
d_-\equiv\frac{hc+ad_0}{\Delta}
\pmod{\mathfrak n^2},
\qquad
a_-\equiv\frac{i}{\Delta}\pmod{\mathfrak n}.
\]
The first two formulas solve the linear system with matrix
\(\begin{psmallmatrix}a&b\\h&i\end{psmallmatrix}\).

## 3. Coefficients after the first composition

Set \(q=g\circ u\). Direct substitution, keeping only the coefficients needed in the constant-term coproduct for \(q\circ g^{-1}\), gives
\[
\begin{aligned}
c(q)&=c,&d_0(q)&=d_0,&h(q)&=h,\\
a(q)&=a,&b(q)&=b,&i(q)&=i,\\
\alpha(q)-\alpha&=aA,&
\gamma(q)-\gamma&=aC+bA,\\
\phi(q)-\phi&=hA,&
\eta(q)-\eta&=hC+iA.
\end{aligned}
\]
All these are exact coefficient identities at the indicated degrees. Cubic coefficient differences contribute only terms of nilradical order at least three when evaluated at the inverse constants.

## 4. Theorem UF-052.1 — Universal conjugation on the quadratic nilradical layer

Use right-to-left composition and put \(gug^{-1}=q\circ g^{-1}\). Subtract the identity-composition formulas for \(g\circ g^{-1}\) from those for \(q\circ g^{-1}\). Modulo \(\mathfrak n^3\), this yields
\[
\begin{aligned}
c(gug^{-1})&\equiv
aA c_-^2+(aC+bA)c_-d_-,\\
d_0(gug^{-1})&\equiv
hA c_-^2+(hC+iA)c_-d_-,\\
h(gug^{-1})&\equiv
(hC+iA)a_-d_-.
\end{aligned}
\]
In the last line the omitted term \((hC+iA)c_-h_-\) has order at least three.

Substituting the linear inverse coefficients and using
\[
c_-^2\equiv\frac{i^2c^2}{\Delta^2},\qquad
c_-d_-\equiv\frac{ihc^2+\Delta cd_0}{\Delta^2}
\pmod{\mathfrak n^3},
\]
gives the explicit formulas
\[
\boxed{
c(gug^{-1})\equiv
\frac{aAi^2c^2+(aC+bA)(ihc^2+\Delta cd_0)}{\Delta^2}
}
\]
\[
\boxed{
d_0(gug^{-1})\equiv
\frac{hAi^2c^2+(hC+iA)(ihc^2+\Delta cd_0)}{\Delta^2}
}
\]
and
\[
\boxed{
h(gug^{-1})\equiv
\frac{i(hC+iA)(hc+ad_0)}{\Delta^2}
}
\qquad (\bmod\ \mathfrak n^3).
\]

These formulas are the degree-two part of the universal conjugation pullback on the three nilpotent coordinate generators. They show explicitly how the four quadratic classes
\[
c^2,\quad cd_0,\quad ch,\quad d_0h
\]
enter the conjugacy family. The displayed formulas do not by themselves compute the full orbit ideal or its largest Hopf ideal.

## 5. Scope and verification

The derivation uses exact substitution for the coefficient differences and the UF-051 coproduct identities; terms of nilpotent order at least three are discarded only after the subtraction. The result is a formula in the associated-graded degree-two layer, not an assertion about all nilpotent orders.

A useful immediate consequence is that the h-coordinate of a conjugate contains the degree-two combination
\[
i(hC+iA)(hc+ad_0)/\Delta^2,
\]
so the two classes ch and d₀h are both visible as A varies. The c and d₀ coordinates involve c² and cd₀. This is a statement about the universal conjugacy pullback; converting it into an ideal of the normal closure still requires the Hopf-core step.

## 6. Next problem UF-053

Compute the coefficient span of these three formulas as A,C vary and the reduced coefficients vary, then determine the annihilator in the four-dimensional degree-two space. Compare that annihilator with the degree-two part of the second-Frobenius candidate. Continue to distinguish the orbit-image ideal from its Hopf core.
