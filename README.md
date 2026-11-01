# Grid Topology Alpha / Janus-Engine

Production-grade implementation of a harmonic envelope auditor and dual-frequency nonce bias detector for elliptic curve cryptography (`secp256k1`).

## Overview
This repository simulates an entropy-failure scenario in low-cost IoT devices where nonces ($k$) are corrupted by hardware thermal shifts or linear counters. The `Janus-Engine` utilizes a harmonic modular matrix approach and dual-frequency baseline matching (`85` / `170`) to detect structured nonces and recover private keys deterministically via linear congruence collapse.

## Features
- **Harmonic Envelope Filtering:** Analyzes low-byte control traces of ECDSA signatures.
- **Dual-Frequency Calibration:** Cross-references bit patterns with symmetrical base states.
- **Deterministic Key Extraction:** Resolves private parameters without brute-force computation when entropy collapse occurs.

## Usage
Run the simulation:
```bash
python main.py