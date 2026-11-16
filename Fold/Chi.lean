/-
  Fold/Chi.lean

  Capping, uncapping, puncturing, filling — on the `χ` ledger and on the
  space.

  The ledger is exact: a cap raises `χ` by one, a puncture lowers it by
  one, and on `χ` alone the two cancel.  The space remembers more: a cap
  consumes a boundary component, a puncture creates a puncture, and
  `puncture ∘ cap` is not the identity on spaces.  That is the precise
  content of "cap and puncture are not inverses".  They are inverse on
  the ledger, not on the space.  What is inverse to capping is
  uncapping; what is inverse to puncturing is filling.

  The false friend is the step from "the ledger cancels" to "the spaces
  are the same".
-/
import Init

namespace Fold

/-- A surface summary: Euler characteristic, boundary components,
punctures.  This is not a topological space; it is the triple of
invariants the argument uses. -/
structure Surface where
  chi : Int
  boundary : Nat
  punctures : Nat
deriving Repr, DecidableEq

/-- Glue a disk to a boundary circle: `χ` rises by one and one boundary
component is consumed. -/
def cap (S : Surface) : Surface :=
  { chi := S.chi + 1, boundary := S.boundary - 1, punctures := S.punctures }

/-- Remove an open disk: `χ` falls by one and a boundary component is
created. -/
def uncap (S : Surface) : Surface :=
  { chi := S.chi - 1, boundary := S.boundary + 1, punctures := S.punctures }

/-- Remove a point: `χ` falls by one and a puncture is created. -/
def puncture (S : Surface) : Surface :=
  { chi := S.chi - 1, boundary := S.boundary, punctures := S.punctures + 1 }

/-- Fill a puncture: `χ` rises by one and a puncture is consumed. -/
def fill (S : Surface) : Surface :=
  { chi := S.chi + 1, boundary := S.boundary, punctures := S.punctures - 1 }

/-- Capping and uncapping are inverse when there is a boundary component
to cap. -/
theorem uncap_cap (S : Surface) (hb : 0 < S.boundary) : uncap (cap S) = S := by
  cases S with
  | mk chi b p =>
    simp [cap, uncap, Nat.sub_add_cancel hb]

/-- Puncturing and filling are inverse. -/
theorem fill_puncture (S : Surface) : fill (puncture S) = S := by
  cases S with
  | mk chi b p =>
    simp [puncture, fill]

/-- On the `χ` ledger, capping and puncturing cancel. -/
theorem chi_puncture_cap (S : Surface) : (puncture (cap S)).chi = S.chi := by
  simp [puncture, cap]

/-- On the space, `puncture ∘ cap` is not the identity: it leaves a
puncture behind. -/
theorem puncture_cap_ne (S : Surface) (_hb : 0 < S.boundary) :
    puncture (cap S) ≠ S := by
  intro h
  have hp : (puncture (cap S)).punctures = S.punctures := by rw [h]
  simp [puncture, cap] at hp

/-- On the space, `cap ∘ puncture` is not the identity: it consumes a
boundary component that the puncture did not create. -/
theorem cap_puncture_ne (S : Surface) (hb : 0 < S.boundary) :
    cap (puncture S) ≠ S := by
  intro h
  have hb' : (cap (puncture S)).boundary = S.boundary := by rw [h]
  simp [cap, puncture] at hb'
  omega

/-- The exact summary. -/
theorem cap_puncture_structure :
    (∀ S : Surface, 0 < S.boundary → uncap (cap S) = S) ∧
    (∀ S : Surface, fill (puncture S) = S) ∧
    (∀ S : Surface, (puncture (cap S)).chi = S.chi) ∧
    (∀ S : Surface, 0 < S.boundary → puncture (cap S) ≠ S) ∧
    (∀ S : Surface, 0 < S.boundary → cap (puncture S) ≠ S) :=
  ⟨uncap_cap, fill_puncture, chi_puncture_cap, puncture_cap_ne, cap_puncture_ne⟩

end Fold
