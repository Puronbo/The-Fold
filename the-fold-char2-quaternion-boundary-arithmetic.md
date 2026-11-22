# G-4f — Arithmetic of the quaternion boundary over imperfect fields

Let k have characteristic two and let G_lambda be the mixed Hopf group
`0 -> mu_2 -> G_lambda -> alpha_4 -> 0` with parameter lambda in k.
Its fppf boundary is
[
\delta_\lambda:k/k^4\longrightarrow \operatorname{Br}(k)[2],
\qquad [a]\longmapsto [Q(a,\lambda)].
]
For lambda nonzero, the quaternion algebra has symbol presentation
[
Q(a,\lambda)\simeq[a\lambda,\lambda)_2.
]
The boundary factors through k/k^2. Its vanishing criterion is
[
\delta_\lambda([a])=0
\quad\Longleftrightarrow\quad
\exists c,d\in k:\ c^2+a d^2+d=\lambda.
]
This equation also constructs the lift torsor explicitly; see
`the-fold-char2-mixed-torsor-models.md`.

## 1. The image

For lambda nonzero, multiplication by lambda is a bijection of the additive
field k. Hence the image is exactly the set of quaternion classes
[
\operatorname{im}(\delta_\lambda)
=\{[b,\lambda)_2:b\in k\}
\subseteq\operatorname{Br}(k)[2].
]
Here `[b,lambda)_2` denotes the characteristic-two symbol algebra generated
by i,j with i^2+i=b, j^2=lambda, and jij^{-1}=i+1. This is a subgroup because
the boundary is a homomorphism of fppf cohomology groups. The formula is an
image description, not a claim that the parameterization by b is injective.

If lambda is a square, every symbol in this image is split, so the boundary
is zero. If lambda is nonzero and nonsquare, the image can be nonzero.

For lambda=0 the extension is split and the boundary is identically zero.

## 2. A nonzero class over a rational function field

Take
[
k=\mathbb F_2(s,t),\qquad \lambda=s,\qquad a=t.
]
Then
[
\delta_s([t])=[st,s)_2.
]
The splitting criterion would require
[
c^2+t d^2+d=s.
]
Multiplying by t and setting y=td gives
[
y^2+y=t(s+c^2).
]
Use the t-adic valuation at infinity, normalized by v(t)=-1, with residue
field F_2(s).

If v(c)<0, then v(s+c^2)=2v(c), so
v(t(s+c^2))=-1+2v(c), an odd negative integer. If v(c)>=0, the residue
of s+c^2 is nonzero: when v(c)>0 it is s, and when v(c)=0 it is
s+\bar c^2, which cannot vanish because s is not a square in F_2(s).
Thus v(t(s+c^2))=-1, again odd and negative.

But for any y with v(y)<0, v(y^2+y)=2v(y) is even and negative; if
v(y)>=0, then v(y^2+y)>=0. The displayed equation is impossible.
Therefore [st,s)_2 is nonzero in Br(k), and [t] is not in the boundary
kernel.

This is an exact valuation proof, not a numerical or symbolic sample.

## 3. Behavior under field extensions

For any extension L/k, the boundary commutes with scalar extension:
[
\delta_{\lambda,L}([a])=
\operatorname{res}_{L/k}(\delta_{\lambda,k}([a])).
]
If lambda becomes a square in L, then every symbol [a lambda,lambda)_2
splits over L, so the entire boundary map over L is zero.

In particular, adjoining sqrt(lambda) kills all these quaternion
obstructions. This is a sufficient splitting extension; it need not be
minimal for an individual class.

For purely transcendental extensions, a nonzero Brauer class remains
nonzero under restriction. Thus the class [st,s)_2 remains nonzero after
adjoining independent transcendental variables to F_2(s,t).

## 4. Exact kernel and image questions still open

The exact kernel over a general imperfect field is
[
\ker\delta_\lambda=
\{[a]\in k/k^2:
\exists c,d\in k,\ c^2+a d^2+d=\lambda\},
]
viewed inside k/k^4 by Frobenius factorization. This criterion is explicit,
but a field-uniform description in terms of valuations, norm groups, or
differential invariants remains open.

Useful next cases:
1. k=F_2(s,t) with lambda=s: classify all a for which the equation has a
   solution, not only the class a=t.
2. Finite purely inseparable extensions adjoining lambda^(1/2^n), and
   extensions that do not make lambda square.
3. One-variable function fields over imperfect coefficient fields, where
   valuations can detect nontrivial symbols.
4. Relate the kernel equation to the norm subgroup for the Artin-Schreier
   extension defined by b^2+b=a lambda, and determine when this gives a
   practical arithmetic classification.

## 5. Scope

This note computes the image description and gives a nonzero rational
function field example. It does not claim a complete classification of the
kernel for F_2(s,t), nor a complete classification over all imperfect fields.


## 6. Exact kernel parameterization for F₂(s,t), lambda=s

The splitting equation is
[
c^2+a d^2+d=s.
]
Since s is not a square in k, d cannot be zero. Put r=d^{-1}. Solving for a gives
[
a=s r^2+r+(cr)^2.
]
Thus the square class of a is [s r²+r]. Conversely, for any r in k×,
choose d=r^{-1}, c=0, and a=s r²+r; then the splitting equation holds.
Therefore
[
\boxed{\ker\delta_s
=\{[s r^2+r]\in k/k^2:r\in k^\times\}.}
]
Equivalently this is the image of the additive polynomial
L_s(r)=s r²+r, modulo k². The parameterization is invariant under changing
a by a square: such a change is absorbed into c² in the splitting equation.
It gives the entire kernel as a subset of k/k², though it does not yet give
a simpler intrinsic description of the image subspace or its quotient.

The class [t] is not in this image, by the valuation obstruction in Section 2.

## 7. G-4h — Coefficient criterion over the square subfield

Put
\[
K=k^2=\mathbb F_2(S,T),\qquad S=s^2,\quad T=t^2,
\]
so that \(K^2=k^4=\mathbb F_2(S^2,T^2)\). Every class in \(k/K\) has a unique expression
\[
[a]=\alpha s+\beta t+\gamma st,\qquad \alpha,\beta,\gamma\in K.
\]
Write \(r=r_0+r_1s+r_2t+r_3st\), with \(r_i\in K\). Since
\[
r^2=r_0^2+S r_1^2+T r_2^2+ST r_3^2\in K,
\]
the coefficient vector of \(sr^2+r\) modulo \(K\) is
\[
(r_1+r^2,\ r_2,\ r_3)
\]
in the basis \(s,t,st\). Therefore \([a]\) belongs to the boundary kernel precisely when there are \(r_0,r_1\in K\) with
\[
\beta=r_2,\quad\gamma=r_3,\quad
\alpha=r_1+r_0^2+S r_1^2+T\beta^2+ST\gamma^2.
\]
The Frobenius map \(K\to K^2\) is onto. Eliminating \(r_0\) gives the one-variable criterion
\[
\boxed{
[a]\in\ker\delta_s
\iff
\exists u\in K:\ 
\alpha+T\beta^2+ST\gamma^2+u+Su^2\in K^2.
}
\]
This is an exact equivalence: the discarded term is \(r_0^2\), and every element of \(K^2\) has a square root in \(K\).

There is also an Artin--Schreier form. Put
\[
A=\alpha+T\beta^2+ST\gamma^2,\qquad q=Su.
\]
Multiplication by \(S\) shows that the criterion is equivalent to
\[
\boxed{\exists q\in K:\quad q^2+q+SA\in S K^2.}
\]
Thus the full kernel membership question is reduced to an Artin--Schreier coset test over \(K=\mathbb F_2(S,T)\). This does not yet evaluate that test in closed form for arbitrary rational functions \(\alpha,\beta,\gamma\); in particular, it is not a claim that the image is a \(K\)-linear subspace.


## 8. G-4i — intrinsic additive quotient for the boundary image

Retain \(K=\mathbb F_2(S,T)=k^2\), with \(S=s^2\), \(T=t^2\). For
\([a]=\alpha s+\beta t+\gamma st\in k/K\), define
\[
A(a)=\alpha+T\beta^2+ST\gamma^2\in K.
\]
The expression is additive in \([a]\). The G-4h coefficient criterion says
\[
[a]\in\ker\delta_s
\iff A(a)\in K^2+L_S(K),\qquad
L_S(u)=u+Su^2.
\]
Consequently the map
\[
\Psi:k/K\longrightarrow K/(K^2+L_S(K)),\qquad
[a]\longmapsto[A(a)]
\]
is a well-defined surjective additive homomorphism: for every \(A\in K\),
\(\Psi([As])=[A]\). Its kernel is exactly \(\ker\delta_s\). The first
isomorphism theorem therefore gives the exact image structure
\[
\boxed{\operatorname{im}(\delta_s)\cong
K/(K^2+\{u+Su^2:u\in K\})}
\]
as additive groups (equivalently, \(\mathbb F_2\)-vector spaces).

Equivalently every image class has a representative symbol
\([AS,s)_2\), with two parameters giving the same class precisely when
their difference lies in \(K^2+L_S(K)\). This is an intrinsic quotient
presentation, not a dimension computation: determining the dimension or a
basis of this quotient remains open. The class \(\delta_s([t])\) corresponds
to the coset of \(T\), which is nonzero by the valuation argument in §2.


## 9. G-4j — infinite-dimensionality of the quaternion-boundary image

Let
\[
Q=K/(K^2+L_S(K)),\qquad K=\mathbb F_2(S,T),\quad
L_S(u)=u+Su^2.
\]
Use the valuation at \(T=\infty\), whose residue field is
\(\kappa=\mathbb F_2(S)\). Every element of the denominator with a pole
at infinity has even pole order. To see this, write it as
\[
z^2+u+Su^2.
\]
If \(u\) has pole order \(n>0\), then \(Su^2\) has pole order \(2n\),
strictly larger than the pole order of \(u\). The two even-order terms
\(z^2\) and \(Su^2\), if they have equal pole order, cannot cancel:
cancellation of leading coefficients would give
\(S=(\bar z/\bar u)^2\) in \(\kappa\), impossible because \(S\) is
not a square in \(\mathbb F_2(S)\). If their pole orders differ, the
larger even order survives. If \(u\) has no pole, then only \(z^2\)
can contribute a pole, and its order is even. Thus every nonzero
denominator element with a pole has even pole order.

Every nonzero finite \(\mathbb F_2\)-linear combination of
\[
T,\ T^3,\ T^5,\ T^7,\ldots
\]
has odd pole order at infinity. No such combination belongs to the
denominator. Their classes are therefore linearly independent in \(Q\),
so
\[
\boxed{\dim_{\mathbb F_2}Q=\infty.}
\]
By G-4i this proves
\[
\boxed{\dim_{\mathbb F_2}\operatorname{im}(\delta_s)=\infty.}
\]
More explicitly, the independent image classes are represented by
\([S T^{2n+1},s)_2\), for \(n\ge0\), since they correspond under the
G-4i quotient isomorphism to \([T^{2n+1}]\in Q\). Equivalently they are
the boundary values \(\delta_s([sT^{2n+1}])\). This proves infinite
rank, not a basis or a complete normal form for the quotient.


## 10. G-4k — exact countable dimension and finite-place independent family

The valuation argument of G-4j applies at every place \(v_a=v_{T-a}\),
for \(a\in\mathbb F_2(S)\). The residue field is
\(\mathbb F_2(S)\), in which \(S\) is not a square. For a denominator
element \(d=z^2+u+Su^2\), if \(u\) has a pole of order \(m>0\) at
\(v_a\), then \(Su^2\) has pole order \(2m\), strictly exceeding
the pole order \(m\) of \(u\). Its leading term cannot cancel with
that of \(z^2\), since such cancellation would make \(S\) a square
in the residue field. If \(u\) is regular, any pole comes from \(z^2\)
and has even order. Hence every denominator element has either no pole
or an even pole order at each \(v_a\).

It follows that
\[
\left\{(T-a)^{-(2n+1)}:
a\in\mathbb F_2(S),\ n\ge0\right\}
\]
is linearly independent in \(Q=K/(K^2+L_S(K))\): in a finite
nontrivial linear combination, choose a place \(v_a\) that occurs;
the largest odd pole order at that place survives, whereas all other
terms are regular there. It cannot equal a denominator element.

The indexing set is countably infinite, and \(K=\mathbb F_2(S,T)\)
is countable. Therefore
\[
\boxed{\dim_{\mathbb F_2}Q=\aleph_0
=\dim_{\mathbb F_2}\operatorname{im}(\delta_s).}
\]
Under G-4i the corresponding independent boundary representatives are
\[
\left[S(T-a)^{-(2n+1)},s\right)_2.
\]
This establishes the exact vector-space dimension, but does not give a
canonical basis or a reduction algorithm for arbitrary rational functions.


## 11. G-4l — separable-place parity obstruction

Let \(F=\mathbb F_2(S)\), \(K=F(T)\), and let \(P\in F[T]\) be monic,
irreducible, and separable. Its residue field
\(E_P=F[T]/(P)\) is finite separable over F. Since \(S\) is nonsquare
in F, adjoining \(\sqrt S\) is a nontrivial purely inseparable
extension. A finite separable extension cannot contain this element;
therefore S remains nonsquare in \(E_P\).

For \(d=z^2+u+Su^2\), consider the P-adic valuation. If u has a pole
of order m, then \(Su^2\) has pole order 2m; if z has a pole of order
n, then \(z^2\) has pole order 2n. If these orders tie, cancellation
of their leading coefficients would imply that S is a square in
\(E_P\), impossible. If they do not tie, the larger even pole order
survives. If u is regular, any pole comes from z² and is even. Thus
every denominator element has either no pole or even pole order at P.

Choose an F2-basis of E_P and polynomial representatives r(T) of
degree less than deg(P). For all such representatives and all n≥0,
the classes
\[
r(T)/P^{2n+1}
\]
are jointly linearly independent in Q, as P ranges over the monic
separable irreducibles. For a finite relation, choose a P occurring
in it and the largest n with nonzero coefficient at that P. The
corresponding residue coefficient is nonzero by basis independence,
so the relation has an odd pole order at P. Terms indexed by other
irreducibles are regular at P, and denominator elements cannot have
that odd pole order.

This refines the rational-place family in G-4k. It is still an
independent family, not a complete basis or a reduction algorithm
for Q.


## 12. G-4m — exact local parity criterion

Let P be any monic irreducible of F[T], where F=F2(S), and let
E=F[T]/(P). If S is nonsquare in E, the leading-pole argument in G-4l
shows every denominator element z²+u+Su² has either no pole or even
pole order at P.

Conversely, suppose S is square in E. Choose r∈F[T] lifting a square
root of S in E, so P divides r²+S. Write r²+S=PC. Since E is infinite,
choose w∈F[T] with residue satisfying Cbar*wbar²+wbar ≠ 0; this is
possible because X↦Cbar X²+X is a nonzero polynomial. Put
z=rw/P and u=w/P. Direct calculation gives
\[
z^2+u+Su^2
=\frac{(r^2+S)w^2+wP}{P^2}
=\frac{Cw^2+w}{P},
\]
which has a simple pole at P.

Consequently the local parity obstruction is exact:
\[
\text{every denominator element has no pole or even pole order at P}
\iff S\notin E^2.
\]
In particular, if S becomes a square in E, then E/F is not separable,
so P is inseparable. This identifies exactly the places where the
G-4l parity argument applies; it does not by itself compute the full
local quotient or a global normal form.


## 13. G-4n — explicit exceptional inseparable place

Take P=T²-S=T²+S in F[T], F=F₂(S). It is irreducible and
inseparable, with residue field F(√S), so S becomes a square there.
The exceptional-place construction is explicit:
\[
u=S/P,\qquad z=TS/P.
\]
Since T²+S=P,
\[
z²+u+Su²
=\frac{T²S²+S³}{P²}+\frac SP
=\frac{S²(T²+S)+SP}{P²}
=\frac{S²+S}{P}.
\]
The numerator is nonzero in the residue field, so this denominator
element has a genuine simple pole at P. This confirms concretely that
the separable-place parity obstruction cannot be extended to every
irreducible. It does not imply that arbitrary simple principal parts
at P are removable: the coefficient S²+S is specific, and the
denominator subgroup is only an F₂-vector space, not an F-vector space.


## 14. G-4o — higher odd poles at the exceptional place

The exact local behavior at the inseparable place P=T²+S can be refined
beyond the simple-pole witness. For every w∈F[T] and m≥1, set
\[
u=w/P^{m+1},\qquad z=Tw/P^{m+1}.
\]
Using T²+S=P gives
\[
z²+u+Su²
=\frac{w²+wP^m}{P^{2m+1}}.
\]
If w is a P-adic unit, this has pole order 2m+1 and leading
coefficient w̄² in E=F(√S). Thus this explicit family realizes
arbitrarily high odd pole orders with square leading coefficient.

For m=0 the corresponding identity instead gives
\[
(Tw/P)²+w/P+S(w/P)²=(w²+w)/P.
\]
Its simple-pole coefficient is the Artin–Schreier value w̄²+w̄,
not generally a square. The earlier G-4n witness is w=S and has
coefficient S²+S. Therefore the square-leading-coefficient statement
is restricted to the displayed higher-pole family m≥1; it is not a
classification of all odd principal parts of arbitrary denominator
elements.

The local quotient at P remains open. In particular, these identities
do not show that every principal part with a square leading coefficient
is removable, nor do they determine the interaction between successive
principal-part coefficients.


## 15. G-4p — exact completed local coordinate description

Let F=F₂(S), K=F(T), and P=T²+S. The P-adic completion of K
contains F((P)) as its coefficient subfield and has degree two over it:
\[
K_P=F((P))[T],\qquad T²=S+P.
\]
Indeed X²+S+P is irreducible over F((P)), since its reduction
X²+S is irreducible over F. Every element therefore has a unique
coordinate expression x+Ty with x,y∈F((P)).

Write z=x+Ty and u=r+Tq. In characteristic two,
\[
z²=x²+(S+P)y²,\qquad
u²=r²+(S+P)q².
\]
Hence the denominator map has the exact coordinate formula
\[
z²+u+Su²
=\bigl(x²+(S+P)y²+r+Sr²+S(S+P)q²\bigr)+Tq.
\]
Thus its completed local image, as a subset of
F((P))⊕T F((P)), is exactly
\[
\left\{
\left(x²+(S+P)y²+r+Sr²+S(S+P)q²,\ q\right):
x,y,r,q\in F((P))
\right\}.
\]

This gives an exact two-coordinate description of the completed local
image. The T-coordinate q is freely specified, but it contributes
S(S+P)q² to the scalar coordinate. The scalar-coordinate quotient
after this coupling, and the image modulo the integral local ring,
remain to be computed. This is not yet a global normal form for Q.


## 16. G-4q — coefficient filtration of the exceptional scalar coordinate

Retain \(F=\mathbb F_2(S)\), \(P=T^2+S\), and the completed
coordinates of G-4p. The scalar coordinate is
\[
A=x^2+(S+P)y^2+r+Sr^2+S(S+P)q^2.
\]
Set \(X=x+Sq\). Since \(x\) and \(q\) vary independently, so do
\(X\) and \(q\), and the formula becomes
\[
\boxed{A=X^2+(S+P)y^2+SPq^2+r+Sr^2.}
\]
This separates the three-square part from the additive polynomial
\(L_S(r)=r+Sr^2\).

Write Laurent expansions
\[
X=\sum_jX_jP^j,\quad y=\sum_jy_jP^j,\quad
q=\sum_jq_jP^j,\quad r=\sum_jr_jP^j,
\]
with coefficients in \(F\) and finite negative support. Coefficient
comparison gives the exact equations
\[
\boxed{
\begin{aligned}
[P^{2j}]A&=X_j^2+Sy_j^2+r_{2j}+Sr_j^2,\\
[P^{2j+1}]A&=y_j^2+Sq_j^2+r_{2j+1}.
\end{aligned}}
\]
In particular, the same \(y_j^2\) couples the even coefficient at
\(2j\) to the odd coefficient at \(2j+1\); the term \(Sr_j^2\)
also couples coefficient \(j\) of \(r\) to coefficient \(2j\) of
\(L_S(r)\). Thus pole orders cannot be analyzed independently one
coefficient at a time.

There is a sharper exact description if the additive-polynomial term
is temporarily omitted. Since \(F=F^2\oplus SF^2\) as an
\(F^2\)-vector space, uniquely write
\[
c_{2j}=a_j+Sb_j,\qquad c_{2j+1}=e_j+Sd_j,
\quad a_j,b_j,e_j,d_j\in F^2.
\]
A Laurent series \(c=\sum_nc_nP^n\) lies in
\[
F((P))^2+(S+P)F((P))^2+SPF((P))^2
\]
if and only if
\[
\boxed{b_j=e_j\quad\text{for every }j.}
\]
Indeed, the square part has coefficients
\(c_{2j}=X_j^2+Sy_j^2\) and
\(c_{2j+1}=y_j^2+Sq_j^2\); conversely the equality \(b_j=e_j\)
allows one to choose the square roots \(X_j^2=a_j\),
\(y_j^2=b_j=e_j\), and \(q_j^2=d_j\) independently for each
\(j\). This is an exact coefficient test for the square-only image,
not for the full scalar image, where \(r+Sr^2\) must still be
included.

**Status:** the completed scalar image now has an explicit coefficient
system, and its square-only subspace has a complete coefficient test.
The quotient by the full image of \(X^2+(S+P)y^2+SPq^2+r+Sr^2\),
modulo \(F[[P]]\), is still open. The next target is to analyze the
coupled recurrence contributed by \(r_{2j}+Sr_j^2\), then determine
which negative coefficient classes survive in the associated
principal-part filtration. No global quotient normal form is claimed.


