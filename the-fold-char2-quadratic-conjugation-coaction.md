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


## 7. Correction — the h-coordinate requires the inverse h-coefficient

The displayed h-coordinate formula in Section 4 omitted the term involving the inverse coefficient h₋. The exact difference of the h-coproducts contains
\[
(hC+iA)(c_-h_-+d_-a_-),
\]
not only \((hC+iA)d_-a_-\). To first nilpotent order,
\[
c_-\equiv\frac{ic+bd_0}{\Delta},\quad
d_-\equiv\frac{hc+ad_0}{\Delta},\quad
h_-\equiv\frac h\Delta,\quad
a_-\equiv\frac i\Delta.
\]
At the lowest nonzero order this gives
\[
c_-h_-+d_-a_-
\equiv
\frac{(ic+bd_0)h+(hc+ad_0)i}{\Delta^2}
=\frac{d_0}{\Delta}
\quad\pmod{\mathfrak n^2},
\]
where \(d_0^2=h^2=0\), characteristic two, and \(ai+bh=\Delta\) were used. In particular, the apparent \(ch\) terms cancel at this order.

This calculation exposes the omission but does not determine the full expression modulo \(\mathfrak n^3\): that would require the second-order part of \(d_-\) and the corresponding inverse coefficients. Accordingly, the boxed h-coordinate formula and the claim that it independently detects both \(ch\) and \(d_0h\) in Section 4 are withdrawn pending that calculation. The c- and d₀-coordinate formulas are not affected by this specific omission.

**Revised status:** UF-052's h-coordinate result is provisional and must not be used to infer the quadratic coefficient span. UF-053 is reopened to compute the inverse coefficients to sufficient order before taking the span.


## 8. Second-order inverse expansion and corrected h-coordinate

The inverse constants can be expanded one order further. Put
\[
c_1=\frac{ic+bd_0}{\Delta},\qquad
d_1=\frac{hc+ad_0}{\Delta}.
\]
Solving the two constant equations for the inverse, the degree-two part of \(d_-\) is
\[
d_2\equiv\frac{a}{\Delta}
\left(\phi c_1^2+\eta c_1d_1\right)
\pmod{\mathfrak n^3}.
\]
The term multiplied by h in the second-row inverse matrix has degree at least three and is omitted. The inverse linear coefficients satisfy
\[
a_-\equiv\frac{i}{\Delta}\pmod{\mathfrak n}
\]
and their first correction contributes only degree at least three to \(d_-a_-\). Thus
\[
c_-h_-+d_-a_-
\equiv c_1\frac h\Delta+d_1\frac i\Delta
+d_2\frac i\Delta
\pmod{\mathfrak n^3}.
\]
The first two terms simplify to \(d_0/\Delta\), as in Section 7. Substituting
\[
c_1^2=\frac{i^2c^2}{\Delta^2},\qquad
c_1d_1=\frac{ihc^2+\Delta cd_0}{\Delta^2}
\]
gives
\[
\boxed{
c_-h_-+d_-a_-
\equiv
\frac{d_0}{\Delta}
+\frac{ai\left(\phi i^2c^2+
\eta(ihc^2+\Delta cd_0)\right)}{\Delta^4}
\pmod{\mathfrak n^3}.
}
\]
Consequently the corrected h-coordinate of the conjugate is
\[
\boxed{
h(gug^{-1})\equiv
(hC+iA)\left[
\frac{d_0}{\Delta}
+\frac{ai\left(\phi i^2c^2+
\eta(ihc^2+\Delta cd_0)\right)}{\Delta^4}
\right]
\pmod{\mathfrak n^3}.
}
\]
This replaces the earlier boxed formula in Section 4. In particular, the degree-two correction here involves c² and cd₀ (with coefficients depending on h and the reduced parameters); it does not supply independent evidence for ch or d₀h. The four-dimensional associated-graded space still has to be analyzed using the full universal pullback, including all coordinate functions, rather than only the h-coordinate.



## 9. Coupled inverse equations — replacement for Section 8

A further audit shows that Section 8 still treated \(a_-\) and \(h_-\) as though their first-order terms were determined by the linear inverse matrix alone. This is false: the exact coproducts contain the feedback term
\[
S:=c_-h_-+d_-a_-,
\]
and
\[
1=aa_-+bh_-+\gamma S,\qquad
0=ha_-+ih_-+\eta S.
\]
Thus the boxed formula in Section 8 is withdrawn as well.

The correct filtered computation is recursive. Write
\[
c_-=c_1+c_2+O(\mathfrak n^3),\quad
d_-=d_1+d_2+O(\mathfrak n^3),
\]
where the degree-one terms are
\[
c_1=\frac{ic+bd_0}{\Delta},\qquad
d_1=\frac{hc+ad_0}{\Delta}.
\]
Set
\[
Q_X=\alpha c_1^2+\gamma c_1d_1,\qquad
Q_Z=\phi c_1^2+\eta c_1d_1.
\]
The constant-term inverse equations give
\[
c_2=\frac{iQ_X+bQ_Z}{\Delta},\qquad
d_2=\frac{hQ_X+aQ_Z}{\Delta}
\equiv\frac{aQ_Z}{\Delta}\pmod{\mathfrak n^3},
\]
since h has nilpotent degree one.

