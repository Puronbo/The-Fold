# Fppf torsors under the nilpotent-p-map Hopf group G_D

Let G_D be the sixth Hopf structure on A=k[x,z]/(x⁴,z²), with
\[
\Delta(x)=x\otimes1+1\otimes x+z\otimes z,\qquad
\Delta(z)=z\otimes1+1\otimes z.
\]
Projection to z and inclusion of the x-axis give an exact sequence
\[
0\longrightarrow\alpha_4\longrightarrow G_D
\longrightarrow\alpha_2\longrightarrow0.
\]
The group law is \((x,z)+(x',z')=(x+x'+zz',z+z')\), and G_D is killed by two.

## 1. Cohomology sequence

Over a field k of characteristic two,
\[
H^1(k,\alpha_4)=k/k^4,\qquad H^1(k,\alpha_2)=k/k^2,
\]
and \(H^2_{\mathrm{fppf}}(k,\alpha_4)=0\), by the Frobenius exact sequence and affine vanishing for \(\mathbb G_a\). Since \(\alpha_2(k)=0\), the long exact sequence gives
\[
0\longrightarrow k/k^4
\longrightarrow H^1_{\mathrm{fppf}}(k,G_D)
\longrightarrow k/k^2
\longrightarrow0.
\]
Because G_D is commutative and killed by two, this is a short exact sequence of \(\mathbb F_2\)-vector spaces and splits noncanonically. Abstractly,
\[
H^1_{\mathrm{fppf}}(k,G_D)\cong(k/k^4)\oplus(k/k^2),
\]
with no canonical splitting asserted.

## 2. Explicit torsors

For a,b in k, set
\[
B_{a,b}=k[u,v]/(u^4-a,\ v^2-b).
\]
Define the right coaction
\[
\rho(u)=u\otimes1+1\otimes x+v\otimes z,\qquad
\rho(v)=v\otimes1+1\otimes z.
\]
The relations are preserved:
\[
\rho(u)^4=a,\qquad \rho(v)^2=b,
\]
because x⁴=z²=0 and z⁴=0.

The canonical map \(B_{a,b}\otimes B_{a,b}\to B_{a,b}\otimes k[G_D]\) is an isomorphism. In the two copies of B, write u₁,v₁,u₂,v₂. The canonical map sends
\[
u_1\mapsto u,\quad v_1\mapsto v,\quad
u_2\mapsto u+x+vz,\quad v_2\mapsto v+z.
\]
Its inverse is
\[
z\mapsto v_1+v_2,\qquad
x\mapsto u_1+u_2+v_1(v_1+v_2),
\]
with u↦u₁ and v↦v₁. These formulas respect x⁴=0 and z²=0, and the two substitutions are inverse. Thus every B_{a,b} is a finite faithfully flat G_D-torsor of rank eight.

For fixed b, varying a moves through the kernel \(H^1(k,\alpha_4)=k/k^4\). After choosing representatives for k/k², this family gives a set-theoretic parameterization of all G_D-torsor classes; the abstract group splitting is noncanonical.

## 3. Perfect and imperfect fields

Over a perfect field both k/k² and k/k⁴ vanish, so every G_D-torsor is trivial. Over an imperfect field such as k=F₂(t), the class of t is neither a square nor a fourth power, and nontrivial torsors occur.

This classifies fppf torsors under the fixed group scheme G_D. It does not classify all Hopf structures or all forms of G_D.
