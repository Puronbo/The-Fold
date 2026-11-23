# G-EP15 — inspecting real transformer checkpoints

## Scope

G-EP15 adds `tools/transformer_checkpoint.py`, a checkpoint inspection path that reuses the G-EP13 adapter and G-EP14 finite-field methodology. It discovers named two-dimensional weight tensors in a state-dictionary-like mapping and reports modular ranks across caller-selected primes and quantization scales. Optional full spectral/Jordan analysis is limited to square matrices below a caller-selected dimension threshold.

## Loading and safety

The analysis function `inspect_state_dict` has no PyTorch dependency and accepts an already-loaded mapping. The command-line loader imports PyTorch only when invoked and calls `torch.load(..., map_location="cpu", weights_only=True)`. It deliberately does not fall back to unrestricted pickle deserialization for older PyTorch versions or untrusted checkpoint files. The input should be a trusted weights-only checkpoint in a format supported by the installed PyTorch release.

The loader recognizes a raw state dictionary or common `state_dict`, `model_state_dict`, and `model` wrappers. It does not instantiate arbitrary model classes, download model weights, execute model code, or alter checkpoint contents.

## Resource controls

By default, matrices larger than 250,000 entries are skipped. Full spectral analysis is opt-in and limited to square matrices of dimension at most 32 by default. These conservative bounds matter because characteristic factorization and Jordan analysis are substantially more expensive than modular rank. Skipped layers are listed with reasons rather than silently omitted.

## Example

```bash
python -m tools.transformer_checkpoint model.pt \\
  --primes 101,103 --scales 100,1000 \\
  --output report.json
```

To add square spectral profiles for small square matrices:

```bash
python -m tools.transformer_checkpoint model.pt \\
  --primes 101 --scales 1000 \\
  --include-square-spectra --spectral-max-dimension 24 \\
  --output spectral-report.json
```

Programmatic use after loading a state mapping:

```python
from tools.transformer_checkpoint import inspect_state_dict
report = inspect_state_dict(state_dict, primes=[101, 103], scales=[100, 1000])
```

## Interpretation and limits

The report records layer names, shapes, primes, scales, quantization policy, ranks, and optional spectral fingerprints. Each value describes a matrix produced by `round(scale * weight) mod p`; it is not an invariant of the original real-valued layer. A rank change can be caused by modular reduction even when the real-valued matrix has full rank. A matching finite-field signature does not establish equal network functions, equal predictions, or equal model quality.

This milestone supplies a reproducible route to examine an actual checkpoint. It does not claim that any particular model has been tested: that requires the user to supply a checkpoint and inspect its output. A future empirical study should compare multiple training checkpoints, primes, and scales with conventional diagnostics and validation metrics.