For the linear inverse coefficients, write
\[
a_-=a_0+a_1+O(\mathfrak n^2),\qquad
h_-=h_1+O(\mathfrak n^2).
\]
Since \(S\) has degree-one part \(S_1=d_1/a\), the two linear coproduct equations yield
\[
a_0=\frac1a,\qquad
h_1=\frac{h+\eta d_1}{ai},\qquad
a_1=\frac{b h_1+\gamma d_1/a}{a}.
\]
Consequently the complete expression needed through degree two is
\[
\boxed{
S=c_-h_-+d_-a_-
\equiv
\frac{d_1}{a}+c_1h_1+d_1a_1+\frac{d_2}{a}
\pmod{\mathfrak n^3}.
}
\]
This is a coupled recursive formula in the full coordinate ring, with no discarded degree-two feedback terms. It replaces the simplification in Section 8. In particular, no coefficient-span conclusion for \(ch,d_0h\) is drawn until this expression is substituted into the conjugation formula and the remaining target coordinates are computed.

**Status:** the first-order inverse constants \(c_1,d_1\) remain valid. The prior explicit Section 8 expression for S and the resulting boxed h-coordinate formula are withdrawn. The recursion above is the verified filtered reduction of the exact inverse equations; further expansion and comparison with all target coordinates remain open.


## 10. Simplification and the degree-two coefficient span

The recursion in Section 9 simplifies. Using \(d_1^2=0\), one obtains
\[
d_1a_1=\frac{b d_0h}{ai\Delta},\qquad
c_1h_1=\frac{ich+bd_0h}{ai\Delta}
       +\frac{\eta c_1d_1}{ai}.
\]
Also
\[
\frac{d_2}{a}=\frac{\phi c_1^2+\eta c_1d_1}{\Delta}.
\]
The two \(\eta\)-terms combine to a multiple of \(bhc_1d_1\), hence have degree at least three. The \(bd_0h\)-terms cancel, and the \(ch\)-terms cancel against the \(hc\)-part of \(d_1/a\). Therefore
\[
\boxed{
S=c_-h_-+d_-a_-
\equiv \frac{d_0}{\Delta}
       +\frac{\phi i^2c^2}{\Delta^3}
       \pmod{\mathfrak n^3}.
}
\]
This is the simplified result of the coupled inverse system, not the earlier incomplete linear-matrix approximation.

Since the h-coordinate difference under conjugation is exactly \((hC+iA)S\), its expansion is
\[
h(gug^{-1})\equiv
\frac{iA d_0}{\Delta}
+\frac{i^3A\phi c^2}{\Delta^3}
+\frac{hC d_0}{\Delta}
\pmod{\mathfrak n^3}.
\]
For the c- and d₀-coordinates, the valid formulas of Section 4 reduce to
\[
c(gug^{-1})\equiv
\frac{aAi^2}{\Delta^2}c^2
+\frac{aC+bA}{\Delta}cd_0,
\qquad
d_0(gug^{-1})\equiv\frac{iA}{\Delta}cd_0
\pmod{\mathfrak n^3}.
\]
To read off homogeneous degree two, expand \(\Delta^{-1}\) using
\(\Delta=ai+bh\):
\[
\Delta^{-1}\equiv (ai)^{-1}
+\frac{bh}{a^2i^2}\pmod{\mathfrak n^2}.
\]
The degree-two components are therefore
\[
\begin{aligned}
[c(gug^{-1})]_2
&=\frac A a c^2+
  \left(\frac C i+\frac{bA}{ai}\right)cd_0,\\
[d_0(gug^{-1})]_2
&=\frac A a cd_0,\\
[h(gug^{-1})]_2
&=\frac{A\phi}{a^3}c^2+
  \left(\frac{Ab}{a^2i}+\frac C{ai}\right)d_0h.
\end{aligned}
\]
Here all coefficients are read in the reduced degree-zero coefficient ring. Because A and C are independent subgroup parameters and a,i are units, the coefficient module generated by these three output coordinates is exactly
\[
\boxed{
M_2=\langle c^2,\;cd_0,\;d_0h\rangle
\subset\operatorname{gr}^2_{\mathfrak n}A.
}
\]
It has rank three. The remaining basis vector \(ch\) is not detected by the degree-two parts of the three nilpotent coordinate outputs.

**Interpretation limit.** This is the coefficient span for the three coordinate functions c,d₀,h under the universal conjugation family. It is not the full orbit-image ideal: other target coordinate functions may detect additional classes. Nor is it the Hopf core or the degree-two part of the normal-closure ideal. Thus UF-053 is partially resolved, with a concrete rank-three submodule and a specific missing direction to test against the remaining coordinates.
