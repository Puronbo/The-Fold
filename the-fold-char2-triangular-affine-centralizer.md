# UF-057 — A triangular affine centralizer of the seven-dimensional subgroup

## 1. The affine family

Work over a commutative algebra of characteristic two. Let
\[
C=k[x,z]/(x^4,z^2)
\]
and let U be the seven-dimensional subgroup
\[
\begin{aligned}
u(x)&=x+Ax^2+Bx^3+Cxz+Dx^2z+Ex^3z,\\
u(z)&=z+Axz+Gx^3+(B+G)x^2z+Jx^3z.
\end{aligned}
\]

Consider the triangular affine substitutions
\[
g(x)=c+ax,\qquad g(z)=d+hx+iz,
\]
where a and i are units and
\[
c^4=0,\qquad d^2=0,\qquad h^2=0.
\]
The cotangent determinant is ai, hence g is an automorphism. Writing p=a^{-1} and q=i^{-1}, its inverse is
\[
g^{-1}(x)=p(x+c),\qquad
g^{-1}(z)=q\bigl(z+d+hp(x+c)\bigr).
\]

## 2. Theorem UF-057

**Every such triangular affine automorphism centralizes U:**
\[
\boxed{gug^{-1}=u\quad\text{for every }u\in U.}
\]

This extends UF-056: the centralizer family allows arbitrary invertible diagonal scalings a,i and an independent infinitesimal z-translation d, in addition to the x-translation c and shear h.

## 3. Proof by exact substitution

For each u, substitute
\[
x\mapsto p(x+c),\qquad
z\mapsto q(z+d+hp(x+c))
\]
into the two displayed coordinate polynomials for u. Then apply g to the resulting outputs by substituting
\[
x\mapsto c+ax,\qquad z\mapsto d+hx+iz.
\]
Reduce using characteristic two and
\[
x^4=z^2=c^4=d^2=h^2=0.
\]
Using ap=iq=1, the resulting coordinate polynomials are
\[
\begin{aligned}
(gug^{-1})(x)
&=x+Ax^2+Bx^3+Cxz+Dx^2z+Ex^3z,\\
(gug^{-1})(z)
&=z+Axz+Gx^3+(B+G)x^2z+Jx^3z.
\end{aligned}
\]
These are exactly u(x) and u(z). In particular, all terms involving c,d,h cancel; the relation between the x³z coefficient of u(z) and the x³ coefficient of u(x) is not needed for this triangular affine centralizer calculation, whereas the shared A coefficient and the paired B,G coefficients are respected by the substitution.

The proof is an identity over the full truncated coefficient algebra, not only on field-valued points. The inverse is valid because a and i are units, and all reductions use defining nilpotence relations.

## 4. Consequences

1. The displayed triangular affine subgroup scheme is contained in the scheme-theoretic centralizer of U.
2. Its coordinate algebra contains mixed nilpotent products such as ch and dh, but no target coefficient of gug⁻¹ varies along this family.
3. Thus neither the presence nor absence of ch in this restricted family decides whether ch occurs in the full universal conjugation image.
4. The result does not include affine automorphisms with a z-term in g(x), nor arbitrary quadratic and cubic ambient terms. Those remain to be tested.
5. This centralizer theorem does not compute the full orbit-image ideal or its largest Hopf ideal.

## 5. Verification boundary and next question

The assertion is a finite substitution identity in
\[
k[a^{\pm1},i^{\pm1},c,d,h,A,B,C,D,E,G,J,x,z]/
(c^4,d^2,h^2,x^4,z^2),
\]
with characteristic two understood. It can be checked by direct expansion and coefficient comparison.

**Open UF-058:** add the missing off-diagonal linear term b z to g(x), preserving the full determinant-open affine family, and determine whether the mixed class ch then appears in one or more of the sixteen target coefficient functions. After that, higher ambient coefficients must be incorporated before any claim about the full conjugacy-image kernel or Hopf core.
