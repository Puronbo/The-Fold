# Synchronized arrival at different rates

This note records a precise, deliberately limited interpretation of the statement:

> Everything reaches first at the same time at different speeds.

The mathematical content is **simultaneous arrival with unequal rates**. It is not a universal law that unrelated processes must synchronize.

## Discrete model

Fix a destination D in Z, an arrival time T in N, and a rate v in N. For times 0 <= t <= T, define

    x_(v,T)(t) = D - v(T - t).

Then x_(v,T)(T) = D for every rate v. Thus all members of this family arrive at the same destination at the same time. Their one-tick displacement is v, so distinct rates remain distinct.

For two rates a < b and positive remaining time r, a*r < b*r. The faster trajectory has a larger remaining displacement when both trajectories are measured against the same destination and the same remaining time.

## What is and is not invariant

- **Shared:** destination D, arrival time T.
- **Variable:** rate v, initial position D-vT, and the path between start and arrival.
- **Not implied:** equal distance, equal path, equal energy, equal acceleration, or spontaneous synchronization of arbitrary systems.

The path formula is a constant-rate discrete model. Its natural-number subtraction is intended for 0 <= t <= T.

## Relation to Origin → Fold

The synchronization condition is a level-set condition on a family of trajectories:

    for every v, x_(v,T)(T) = D.

It is not itself an involution, a reflection, or a quotient. A Fold operation may be applied to trajectory states only after specifying the state space and proving that the operation is involutive. Synchronization alone does not supply that proof.

## Formalization

Fold/Synchronization.lean proves:

- every speed-indexed path reaches the common destination at T;
- the discrete-rate encoding is injective;
- distinct rates can share the same arrival event;
- a larger rate gives a larger remaining displacement for positive remaining time.

These are exact statements about the declared discrete model, not empirical claims about all physical processes.


## Beyond constant-rate paths

The generalization uses a gap function (g_p(t)\in\mathbb N), measuring the remaining distance of process (p) from its target. No linearity or constant-speed assumption is imposed.

A process first arrives at (T) if

\[
g_p(T)=0
\quad\text{and}\quad
\forall t<T,\;g_p(t)>0.
\]

For a family (P), simultaneous first arrival at (T) follows if these two conditions hold for every (p\in P). If (P) is nonempty, the common first-arrival time is unique.

This is a general criterion for discrete trajectories, not a prediction that arbitrary trajectories will satisfy it. The trajectories may have unrelated rates, acceleration patterns, pauses, or nonlinear changes; the theorem only applies when each gap is positive before the common time and zero at that time.



### Explicit nonlinear example

For remaining time (r=T-t), consider two gap profiles:

\[
g_1(t)=r^2,\qquad g_2(t)=r(r+1).
\]

They are different before arrival (one tick before, their gaps are (1) and (2)), but both are zero at (T) and positive at every earlier tick. Thus both have the same unique first-arrival time despite having different, nonlinear gap profiles.

This is an existence example inside the discrete model. It demonstrates that constant-rate motion is not necessary for synchronization; the necessary condition used by the theorem is positivity of each gap before the shared boundary and zero gap at that boundary.


### Explicit variable-rate example

The Lean module also constructs two cumulative-progress paths whose per-tick rates are

\[
(1,2)\qquad\text{and}\qquad(2,1).
\]

Both accumulate total progress (3) for the first time at tick (2), although their rate histories differ at each tick. This is a stronger example than the two gap profiles: it builds the paths from distinct, time-varying rates and verifies their common first hit.


## Fold-preservation criterion

A Fold does not automatically preserve first arrival at an arbitrary target. The exact sufficient condition is target invariance:

`hit(F(x)) ↔ hit(x)` for every state `x`.

For a trajectory `p(t)`, this condition makes the hit predicates of `p(t)` and `F(p(t))` equivalent at every tick. Therefore one trajectory reaches the target for the first time at (T) if and only if its pointwise-folded trajectory does. The proof checks both the hit at (T) and the absence of every earlier hit.

