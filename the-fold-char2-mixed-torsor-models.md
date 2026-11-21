# Explicit fppf torsors under the imperfect mixed Hopf family

Let k have characteristic two and
\[
G_\lambda:\quad
(x,t)(r,\tau)=
\bigl(x+r,\ t\tau(1+\lambda x^2r^2)\bigr),
\qquad x^4=r^4=0,\quad t^2=\tau^2=1.
\]
This is the central extension \(0\to\mu_2\to G_\lambda\to\alpha_4\to0\).

## Theorem 1. Explicit lift of an \(\alpha_4\)-torsor

Fix \(a\in k\). Suppose there are \(c,d\in k\) such that
\[
c^2+a d^2+d=\lambda.
\]
For any \(q\in k^\times\), put
\[
P^\lambda_{a,q;c,d}
=\operatorname{Spec}k[u,v]/(u^4-a,\ v^2-q).
\]
Define a right action of \(G_\lambda\) by
\[
\boxed{
(u,v)\cdot(r,\tau)
=\left(u+r,\ v\tau\bigl(1+(c+d u^2)r^2\bigr)\right).
}
\]
Then \(P^\lambda_{a,q;c,d}\) is a \(G_\lambda\)-torsor.

### Proof

Set \(f(u)=c+d u^2\). The defining equation gives
\[
f(u)^2+d=c^2+d^2u^4+d=c^2+a d^2+d=\lambda.
\]
For two group elements \((r,\tau)\), \((s,\sigma)\), composing the displayed action gives the multiplicative factor
\[
\tau\sigma\left(
1+f(u)(r^2+s^2)+(f(u)^2+d)r^2s^2
\right).
\]
Since \(f(u)^2+d=\lambda\), this is
\[
\tau\sigma\left(1+f(u)(r+s)^2+\lambda r^2s^2\right),
\]
which is exactly the action of their product
\((r+s,\tau\sigma(1+\lambda r^2s^2))\). Thus it is an action.

The relation \(v^2=q\) is preserved because
\[
\left(1+f(u)r^2\right)^2=1
\]
as \(r^4=0\), and \(\tau^2=1\).

Given two points \((u,v),(u',v')\), the unique group element carrying the first to the second is
\[
r=u'+u,\qquad
\tau=\frac{v'}{v}\left(1+f(u)r^2\right).
\]
Here \(r^4=0\), and \(\tau^2=1\). These formulas give the inverse of the canonical action map, proving the torsor assertion.

## Theorem 2. Completeness of the model

The quotient \(\alpha_4\)-torsor associated with a \(G_\lambda\)-torsor is represented by \(u^4=a\), with \(a\) determined modulo \(k^4\). The boundary calculation proves that this quotient torsor lifts if and only if there exist \(c,d\in k\) with
\[
c^2+a d^2+d=\lambda.
\]
The action in Theorem 1 constructs such a lift explicitly.

For a fixed quotient torsor and a fixed choice of \(c,d\), all lifts form a principal homogeneous space under
\[
H^1(k,\mu_2)=k^\times/(k^\times)^2.
\]
Changing \(q\) by a square gives an isomorphic torsor via rescaling \(v\). Thus \(q\) supplies exactly the remaining kernel-torsor parameter. Different choices of \(c,d\), or a different representative of \(a\bmod k^4\), change the identification of this fiber; there is no canonical product decomposition in general.

Consequently the model realizes every class in the exact sequence
\[
0\to k^\times/(k^\times)^2
\to H^1(k,G_\lambda)
\to
\ker\!\left(k/k^4\xrightarrow{[a]\mapsto[Q(a,\lambda)]}
\operatorname{Br}(k)[2]\right)
\to0.
\]

## 3. Relation to the quaternion algebra

The condition \(c^2+a d^2+d=\lambda\) is precisely the splitting criterion for
\[
Q(a,\lambda)=
k\langle U,D\rangle/
(U^2=a,\ D^2=\lambda,\ DU+UD=1).
\]
Thus the explicit torsor action exists exactly when the associated quaternion algebra splits. This makes the Brauer obstruction visible directly in the affine equations of the torsor, rather than only as an abstract connecting homomorphism.
