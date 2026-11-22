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
are not merely independent (G-4af): they form an F₂-basis of C_r for every odd r. Therefore the full local scalar quotient has the explicit basis
\[
\boxed{
\left\{S^n p^{-r}: n\ge0,\ r\ge1\text{ odd}\right\}.
}
\]
This proves the quotient is countably infinite-dimensional and supplies a complete normal form: reduce independently along each odd-core chain, then collect the resulting zeroth-coordinate coefficients.

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
