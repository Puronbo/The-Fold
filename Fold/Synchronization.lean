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

end Fold
