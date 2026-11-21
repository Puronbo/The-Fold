# Comparative fppf torsor groups of all known Fold Hopf structures

Let k be a field of characteristic two and A=k[x,z]/(x^4,z^2). The following table collects the fppf \(H^1\)-groups of the seven currently constructed commutative Hopf structures on this algebra.

## 1. Torsor-group table

| Hopf group scheme | Exact description of \(H^1_{\mathrm{fppf}}(k,-)\) |
|---|---|
| \(\alpha_4\times\alpha_2\) | \((k/k^4)\oplus(k/k^2)\) |
| \(\mu_4\times\alpha_2\) | \(k^\times/(k^\times)^4\oplus k/k^2\) |
| \(\alpha_4\times\mu_2\) | \(k/k^4\oplus k^\times/(k^\times)^2\) |
| \(\mu_4\times\mu_2\) | \(k^\times/(k^\times)^4\oplus k^\times/(k^\times)^2\) |
| \(G_C\) | abstractly \((k/k^2)\oplus(k/k^4)\), noncanonically |
| \(G_D\) | abstractly \((k/k^4)\oplus(k/k^2)\), noncanonically |
| \(G_\lambda\) | an extension of \(\ker([a]\mapsto[Q(a,\lambda)])\subseteq k/k^4\) by \(k^\times/(k^\times)^2\), split noncanonically |

Here
\[
Q(a,\lambda)=k\langle U,D\rangle/
(U^2=a,\ D^2=\lambda,\ DU+UD=1)
\]
is the characteristic-two quaternion algebra from the mixed-family boundary calculation.

## 2. Proof of the product rows

The fppf Kummer sequence gives
\[
H^1(k,\mu_{2^n})=k^\times/(k^\times)^{2^n},
\]
and the Frobenius sequence gives
\[
H^1(k,\alpha_{2^n})=k/k^{2^n}.
\]
Products of commutative group schemes give products on \(H^1\), proving the first four rows.

## 3. Proof of the non-product rows

For \(G_C\) and \(G_D\), the exact sequences and noncanonical splittings are proved in the separate non-product torsor note.

For \(G_\lambda\), the exact sequence is
\[
0\longrightarrow k^\times/(k^\times)^2
\longrightarrow H^1(k,G_\lambda)
\longrightarrow
\ker\!\left(k/k^4\xrightarrow{[a]\mapsto[Q(a,\lambda)]}
\operatorname{Br}(k)[2]\right)
\longrightarrow0.
\]
The group \(G_\lambda\) is killed by two, so this is a short exact sequence of \(\mathbb F_2\)-vector spaces and splits noncanonically.

## 4. Interpretation

The two non-product groups \(G_C,G_D\) have abstractly the same \(H^1\)-group as \(\alpha_4\times\alpha_2\). Thus their torsor groups alone do not distinguish their group-scheme structures.

The mixed family \(G_\lambda\) is different: its torsors are cut out by a quaternion splitting condition. If \(\lambda\in k^2\), the extension splits and the \(G_\lambda\)-row reduces to the product row for \(\alpha_4\times\mu_2\). If \(\lambda\notin k^2\), the boundary can be nonzero, and the allowed fourth-power classes are precisely those for which \(Q(a,\lambda)\) is split.

These are classifications of torsors under each fixed Hopf group scheme, not a classification of all Hopf structures or all algebra forms of A.
