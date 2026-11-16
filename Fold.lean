/-
  Fold.lean

  The root module.  Build with `lake build`; the target is
  dependency-free and imports only `Init`.
-/
import Fold.Basic
import Fold.Scale
import Fold.Chi
import Fold.Arithmetic
import Fold.Wheel
import Fold.Problems
import Fold.Pressure
import Fold.Examples

/-
  Inventory.  `#check` is a compile-time audit: if a name changes or a
  statement stops elaborating, the build fails here.
-/

#check Fold.fix_iff
#check Fold.orbit_equivalence
#check Fold.chart_eq_iff
#check Fold.chart_fold
#check Fold.desc
#check Fold.desc_chart
#check Fold.desc_injective
#check Fold.desc_bijective
#check Fold.Cut.fix_iff
#check Fold.Cut.lift_chart
#check Fold.Cut.lift_fix

#check Fold.datum_fixed
#check Fold.scale_fix_iff
#check Fold.scale_moves
#check Fold.scale_collapse

#check Fold.uncap_cap
#check Fold.fill_puncture
#check Fold.chi_puncture_cap
#check Fold.puncture_cap_ne
#check Fold.cap_puncture_ne

#check Fold.formats_mod_99
#check Fold.gregorian_cycle
#check Fold.unix_weeks

#check Fold.rot_period
#check Fold.rot_closed

#check Fold.simpson_reversal
#check Fold.tolerance_not_trans
#check Fold.contraposition
#check Fold.monty_two_of_three

#check Fold.swapFold
#check Fold.swapFold_desc_bijective
#check Fold.Dessin.euler_eq_two
#check Fold.dessin2_euler

#check Fold.dessinSigma0_invol
#check Fold.dessinSigma0_ne_id
#check Fold.dessinSigma_product
#check Fold.dessinMonodromy_transitive
#check Fold.dessin_passport
#check Fold.dessinMonodromy_group

#check Fold.pressure_strict
#check Fold.pressure_unbounded
#check Fold.pressure_finite
#check Fold.pressure_gauge
