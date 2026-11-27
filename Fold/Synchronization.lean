/-
  Fold/Synchronization.lean

  A minimal exact model of simultaneous arrival at different constant rates.
  Paths are indexed by speed and share a destination and arrival time.
-/
namespace Fold

/-- A discrete constant-rate path ending at destination at time T. -/
def synchronizedPath (destination : Int) (speed arrival t : Nat) : Int :=
  destination - (Int.ofNat speed) * Int.ofNat (arrival - t)

/-- Every speed-indexed path reaches the common destination at time T. -/
theorem synchronizedPath_arrives (destination : Int) (speed arrival : Nat) :
    synchronizedPath destination speed arrival arrival = destination := by
  simp [synchronizedPath]

/-- The one-tick displacement records the chosen speed. -/
def discreteRate (speed : Nat) : Int := Int.ofNat speed

theorem discreteRate_injective :
    Function.Injective discreteRate := by
  intro a b h
  exact Int.ofNat.inj h

/-- Distinct rates remain distinguishable even though arrival is shared. -/
theorem distinct_rates_same_arrival
    (destination : Int) (arrival a b : Nat) (hab : a ≠ b) :
    synchronizedPath destination a arrival arrival =
        synchronizedPath destination b arrival arrival ∧
      discreteRate a ≠ discreteRate b := by
  constructor
  · rw [synchronizedPath_arrives, synchronizedPath_arrives]
  · intro h
    exact hab (discreteRate_injective h)

/-- Before arrival, a faster path has a larger remaining displacement
    when both paths have the same destination and remaining time. -/
theorem faster_has_larger_remaining_displacement
    (a b remaining : Nat) (hab : a < b) (hremaining : 0 < remaining) :
    a * remaining < b * remaining := by
  exact Nat.mul_lt_mul_of_pos_right hab hremaining


/-- Remaining distance in the discrete constant-rate model. -/
def remainingDisplacement (speed arrival t : Nat) : Nat :=
  speed * (arrival - t)

/-- Positive speed implies strictly positive remaining distance before arrival. -/
theorem remainingDisplacement_pos_before_arrival
    (speed arrival t : Nat) (hspeed : 0 < speed) (ht : t < arrival) :
    0 < remainingDisplacement speed arrival t := by
  exact Nat.mul_pos hspeed (Nat.sub_pos_of_lt ht)

/-- At the designated arrival time, remaining distance is zero. -/
theorem remainingDisplacement_zero_at_arrival
    (speed arrival : Nat) :
    remainingDisplacement speed arrival arrival = 0 := by
  simp [remainingDisplacement]


/-- A process first reaches its target at t if it reaches it then and
    never at any earlier natural-number time. -/
def FirstArrival {α : Type} (reaches : α → Nat → Prop)
    (process : α) (t : Nat) : Prop :=
  reaches process t ∧ ∀ earlier, earlier < t → ¬ reaches process earlier

/-- Remaining distance is the target-reach predicate for this model. -/
def reachesDestination (speed arrival t : Nat) : Prop :=
  remainingDisplacement speed arrival t = 0

/-- Every positive-speed path has its designated arrival as its first
    destination-reaching time. -/
theorem positiveSpeed_firstArrival (speed arrival : Nat)
    (hspeed : 0 < speed) :
    FirstArrival (fun v t => reachesDestination v arrival t) speed arrival := by
  constructor
  · simp [reachesDestination, remainingDisplacement]
  · intro earlier hearlier hzero
    have hpositive :=
      remainingDisplacement_pos_before_arrival speed arrival earlier hspeed hearlier
    unfold reachesDestination at hzero
    omega


/-- Positive speed is essential: a zero-speed path is already at the
    target in this remaining-distance encoding at every tick, so a
    positive designated arrival cannot be its first arrival. -/
theorem zeroSpeed_not_firstArrival (arrival : Nat) (harrival : 0 < arrival) :
    ¬ FirstArrival
      (fun v t => reachesDestination v arrival t) 0 arrival := by
  intro hfirst
  have hearly := hfirst.2 0 harrival
  apply hearly
  simp [reachesDestination, remainingDisplacement]

/-- A list of positive-speed paths is synchronized at their common first
    arrival time. -/
def SynchronizedFirstArrival (arrival : Nat) (speeds : List Nat) : Prop :=
  ∀ speed, speed ∈ speeds →
    FirstArrival (fun v t => reachesDestination v arrival t) speed arrival

