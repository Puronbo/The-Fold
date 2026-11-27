# Origin to Fold

## Purpose

This note rebuilds the argument from its starting objects. It does not take the later complexity-theory applications, numerical analogies, or physical interpretations as premises.

The derivation has two related but distinct constructions:

1. **Scale ledger:** an affine scaling about a chosen datum. Its zero parameter collapses all points to the datum.
2. **Fold ledger:** an involution that pairs points and fixes a crease. A reflection is the geometric model.

They are related, but they are not the same operation. In particular, a collapse is generally not invertible, while an involution is invertible.

## 0. The starting point: a datum and a distinguishable state

Let (V) be a real or complex vector space, let (P_0\in V) be a chosen datum, and let (P\in V) be a state. The displacement from the datum is

[
v=P-P_0.
]

The datum is not assumed to be absolute nothingness. It is a selected reference relative to which displacement is defined.

## 1. The scale family

For a scalar (k), define

[
g_k(P)=P_0+k(P-P_0)=P_0+kv.
]

Three parameter values establish the basic cases:

[
g_1(P)=P,\qquad
g_0(P)=P_0,qquad
g_{-1}(P)=2P_0-P.
]

- (k=1): identity; the state is unchanged.
- (k=0): collapse to the datum; every input has the same output.
- (k=-1): central reflection through the datum; the displacement changes sign.

For real (k), the map scales the displacement, with a sign reversal when (k<0). For complex (k\) acting on a complex vector space, its modulus scales and its argument rotates. This statement depends on the chosen complex structure; it is not a claim that every physical system has a complex-valued scale.

The composition law is

[
g_k\circ g_\ell=g_{k\ell}.
]

**Proof.** Applying (g_\ell) gives (P_0+\ell(P-P_0)). Applying (g_k) about the same datum gives
(P_0+k\ell(P-P_0)=g_{k\ell}(P)). (square)

The determinant statement requires a finite-dimensional vector space of dimension (n): the linear part is (kI), so its determinant is (k^n).

## 2. What collapse does and does not preserve

The map (g_0) is constant. If two distinct states (P,Q) are supplied, then

[
g_0(P)=P_0=g_0(Q).
]

Therefore (g_0) is not injective (unless the state space has only one point), and no inverse map can recover an arbitrary input from the collapsed output alone.

A retained reference can preserve a selected origin or datum. Introduce the augmented state

[
S=(x,r),\qquad F_k(x,r)=(kx,r).
]

Here (r) is explicitly retained while (x) is scaled. At (k=0), the output is ((0,r)). The recovery map

[
U(x,r)=(r,r)
]

returns the retained reference as the first coordinate. It does **not** reconstruct an arbitrary pre-collapse (x); it reconstructs the designated reference (r). If the initial normalized state is (x=r=1), this convention represents a chosen beginning (1), collapse of the first coordinate to (0), and recovery of the retained reference.

This is a proposed bookkeeping convention, not a theorem that information can be recovered after arbitrary physical destruction.

## 3. From scaling to a fold: introduce an involution

A fold in the strict mathematical sense is not the zero-scale map. It is an involution.

Let (X) be a type and (f:X\to X). The involution condition is

[
f(f(x))=x\quad\text{for every }x\in X.
]

This condition says that applying the operation twice returns the original state. It makes (f) bijective, with (f) itself as its inverse.

A concrete Euclidean example is reflection across a hyperplane. Let (n) be a unit normal and let the hyperplane pass through (P_0). Then

[
R(P)=P-2\langle P-P_0,n\rangle n.
]

The normal component changes sign and the tangential component stays fixed. Applying (R) twice restores both components, so (R^2=I).

The fixed set is the crease:

[
H=\operatorname{Fix}(R)=\{P:\langle P-P_0,n\rangle=0\}.
]

The point reflection (g_{-1}) is also an involution, but its fixed set is just the centre (P_0); it is not the same geometry as reflection across a hyperplane.

## 4. Fixed points and paired states

For any involution (f), define

[
\operatorname{Fix}(f)=\{x:f(x)=x\},
\qquad
[x]=\{x,f(x)\}.
]

Each orbit has either one element (when (x) is fixed) or two elements. The involution partitions the state space into these orbits.

This is the exact algebraic content of “two sides meet at the crease.” The phrase is geometric intuition; the theorem is the orbit-size statement.

## 5. The quotient: identifying the two sides

Define (x\sim y) when (y=x) or (y=f(x)). The involution laws make this an equivalence relation. The quotient

[
X/\sim
]

is the space of orbits. Its projection (q:X\to X/\sim) satisfies

[
q(f(x))=q(x).
]

Thus the quotient forgets which representative of a two-point orbit was selected. This is a precise sense in which the fold becomes invisible after passing to the orbit chart.

## 6. The observer or cut is extra structure

A cut is a map (p:X\to X) that retracts onto the fixed set and is constant on each fold orbit:

[
p(p(x))=p(x),\qquad f(p(x))=p(x),\qquad p(f(x))=p(x).
]

Such a map is idempotent and cannot distinguish the two members of an orbit.

Important qualification: an arbitrary involution need not come with such a cut. Existence of a cut is additional structure (for example, an appropriate geometric projection onto a reflection hyperplane). The abstract involution theorem alone does not supply an observer.

## 7. Direction and reversal

If motion is included, direction must be part of the state. For a one-dimensional model use (S=(x,r,d)), with (d\in\{-1,+1\}). A turn changes direction:

[
T(x,r,d)=(x,r,-d),\qquad T^2=I.
]

A step that does not turn preserves (d), for example (x_{m+1}=x_m+d\,\Delta) with (Delta>0). In this model, reversing direction requires a turn event. This is a rule of the proposed discrete model, not a universal theorem about all motion.

## 8. The dependency chain

[
\boxed{
\text{datum}
\to\text{displacement}
\to\text{scale family}
\to\text{collapse/identity/reflection}
\to\text{involution}
\to\text{fixed set and orbits}
\to\text{quotient}
\to\text{optional cut}
}
]

The first three stages define the scale ledger. The involution and quotient stages define the fold ledger. The cut and direction state are further structures, not consequences of collapse alone.

## 9. Status of claims

| Claim | Status |
|---|---|
| (g_k(P)=P_0+k(P-P_0)), its composition law, and the cases (k=0,1,-1) | Exact algebra |
| An involution is bijective and has orbits of size one or two | Exact theorem |
| The orbit quotient identifies each point with its fold image | Exact quotient construction |
| A cut exists for every involution | False in general; extra structure is required |
| The normalized (1\to0\to1) retained-reference story | Proposed convention |
| “The Fold” as a universal account of physical reality or intelligence | Research hypothesis, not established by these constructions |

## 10. What follows next

Only after this foundation is stable should applications be derived. The efficient order is:

1. verify every algebraic statement in Lean;
2. distinguish the affine scale map from the involutive fold in the formal API;
3. add explicit examples and counterexamples;
4. test which later applications are exact consequences, reformulations, rhymes, or false friends;
5. approach computation and learning only after their required structures are stated independently.

The governing discipline is simple: derive each layer from its stated premises, and never let a resemblance substitute for a missing proof.


## 11. Shared first arrival at different speeds

The statement “everything reaches first at the same time at different speeds” can be made precise as a **synchronized first-arrival condition**. It is not a consequence of motion alone; it is a constraint on the trajectories.

Let each process (i\) have a path length (L_i\geq 0\), a constant speed (s_i>0\), and a common target. Its arrival time is

\[
T_i=\frac{L_i}{s_i}.
\]

They arrive simultaneously at time (T\) exactly when

\[
\forall i,\quad L_i=s_iT.
\]

Thus path lengths and speeds may differ while arrival times agree. For example, over a common duration (T=1\), path lengths (2,5,9\) require speeds (2,5,9\), respectively. None is “faster” in arrival time: each reaches its target at the same instant.

To say they reach **first** at that instant requires one more condition: no process has reached its target at any earlier time. For a progress function (d_i(t)\), define its first-arrival time as the least (t\geq0\) for which (d_i(t)=L_i\), when such a least time exists. Synchronization means these first-arrival times are all the same (T\), not merely that the processes happen to occupy their targets at time (T\).

This gives three distinct claims:

- **Exact conditional statement:** if (L_i=s_iT\) for every process, their constant-speed arrival times coincide at (T\).
- **First-arrival refinement:** if (T\) is the least target-hitting time for every trajectory, they all arrive first together.
- **Universal reading (“everything”):** not established by the equations. It is a proposed global principle that would require a defined system boundary, target, clock, and evidence that every included process satisfies the synchronization condition.

In the Origin → Fold development, this is a shared terminal event with distinct rates—not a claim that speeds become equal, that paths are identical, or that the terminal event causes the motion. The common time is an invariant of the synchronized family; each process retains its own rate and path.


## 12. The shared time-factor invariant

The discrete constant-rate model gives a stronger statement than common arrival alone. At any fixed observation tick (t), every path's remaining displacement factors as

\\[
R_i(t)=s_i(T-t).
\\]

The rate (s_i) is path-specific, while the time-to-arrival factor (T-t) is common to the whole synchronized family. Consequently, for any two rates (a,b),

\\[
R_a(t)\\,b=R_b(t)\\,a.
\\]

This cross-multiplied identity is the division-free form of proportional remaining displacement. It remains meaningful over natural-number arithmetic, including when a rate is zero; positive rates are separately required for strict first arrival. The Lean theorem `remainingDisplacement_cross_scale` formalizes this identity, and `remainingDisplacement_factors` records the shared factorization.

This is a **within-model invariant**, not a claim that arbitrary real-world processes share a clock or obey constant-rate motion. The common terminal time is one property; proportional remaining displacement at every shared observation tick is a stronger property supplied by the constant-rate model.


## 13. Variable-rate synchronization

Constant speed is sufficient for synchronized first arrival, but it is not necessary. A discrete trajectory can instead be specified by a rate sequence, with cumulative progress defined recursively:

\\[
P(0)=0,\\qquad P(n+1)=P(n)+s(n).
\\]

Two exact examples reach the same target, 3, at tick 2:

- Path A uses rates (1, 2), so its cumulative progress is (0, 1, 3).
- Path B uses rates (2, 1), so its cumulative progress is (0, 2, 3).

Their rate histories differ at every transition, yet each has first-arrival time 2. The Lean declarations `variableRateA_firstArrival`, `variableRateB_firstArrival`, and `variable_rates_distinct_but_synchronized` check this finite example directly.

This demonstrates a precise separation: **equal arrival time does not require equal instantaneous rates or identical histories**. The general sufficient condition remains that each trajectory is strictly short of its target at every earlier tick and exactly at the target at the shared tick. This is a discrete mathematical model, not evidence that arbitrary physical processes synchronize spontaneously.