## 17. G-4r — nontriviality and countable dimension of the exceptional completed local quotient

Let \(\mathcal O=F[[P]][T]\subset K_P=F((P))[T]\), with
\(T^2=S+P\), and let \(\mathcal D\) be the additive denominator
image \(\{z^2+u+Su^2:z,u\in K_P\}\). We study
\(K_P/(\mathcal O+\mathcal D)\) as an \(\mathbb F_2\)-vector
space. Write \(F=F^2\oplus SF^2\), and let \(\pi_0,\pi_S\)
be the two coefficient projections, with the factor \(S\) removed
in \(\pi_S\).

For a target with zero \(T\)-coordinate, its representation must
have \(q=0\) in G-4p. Its scalar denominator then has the form
\[
X^2+(S+P)y^2+r+Sr^2.
\]
For any scalar Laurent series \(c=\sum c_nP^n\), define the two
square-only obstructions at pair index \(j\) by
\[
E_j(c)=\pi_S(c_{2j})+\pi_0(c_{2j+1}),\qquad
D_j(c)=\pi_S(c_{2j+1}).
\]
Both vanish on \(X^2+(S+P)y^2\). On \(r+Sr^2\), they are
\[
E_j(r+Sr^2)=\pi_S(r_{2j})+r_j^2+\pi_0(r_{2j+1}),
\qquad D_j(r+Sr^2)=\pi_S(r_{2j+1}).
\]

Now suppose the target principal part has lowest pair index
\(j_0\le -2\), meaning its coefficients at \(P^{2j}\) and
\(P^{2j+1}\) vanish for every \(j<j_0\). If a representing
\(r\) had a nonzero coefficient at some index below \(j_0\),
choose its least index \(m\). Then \(r_{2m}=r_{2m+1}=0\),
and the vanishing of \(E_m\) for the target would force
\(r_m^2=0\), a contradiction. Thus \(r_n=0\) for all
\(n<j_0\). Since \(2j_0+1<j_0\), this forces
\[
D_{j_0}(c)=\pi_S(c_{2j_0+1})=0.
\]
This is a necessary leading-pole condition for local denominator
representability.

In particular, for every nonzero \(b\in F^2\) and every \(m\ge1\),
\[
\boxed{\frac{Sb}{P^{2m+1}}\notin\mathcal O+\mathcal D.}
\]
More strongly, choose an \(\mathbb F_2\)-basis \(\mathcal B\) of
\(F^2\). Then
\[
\left\{\frac{Sb}{P^{2m+1}}:b\in\mathcal B,\ m\ge1\right\}
\]
is linearly independent in \(K_P/(\mathcal O+\mathcal D)\): in any
finite nonzero relation, take the largest pole order (smallest pair
index); its \(D_j\) obstruction is the nonzero basis combination at
that level.

The field \(F=\mathbb F_2(S)\) is countable, so the set of finite
principal parts in \(K_P\) is countable. Hence the local quotient has
at most countable dimension. The independent family above is countably
infinite, giving the exact result
\[
\boxed{\dim_{\mathbb F_2}K_P/(\mathcal O+\mathcal D)=\aleph_0.}
\]
This is a theorem about the completed local quotient at the exceptional
inseparable place. It does not compute the global rational quotient
\(K/(K^2+L_S(K))\), nor does it assert that every local class is
represented by a rational global class.


## 18. G-4s — explicit global independent family from the exceptional place

The local classes in G-4r are represented by rational functions in
\(K=F(T)\), not merely by formal Laurent series. The natural map from
the global quotient
\[
Q=K/(K^2+\{u+Su^2:u\in K\})
\]
to the completed local quotient at \(P=T^2+S\) is well-defined:
a global denominator relation remains a denominator relation after
embedding \(K\hookrightarrow K_P\). Therefore any family independent
in the completed local quotient remains independent globally.

In particular, choose the explicit \(\mathbb F_2\)-independent
coefficient family \(b=S^{2n}\in F^2\), \(n\ge0\). G-4r gives
\[
\boxed{
\left\{\frac{S^{2n+1}}{(T^2+S)^{2m+1}}:
 n\ge0,\ m\ge1\right\}
\text{ is linearly independent in }Q.
}
\]
For a finite nonzero relation, choose the largest \(m\), equivalently
the lowest pair index at \(P\). Its odd Laurent coefficient has
nonzero \(S F^2\)-component \(S\sum_n\epsilon_n S^{2n}\), while all
terms with smaller \(m\) are less singular. This violates the
G-4r leading-pole condition for a denominator class.

This is an explicit two-parameter independent family in the original
global quotient. It complements the separable-place families of G-4l.
The quotient's exact dimension was already established as countably
infinite in G-4k; G-4s supplies a concrete independent family supported
at the exceptional inseparable place, not a full global basis or
reduction algorithm.


## 19. G-4t — a combined independent system across finite places

For a monic irreducible \(R\in F[T]\), write
\(E_R=F[T]/(R)\). If \(S\) is nonsquare in \(E_R\), G-4m
shows that every denominator \(z^2+u+Su^2\) has no pole or an
even-order pole at \(R\). Choose an \(\mathbb F_2\)-basis
\(\mathcal B_R\) of \(E_R\), and for each \(e\in\mathcal B_R\)
choose a polynomial lift \(\widetilde e\) of degree less than
\(\deg R\). Then
\[
\left\{\frac{\widetilde e}{R^{2m+1}}:
R\text{ monic irreducible},\ S\notin E_R^2,
 e\in\mathcal B_R,\ m\ge0\right\}
\]
is jointly linearly independent in \(Q\). To prove this, localize
a finite relation at a place \(R\) occurring in it and take the
largest odd pole order with nonzero residue coefficient. Terms
supported at other irreducibles are integral there, while a
denominator has only even pole order. This contradicts the assumed
relation.

There is also a family at a concrete infinite collection of
exceptional inseparable places. For every \(c\in F^\times\), put
\[
R_c=T^2+Sc^2.
\]
It is irreducible over \(F\), since \(S\) is nonsquare, and its
residue field contains \(\sqrt S\). In its completion write
\(T^2=Sc^2+R_c\) and \(z=x+Ty\), \(u=r+Tq\). For a target
with zero \(T\)-coordinate modulo the valuation ring, \(q\) is
integral and its scalar contribution is integral. The scalar
principal-part denominator is therefore
\[
X^2+(Sc^2+R_c)y^2+r+Sr^2.
\]
For \(F=F^2\oplus SF^2\), define \(\pi_0,\pi_S\) as before.
The square-only relation at pair index \(j\) is
\[
\pi_S(c_{2j})+c^2\pi_0(c_{2j+1})=0,
\]
while the second obstruction is \(\pi_S(c_{2j+1})\). The first
obstruction applied to \(r+Sr^2\) contains \(r_j^2\). The same
least-index argument as G-4r therefore proves that
\[
\boxed{\left\{\frac{S^{2n+1}}{R_c^{2m+1}}:
 n\ge0,\ m\ge1\right\}}
\]
is linearly independent at \(R_c\). Localizing at each distinct
\(R_c\) proves joint independence as \(c\) varies, and also proves
independence jointly with the preceding nonsquare-residue family.

Consequently the union of these two place-indexed families is an
explicit countably infinite independent family in the global quotient
\(Q\). It covers every finite irreducible place where \(S\) remains
nonsquare, together with the exceptional quadratic places
\(T^2+Sc^2\). It does not yet classify all irreducibles whose residue
field makes \(S\) square, nor does it give a complete global basis.
The already established upper bound \(\dim_{\mathbb F_2}Q\le\aleph_0\)
shows that this independent family is maximal in cardinality, not
necessarily a Hamel basis.


## 20. G-4u — a quartic exceptional residue place and its local coordinates

Let \(F=\mathbb F_2(S)\) and
\[
P(T)=T^4+T^2+S.
\]
This polynomial is irreducible over F. To see this, let \(\beta\) be a root of \(X^2+X+S\). That quadratic is irreducible: if \(r^2+r=S\) for \(r\in F\), the pole order at infinity of the left side is even whenever it has a pole, whereas S has pole order one. In \(F(\beta)\), a square root of \(\beta\) would have form \(x+y\beta\); comparing coefficients in
\[
(x+y\beta)^2=(x^2+Sy^2)+y^2\beta=\beta
\]
forces \(y=1\) and \(x^2=S\), impossible in F. Thus \(X^2-\beta\) is irreducible over \(F(\beta)\). If \(\alpha^2=\beta\), then \([F(\alpha):F]=4\), and \(\alpha\) has minimal polynomial \(P\). Moreover
\[
(\alpha+\beta)^2=\beta+\beta^2=S,
\]
so S becomes a square in the degree-four residue field. This is an explicit higher-degree exceptional irreducible, not covered by the quadratic family \(T^2+Sc^2\).

Put \(p=P(T)\). The P-adic completion is \(F((p))[T]\) with basis \(1,T,T^2,T^3\), since reduction modulo p is the irreducible polynomial P. The relation is
\[
T^4=p+T^2+S,\qquad
T^6=p+(p+1+S)T^2+S.
\]
For
\[
z=x_0+x_1T+x_2T^2+x_3T^3,\quad
u=r_0+r_1T+r_2T^2+r_3T^3,
\]
where all coefficients lie in \(F((p))\), the denominator \(z^2+\nu+S\nu^2\) has coordinates
\[
\begin{aligned}
[1]:\;&x_0^2+(p+S)(x_2^2+x_3^2)+r_0+Sr_0^2
       +S(p+S)(r_2^2+r_3^2),\\
[T]:\;&r_1,\\
[T^2]:\;&x_1^2+x_2^2+(p+1+S)x_3^2+r_2
       +S(r_1^2+r_2^2+(p+1+S)r_3^2),\\
[T^3]:\;&r_3.
\end{aligned}
\]
These identities are exact. They reduce the local quotient problem at P to a coupled coefficient problem in F((p)); they do not yet establish its dimension or a principal-part criterion. In particular, the quadratic exceptional-place proof G-4r cannot simply be copied: there are now four basis coordinates, and the T²-coordinate imposes an additional coupled integrality condition. **Open task G-4u.1:** determine \(K_P/(\mathcal O_P+\{z^2+\nu+S\nu^2\})\), or at least construct an infinite independent family in it, with \(\mathcal O_P=F[[p]][T]\).


## 21. G-4v — explicit odd-pole denominator elements at the quartic exceptional place

At the quartic place \(P=T^4+T^2+S\), put \(r=T^2+T\). The exact identity \(r^2+S=P\) gives, for \(w\in F[T]\) and \(m\ge1\),
\[
z=rw/P^{m+1},\quad u=w/P^{m+1}
\quad\Longrightarrow\quad
z^2+u+Su^2=(w^2+wP^m)/P^{2m+1}.
\]
For P-unit w this has pole order exactly \(2m+1\), with leading residue coefficient \(\bar w^2\). In particular w=1 gives \((1+P^m)/P^{2m+1}\), a denominator element with every prescribed odd pole order at least three and leading coefficient one. For the simple pole, use m=0 and w=T:
\[
z=rT/P,\quad u=T/P,
\quad z^2+u+Su^2=(T^2+T)/P,
\]
which has a genuine simple pole because P does not divide \(T^2+T\).

This proves that odd pole order alone cannot obstruct classes at this quartic exceptional place. The construction is an explicit family inside the denominator image; it is not a classification of all principal parts and does not establish the dimension of the quartic local quotient. The extra T²-coordinate coupling in G-4u remains the central open issue.


## 22. G-4w — exact two-coordinate reduction at the quartic place

Let \(p=P(T)\), and let a target have scalar and \(T^2\)-coordinates A,B, with its T and T³ coordinates integral. In any representation modulo \(\mathcal O_P=F[[p]][T]\), the exact T,T³ denominator coordinates r₁,r₃ must be integral. Their contributions to A,B are then integral. Set \(C=A+(p+S)B\). Substitution into the four-coordinate formulas of G-4u gives
\[
C\equiv x_0^2+(p+S)x_1^2+((p+S)x_3)^2
+r_0+Sr_0^2+(p+S)r_2\pmod{F[[p]]},
\]
\[
B\equiv x_1^2+x_2^2+(p+1+S)x_3^2+r_2+Sr_2^2
\pmod{F[[p]]}.
\]
The x₂ term cancels from C; the r₁,r₃ terms are integral. These two equations are equivalent to the scalar/T² part of the local representation problem, since A=C+(p+S)B. The first equation by itself has no obstruction because p+S is a unit and r₂ appears linearly. Any obstruction must use both equations and their shared variables x₁,x₃,r₂. This is an exact reduction, not a solution of the quartic local quotient.


## 23. G-4x — erratum and corrected quartic coupled equations

**Erratum to G-4w:** the displayed coefficient of x₃² in C there is correct; the subsequent G-4x attempted correction was itself erroneous. From the exact G-4u coordinates
\[
A=x_0^2+(p+S)(x_2^2+x_3^2)+r_0+Sr_0^2+S(p+S)(r_2^2+r_3^2),
\]
\[
B=x_1^2+x_2^2+(p+1+S)x_3^2+r_2+S(r_1^2+r_2^2+(p+1+S)r_3^2),
\]
and C=A+(p+S)B, the x₂² and r₂² terms cancel. The x₃² coefficient is
\[
(p+S)+(p+S)(p+1+S)=(p+S)^2,
\]
not p+S. Since r₁,r₃ are integral for a target with integral T,T³ coordinates, their remaining terms are integral. The correct coupled equations modulo F[[p]] are therefore
\[
C=x_0^2+(p+S)x_1^2+(p+S)^2x_3^2+r_0+Sr_0^2+(p+S)r_2,
\]
\[
B=x_1^2+x_2^2+(p+1+S)x_3^2+r_2+Sr_2^2.
\]
G-4w's displayed equations were correct; G-4x's alleged correction and all downstream formulas depending on the smaller x₃² coefficient are superseded.


## 24. G-4y — eliminate the linear shared variable and reduce to a square-class test

Use the corrected G-4x equations. Given a target pair (C,B), the first equation uniquely determines r₂ once x₀,x₁,x₃,r₀ are chosen:
\[
R=\frac{C+x_0^2+(p+S)x_1^2+(p+S)^2x_3^2+r_0+Sr_0^2}{p+S},\qquad r_2=R.
\]
The second equation is then
\[
B=x_1^2+x_2^2+(p+1+S)x_3^2+R+SR^2
\pmod{F[[p]]}.
\]
Since x₂ is free, x₁²+x₂² ranges over all squares (for fixed x₁, vary x₂; equivalently x₁+x₂ ranges over F((p))). Hence the exact criterion is
\[
\boxed{(C,B)\text{ is represented modulo }F[[p]]iff
\exists x_0,x_1,x_3,r_0\in F((p)):\
B+(p+1+S)x_3^2+R+SR^2\in F((p))^2+F[[p]],}
\]
with R as above. This is an exact elimination of r₂ and x₂, not yet a closed-form classification because of the remaining existential parameters.

For interpretation, write \(F=\mathbb F_2(S)\) and use \(F=F^2\oplus SF^2\). The quotient \(F((p))/(F((p))^2+F[[p]])\) has one F₂-coordinate from the S-component of each negative even Laurent coefficient, and two F₂-coordinates (the full coefficient in F) from each negative odd Laurent coefficient. Thus the remaining condition is an explicit infinite sequence of coefficient constraints on the four parameters. It is not legitimate to discard those parameters or infer a parity obstruction without solving the coupled constraints.


**G-4y coefficient clarification.** Each negative even exponent contributes a copy of \(F/F^2\cong SF^2\), and each negative odd exponent contributes a copy of F. Both coefficient spaces have countably infinite F₂-dimension. Since a Laurent series has only finitely many negative terms, the total square-class quotient is the direct sum of these coefficient spaces and has countably infinite F₂-dimension.


## 25. G-4z — explicit coefficient projections and recursion

Let \(K_P=F((p))\), \(F=\mathbb F_2(S)\), and \(\mathcal H=K_P/(K_P^2+F[[p]])\). Every class has the exact coordinates
\[
\bigl((f_{-(2j-1)})_{j\ge1},\ (\pi_S(f_{-2j}))_{j\ge1}\bigr)
\in \bigoplus_{j\ge1}F\ \oplus\ \bigoplus_{j\ge1}F^2,
\]
with finite support in the pole index for each Laurent series. Here \(F=F^2\oplus SF^2\), and \(\pi_S(a+Sb)=b\) for a,b∈F²; identifying F/F² with F² by this projection gives the even coordinates. Equivalently, as F₂-vector spaces,
\[
\mathcal H\cong\bigoplus_{j\ge1}F\,p^{-(2j-1)}\oplus\bigoplus_{j\ge1}(F/F^2)\,p^{-2j}.
\]

There is a direct coefficient recursion for the G-4y criterion. Put q=S+p and
\[
U=C+x_0^2+q x_1^2+q^2 x_3^2+r_0+Sr_0^2,
\qquad R=q^{-1}U.
\]
Write each series as \(x_i=\sum_k x_{i,k}p^k\), \(r_0=\sum_k r_kp^k\), and similarly for U,R,C. For any integer n,
\[
U_n=C_n+\mathbf1_{2\mid n}x_{0,n/2}^2
+\mathbf1_{2\mid n}S x_{1,n/2}^2
+\mathbf1_{n\equiv1\ (2)}x_{1,(n-1)/2}^2
+\mathbf1_{2\mid n}S^2x_{3,n/2}^2
+\mathbf1_{2\mid n}x_{3,(n-2)/2}^2
+r_n+\mathbf1_{2\mid n}S r_{n/2}^2.
\]
The identity qR=U is equivalent to the triangular recursion
\[
R_n=S^{-1}(U_n+R_{n-1}),
\]
with all coefficients below a common lower bound zero. Finally, the residual expression in G-4y is
\[
E=B+(1+S)x_3^2+p x_3^2+R+SR^2,
\]
so
\[
E_n=B_n+R_n+
\begin{cases}
(1+S)x_{3,n/2}^2+S R_{n/2}^2,&n\text{ even},\\
x_{3,(n-1)/2}^2,&n\text{ odd}.
\end{cases}
\]
The target is represented precisely when E_n=0 for every negative odd n and E_n∈F² for every negative even n. This is a fully explicit infinite coefficient test, with existential Laurent coefficient sequences x₀,x₁,x₃,r₀. It does not yet decide whether every target pair is represented or determine the codimension of the image.


## 26. G-4aa — no finite-slot dual functional annihilates the local denominator image

Let
\[
\mathcal H=F((p))/(F((p))^2+F[[p]])
\cong\bigoplus_{j\ge1}F p^{-(2j-1)}
\oplus\bigoplus_{j\ge1}(F/F^2)p^{-2j}.
\]
Let \(\ell:\mathcal H\to\mathbb F_2\) be an F₂-linear functional supported on a finite set I of negative exponent slots. Suppose \(\ell\) annihilates the image of \(u\mapsto u+Su^2\), hence in particular the full denominator image \(z^2+u+Su^2\).

If \(\ell\ne0\), choose the most negative exponent n in its finite slot support on which its component is nonzero. Vary the Laurent coefficient u_n freely while setting all other coefficients of u to zero. The resulting principal part of u+Su² has contributions only at exponents n and 2n. Since 2n<n and is more negative than every exponent in I, its 2n contribution is invisible to ell. The n-slot contribution is the arbitrary class of u_n in F when n is odd, or in F/F² when n is even. Thus the n-slot component of ell must vanish, a contradiction. Therefore ell=0.

Consequently, no nonzero finite-slot F₂-linear functional separates a class from the denominator image. This does **not** imply that the denominator image is all of H: a nonzero algebraic separating functional on a proper subspace may have infinite slot support. Any dual obstruction must therefore involve infinitely many principal-part slots. This is a restriction on certificate shape, not a local quotient classification.


## 27. G-4ab — an infinite-support annihilator exists

Let \(F=\mathbb F_2(S)\) and
\[
\mathcal H=F((p))/(F((p))^2+F[[p]])
\cong\bigoplus_{r\ge1}F p^{-(2r-1)}
\oplus\bigoplus_{r\ge1}(F/F^2)p^{-2r}.
\]
For the exponent chain \(-1,-2,-4,-8,\ldots\), define the injective F₂-linear map
\[
\phi:F\longrightarrow F/F^2,\qquad x\longmapsto[Sx^2].
\]
It is injective: if \(Sx^2=y^2\) and x is nonzero, then \(S=(y/x)^2\), contrary to S being nonsquare in F.

Choose a nonzero F₂-linear functional \(\ell_{-1}:F\to\mathbb F_2\). Since \(\phi\) is injective, extend it to \(\ell_{-2}:F/F^2\to\mathbb F_2\) such that
\[
\ell_{-2}([Sx^2])=\ell_{-1}(x).
\]
Inductively, after choosing \(\ell_{-2^j}\) for j≥1, define a functional on the subspace \(\phi(F)\) by
\[
[Sx^2]\longmapsto\ell_{-2^j}([x]),
\]
and extend it to all of \(F/F^2\), obtaining \(\ell_{-2^{j+1}}\). Injectivity of phi makes each extension well-defined. Set all coefficient functionals at negative exponents outside this chain equal to zero.

