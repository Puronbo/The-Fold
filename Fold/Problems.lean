/-
  Fold/Problems.lean

  Finite, checkable facts from the second problem map.  These are not
  analogies: each is a computation that `decide` closes.  The prose in
  `the-fold-problems.md` says which problem each one is allowed to
  touch and which inference would be the false friend.

  Included here:

  * Simpson's reversal — a quotient (pooling) need not preserve order;
  * the tolerance relation — reflexive and symmetric, not transitive,
    so it generates no quotient;
  * contraposition — the involution on a pair of truth values;
  * Monty Hall — switching wins two of the three configurations.
-/
import Init

namespace Fold

/-! ## Simpson's reversal

Two strata in which treatment beats control, and a pool in which control
beats treatment.  The counts are the classical kidney-stone table; the
comparisons are cross-multiplied so that no division is needed. -/

/-- Treatment wins both strata; the pool reverses. -/
theorem simpson_reversal :
    (81 : Nat) * 270 > 234 * 87 ∧
    (192 : Nat) * 80 > 55 * 263 ∧
    (273 : Nat) * 350 < 289 * 350 := by
  decide

/-- The pooled totals are the sums of the strata. -/
theorem simpson_totals :
    (81 : Nat) + 192 = 273 ∧
    (87 : Nat) + 263 = 350 ∧
    (234 : Nat) + 55 = 289 ∧
    (270 : Nat) + 80 = 350 := by
  decide

/-! ## The tolerance relation

`Tolerance a b` says `a` and `b` differ by at most one.  It is
reflexive and symmetric, and it is not transitive: `0 ~ 1` and `1 ~ 2`
but not `0 ~ 2`.  A tolerance is not an equivalence, so it has no
quotient in the Fold's sense. -/

/-- `a` and `b` differ by at most one. -/
def Tolerance (a b : Nat) : Prop := a ≤ b + 1 ∧ b ≤ a + 1

theorem tolerance_refl (a : Nat) : Tolerance a a := by
  unfold Tolerance
  omega

theorem tolerance_symm {a b : Nat} (h : Tolerance a b) : Tolerance b a := by
  unfold Tolerance at *
  omega

/-- Tolerance is not transitive, so it does not generate an equivalence
relation and the quotient does not exist. -/
theorem tolerance_not_trans :
    ¬ ∀ a b c : Nat, Tolerance a b → Tolerance b c → Tolerance a c := by
  intro h
  have h01 : Tolerance 0 1 := by unfold Tolerance; omega
  have h12 : Tolerance 1 2 := by unfold Tolerance; omega
  have h02 : Tolerance 0 2 := h 0 1 2 h01 h12
  unfold Tolerance at h02
  omega

/-- The exact summary: reflexive, symmetric, not transitive. -/
theorem tolerance_structure :
    (∀ a : Nat, Tolerance a a) ∧
    (∀ a b : Nat, Tolerance a b → Tolerance b a) ∧
    (¬ ∀ a b c : Nat, Tolerance a b → Tolerance b c → Tolerance a c) :=
  ⟨tolerance_refl, fun _ _ h => tolerance_symm h, tolerance_not_trans⟩

/-! ## Contraposition

`(P → Q) ↔ (¬Q → ¬P)` is an exact involution on the pair of truth
values.  What it does not preserve is confirmation: the involution is a
logical identity, not a theory of evidence. -/

/-- Material implication on `Bool`. -/
def imp (a b : Bool) : Bool := !a || b

/-- Contraposition is an involution on the pair. -/
theorem contraposition (a b : Bool) : imp a b = imp (!b) (!a) := by
  cases a <;> cases b <;> rfl

/-- The pair map `(a,b) ↦ (¬b,¬a)`. -/
def swapNot (p : Bool × Bool) : Bool × Bool := (!p.2, !p.1)

/-- The pair map is an involution: contraposition applied twice is the identity. -/
theorem contraposition_invol (p : Bool × Bool) : swapNot (swapNot p) = p := by
  rcases p with ⟨a, b⟩
  cases a <;> cases b <;> rfl

/-! ## Monty Hall

With the car fixed behind door `0`, switching wins exactly when the
initial pick was not `0`: two of the three configurations. -/

/-- Switching wins iff the initial pick was not the car. -/
def switchWins (car pick : Nat) : Bool := car != pick

theorem monty_switch :
    switchWins 0 0 = false ∧
    switchWins 1 0 = true ∧
    switchWins 2 0 = true := by
  decide

/-- Two of the three configurations win by switching. -/
theorem monty_two_of_three :
    (switchWins 0 0).toNat + (switchWins 1 0).toNat +
      (switchWins 2 0).toNat = 2 := by
  decide

end Fold
