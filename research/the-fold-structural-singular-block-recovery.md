# G-EP32 — Structural recovery of one singular Kronecker block

G-EP31 used exhaustive enumeration of (GL_m(\mathbb F_p)\times GL_n(\mathbb F_p)). G-EP32 replaces that search in the one-block case with a basis construction from a certified polynomial minimal vector.

For (P(t)=Q+tK), let
[
x(t)=x_0+x_1t+\cdots+x_et^e
]
be the unique right minimal-basis generator of a single right singular block. Its coefficient equations are
[
Qx_0=0,\quad Qx_j=-Kx_{j-1}\ (1\le j\le e),\quad Kx_e=0.
]
Define (z_j=(-1)^{e-j}x_{e-j}). Then
[
Qz_j=Kz_{j+1},\quad Kz_0=0,\quad Qz_e=0.
]
For a genuine single block, the columns of (T=[z_0\ \cdots\ z_e]) form a domain basis, and the columns of (B=[Kz_1\ \cdots\ Kz_e]) form a codomain basis. Taking (S=B^{-1}) gives
[
SQT=[I_e\ 0],\qquad SKT=[0\ I_e].
]

The implementation first invokes the G-EP27 polynomial-nullspace certificate, requiring exactly one right minimal index (e), no left minimal indices, and complete bounded-degree span certification through degree (e). It then checks both basis determinants, constructs (S,T), and passes them to the G-EP30 strict-equivalence verifier.

This removes GL-group enumeration and scales with exact polynomial-kernel and matrix operations, but the surrounding G-EP27/G-EP24 machinery still has a combinatorial minor budget. The algorithm is restricted to a *single pure* right or left singular block; mixed pencils, multiple singular blocks, and regular components are refused rather than misclassified. It constructs no general Kronecker decomposition.
