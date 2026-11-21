# A parameterized mixed Hopf law over imperfect fields

Let k have characteristic two and choose \(\lambda\in k\). Put \(t=1+z\), so
\[
A=k[x,t]/(x^4,t^2-1)\cong k[x,z]/(x^4,z^2).
\]
Define
\[
\Delta(x)=x\otimes1+1\otimes x,\qquad
\Delta(t)=(t\otimes t)(1+\lambda x^2\otimes x^2),
\]
with \(\epsilon(x)=0,\epsilon(t)=1\) and \(S(x)=x,S(t)=t\).

## 1. Hopf verification

The correction factor \(C(x,y)=1+\lambda x^2y^2\) is \(\mu_2\)-valued because \(C^2=1\). It is a normalized symmetric multiplicative 2-cocycle on \(\alpha_4\):
\[
C(x,y)C(x+y,w)=C(y,w)C(x,y+w).
\]
Both sides expand to
\[
1+\lambda(x^2y^2+x^2w^2+y^2w^2);
\]
all cross-products vanish by x⁴=y⁴=w⁴=0. This proves coassociativity. The relation t²=1 is preserved because \(\Delta(t)^2=1\), and x⁴=0 is preserved by the primitive coproduct. Since C(x,x)=1+\lambda x⁴=1, the antipode is S(t)=t. Thus these formulas define a commutative Hopf algebra for every \(\lambda\).

This is a central extension
\[
0\longrightarrow\mu_2\longrightarrow G_\lambda
\longrightarrow\alpha_4\longrightarrow0.
\]

## 2. Splitting criterion

A section of the quotient \(\alpha_4\) must have x-coordinate x and t-coordinate h(x), where h(0)=1 and h(x)^2=1. Every such unit is
\[
h(x)=1+\beta x^2+\gamma x^3.
\]
The section is a group homomorphism exactly when its multiplicative coboundary cancels C. Direct expansion gives
\[
h(x)h(y)h(x+y)
=1+\beta^2x^2y^2+\gamma(x^2y+xy^2)+\gamma^2x^3y^3.
\]
It equals \(C(x,y)\) exactly when \(\gamma=0\) and \(\beta^2=\lambda\). Consequently
\[
G_\lambda\cong\alpha_4\times\mu_2
\quad\text{as this extension iff}\quad
\lambda\in k^2.
\]
When \(\lambda=\beta^2\), the coordinate change \(T=t(1+\beta x^2)\) makes T group-like and splits the extension.

If \(\lambda\notin k^2\), the extension is non-split. The subgroup \(\mu_2\) is the unique subgroup of multiplicative type of rank two: any map \(\mu_2\to\alpha_4\) is trivial. Therefore a group-scheme isomorphism to the product would carry this kernel to the product's unique \(\mu_2\) factor and split the extension. Hence a nonsquare \(\lambda\) gives a group scheme not isomorphic to \(\alpha_4\times\mu_2\).

## 3. Invariants and scope

The relative Frobenius image is \(\alpha_2\), and the Frobenius kernel is \(\alpha_2\times\mu_2\). The restricted Lie 2-map has one nonzero semisimple direction, as for the product \(\alpha_4\times\mu_2\); the distinction is the non-split extension class. Thus for an imperfect field, for example \(k=\mathbb F_2(s)\) with \(\lambda=s\), this gives another Hopf structure on the same algebra, non-isomorphic to the six previously listed structures.

Over a perfect field every \(\lambda\) is a square, so this family contributes no new isomorphism class there. This is a family of extensions with a fixed quotient and kernel, not a classification of all Hopf structures or all isomorphisms between arbitrary Hopf laws.


## 4. Cocycle classes in the fixed global-section model

A normalized symmetric polynomial (mu_2)-valued cocycle on alpha_4 has the form C=1+F, where F²=0. The complete normalized symmetric basis initially allows a coefficient rho of xy, in addition to alpha, beta, lambda, delta, eps for the other five symmetric monomials. The equation F²=0 gives rho²=0; since the base is a field, rho=0. Substituting rho=0 into the cocycle identity, the remaining coefficient equations force
[
F=alpha(x^2y+xy^2)+lambda x^2y^2+alpha^2x^3y^3.
]
The terms involving alpha are the multiplicative coboundary of (h(x)=1+alpha x^3). A general allowed 1-cochain (h(x)=1+eta x^2+gamma x^3) changes the coefficient lambda by (eta^2), while gamma removes the alpha-term. Thus the extension classes in this fixed global-section polynomial-cocycle model are parameterized by
[
k/k^2.
]
The family G_lambda represents the class of lambda. This is not a classification of extensions that are not trivial as torsors over alpha_4, nor a classification of all Hopf structures on A.


## 5. Torsor-cohomology sequence and next calculation

The extension also gives the fppf cohomology sequence
\[
0\longrightarrow k^\times/(k^\times)^2
\longrightarrow H^1_{\mathrm{fppf}}(k,G_\lambda)
\longrightarrow k/k^4
\xrightarrow{\delta_\lambda}\operatorname{Br}(k)[2].
\]
Here the first term is \(H^1(k,\mu_2)\), the middle quotient is \(H^1(k,\alpha_4)\), and \(H^2(k,\mu_2)\cong\operatorname{Br}(k)[2]\). The boundary map \(\delta_\lambda\), determined by the cocycle class of lambda, has not been computed. Determining it is the next torsor problem for this family.


## 6. Frobenius factorization of the torsor obstruction

Let \(E_\lambda\) be the central extension of \(\alpha_2\) by \(\mu_2\) with cocycle
\[
C_\lambda(r,s)=1+\lambda rs.
\]
The cocycle defining \(G_\lambda\) is its pullback along relative Frobenius
\[
F:\alpha_4\longrightarrow\alpha_2,\qquad x\longmapsto x^2,
\]
because \(C_\lambda(F(x),F(y))=1+\lambda x^2y^2\). Hence \(G_\lambda\) is the pullback extension \(F^*E_\lambda\).

Naturality of the fppf connecting map gives
\[
\delta_\lambda
=\delta'_\lambda\circ F_*:
H^1(k,\alpha_4)=k/k^4
\longrightarrow H^2(k,\mu_2)=\operatorname{Br}(k)[2].
\]
Under the standard descriptions, \(F_*\) sends the class of \(a\) modulo fourth powers to the same element \(a\) modulo squares: the \(\alpha_4\)-torsor \(u^4=a\) maps to the \(\alpha_2\)-torsor \((u^2)^2=a\). Therefore \(\delta_\lambda\) depends only on the image of \(a\) in \(k/k^2\). In particular it vanishes on the subgroup \(k^2/k^4\subset k/k^4\).

The remaining arithmetic problem is now reduced to computing the connecting map \(\delta'_\lambda:k/k^2\to\operatorname{Br}(k)[2]\) for the rank-four extension \(E_\lambda\). This is a sharper problem than computing \(\delta_\lambda\) directly.