These coefficient functionals define a linear functional \(\ell\) on the direct sum \(\mathcal H\): each principal part has only finitely many nonzero slots. For an arbitrary Laurent principal part u, the coefficient u_m contributes to \(u+Su^2\) at exponents m and 2m. The chain recurrences
\[
\ell_{-1}(x)=\ell_{-2}([Sx^2]),\qquad
\ell_{-2^j}([x])=\ell_{-2^{j+1}}([Sx^2])\quad(j\ge1)
\]
therefore cancel these contributions in pairs. All off-chain contributions vanish. Hence \(\ell(u+Su^2)=0\). Squares are already zero in H, so \(\ell\) annihilates the full denominator \(z^2+u+Su^2\). Since \(\ell_{-1}\ne0\), the resulting functional is nonzero.

Thus the local quotient H is nonzero, with a separating functional of necessarily infinite slot support. The construction is noncanonical (it uses successive vector-space extensions); it is not an explicit finite certificate or a classification of H.


## 28. G-4ac — exact inverse-limit description of all local annihilators

For each positive odd integer r, the coefficient spaces along the chain of exponents \(-r,-2r,-4r,\ldots\) are
\[
V_{r,0}=F,\qquad V_{r,j}=F/F^2\quad(j\ge1).
\]
Write \(q:F\to F/F^2\) for the quotient map and \(\phi:F\to F/F^2\) for \(x\mapsto[Sx^2]\). A functional on the principal-part quotient is a family
\[
\lambda_{r,0}\in V_{r,0}^*,\qquad
\lambda_{r,j}\in V_{r,j}^*\quad(j\ge1),
\]
where stars denote algebraic F₂-duals. It annihilates every \(u+Su^2\) if and only if, for every odd r,
\[
\lambda_{r,1}\circ\phi=\lambda_{r,0},
\qquad
\lambda_{r,j+1}\circ\phi=\lambda_{r,j}\circ q
\quad(j\ge1).
\]
Indeed, a coefficient x of u at exponent \(-2^jr\) contributes [x] at that same exponent (x itself when j=0) and [Sx²] at the doubled exponent. These are the only two contributions, and distinct odd-core chains are disjoint. Thus the displayed equations are necessary and sufficient.

Equivalently, the full annihilator is the product over odd r of the inverse limits of the dual spaces under the restriction maps
\[
(F/F^2)^*\longrightarrow F^*,\quad \mu\longmapsto\mu\circ\phi,
\]
and
\[
(F/F^2)^*\longrightarrow(F/F^2)^*,\quad
\mu\longmapsto\mu\circ\phi\circ q^{-1}
\]
understood as the relation \(\lambda_{j+1}\circ\phi=\lambda_j\circ q\), not as a globally defined inverse to q. Each extension step is surjective because phi is injective: define the next functional on phi(F) by the prescribed right-hand side and extend linearly to all of F/F².

Since F is countable and has countably infinite F₂-dimension, \(F^*\) has cardinality \(2^{\aleph_0}\). Projection of each chain inverse limit onto its initial \(F^*\) is surjective, while the set of all countable sequences of coefficient functionals has cardinality at most \((2^{\aleph_0})^{\aleph_0}=2^{\aleph_0}\). Hence even one chain contributes continuum many annihilators, and the full annihilator has cardinality exactly continuum. As an F₂-vector space its dimension is therefore continuum.

This classifies the annihilator abstractly as an inverse-limit space; it does not identify a canonical basis or a canonical splitting of the restriction maps.


## 29. G-4ad — canonical chain-cokernel / zigzag-colimit model

The scalar principal-part quotient
\[
F((p))/(F((p))^2+F[[p]])
\]
splits as a direct sum over odd positive integers r, one summand for each exponent chain \(-r,-2r,-4r,\ldots\). The map \(u\mapsto u+Su^2\) preserves this decomposition.

For one chain put \(W_0=F\), \(W_j=F/F^2\) for j≥1, and let q:F→F/F² and phi(x)=[Sx²]. The chain denominator map is the finite-support linear map
\[
T_r:\bigoplus_{j\ge0}F\longrightarrow
W_0\oplus\bigoplus_{j\ge1}W_j
\]
given by
\[
T_r((x_j)_{j\ge0})_0=x_0,\qquad
T_r((x_j)_{j\ge0})_j=q(x_j)+\phi(x_{j-1})\quad(j\ge1).
\]
It maps finite-support sequences to finite-support sequences (with support enlarged by at most one slot). Therefore the full scalar quotient by the u+Su² image has the canonical decomposition
\[
\boxed{
\bigoplus_{r\ge1,\ r\text{ odd}}
\operatorname{coker}(T_r).
}
\]
The z² term is already zero in the ambient quotient by F((p))².

Equivalently, each chain cokernel is the colimit of the zigzag of F₂-vector spaces
\[
W_0\ \longleftarrow\ F_0\ \longrightarrow\ W_1
\ \longleftarrow\ F_1\ \longrightarrow\ W_2
\ \longleftarrow\ F_2\ \longrightarrow\cdots,
\]
where the maps from F_0 are identity to W_0 and phi to W_1, and for j≥1 the maps from F_j are q to W_j and phi to W_{j+1}. This is a genuine categorical colimit presentation; it avoids pretending that phi descends to F/F² (it generally does not).

Dualizing this presentation gives exactly the compatibility equations of G-4ac. Thus G-4ac is the algebraic dual of this canonical cokernel model. This description is canonical, but it is still a presentation rather than a simpler closed-form evaluation of each cokernel.


## 30. G-4ae — each odd-core chain cokernel has countably infinite dimension

Let C denote the cokernel of the chain map T_r in G-4ad. Its presentation is independent of the odd chain label r.

The target of T_r is a countable F₂-vector space: F=F₂(S) is countable, as is F/F², and a countable direct sum of countable sets is countable. Hence C is countable as a set and has dimension at most aleph₀.

On the other hand, the algebraic dual C* is the space of compatible coefficient-functional sequences from G-4ac. The projection from this space to the initial functional λ₀∈F* is surjective, because phi is injective and each prescribed functional on phi(F) extends to F/F². Since F has countably infinite F₂-dimension, |F*|=2^{aleph₀}. Thus |C*|≥2^{aleph₀}; the reverse inequality follows because C is countable. Consequently |C*|=2^{aleph₀}, and since the scalar field is finite, dim_F₂ C*=2^{aleph₀}.

In particular C cannot be finite-dimensional. Together with its countable upper bound,
\[
\boxed{\dim_{\mathbb F_2} C=\aleph_0.}
\]
All odd-core chain cokernels are canonically isomorphic by their identical presentations. There are countably infinitely many odd r, so the full local scalar quotient is a direct sum of countably infinitely many countably infinite-dimensional chain cokernels. This determines the dimension of each summand, but does not supply a canonical basis or explicit normal forms.


## 31. G-4af — explicit independent family in every chain cokernel

Fix any positive odd integer r and let C_r=coker(T_r) be the chain cokernel of G-4ad. The zeroth-coordinate inclusion
\[
F\longrightarrow W_0\oplus\bigoplus_{j\ge1}W_j,
\qquad a\longmapsto(a,0,0,\ldots)
\]
has zero intersection with im(T_r). Indeed, if T_r(x) has finite support and x is a nonzero finite-support sequence, let N be the largest index with x_N≠0. Its (N+1)-st output coordinate is
\[
q(x_{N+1})+\phi(x_N)=\phi(x_N)\ne0,
\]
since x_{N+1}=0 and phi is injective. Therefore T_r(x) cannot be supported only in coordinate zero. Hence F embeds in C_r.

In particular, because the monomials 1,S,S²,… are F₂-linearly independent in F=F₂(S), the classes
\[
\boxed{[S^n p^{-r}]\in C_r,\qquad n\ge0}
\]
are an explicit countably infinite linearly independent family, for every odd r. This makes the lower bound in G-4ae constructive. Combined with the countable upper bound, it gives dim_F₂ C_r=aleph₀ without invoking the algebraic dual.

The family is an embedded copy of the polynomial subspace F₂[S] in each chain. It is not claimed to span C_r; determining a complementary normal form remains open.


## 32. G-4ag — the chain cokernel is canonically F

A crucial strengthening is that
\[
\phi:F\to F/F^2,\qquad x\mapsto[Sx^2]
\]
is bijective, not merely injective. Indeed, F=F₂(S), F²=F₂(S²), and [F:F²]=2. Since S∉F²,
\[
F=F^2\oplus S F^2
\]
as F²-vector spaces. Every class in F/F² therefore has a unique form [Sx²], because Frobenius maps F bijectively onto F².

Consequently every chain cokernel C_r=coker(T_r) from G-4ad is canonically isomorphic to F, via the zeroth-coordinate embedding. To prove surjectivity, let y=(y_0,y_1,\ldots,y_N,0,\ldots) be a finite-support target, with y_0∈F and y_j∈F/F² for j≥1. Set x_N=0 and recursively, for j=N,N−1,…,1, define
\[
x_{j-1}=\phi^{-1}\bigl(y_j+q(x_j)\bigr).
\]
Then x=(x_0,…,x_{N-1},0,…) has finite support and the higher coordinates of y+T_r(x) vanish. Thus every cokernel class has a zeroth-coordinate representative.

That representative is unique: if T_r(x) is supported only in coordinate zero and x is nonzero, let N be the largest index with x_N≠0. The (N+1)-st coordinate of T_r(x) is phi(x_N)≠0, contradiction. Hence
\[
\boxed{C_r\cong F=\mathbb F_2(S).}
\]
The reduction algorithm above is canonical and finite for every finite principal part.

In particular, the classes
\[
\boxed{[S^n p^{-r}],\quad n\ge0}
\]
are not merely independent (G-4af): they form an F₂-basis of C_r for every odd r. Therefore the auxiliary quotient H₀ has the explicit basis
\[
\boxed{
\left\{S^n p^{-r}: n\ge0,\ r\ge1\text{ odd}\right\}.
}
\]
This proves H₀ is countably infinite-dimensional and supplies a complete normal form for that auxiliary quotient: reduce independently along each odd-core chain, then collect the resulting zeroth-coordinate coefficients.

**Correction to G-4ac:** because phi is bijective, every extension step in the dual recurrence is unique, not merely possible after choosing a vector-space complement. On each chain, an initial functional lambda_0∈F* determines all later functionals uniquely by
\[
\lambda_{j+1}=\lambda_j\circ q\circ\phi^{-1}\quad(j\ge0),
\]
where for j=0 the same formula uses q:F→F/F² and for j≥1 q acts on the coefficient representative F→F/F². More precisely, the recurrence is lambda_1∘phi=lambda_0 and lambda_{j+1}∘phi=lambda_j∘q for j≥1. Since phi is bijective, these determine lambda_{j+1} uniquely. Thus the chain annihilator is canonically F*, and the full annihilator is the product of F* over odd r. Its F₂-dimension is continuum, as previously established, but its inverse-limit ambiguity disappears.


## 33. G-4ah — scope correction and exact full local quotient

The chain-cokernel results G-4ad through G-4ag concern the **auxiliary** quotient
\\[
H_0=F((p))\\big/\\bigl(F[[p]]+F((p))^2+\\{r+Sr^2:r\\in F((p))\\}\\bigr).
\\]
They do not, by themselves, classify the full exceptional completed local quotient. In K_P=F((p))[T], with T²=S+p, a square is
\\[
(x+Ty)^2=x^2+(S+p)y^2,
\\]
and the second summand is not generally a square in F((p)). Thus the G-4ag chain basis is a basis of H₀ only.

There is nevertheless an exact scalar model for the **full** quotient. Write a general element as A+TB, and let B₋ be the negative-power part of B. Taking u=TB₋ gives
\\[
u+Su^2=TB_-+S(S+p)B_-^2.
\\]
Adding this denominator element removes the negative T-coordinate; the remaining integral T-coordinate is absorbed into O=F[[p]][T]. Hence every class has a scalar representative.

Moreover, a scalar A lies in O+𝒟 only if the T-coordinate q of the chosen u=r+Tq is integral, since the T-coordinate of O is integral. For integral q, S(S+p)q² is integral and can be absorbed into F[[p]]. Conversely, every scalar expression x²+(S+p)y²+r+Sr² is visibly in O+𝒟. Therefore
\\[
\\boxed{
K_P/(O+\\mathcal D)\\cong
F((p))\\Big/
\\Bigl(F[[p]]+F((p))^2+(S+p)F((p))^2+
\\{r+Sr^2:r\\in F((p))\\}\\Bigr).
}
\\]
The extra term (S+p)F((p))² is exactly the missing coupling between neighboring exponent positions: for y=\\sum a_n p^n, its square contributes S a_n² at exponent 2n and a_n² at exponent 2n+1.

Equivalently, the full quotient is the auxiliary chain cokernel H₀ from G-4ad, further quotiented by the image of (S+p)F((p))². The G-4r local parity obstruction and G-4s global independent family were established against the full denominator and remain valid. The G-4ac through G-4ag dual and chain calculations must be read as auxiliary-quotient results only.

**Revised open problem:** compute the image of (S+p)F((p))² inside the explicit chain normal form H₀≅⊕_{r odd}F. Determine the resulting quotient, including whether the G-4r independent family spans the full local quotient.


## 34. G-4ai — exact relation presentation of the full local quotient

Let q:F→F/F² be the quotient map, phi(x)=[Sx²], and define
\[
\tau=\phi^{-1}\circ q:F\to F.
\]
Since F=F²⊕SF², every a has a unique decomposition a=x²+Sy² and tau(a)=y. In particular tau is F₂-linear.

Under the auxiliary normal-form isomorphism H₀≅⊕_{r odd}F e_r of G-4ag, a coefficient c∈F/F² at chain level j≥1 reduces to
\[
\rho_j(c),\qquad
\rho_1=\phi^{-1},\quad
\rho_{j+1}=\rho_j\circ q\circ\phi^{-1}.
\]
Thus for a∈F,
\[
\rho_j(\phi(a))=\tau^{j-1}(a).
\]

Now let y=\sum_n a_n p^n∈F((p)). The additional square term is
\[
(S+p)y^2=\sum_n \bigl(Sa_n^2p^{2n}+a_n^2p^{2n+1}\bigr).
\]
Only n<0 contributes to the principal part. Put m=−n≥1, write m=2^v r with r odd, and consider the corresponding pair:
- the coefficient S a² at exponent −2m lies at level v+1 of chain r; its auxiliary normal form is \(\tau^v(a)\) at the zeroth coordinate of chain r;
- the coefficient a² at exponent −(2m−1) lies at level zero of chain 2m−1.

Therefore the image of (S+p)F((p))² in H₀ is exactly the F₂-span of
\[
e_{2m-1}(a^2)+e_{\operatorname{odd}(m)}(\tau^{v_2(m)}(a)),
\qquad m\ge1,\ a\in F.
\]
It follows that the full local quotient has the exact presentation
\[
\boxed{
K_P/(O+\mathcal D)\cong
\left(\bigoplus_{r\ge1,\ r\text{ odd}}F e_r\right)
\Big/
\left\langle
e_{2m-1}(a^2)+e_{\operatorname{odd}(m)}(\tau^{v_2(m)}a)
\right\rangle_{\mathbb F_2}.
}
\]
This is an exact presentation, not yet a normal form. The independent full-quotient family from G-4r/G-4s supplies a countably infinite lower bound; the ambient principal-part space is countable, so the full local quotient has dimension exactly aleph₀. The remaining task is to reduce the displayed relations to a canonical basis or prove that a chosen family spans.


## 35. G-4aj — complete triangular normal form for the full local quotient

For each odd r≥3, the unique relation family indexed by m=(r+1)/2 is
\[
e_r(a^2)=e_{r_0}(\tau^v(a)),\quad
r_0=\operatorname{odd}(m),\quad v=v_2(m).
\]
Here r₀<r. Since Frobenius F→F² is bijective, this relation eliminates exactly the F²-component at chain r. Decompose every coefficient uniquely as c=x²+Sy². Retain Sy² at chain r and transfer x² to the smaller chain r₀. Repeating in decreasing chain index terminates for every finite-support vector. At chain 1, the relation is e₁(a²+a)=0.

This yields the canonical vector-space isomorphism
\[
\boxed{
K_P/(O+\mathcal D)
\cong
F/\wp(F)\oplus
\bigoplus_{\substack{r\ge3\\r\text{ odd}}}SF^2,
\qquad \wp(a)=a^2+a.
}
\]
The isomorphism is obtained by the finite reduction algorithm just described. To prove uniqueness, suppose a finite sum of defining relations lies in the proposed normal-form subspace. Choose the largest r≥3 whose relation parameter a_r is nonzero. At coordinate r, only that relation contributes, and its component is a_r²∈F². The normal-form subspace at r is SF², and F²∩SF²=0, so a_r=0, contradiction. Descending induction removes all r≥3 relations; at r=1 the only remaining relation space is exactly wp(F).

### Explicit basis of the Artin–Schreier summand

Let Q range over monic irreducible polynomials in F₂[S]. For each Q choose the standard F₂-basis
\[
1,S,\ldots,S^{\deg Q-1}
\]
of the residue field F₂[S]/(Q). Then a basis of F/\wp(F) is
\[
\boxed{
\{1\}
\cup\{S^d:d\ge1\text{ odd}\}
\cup
\left\{
\frac{S^j}{Q(S)^d}:
Q\text{ monic irreducible},d\ge1\text{ odd},0\le j<\deg Q
\right\}.
}
\]
Spanning follows from partial fractions. At a finite place Q, if a principal part has highest pole order d even, choose a numerator whose residue is the square root of its leading residue coefficient and subtract its Artin–Schreier image; this removes the even leading pole and lowers the pole order. Iterate until only odd pole orders remain. At infinity, reduce even polynomial degrees by subtracting \(\wp(S^{d/2})=S^d+S^{d/2}\). This leaves the displayed representatives.

For independence, any nonconstant \(g^2+g\) has at every pole of g a pole of even order, since the leading pole of g² strictly dominates that of g. Thus a nonzero finite combination of the displayed finite-place terms has an odd pole at some Q, or, after those vanish, a polynomial with odd degree has an odd pole at infinity. Neither can be Artin–Schreier. The constant 1 is not in \(\wp(F)\), since a rational function with no poles is in F₂ and \(\wp(F₂)=0\).

### Explicit basis of the full local quotient

A standard F₂-basis of F itself, by partial fractions, is
\[
\mathcal E=
\{S^d:d\ge0\}
\cup
\left\{
\frac{S^j}{Q(S)^d}:
Q\text{ monic irreducible},d\ge1,0\le j<\deg Q
\right\}.
\]
Its Frobenius image \(\mathcal E^2\) is a basis of F². Therefore a basis of the full local quotient is the union of:
1. the chain-1 Artin–Schreier basis displayed above; and
2. for every odd r≥3, the classes \(S b\,p^{-r}\) with b∈\(\mathcal E^2\).

The second family is precisely the full chain family underlying G-4r/G-4s. The first family supplies the previously unaccounted chain-1 summand. In particular the full quotient has countably infinite F₂-dimension, with an explicit countable basis.



## 36. G-4ak — global comparison: correct surface-level framework and scope correction

The base field in the quaternion-boundary problem is
\[
K=\mathbb F_2(S,T),
\]
which has transcendence degree two over its finite constant field. It is not a global field in the Albert–Brauer–Hasse–Noether sense (a number field or a one-variable function field over a finite field). Consequently, the exact sequence
\[
0\to\operatorname{Br}(K)\to\bigoplus_v\operatorname{Br}(K_v)
\xrightarrow{\sum\operatorname{inv}_v}\mathbb Q/\mathbb Z\to0
\]
must not be invoked for this K. It would be a category error to infer a global classification of the present boundary image from a parity condition on places.

The relevant geometric object is the regular surface
\[
X=\operatorname{Spec}\mathbb F_2[S,T]
\]
(or a suitable regular proper compactification), with function field K. The divisor P=(T²+S) is one codimension-one point. Its residue field is
\[
\kappa(P)=\mathbb F_2(S)[T]/(T²+S)\cong\mathbb F_2(T),
\]
where the residue image of S is T². The completion used in G-4aj is the completion of K at this divisorial valuation, with a purely inseparable residue extension over the coefficient field F=F₂(S) encoded by T²=S in the residue.

For prime-to-characteristic torsion, one expects the familiar Gersten/Bloch–Ogus residue pattern on a regular surface. Here the classes are 2-primary in characteristic two, so the residue formalism must instead be the characteristic-p Kato/logarithmic-Hodge–Witt one; the p-primary Gersten/Kato complex is not interchangeable with the prime-to-p Brauer residue complex. In particular, one must specify the cohomological theory, twists, and residue maps before claiming exactness. The Kato complex for a regular surface has codimension-one residue fields and a further codimension-two boundary; this is the appropriate shape of the global compatibility problem.

### Established scope versus open bridge

- G-4aj is a complete computation of the explicitly defined additive local quotient \(K_P/(\mathcal O_P+\mathcal D_P)\). Its normal form and basis are local algebra statements.
- This computation does not by itself identify that quotient with a Kato residue group, a kernel of a global localization map, or a summand of \(\operatorname{Br}(K)[2]\).
- The global symbol map \([a]\mapsto[aS,S)_2\) and its kernel criterion remain the algebraic objects to compare with the local calculation.
- The next proof obligation is to write the characteristic-two Kato residue of the quaternion symbol at P directly, determine whether the G-4aj quotient maps to its unramified/ramified filtration, and check the codimension-two compatibility at closed points on the divisor P.
- Only after this local symbol-to-Kato comparison is proved should one assemble the residues over all irreducible curves of X and impose the surface-level reciprocity relation.

This scope correction prevents the use of a one-dimensional global-field theorem in a two-dimensional function-field problem. It does not alter the local normal-form theorem G-4aj.