theorem positive_speeds_synchronized_first_arrival
    (arrival : Nat) (speeds : List Nat)
    (hpositive : ∀ speed, speed ∈ speeds → 0 < speed) :
    SynchronizedFirstArrival arrival speeds := by
  intro speed hmem
  exact positiveSpeed_firstArrival speed arrival (hpositive speed hmem)


/-- A process cannot have two distinct first-arrival times. -/
theorem firstArrival_unique {α : Type} (reaches : α → Nat → Prop)
    (process : α) (a b : Nat)
    (ha : FirstArrival reaches process a)
    (hb : FirstArrival reaches process b) :
    a = b := by
  have hab : a ≤ b := by
    by_cases h : a ≤ b
    · exact h
    · exact False.elim ((ha.2 b (Nat.lt_of_not_ge h)) hb.1)
  have hba : b ≤ a := by
    by_cases h : b ≤ a
    · exact h
    · exact False.elim ((hb.2 a (Nat.lt_of_not_ge h)) ha.1)
  exact Nat.le_antisymm hab hba

/-- Any member of a family determines the unique synchronized boundary
    when its reach predicate is independent of that boundary. -/
theorem common_first_arrival_unique
    {α : Type} (reaches : α → Nat → Prop)
    (process : α) (a b : Nat)
    (ha : FirstArrival reaches process a)
    (hb : FirstArrival reaches process b) :
    a = b :=
  firstArrival_unique reaches process a b ha hb


/-- Generic synchronized first-arrival condition for a fixed reach relation. -/
def SynchronizedBoundary {α : Type} (reaches : α → Nat → Prop)
    (processes : List α) (time : Nat) : Prop :=
  ∀ process, process ∈ processes → FirstArrival reaches process time

/-- A nonempty synchronized family has at most one common first-arrival time. -/
theorem synchronizedBoundary_unique
    {α : Type} (reaches : α → Nat → Prop)
    (processes : List α) (process : α) (a b : Nat)
    (hmem : process ∈ processes)
    (ha : SynchronizedBoundary reaches processes a)
    (hb : SynchronizedBoundary reaches processes b) :
    a = b :=
  firstArrival_unique reaches process a b (ha process hmem) (hb process hmem)


/-- Remaining displacement is proportional to speed with one shared
    time-to-arrival factor. This cross-multiplied form avoids division,
    so it remains valid over natural numbers. -/
theorem remainingDisplacement_cross_scale
    (a b arrival t : Nat) :
    remainingDisplacement a arrival t * b =
      remainingDisplacement b arrival t * a := by
  simp [remainingDisplacement]
  ac_rfl

/-- The shared factor in every path's remaining displacement. -/
def timeToArrival (arrival t : Nat) : Nat := arrival - t

/-- The remaining displacement factors into its individual rate and
    the family-wide time-to-arrival factor. -/
theorem remainingDisplacement_factors
    (speed arrival t : Nat) :
    remainingDisplacement speed arrival t =
      speed * timeToArrival arrival t := by
  rfl


/-- A general trajectory is represented by its nonnegative integer gap
    from a target. It need not have constant rate or a linear path. -/
def GapFirstArrival {α : Type} (gap : α → Nat → Nat)
    (process : α) (time : Nat) : Prop :=
  FirstArrival (fun p t => gap p t = 0) process time

/-- If a trajectory's gap is zero at T and strictly positive at every
    earlier tick, then T is its unique first-arrival time. -/
theorem firstArrival_of_positive_gap
    {α : Type} (gap : α → Nat → Nat) (process : α) (time : Nat)
    (hat : gap process time = 0)
    (hbefore : ∀ earlier, earlier < time → 0 < gap process earlier) :
    GapFirstArrival gap process time := by
  constructor
  · exact hat
  · intro earlier hearlier hzero
    have hpos := hbefore earlier hearlier
    omega

/-- A family of arbitrary, potentially nonlinear discrete trajectories
    synchronizes when each gap vanishes for the first time at the same T. -/
def SynchronizedGapArrival {α : Type} (gap : α → Nat → Nat)
    (processes : List α) (time : Nat) : Prop :=
  ∀ process, process ∈ processes → GapFirstArrival gap process time

/-- Individual positive-gap conditions are sufficient for simultaneous
    first arrival, without assuming equal speeds or constant rates. -/
theorem synchronized_of_positive_gaps
    {α : Type} (gap : α → Nat → Nat) (processes : List α) (time : Nat)
    (hat : ∀ process, process ∈ processes → gap process time = 0)
    (hbefore : ∀ process, process ∈ processes →
      ∀ earlier, earlier < time → 0 < gap process earlier) :
    SynchronizedGapArrival gap processes time := by
  intro process hmem
  exact firstArrival_of_positive_gap gap process time
    (hat process hmem) (hbefore process hmem)

