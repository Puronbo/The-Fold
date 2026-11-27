/-
  Fold/Scale.lean

  The scale action `g_k(x) = k x` on `ℤ`, and its exact bookkeeping:
  the datum `0` is fixed by every `k`; for `k ≠ 1` it is the only fixed
  point; a nonzero point is moved by every non-identity scale; `k = 0`
  collapses everything to the datum.

  The integral model is deliberate.  It makes `0` the unique fixed
  point and makes the collapse exact.  The reciprocal `k ↦ 1/k` needs a
  field (`ℚ` or `ℝ`); it is the completion `0 ~ ∞` and is not part of
  this integral slice.
-/
import Fold.Basic

namespace Fold

/-- The scale action: `g_k(x) = k x`. -/
def scale (k : Int) (x : Int) : Int := k * x

/-- The identity scale is the identity map. -/
theorem scale_one : scale 1 = id := by
  funext x
  exact Int.one_mul x

/-- Scales compose by multiplying the factors. -/
theorem scale_comp (k l : Int) : scale (k * l) = scale k ∘ scale l := by
  funext x
  exact Int.mul_assoc k l x

/-- Every scale fixes the datum `0`. -/
theorem datum_fixed (k : Int) : scale k 0 = 0 := Int.mul_zero k

/-- The zero scale collapses the line to the datum. -/
theorem scale_collapse : scale 0 = fun _ => 0 := by
  funext x
  exact Int.zero_mul x

/-- For `k ≠ 1`, the datum is the only fixed point.  This is the exact
content of "the scale fixes one point and moves every other". -/
theorem scale_fix_iff (k : Int) (hk : k ≠ 1) (x : Int) :
    scale k x = x ↔ x = 0 := by
  constructor
  · intro h
    have h' : (k - 1) * x = 0 := by
      unfold scale at h
      rw [Int.sub_mul, Int.one_mul]
      omega
    rcases Int.mul_eq_zero.mp h' with hk0 | hx0
    · have hk1 : k = 1 := by omega
      exact absurd hk1 hk
    · exact hx0
  · intro h
    subst h
    exact datum_fixed k

/-- A nonzero point is moved by every non-identity scale. -/
theorem scale_moves (k : Int) (hk : k ≠ 1) (x : Int) (hx : x ≠ 0) :
    scale k x ≠ x := by
  intro h
  exact hx ((scale_fix_iff k hk x).1 h)

/-- A positive scale preserves the positive ray. -/
theorem scale_pos (k x : Int) (hk : 0 < k) (hx : 0 < x) : 0 < scale k x :=
  Int.mul_pos hk hx

/-- The reflection `x ↦ −x` is a fold on `ℤ`. -/
def negFold : Fold Int where
  f := fun x => -x
  invol := by
    intro x
    exact Int.neg_neg x

/-- The reflection fixes `0` and pairs each nonzero point with its
negative. -/
theorem negFold_fix (x : Int) : Fix negFold x ↔ x = 0 := by
  constructor
  · intro h
    have h' : -x = x := h
    omega
  · intro h
    subst h
    rfl

end Fold


/-- Affine scaling about an arbitrary datum: g_k(p) = p₀ + k(p - p₀). -/
def affineScale (k p0 p : Int) : Int := p0 + k * (p - p0)

/-- Unit scale leaves every point unchanged. -/
theorem affineScale_one (p0 p : Int) : affineScale 1 p0 p = p := by
  simp [affineScale]

/-- Zero scale collapses every point to the chosen datum. -/
theorem affineScale_zero (p0 p : Int) : affineScale 0 p0 p = p0 := by
  simp [affineScale]

/-- Scale minus one is point reflection through the datum. -/
theorem affineScale_neg_one (p0 p : Int) :
    affineScale (-1) p0 p = 2 * p0 - p := by
  simp [affineScale]
  ring

/-- Scales about the same datum compose by multiplying their parameters. -/
theorem affineScale_comp (k l p0 p : Int) :
    affineScale k p0 (affineScale l p0 p) =
      affineScale (k * l) p0 p := by
  simp [affineScale]
  ring

/-- Point reflection through p₀ is an involution. -/
def pointReflect (p0 p : Int) : Int := 2 * p0 - p

theorem pointReflect_invol (p0 p : Int) :
    pointReflect p0 (pointReflect p0 p) = p := by
  simp [pointReflect]
  ring
