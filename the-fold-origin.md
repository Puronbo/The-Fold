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


## 14. Pauses, reversals, and first arrival

A zero increment is a pause, not an arrival. For example, the nonnegative rate sequence (1, 0, 2) produces cumulative positions (0, 1, 1, 3). The target 3 is first reached at tick 3. The Lean result `pausedRate_firstArrival` verifies that no earlier tick reaches the target.

To model retreats, allow signed increments and define

\\[
P(0)=0,\\qquad P(n+1)=P(n)+s(n),\\quad s(n)\\in\\mathbb Z.
\\]

The sequence (2, -1, 2) produces positions (0, 2, 1, 3). It moves backward on the second transition, then reaches 3 for the first time at tick 3. The Lean results `reversalRate_firstArrival` and `reversal_still_has_first_arrival` verify this finite trajectory.

For signed or otherwise non-monotone paths, the exact first-arrival condition is

\\[
P(T)=G\\quad\\text{and}\\quad
\\forall t<T,\\;P(t)\\ne G.
\\]

It is not generally equivalent to requiring every earlier position to be below the target: a path may overshoot and return without hitting the target exactly. First arrival is about the first equality with the target, not monotonicity. These examples formalize discrete trajectories only; they do not establish a universal law of physical synchronization.

## 15. Discrete overshoot and return

A signed-rate path can move numerically beyond a target without equaling it
at a sampled tick, then return and hit the target later. The Lean example
uses increments `(4, -2, 1)`, giving sampled positions
`0 → 4 → 2 → 3`. For target `3`, tick 1 is above the target, tick 2
is below it, and tick 3 is the first exact hit.

This is a statement about a discrete sequence of sampled states. It does
not imply that a continuous path can pass from 0 to 4 without crossing 3;
a continuous interpolation would generally cross intermediate values.
The exact predicate remains: the target is attained at time T and is not
attained at any earlier sampled time. Numeric overshoot alone does not
invalidate first arrival.



## 15. Overshoot and return

A signed trajectory can pass numerically beyond a target without hitting the target exactly, then reverse and hit it later. The increment sequence (4, -2, 1) produces positions (0, 4, 2, 3). For target 3, the first sampled equality occurs at tick 3: tick 1 is an overshoot, not an arrival, and tick 2 is a retreat but still not an arrival.

The Lean results `overshootRate_firstArrival` and `overshoot_and_return_first_arrival` verify this example. It makes the distinction precise: first arrival is the first time the state satisfies the target predicate, not the first time a numerical threshold is crossed. If the target is instead defined as crossing a boundary (for example, position greater than or equal to 3), this trajectory's first crossing is tick 1. The event predicate must therefore be stated before an arrival theorem can be interpreted.

## 16. General synchronized first-arrival theorem

Let a family of processes be indexed by a type (A), with a shared natural-number clock and an arbitrary reach predicate (H : A → ℕ → Prop). The exact synchronized-first-arrival condition at time (T) is

\\[
\\forall a\\in A,\\quad H(a,T)\\quad\\text{and}\\quad
\\forall t<T,\\;\\neg H(a,t).
\\]

No shared rate, monotonicity, or common trajectory shape is required. This is formalized by `SynchronizedBoundary` and `synchronizedBoundary_unique`: if the family is nonempty and every member has first-arrival time (T), then that common time is unique. For nonnegative gap models, `synchronized_of_positive_gaps` gives a sufficient certificate: each gap is zero at (T) and strictly positive at every earlier tick. For signed paths, use exact target equality and the no-earlier-hit condition instead; a positive-gap argument alone does not cover reversals or overshoots.

This is a conditional theorem about a specified family, clock, and event predicate. It does not assert that every process in nature shares a clock or synchronizes.


## 16. First arrival is invariant under a change of datum

The first-arrival predicate is preserved by any pointwise equivalent
description of reaching the target. In particular, translating every
signed position and the target by the same integer datum does not change
which tick is first:

\\[
P(t)=G
\\quad\\Longleftrightarrow\\quad
(P(t)+r)=(G+r).
\\]

The Lean theorem `firstArrival_congr` proves the general logical
invariance, and `signed_firstArrival_translation_invariant` applies it
to cumulative signed progress. This is the precise datum-independence
available here: a common translation preserves equality and therefore
preserves first arrival. It does not say that arbitrary rescaling,
non-injective collapse, or a change in the trajectory's increments
preserves arrival times.


## 17. Process-specific targets and reversible fold transport

A synchronized family need not share one numerical target or even one fold. Let each process (a) have its own state path (P_a(t)), target predicate (H_a), and involution (f_a). Define the transported target by

\\[
H'_a(x)\\;\\Longleftrightarrow\\;H_a(f_a(x)).
\\]

Then, at every tick, (H_a(f_a(P_a(t)))) and (H'_a(P_a(t))) are definitionally the same event. Consequently, the family has the same synchronized first-arrival time before and after this change of description. No assumption that the original targets are individually fold-invariant is needed: the target is moved along with the state transformation.

Because each (f_a) is an involution, transporting each target a second time restores it:

\\[
H''_a(x)=H_a(f_a(f_a(x)))=H_a(x).
\\]

The Lean declarations `foldTransportFamilyTarget`, `synchronizedBoundary_fold_target_transport`, and `foldTransportFamilyTarget_involutive` formalize this process-by-process result. The conclusion is exact but conditional: it preserves arrival under a coordinated change of representation, not under an arbitrary fold while holding a non-invariant target fixed.
