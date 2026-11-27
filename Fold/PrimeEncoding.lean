import Fold.Basic

namespace Fold.PrimeEncoding

abbrev Factor := Nat × Nat

def decode : List Factor → Nat
  | [] => 1
  | (p, e) :: rest => p ^ e * decode rest

def merge (left right : List Factor) : List Factor :=
  left ++ right

theorem decode_merge (left right : List Factor) :
    decode (merge left right) = decode left * decode right := by
  induction left with
  | nil =>
      simp [merge, decode]
  | cons entry rest ih =>
      rcases entry with ⟨p, e⟩
      calc
        decode (merge ((p, e) :: rest) right)
            = p ^ e * decode (merge rest right) := by
                simp [merge, decode]
        _ = p ^ e * (decode rest * decode right) := by
              rw [ih]
        _ = (p ^ e * decode rest) * decode right := by
              rw [Nat.mul_assoc]
        _ = decode ((p, e) :: rest) * decode right := by
              simp [decode]

structure State where
  position : Nat
  factors : List Factor
  forward : Bool
  deriving DecidableEq, Repr

def collapse (s : State) : State :=
  { s with position := 0 }

def turn (s : State) : State :=
  { s with forward := !s.forward }

def value (s : State) : Nat :=
  decode s.factors

theorem collapse_preserves_factors (s : State) :
    (collapse s).factors = s.factors := rfl

theorem collapse_preserves_value (s : State) :
    value (collapse s) = value s := rfl

theorem collapse_zero (s : State) :
    (collapse s).position = 0 := rfl

theorem turn_involutive (s : State) :
    turn (turn s) = s := by
  cases s
  simp [turn, Bool.not_not]

theorem turn_preserves_value (s : State) :
    value (turn s) = value s := rfl

theorem multiply_correct (left right : List Factor) :
    decode (merge left right) = decode left * decode right :=
  decode_merge left right

end Fold.PrimeEncoding