The crease is a canonical invariant target: for an involution, (F(x)) is fixed exactly when (x) is fixed. The Lean module `Fold/ArrivalFold.lean` formalizes both the general target-invariance theorem and the crease-specific corollary.

**Boundary of the result:** involutivity alone does not preserve a target that is not invariant under the fold. If the target changes under folding, compare against the transformed target (F^{-1}(H)) (which equals (F(H)) for an involution), rather than claiming the original target is unchanged.


### Transporting a non-invariant target

There is also an exact theorem when the target is **not** Fold-invariant. Instead of requiring the original path and folded path to hit the same target, transport the target backwards:

\[
H_F = \{x : F(x)\in H\}.
\]

Then the folded trajectory hits \(H\) at exactly the same times that the original trajectory hits \(H_F\). Because \(F(F(x))=x\), transporting the target twice recovers \(H\). Thus the correspondence is reversible.

This separates two cases cleanly:

- If \(F^{-1}(H)=H\), the target is invariant and first-arrival time is unchanged with the same target.
- Otherwise, the first-arrival time is still preserved under the paired transformation of trajectory and target; comparing against the untransformed target would be incorrect.

The Lean module `Fold/ArrivalFold.lean` formalizes target transport, its involutive round trip, and the first-arrival equivalence without assuming target invariance.


## First arrival under coordinate changes

The same argument extends beyond involutions. Let \(e:X\to Y\) be any coordinate map and let \(H\subseteq Y\) be a target. The corresponding target in the original coordinates is the preimage

\[
e^{-1}(H)=\{x\in X:e(x)\in H\}.
\]

A path \(p(t)\) hits \(e^{-1}(H)\) at exactly the ticks when the mapped path \(e(p(t))\) hits \(H\). Therefore the full first-arrival predicate—not only the arrival tick—is equivalent in the two coordinate descriptions. This forward result does not require the coordinate map to be injective or surjective.

If \(e\) is bijective with inverse \(e^{-1}\), target transport is reversible: pulling the target back and then pushing it forward recovers the original target. The Lean development records this as `coordinateTransportTarget_round_trip` and checks the first-arrival equivalence in `firstArrival_bijective_coordinate_change`.

**Interpretation:** a change of coordinates does not itself create synchronization. It preserves the event structure when the path and target are transformed consistently. A Fold is a special case, with its involution supplying its own inverse.


## First arrival under discrete time sampling

A clock \(c:\mathbb N\to\mathbb N\) samples an original trajectory only at times \(c(t)\). The exact first-arrival condition for the sampled path is

\[
R(c(T))\quad\text{and}\quad
\forall t<T,\;\neg R(c(t)).
\]

It excludes earlier **sampled** hits, not every earlier hit on the original time axis. This distinction matters: a clock can skip an earlier hit or collapse multiple indices onto the same sampled time.

The Lean theorem `firstArrival_sampled_characterization` states this condition exactly. The strict-clock theorem gives a useful sufficient direction: if \(c\) is strictly increasing and the original path first hits at \(c(T)\), then the sampled path first hits at index \(T\). The converse is not automatic because a sampled clock may skip an earlier hit.

A concrete counterexample uses the constant clock \(c(t)=3\). The original predicate \(R(n)\equiv(n=3)\) first holds at tick 3, but its sampled version holds at every index, including index 0. Thus the sampled path does not first arrive at index 3.

**Conclusion:** strict order preservation prevents earlier sampled indices from being mapped to the same or a later event time. To recover a two-way equivalence for arbitrary predicates, sampling must also retain all potentially earlier event times; strict increase alone does not supply that coverage.


## First arrival on the quotient chart

The orbit chart forgets which representative of a Fold-orbit was selected. A target predicate on states can therefore define a target on the chart only if it gives the same answer for both representatives.

The exact criterion is

\[
H(F(x))\iff H(x).
\]

If this holds, the state-level predicate descends to a predicate on the quotient chart. A trajectory's first arrival at that chart target is then equivalent to its first arrival at the original state-level target. The Lean development proves both directions:

