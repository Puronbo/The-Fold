# Explicit torsor models for the non-product Hopf structures

Let k be a field of characteristic two.

## 1. The cocycle group \(G_C\)

Its group law on points is
\[
(x,z)+(r,s)=(x+r,\ z+s+x^2r^2),
\qquad r^4=s^2=0.
\]
It is the central extension \(0\to\alpha_2\to G_C\to\alpha_4\to0\).

For \(a,b\in k\), define
\[
P^C_{a,b}=\operatorname{Spec}k[u,v]/(u^4-a,\ v^2-b).
\]
Give it the right \(G_C\)-action
\[
(u,v)\cdot(r,s)=(u+r,\ v+s+u^2r^2).
\]
This is an action: composing \((r,s)\) and \((r',s')\) adds the correction \(r^2r'^2\), exactly as required by the group law of \(G_C\).

It is a torsor. Given two points \((u,v)\), \((u',v')\), the unique group element carrying the first to the second is
\[
r=u'+u,\qquad s=v'+v+u^2r^2.
\]
The relations \(r^4=s^2=0\) follow from \(u'^4=u^4=a\), \(v'^2=v^2=b\), and \(u^4r^4=0\). These formulas give the inverse to the canonical action map.

### Equivalence of parameters

For \(p,q\in k\), the coordinate change
\[
u'=u+q,\qquad v'=v+q^2u^2+p
\]
is \(G_C\)-equivariant and changes the parameters by
\[
\boxed{(a,b)\longmapsto(a+q^4,\ b+q^4a+p^2).}
\]
Conversely, an equivariant isomorphism must induce an isomorphism of the quotient \(\alpha_4\)-torsors, hence \(u'=u+q\). Compatibility with the kernel translations forces \(v'=v+F(u)\), and compatibility with the \(G_C\)-action gives
\(F(u+r)+F(u)=q^2r^2\). The solutions are \(F(u)=q^2u^2+p\), since the invariant functions for the translation action on an \(\alpha_4\)-torsor are constants. Thus the displayed relation is complete.

Every \(G_C\)-torsor is represented by some \(P^C_{a,b}\): the quotient torsor is \(u^4=a\), it has the explicit lift \(P^C_{a,0}\), and the fiber over it is a principal homogeneous space under \(H^1(k,\alpha_2)=k/k^2\). Adding the kernel torsor \(v^2=b\) gives \(P^C_{a,b}\).

### Addition of torsor classes

The contracted product of \(P^C_{a,b}\) and \(P^C_{a',b'}\) is represented by
\[
\boxed{(a,b)+(a',b')=(a+a',\ b+b'+aa').}
\]
Indeed, on the product take
\[
U=u+u',\qquad V=v+v'+u^2u'^2.
\]
These are invariant under the diagonal action, satisfy \(U^4=a+a'\) and \(V^2=b+b'+aa'\), and define the resulting torsor. The parameter equivalence above makes this law independent of representatives. Doubling gives \((0,a^2)\), which is equivalent to \((0,0)\) by a square shift, as required because \(G_C\) is killed by two.

## 2. The nilpotent-cocycle group \(G_D\)

Its group law is
\[
(x,z)+(r,s)=(x+r+zs,\ z+s),
\qquad r^4=s^2=0.
\]
It is the central extension \(0\to\alpha_4\to G_D\to\alpha_2\to0\).

For \(a,b\in k\), define
\[
P^D_{a,b}=\operatorname{Spec}k[u,v]/(u^2-a,\ v^4-b).
\]
The right action is
\[
(u,v)\cdot(r,s)=(u+s,\ v+r+us).
\]
The action law follows from the cross term \(ss'\) in the x-coordinate of the group law.

It is a torsor. Given \((u,v)\) and \((u',v')\), the unique element carrying the first to the second is
\[
s=u'+u,\qquad r=v'+v+us.
\]
Here \(s^2=0\) and \(r^4=0\), so this again gives the inverse canonical map.

### Equivalence of parameters

For \(p,q\in k\), the equivariant coordinate change
\[
u'=u+q,\qquad v'=v+qu+p
\]
changes parameters by
\[
\boxed{(a,b)\longmapsto(a+q^2,\ b+q^4a^2+p^4).}
\]
Conversely, an equivariant isomorphism induces \(u'=u+q\); compatibility with the kernel \(\alpha_4\)-translations forces \(v'=v+F(u)\), and compatibility with the action gives \(F(u+s)+F(u)=qs\). The solutions are \(F(u)=qu+p\), because the invariants of the \(\alpha_2\)-translation action on its torsor are constants. Thus this parameter relation is complete.

Every \(G_D\)-torsor is represented: each quotient \(\alpha_2\)-torsor \(u^2=a\) has the explicit lift \(P^D_{a,0}\), and the fiber is a principal homogeneous space under \(H^1(k,\alpha_4)=k/k^4\). Adding the kernel torsor \(v^4=b\) gives \(P^D_{a,b}\).

### Addition of torsor classes

The contracted-product law is
\[
\boxed{(a,b)+(a',b')=(a+a',\ b+b'+a^2a'^2).}
\]
Use
\[
U=u+u',\qquad V=v+v'+uu'.
\]
These descend under the diagonal action and satisfy \(U^2=a+a'\), \(V^4=b+b'+a^2a'^2\). Doubling gives \((0,a^4)\), equivalent to zero by a fourth-power shift.

## 3. Relation to the abstract cohomology sequences

These explicit parameter models refine the short exact sequences
\[
0\to k/k^2\to H^1(k,G_C)\to k/k^4\to0,
\]
\[
0\to k/k^4\to H^1(k,G_D)\to k/k^2\to0.
\]
They show why the splittings are generally not canonical: changing a representative of the quotient torsor changes the kernel parameter by \(q^4a\) for \(G_C\), or \(q^4a^2\) for \(G_D\).

The parameter addition laws are twisted, even though each resulting group is abstractly an \(\mathbb F_2\)-vector space and hence admits a noncanonical linear splitting. The twist records the nontrivial group law of the original Hopf structure.
