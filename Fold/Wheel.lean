/-
  Fold/Wheel.lean

  The combinatorial wheel: one turn is `n ↦ (n + 1) % m`; `m` turns
  return every mark to its residue.  This is the exact closure content
  of `m = π/α`; the analytic relation between `m` and the angle is not
  formalized here, and the crystallographic restriction
  `m ∈ {1,2,3,4,6}` is a separate theorem about lattices, stated in the
  prose note but not proved in this file.
-/
import Init

namespace Fold

/-- One turn of an `m`-spoke wheel. -/
def rot (m : Nat) (n : Nat) : Nat := (n + 1) % m

/-- `k` turns, starting at a residue. -/
def rotIter (m : Nat) : Nat → Nat → Nat
  | 0, n => n
  | k + 1, n => rot m (rotIter m k n)

theorem rotIter_succ (m k n : Nat) :
    rotIter m (k + 1) n = rot m (rotIter m k n) := rfl

/-- After `k` turns a mark that starts at residue `n % m` is at
`(n + k) % m`. -/
theorem rotIter_eq (m k n : Nat) : rotIter m k (n % m) = (n + k) % m := by
  induction k with
  | zero => rfl
  | succ k ih =>
      rw [rotIter_succ, ih]
      unfold rot
      rw [Nat.mod_add_mod, Nat.add_assoc]

/-- The wheel closes after `m` turns: the mark returns to its residue.
This is the exact closure law; the identification `m = π/α` is the
analytic statement relating the spoke count to the twist angle. -/
theorem rot_period (m n : Nat) : rotIter m m (n % m) = n % m := by
  rw [rotIter_eq, Nat.add_mod, Nat.mod_self, Nat.add_zero, Nat.mod_mod]

/-- A mark already on the rim is fixed by a full turn. -/
theorem rot_closed (m n : Nat) : rotIter m m (n % m) = n % m :=
  rot_period m n

end Fold
