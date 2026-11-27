import Fold.Basic

namespace Fold.PrimeEncoding

/-- A finite prime-exponent entry. Primality and canonical ordering are
    separate invariants; this first layer proves the arithmetic of lists. -/
abbrev Factor := Nat × Nat

/-- Decode a finite list of prime-power entries. -/
def decode : List Factor → Nat
  | [] => 1
  | (p, e) :: rest => p ^ e * decode rest

/-- Merge two finite factor lists. Repeated primes are permitted here:
    canonical normalization can be added as a separate layer. -/
def merge (left right : List Factor) : List Factor :=
  left ++ right

/-- Appending factor lists multiplies their decoded values. -/
theorem decode_merge (left right : List Factor) :
    decode (merge left right) = decode left * decode right := by
  induction left with
  | nil =>
      simp [merge, decode]
  | cons entry rest ih =>
      rcases entry with ⟨p, e⟩
      simp [merge, decode, ih, Nat.mul_assoc]

/-- A Fold arithmetic state keeps its visible position, finite factor
    representation, and orientation as independent components. -/
structure State where
  position : Nat
  factors : List Factor
  forward : Bool
  deriving DecidableEq, Repr

/-- Collapse changes only the visible position. -/
def collapse (s : State) : State :=
  { s with position := 0 }

/-- Turning changes only orientation. -/
def turn (s : State) : State :=
  { s with forward := !s.forward }

/-- The represented arithmetic value. -/
def value (s : State) : Nat :=
  decode s.factors

/-- Collapse preserves the finite arithmetic representation. -/
theorem collapse_preserves_factors (s : State) :
    (collapse s).factors = s.factors := rfl

/-- Collapse preserves the represented arithmetic value. -/
theorem collapse_preserves_value (s : State) :
    value (collapse s) = value s := rfl

/-- Collapse sets the visible position to zero. -/
theorem collapse_zero (s : State) :
    (collapse s).position = 0 := rfl

/-- Turning twice restores the original orientation and complete state. -/
theorem turn_involutive (s : State) :
    turn (turn s) = s := by
  cases s
  simp [turn, Bool.not_not]

/-- Turning does not change the represented arithmetic value. -/
theorem turn_preserves_value (s : State) :
    value (turn s) = value s := rfl

/-- Multiplication of represented values is implemented by list merge. -/
theorem multiply_correct (left right : List Factor) :
    decode (merge left right) = decode left * decode right :=
  decode_merge left right

end Fold.PrimeEncoding
