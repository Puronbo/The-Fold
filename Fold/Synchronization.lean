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

end Fold
