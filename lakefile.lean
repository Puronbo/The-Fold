import Lake
open Lake DSL

/-
  The Fold, formal core.

  This library is deliberately dependency-free: it imports only `Init`,
  so it builds with the bare Lean 4 toolchain and no Mathlib download.
  The exact statements live in `Fold/`; the prose map is
  `the-fold-lean.md`.
-/

package «fold» where
  leanOptions := #[
    ⟨`autoImplicit, false⟩
  ]

@[default_target]
lean_lib Fold where
  srcDir := "."
  globs := #[.andSubmodules `Fold]