## 37. G-4al — the residue logarithmic differential vanishes at the exceptional divisor

At P=(T²+S), the residue field is E=F₂(T), with residue image \(\bar S=T²\). Hence
\[
d\log(\bar S)=\frac{d(T²)}{T²}=0
\quad\text{in }\Omega^1_{E/\mathbb F_2},
\]
because the absolute differential of a square vanishes in characteristic two. Thus the ordinary residue-field logarithmic differential of the second entry S of the symbol \([aS,S)_2\) is zero at P.

This is a concrete warning against expecting the tame/logarithmic residue of the second entry to detect the G-4aj local classes. The vanishing does not prove that the quaternion class is unramified or trivial: the coefficient a may have poles, and the p-primary Brauer class can carry wild information invisible to this residue differential. The next local task is to compute the Kato filtration/refined Swan data of \([aS,S)_2\) for representatives a in the G-4aj normal-form basis, and determine whether the filtration detects all or only part of the local quotient. No identification of the quotient with a Kato graded piece is claimed here.


## 38. G-4am — the exceptional symbol has differential representative \(a\,dp\)

Let \(K=\mathbb F_2(S,T)\), \(P=(p)\) with \(p=T^2+S\), and let \(K_P\) be the completion. In absolute Kähler differentials over \(\mathbb F_2\), the identity \(p=T^2+S\) gives
\[
dp=d(T^2)+dS=dS,
\]
since the characteristic is two. Therefore
\[
d\log S=\frac{dS}{S}=\frac{dp}{S},
\qquad
(aS)d\log S=a\,dp.
\]
Under the standard characteristic-two differential-symbol map for the quaternion symbol, \([x,b)_2\) is represented by \(x\,d\log b\). Thus the local differential representative of \([aS,S)_2\) at P is exactly
\[
\boxed{a\,dp.}
\]

This identifies the direction in which the exceptional symbol can carry wild information: although the residue image \(\bar S=T^2\) has \(d\log\bar S=0\), the absolute differential before reduction is \(dp/S\), and multiplication by the first slot \(aS\) leaves \(a\,dp\). In particular, for a Laurent principal part \(a=c p^{-r}\), the representative is \(c p^{-r}dp\); its pole order is visible in the uniformizer differential.

**Scope:** this is an exact identity of differential representatives. It does not yet identify \(K_P/(\mathcal O_P+\mathcal D_P)\) with a Kato cohomology group or a Kato graded piece. The remaining calculation is to pass from \(a\,dp\) to the quotient defining characteristic-two \(H^2\), track Cartier/Frobenius relations and exact differentials, and compare the resulting filtration with the G-4aj normal form. In particular, no injectivity or surjectivity from the G-4aj additive quotient is claimed.


## 39. G-4an — explicit Kato differential quotient in the p-basis \(\{T,p\}\)

The coordinate change \(S=T^2+p\) gives \(K=\mathbb F_2(T,p)\), and completion at \(p=0\) gives
\[
K_P=\mathbb F_2(T)((p)).
\]
The pair \(\{T,p\}\) is a 2-basis: every \(f\in K_P\) has a unique decomposition
\[
f=f_{00}^2+T f_{10}^2+p f_{01}^2+Tp f_{11}^2.
\]
Consequently \(\Omega^1_{K_P/\mathbb F_2}=K_PdT\oplus K_Pdp\).

For a field of characteristic 2, the standard differential presentation is
\[
H_2^2(K_P)
=\operatorname{coker}\left(
1-\gamma:\Omega^1_{K_P}\longrightarrow
\Omega^1_{K_P}/dK_P
\right),
\]
where \(\gamma\) is the additive Frobenius-semilinear map characterized by
\[
\gamma(h\,dT)=[h^2T\,dT],\qquad
\gamma(h\,dp)=[h^2p\,dp].
\]
Thus the differential quotient is explicitly
\[
\frac{K_PdT\oplus K_Pdp}
{dK_P+
\left\langle
h,dT+h^2T,dT,\;
h,dp+h^2p,dp
: h\in K_P
\right\}_{\mathbb F_2}},
\]
where the displayed relations are interpreted as additive generators (and the formula is in characteristic two). The local symbol \([aS,S)_2\) is represented by \(a,dp\), so its class is obtained by inserting \(a\) into the second summand and reducing by these exact and Cartier relations.

**Important correction to the preceding preliminary calculation:** Cartier \(C\) is naturally defined on closed forms (or their de Rham classes), not as an operator on arbitrary 1-forms. Therefore formulas such as \(C(f\,dT)=f_{10}dT\) for arbitrary f must not be used. The valid all-forms operation in the Kato cokernel presentation is \(\gamma\) above, i.e. inverse Cartier followed by reduction modulo exact forms. The p-basis formulas for \(\gamma\) are the formulas used in this section.

This gives a concrete presentation of the local Kato group and a representative-level map from the quaternion symbol. It still does **not** prove that the separate additive quotient G-4aj is isomorphic to this Kato group, nor that its displayed basis maps injectively or surjectively. Such a comparison requires computing the image of \(\mathcal O_P+\mathcal D_P\) under \(a\mapsto a\,dp\) and its intersection with the exact/Cartier relation subgroup.


## 40. G-4ao — correction: the Kato group is a Cartier-filtration cokernel

The provisional G-4an presentation that quotiented \(\Omega^1_{K_P}\) only by exact forms and the additive expressions \(h\,dT+h^2T\,dT\), \(h\,dp+h^2p\,dp\) is **not** the correct complete presentation. It omitted the higher Cartier filtration. Replace that presentation by the following standard one.

For a characteristic-two field F, put \(B_1=dF\subset\Omega_F^1\). Recursively, for \(i\ge2\), let \(B_i\subset\Omega_F^1\) be the inverse image of \(C^{-1}(B_{i-1})\) under the quotient map \(\Omega_F^1\to\Omega_F^1/B_1\). The inverse Cartier isomorphism gives
\[
C^{-1}:B_i\xrightarrow{\sim}B_{i+1}/B_1.
\]
Put \(B_\infty=\bigcup_{i\ge1}B_i\). The characteristic-two Kato group has the presentation
\[
\boxed{
H_2^2(F)\simeq
\operatorname{coker}\left(
\wp:\Omega_F^1/B_\infty\to\Omega_F^1/B_\infty
\right),\qquad
\wp=C^{-1}-\mathrm{id}.
}
\]
Here \(C^{-1}:\Omega_F^1\to\Omega_F^1/dF\) is the inverse Cartier map, and the displayed endomorphism is understood on the quotient by \(B_\infty\). This is the differential-form presentation in Hiranouchi–Sugiyama, *Extended differential symbol and the Kato homology groups* (2025), §3.3, equations (3.4)–(3.5) and Corollary 3.5.

For \(F=K_P=\mathbb F_2(T)((p))\), the 2-basis \(\{T,p\}\) gives
\[
C^{-1}(h\,dT)=[h^2T\,dT],\qquad
C^{-1}(h\,dp)=[h^2p\,dp]
\quad\text{in }\Omega_F^1/dF.
\]
Indeed, these follow from \(C^{-1}(a\,d\log b)=a^2d\log b\), writing \(dT=T\,d\log T\) and \(dp=p\,d\log p\). These are identities modulo exact forms, not a license to omit \(B_\infty\).

The exceptional quaternion symbol \([aS,S)_2\) is represented by \(a\,dp\), as in G-4am. Its Kato class is therefore the class of \(a\,dp\) in the Cartier-filtration cokernel above.

**Remaining bridge:** compute the image/intersection of the additive subspace \(\mathcal O_P+\mathcal D_P\) under \(a\mapsto a\,dp\) in this cokernel, and establish whether the induced map from G-4aj is well-defined, injective, surjective, or neither. No such comparison is asserted. This correction supersedes the oversimplified quotient written in G-4an; the p-basis and inverse-Cartier formulas themselves remain valid.


## 39. G-4an — geometry-first proof strategy: the divisor as the organizing object

The exceptional calculation suggests changing the order of attack. Rather than first presenting the local quotient by generators and relations and only afterwards interpreting it, organize the proof around the geometry of the divisor.

Let
\[
X=\operatorname{Spec}\mathbb F_2[S,T],\qquad
P=V(p),\qquad p=T^2+S.
\]
The divisor P is smooth: \(dp=dS\), and the conormal sequence for the smooth Cartier divisor is
\[
0\longrightarrow (p)/(p^2)
\xrightarrow{\ d\ }
\Omega^1_{X/\mathbb F_2}|_P
\longrightarrow
\Omega^1_{P/\mathbb F_2}
\longrightarrow0.
\]
On P, \(S=T^2\), so \(dS=0\) in \(\Omega^1_P\). Thus the conormal line is generated by \(dp=dS\), while the tangent differential is generated by \(dT\). The symbol representative from G-4am,
\[
(aS)d\log S=a\,dp,
\]
lies in the normal/conormal direction. This is the geometric reason the residue-field logarithmic differential alone loses the information.

### Proposed proof architecture

1. **Stratify geometrically.** Fix the divisor P and its closed points. Separate the normal parameter p from residue/tangent coordinates. Record which coefficients have poles along P and which vary along P.
2. **Filter before quotienting.** Put the pole-order filtration on the differential representatives \(a\,dp\). Compute each associated-graded layer using the conormal line and the residue field \(\kappa(P)=\mathbb F_2(T)\).
3. **Apply the characteristic-two operator on each layer.** Determine the exact action of Cartier/Frobenius and exact differentials on the associated graded. This is where the square and Artin–Schreier relations should appear geometrically, rather than being guessed from a large presentation.
4. **Recover the normal form.** Compare the resulting graded relations with the G-4aj decomposition: the chain-1 Artin–Schreier part and the odd chains \(r\ge3\). Prove that the filtration is exhaustive and separated, and that the proposed representatives survive independently.
5. **Only then glue.** At closed points of P, compute the codimension-two boundary of the filtered classes. This tests whether the local representatives extend or cancel globally; it is the surface-level compatibility step, not an ABHN parity argument.

### What is proved and what remains a research target

The smoothness of P, the conormal sequence, the identification of its conormal generator with dp, and the representative identity \((aS)d\log S=a\,dp\) are exact. The assertion that the G-4aj quotient is a Kato graded object is **not** proved. In particular, the associated-graded Cartier calculation, filtration comparison, and closed-point gluing remain open.

The efficiency gain sought here is structural: one geometric filtration should simultaneously organize the local computation, the proof of independence, and the compatibility checks. If the associated-graded calculation fails to reproduce G-4aj, that failure is a diagnostic that the proposed symbol-to-quotient bridge is incomplete, rather than a reason to force an algebraic identification.


## 40. G-4ao — first pole-graded calculation: exact differentials eliminate even normal pole layers

Choose an equicharacteristic coefficient-field coordinate \(t\) lifting the residue parameter T, so locally \(S=t^2+p\), with residue field \(E=\mathbb F_2(t)\). The conormal generator is \(dp\), and \(dt\) is tangent. Filter absolute one-forms by pole order in p, with normal layer of pole index m represented by \(c p^{-m}dp\), \(c\in E\).

For a lifted coefficient \(c(t)\) and integer r≥1,
\[
d(c(t)p^{-r})
=p^{-r}c'(t)dt-r c(t)p^{-r-1}dp.
\]
In characteristic two, the leading normal term is present exactly when r is odd:
\[
\operatorname{in}_{\mathrm{nor}}d(c(t)p^{-r})=
\begin{cases}
c(t)p^{-(r+1)}dp,&r\text{ odd},\\
0,&r\text{ even}.
\end{cases}
\]
(The sign is immaterial in characteristic two.) Since c ranges over all residue coefficients, every even-index normal graded layer \(m=r+1\) is hit by a leading exact differential. Thus the associated-graded quotient by exact forms has no even-index normal layer; odd normal pole indices are the candidate surviving layers.

