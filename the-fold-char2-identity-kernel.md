# UF-037 — The characteristic-two identity-linear kernel and the failure of normality

## 1. Coordinates for the full identity-linear kernel

Work over a field k of characteristic two with
\[
C_k=k[x,z]/(x^4,z^2),\qquad z=x+y.
\]
The maximal ideal is \(\mathfrak m=(x,z)\), and
\[
\mathfrak m^2=\langle x^2,x^3,xz,x^2z,x^3z\rangle_k.
\]

An automorphism inducing the identity on \(\mathfrak m/\mathfrak m^2\) must have the form
\[
\begin{aligned}
X={}&x+A x^2+B x^3+C xz+D x^2z+E x^3z,\\
Z={}&z+F x^2+G x^3+H xz+I x^2z+J x^3z.
\end{aligned}
\]
Every one of these ten coefficients is arbitrary. Indeed, \(X^4=0\) and \(Z^2=0\) hold automatically in this form, and the induced cotangent map is the identity, so the endomorphism is an automorphism of the finite local algebra. Thus the identity-linear kernel is the affine space
\[
H\cong\mathbb A^{10}_k.
\]

## 2. The seven-dimensional flat subgroup inside H

Reduce the integral UF-026 substitutions modulo two and change variables to \(z=x+y\). Write their seven parameters as \((a,b,c,d,u,e,v)\), in the order inherited from
\[
X=x+a x^2+bxy+c x^3+d x^2y+u x^3y,
\quad
Y=y-bx^2+a xy-dx^3+e x^2y+v x^3y.
\]
The resulting coefficients in the \((x,z)\) presentation are
\[
\begin{aligned}
X={}&x+(a+b)x^2+b xz+(c+d)x^3+d x^2z+u x^3z,\\
Z={}&z+(a+b)xz+(c+e)x^3+(d+e)x^2z+(u+v)x^3z.
\end{aligned}
\]
Consequently the image \(U_k\subset H\) is exactly the closed linear subspace cut out by
\[
\boxed{F=0,\qquad H=A,\qquad C+G+I=0.}
\]
These are three independent linear equations in the ten coordinates. Conversely, any tuple satisfying them is obtained uniquely from the seven original parameters. Hence
\[
U_k\cong\mathbb A^7_k,\qquad \dim(H)-\dim(U_k)=3.
\]
This identifies the three extra reduced directions explicitly: the coefficient \(F\) of \(x^2\) in \(Z\), the difference \(H-A\) between the \(xz\) coefficient of \(Z\) and the \(x^2\) coefficient of \(X\), and the linear combination \(C+G+I\).

## 3. Theorem UF-037.1 — The subgroup U_k is not normal in H

The inclusion \(U_k\subset H\) is not a normal-subgroup inclusion. In particular, there is no quotient group scheme \(H/U_k\) in the usual sense of quotient by a normal subgroup.

**Proof by explicit conjugation.** Consider the two automorphisms
\[
g(x)=x,\quad g(z)=z+x^2,
\]
and
\[
u(x)=x+xz,\quad u(z)=z.
\]
Both have identity linear part. The element \(u\) belongs to \(U_k\): it is obtained from the integral family by taking \(a=b=1\) and all other parameters zero. The element \(g\) belongs to \(H\).

Both are involutions in characteristic two. A direct substitution gives
\[
(g\circ u\circ g)(x)=x+xz+x^3,
\qquad
(g\circ u\circ g)(z)=z+x^2.
\]
The conjugate is still in H, but it is not in U_k because its \(Z\)-image has a nonzero \(x^2\)-coefficient \(F=1\), whereas every element of U_k has \(F=0\). Thus U_k is not normal. \(\square\)

This corrects the natural but invalid interpretation of the three-dimensional difference as a quotient *group*. The codimension is three, but the subgroup is not normal.

## 4. What the three directions do and do not mean

The three linear equations above give a canonical description of the embedded subgroup relative to the chosen coordinates \((x,z)\). They do not, by themselves, define a three-dimensional group quotient. Since U_k is not normal, the set/fppf quotient \(H/U_k\), if represented as a homogeneous space, is not a quotient group.

There is nevertheless a three-dimensional transverse parameter count. A next step is to determine whether the homogeneous space is representable and whether it admits a useful affine chart or a filtration compatible with conjugation. The conjugation example shows that any such structure must account for the nontrivial action of H on the three transverse directions.

## 5. Tangent-space warning

The ten-dimensional group H above is the reduced identity-linear subgroup over the field k. It is not the full tangent space of the characteristic-two automorphism scheme. UF-033 gives the latter dimension as 16, because three nilpotent coefficient directions in the general automorphism-scheme equations contribute additional infinitesimal directions beyond the field-valued reduced locus.

Thus the three-dimensional codimension here compares two ordinary reduced subgroups; it is not the three-dimensional smoothness defect of the full automorphism scheme.

## 6. Consequences for the research program

1. The flat integral closure \(U_{\mathbb Z}\) remains a seven-dimensional subgroup in characteristic two.
2. The full reduced identity-linear kernel is ten-dimensional and contains \(U_{\mathbb F_2}\) properly.
3. The three extra coordinates are explicitly \(F\), \(H-A\), and \(C+G+I\).
4. The inclusion is not normal, so a quotient *group* is unavailable without replacing U by a normal subgroup or taking its normal closure.
5. The next meaningful problem is the normal closure of U in H, and separately the geometry of the homogeneous space H/U.

## Reproducibility

Run:
```sh
python3 tools/fold_char2_identity_kernel.py
```
The verifier checks the seven-parameter coordinate constraints and the explicit conjugation counterexample in the truncated polynomial ring over \(\mathbb F_2\).
