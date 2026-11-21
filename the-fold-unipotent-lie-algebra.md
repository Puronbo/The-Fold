# UF-028 — Lie algebra, center, and commutator subgroup of the nonlinear automorphism group

## Setup

Let k be a characteristic-zero field and C=k[x,y]/(y²+x²,x⁴), with socle s=x³y. Let U=Aut₁(C), the identity-linear subgroup from UF-026. Parameterize Φθ by θ=(a,b,c,d,e,u,v):
\[
\begin{aligned}
\Phi_\theta(x)&=x+ax²+bxy+cx³+dx²y+us,\\
\Phi_\theta(y)&=y-bx²+axy-dx³+ex²y+vs.
\end{aligned}
\]

## Theorem 1 — Lie algebra

The Lie algebra u=Lie(U) consists of derivations D determined by
\[
\begin{aligned}
D(x)&=ax²+bxy+cx³+dx²y+us,\\
D(y)&=-bx²+axy-dx³+ex²y+vs.
\end{aligned}
\]
For D₁,D₂ with parameters (a₁,b₁,c₁,d₁,e₁,u₁,v₁) and (a₂,b₂,c₂,d₂,e₂,u₂,v₂), the bracket is
\[
[D₁,D₂](x)=\omega_u s,\qquad [D₁,D₂](y)=\omega_v s,
\]
where
\[
\begin{aligned}
\omega_u={}&a₁d₂-a₂d₁+2b₁c₂-b₁e₂-2b₂c₁+b₂e₁,\\
\omega_v={}&-a₁c₂+2a₁e₂+a₂c₁-2a₂e₁-b₁d₂+b₂d₁.
\end{aligned}
\]

**Proof.** A derivation is determined by P=D(x), Q=D(y), subject to xP+yQ=0 and x³P=0, obtained by differentiating the two defining relations. The second condition is automatic for P∈m² because m⁵=0. Expanding the first in the basis x³,x²y,s gives the displayed constraints on the coefficients. Applying D₁D₂−D₂D₁ to x and y and reducing with y²=−x² and x⁴=0 gives the bracket formula. ∎

## Theorem 2 — Exact center and derived algebra

\[
\boxed{Z(\mathfrak u)=[\mathfrak u,\mathfrak u]
=\langle U,V\rangle\cong k²,}
\]
where U(x)=s,U(y)=0 and V(x)=0,V(y)=s. Thus u is a seven-dimensional, two-step nilpotent Lie algebra.

**Proof.** Every bracket has only socle components, and socle-valued derivations commute with all derivations because applying a derivation to s has degree at least five and hence vanishes. Conversely, the bracket form is surjective onto the two socle directions: choose D₁ with a₁=1 and D₂ with d₂=1 to obtain U; choose D₁ with a₁=1 and D₂ with c₂=1 to obtain −V. If a derivation commutes with every other derivation, pairing successively with test derivations supported in a,d,b,c,e forces a=b=c=d=e=0. Only u,v remain. ∎

## Theorem 3 — Group-level commutator and center

Use the composition convention Φθ⋆ΦΘ=Φθ∘ΦΘ from UF-027. The group commutator
\[
[\Phi_\theta,\Phi_\Theta]
=\Phi_\theta\Phi_\Theta\Phi_\theta^{-1}\Phi_\Theta^{-1}
\]
has its first five coordinates equal to zero. Its final two coordinates are
\[
\begin{aligned}
K_u={}&-A²b-2ABa+2Aab-Ad+B²b+Ba²-Bb²-2Bc+Be+2Cb+Da-Eb,\\
K_v={}&-A²a+2ABb+Aa²-Ab²+Ac-2Ae+B²a-2Bab+Bd-Ca-Db+2Ea.
\end{aligned}
\]
Therefore every group commutator lies in the central socle-translation subgroup
\[
Z_U=\{(0,0,0,0,0,u,v):u,v\in k\}.
\]
This subgroup is exactly the center and exactly the derived subgroup:
\[
\boxed{Z(U)=[U,U]=Z_U\cong (k²,+).}
\]
In particular U is a two-step nilpotent group (nilpotency class exactly two).

**Proof.** Substitute the triangular inverse coordinates from the UF-027 group law into the fourfold product. The first five coordinates cancel and the displayed socle terms remain. To see that the center has no further elements, set Θ successively to have only one nonzero coordinate among A,B,C,D,E; vanishing of K_u,K_v for every such Θ forces a=b=c=d=e=0. Conversely, elements with only u,v coordinates commute with every element. Finally, every socle translation is a commutator: take θ=(1,0,0,0,0,0,0) and Θ=(0,0,C,D,0,0,0); the commutator has coordinates (0,0,0,0,0,D,−C). ∎

## Consequences

1. The seven-dimensional kernel is a central extension of a five-dimensional abelian group by a two-dimensional center.
2. Its derived subgroup and center coincide; its lower central series is U ⊃ Z_U ⊃ {1}.
3. The commutator pairing on the five-dimensional quotient U/Z_U is alternating and takes values in k². Its infinitesimal form is the pair (ω_u,ω_v) above.
4. Since the graded linear group G_gr acts on U by conjugation, it acts on this two-dimensional center. The socle itself transforms by its induced character; the precise D16 representation on the full Lie algebra is the next natural calculation.

## Scope and reproducibility

The results are for characteristic zero. The script `tools/fold_unipotent_commutators.py` verifies the derivation constraints, Lie bracket, triangular inverse, and exact group commutator formula by symbolic reduction. These computations supplement the proofs; they are not a full CI or Lean build.

## Open problem UF-028-A

Determine the representation of G_gr (including its D16 subgroup) on u and on Z(u). Decompose u/Z(u) and Z(u) into irreducibles, and determine whether the commutator pairing is equivariant for this action.
