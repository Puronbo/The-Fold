# UF-014 — Complete D4 Classification of Analytic Semi-Invariants on the Cone

**Research question.** For the singular cone

\[
X=\{(x,y,z):z^2=x^4+y^4\},
\]

classify every convergent analytic scalar height germ transforming by a one-dimensional character of the natural square-symmetry group \(D_4\), not merely polynomial examples. Determine the exact crease divisors forced by each character and all symmetry-compatible multiplicities on those supports.

**Main result.** Let

\[
r(x,y,z)=(-y,x,z),\qquad s(x,y,z)=(y,x,z),
\]

so \(r^4=s^2=1\) and \(srs=r^{-1}\). Define invariant coordinates

\[
p=x^2+y^2,\qquad z=z,
\]

and four relative invariants

\[
\Delta_{++}=1,\quad
\Delta_{-+}=xy,\quad
\Delta_{--}=x^2-y^2,\quad
\Delta_{+-}=xy(x^2-y^2).
\]

Then **every real-analytic or complex-analytic germ** \(h\) at the cone vertex satisfying

\[
h(g\cdot q)=\chi(g)h(q)\quad(g\in D_4)
\]

for the character \(\chi(r)=\alpha,\chi(s)=\beta\in\{\pm1\}\) has a unique representation

\[
\boxed{h=\Delta_{\alpha\beta}\,F(p,z),\qquad F\in\mathbb K\{p,z\},}
\]

where \(\mathbb K=\mathbb R\) or \(\mathbb C\). Thus each scalar character space is a free rank-one module over the invariant analytic ring. This is a classification of all convergent analytic **character semi-invariants**; it does not claim that every analytic germ is a sum of one-dimensional characters (the two-dimensional irreducible representation also occurs).

## 1. The group and its four scalar characters

The generators satisfy

