/-
  Fold/Geometry.lean

  A concrete geometric fold: reflection of the integer plane across the
  horizontal axis. The fixed set is exactly the axis, and orthogonal
  projection onto that axis is a cut in the abstract Fold sense.
-/
import Fold.Basic

namespace Fold

/-- Reflection across the horizontal axis: (x,y) ↦ (x,-y). -/
def horizontalReflection : Fold (Int × Int) where
  f := fun p => (p.1, -p.2)
  invol := by
    intro p
    cases p with
    | mk x y =>
      simp

/-- The crease of horizontal reflection is precisely the x-axis. -/
theorem horizontalReflection_fix_iff (p : Int × Int) :
    Fix horizontalReflection p ↔ p.2 = 0 := by
  change (p.1, -p.2) = p ↔ p.2 = 0
  constructor
  · intro h
    have hs := congrArg Prod.snd h
    omega
  · intro h
    cases p with
    | mk x y =>
      simp at h
      subst y
      rfl

/-- The fixed set is the horizontal axis, represented by y = 0. -/
def horizontalCrease (p : Int × Int) : Prop :=
  p.2 = 0

theorem horizontalCrease_eq_fix (p : Int × Int) :
    horizontalCrease p ↔ Fix horizontalReflection p :=
  (horizontalReflection_fix_iff p).symm

/-- Orthogonal projection to the horizontal axis. -/
def horizontalProjection (p : Int × Int) : Int × Int := (p.1, 0)

/-- Projection lands on the crease. -/
theorem horizontalProjection_fix (p : Int × Int) :
    Fix horizontalReflection (horizontalProjection p) := by
  change (p.1, -(0 : Int)) = (p.1, 0)
  simp

/-- The geometric projection is a valid abstract cut for this fold. -/
def horizontalCut : Cut horizontalReflection where
  p := horizontalProjection
  image_fix := horizontalProjection_fix
  fix_eq := by
    intro p hp
    rcases p with ⟨x, y⟩
    have hy : y = 0 := (horizontalReflection_fix_iff (x, y)).mp hp
    simp [horizontalProjection, hy]
  orbit_eq := by
    intro p
    rcases p with ⟨x, y⟩
    rfl

/-- Projection onto the crease is idempotent. -/
theorem horizontalProjection_idempotent (p : Int × Int) :
    horizontalProjection (horizontalProjection p) = horizontalProjection p := by
  rfl

/-- Reflection leaves the orbit quotient unchanged. -/
theorem horizontalChart_reflection (p : Int × Int) :
    chart horizontalReflection (horizontalReflection.f p) =
      chart horizontalReflection p :=
  chart_fold horizontalReflection p

end Fold