/-- For a nonempty family, a synchronized first-arrival time is unique,
    even when trajectories are nonlinear and have unrelated rates. -/
theorem synchronizedGapArrival_unique
    {α : Type} (gap : α → Nat → Nat) (processes : List α)
    (process : α) (a b : Nat) (hmem : process ∈ processes)
    (ha : SynchronizedGapArrival gap processes a)
    (hb : SynchronizedGapArrival gap processes b) :
    a = b :=
  firstArrival_unique (fun p t => gap p t = 0) process a b
    (ha process hmem) (hb process hmem)


/-- Two example nonlinear gap profiles with a common arrival boundary.
    The Boolean index selects a quadratic profile or a quadratic profile
    with a different coefficient. -/
def nonlinearExampleGap (profile : Bool) (arrival t : Nat) : Nat :=
  let remaining := arrival - t
  if profile then remaining * remaining else remaining * (remaining + 1)

/-- Both nonlinear profiles vanish at their shared designated time. -/
theorem nonlinearExampleGap_zero (profile : Bool) (arrival : Nat) :
    nonlinearExampleGap profile arrival arrival = 0 := by
  simp [nonlinearExampleGap]

/-- Both nonlinear profiles remain strictly positive before arrival. -/
theorem nonlinearExampleGap_positive (profile : Bool) (arrival t : Nat)
    (ht : t < arrival) :
    0 < nonlinearExampleGap profile arrival t := by
  have hr : 0 < arrival - t := Nat.sub_pos_of_lt ht
  cases profile
  · change 0 < (arrival - t) * ((arrival - t) + 1)
    exact Nat.mul_pos hr (by omega)
  · change 0 < (arrival - t) * (arrival - t)
    exact Nat.mul_pos hr hr

/-- These distinct nonlinear profiles have the same unique first-arrival
    time, without being constant-rate paths. -/
theorem nonlinear_examples_synchronize (arrival : Nat) :
    SynchronizedGapArrival (fun profile t => nonlinearExampleGap profile arrival t)
      [true, false] arrival := by
  intro profile hmem
  apply firstArrival_of_positive_gap
  · exact nonlinearExampleGap_zero profile arrival
  · intro earlier hearlier
    exact nonlinearExampleGap_positive profile arrival earlier hearlier

/-- One tick before arrival, the two profiles already have different gaps. -/
theorem nonlinear_profiles_differ_one_tick (arrival : Nat) :
    nonlinearExampleGap true (arrival + 1) arrival ≠
      nonlinearExampleGap false (arrival + 1) arrival := by
  simp [nonlinearExampleGap]


/-- Cumulative progress generated by a time-varying nonnegative rate.
    The rate used on the transition from n to n+1 is rate n. -/
