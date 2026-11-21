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
Here the first term is \(H^1(k,\mu_2)\), the middle quotient is \(H^1(k,\alpha_4)\), and \(H^2(k,\mu_2)\cong\operatorname{Br}(k)[2]\). The boundary map \(\delta_\lambda\) is further analyzed in Sections 6–7 below: it factors through \(k/k^2\), and its vanishing is characterized by an explicit quadratic equation. The Brauer class is identified explicitly in Section 8.


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

The Brauer class itself is identified in Section 8.


## 7. Exact vanishing criterion for the boundary

Let \(E_\lambda\) be the rank-four extension of \(\alpha_2\) by \(\mu_2\) from Section 6. Fix an \(\alpha_2\)-torsor
\[
P_a=\operatorname{Spec}B,\qquad B=k[u]/(u^2-a).
\]
Then
\[
\boxed{\ \delta'_\lambda([a])=0
\quad\Longleftrightarrow\quad
\exists\,c,d\in k:\ c^2+a d^2+d=\lambda.\ }
\]

### Proof

A lift of \(P_a\) to an \(E_\lambda\)-torsor is a \(\mu_2\)-torsor over \(P_a\) equipped with a compatible \(E_\lambda\)-action. The ring \(B\) is local (a field or a local dual-number algebra), so \(\operatorname{Pic}(B)=0\). Every \(\mu_2\)-torsor over \(P_a\) therefore has the form
\[
Q=\operatorname{Spec}B[v]/(v^2=q(u))
\]
for a unit \(q(u)=q_0+q_1u\in B^\times\).

Write the lifted action in the form
\[
u\longmapsto u+r,\qquad
v\longmapsto vt\,\varphi(u,r),
\]
where \(r^2=0\), \(t^2=1\), and \(\varphi(u,0)=1\). Preservation of \(v^2=q(u)\) requires
\[
\varphi(u,r)^2=q(u+r)/q(u).
\]
Every square in \(B[r]/(r^2)\) has zero \(r\)-coefficient. Since
\(q(u+r)=q(u)+q_1r\), it follows that \(q_1=0\). Thus \(q=q_0\in k^\times\), and \(\varphi^2=1\), so
\[
\varphi(u,r)=1+f(u)r,\qquad f(u)=c+du.
\]

The group law in \(E_\lambda\) is
\[
(r,t)(s,t')=(r+s,tt'(1+\lambda rs)).
\]
The action law is equivalent to
\[
\varphi(u,r)\varphi(u+r,s)
=(1+\lambda rs)\varphi(u,r+s).
\]
Using \(f(u+r)=f(u)+dr\), this identity is equivalent to
\[
f(u)^2+d=\lambda.
\]
Since \(u^2=a\), this is exactly \(c^2+a d^2+d=\lambda\).

Conversely, any \(c,d\) satisfying this equation gives the action
\[
u\mapsto u+r,\qquad v\mapsto vt(1+(c+du)r)
\]
on \(B[v]/(v^2-q_0)\), for any \(q_0\in k^\times\). The canonical map is an isomorphism: its inverse recovers
\[
r=u_1+u_2,\qquad
t=(v_2/v_1)\bigl(1+(c+du_1)(u_1+u_2)\bigr).
\]
Thus the lift exists exactly under the stated condition, proving the criterion.

By Frobenius factorization, the same criterion governs
\(\delta_\lambda([a])\) for an \(\alpha_4\)-torsor \(u^4=a\). In particular, the boundary vanishes on square classes and vanishes identically if \(\lambda\in k^2\) (take \(d=0\), \(c^2=\lambda\)).

This gives the exact vanishing criterion; Section 8 identifies the full Brauer class.


## 8. Explicit quaternion Brauer class

For \(a,\lambda\in k\), define the four-dimensional algebra
\[
Q(a,\lambda)
=k\langle U,D\rangle/
(U^2=a,\ D^2=\lambda,\ DU+UD=1).
\]
It is a central simple algebra of degree two, hence a quaternion algebra.

The boundary is exactly
\[
\boxed{\ \delta'_\lambda([a])=[Q(a,\lambda)]
\in\operatorname{Br}(k)[2].\ }
\]
Consequently
\[
\boxed{\ \delta_\lambda([a]\bmod k^4)
=[Q(a,\lambda)]\ }
\]
for the \(G_\lambda\)-torsor \(u^4=a\).

### Proof by the standard \(SL_2\)-cover

