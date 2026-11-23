# G-EP16 — synthetic transformer-shaped end-to-end experiment

## Purpose

G-EP16 supplies a deterministic, dependency-free fixture that exercises the G-EP13 adapter, G-EP14 snapshot comparison, and G-EP15 checkpoint scanner together. It removes the need for a user-provided checkpoint when checking the software pipeline itself.

The fixture has four square attention projections (Q/K/V/O), rectangular MLP up/down projections, a normalization vector, and a bias vector. It creates three snapshots: a reference, a small scalar perturbation, and a deliberately rank-deficient Q projection. The test suite verifies that the scanner includes the six 2-D weights, skips the vector and bias, applies square spectra only to square matrices, and detects the designed rank change.

## Run

```bash
python -m tools.transformer_demo
python -m tools.transformer_demo --primes 5,7,11 --scales 1,10,100 --output demo-report.json
python -m unittest tests.test_transformer_demo -v
```

The JSON labels the output `synthetic_fixture_not_trained_model` and records the limitations. The fixture is intentionally hand-constructed and deterministic; it is not a trained neural network, does not run a forward pass, and says nothing about prediction quality or learned representations.

## What this validates

- The checkpoint scanner can process a transformer-like mixture of square and rectangular weight tensors.
- Square attention projections receive finite-field spectral/Jordan fingerprints; rectangular MLP projections receive rank-only diagnostics.
- Non-weight vectors and biases are skipped with reasons.
- The snapshot audit detects a controlled rank drop and reports exact signature equality for each prime/scale pair.

## What it does not validate

This is software plumbing, not empirical evidence for the eigenprime framework as a useful neural-network diagnostic. The conversion `round(scale * weight) mod p` is lossy; the chosen prime and scale can change the result. Equal fingerprints do not imply equal functions, activations, outputs, or model quality. A real evaluation still requires actual trained checkpoints and comparison with conventional diagnostics and task metrics.
