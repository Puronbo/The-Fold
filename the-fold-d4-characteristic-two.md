# UF-032 — Characteristic-two D4 module and bracket

## Scope

This note reduces the integral D4 action and the integral two-step alternating Lie bracket from UF-031/UF-030 modulo 2. It classifies the resulting seven-dimensional D4-module and computes its center and derived algebra.

**Scope warning.** This is the characteristic-two reduction of the specified integral Lie algebra and D4 action. It is not, without a separate group-scheme calculation, a theorem identifying this Lie algebra with the full tangent Lie algebra of the automorphism group scheme of the original algebra in characteristic two.

## Theorem 1 — The D4 action factors through C2

Write the coordinates as \((a,b,c,d,e,u,v)\). The integral generators are
\[
t(a,b,c,d,e,u,v)=(b,-a,-e,-d,-c,v,-u),
\]
\[
s(a,b,c,d,e,u,v)=(a,-b,c,-d,e,-u,v).
\]
Over \(k=\mathbb F_2\), these become
\[
t(a,b,c,d,e,u,v)=(b,a,e,d,c,v,u),\qquad s=I.
\]
In particular, \(t^2=I\) and the D4 action factors through the quotient
\[
D_4\twoheadrightarrow C_2=\langle t\rangle.
\]

**Proof.** Reduce every matrix entry modulo two. Every minus sign equals plus, and the displayed formulas give the result. \(\square\)

## Theorem 2 — Indecomposable module decomposition

Let \(J_1\) denote the one-dimensional trivial \(k[C_2]\)-module and let
\[
J_2=k[C_2]\cong k[\epsilon]/(\epsilon^2),\qquad \epsilon=t-1,
\]
be its two-dimensional indecomposable regular module. Then
\[
\boxed{\mathfrak u_{\mathbb F_2}\cong 3J_2\oplus J_1.}
\]
More explicitly, the three invariant swap planes are
\[
\langle a,b\rangle,\quad\langle c,e\rangle,\quad\langle u,v\rangle,
\]
and the fixed line is \(\langle d\rangle\). The quotient by the center is
\[
\mathfrak u/Z\cong 2J_2\oplus J_1.
\]

**Proof.** On each listed plane, \(t\) interchanges the two basis vectors, so its matrix is \(\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}=I+N\), where \(N^2=0\) and \(N\ne0\). This is the indecomposable length-two module \(J_2\). The vector \(d\) is fixed. Since \(k[C_2]\cong k[\epsilon]/(\epsilon^2)\), its indecomposable finite-dimensional modules are the Jordan blocks of sizes one and two. The decomposition is therefore indecomposable and complete. The center plane is the \((u,v)\) swap plane. \(\square\)

## Theorem 3 — The reduced bracket and its center

In characteristic two the only nonzero brackets between the five noncentral coordinate vectors are
\[
\boxed{[a,d]=u,\quad [b,e]=u,\quad
[a,c]=v,\quad [b,d]=v.}
\]
The bracket is alternating, its image is the full two-dimensional space
\[
[\mathfrak u,\mathfrak u]=\langle u,v\rangle,
\]
and its radical on the five-dimensional quotient is zero. Consequently
\[
\boxed{Z(\mathfrak u_{\mathbb F_2})=[\mathfrak u_{\mathbb F_2},\mathfrak u_{\mathbb F_2}]
=\langle u,v\rangle,\quad \dim Z=2.}
\]

**Proof.** Reduce the UF-028 structure constants modulo two: terms with coefficient 2 vanish and minus signs become plus. The four displayed brackets remain. They show surjectivity onto \(\langle u,v\rangle\). If \(z=\alpha a+\beta b+\gamma c+\delta d+\eta e\) brackets to zero with every vector, then testing against \(d\) gives \(\alpha u+\beta v=0\), hence \(\alpha=\beta=0\). Testing against \(a\) then gives \(\delta u+\gamma v=0\), hence \(\delta=\gamma=0\). Finally, testing against \(b\) gives \(\eta u+\delta v=0\), hence \(\eta=0\). Equivalently, the radical matrix has rank five over \(\mathbb F_2\). Thus no noncentral direction joins the center. All brackets land in \(\langle u,v\rangle\), which is central by construction. \(\square\)

The center does **not** grow in characteristic two for this integral bracket model. This contrasts with characteristic three, where the radical gains the extra cubic trivial-character line.

## Theorem 4 — D4-equivariance survives reduction

The reduced action preserves the bracket:
\[
t[x,y]=[tx,ty],\qquad s[x,y]=[sx,sy].
\]
Since \(s=I\), only equivariance under the swap \(t\) is nontrivial. The four surviving brackets form two swap-compatible pairs:
\[
[a,d]=u\longleftrightarrow[b,d]=v,
\qquad
[b,e]=u\longleftrightarrow[a,c]=v.
\]
Thus the characteristic-two bracket is a well-defined D4-equivariant alternating map
\[
\Lambda^2(2J_2\oplus J_1)\longrightarrow J_2.
\]

## Prime-by-prime picture

For the specified integral alternating Lie algebra:
- characteristic zero and odd primes other than 3: center and derived algebra have dimension two;
- characteristic 3: center has dimension three, with one extra trivial-character direction;
- characteristic 2: the D4 module is \(3J_2\oplus J_1\), and the center and derived algebra both have dimension two.

The characteristic-two representation is nonsemisimple, but its bracket does not acquire a larger radical. This separates the modular failure of Maschke semisimplicity from degeneration of the Lie bracket.

## Reproducibility

Run `python3 tools/fold_d4_characteristic_two.py`. The verifier checks the integral group relations, reduction of the action, the indecomposable block ranks, the bracket table, equivariance, and the five-dimensional radical rank over \(\mathbb F_2\).

## Open problem UF-032-A

Compute the full automorphism group scheme of the original vertex algebra over \(\mathbb Z\), especially its tangent space and smoothness at characteristic two. The seven-dimensional integral Lie algebra studied here is a specified bracket lattice; it must not be silently identified with the full characteristic-two derivation algebra before that scheme-theoretic calculation is done.
