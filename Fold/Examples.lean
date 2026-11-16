/-
  Fold/Examples.lean

  Two finite checks on the exact core.

  The first is a non-vacuous instance of `desc_bijective`: the
  involution on `Option Bool` that fixes `none` and swaps the two
  `some` values.  Its quotient has two points, so the descent is a
  bijection onto `Bool`, not onto a singleton.

  The second is the Euler characteristic of the `m = 2` dessin:
  two vertices, two edges, two faces, `V + F - E = 2`.
-/
import Fold.Basic

namespace Fold

/-! ### A non-vacuous descent -/

/-- The involution on `Option Bool` that fixes `none` and swaps the two
`some` values.  This is the smallest non-free involution: one fixed
point and one two-point orbit. -/
def swapFold : Fold (Option Bool) where
  f
    | none => none
    | some b => some (!b)
  invol := by
    intro x
    cases x with
    | none => rfl
    | some b => cases b <;> rfl

/-- The invariant: `none` is the fixed orbit, the two `some` values are
the other orbit. -/
def swapInv : Option Bool → Bool
  | none => false
  | some _ => true

/-- `swapInv` is constant on the orbits of `swapFold`. -/
theorem swapInv_fold (x : Option Bool) : swapInv (swapFold.f x) = swapInv x := by
  cases x with
  | none => rfl
  | some b => rfl

/-- `swapInv` separates the orbits: equal values force the same orbit. -/
theorem swapInv_sep (x y : Option Bool) (h : swapInv x = swapInv y) :
    Orbit swapFold x y := by
  revert h
  cases x with
  | none =>
    cases y with
    | none =>
      intro _
      exact Or.inl rfl
    | some b =>
      intro h
      cases h
  | some a =>
    cases y with
    | none =>
      intro h
      cases h
    | some b =>
      intro _
      cases a <;> cases b
      · exact Or.inl rfl
      · exact Or.inr rfl
      · exact Or.inr rfl
      · exact Or.inl rfl

/-- `swapInv` is surjective. -/
theorem swapInv_surj (y : Bool) : ∃ x : Option Bool, swapInv x = y := by
  cases y
  · exact ⟨none, rfl⟩
  · exact ⟨some true, rfl⟩

/-- The descent of `swapInv` is a bijection onto `Bool`: the quotient of
`swapFold`, which has two orbits, is `Bool`. -/
theorem swapFold_desc_bijective :
    Function.Injective (desc swapFold swapInv swapInv_fold) ∧
    Function.Surjective (desc swapFold swapInv swapInv_fold) :=
  desc_bijective swapFold swapInv swapInv_fold swapInv_sep swapInv_surj

/-! ### The `m = 2` dessin -/

/-- A spherical dessin: `V` vertices, `E` edges, `F` faces, with the
Euler relation. -/
structure Dessin where
  V : Nat
  E : Nat
  F : Nat
  sphere : V + F = E + 2

namespace Dessin

/-- Euler characteristic of a spherical dessin, stated without
truncating subtraction: `V + F - E`. -/
def euler (d : Dessin) : Nat := d.V + d.F - d.E

/-- The Euler characteristic of a spherical dessin is `2`. -/
theorem euler_eq_two (d : Dessin) : d.euler = 2 := by
  unfold euler
  rw [d.sphere]
  exact Nat.add_sub_cancel_left d.E 2

end Dessin

/-- The `m = 2` dessin: the unit circle with the two marks `±1`.  The
two semicircles are the edges; the inside and outside are the faces. -/
def dessin2 : Dessin where
  V := 2
  E := 2
  F := 2
  sphere := rfl

/-- The `m = 2` dessin has Euler characteristic `2`. -/
theorem dessin2_euler : dessin2.euler = 2 := Dessin.euler_eq_two dessin2

end Fold
