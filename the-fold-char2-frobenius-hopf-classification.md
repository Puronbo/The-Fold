# Frobenius reduction of the Hopf-structure classification (G-3f)

Let k be algebraically closed of characteristic two and let
\[
A=k[x,z]/(x^4,z^2)
\]
carry any commutative Hopf algebra structure with this fixed underlying algebra.

## 1. Two structure-independent Frobenius facts

The square subalgebra of A is
\[
A^2=k[x^2]/(x^4),
\]
of dimension two. This is independent of the coproduct: in characteristic two, every square is a polynomial in x², and x² itself is a square.

The relative Frobenius of a commutative group scheme is a group homomorphism. Its image therefore has coordinate algebra A², while its kernel has coordinate algebra
\[
A/(x^2,z^2)\cong k[x,z]/(x^2,z^2),
\]
of dimension four. Also the second relative Frobenius is zero because x⁴=z⁴=0. Thus every possible group scheme is connected, has height at most two, and fits into its Frobenius kernel/image sequence with a rank-four height-one kernel and rank-two image.

Over an algebraically closed field, the connected commutative group schemes of rank two are alpha_2 and mu_2. Therefore the Frobenius image of any Hopf structure on A is one of these two group schemes.

## 2. The five known examples in Frobenius terms

\[
\begin{array}{c|c|c}
G & G[F] & F(G)\\
\hline
\alpha_4\times\alpha_2 & \alpha_2\times\alpha_2 & \alpha_2\\
\mu_4\times\alpha_2 & \mu_2\times\alpha_2 & \mu_2\\
\alpha_4\times\mu_2 & \alpha_2\times\mu_2 & \alpha_2\\
\mu_4\times\mu_2 & \mu_2\times\mu_2 & \mu_2\\
G_C & \alpha_2\times\alpha_2 & \alpha_2
\end{array}
\]
Here G_C is the non-product cocycle group from G-3c. Its cross term x² tensor x² vanishes after restricting to the Frobenius kernel, so its kernel is alpha_2 x alpha_2; its Frobenius image is alpha_2.

The five structures show that the Frobenius kernel and image do not determine the extension: alpha_4 x alpha_2 and G_C have the same Frobenius kernel and image but are non-isomorphic.

## 3. A reduced classification problem

Any further Hopf structure must arise from extension data with:
- a rank-four height-one kernel whose coordinate algebra is k[x,z]/(x²,z²);
- a rank-two Frobenius image, either alpha_2 or mu_2;
- compatibility with the fixed total algebra k[x,z]/(x⁴,z²) and its Frobenius map.

The rank-four kernel is controlled by its two-dimensional abelian restricted Lie algebra. Its restricted 2-power map is a necessary invariant. The known product examples realize zero, rank-one, and rank-two semisimple behaviours. Whether other height-one kernels or extension classes lift to the fixed rank-eight algebra is open.

## 4. Open classification tasks

1. Classify the height-one Hopf structures on k[x,z]/(x²,z²) that can occur as G[F].
2. For each possible kernel and quotient alpha_2 or mu_2, classify extensions whose total coordinate algebra is k[x,z]/(x⁴,z²).
3. Determine which extension classes are isomorphic after allowing all algebra automorphisms of A, not merely changes of section.
4. Establish whether the resulting list is exhaustive over algebraically closed fields, then study descent to imperfect fields.


## 5. A sixth structure realizes the nilpotent height-one kernel

The G-3g group G_D has
```
Delta(x) = x tensor 1 + 1 tensor x + z tensor z
Delta(z) = z tensor 1 + 1 tensor z
```
Its Frobenius kernel has coordinate algebra k[x,z]/(x²,z²) with this induced coproduct. Its invariant derivations satisfy D_z^[2]=D_x and D_x^[2]=0, so its two-dimensional restricted Lie algebra has a nonzero nilpotent Jordan 2-map. The Frobenius image is alpha_2.

Thus the height-one kernel in the reduction need not be a product alpha_2 x alpha_2, alpha_2 x mu_2, or mu_2 x mu_2. The nilpotent-Jordan type is realized by an actual lift to the fixed rank-eight algebra.