In \(M_2(k)\), put
\[
D_0=\begin{pmatrix}0&\lambda\\1&0\end{pmatrix},
\qquad
N=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
Then
\[
D_0^2=\lambda I,\quad N^2=0,\quad D_0N+ND_0=I.
\]
The formula
\[
(r,t)\longmapsto t(I+rD_0)
\]
embeds \(E_\lambda\) into \(SL_2\): its determinant is one because \(r^2=0\), and multiplication reproduces
\((r,t)(s,t')=(r+s,tt'(1+\lambda rs))\).
Modulo the central scalar \(\mu_2\), this gives the subgroup
\[
\alpha_2\longrightarrow PGL_2,\qquad
r\longmapsto[I+rD_0].
\]
Thus \(E_\lambda\) is the pullback of the central extension
\[
1\longrightarrow\mu_2\longrightarrow SL_2
\longrightarrow PGL_2\longrightarrow1
\]
along this \(\alpha_2\)-subgroup. Its connecting map is therefore the Brauer class of the associated degree-two central simple algebra.

For the torsor \(P_a=\operatorname{Spec}k[u]/(u^2-a)\), the descent cocycle is represented by \(I+rD_0\), where \(r=u_2+u_1\). Over \(k[u]/(u^2-a)\), set
\[
U=uI+N,\qquad D=D_0.
\]
Conjugation by \(I+rD_0\) sends \(U\) to \(U+rI\), because \(D_0U+UD_0=I\), and fixes \(D\). These are exactly the descent transformations for \(u\mapsto u+r\). The descended algebra is generated by \(U,D\) with
\[
U^2=aI,\quad D^2=\lambda I,\quad DU+UD=I.
\]
It is \(Q(a,\lambda)\). This identifies the connecting Brauer class, not merely its zero locus.

The vanishing criterion from Section 7 is consequently an explicit splitting criterion for \(Q(a,\lambda)\):
\[
Q(a,\lambda)\cong M_2(k)
\quad\Longleftrightarrow\quad
\exists c,d\in k:\ c^2+a d^2+d=\lambda.
\]


## 9. Resulting description of the torsor classes

The nonabelian cohomology sequence is a sequence of abelian groups here because \(G_\lambda\) is commutative. The boundary formula gives
\[
0\longrightarrow k^\times/(k^\times)^2
\longrightarrow H^1_{\mathrm{fppf}}(k,G_\lambda)
\longrightarrow
\ker\!\left(
k/k^4\xrightarrow{[a]\mapsto[Q(a,\lambda)]}
\operatorname{Br}(k)[2]\right)
\longrightarrow0.
\]
Since \(G_\lambda\) is killed by two, all groups in this sequence are \(\mathbb F_2\)-vector spaces, so the sequence splits noncanonically.

Equivalently, the quotient parameter consists exactly of those fourth-power classes \([a]\) for which
\[
c^2+a d^2+d=\lambda
\]
is solvable in k. The remaining independent parameter is a square class in \(k^\times/(k^\times)^2\). When \(\lambda\in k^2\), every \([a]\in k/k^4\) is allowed.


## 10. Isomorphism criterion between parameters

For \(\lambda,\mu\in k\), the groups \(G_\lambda\) and \(G_\mu\) are isomorphic over k if and only if
\[
\boxed{\ \exists a\in k^\times:\quad
\lambda+\mu a^4\in k^2.\ }
\]
Indeed, an isomorphism must preserve the unique multiplicative-type subgroup \(\mu_2\) and induce an automorphism \(x\mapsto ax+bx^2\) of the quotient \(\alpha_4\). The lift has \(t\mapsto t(1+\beta x^2)\) over the field, and Hopf compatibility is precisely
\[
\beta^2=\lambda+\mu a^4.
\]
Conversely, any such \(a,\beta\) gives an isomorphism. The parameter b is unrestricted and does not affect the obstruction.

Thus the fixed-section extension classes \(k/k^2\) must still be quotiented by the scaling action induced by \(\operatorname{Aut}(\alpha_4)\) to obtain isomorphism classes of the total group schemes. In particular, \(\lambda\notin k^2\) guarantees \(G_\lambda\) is not isomorphic to the product \(G_0=\alpha_4\times\mu_2\).


## 11. Standard characteristic-two quaternion symbol

For \(\lambda\ne0\), the quaternion algebra \(Q(a,\lambda)\) is isomorphic to the standard characteristic-two symbol algebra
\[
[a\lambda,\lambda)_2
=k\langle I,J\rangle/
(I^2+I=a\lambda,\ J^2=\lambda,\ JI=(I+1)J).
\]
Indeed, inside \(Q(a,\lambda)\) take \(I=UD\) and \(J=D\). Then
\[
I^2+I=a\lambda,\qquad J^2=\lambda,\qquad JI=(I+1)J.
\]
Because \(\lambda\ne0\), \(D\) is invertible and \(U=ID^{-1}\), so \(I,J\) generate the full algebra. Both algebras have dimension four, hence this gives the claimed isomorphism.

Therefore, for \(\lambda\ne0\),
\[
\delta_\lambda([a])=[a\lambda,\lambda)_2.
\]
This places the Fold boundary directly in the standard characteristic-two quaternion-symbol calculus. When \(\lambda=0\), the original presentation \(Q(a,0)\) is split by the criterion of Section 7, so the boundary is zero; the standard symbol notation with second parameter zero is not used.
