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

/-- Reflection across the translated horizontal line y = c. -/
def horizontalReflectionAt (c : Int) : Fold (Int × Int) where
  f := fun p => (p.1, 2 * c - p.2)
  invol := by
    intro p
    rcases p with ⟨x, y⟩
    simp
    omega

/-- The crease of the translated reflection is exactly y = c. -/
theorem horizontalReflectionAt_fix_iff (c : Int) (p : Int × Int) :
    Fix (horizontalReflectionAt c) p ↔ p.2 = c := by
  change (p.1, 2 * c - p.2) = p ↔ p.2 = c
  constructor
  · intro h
    have hs := congrArg Prod.snd h
    omega
  · intro h
    rcases p with ⟨x, y⟩
    simp at h
    subst y
    simp
    omega

/-- Projection onto the translated crease y = c. -/
def horizontalProjectionAt (c : Int) (p : Int × Int) : Int × Int :=
  (p.1, c)

/-- Projection lands on the translated crease. -/
theorem horizontalProjectionAt_fix (c : Int) (p : Int × Int) :
    Fix (horizontalReflectionAt c) (horizontalProjectionAt c p) := by
  apply (horizontalReflectionAt_fix_iff c _).2
  rfl

/-- Projection onto y = c is a cut for reflection across y = c. -/
def horizontalCutAt (c : Int) : Cut (horizontalReflectionAt c) where
  p := horizontalProjectionAt c
  image_fix := horizontalProjectionAt_fix c
  fix_eq := by
    intro p hp
    rcases p with ⟨x, y⟩
    have hy : y = c := (horizontalReflectionAt_fix_iff c (x, y)).mp hp
    simp [horizontalProjectionAt, hy]
  orbit_eq := by
    intro p
    rcases p with ⟨x, y⟩
    simp [horizontalProjectionAt, horizontalReflectionAt]

/-- The translated projection is idempotent. -/
theorem horizontalProjectionAt_idempotent (c : Int) (p : Int × Int) :
    horizontalProjectionAt c (horizontalProjectionAt c p) =
      horizontalProjectionAt c p := by
  rfl


/-- Reflection across the translated vertical line x = c. -/
def verticalReflectionAt (c : Int) : Fold (Int × Int) where
  f := fun p => (2 * c - p.1, p.2)
  invol := by
    intro p
    rcases p with ⟨x, y⟩
    simp
    omega

/-- The crease of vertical reflection is exactly x = c. -/
theorem verticalReflectionAt_fix_iff (c : Int) (p : Int × Int) :
    Fix (verticalReflectionAt c) p ↔ p.1 = c := by
  change (2 * c - p.1, p.2) = p ↔ p.1 = c
  constructor
  · intro h
    have hs := congrArg Prod.fst h
    omega
  · intro h
    rcases p with ⟨x, y⟩
    simp at h
    subst x
    change (2 * c - c, y) = (c, y)
    congr 1
    omega

/-- Projection onto the translated vertical crease x = c. -/
def verticalProjectionAt (c : Int) (p : Int × Int) : Int × Int :=
  (c, p.2)

theorem verticalProjectionAt_fix (c : Int) (p : Int × Int) :
    Fix (verticalReflectionAt c) (verticalProjectionAt c p) := by
  apply (verticalReflectionAt_fix_iff c _).2
  rfl

/-- Every translated vertical crease has its own observer cut. -/
def verticalCutAt (c : Int) : Cut (verticalReflectionAt c) where
  p := verticalProjectionAt c
  image_fix := verticalProjectionAt_fix c
  fix_eq := by
    intro p hp
    rcases p with ⟨x, y⟩
    have hx : x = c := (verticalReflectionAt_fix_iff c (x, y)).mp hp
    simp [verticalProjectionAt, hx]
  orbit_eq := by
    intro p
    rcases p with ⟨x, y⟩
    simp [verticalProjectionAt, verticalReflectionAt]

theorem verticalProjectionAt_idempotent (c : Int) (p : Int × Int) :
    verticalProjectionAt c (verticalProjectionAt c p) =
      verticalProjectionAt c p := by
  rfl


/-- Coordinate exchange sends the horizontal crease to the vertical crease. -/
def swapCoordinates (p : Int × Int) : Int × Int := (p.2, p.1)

theorem swapCoordinates_invol (p : Int × Int) :
    swapCoordinates (swapCoordinates p) = p := by
  rcases p with ⟨x, y⟩
  rfl

/-- Horizontal reflection conjugates to vertical reflection under coordinate exchange. -/
theorem swap_horizontal_to_vertical (c : Int) (p : Int × Int) :
    verticalReflectionAt c (swapCoordinates p) =
      swapCoordinates (horizontalReflectionAt c p) := by
  rfl

/-- Coordinate exchange also conjugates the corresponding crease projections. -/
theorem swap_horizontal_projection (c : Int) (p : Int × Int) :
    verticalProjectionAt c (swapCoordinates p) =
      swapCoordinates (horizontalProjectionAt c p) := by
  rfl

end Fold