def cumulativeProgress (rate : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => cumulativeProgress rate n + rate n

/-- A trajectory whose rate changes from 1 to 2 over two ticks. -/
def variableRateA (n : Nat) : Nat :=
  if n = 0 then 1 else if n = 1 then 2 else 0

/-- A second trajectory with the same total progress but reversed rates. -/
def variableRateB (n : Nat) : Nat :=
  if n = 0 then 2 else if n = 1 then 1 else 0

/-- The first variable-rate trajectory reaches total progress 3 for
    the first time at tick 2. -/
theorem variableRateA_firstArrival :
    FirstArrival (fun _ t => cumulativeProgress variableRateA t = 3) 0 2 := by
  change cumulativeProgress variableRateA 2 = 3 ∧
    ∀ earlier, earlier < 2 → cumulativeProgress variableRateA earlier ≠ 3
  constructor
  · simp [cumulativeProgress, variableRateA]
  · intro earlier hearlier hreach
    have hcases : earlier = 0 ∨ earlier = 1 := by omega
    rcases hcases with h0 | h1
    · subst earlier
      simp [cumulativeProgress, variableRateA] at hreach
    · subst earlier
      simp [cumulativeProgress, variableRateA] at hreach

/-- The second variable-rate trajectory also reaches total progress 3
    for the first time at tick 2, despite having a different rate history. -/
theorem variableRateB_firstArrival :
    FirstArrival (fun _ t => cumulativeProgress variableRateB t = 3) 0 2 := by
  change cumulativeProgress variableRateB 2 = 3 ∧
    ∀ earlier, earlier < 2 → cumulativeProgress variableRateB earlier ≠ 3
  constructor
  · simp [cumulativeProgress, variableRateB]
  · intro earlier hearlier hreach
    have hcases : earlier = 0 ∨ earlier = 1 := by omega
    rcases hcases with h0 | h1
    · subst earlier
      simp [cumulativeProgress, variableRateB] at hreach
    · subst earlier
      simp [cumulativeProgress, variableRateB] at hreach

/-- The rate histories differ at both ticks, while their first-arrival
    times coincide. -/
theorem variable_rates_distinct_but_synchronized :
    variableRateA 0 ≠ variableRateB 0 ∧
    variableRateA 1 ≠ variableRateB 1 ∧
    FirstArrival (fun _ t => cumulativeProgress variableRateA t = 3) 0 2 ∧
    FirstArrival (fun _ t => cumulativeProgress variableRateB t = 3) 0 2 := by
  exact ⟨by decide, by decide,
    variableRateA_firstArrival, variableRateB_firstArrival⟩



/-- A trajectory may pause for a tick and still have a well-defined
    first-arrival time. -/
def pausedRate (n : Nat) : Nat :=
  if n = 0 then 1 else if n = 1 then 0 else if n = 2 then 2 else 0

/-- The paused trajectory has cumulative positions 0, 1, 1, 3. -/
theorem pausedRate_firstArrival :
    FirstArrival (fun _ t => cumulativeProgress pausedRate t = 3) 0 3 := by
  change cumulativeProgress pausedRate 3 = 3 ∧
    ∀ earlier, earlier < 3 → cumulativeProgress pausedRate earlier ≠ 3
  constructor
  · simp [cumulativeProgress, pausedRate]
  · intro earlier hearlier hreach
    have hcases : earlier = 0 ∨ earlier = 1 ∨ earlier = 2 := by omega
    rcases hcases with h0 | h1 | h2
    · subst earlier
      simp [cumulativeProgress, pausedRate] at hreach
    · subst earlier
      simp [cumulativeProgress, pausedRate] at hreach
    · subst earlier
      simp [cumulativeProgress, pausedRate] at hreach

/-- A zero-rate transition (a pause) does not invalidate first arrival;
    it simply changes the common arrival time when it occurs before the target. -/
theorem pause_preserves_first_arrival :
    pausedRate 1 = 0 ∧
    cumulativeProgress pausedRate 1 = cumulativeProgress pausedRate 2 ∧
    FirstArrival (fun _ t => cumulativeProgress pausedRate t = 3) 0 3 := by
  exact ⟨by decide, by decide, pausedRate_firstArrival⟩



/-- Cumulative signed progress permits retreats as well as advances.
    The increment rate(n) is applied on the transition n to n+1. -/
def cumulativeSignedProgress (rate : Nat → Int) : Nat → Int
  | 0 => 0
  | n + 1 => cumulativeSignedProgress rate n + rate n

/-- A path that advances, retreats, then advances to the target. -/
def reversalRate (n : Nat) : Int :=
  if n = 0 then 2 else if n = 1 then -1 else if n = 2 then 2 else 0

/-- Signed trajectory positions are 0, 2, 1, 3: it retreats before
    reaching the target, but does not hit the target early. -/
theorem reversalRate_firstArrival :
    FirstArrival (fun _ t => cumulativeSignedProgress reversalRate t = 3) 0 3 := by
  change cumulativeSignedProgress reversalRate 3 = 3 ∧
    ∀ earlier, earlier < 3 →
      ¬ cumulativeSignedProgress reversalRate earlier = 3
  constructor
  · simp [cumulativeSignedProgress, reversalRate]
  · intro earlier hearlier hreach
    have hcases : earlier = 0 ∨ earlier = 1 ∨ earlier = 2 := by omega
    rcases hcases with h0 | h1 | h2
    · subst earlier
      simp [cumulativeSignedProgress, reversalRate] at hreach
    · subst earlier
      simp [cumulativeSignedProgress, reversalRate] at hreach
    · subst earlier
      simp [cumulativeSignedProgress, reversalRate] at hreach

/-- The middle increment is negative, so the path genuinely reverses;
    nevertheless, its first target hit is exactly tick 3. -/
theorem reversal_still_has_first_arrival :
    reversalRate 1 < 0 ∧
    cumulativeSignedProgress reversalRate 2 = 1 ∧
    FirstArrival (fun _ t => cumulativeSignedProgress reversalRate t = 3) 0 3 := by
  exact ⟨by decide, by decide, reversalRate_firstArrival⟩


/-- A discrete path can overshoot a target without landing on it, then
    return and hit it exactly.  The sampled positions are 0, 4, 2, 3. -/
def overshootRate (n : Nat) : Int :=
  if n = 0 then 4 else if n = 1 then -2 else if n = 2 then 1 else 0

/-- The overshoot trajectory first reaches 3 at tick 3, despite being
    strictly above 3 at tick 1. -/
theorem overshootRate_firstArrival :
    FirstArrival (fun _ t => cumulativeSignedProgress overshootRate t = 3) 0 3 := by
  change cumulativeSignedProgress overshootRate 3 = 3 ∧
    ∀ earlier, earlier < 3 →
      ¬ cumulativeSignedProgress overshootRate earlier = 3
  constructor
  · simp [cumulativeSignedProgress, overshootRate]
  · intro earlier hearlier hreach
    have hcases : earlier = 0 ∨ earlier = 1 ∨ earlier = 2 := by omega
    rcases hcases with h0 | h1 | h2
    · subst earlier
      simp [cumulativeSignedProgress, overshootRate] at hreach
    · subst earlier
      simp [cumulativeSignedProgress, overshootRate] at hreach
    · subst earlier
      simp [cumulativeSignedProgress, overshootRate] at hreach

/-- Overshooting the target's numeric level is compatible with first
    arrival when the discrete path does not equal the target at that tick. -/
theorem overshoot_and_return_first_arrival :
    cumulativeSignedProgress overshootRate 1 > 3 ∧
    cumulativeSignedProgress overshootRate 2 = 2 ∧
    FirstArrival (fun _ t => cumulativeSignedProgress overshootRate t = 3) 0 3 := by
  exact ⟨by decide, by decide, overshootRate_firstArrival⟩


/-- First arrival depends only on the reach predicate, not on its chosen
    equivalent representation.  Pointwise logical equivalence preserves
    both the target hit and every earlier non-hit. -/
theorem firstArrival_congr
    {α : Type} (reachesA reachesB : α → Nat → Prop)
    (process : α) (time : Nat)
    (hequiv : ∀ t, reachesA process t ↔ reachesB process t) :
    FirstArrival reachesA process time ↔
      FirstArrival reachesB process time := by
  constructor
  · intro hA
    constructor
    · exact (hequiv time).mp hA.1
    · intro earlier hearlier hB
      exact hA.2 earlier hearlier ((hequiv earlier).mpr hB)
  · intro hB
    constructor
    · exact (hequiv time).mpr hB.1
    · intro earlier hearlier hA
      exact hB.2 earlier hearlier ((hequiv earlier).mp hA)

/-- Translating both a signed trajectory and its target by the same
    integer datum leaves its first-arrival times unchanged. -/
theorem signed_firstArrival_translation_invariant
    (rate : Nat → Int) (target offset : Int)
    (process : Unit) (time : Nat) :
    FirstArrival
      (fun _ t => cumulativeSignedProgress rate t + offset =
        target + offset) process time ↔
    FirstArrival
      (fun _ t => cumulativeSignedProgress rate t = target)
      process time := by
  apply firstArrival_congr
  intro t
  constructor <;> intro h <;> omega


/-- A strictly increasing re-indexing of discrete time preserves first
    arrival at the corresponding sampled time.  Earlier samples remain
    earlier, so no new pre-arrival hit can appear. -/
theorem firstArrival_strict_time_reindex
    {α : Type} (reaches : α → Nat → Prop)
    (process : α) (clock : Nat → Nat)
    (hclock : ∀ {a b : Nat}, a < b → clock a < clock b)
    (time : Nat) :
    FirstArrival reaches process (clock time) →
      FirstArrival (fun p t => reaches p (clock t)) process time := by
  intro h
  constructor
  · exact h.1
  · intro earlier hearlier hhit
    exact h.2 (clock earlier) (hclock earlier time hearlier) hhit

/-- For a positive integer clock multiplier, scaling discrete time
    preserves the first-arrival index after translating the target index
    to the corresponding clock sample. -/
theorem firstArrival_nat_mul_time_reindex
    {α : Type} (reaches : α → Nat → Prop)
    (process : α) (factor time : Nat) (hfactor : 0 < factor) :
    FirstArrival reaches process (factor * time) →
      FirstArrival (fun p t => reaches p (factor * t)) process time := by
  apply firstArrival_strict_time_reindex reaches process
    (fun t => factor * t)
    (by
      intro a b hab
      exact Nat.mul_lt_mul_of_pos_left hab hfactor)
    time

end Fold