\[
r=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
s=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

with \(r\) of order four and \(s\) a reflection. The group has order eight and abelianization \(D_4^{\mathrm{ab}}\cong C_2\times C_2\). Hence every one-dimensional character is uniquely specified by

\[
(\alpha,\beta)=(\chi(r),\chi(s))\in\{\pm1\}^2.
\]

The four reflecting elements \(s,r^2s,rs,r^3s\) fix respectively the lines

\[
x=y,\quad x=-y,\quad x=0,\quad y=0.
\]

Their character values are \(\beta,\beta,\alpha\beta,\alpha\beta\). A semi-invariant must vanish on every reflection line whose reflection has character -1. Multiplying the distinct line equations gives exactly the four \(\Delta_{\alpha\beta}\) above.

| \((\chi(r),\chi(s))\) | Forced reflection lines | Relative invariant | Weighted degree |
|---|---|---|---:|
| \((+,+)\) | none | \(1\) | 0 |
| \((-,+)\) | \(x=0, y=0\) | \(xy\) | 2 |
| \((-,-)\) | \(x=y, x=-y\) | \(x^2-y^2\) | 2 |
| \((+,-)\) | all four | \(xy(x^2-y^2)\) | 4 |

**Correction/clarification to UF-013:** \(z\) is an example of a trivial-character function, but the relative-invariant generator of the trivial character module is \(1\), not \(z\). The distinction matters when describing the whole module.

## 2. The invariant analytic ring

The polynomial action on \((x,y)\) is the signed-permutation reflection group of type \(B_2\). In particular, \(rs\) and \(sr\) flip the two coordinates independently, and \(s\) swaps them. If an analytic germ is invariant, invariance under the coordinate flips forces it to be a convergent series in \(u=x^2,v=y^2\); invariance under the swap makes that series symmetric in \(u,v\). The local analytic symmetric-function theorem then writes it uniquely as a convergent germ in the elementary symmetric functions

\[
p=u+v=x^2+y^2,\qquad q=uv=x^2y^2.
\]

Therefore

\[
\mathbb K\{x,y\}^{D_4}=\mathbb K\{p,q\}.
\]

This is also the analytic-germ form of the reflection-group invariant-ring theorem; the explicit sign-flip/swap argument shows exactly why these two generators occur here.

On X,

\[
z^2=x^4+y^4=p^2-2q,
\qquad q=\frac{p^2-z^2}{2}.
\]

Every invariant germ on X is therefore a unique convergent germ in \(p,z\):

\[
\boxed{\mathcal O_{X,0}^{D_4}\cong\mathbb K\{p,z\}.}
\]

The quotient germ is smooth with coordinates \((p,z)\).

## 3. Every analytic germ has a unique two-term Weierstrass remainder

The defining equation of X is monic of degree two in z. Weierstrass division gives a unique representation of every analytic germ on X as

\[
h=a(x,y)+z\,b(x,y),\qquad a,b\in\mathbb K\{x,y\}.
\]

Since the group fixes z, the condition \(g^*h=\chi(g)h\) is equivalent to both a and b transforming by \(\chi\). For either coefficient, divide by the corresponding product of reflection-line equations \(\Delta_{\alpha\beta}\). The quotient is invariant, so

\[
a=\Delta_{\alpha\beta} A(p,q),\qquad
b=\Delta_{\alpha\beta} B(p,q).
\]

Using \(q=(p^2-z^2)/2\), we obtain

\[
h=\Delta_{\alpha\beta}\big(A(p,q)+zB(p,q)\big)
=\Delta_{\alpha\beta}F(p,z).
\]

Conversely every such product has the required character. Uniqueness follows from the unique Weierstrass remainder and the fact that \(\Delta\) is a non-zero-divisor in the domain \(\mathcal O_{X,0}\).

### Theorem 1 — Complete analytic character-module classification

For each one-dimensional character \(\chi_{\alpha\beta}\),

\[
\boxed{\mathcal O_{X,0}^{\chi_{\alpha\beta}}
=\Delta_{\alpha\beta}\,\mathbb K\{p,z\}.}
\]

In particular, **there are no additional analytic semi-invariants outside these four free rank-one modules**. The result includes non-polynomial convergent germs; for example, \(xy\exp(p+z)\) is a non-polynomial \((- ,+)\)-semi-invariant.

## 4. Exact zero divisors and all multiplicities on the forced support

If \(h=\Delta_{\chi}F(p,z)\) and \(F(0,0)\ne0\), then F is a unit and

\[
\operatorname{div}(h)=\operatorname{div}(\Delta_\chi).
\]

Thus all character-semi-invariant generators of this *same* divisor are exactly \(\Delta_\chi\) times invariant analytic units. If F is not a unit, it adds an invariant analytic divisor in the quotient plane \((p,z)\).

For the three nontrivial characters, the forced branches split into two D4-orbits according to the sign of z. Define the quotient branch equations

\[
Q_{c,+}=z-p,\quad Q_{c,-}=z+p,
\]

\[
Q_{d,+}=z-\frac{p}{\sqrt2},\quad
Q_{d,-}=z+\frac{p}{\sqrt2}.
\]

On X the identities are

\[
(z-p)(z+p)=-2x^2y^2,
\]

\[
\left(z-\frac p{\sqrt2}\right)
\left(z+\frac p{\sqrt2}\right)
=\frac12(x^2-y^2)^2.
\]

Therefore each Q-branch pulls back with multiplicity two on each of its two crease components.

### Theorem 2 — Complete odd multiplicity patterns on the forced branches

If an analytic semi-invariant has no extra divisor components beyond the reflection branches forced by its character, its quotient factor F must be a unit times powers of the corresponding Q's. Hence:

- For \((- ,+)\), the four coordinate branches form two orbits; their multiplicities are independently \(1+2k_{c,+}\) and \(1+2k_{c,-}\).
- For \((- ,- )\), the four diagonal branches form two orbits; their multiplicities are independently \(1+2k_{d,+}\) and \(1+2k_{d,-}\).
- For \((+ ,- )\), all eight branches occur in four orbits, with independent multiplicities \(1+2k_{c,+},1+2k_{c,-},1+2k_{d,+},1+2k_{d,-}\).

All k's are nonnegative integers, and multiplicity is constant within each D4-orbit. No even multiplicity can occur on a reflection branch for a nonzero semi-invariant with character -1 on its stabilizing reflection.

The exact general forms, up to an invariant unit, are

\[
(-,+):\quad xy\,Q_{c,+}^{k_+}Q_{c,-}^{k_-},
\]

\[
(-,-):\quad (x^2-y^2)\,Q_{d,+}^{k_+}Q_{d,-}^{k_-},
\]

\[
(+,-):\quad xy(x^2-y^2)\,Q_{c,+}^{k_+}Q_{c,-}^{k_-}
Q_{d,+}^{\ell_+}Q_{d,-}^{\ell_-}.
\]

This is a local classification on the complexified analytic cone; the corresponding real Fold crease network is obtained by taking its real locus.

## 5. Polynomial degrees and analytic completion

Give x,y weight one and z weight two. Then p and z both have weight two, and the invariant ring has weighted Hilbert series

\[
H_{\mathcal O_X^{D_4}}(t)=\frac1{(1-t^2)^2}.
\]

The four scalar character modules have Hilbert series

\[
H_{\chi_{\alpha\beta}}(t)=\frac{t^{d_{\alpha\beta}}}{(1-t^2)^2},
\quad d_{++}=0,\ d_{-+}=2,\ d_{--}=2,\ d_{+-}=4.
\]

Thus the minimal weighted degrees of nonzero scalar semi-invariants are 0, 2, 2, and 4. Passing from polynomials to convergent analytic germs changes the coefficient ring from polynomials in p,z to convergent series in p,z, but creates no new character generators.

## 6. Scope: scalar characters versus all representations

The theorem classifies exactly the scalar heights satisfying \(g^*h=\chi(g)h\) for a one-dimensional character. It does not claim the entire analytic function ring is the direct sum of these four modules. The two-dimensional irreducible representation of D4 also occurs in the regular representation of a generic orbit and contributes additional covariants. If a Fold state is allowed to transform as a vector-valued object, that is a different representation problem.

## 7. UF-014 conclusions

1. The four D4 relative invariants are not merely polynomial examples; each generates the complete convergent analytic semi-invariant module for its character.
2. The invariant analytic quotient is smooth with coordinates \((p,z)\), where \(p=x^2+y^2\).
3. The trivial-character module is generated by 1; z is simply one invariant example.
4. A prescribed reduced forced divisor has exactly the unit multiples of its relative invariant as character-compatible generators.
5. Higher odd multiplicities on forced branches are classified by independent powers of four quotient branch equations, constant on D4-orbits.
6. The exceptional lattice action from UF-013 is not enough to recover this classification; the quotient ring and the reflection stabilizers carry the missing information.

**Conclusion.** UF-014 completes the one-dimensional D4 character classification for convergent analytic scalar heights on the original cone. It identifies every analytic semi-invariant, not only polynomials, and determines all symmetry-compatible odd multiplicity patterns supported on the forced reflection branches.

## References

- C. Chevalley, “Invariants of finite groups generated by reflections,” *American Journal of Mathematics* 77 (1955), 778–782; and G. C. Shephard & J. A. Todd, “Finite unitary reflection groups,” *Canadian Journal of Mathematics* 6 (1954), 274–304. These give the polynomial invariant-ring theorem for finite reflection groups.
- The convergent analytic division used in Section 3 is the Weierstrass division theorem. See [Weierstrass preparation and division](https://openmaths.org/courses/complex-analytic-spaces-and-coherent-sheaves/the-local-ring-of-holomorphic-germs.html).
- Standard invariant theory of the signed permutation group in two variables identifies \(\mathbb K[x,y]^{D_4}=\mathbb K[x^2+y^2,x^2y^2]\); the semi-invariant divisibility proof in this note is given directly from the four reflection hyperplanes.