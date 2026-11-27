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

end Fold
