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