- `target_descends_iff`: a chart predicate whose pullback is the given state predicate exists if and only if the state predicate is Fold-invariant.
- `firstArrival_descended_target`: the full first-arrival predicate is preserved when evaluated on the quotient chart.

This identifies exactly which target questions survive forgetting the representative.

**Boundary:** a non-invariant target cannot be a well-defined property of an orbit. One can still ask about it after choosing a representative, or transport the target together with the fold as in the preceding section, but that is not an intrinsic chart-level predicate.


## What first-arrival information survives the quotient?

The quotient chart forgets the choice between representatives in the same orbit. The formal result `firstArrival_chart_path_congr` makes the consequence explicit: if two state paths have the same chart image at every tick, then every chart-level target gives them exactly the same first-arrival result.

The stronger orbit formulation, `firstArrival_orbit_representative_independent`, requires only that the two representatives lie in the same Fold-orbit at each tick. The chart equality follows from the quotient's defining relation.

This separates two cases:

- **Recoverable from the quotient:** any event defined by a predicate on chart classes. Its first-arrival behavior is independent of representative.
- **Not recoverable from the quotient alone:** a representative-specific event that distinguishes two states in the same orbit. Such a predicate is not well-defined on the quotient unless additional representative data is retained.

Thus quotienting does not erase all event timing. It erases exactly the distinctions that the quotient identifies.


## Trajectory histories and representative independence

A state trajectory induces a chart trajectory by projecting every state to its Fold-orbit. Two state trajectories have exactly the same chart history if and only if their states are orbit-equivalent at every process and time (`chartPath_eq_iff_pointwise_orbit`). This is an exact characterization of the information discarded by the quotient, not an approximation.

Consequently, every property formulated solely in terms of the chart trajectory is independent of the chosen representatives (`chartPath_property_representative_independent`). At a single step, the chart does not change precisely when the next state lies in the same two-point orbit as the current state (`chart_step_eq_iff_orbit`). This does not say the underlying state is stationary: it may have moved from one representative to the other.


## Recovering a state from a quotient observation

A Fold-orbit has at most two representatives: a chosen representative \(s(q)\) and its folded partner \(F(s(q))\). Therefore, once a representative section \(s\) is supplied, a single Boolean selector records which representative is intended:

\[
\operatorname{reconstruct}(q,b)=
\begin{cases}
F(s(q)),&b=\text{true},\\
s(q),&b=\text{false}.
\end{cases}
\]

The Lean theorem `chart_reconstructState` proves that either choice maps back to the same quotient class. The theorem `reconstructState_exists_selector` proves that every state in that class can be recovered by one of the two choices. At a fixed point, the two choices may coincide.

For trajectories, the selector may vary with process and time. If it selects the actual representative at every tick, `firstArrival_reconstruction_exact` proves that every state-level first-arrival statement is recovered exactly.

**Information boundary:** the quotient class alone determines chart-level events, but not which representative-specific state occurred. A representative section plus one bit per observation is sufficient for this two-element orbit model. This is a conditional reconstruction theorem, not a claim that every quotient in mathematics needs one bit; fixed points and larger group orbits have different selector requirements.


### When is the reconstruction bit necessary?

The two selector values are not always two different states. The formal criterion is exact:

\[
\operatorname{reconstruct}(q,\mathrm{false})
=
\operatorname{reconstruct}(q,\mathrm{true})
\quad\Longleftrightarrow\quad
F(s(q))=s(q).
\]

Thus the selector is redundant on the crease, where the representative and its folded partner coincide. Away from the fixed set, the choices are distinct, and reconstructState_selector_unique_off_crease proves that a reconstructed state determines its Boolean selector uniquely. This refines the earlier existence theorem: one bit is sufficient everywhere, but it carries distinguishing information only off the crease.

The result is specific to a two-element involution orbit. It does not establish a universal one-bit bound for arbitrary quotient spaces or group actions.
