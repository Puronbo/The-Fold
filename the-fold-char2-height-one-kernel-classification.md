# Classification of the height-one Frobenius kernels

Let k be algebraically closed of characteristic two. Every Hopf structure on
\[
A=k[x,z]/(x^4,z^2)
\]
has relative Frobenius kernel with coordinate algebra
\[
A/(x^2,z^2)=k[x,z]/(x^2,z^2),
\]
of rank four. This note classifies all possible commutative height-one group schemes on that algebra.

## Theorem 1. Exactly four height-one kernel types

There are exactly four isomorphism classes of commutative height-one group schemes of rank four with this coordinate algebra. They are classified by the restricted 2-map on their two-dimensional abelian restricted Lie algebra:

| Restricted 2-map | Group scheme | Realized by a Fold Hopf law |
|---|---|---|
| zero | \(\alpha_2\times\alpha_2\) | primitive product; also the kernel of \(G_C\) |
| rank one, nilpotent | \(H_D\) (the local-local type \(I_{1,1}\)) | kernel of \(G_D\) |
| rank one, nonnilpotent | \(\alpha_2\times\mu_2\) | product structures |
| invertible | \(\mu_2\times\mu_2\) | product structure |

Thus every possible height-one Frobenius kernel type is already realized by one of the known Fold Hopf structures. Any further Hopf law must differ at the level of extension data or the Frobenius image, not by introducing a fifth height-one kernel type.

## Proof

For a height-one finite commutative group scheme, the restricted Lie algebra controls the group scheme. Since the group scheme is commutative, its Lie algebra \(V\) is abelian, and its restricted 2-map
\[
P:V\longrightarrow V
\]
is additive and 2-semilinear:
\[
P(cv)=c^2P(v).
\]
Choose a basis. Then \(P(v)=M v^{(2)}\) for a \(2\times2\) matrix M. A basis change acts by twisted conjugacy
\[
M\longmapsto S^{-1}M S^{(2)}.
\]

The rank of M is invariant.

- **Rank zero.** Then \(P=0\), giving \(\alpha_2^2\).
- **Rank two.** Then P is a semilinear bijection. By Lang's theorem for the Frobenius endomorphism of \(GL_2\), it has a basis of fixed vectors, so its matrix is the identity. This gives \(\mu_2^2\).
- **Rank one.** Since k is perfect, \(\ker P\) and \(\operatorname{im}P\) are lines. If they coincide, then \(P^2=0\); choose \(e_1\) spanning the common line and \(e_2\) with \(P(e_2)=e_1\), obtaining the nilpotent Jordan type. This is \(H_D=I_{1,1}\). If they are distinct, choose \(e_1\) spanning the image and \(e_2\) spanning the kernel; rescale \(e_1\) to obtain \(P(e_1)=e_1\), \(P(e_2)=0\), giving \(\alpha_2\times\mu_2\).

These four cases exhaust ranks zero, one, and two, and the two rank-one cases are distinguished by whether image equals kernel. Hence there are exactly four types.

## Fold realization audit

The product Hopf structures realize the three split types. The non-product group \(G_C\) has the same height-one kernel as \(\alpha_2\times\alpha_2\), while \(G_D\) realizes the fourth, nilpotent-Jordan type. The imperfect mixed family \(G_\lambda\) has height-one kernel \(\alpha_2\times\mu_2\).

This is a classification of possible height-one kernels over an algebraically closed field. It is not a classification of the full rank-eight Hopf structures: distinct central extensions can share the same kernel and Frobenius image, as the Fold examples already demonstrate.


## 3. Kernel/image incidence matrix for the rank-eight problem

The Frobenius image is independently constrained to be \(\alpha_2\) or \(\mu_2\). Combining that with Theorem 1 gives eight a priori kernel/image pairs:

| Height-one kernel \(K=G[F]\) | Image \(\alpha_2\) | Image \(\mu_2\) |
|---|---|---|
| \(\alpha_2\times\alpha_2\) | realized: \(\alpha_4\times\alpha_2\), \(G_C\) | open |
| \(I_{1,1}\) | realized: \(G_D\) | open |
| \(\alpha_2\times\mu_2\) | realized: \(\alpha_4\times\mu_2\), \(G_\lambda\) | realized: \(\mu_4\times\alpha_2\) |
| \(\mu_2\times\mu_2\) | open | realized: \(\mu_4\times\mu_2\) |

Here “open” means not yet realized or ruled out under the fixed total coordinate algebra \(k[x,z]/(x^4,z^2)\). It is not an assertion that such an extension exists.

The next classification step is therefore finite at the level of kernel/image *types*: determine which of the three open pairs admit extension data whose total coordinate algebra is the Fold algebra, then classify the corresponding extensions up to group-scheme isomorphism. The family \(G_\lambda\) shows that even a fixed realized pair can carry nontrivial arithmetic extension parameters.