This parity calculation gives a geometric explanation for why the G-4aj normal form is indexed by odd r: it is already forced at the first associated-graded stage by the derivative of the normal parameter. It does **not** yet prove that every odd layer survives the full logarithmic Cartier quotient, nor does it identify the additive G-4aj quotient with Kato cohomology. The tangent term \(p^{-r}c'(t)dt\) is one pole level lower and must be tracked in the filtered complex; the next step is to compute its interaction with Cartier and Frobenius, rather than discard it.

**Coordinate caveat:** this calculation is made after choosing a coefficient field and a lift t. The associated graded and the parity statement are intrinsic, while the displayed splitting into dt and dp depends on that choice.


## 41. G-4ap — tangent constraint on exact normal forms

The first normal-symbol calculation G-4ao is valid as a statement about the *leading normal symbol* of an exact differential, but it does not by itself classify exact relations among forms that are required to remain purely normal. The tangent component cannot simply be discarded when passing to the actual quotient.

Work in the completed local field \(L=E((p))\), \(E=\mathbb F_2(t)\), using the chosen coefficient field. Every \(g\in L\) has a unique Laurent expansion \(g=\sum_n c_n(t)p^n\), with finitely many negative terms. Then
\[
dg=\sum_n c_n'(t)p^n\,dt+\sum_n n c_n(t)p^{n-1}\,dp.
\]
The kernel of \(d/dt:E\to E\) is exactly \(E^2=\mathbb F_2(t^2)\). Therefore \(dg\) is purely normal (has zero \(dt\)-component) if and only if every \(c_n\in E^2\). In characteristic two, only odd n contribute to the second sum. Hence
\[
 dL\cap L,dp
 =\left\{\sum_{n\text{ odd}}c_n p^{n-1}dp:c_n\in E^2\right\}.
\]
Equivalently, for finite normal principal parts, the exact purely-normal relations occur at even pole indices \(m=1-n\), with coefficient in \(E^2\), not arbitrary coefficient in E. Conversely every such finite relation is realized by differentiating \(c^2p^{1-m}\) when m is even.

This corrects any inference that the entire even-index normal coefficient space is removed in the actual quotient by exact forms. The associated-graded leading-normal-symbol statement remains: for odd r, \(d(cp^{-r})\) has leading normal symbol \(cp^{-r-1}dp\), while its tangent term is one pole level lower. But this leading-symbol observation alone does not show that the tangent term can be eliminated in the filtered complex. The exact intersection above is a statement about pure-normal forms in \(\Omega_L^1/dL\), and is not yet the full Cartier quotient \(H_2^2(L)\).

For clarity, the two statements must not be conflated:
- **Leading normal symbol:** all coefficients c appear at even pole index r+1 when r is odd.
- **Exact relation staying purely normal:** only coefficients in \(E^2\) are available at even pole indices.

The next calculation must retain the tangent filtration and the higher Cartier filtration simultaneously. No G-4aj/Kato comparison follows from this result.


## 42. G-4aq — explicit normal principal-part de Rham quotient

Let \(L=E((p))\), \(E=\mathbb F_2(t)\), and let
\[
\operatorname{PP}_{\rm nor}=\bigoplus_{m\ge1}E p^{-m}dp
\]
be the finite normal principal parts. By G-4ap, the exact forms that lie in \(Ldp\) are precisely the sums \(c_np^{n-1}dp\) with n odd and \(c_n\in E^2\). Writing \(m=1-n\), these are exactly the even pole indices with square coefficients. Conversely, for every even m and c∈E, \(d(c^2p^{1-m})=c^2p^{-m}dp\). Hence
\[
\boxed{
\operatorname{PP}_{\rm nor}/(dL\cap\operatorname{PP}_{\rm nor})
\cong
\bigoplus_{m\ge1,\ m\text{ odd}}E p^{-m}dp
\oplus
\bigoplus_{m\ge1,\ m\text{ even}}(E/E^2)p^{-m}dp.
}
\]
This is an exact de Rham quotient of pure normal principal parts. It is not yet the Kato group: the higher Cartier filtration and its interaction with tangent terms have not been imposed. In particular, do not infer the G-4aj normal form from this intermediate quotient. It is a checkpoint for the next filtered Cartier calculation.


## 43. G-4ar — inverse-Cartier recurrence on normal pole symbols

Keep \(L=E((p))\), \(E=\mathbb F_2(t)\), with 2-basis \(\{t,p\}\). The inverse Cartier formula on the normal basis differential is
\[
C^{-1}(h\,dp)=[h^2p\,dp]\quad\text{in }\Omega_L^1/dL.
\]
For \(h=cp^{-m}\), this gives the exact recurrence
\[
C^{-1}(cp^{-m}dp)=[c^2p^{-(2m-1)}dp].
\]
Thus the pole-index map is \(m\mapsto2m-1\), and the residue coefficient is squared. Before quotienting by the higher Cartier filtration, the corresponding \(C^{-1}-1\) expression is represented by
\[
 c^2p^{-(2m-1)}dp+cp^{-m}dp.
\]
At m=1 this is \((c^2+c)p^{-1}dp\), the Artin–Schreier shape. For m>1 it links the m-slot to the (2m−1)-slot. Iterating the index map gives \(m_j=2^j(m-1)+1\).

This is an exact inverse-Cartier calculation modulo exact forms. It is a recurrence on the normal representatives and suggests a chain structure, but it does not yet classify \(H_2^2(L)\): the quotient by \(B_\infty\) must still be imposed, and mixed tangent terms generated in the construction of \(B_i\) must be tracked. In particular, the m=1 Artin–Schreier shape is not by itself a proof that the G-4aj chain-1 summand is the corresponding Kato summand. The next task is to calculate which of these normal symbols lie in \(B_\infty\) and how the recurrence interacts with the exact normal quotient G-4aq.


## 44. G-4as — explicit power subspaces in the higher Cartier filtration

Continue with \(L=E((p))\), \(E=\mathbb F_2(t)\), and the filtration \(B_1=dL\), \(B_{n+1}\) defined by inverse Cartier as in G-4ao. For every even integer \(m\ge2\) and \(a\in E\),
\[
d(a^2p^{1-m})=a^2p^{-m}dp,
\]
since \(d(a^2)=0\) and \(1-m\) is odd. Thus this pure normal form lies in \(B_1\).

Applying inverse Cartier repeatedly, using \(C^{-1}(h dp)=[h^2p dp]\), gives
\[
a^2p^{-m}dp\mapsto a^4p^{-(2m-1)}dp
\mapsto a^8p^{-(4m-3)}dp\mapsto\cdots.
\]
Consequently, for every \(n\ge1\),
\[
\boxed{a^{2^n}p^{-\left(2^{n-1}(m-1)+1\right)}dp\in B_n.}
\]
The pole-index sequence is \(r_j=2^j(m-1)+1\); because m−1 is odd, its jth term has \(v_2(r_j-1)=j\). Thus the filtration contains explicit \(2^n\)-power coefficient subspaces at odd indices with prescribed \(2\)-adic valuation of r−1.

**Scope:** this proves inclusion of the displayed representatives in \(B_n\), not equality for \(B_n\cap Ldp\), and not a full description of \(B_\infty\cap\operatorname{PP}_{\rm nor}\). Mixed tangent forms arising from general exact differentials may contribute additional elements. The next problem is to determine whether these inclusions exhaust the pure-normal part of the filtration, then impose the \(C^{-1}-1\) recurrence on the resulting coefficient quotients. No Kato/G-4aj identification is claimed.


## 45. G-4at — exact pure-normal finite Cartier filtration

The inclusions in G-4as can be sharpened to an equality for finite pure-normal principal parts. Let \(L=E((p))\), \(E=\mathbb F_2(t)\), and let \(B_1=dL\), \(B_{n+1}=C^{-1}(B_n)\) be the standard Cartier filtration on one-forms (with \(C:Z^1\to\Omega_L^1\)). Put
\[
V_n=B_n\cap\bigoplus_{m\ge1}E p^{-m}dp,
\]
where the sum means finite principal parts. Then
\[
\boxed{
V_n=
\bigoplus_{m\ge2,\ m\text{ even}} E^2p^{-m}dp
\ \oplus\!
\bigoplus_{\substack{m\ge3,\ m\text{ odd}\\v_2(m-1)\le n-1}}
E^{2^{v_2(m-1)+1}}p^{-m}dp.
}
\]
There is no pole-index-one summand in any finite \(V_n\).

**Proof.** For \(B_1\), G-4ap gives exactly the even-index terms with square coefficients. For the induction, a pure-normal form \(\omega=\sum c_mp^{-m}dp\) in \(B_n\) is closed. Since \(d\omega=\sum c'_mp^{-m}dt\wedge dp\), every \(c_m\in E^2\). Write \(c_m=b_m^2\). The Cartier formula for the p-basis \(\{t,p\}\) gives
\[
C(b_m^2p^{-m}dp)=
\begin{cases}b_mp^{-(m+1)/2}dp&m\text{ odd},\\0&m\text{ even}.\end{cases}
\]
Distinct odd indices descend to distinct indices, so no cancellation occurs. Thus \(\omega\in B_{n+1}\) exactly when its even-index coefficients are in \(E^2\) and, for each odd \(m\), the square root coefficient at index \((m+1)/2\) belongs to \(V_n\). If m=1 this condition recursively forces the coefficient to be zero, since index one is absent from \(V_1\). For odd m≥3, the recursion gives \(v_2(m-1)\le n\) and coefficient space \(E^{2^{v_2(m-1)+1}}\). This proves the displayed formula by induction.

Taking the union over finite n yields
\[
B_\infty\cap\operatorname{PP}_{\rm nor}=
\bigoplus_{m\ge2,\ m\text{ even}}E^2p^{-m}dp
\oplus\bigoplus_{m\ge3,\ m\text{ odd}}E^{2^{v_2(m-1)+1}}p^{-m}dp.
\]
This is an exact description of the pure-normal finite-principal-part intersection. It does not classify arbitrary mixed forms in \(B_\infty\), nor by itself identify the full Kato quotient after imposing \(C^{-1}-1\). The index-one Artin–Schreier slot remains outside \(B_\infty\), as expected.


## 46. G-4au — pure-normal Cartier–Artin–Schreier chain quotient

Define the explicitly restricted model
\[
Q_{\rm nor}:=\operatorname{PP}_{\rm nor}/\left((B_\infty\cap\operatorname{PP}_{\rm nor})+\langle C^{-1}(\omega)-\omega:\omega\in\operatorname{PP}_{\rm nor}\rangle\right),
\]
where \(\operatorname{PP}_{\rm nor}=\bigoplus_{m\ge1}Ep^{-m}dp\), and inverse Cartier expressions are taken modulo exact forms. This is the quotient generated by pure-normal symbols and pure-normal Cartier relations; it is not asserted to equal the full Kato group, because mixed tangent forms may add relations.

By G-4at, the coefficient spaces before imposing \(C^{-1}-1\) are E at index 1, E/E² at even indices, and E/E^{2^{v_2(m-1)+1}} at odd m≥3. The relation is
\[
e_m(c)+e_{2m-1}(c^2)=0.
\]
At m=1 it gives \(E/\wp(E)\). The indices m≥2 split into disjoint chains starting at an even root e≥2:
\[
e,\ 2e-1,\ 4e-3,\ 8e-7,\ldots.
\]
At the root, the relation eliminates the root slot and leaves the first odd slot (index 2e−1, whose valuation \(v_2((2e-1)-1)=1\)) with coefficient quotient E/E⁴. At every subsequent step, Frobenius identifies the preceding coefficient quotient with the square subspace in the next coefficient quotient; quotienting by that image leaves E/E². Therefore, as an F₂-vector space,
\[
\boxed{Q_{\rm nor}\cong E/\wp(E)
\oplus\bigoplus_{\substack{r\ge3\\r\equiv3\ (4)}}E/E^4
\oplus\bigoplus_{\substack{r\ge5\\r\text{ odd},\ r\equiv1\ (4)}}E/E^2.}
\]
Here every odd r≥5 has \(v_2(r-1)\ge2\); the displayed indexing separates first odd chain positions from later positions. The chain argument is finite-support triangular elimination, with Frobenius inducing the isomorphism \(E/E^{2^j}\to E^2/E^{2^{j+1}}\).

**Scope warning:** \(Q_{\rm nor}\) is a pure-normal subquotient model. It is not a proven subspace or quotient decomposition of the full \(H_2^2(L)\), since relations from mixed \(dt\)-components can further identify or kill normal classes. Comparing this model to the G-4aj local quotient is precisely a test for the missing tangent relations.


## 47. G-4av — correction: chain contributions are direct limits

**Correction to G-4au.** The slot-by-slot decomposition stated there is not valid: the relation at each node identifies the preceding coefficient class with its Frobenius square at the next node. The chain must be treated as a direct limit, not as independent residual quotients at each pole index.

For an even root \(e\ge2\), set \(m_j=2^j(e-1)+1\), so \(m_0=e\) and \(m_{j+1}=2m_j-1\). By G-4at, the coefficient space at node \(m_j\) is
\[
W_j=E/E^{2^{j+1}}.
\]
The Cartier–AS relation induces
\[
F_j:W_j\longrightarrow W_{j+1},\qquad[c]\longmapsto[c^2].
\]
This is well-defined and injective: changing c by an element of \(E^{2^{j+1}}\) changes its square by an element of \(E^{2^{j+2}}\), and \(c^2\in E^{2^{j+2}}\) implies \(c\in E^{2^{j+1}}\). The quotient of the direct sum of the node spaces by the graph relations is therefore exactly
\[
\varinjlim_j(W_j,F_j).
\]
The index-one chain separately contributes \(E/\wp(E)\). Hence the corrected pure-normal model is
\[
\boxed{
Q_{\rm nor}\cong E/\wp(E)\oplus\bigoplus_{e\ge2,\ e\text{ even}}\varinjlim_j(E/E^{2^{j+1}},\mathrm{Frob}).}
\]
For each j, the cokernel of \(F_j\) is naturally \(E/E^2\), since \(W_{j+1}/F_j(W_j)\cong E/(E^2+E^{2^{j+2}})=E/E^2\). As F₂-vector spaces the transition maps split (noncanonically), so each chain colimit is noncanonically isomorphic to \(\bigoplus_{j\ge0}E/E^2\). This vector-space splitting is not canonical and should not be mistaken for a preferred normal form.

The earlier G-4au assertion that each first odd slot independently contributes E/E⁴ and each later slot E/E² is withdrawn. The corrected direct-limit model remains restricted to pure-normal symbols and their own Cartier relations; mixed tangent forms can impose further relations in the full Kato group.


## 48. G-4aw — identify the chain direct limit with the perfection quotient

The direct limit in G-4av has a canonical closed form. Let \(E^{\rm perf}=\bigcup_{n\ge0}E^{1/2^n}\) be the perfect closure of \(E=\mathbb F_2(t)\). At stage j define
\[
\Psi_j:E/E^{2^{j+1}}\longrightarrow E^{\rm perf}/E,
\qquad[c]\longmapsto c^{1/2^{j+1}}+E.
\]
This is well-defined: changing c by \(d^{2^{j+1}}\) changes its root by d∈E. It is injective because \(c^{1/2^{j+1}}\in E\) exactly when \(c\in E^{2^{j+1}}\). It is compatible with Frobenius transitions, since \((c²)^{1/2^{j+2}}=c^{1/2^{j+1}}\). It is surjective on the direct limit because every element of \(E^{\rm perf}\) lies in some \(E^{1/2^n}\). Hence
\[
\boxed{\varinjlim_j(E/E^{2^{j+1}},\mathrm{Frob})\simeq E^{\rm perf}/E.}
\]
Consequently the pure-normal Cartier–AS model has the canonical description
\[
\boxed{Q_{\rm nor}\simeq E/\wp(E)\oplus\bigoplus_{e\ge2,\ e\text{ even}}E^{\rm perf}/E.}
\]
The isomorphism is canonical after the chain roots e are fixed. This identifies each chain with the purely inseparable classes added by perfecting the residue coefficient field. It remains only a pure-normal model; mixed tangent relations can further reduce it in the full Kato quotient.


## 49. G-4ax — complete monomial generators for the mixed B₂ layer

The mixed relation in the previous calculation comes from a uniform monomial formula. Write a Laurent monomial \(f=cp^n\), with \(c=c_0^2+t c_1^2\), \(c_0,c_1\in E\). Then
\[
df=c_1^2p^n dt+ncp^{n-1}dp,
\]
and inverse Cartier gives the closed representative
\[
\boxed{
C^{-1}(df)=t c_1^4p^{2n}dt+n(c_0^4+t^2c_1^4)p^{2n-1}dp.
}
\]
Here n is read in \(\mathbb F_2\). Thus:
- If n is even, the generator is pure tangent: \(t c_1^4p^{2n}dt\).
- If n is odd, it is the sum of a tangent term \(t c_1^4p^{2n}dt\), a pure-normal term \(c_0^4p^{2n-1}dp\), and the mixed normal term \(t^2c_1^4p^{2n-1}dp\).

For n=−r with r positive odd, the mixed normal term has pole index 2r+1 and coefficient \(t^2E^4=S F^2\), where \(S=t^2\), \(F=E^2=\mathbb F_2(S)\). Its tangent partner has pole index 2r and coefficient \(tE^4\). This is the precise first-layer geometric occurrence of the higher-chain coefficient \(S F^2\) from G-4aj.

The formula describes generators of \(B_2=C^{-1}(dL)\) arising from monomials; finite sums give all Laurent-polynomial inputs, and coefficientwise continuity gives the completed statement. It does not say the mixed normal term alone lies in \(B_2\): only the full tangent-plus-normal sum is killed. That distinction is essential for the next quotient calculation.


## 50. G-4ay — logarithmic form of the mixed normal–tangent generator

For n=−r with r≥1 odd, the G-4ax formula separates as
\[
C^{-1}(d(cp^{-r}))=
 c_0^4p^{-(2r+1)}dp
 +t c_1^4p^{-2r}dt+t^2c_1^4p^{-(2r+1)}dp,
\]
where \(c=c_0^2+t c_1^2\). Since \(S=t^2\) and in characteristic two
\[
d\log(t/p)=dt/t+dp/p,
\]
the mixed pair is exactly
\[
\boxed{S c_1^4p^{-2r}d\log(t/p).}
\]
Thus
\[
\boxed{C^{-1}(d(cp^{-r}))=
 c_0^4p^{-(2r+1)}dp+S c_1^4p^{-2r}d\log(t/p).}
\]
Here \(c_1^4\in E^4=F^2\), so the logarithmic coefficient lies in \(S F^2\), exactly the higher-chain coefficient space in G-4aj. The normal and tangent components are the two components of one logarithmic differential along the exceptional divisor; they must be tracked together. This is a concrete geometric match of coefficient spaces, but not yet a proof that the full local quotient has precisely the G-4aj normal form: one must still prove that the logarithmic generators account for all mixed Cartier relations and that no additional relations arise.


## 51. G-4az — location of the logarithmic sector in the perfection chain

Fix an even-root chain with first odd normal index \(m=2r+1\), r odd. Its coefficient space at that node is \(E/E^4\). The mixed logarithmic generator from G-4ay has normal coefficient
\[
A=S c_1^4=t^2c_1^4\in S E^4,
\]
and tangent partner at index 2r. Under the direct-limit identification of G-4aw, the normal coefficient maps to
\[
[A]\longmapsto A^{1/4}+E=t^{1/2}c_1+E.
\]
As c₁ ranges over E, this is the distinguished additive subspace \(t^{1/2}E/E\subset E^{\rm perf}/E\), and the map \(S E^4\to t^{1/2}E/E\) is injective. Under inverse Cartier, the logarithmic form \(\eta_{r,A}=A p^{-2r}d\log(t/p)\) satisfies
\[
C^{-1}(\eta_{r,A})=\eta_{2r,A^2},
\]
so the corresponding coefficient at the next node maps to the same element of the direct limit. Thus the G-4aj coefficient space \(S F^2=S E^4\) is identified with the first purely inseparable layer \(t^{1/2}E/E\) inside each pure-normal perfection chain.

This is a precise embedding of the mixed logarithmic sector into the pure-normal chain model. It does not show that this sector exhausts the full chain contribution or that the complementary layers are killed by all mixed relations. Determining that is the next completeness problem.


## 52. G-4ba — exact tangent principal-part relations at B₁

Let \(\operatorname{PP}_{\rm tan}=\bigoplus_{m\ge1}E p^{-m}dt\). For \(g=\sum_n c_n(t)p^n\),
\[
dg=\sum_n c_n'(t)p^n dt+\sum_n n c_n(t)p^{n-1}dp.
\]
The differential is purely tangent exactly when \(c_n=0\) for every odd n. For even n, the tangent coefficient is \(c_n'\), and \(dE/dt=E^2\), since \(c=c_0^2+t c_1^2\) gives \(c'=c_1^2\). Therefore
\[
\boxed{dL\cap\operatorname{PP}_{\rm tan}=\bigoplus_{m\ge1,\ m\text{ even}}E^2p^{-m}dt.}
\]
This is the tangent counterpart of G-4ap's pure-normal exact relation. At B₁ the two directions are symmetric; the mixed logarithmic coupling first appears in B₂, as in G-4ax–G-4ay.


## 53. G-4bb — complete monomial shape of the second Cartier layer

Modulo B₁, the monomial formula G-4ax gives the following decomposition of the finite-principal-part part of B₂. For negative even exponent n=−2k, k≥1, one gets a pure tangent term
\[
tE^4p^{-4k}dt.
\]
For negative odd exponent n=−r, r≥1 odd, one gets
\[
tE^4p^{-2r}dt
+E^4p^{-(2r+1)}dp
+SE^4p^{-(2r+1)}dp.
\]
The last two normal coefficient spaces are complementary inside E² because \(E²=E^4\oplus SE^4\). Thus, for each odd r, the second Cartier layer has:
- a tangent component \(tE^4\) at pole index 2r;
- a pure-normal component \(E^4\) at normal pole index 2r+1;
- a mixed-normal component \(SE^4\) at the same normal pole index, paired with the tangent component.

Together with B₁, which contributes square-coefficient tangent and normal principal parts at even pole indices, this describes the monomial-generated finite-principal-part B₂ layer. The decomposition is direct at the displayed coefficient slots: \(E²\cap tE^4=0\), and \(E^4\cap SE^4=0\). Distinct Laurent exponents do not cancel. This is a complete B₂ calculation for finite Laurent inputs; the extension to arbitrary completed inputs follows coefficientwise when the relevant topology is fixed.

This makes the geometry of the G-4aj coefficient transparent: \(SE^4\) is not the pure-normal B₂ piece but the normal half of a mixed tangent/logarithmic generator. The next task is to iterate this paired decomposition through B₃ and beyond, and determine whether its full Cartier orbit exhausts the mixed constraints needed for the G-4aj normal form.


## 54. G-4bc — iterated mixed logarithmic Cartier generators

For every j≥1, positive odd r, and b∈E, define
\[
\eta_{j,r,b}=S^{2^{j-1}}b^{2^{j+1}}p^{-2^jr}d\log(t/p).
\]
Writing \(A=S^{2^{j-1}}b^{2^{j+1}}\), the two components are \((A/t)p^{-2^jr}dt\) and \(A p^{-(2^jr+1)}dp\). Since \(A\in E^2\), inverse Cartier gives
\[
C^{-1}(\eta_{j,r,b})=\eta_{j+1,r,b}.
\]
Thus the mixed logarithmic sector is stable under inverse Cartier, with the pole indices doubling and the coefficient squaring.

At the same normal pole index \(m=2^jr+1\), the pure-normal generator has coefficient space \(E^{2^{j+1}}\), while the mixed-normal component has coefficient space
\[
S^{2^{j-1}}E^{2^{j+1}}=t^{2^j}E^{2^{j+1}}.
\]
Because \(E^{2^j}=E^{2^{j+1}}\oplus t^{2^j}E^{2^{j+1}}\), these are complementary and together span the full coefficient space \(E^{2^j}\). The mixed summand is paired with the tangent component \(t^{2^j-1}E^{2^{j+1}}p^{-2^jr}dt\).

This yields the complete shape of the iterated monomial generators of \(B_\infty\) on finite principal parts: B₁ contributes pure tangent and pure normal square-coefficient terms at even pole indices; for each j≥1, r odd, and b∈E, there are (i) pure-normal terms \(b^{2^{j+1}}p^{-(2^jr+1)}dp\), (ii) mixed logarithmic terms \(\eta_{j,r,b}\), and (iii) pure-tangent terms \(t^{2^j-1}b^{2^{j+1}}p^{-2^{j+1}k}dt\) for k≥1. These arise by applying inverse Cartier j times to exact monomials with odd or even p-exponent, respectively. Distinct pole indices and the displayed complementary coefficient decompositions give the finite-principal-part normal/tangent organization.

This is a description of the Cartier filtration generators, not yet of the quotient by \(C^{-1}-1\). The remaining step is to impose that operator on the paired tangent/logarithmic sector and prove that its cokernel yields the G-4aj higher-chain summands without extra classes.


## 55. G-4bd — all finite-principal-part Cartier generators by level

The monomial calculation gives a uniform description of the finite-principal-part generators of the full Cartier filtration. B₁ contributes pure tangent and pure normal terms \(E²p^{-m}dt\) and \(E²p^{-m}dp\) at even pole indices m.

For each level j≥1, each positive odd r, and each b∈E, inverse Cartier iterates of the exact monomial inputs give:
\[
\begin{aligned}
\nu_{j,r,b}&=b^{2^{j+1}}p^{-(2^jr+1)}dp,\\
\eta_{j,r,b}&=S^{2^{j-1}}b^{2^{j+1}}p^{-2^jr}d\log(t/p),\\
\tau_{j,k,b}&=t^{2^j-1}b^{2^{j+1}}p^{-2^{j+1}k}dt\quad(k\ge1).
\end{aligned}
\]
Here \(\nu\) is pure normal, \(\eta\) is mixed logarithmic, and \(\tau\) is pure tangent. The mixed family satisfies \(C^{-1}(\eta_{j,r,b})=\eta_{j+1,r,b}\); the pure families propagate by the same coefficient-squaring and pole-doubling rule.

At normal pole index \(m=2^jr+1\), the pure-normal coefficient space is \(E^{2^{j+1}}\), while the mixed-normal coefficient space is
\[
S^{2^{j-1}}E^{2^{j+1}}=t^{2^j}E^{2^{j+1}}.
\]
These are complementary in \(E^{2^j}\). The mixed coefficient is paired with tangent coefficient \(t^{2^j-1}E^{2^{j+1}}\) at pole index \(2^jr\). At tangent pole indices divisible by \(2^{j+1}\), the pure tangent coefficient space is \(t^{2^j-1}E^{2^{j+1}}\).

These families, together with B₁, give all finite-principal-part generators obtained by iterating inverse Cartier on exact Laurent monomials: decompose each coefficient as \(c_0²+t c_1²\), and treat even and odd p-exponents separately. Thus the finite-principal-part filtration is now explicitly organized into pure normal, pure tangent, and mixed logarithmic pieces. The remaining Kato problem is the cokernel of \(C^{-1}-1\) on this paired system, with exact differentials already accounted for; this is where the G-4aj local normal form must be recovered.


## 56. G-4be — corrected complete Cartier tower including the B₁ mixed term

**Refinement of G-4bd:** B₁ itself has mixed exact principal parts, so the logarithmic tower starts at j=0, not j=1. For an odd negative exponent n=−r and \(c=c_0²+t c_1²\),
\[
d(cp^{-r})=c_1²p^{-r}dt+c_0²p^{-(r+1)}dp+t c_1²p^{-(r+1)}dp.
\]
The last two terms split into a pure-normal exact term and a mixed logarithmic exact term:
\[
 c_0²p^{-(r+1)}dp,
\qquad
 t c_1²p^{-r}d\log(t/p).
\]
Thus, for every j≥0, odd r and b∈E, the iterated Cartier families are
\[
\begin{aligned}
\nu_{j,r,b}&=b^{2^{j+1}}p^{-(2^jr+1)}dp,\\
\eta_{j,r,b}&=t^{2^j}b^{2^{j+1}}p^{-2^jr}d\log(t/p).
\end{aligned}
\]
The mixed family obeys \(C^{-1}(\eta_{j,r,b})=\eta_{j+1,r,b}\). For even negative exponents n=−2k, the pure tangent family is
\[
\tau_{j,k,b}=t^{2^j-1}b^{2^{j+1}}p^{-2^{j+1}k}dt,
\qquad j\ge0, k\ge1.
\]
At j=0 this is \(b²p^{-2k}dt\), the pure tangent exact term in B₁. Together these families give all finite-principal-part generators obtained by iterating inverse Cartier on exact Laurent monomials; coefficient decomposition \(c=c_0²+t c_1²\) and parity of n prove completeness.

At normal pole index \(m=2^jr+1\), the pure-normal coefficient space is \(E^{2^{j+1}}\), and the mixed-normal coefficient space is \(t^{2^j}E^{2^{j+1}}\). They complement to \(E^{2^j}\). The mixed component is paired with tangent coefficient \(t^{2^j-1}E^{2^{j+1}}\) at tangent pole index \(2^jr\). Thus the full finite-principal-part Cartier filtration is organized by pure-normal, pure-tangent, and mixed logarithmic families from level j=0 onward.

This corrects the incomplete B₁ description in G-4bd: B₁ is not merely the sum of pure tangent and pure normal intersections; it also contains the mixed exact logarithmic pairs above. The full \(C^{-1}-1\) cokernel is still the remaining task.


## 57. G-4bf — odd-pole normal coefficient splitting matches G-4aj

Let \(F=E²=\mathbb F_2(S)\), \(S=t²\). For every odd normal pole index m≥3, write
\[
j=v_2(m-1)\ge1,\qquad r=(m-1)/2^j\quad(r\text{ odd}).
\]
The pure-normal Cartier generator at this slot has coefficient space
\[
E^{2^{j+1}}=F^{2^j}.
\]
The mixed logarithmic generator has normal coefficient space
\[
t^{2^j}E^{2^{j+1}}=S^{2^{j-1}}F^{2^j},
\]
paired with tangent coefficient \(t^{2^j-1}E^{2^{j+1}}\) at tangent pole index \(2^jr\). These two spaces are complementary in
\[
E^{2^j}=F^{2^{j-1}}=F^{2^j}\oplus S^{2^{j-1}}F^{2^j}.
\]
The mixed coefficient space is canonically isomorphic to \(S F²\) by inverse Frobenius:
\[
S^{2^{j-1}}b^{2^j}\longmapsto S b².
\]
Thus every odd normal pole index m≥3 carries exactly the same abstract coefficient space \(S F²\) in its tangent-coupled graded component. This recovers the higher-chain coefficient space in G-4aj at all odd indices, not only those congruent to 3 modulo 4. The pole-index-one component is exceptional and remains the Artin–Schreier summand \(F/\wp(F)\).

**Scope:** this is an exact splitting of the coefficient spaces in the iterated Cartier generators and a canonical identification of the mixed graded coefficient component. It is not yet a proof that the full local quotient is the direct sum in G-4aj: one must still prove that the mixed tangent relations create no further dependencies among the \(S F²\) components and leave no additional classes.


## 58. G-4bg — index-one Artin–Schreier coefficient bridge

The geometric coefficient field \(E=\mathbb F_2(t)\) and scalar coefficient field \(F=\mathbb F_2(S)\) satisfy \(E=F(t)\), \(t²=S\). Every c∈E is uniquely \(c=a+bt\), a,b∈F. Define the additive map
\[
\rho:E\to F,\qquad \rho(a+bt)=a+Sb².
\]
It induces an isomorphism
\[
\boxed{E/\wp_E(E)\xrightarrow{\sim}F/\wp_F(F).}
\]
Indeed, for u,v∈F,
\[
\wp_E(u+vt)=(u²+u+Sv²)+vt,
\]
so \(\rho(\wp_E(u+vt))=u²+u=\wp_F(u)\). Surjectivity is immediate from \(\rho(a)=a\). If \(\rho(a+bt)=\wp_F(u)\), then
\[
a+bt=\wp_F(u)+(Sb²+bt)=\wp_E(u)+\wp_E(bt)=\wp_E(u+bt),
\]
so the induced map is injective.

This resolves the apparent mismatch between the geometric index-one coefficient \(E/\wp(E)\) and the scalar local normal-form coefficient \(F/\wp(F)\) in G-4aj. Combined with G-4bf, which identifies each higher odd-pole mixed coefficient with \(S F²\), the geometry now reproduces every coefficient space in the G-4aj normal form.

**Scope:** matching all coefficient spaces is not yet a proof that the geometric filtration and the scalar quotient have identical relations. The remaining theorem is to prove that the mixed tangent relations impose exactly the G-4ai/G-4aj relations and no others, including the independence of the resulting higher-chain summands.


## 59. G-4bh — logarithmic-coordinate presentation of the Cartier filtration

Use the logarithmic basis \((d\log t,d\log p)\). In the inverse-Cartier representative convention,
\[
C^{-1}(A\,d\log t+B\,d\log p)
=[A²d\log t+B²d\log p]\quad\bmod dL.
\]
For a finite Laurent monomial \(f=cp^n\), write uniquely \(c=a+bt\) with a,b∈F=E²=\mathbb F_2(S). Then
\[
df=(tb\,d\log t+n(a+bt)\,d\log p)p^n.
\]
Its j-fold inverse-Cartier representative is
\[
\boxed{\big(t^{2^j}b^{2^j},\ (n\bmod2)^{2^j}(a+bt)^{2^j}\big)p^{2^jn},}
\]
where for j=0 the second component is n(a+bt), and for j≥1 it is zero if n is even and \((a+bt)^{2^j}\) if n is odd. Equivalently, the pair is \(((tb)^{2^j},(nc)^{2^j})p^{2^jn}\) for every j≥0.

Every finite Laurent input is a finite sum of monomials, so these pairs generate the finite-principal-part Cartier filtration. This gives a compact two-coordinate presentation: the Cartier operation itself is coefficientwise Frobenius in logarithmic coordinates; all geometric coupling is encoded in the exact-input pairs \((tb,n(a+bt))\). It is the appropriate starting point for comparing the full mixed relation system with G-4ai/G-4aj.

**Scope:** this is a representative-level description of the iterated inverse-Cartier images of finite Laurent exact forms. For arbitrary completed series, one must specify the topology and continuity of the chosen Cartier representatives before extending the generation statement. The Kato quotient still requires imposing the full \(C^{-1}-1\) relations and proving the resulting normal form.


## 60. G-4bi — full two-coordinate exponent-orbit presentation

Work in logarithmic coordinates \(d\log t,d\log p\), with coefficient space \(V=E\oplus E\). For a nonzero odd integer r, consider the exponent-doubling orbit \(r,2r,4r,\ldots\). At stage j, the exponent is \(2^jr\). The Cartier relation identifies \((A,B)\) at stage j with \((A²,B²)\) at stage j+1.

The exact-form relations at stage j are generated by the j-fold Cartier image of an exact input at the root exponent r,
\[
G_j=\{(t^{2^j}b^{2^j},(a+bt)^{2^j}):a,b\in F\},
\]
and by the Cartier images of exact inputs at the intermediate even exponents \(2^\ell r\), 1≤ℓ≤j. These latter relations are the tangent-only subspaces
\[
(t^{2^k}F^{2^k},0),\qquad 0≤k<j,
\]
where k=j−ℓ. Thus put
\[
R_{r,j}=G_j+\sum_{k=0}^{j-1}(t^{2^k}F^{2^k},0)\subset E\oplus E,
\qquad V_{r,j}=(E\oplus E)/R_{r,j}.
\]
The Frobenius map \((A,B)\mapsto(A²,B²)\) sends \(R_{r,j}\) into \(R_{r,j+1}\), so it induces transition maps. The contribution of this nonzero exponent orbit to the finite-principal-part Kato presentation is therefore
\[
\boxed{\varinjlim_j(V_{r,j},\mathrm{Frob}).}
\]
This presentation retains both logarithmic directions and all exact-form relations; unlike the earlier pure-normal model, it does not discard the tangent partner. Positive and negative odd roots r label distinct exponent orbits.

The exponent-zero orbit is separate because doubling fixes zero rather than moving along an infinite chain. It must be treated as the cokernel of coefficient Frobenius-minus-identity on \(E\oplus E\), modulo the Cartier iterates of the exact pairs \((tb,0)\), b∈F. This is not included in the displayed nonzero-orbit direct sum.

**Scope:** the decomposition is exact for finite Laurent principal parts, where all sums have finite support. Passing to the completed Laurent field requires specifying the topology and proving continuity/closedness of the relation subspaces. Simplifying the direct limits and comparing their result with G-4aj remain open.


## 61. G-4bj — perfect-closure quotient for each nonzero exponent orbit

The direct limit in G-4bi admits a canonical realization inside \((E^{\rm perf})²\). At stage j, map
\[
(A,B)\longmapsto(A^{1/2^j},B^{1/2^j}).
\]
These maps are compatible with the Frobenius transitions and their union identifies the ambient direct limit with \((E^{\rm perf})²\). Under this map, the root graph \(G_j\) becomes the fixed subspace
\[
G_0=\{(tb,a+bt):a,b\in F\}.
\]
The intermediate tangent subspace \((t^{2^k}F^{2^k},0)\), k<j, becomes
\[
(t^{1/2^{j-k}}F^{1/2^{j-k}},0).
\]
Taking the union over stages gives
\[
U_\infty=\sum_{h\ge1}t^{1/2^h}F^{1/2^h}\subset E^{\rm perf}.
\]
Consequently each nonzero exponent orbit has the canonical presentation
\[
\boxed{(E^{\rm perf}\oplus E^{\rm perf})/(G_0+(U_\infty,0)).}
\]
This removes the explicit Frobenius direct-limit notation. The remaining algebraic task is to describe \(U_\infty\), then simplify the residual graph relation and compare the resulting quotient with the higher-chain \(S F²\) summands in G-4aj. Positive and negative odd roots still give distinct copies; exponent zero remains separate.


## 62. G-4bk — simplify each negative exponent orbit to two residue-field copies

Let \(E_h=F^{1/2^h}\), so \(E_0=F\), \(E_1=E=F(t)\), and \(E_{h+1}=E_h(t^{1/2^h})\). The extension has degree two and
\[
E_{h+1}=E_h\oplus t^{1/2^h}E_h.
\]
The tangent relation space in G-4bj is therefore
\[
U_\infty=\bigoplus_{h\ge1}t^{1/2^h}E_h,
\]
a canonical additive complement to E in \(E^{\rm perf}\). Thus quotienting the first coordinate by \(U_\infty\) reduces the orbit presentation to \((E\oplus E)/G_0\).

Write \(A=A_0+tA_1\), \(B=B_0+tB_1\), with coefficients in F. The map
\[
\Phi:E\oplus E\to F\oplus F,
\qquad (A,B)\mapsto(A_0,A_1+B_1)
\]
is surjective and has kernel exactly
\[
G_0=\{(tb,a+bt):a,b\in F\},
\]
since \(G_0\) has coordinates \((A_0,A_1,B_0,B_1)=(0,b,a,b)\). Consequently
\[
\boxed{(E^{\rm perf}\oplus E^{\rm perf})/(G_0+(U_\infty,0))\simeq F\oplus F.}
\]
Every negative exponent orbit \(-r,-2r,-4r,\ldots\), r positive odd, therefore contributes exactly two additive copies of F to the finite-principal-part Kato presentation. The two coordinates are the constant-in-t component of the first logarithmic coefficient and the sum of the t-components of the two logarithmic coefficients.

This is an exact computation for each negative orbit. It does not yet include the exponent-zero orbit or establish a topological completion statement for the full Laurent field.


## 63. G-4bl — exponent-zero orbit and complete finite-polar-part presentation

At exponent zero, Frobenius fixes the exponent. The exact differential of c=a+bt∈E, a,b∈F, has logarithmic coefficient pair \((tb,0)\). The \(C^{-1}-1\) relation is coordinatewise Artin–Schreier. Since the Frobenius relation identifies every iterate of \((tb,0)\) with its initial class, the zero-orbit quotient is
\[
\frac{E\oplus E}{(tF,0)+(\wp_E(E),\wp_E(E))}
\simeq \frac{E}{tF+\wp_E(E)}\oplus\frac{E}{\wp_E(E)}.
\]
The second factor is \(F/\wp_F(F)\) by G-4bg. For the first, write c=a+bt and project modulo tF. The image of \(\wp_E(c)=a²+a+Sb²+bt\) is \(\wp_F(a)+Sb²\), so
\[
\boxed{E/(tF+\wp_E(E))\simeq F/(\wp_F(F)+SF²).}
\]
Therefore the zero-exponent contribution is
\[
\boxed{F/(\wp(F)+SF²)\oplus F/\wp(F).}
\]

Combining this with G-4bk gives the complete finite-polar-part presentation
\[
\boxed{
\mathcal H_{\rm pol}\simeq F/(\wp(F)+SF²)\oplus F/\wp(F)
\oplus\bigoplus_{r\ge1,\ r\text{ odd}}(F\oplus F).
}
\]
Here \(\mathcal H_{\rm pol}\) means the quotient of finite logarithmic differential principal parts with exponents n≤0 by exact differentials and the inverse-Cartier-minus-identity relations. Negative exponent orbits are indexed by negative odd roots −r. The decomposition is algebraic and finite-support; it does not yet assert a completed-field/topological isomorphism for all Laurent series.

This result gives a precise two-component contribution at every negative odd pole orbit, plus the two distinct zero-orbit terms. The comparison with the scalar quotient G-4aj must now be understood as a projection/subquotient question, not as equality of the full two-coordinate Kato model with the one-coordinate scalar normal form.


## 64. G-4bm — correction: the second-coordinate perfection tail survives

**Correction to G-4bk and G-4bl.** The simplification there incorrectly quotiented the second logarithmic coordinate by \(U_\infty\). The tangent-only relations \((U_\infty,0)\) occur in the first coordinate only. They do not remove the perfection tail in the second coordinate.

Since \(E^{\rm perf}=E\oplus U_\infty\),
\[
\frac{(E^{\rm perf})²}{G_0+(U_\infty,0)}
\simeq \frac{E\oplus E^{\rm perf}}{G_0}
\simeq \left(\frac{E\oplus E}{G_0}\right)\oplus E^{\rm perf}/E.
\]
The explicit map \((A,B)\mapsto(A_0,A_1+B_1)\) from G-4bk identifies \((E\oplus E)/G_0\) with \(F\oplus F\). Therefore the corrected contribution of each negative odd exponent orbit is
\[
\boxed{F\oplus F\oplus E^{\rm perf}/E.}
\]
The earlier G-4bk assertion that the whole orbit quotient is just F⊕F is withdrawn; it computed only the finite E⊕E graph quotient and omitted the residual second-coordinate perfection tail.

Accordingly, the corrected finite-polar-part presentation is
\[
\boxed{
F/(\wp(F)+SF²)\oplus F/\wp(F)
\oplus\bigoplus_{r\ge1,\ r\text{ odd}}\left(F\oplus F\oplus E^{\rm perf}/E\right).
}
\]
The exponent-zero terms from G-4bl are unchanged. This remains an algebraic finite-support statement, not yet a topological completion theorem.


## 65. G-4bn — recover the scalar local normal form as a quotient of the geometric polar model

The corrected negative-orbit contribution from G-4bm is
\[
F\oplus F\oplus E^{\rm perf}/E.
\]
The inseparable tail has the canonical layer decomposition
\[
E^{\rm perf}/E=\bigoplus_{h\ge1}U_h,
\qquad U_h=t^{1/2^h}F^{1/2^h},
\]
because, with \(E_h=F^{1/2^h}\), one has \(E_{h+1}=E_h\oplus t^{1/2^h}E_h\).

For every h≥1 define
\[
\theta_h:U_h\to SF²,
\qquad t^{1/2^h}x\longmapsto Sx^{2^{h+1}}.
\]
This is an additive isomorphism: \(x\mapsto x^{2^{h+1}}\) maps \(F^{1/2^h}\) bijectively onto F², and multiplication by S identifies F² with SF².

A negative exponent orbit is rooted at \(-q\), q≥1 odd. Its hth perfection layer corresponds to scalar odd pole index
\[
m=2^h q+1.
\]
Every odd m≥3 occurs exactly once, since \(m-1=2^h q\) has a unique 2-adic valuation h≥1 and odd part q. Thus the direct sum of all perfection tails, over all negative odd roots q, maps bijectively to
\[
\bigoplus_{m\ge3,\ m\text{ odd}}SF²,
\]
with the coefficient at m given by \(\theta_h\).

The zero-exponent contribution from G-4bl is
\[
F/(\wp(F)+SF²)\oplus F/\wp(F).
\]
Projecting onto the second factor gives the index-one Artin–Schreier component. Projecting each negative orbit onto its perfection tail and applying \(\theta_h\) gives every higher scalar component. Therefore there is a coordinate-defined surjection from the finite-polar geometric Cartier quotient onto
\[
\boxed{F/\wp(F)\oplus\bigoplus_{m\ge3,\ m\text{ odd}}SF²,}
\]
which is exactly the G-4aj scalar local normal form. Its kernel is explicitly the zero-mode summand \(F/(\wp(F)+SF²)\) together with the two F-components from each negative exponent orbit.

This establishes a complete match of pole indexing and coefficient spaces, and realizes the scalar quotient as a quotient of the full two-coordinate finite-polar model. **Remaining identification problem:** prove that this coordinate-defined projection agrees with the map induced by the original quaternion boundary symbols \([aS,S)_2\), rather than merely being an abstract/coordinate-defined quotient with the same normal form. Completion/topological issues also remain outside the finite-support setting.


## 66. G-4bo — correct the scalar pole/Cartier orbit shift and identify the symbol projection

**Correction to the indexing in G-4bn:** the scalar differential representative is \(a\,dp\), while the Cartier orbit is written in the logarithmic basis \(d\log p=dp/p\). Hence a scalar coefficient with pole \(p^{-m}\) occurs at logarithmic exponent \(-(m-1)\), not \(-m\).

Write an odd scalar pole index m≥3 uniquely as
\[
m=2^j q+1,\qquad j\ge1,\quad q\ge1\text{ odd}.
\]
The logarithmic exponent \(-2^j q\) belongs to the negative orbit rooted at \(-q\). Its coefficient \(S c²\), with c∈F, is transported to the direct-limit root by taking the \(2^j\)-th root:
\[
(S c²)^{1/2^j}=t^{1/2^{j-1}}c^{1/2^{j-1}}.
\]
For j=1 this is \(tc\in E\). In the graph quotient \((E\oplus E)/G_0\), the pure-normal pair \((0,tc)\) maps under \((A,B)\mapsto(A_0,A_1+B_1)\) to \((0,c)\). Thus the second F-coordinate of each negative orbit gives the first scalar pole \(m=2q+1\), via \(c\mapsto Sc²\).

For j≥2, the root lies in the perfection layer
\[
U_{j-1}=t^{1/2^{j-1}}F^{1/2^{j-1}},
\]
and the isomorphism
\[
\theta_{j-1}:U_{j-1}\to SF²,
\qquad t^{1/2^{j-1}}x\mapsto Sx^{2^j}
\]
sends it to \(Sc²\). Thus the tail layers map to scalar poles \(m=2^{h+1}q+1\), h≥1. Together with the first F-coordinate at j=1, this accounts for every odd scalar pole m≥3 exactly once.

At exponent zero, the second summand \(F/\wp(F)\) maps to the scalar pole-one Artin–Schreier component. Therefore the coordinate-defined scalar projection is
\[
\mathcal H_{\rm pol}\twoheadrightarrow F/\wp(F)\oplus\bigoplus_{m\ge3,\ m\text{ odd}}SF²,
\]
with kernel exactly the zero-mode factor \(F/(\wp(F)+SF²)\) and the first F-coordinate from each negative exponent orbit. This corrects G-4bn's one-step shift and its overlarge kernel claim.

Finally, for the original quaternion symbol, the standard differential representative of \([aS,S)_2\) is \(aS\,d\log S=a\,dS=a\,dp\), since \(S=t²+p\) and \(d(t²)=0\). Thus its logarithmic coefficient is precisely \(ap\) in the \(d\log p\) coordinate. On the scalar normal-form generators \(a=Sc²p^{-m}\), the orbit computation above gives exactly the coefficient maps \(c\mapsto Sc²\). This verifies the projection on the normal-form generators of the scalar quotient. The remaining formal step is to check the map on arbitrary representatives and the completed topology; the generator-level comparison is now explicit.


## 67. G-4bp — compatibility with the original quaternion boundary symbols

The coordinate-defined projection in G-4bo agrees with the original quaternion-symbol map on the complete scalar normal-form basis. In characteristic two, the differential symbol representative is
\[
[aS,S)_2\longleftrightarrow aS\,d\log S=a\,dS=a\,dp,
\]
since \(S=t²+p\) and \(d(t²)=0\). Hence in logarithmic coordinates the symbol has pair \((0,ap)\).

For the pole-one basis generator \(a=c p^{-1}\), the log exponent is zero and the second coordinate is c. The zero-orbit projection \(E/\wp_E(E)\to F/\wp_F(F)\) from G-4bg sends c∈F to its class [c], exactly the scalar AS basis element.

For a higher scalar basis generator \(a=Sc²p^{-m}\), m≥3 odd, write \(m-1=2^j q\), q odd and j≥1. Its log coefficient is \(Sc²p^{-2^jq}\), at stage j of the orbit rooted at −q. Taking the \(2^j\)-th root gives \(t^{1/2^{j-1}}c^{1/2^{j-1}}\). If j=1, the graph quotient invariant \(A_1+B_1\) is c, and its scalar image is \(Sc²\). If j≥2, the root lies in \(U_{j-1}\), and \(\theta_{j-1}\) sends it to \(Sc²\). Thus every higher scalar basis generator maps to its identical coefficient in \(SF²\).

The G-4aj normal form is a direct sum with precisely these pole-one and higher odd-pole generators. Both maps are additive, and every scalar class is a finite linear combination of this basis. Therefore agreement on these generators proves that the coordinate-defined quotient projection is the original quaternion differential-symbol boundary map on the entire algebraic scalar quotient. This closes the algebraic symbol-compatibility step; it does not by itself prove a topological identification of the full completed Kato group beyond the finite-polar-part subspace.


## 68. G-4bq — coefficient-field correction in the quaternion-symbol comparison

**Refinement of G-4bp:** the base-field element S is not literally the geometric coefficient-field square t². In the chosen equicharacteristic coordinate,
\[
S_{\rm base}=t²+p.
\]
Therefore for a higher scalar normal-form generator \(a=S_{\rm base}c²p^{-m}\), m≥3 odd, the differential symbol is
\[
a\,dp=(t²c²p^{-(m-1)}+c²p^{-(m-2)})\,dp.
\]
In logarithmic coordinates this has the two terms
\[
(t²c²p^{-(m-1)+1})d\log p+(c²p^{-(m-2)+1})d\log p.
\]
The second term has logarithmic exponent \(-(m-3)\) if expressed after multiplying by p; equivalently, in the dp coefficient it is at pole order m−2. Its coefficient c² lies in F and its logarithmic exponent is an odd integer (because m−3 is even; the p-exponent in the log coefficient is −(m−3)). More directly, in the orbit presentation the scalar normal term \(c²p^{-(m-2)}dp\) is \(c²p^{-(m-3)}d\log p\). Its coefficient belongs to F and is killed by the root exact graph whenever the exponent \(-(m-3)\) is a negative odd root; for m=3 it is exponent zero and is handled by the zero-mode relation. Thus this adjacent term contributes no higher scalar normal-form class.

The first term is
\[
t²c²p^{-(m-1)}dp=t²c²p^{-(m-2)}d\log p.
\]
Writing \(m-1=2^j q\), j≥1, q odd, its logarithmic exponent is \(-(m-2)=-(2^j q-1)\), so the exact orbit indexing must be read from the logarithmic coefficient, not from the dp pole order alone. The scalar normal-form comparison is therefore made after the full dp-to-dlog conversion and the root-graph reduction; G-4bp's shorthand that treated S as the coefficient-field element without displaying the adjacent term is incomplete.

**Outstanding verification:** redo the pole-index bookkeeping in the symbol map with the exact logarithmic exponents in both terms above. Do not use the simplified G-4bo correspondence until this adjacent-term calculation is fully reconciled with the (m=2^j q+1) orbit indexing.


## 69. G-4br — exact logarithmic exponents and completion of the adjacent-term check

Correct the exponent wording in G-4bq. Starting from \(a=S_{\rm base}c²p^{-m}\), m odd≥3, and using \(S_{\rm base}=t²+p\), one has
\[
a\,dp=t²c²p^{-m}dp+c²p^{-(m-1)}dp.
\]
Since \(dp=p\,d\log p\), the logarithmic-coordinate expression is
\[
\boxed{a\,dp=t²c²p^{-(m-1)}d\log p+c²p^{-(m-2)}d\log p.}
\]
The second log exponent is \(-(m-2)\), which is a negative odd integer. It is the root stage (j=0) of its exponent-doubling orbit, and its coefficient c²∈F is killed by the root exact graph \(G_0\), which contains \((0,a)\) for every a∈F.

The first term has exponent \(-(m-1)=-2^j q\), with j=v₂(m−1)≥1 and q odd. Its coefficient is t²c². Taking the \(2^j\)-th root gives
\[
(t²c²)^{1/2^j}=t^{1/2^{j-1}}c^{1/2^{j-1}}.
\]
For j=1 this is tc, whose graph-quotient invariant is c in the second F-coordinate. For j≥2 it lies in \(U_{j-1}\), and the map \(\theta_{j-1}\) sends it to \(Sc²\in SF²\). Thus the surviving term maps to exactly the scalar normal-form coefficient, while the adjacent term is killed by the root exact relation.

This completes the coefficient-field correction: G-4bp's symbol compatibility is valid after including the adjacent term explicitly. The erroneous intermediate exponent \(-(m-3)\) in G-4bq is withdrawn; the correct exponent is \(-(m-2)\).


## 70. G-4bs — positive-tail contraction and completed local Kato quotient

Let \(L=E((p))\) with logarithmic differential module \(\Omega_L^1=L,d\log t\oplus L,d\log p\), equipped with the p-adic topology. In these coordinates inverse Cartier has representative
\[
F_C(A,d\log t+B,d\log p)=A²d\log t+B²d\log p,
\]
and doubles the p-exponent. If \(\omega_+\in p\Omega^1_{E[[p]]}\), then
\[
\eta=\sum_{k=0}^{\infty}F_C^k(\omega_+)
\]
converges p-adically, since \(v_p(F_C^k\omega_+)\ge2^k\). Telescoping gives
\[
(1-F_C)\eta=\omega_+-\lim_{N\to\infty}F_C^{N+1}(\omega_+)=\omega_+.
\]
Thus every positive-power tail vanishes in the cokernel of \(1-C^{-1}\). The negative part of a Laurent series is finite, and exponent zero is fixed by Frobenius, so the full completed local quotient is determined by the finite negative principal parts and the zero mode. No additional positive-tail classes occur.

Combining G-4bl and G-4bm, the completed local Kato group in this two-dimensional p-basis model is therefore algebraically
\[
\boxed{
H_2^2(L)\simeq F/(\wp(F)+SF²)\oplus F/\wp(F)
\oplus\bigoplus_{q\ge1,\ q\text{ odd}}\left(F\oplus F\oplus E^{\rm perf}/E\right),
}
\]
with the topology used only to contract the positive tail. The direct-sum terms are finite-support negative exponent orbits. The scalar quaternion boundary quotient is obtained from this full Kato group by the projection in G-4bo/G-4br: retain the zero-mode \(F/\wp(F)\), the second F-coordinate at stage one of each negative orbit, and all later perfection layers; discard the zero-mode \(F/(\wp(F)+SF²)\) and the first F-coordinate of each orbit.

**Scope:** this calculation is for the completed field with the chosen coefficient-field parameter t and p-basis \(\{t,p\}\). Any comparison under a different coefficient-field section must transport the logarithmic coordinates and filtration accordingly.


## 71. G-4bt — separate the base parameter from the coefficient-field square

To prevent a notational collision in G-4bs–G-4br, write \(S_0\) for the original rational-function parameter in \(F_0=\mathbb F_2(S_0)\), and write
\[
\Sigma=t²=S_0+p
\]
for the square of the chosen coefficient-field parameter in \(E=\mathbb F_2(t)\). The coefficient field used in the logarithmic Cartier computation is
\[
F_c=E²=\mathbb F_2(\Sigma),
\]
whereas the scalar normal-form quotient G-4aj is expressed over \(F_0\) and uses \(S_0\). These are related inside the completion by \(S_0=\Sigma+p\), not by equality.

Accordingly, every occurrence of \(F,S\) in the geometric Cartier formulas G-4ap–G-4bs means \(F_c,\Sigma\). Every occurrence of \(F,S\) in the scalar normal form G-4aj means \(F_0,S_0\). The symbol comparison G-4br explicitly uses \(S_0=\Sigma+p\) and is the bridge between these two coefficient-field sections. This distinction is essential: replacing \(S_0\) by \(\Sigma\) before expanding in p would erase the adjacent-pole term that is killed by the root exact graph.


## 72. G-4bu — change of coefficient-field section and intrinsic associated graded

The decomposition in G-4bs is written using a chosen coefficient-field lift t of the residue parameter and the logarithmic basis (dlog t,dlog p). The completed Kato quotient and the scalar quaternion boundary map are intrinsic, but the displayed direct-sum splitting need not be. We now compute the transition law under a change of lift.

Let t' be another lift of the same residue element t. Since t'/t ≡ 1 mod p, there is a unique v in E[[p]] such that
\[
t'=t(1+pv),\qquad E=\mathbb F_2(t).
\]
Write the coefficientwise derivations on E[[p]] as ∂_t and ∂_p, so that
\[
dv=(t\partial_t v)d\log t+(p\partial_p v)d\log p.
\]
Differentiating t'=t(1+pv) gives the exact transition formula
\[
\boxed{
d\log t'=
\left(1+\frac{pt\partial_t v}{1+pv}\right)d\log t
+
\frac{p(v+p\partial_p v)}{1+pv}d\log p,
\qquad d\log p'=d\log p.
}
\]
All denominators are units. The transition matrix is the identity modulo p.

The coefficient functions transform compatibly: for f in E, f(t') ≡ f(t) mod p. Consequently, for every integer n, the induced map on the ambient logarithmic differential lattice satisfies
\[
p^n\Omega^1_{E[[p]]}/p^{n+1}\Omega^1_{E[[p]]}
\xrightarrow{\ \sim\ }
p^n\Omega^1_{E[[p]]}/p^{n+1}\Omega^1_{E[[p]]}
\]
as the identity after the common residue-field identification. In particular, a Laurent differential's leading p-order coefficient pair is independent of the chosen coefficient-field lift. The transition is filtered and triangular: its correction terms raise p-order by at least one, hence lower pole order by at least one for negative powers.

The square coefficient field changes only at second order:
\[
(t')^2=t^2(1+p^2v^2).
\]
Thus if Σ=t² and Σ'=(t')², then Σ'−Σ is divisible by p². This is compatible with the earlier base/coefficient distinction S₀=Σ+p: the first adjacent-pole correction in the quaternion symbol is stable under a change of section at its leading graded order, while higher corrections can alter lower-pole representatives.

**Intrinsic conclusion.** The divisor parameter p, the logarithmic differential filtration, the Cartier operator, the exact-differential subspace, and the original quaternion symbol map are independent of the coefficient-field section. The leading graded differential data are canonically identified under every change t↦t'. By contrast, the explicit direct-sum coordinates F_c⊕F_c⊕E^perf/E in G-4bs are a section-dependent splitting; the transition formula shows why they should not yet be called canonical summands.

**Important limitation.** Identity on the associated graded of the ambient differential module does not, by itself, prove strictness of the induced filtration after quotienting by exact forms and (C⁻¹−1)-relations. Nor does it prove that the section-dependent orbit splittings are related by a uniquely determined triangular automorphism of the final quotient. Those are the remaining functoriality questions. The scalar projection is better behaved: it is characterized on the intrinsic quaternion differential symbols and the section-independent scalar normal form G-4aj, so its target quotient does not depend on the auxiliary lift.

**Next task.** Prove strictness for the combined relation subspace B¹+(C⁻¹−1)Ω¹ with respect to the p-adic filtration, or find the first filtration degree where strictness fails. If strictness holds, the associated-graded quotient is intrinsic and the coordinate splittings are filtered choices of section; if it fails, the failure identifies an additional extension term that the present direct-sum model misses.


## 73. G-4bv — strictness of the Cartier/exact relation filtration

We can now close the strictness problem posed in G-4bu. Put
\[
M=\Omega^1_L=L\,d\log t\oplus L\,d\log p,
\qquad L=E((p)),\quad E=\mathbb F_2(t),\quad F=E^2.
\]
Let \(B^1=dL\), and let \(\Phi\) be the chosen logarithmic representative of inverse Cartier,
\[
\Phi\big(p^n(A,B)\big)=p^{2n}(A^2,B^2).
\]
The relation space defining the Kato quotient is
\[
R=B^1+(\Phi-1)M.
\]
For \(c=a+bt\in E\), with a,b∈F, one has
\[
d(cp^n)=p^n\big(tb,\,(n\bmod 2)c\big)
\]
in the logarithmic basis. Hence the exact subspace at exponent n is
\[
D_n=
\begin{cases}
G=\{(tb,a+bt):a,b\in F\},&n\text{ odd},\\
T=\{(tb,0):b\in F\},&n\text{ even}.
\end{cases}
\]

We compute the initial relation subspace at each exponent, using the least p-exponent as the leading term.

- If n>0, the leading term of (Φ−1)(p^n(A,B)) is p^n(A,B). Since (A,B) is arbitrary, the positive associated-graded relation space is all E⊕E. Independently, the whole positive tail is in (Φ−1)M by the convergent geometric series from G-4bs.
- If n=0, the exponent is fixed by Φ. The relation space is exactly \(T+(\wp(E)\oplus\wp(E))\), where \(\wp(x)=x^2+x\).
- If n<0 is odd, no inverse-Cartier image can have leading exponent n, because doubling a negative integer gives an even integer. Thus the initial relation space is exactly G.
- If n<0 is even, write n=2r with r<0. The leading term of (Φ−1)(p^r(A,B)) is p^n(A²,B²), so its coefficient space is F⊕F. Exact forms at exponent n contribute T. These spaces intersect trivially: E=F⊕tF, hence \((F\oplus F)\cap T=0\).

There is no hidden cancellation in the negative range. At a fixed negative even exponent n, the only inverse-Cartier input capable of producing its leading term is the coefficient at n/2; Frobenius is injective, and its leading coefficient space F⊕F has zero intersection with the exact tangent space T. At a negative odd exponent there is no incoming doubled exponent at all. Therefore the initial relation space is precisely
\[
\operatorname{in}_n(R)=
\begin{cases}
G,&n<0\text{ odd},\\
(F\oplus F)\oplus T,&n<0\text{ even},\\
T+(\wp(E)\oplus\wp(E)),&n=0,\\
E\oplus E,&n>0.
\end{cases}
\]
Every listed vector is realized by an exact differential or a single Cartier relation, so these are equalities, not just inclusions.

**Conclusion.** The relation space \(B^1+(\Phi-1)M\) is strict for the p-adic exponent filtration. The associated-graded quotient is consequently intrinsic under coefficient-section changes, because G-4bu showed that those changes are filtered and identity on the ambient associated graded.

This does **not** make the full direct-sum splitting in G-4bs canonical. It proves that its associated-graded layers are canonical; choosing representatives and splitting the successive extensions still depends on the coefficient-field lift. The nontrivial extension data are exactly where the Frobenius orbit/direct-limit model lives.

The next step is to compute the extension maps between the canonical graded layers and show that the coordinate-dependent orbit decomposition is a filtered splitting of this intrinsic object.


## 74. G-4bw — first-order extension maps under a change of coefficient section

We now compute the first nontrivial off-diagonal action of a section change on the intrinsic associated-graded quotient from G-4bv. Let
\[
t'=t(1+pv_0)+O(p^2),\qquad v_0=e+ft,\quad e,f\in F.
\]
Expanding the exact transition formula of G-4bu to first order gives
\[
d\log t'=(1+ptf)d\log t+pv_0d\log p+O(p^2).
\]
If a logarithmic form has coefficient pair (A,B), its coefficients in the new basis, expressed in the new residue parameter, are
\[
A'=A+p\,t(v_0\partial_t A+fA)+O(p^2),
\]
\[
B'=B+p\,(t v_0\partial_t B+v_0A)+O(p^2).
\]
Thus the correction from exponent n to exponent n+1 is
\[
\delta_{v_0}(A,B)=
\big(t(v_0A'+fA),\;t v_0B'+v_0A\big),
\]
where primes in this display mean \(\partial_t\).

For negative odd n, the graded quotient is
\[
Q_n=(E\oplus E)/G\simeq F^2,
\qquad
A=a+bt, B=c+dt\longmapsto(x,y)=(a,b+d).
\]
For negative even n, it is
\[
Q_n=(E\oplus E)/((F\oplus F)+T)\simeq F,
\qquad
A=a+bt, B=c+dt\longmapsto d.
\]
Substitution into the correction formula gives the adjacent-layer maps:

- From negative odd n≤−3 to negative even n+1:
\[
\boxed{\delta_{v_0}:F^2\to F,\qquad (x,y)\mapsto fx+ey.}
\]
- From negative even n≤−2 to negative odd n+1:
\[
\boxed{\delta_{v_0}:F\to F^2,\qquad d\mapsto(0,ed).}
\]

These maps are independent of the exponent within each parity class. They are additive in v₀, as expected from composition of section changes modulo p². They are the first-order extension data that the associated-graded calculation alone cannot see.

**Scope.** This computes the adjacent graded action modulo p². It does not yet compute the higher-order transition terms or prove that the resulting filtered extension is classified by these first-order maps alone. The exponent-zero layer must also be treated separately.


## 75. G-4bx — second-order section-change maps and the zero mode

Let a change of coefficient-field section be
\[
s=t'=t(1+pv_0+p^2v_1)+O(p^3),
\qquad
v_0=e+ft,\quad v_1=e_1+f_1t,
\]
with e,f,e₁,f₁∈F and t²=S in the residue coefficient field. We compute the induced transition through order p².

The inverse coordinate substitution is
\[
t=s+p\alpha+p^2\beta+O(p^3),
\quad
\alpha=sv_0,
\quad
\beta=sv_0^2+s^2fv_0+sv_1.
\]
The logarithmic basis transition, expressed in s, is
\[
d\log t=(1+psf+p^2((sf)^2+sv_1'))d\log s
+(pv_0+p^2v_0^2)d\log p+O(p^3),
\]
where v₁'=∂ₛv₁=f₁. Therefore, for a form pⁿ(A,B) in the old logarithmic coordinates, its new coefficient pair has expansion
\[
A_{m new}=p^n(A+pA_1+p^2A_2)+O(p^{n+3}),
\quad
B_{m new}=p^n(B+pB_1+p^2B_2)+O(p^{n+3}),
\]
where all coefficient functions below are evaluated at s and
\[
A_1=\alpha\partial_s A+sfA,
\qquad
B_1=\alpha\partial_s B+v_0A,
\]
\[
A_2=\beta\partial_s A+\alpha^2\partial_s^{[2]}A
+\alpha sf\partial_s A+((sf)^2+sf_1)A,
\]
\[
B_2=\beta\partial_s B+\alpha^2\partial_s^{[2]}B
+\alpha(v_0\partial_s A+fA)+v_0^2A.
\]
Here ∂ₛ^[2] is the second Hasse derivative, required for the Taylor expansion in characteristic two.

For an odd negative exponent, choose the representative (A,B)=(x,sy) of its class (x,y)∈F². The quotient map is
\[
(A,B)\longmapsto(A_0,A_1+B_1),
\]
where subscripts denote the F and sF coefficients. Substitution into the second-order terms gives
\[
\boxed{
(x,y)\longmapsto
\left(Sf^2x,\ (f_1+ef)x+(e^2+e_1)y\right).
}
\]
For an even negative exponent, choose representative (A,B)=(0,sd), d∈F. Its second-order contribution is B₂=βd, whose sF coefficient is (e²+e₁)d. Thus
\[
\boxed{d\longmapsto(e^2+e_1)d.}
\]
These are the p² diagonals, mapping a graded layer to the layer two exponents higher, hence preserving parity. The p¹ diagonals are the opposite-parity maps of G-4bw.

At exponent zero, the induced associated-graded map is the identity. Indeed, the coordinate substitution is congruent to t modulo p, and the logarithmic basis transition is the identity modulo p; all corrections have strictly positive p-order. Thus the zero-mode quotient
\[
(E\oplus E)/(T+(\wp(E)\oplus\wp(E)))
\]
is unchanged on its leading graded layer.

**Scope and next check.** The displayed maps are the second-order diagonals for a single section change, not a classification of the full filtered automorphism. We must still verify the composition law for two successive changes, including the cross terms contributed by the first-order maps, and determine whether the resulting higher diagonals are forced by the first-order data or carry new independent parameters.


## 76. G-4by — corrected second-order maps and composition law

**Corrigendum to G-4bx.** The p² calculation must transport the coefficient field F as well as the parameter t. Since
\[
s^2=t^2(1+pv_0+p^2v_1)^2
=t^2+p^2t^2v_0^2+O(p^3),
\]
an old coefficient c(S), S=t², is expressed in the new coefficient field as
\[
c(S_{old})=c(S_{new})+p^2S v_0^2\partial_Sc+O(p^3).
\]
This adds the derivation
\[
D_{v_0}=S v_0^2\partial_S
=S(e^2+Sf^2)\partial_S
\]
to both F-coordinates. Also, the correct second-order B-coordinate formula has no extra \(\alpha fA\) term: because the basis transition is expressed in the new coordinate, its off-diagonal coefficient is \(pv_0+p^2v_0^2\).

Thus the corrected p² diagonals are
\[
\boxed{
N_{odd}(x,y)=
\big(Sf^2x+D_{v_0}x,\;
f_1x+(e^2+e_1)y+D_{v_0}y\big),
}
\]
and
\[
\boxed{
N_{even}(d)=(e^2+e_1)d+D_{v_0}d.
}
\]
These replace the formulas in G-4bx. The zero-mode graded layer remains fixed.

We can now verify composition. Apply first the section change v and then u, with
\[
v_0=e_v+f_vt,\quad u_0=e_u+f_ut.
\]
The composite parameter is
\[
w_0=v_0+u_0,
\quad
w_1=v_1+u_1+t v_0\partial_tu_0+v_0u_0.
\]
Since \(\partial_tu_0=f_u\), the cross term simplifies in characteristic two to
\[
t v_0f_u+v_0u_0=e_uv_0.
\]
Consequently
\[
e_{w_1}=e_{v_1}+e_{u_1}+e_ue_v,
\quad
f_{w_1}=f_{v_1}+f_{u_1}+e_uf_v,
\quad
D_{w_0}=D_{v_0}+D_{u_0}.
\]

Let \(L_v:Q_{odd}\to Q_{even}\) and \(M_v:Q_{even}\to Q_{odd}\) be the first-order maps from G-4bw:
\[
L_v(x,y)=f_vx+e_vy,
\qquad M_v(d)=(0,e_vd).
\]
The corrected second-order maps satisfy exactly
\[
N_{odd}(w)=N_{odd}(v)+N_{odd}(u)+M_uL_v,
\]
\[
N_{even}(w)=N_{even}(v)+N_{even}(u)+L_uM_v.
\]
For the odd layer, the cross term is \(M_uL_v(x,y)=(0,e_u(f_vx+e_vy))\); for the even layer it is \(L_uM_v(d)=e_ue_vd\). These are precisely the cross terms dictated by composition of filtered triangular maps. The derivation terms add because \((v_0+u_0)^2=v_0^2+u_0^2\).

**Conclusion.** The first- and second-order section-change maps satisfy the composition law through order p², once the induced motion of the coefficient field is included. The second-order maps are therefore not arbitrary corrections: their nonlinear cross terms are forced by the group law of coefficient-section changes. This is a genuine functoriality check, but it does not yet prove that the full filtered extension is determined by its first two diagonals; orders p³ and above remain.


## 77. G-4bz — independent cubic section data

We isolate the genuinely new cubic parameter by taking
\[
s=t'=t(1+p^3v_2),\qquad v_2=e_2+f_2t,\quad e_2,f_2\in F.
\]
Since
\[
s^2=t^2(1+p^6v_2^2),
\]
the coefficient field is unchanged through order p³. The inverse substitution is
\[
t=s+p^3s v_2+O(p^6).
\]
Differentiating in logarithmic coordinates gives
\[
d\log t=(1+p^3sf_2)d\log s+p^3v_2d\log p+O(p^6).
\]
For a coefficient pair (A,B), the transported pair is therefore
\[
(A,B)+p^3\big(s(v_2\partial_sA+f_2A),\;
s v_2\partial_sB+v_2A\big)+O(p^6).
\]

For a negative odd layer, use the representative (A,B)=(x,sy), x,y∈F. Since ∂ₛx=0 and ∂ₛ(sy)=y, the cubic correction is
\[
( sf_2x,\;s v_2y+v_2x).
\]
Projecting to the next even graded quotient, which reads the s-coefficient of the second coordinate, gives
\[
\boxed{L_{v_2}(x,y)=f_2x+e_2y.}
\]
For a negative even layer, use (A,B)=(0,sd), d∈F. The correction is (0,sv_2d), whose next odd quotient class is
\[
\boxed{M_{v_2}(d)=(0,e_2d).}
\]

These are exactly the first-order transition formulas of G-4bw, now appearing three filtration steps higher. But their parameters e₂,f₂ are independent of e,f,e₁,f₁: one may take v₀=v₁=0 and choose v₂ arbitrarily. Hence the cubic action is not determined by the first- and second-order data. It contains a genuinely new graded section parameter.

We can also record the cubic coefficient in the composition law. Let
\[
t_1=t(1+pv_0+p^2v_1+p^3v_2),\quad
t_2=t_1(1+pu_0(t_1)+p^2u_1(t_1)+p^3u_2(t_1)),
\]
where each uᵢ=eᵤᵢ+fᵤᵢt and each vᵢ=eᵥᵢ+fᵥᵢt. Expanding the product and evaluating the uᵢ at t₁ gives
\[
w_0=v_0+u_0,
\]
\[
w_1=v_1+u_1+t f_{u_0}v_0+v_0u_0,
\]
\[
\boxed{
w_2=v_2+u_2+t f_{u_0}v_1+t f_{u_1}v_0
+v_0u_1+t f_{u_0}v_0^2+v_1u_0.
}
\]
Thus the composite cubic coefficient consists of the freely chosen cubic coefficients v₂+u₂ plus cross terms forced by lower orders. This is the expected filtered composition law: lower-order data determine the nonlinear correction, but do not determine the new cubic parameter.

**Conclusion.** The section-change action has independent graded parameters at cubic order. The first two diagonals do not determine the full filtered extension. The cubic leading maps and the cubic composition parameter are established; a complete formula for the p³ action when v₀ and v₁ are simultaneously nonzero, including all quotient projections, remains a separate calculation.


## 78. G-4ca — arbitrary-depth isolated section changes and clockwise filtration

We now compute the first nonzero graded effect of an isolated section parameter at arbitrary depth. Fix r≥1 and put
\[
s=t'=t(1+p^r v_r),\qquad v_r=e_r+f_rt,\quad e_r,f_r\in F.
\]
All formulas in this section are modulo terms of p-order at least 2r. Since
\[
s^2=t^2(1+p^{2r}v_r^2),
\]
the coefficient field does not move before order 2r. The inverse coordinate substitution and logarithmic basis change are
\[
t=s+p^rsv_r+O(p^{2r}),
\]
\[
d\log t=(1+p^rsf_r)d\log s
+(r\bmod2)p^rv_r d\log p+O(p^{2r}).
\]
Consequently a coefficient pair transforms by
\[
(A,B)\longmapsto(A,B)+p^r
\left(
s(v_r\partial_sA+f_rA),\;
sv_r\partial_sB+(r\bmod2)v_rA
\right)+O(p^{2r}).
\]

For an odd negative layer, take (A,B)=(x,sy), x,y∈F. The correction is
\[
\left(sf_rx,\;sv_ry+(r\bmod2)v_rx\right).
\]
The even-layer quotient reads the s-coefficient of the second coordinate. As s²=S∈F, that coefficient is
\[
\boxed{L_r(x,y)=
\begin{cases}
f_rx+e_ry,&r\text{ odd},\\
e_ry,&r\text{ even}.
\end{cases}}
\]
For an even negative layer, take (A,B)=(0,sd). The correction is (0,sv_rd), whose odd-layer quotient is
\[
\boxed{M_r(d)=(0,e_rd)}
\]
for either parity of r.

This recovers G-4bw at r=1 and the isolated v₂ contribution to G-4by at r=2. At r=3 it recovers G-4bz. The parity distinction has a geometric source: dlog(p^r) contributes r·dlog p, which survives precisely for odd r in characteristic two. Thus f_r contributes to the odd-to-even arrow only at odd depths; e_r contributes at every depth.

**Clockwise convention.** Regard the negative graded layers as an oriented sequence, with the odd and even quotient types alternating. Declare clockwise to mean forward in filtration depth: a term at exponent n that contributes at exponent n+r has moved r places clockwise. Since n<0, this is motion toward exponent zero and toward less singular principal parts. This is a convention for visualizing the filtration, not an extra algebraic structure or a claim that the exponent lattice is literally periodic. In this convention every isolated section parameter produces a forward arrow; odd r crosses to the opposite parity type, while even r returns to the same parity type.

**Scope.** These are the first nonzero graded arrows of an isolated parameter v_r. They do not give the complete p^{2r} and higher corrections, where the coefficient field moves, nor do they classify simultaneous parameters v₀,…,vᵣ. In particular, the even-depth parameter f_r is invisible in this first graded arrow and may reappear in its higher-order corrections.


## 79. G-4cb — second clockwise movement for an isolated depth-r change

Set q=pʳ and make the isolated change s=t(1+qv), v=e+ft. The first graded arrow is G-4ca. To compute the next diagonal, one must include the motion of the coefficient coordinate:
\[
s²=S(1+q²v²),\qquad
S_{old}=S_{new}+q²S_{new}(e²+S_{new}f²)+O(q⁴).
\]
Thus for a coefficient function g(S), the second-diagonal coefficient-field contribution is
\[
D_vg=S(e²+Sf²)\partial_Sg.
\]
This is not optional: freezing S would omit a genuine term.

Rescaling the corrected second-order coordinate calculation (G-4by) from p to q gives the isolated quadratic diagonal. There is no independent order-q² section parameter in this isolated family, so the independent e₁,f₁ terms of G-4by are set to zero. On the odd and even representatives used above, the second diagonal is
\[
\boxed{N^{(r)}_{odd}(x,y)=
\big(Sf²x+D_vx,\;e²y+D_vy\big),}
\]
\[
\boxed{N^{(r)}_{even}(d)=e²d+D_vd.}
\]
These terms occur at p^{2r}. The formulas are independent of the parity of r: parity affects the first diagonal through dlog(q)=r dlog(p), whereas dlog(q²)=0 in characteristic two. In particular, f is invisible in the first arrow when r is even, but it reappears through Sf² and through D_v on the second diagonal.

This gives a two-diagonal picture:
- at distance r clockwise, the differential-frame arrow is parity-sensitive;
- at distance 2r clockwise, the coefficient-field displacement and quadratic frame correction are parity-insensitive.

**Qualification.** These are the isolated-parameter diagonals. They do not include cross terms from simultaneous parameters at intermediate depths, and they do not assert that the displayed operators alone determine the full p-adic section-change action. A full composition law at arbitrary depth remains to be proved.


## 80. G-4cc — leading composition interaction at two distinct depths

Take two isolated changes, in the stated order,
\[
t_1=t(1+p^rv),\qquad t_2=t_1(1+p^su),
\]
with v=e_v+f_vt and u=e_u+f_ut. For the leading mixed order p^{r+s}, coefficient functions in F may be held fixed: the coefficient coordinate S=t² moves under the first change only at p^{2r}, so its effect on the second factor begins at p^{2r+s}. But the linear t-dependence of u must be evaluated at t₁:
\[
u(t_1)=u(t)+f_up^rtv+O(p^{2r+s}	ext{ coefficient-field terms}).
\]
Multiplying gives
\[
\frac{t_2}{t}
=1+p^rv+p^su+p^{r+s}(f_utv+vu)+O(\text{higher mixed order}).
\]
Since u=e_u+f_ut and the characteristic is two,
\[
f_utv+vu=v(f_ut+u)=e_uv.
\]
Hence the leading mixed composition coefficient is
\[
\boxed{w_{r+s}^{\rm mixed}=e_uv.}
\]
In coordinates, this is (e_ue_v)+(e_uf_v)t. It is a generated depth-(r+s) parameter, even though neither input had a parameter at that depth.

Reversing the order gives e_vu. Thus the leading order-sensitive difference (equivalently, the characteristic-two sum of the two mixed coefficients) is
\[
e_uv+e_vu=t(e_uf_v+e_vf_u).
\]
It vanishes precisely when e_uf_v=e_vf_u. This is a leading commutator calculation for the coordinate substitutions; it does not yet assert a global group commutator formula after all higher coefficient-field corrections are included.

**Resonance warning.** If r+s equals an existing diagonal such as 2r or 2s, this generated mixed coefficient must be added to the intrinsic quadratic diagonal at that same p-order. The isolated second-diagonal operators G-4cb alone do not include this interaction. The calculation is cleanest as a two-depth associated-graded composition statement.

**Geometric reading.** Clockwise arrows do not merely superpose. Two forward motions at depths r and s can generate a new forward motion at depth r+s. The first nontrivial interaction is controlled only by the constant coefficient e_u of the second change and the full coefficient v of the first.


## 81. G-4cd — the section-change bracket is a two-dimensional Lie algebra

Let E=F(t), t²=S, F=F₂(S), and regard ∂ₜ as the F-derivation of E with ∂ₜ(t)=1. For v=e_v+f_vt define
\[
X_v=t v\partial_t.
\]
A direct commutator calculation gives
\[
[X_v,X_u](t)
=X_v(tu)+X_u(tv)
=t²(vf_u+uf_v),
\]
where subtraction is addition in characteristic two. Since
\[
vf_u+uf_v=e_vf_u+e_uf_v\in F,
\]
we obtain
\[
\boxed{[X_v,X_u]=X_{[v,u]_*},\qquad
[v,u]_*:=t(e_vf_u+e_uf_v).}
\]
This is exactly the order-sensitive coefficient found in G-4cc. The bracket is F-bilinear, alternating ([v,v]₊=0), and satisfies Jacobi because it is the commutator bracket of derivations.

In the F-basis H=1 and X=t of the parameter space E, the bracket is
\[
[H,H]_*=[X,X]_* =0,\qquad [H,X]_* =X.
\]
Thus the infinitesimal section-change algebra is the two-dimensional nonabelian affine Lie algebra over F (in characteristic two). Its derived algebra is F·X and its center is zero.

Attach filtration depth by declaring X_v^{(r)} to have degree r. The leading mixed commutator has degree r+s and parameter [v,u]_*; hence the depth-graded infinitesimal algebra is the positive-depth current form of this two-dimensional Lie algebra, with bracket
\[
[v z^r,u z^s]=[v,u]_*z^{r+s}.
\]
This is a statement about the associated graded infinitesimal coordinate-change algebra. It does not by itself identify the full nonlinear section-change group with the exponential of this Lie algebra: in characteristic two, exponential/logarithm arguments are not generally available, and higher divided-power terms must be handled directly.

**Geometric consequence.** The first noncommutativity is not arbitrary: it is rank one, always lands in the tF direction, and is generated by the interaction between the constant and t-coefficients. The clockwise depth grading is compatible with the bracket because depths add.


## 82. G-4ce — restricted square and logarithmic-form representation

Continue with E=F(t), t²=S, F=F₂(S), and X_v=tv∂ₜ for v=e+ft. The square of a derivation is again a derivation in characteristic two. Here it can be computed explicitly:
\[
X_v(t)=et+fS,\qquad
X_v²(t)=e(et+fS)=e²t+efS.
\]
Therefore
\[
\boxed{X_v^{[2]}=X_v²=X_{ev},\qquad (e+ft)^{[2]}=e(e+ft).}
\]
In particular H^{[2]}=H and X^{[2]}=0 for H=X_1 and X=X_t. Together with [H,X]=X, this equips the two-dimensional affine Lie algebra from G-4cd with its concrete restricted 2-map. The identity ad_{D²}=(ad_D)² holds because these are actual derivations.

Now extend X_v to E((p)) by fixing p and acting coefficientwise. On the logarithmic differential module with ω=dlog t and η=dlog p, the Lie derivative satisfies
\[
\mathcal L_{X_v}(g\omega+h\eta)
=X_v(g)\omega+g f t\omega+X_v(h)\eta,
\]
because X_v(t)/t=v and d(v)=fdt=ft\omega, while X_v(p)=0. Thus on the coefficient pair (g,h)∈E((p))²,
\[
\boxed{\rho_v(g,h)=(X_v(g)+ftg,\;X_v(h)).}
\]
This is a genuine representation of the restricted Lie algebra on the ambient logarithmic differential module: it is the standard Lie-derivative action, so [ρ_v,ρ_u]=ρ_[v,u] and ρ_v²=ρ_{ev}. On pairs with g,h∈F((p)), X_v fixes the coefficients and the action reduces to (ftg,0), but the image generally lies in E((p))², not F((p))².

**Crucial quotient caveat.** This establishes a representation on the ambient differential module, not yet on the Kato-style quotient by exact forms and Artin–Schreier/Frobenius relations. Lie derivative preserves exact forms because L_D(dg)=d(Dg). But for an Artin–Schreier relation m²+m, one has X_v(m²+m)=X_v(m), since X_v(m²)=0; this is not automatically another Artin–Schreier relation. Thus stability of the full denominator is unproved and may fail. The quotient representation test must explicitly compute this obstruction before any induced action is claimed.


**G-4ce correction (denominator stability test).** The quotient denominator uses the differential Frobenius operator Φ on logarithmic forms, not the scalar Artin–Schreier map m↦m²+m. Accordingly, the scalar observation X_v(m²+m)=X_v(m) is not itself a proof about quotient stability and should not be used for that purpose. The correct test is whether
\[
\mathcal L_{X_v}(\Phi(m)-m)
\]
belongs to B¹+(Φ−1)M for every m∈M. In general Lie derivative and Φ do not commute. For m=pⁿω with ω=dlogt,
\[
\mathcal L_{X_v}(\Phi(m)-m)
=(p^{2n}+p^n)ft\,ω,
\]
whereas
\[
\Phi(\mathcal L_{X_v}m)=p^{2n}S f²\,ω.
\]
This exhibits the noncommutation but does not by itself prove that the denominator is not stable, since exact forms may absorb the discrepancy. The quotient-action question remains open pending reduction modulo B¹+(Φ−1)M.


## 83. G-4cf — explicit failure of quotient stability

We now settle the quotient-action test left open in G-4ce. Retain
\[
M=L\,\omega\oplus L\,\eta,\quad L=E((p)),\quad
R=B^1+(\Phi-1)M,
\]
where \(\omega=d\log t\), \(\eta=d\log p\),
\(B^1=dL\), and
\[
\Phi(p^j(A,B))=p^{2j}(A^2,B^2).
\]
Let \(X_v=tv\partial_t\), with \(v=e+ft\), and let
\[
\rho_v(A,B)=(X_v(A)+ftA,\ X_v(B)).
\]

Choose the simplest nonzero t-direction, \(v=t\), so \(e=0,f=1\) and
\(X_t=t^2\partial_t=S\partial_t\). Take any negative odd integer
\(n\), and set \(m=p^n\omega\). Then
\[
r=(\Phi-1)m=p^{2n}\omega+p^n\omega\in R.
\]
Since \(\rho_t(\omega)=t\omega\) and \(X_t(p)=0\),
\[
\rho_t(r)=p^{2n}t\omega+p^nt\omega.
\]
The first summand is exact:
\[
p^{2n}t\omega=p^{2n}dt=d(p^{2n}t),
\]
because \(2n=0\) in the coefficient of \(d\log p\). Therefore
\[
[\rho_t(r)]_M=[p^nt\omega] \quad\text{mod }B^1.
\]

At the negative odd exponent \(n\), the initial relation space of R is
exactly
\[
G=\{(tb,a+bt):a,b\in F\},\qquad E=F\oplus tF.
\]
The coefficient pair of \(t\omega\) is \((t,0)\), and it is not in G:
the first coordinate forces \(b=1\), while the second would force
\(a=t\notin F\). Thus its class in the odd graded quotient is nonzero.
By the strictness result G-4bv, this nonzero initial class cannot be
cancelled by higher-exponent terms of a putative relation in R.
Consequently
\[
\boxed{\rho_t(R)\not\subseteq R.}
\]
More generally the same witness works for every \(v=e+ft\) with
\(f\ne0\): after removing the exact \(p^{2n}ft\omega\) term, the
surviving odd-layer class is \((0,f)\in Q_n\simeq F^2\).

**Conclusion.** The restricted Lie-algebra representation on the ambient
logarithmic module does not descend to the Kato-style quotient. The
failure is already visible in the first t-direction and at every negative
odd layer. This does not contradict functoriality of Cartier under actual
morphisms: an infinitesimal derivation need not preserve the Frobenius
relation subspace. Any quotient-level symmetry must be restricted to the
stabilizer of R, or formulated using a different, genuinely functorial
action; neither replacement is asserted here.

**Correction to the earlier G-4ce caveat.** The scalar
Artin–Schreier observation involving \(m^2+m\) is irrelevant to this
denominator. The failure above is proved directly for
\(R=B^1+(\Phi-1)M\), using its strict negative associated-graded
relations.


## 84. G-4cg — the quotient has zero infinitesimal stabilizer

G-4cf used \(m=p^n\omega\) to detect every parameter with \(f\ne0\).
The complementary test detects the constant parameter. Let \(e\ne0\),
take \(v=e+ft\), choose negative odd n, and set \(m=p^nt\omega\).
Then
\[
(\Phi-1)m=p^{2n}S\omega+p^nt\omega.
\]
Using \(X_v(t)=et+fS\), \(X_v(S)=0\), and the connection term
\(ft\cdot t=fS\), we get
\[
\rho_v(t\omega)=et\omega,\qquad
\rho_v(S\omega)=Sft\omega.
\]
Therefore
\[
\rho_v((\Phi-1)m)
=p^{2n}Sft\omega+p^net\omega.
\]
The first term is exact:
\[
p^{2n}Sft\omega=d(p^{2n}Sft),
\]
since \(dS=df=0\) in \(E=F_2(t)\) and \(2n=0\) in characteristic two.
The remaining term \(e p^nt\omega\) has nonzero class in the negative
odd graded quotient, because \((t,0)\notin G\).

Combining this with G-4cf:
- if \(f\ne0\), the test \(m=p^n\omega\) leaves the nonzero class
  \((0,f)\in Q_n\simeq F^2\);
- if \(e\ne0\), the test \(m=p^nt\omega\) leaves the nonzero class
  \((0,e)\in Q_n\simeq F^2\).

Thus every nonzero \(v=e+ft\in E\) fails to preserve R. We have proved
\[
\boxed{\{v\in E:\rho_v(R)\subseteq R\}=0.}
\]
Equivalently, the two-dimensional restricted section-change Lie algebra
has zero infinitesimal stabilizer on this Kato-style quotient under the
ambient Lie-derivative action.

**Scope.** This rules out a nonzero infinitesimal action induced by these
Lie derivatives. It does not rule out actions of discrete coordinate
automorphisms, nor does it classify a different quotient-level symmetry
constructed independently of this ambient action.


## 85. G-4ch — finite section changes do preserve the Cartier quotient

G-4cg says that the ambient Lie derivative has zero stabilizer on
\(M/R\). This does **not** imply that finite coefficient-section
automorphisms fail to act. In fact, they do act, for a different reason:
naturality of inverse Cartier is a statement modulo exact forms.

Let \(L=E((p))\), \(E=\mathbb F_2(t)\), and fix \(r\ge1\) and
\(v=e+ft\in E\). Define the continuous substitution
\[
\sigma_{r,v}(p)=p,\qquad
\sigma_{r,v}(t)=t(1+p^rv).
\]
It is a well-defined continuous \(\mathbb F_2((p))\)-automorphism of L.
Indeed, writing \(S=t^2\), with \(e,f\in\mathbb F_2(S)\), the formal
derivative of the new t-coordinate with respect to t is
\[
\frac{\partial}{\partial t}\bigl(t(1+p^r(e+ft))\bigr)
=1+p^re,
\]
a p-adic unit. The substitution is the identity on the residue field,
so the formal inverse-function argument gives an automorphism.

Let \(\sigma=\sigma_{r,v}\) and let \(\sigma^*\) denote pullback on
differentials. It preserves exact forms:
\[
\sigma^*(B^1)=B^1,\qquad B^1=dL,
\]
because \(\sigma^*(dg)=d(\sigma(g))\).

The chosen operator
\[
\Phi(p^n(A,B))=p^{2n}(A^2,B^2)
\]
is a logarithmic representative of inverse Cartier. The essential
point is that inverse Cartier is natural under field/scheme
isomorphisms: on cohomology modulo exact forms,
\[
[\sigma^*\Phi(m)]=[\Phi(\sigma^*m)]
\quad\text{in }Z^1/B^1.
\]
This is the standard functoriality of the Cartier isomorphism; the
representative maps need not commute strictly, only modulo \(B^1\).
Consequently
\[
\sigma^*((\Phi-1)m)
=\bigl(\Phi(\sigma^*m)-\sigma^*m\bigr)+b_m,
\qquad b_m\in B^1.
\]
It follows that
\[
\sigma^*(R)\subseteq R,\qquad
R=B^1+(\Phi-1)M.
\]
Applying the same argument to \(\sigma^{-1}\) gives equality. Hence
\[
\boxed{\sigma_{r,v}^*(R)=R,}
\]
and every finite section change induces an automorphism of \(M/R\).

This resolves the apparent conflict with G-4cf–G-4cg. Those results
differentiate the finite action by the ambient Lie derivative and
then ask that this derivative preserve R. But inverse Cartier
naturality is only an equality modulo exact forms, and it is tied to
the Frobenius twist of the automorphism. It does not imply that the
naive tangent operator \(\rho_v\) preserves the chosen representative
subspace \(R\). In particular, the finite automorphism action on
\(M/R\) need not be differentiable as an action of the ordinary
two-dimensional section-change Lie algebra on this quotient.

**Scope and next calculation.** The existence of the finite quotient
action is proved. Its explicit filtered matrices, their composition
law on the quotient, and the relation (if any) between different
depths remain to be computed. The associated-graded arrows G-4ca are
the first-order-in-\(p^r\) data, not yet a complete formula for the
induced quotient automorphism.

