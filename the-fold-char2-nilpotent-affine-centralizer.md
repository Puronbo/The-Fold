# UF-056 — A nilpotent affine centralizer of the seven-dimensional subgroup

## 1. Statement

Work over a commutative algebra of characteristic two. In
\[
C=k[x,z]/(x^4,z^2),
\]
let \(U\) be the seven-parameter subgroup with
\[
\begin{aligned}
u(x)&=x+A x^2+B x^3+C xz+D x^2z+E x^3z,\\
u(z)&=z+A xz+G x^3+(B+G)x^2z+J x^3z.
\end{aligned}
\]
This is the parameterization \(F=0\), \(H_1=A\), \(I=B+G\) of the identity-linear subgroup equations.

Let \(T\) be the family
\[
g_{c,h}(x)=x+c,\qquad g_{c,h}(z)=z+hx,
\qquad c^4=0,\quad h^2=0.
\]
Its inverse is
\[
g_{c,h}^{-1}(x)=x+c,\qquad
g_{c,h}^{-1}(z)=z+hx+hc.
\]

**Theorem UF-056.** Every \(g_{c,h}\in T\) centralizes every \(u\in U\):
\[
g_{c,h}\,u\,g_{c,h}^{-1}=u.
\]
In particular, this two-parameter infinitesimal affine family contributes no new conjugates of \(U\), despite the fact that its parameters include the mixed nilpotent product \(ch\).

## 2. Exact substitution check

Use the right-to-left polynomial-map convention of the preceding notes. First substitute the inverse inputs
\[
x\longmapsto x+c,\qquad
z\longmapsto z+hx+hc
\]
into \(u(x),u(z)\), then apply \(g_{c,h}\) to the resulting outputs, i.e. substitute
\[
x\longmapsto x+c,\qquad z\longmapsto z+hx.
\]
Reduce in the coefficient-and-algebra ring by
\[
x^4=z^2=c^4=h^2=0
\]
and characteristic two. The resulting normal forms are
\[
\begin{aligned}
(gug^{-1})(x)
={}&x+A x^2+B x^3+C xz+D x^2z+E x^3z,\\
(gug^{-1})(z)
={}&z+A xz+G x^3+(B+G)x^2z+J x^3z.
\end{aligned}
\]
These are exactly the defining images of \(u\). The cancellation uses both the inverse's \(hc\) term and the relation \(I=B+G\); dropping either before substitution is not valid.

The calculation is an identity in the truncated polynomial ring, not merely an equality after setting \(c,h\) to field-valued points. It therefore applies to the full infinitesimal coefficient algebra with \(c^4=h^2=0\).

## 3. Consequences and limits

1. The subgroup family \(T\) lies in the scheme-theoretic centralizer of \(U\).
2. The mixed class \(ch\) is present in the coefficient algebra of \(T\), but this particular conjugation restriction does not detect it in any target coefficient: the entire conjugate is identically \(u\).
3. This does **not** show that \(ch\) is absent from the full universal conjugation image. General ambient automorphisms have additional linear, quadratic, and higher coefficients, and must still be included in UF-057.
4. This centralizer computation does not determine the orbit-image ideal or its largest Hopf ideal.

## 4. Verification boundary

The proof is a finite polynomial substitution in the explicitly stated quotient ring. It is independently reproducible by expanding the two displayed substitutions and discarding monomials divisible by \(x^4,z^2,c^4\), or \(h^2\), with coefficients reduced modulo two. No claim is made about the full ambient centralizer of \(U\), only the displayed family \(T\).
