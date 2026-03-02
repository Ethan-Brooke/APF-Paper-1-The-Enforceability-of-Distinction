# Admissibility Physics Framework — Paper 1

**The Structural Skeleton of Quantum Mechanics from Finite Enforcement Capacity**

<p align="center">
  <a href="https://[your-username].github.io/apf-paper1/">🔬 Interactive Derivation DAG</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#the-23-theorems">Theorem Index</a> ·
  <a href="#citation">Citation</a>
</p>

---

## The argument in one paragraph

Physical distinctions require enforcement. Enforcement costs resources. Those resources are finite. From this single axiom — **finite enforcement capacity** — the mathematical structure of quantum mechanics emerges as the unique admissible physics. Hilbert spaces, the Born rule, CPTP dynamics, tensor products, gauge symmetry, and entropy are all *derived consequences*, not assumptions. This repository is the executable proof.

## Interactive visualization

👉 **[Launch the Derivation DAG](https://[your-username].github.io/apf-paper1/)**

The visualization is a complete interactive map of the 23-theorem derivation chain:

- **Explore the graph.** Every node is a theorem. Every edge is a logical dependency. Nodes are arranged by derivation tier: Axiom A1 at top, structural lemmas in the middle, the quantum skeleton at the bottom.
- **Hover any node** to see its full name, key mathematical result, plain-English explanation, the shortest derivation chain back to A1, and the number of distinct paths connecting it to the axiom. Multiple paths mean the result is over-determined — it would survive even if one chain were weakened.
- **Click a node** for the deep-dive panel: direct dependencies (clickable), chain visualization, path/ancestor/depth statistics, and cross-links to walk the entire DAG.
- **Run the verification.** Hit `▶ Run Checks` and watch the 23 theorems verify in topological order, each node flashing green as it passes. The terminal panel logs results in real time. This mirrors exactly what `python run_checks.py` does on your machine.

The visualization is served via GitHub Pages from the `docs/` directory. No build step, no dependencies — it's a single self-contained HTML file.

## Quick start

```bash
git clone https://github.com/[your-username]/apf-paper1.git
cd apf-paper1
python run_checks.py
```

No dependencies. No `pip install`. Python 3.9+ and the standard library — that's it.

You should see:

```
  APF Paper 1 — Structural Skeleton (SPINE)
  ==================================================
  23 theorems from A1 (finite enforcement capacity)

  [AXIOM] PASS  A1
         Finite enforcement capacity exists (C > 0, C < infinity)
  [P] PASS  M
         Multiple distinguishable subsystems exist
  [P] PASS  NT
         Subsystems are not all identical
  [P] PASS  L_epsilon*
         eps_Gamma > 0: meaningful distinctions have minimum enforcement cost
  ...
  [P] PASS  T_tensor
         Tensor product forced by compositional closure

  ============================================================
  Paper 1 (SPINE): 23 passed, 0 failed, 0 errors — 23 theorems
  ============================================================
```

## The derivation chain

Paper 1 establishes the root and first two tiers of the APF derivation DAG:

```
                              A1
                    (finite enforcement capacity)
                            │
                     ┌──────┴──────┐
                     M             NT
                (multiplicity)  (non-triviality)
                     │              │
          ┌──────────┼──────────────┼──────────┐
         L_ε*       L_loc         L_nc        L_irr
       (min cost)  (locality)  (non-closure) (irreversibility)
          │          │            │             │
          └──────────┴─────┬──────┴─────────────┘
                           │
     ┌────┬────┬────┬──────┼──────┬──────┬──────┬────┐
    T1   T2   T3  T_Born T_CPTP T_Herm T_M  T_can  ...
         │                                    │
     (Hilbert)                          (canonical object)
```

The critical path: **A1 → L_ε\* → L_loc → L_nc → T1 → T2 → T3**

Every downstream theorem traces back to A1 through this chain. Many theorems have *multiple* paths to A1 — this is structural redundancy, not disorder. The interactive visualization shows exact path counts for every node.

## The 23 theorems

| # | Theorem | Full Name | Key Result | Tier |
|---|---------|-----------|------------|------|
| 1 | **A1** | Finite Enforcement Capacity | C > 0, C < ∞ | Axiom |
| 2 | **M** | Multiplicity | \|D\| ≥ 2 | Sub-clause |
| 3 | **NT** | Non-Triviality | ε(d₁) ≠ ε(d₂) | Sub-clause |
| 4 | **L_ε\*** | Minimum Cost | ε\* > 0 | Tier 0 |
| 5 | **L_nc** | Non-Closure | State space ≠ simplex | Tier 0 |
| 6 | **L_loc** | Locality | E(S₁∪S₂) = E(S₁) + E(S₂) | Tier 0 |
| 7 | **L_irr** | Irreversibility | ∃ irreversible processes | Tier 0 |
| 8 | **L_T2** | Finite GNS | dim(H) = 4 witness | Tier 1 |
| 9 | **L_cost** | Cost Uniqueness | C(G) = dim(G)·ε forced | Tier 1 |
| 10 | **T0** | Axiom Witnesses | Δ = 4, [A,B] ≠ 0 | Tier 1 |
| 11 | **T1** | Incompatible Observables | ∃ incompatible A, B | Tier 1 |
| 12 | **T2** | Hilbert Space | H = Hilbert space | Tier 1 |
| 13 | **T3** | Gauge Bundle | P → M, ∇ connection | Tier 1 |
| 14 | **T_Born** | Born Rule | p = \|⟨ψ\|φ⟩\|² | Tier 1 |
| 15 | **T_CPTP** | CPTP Dynamics | Φ: CPTP maps | Tier 1 |
| 16 | **T_Hermitian** | Hermitian Observables | O = O† | Tier 1 |
| 17 | **T_M** | Interface Monogamy | Disjoint ⇒ independent | Tier 1 |
| 18 | **T_canonical** | Canonical Object | Sheaf + Ω_inter | Tier 1 |
| 19 | **T_entropy** | Entropy | S = −Tr(ρ ln ρ) | Tier 1 |
| 20 | **T_ε** | Min Cost Parameter | ε = min cost > 0 | Tier 1 |
| 21 | **T_κ** | Binary Multiplier | κ = 2 | Tier 1 |
| 22 | **T_η** | Correlation Bound | η/ε ≤ 1 | Tier 1 |
| 23 | **T_⊗** | Tensor Products | H_AB = H_A ⊗ H_B | Tier 1 |

Every theorem tagged **[P]** is proved from A1. The only input is A1 itself (**[AXIOM]**).

## Repository structure

```
apf-paper1/
├── README.md             ← you are here
├── LICENSE               ← MIT
├── pyproject.toml        ← package metadata (zero dependencies)
├── run_checks.py         ← convenience script
├── .gitignore
├── apf/
│   ├── __init__.py       ← package marker + version
│   ├── apf_utils.py      ← shared math utilities (stdlib only)
│   ├── core.py           ← the 23 theorem check functions
│   └── bank.py           ← registry + runner
└── docs/
    └── index.html        ← interactive derivation DAG (GitHub Pages)
```

## Usage

### Command line

```bash
# Run all 23 checks
python run_checks.py

# Run a single theorem
python run_checks.py T2

# List all theorem names
python run_checks.py --list

# Show dependency chain for a theorem
python run_checks.py --deps T3
```

### Python API

```python
from apf.bank import run_all, get_check

# Run everything
results = run_all()

# Inspect a single theorem
r = get_check('T_Born')()
print(r['key_result'])
# → "Born rule is unique admissibility-invariant probability (Gleason, d>=3)"
print(r['dependencies'])
# → ['T2', 'T_Hermitian', 'A1', 'L_Gleason_finite']
```

### GitHub Pages setup

The interactive visualization at `docs/index.html` is ready for GitHub Pages:

1. Go to your repo's **Settings → Pages**
2. Under **Source**, select **Deploy from a branch**
3. Set **Branch** to `main` and **Folder** to `/docs`
4. Save — your visualization will be live at `https://[your-username].github.io/apf-paper1/`

No build step. No CI. It's a single self-contained HTML file with zero dependencies.

## What this does and does not cover

**Derived in Paper 1:** The structural skeleton of quantum mechanics — Hilbert spaces, Born rule, Hermitian observables, CPTP dynamics, tensor products, gauge symmetry skeleton, entropy, and the canonical enforcement object. All from A1.

**Deferred to later papers:** Specific gauge groups (SU(3) × SU(2) × U(1)), particle content (61 types, 3 generations), mass hierarchies, mixing matrices, CP violation, spacetime dimension (d = 4), cosmological parameters, and the 47 zero-parameter quantitative predictions. The full APF codebase (312 theorems across 16+ modules) will be released as the paper series is published.

## Epistemic tags

Each theorem result includes an `epistemic` field:

- **`AXIOM`** — The single input (A1 only)
- **`P`** — Proved from A1 (all 22 non-axiom theorems in this release)

Later papers introduce additional tags for conjectures (`C`), red-team adversarial tests (`RED_TEAM`), and results with external mathematical dependencies.

## Design principles

- **Zero external dependencies.** Python stdlib only. No NumPy, no SciPy, no frameworks. Every matrix operation is hand-implemented in `apf_utils.py` using exact arithmetic (`fractions.Fraction`) where possible.
- **Code is the specification.** The paper is a guide to reading the code. If the paper and the code disagree, the code is authoritative.
- **Machine-verifiable.** Every theorem is a function that returns pass/fail. No trust required — run it yourself.
- **Multiple derivation paths.** Many theorems depend on A1 both directly and through intermediate lemmas. This structural redundancy means results are over-determined — they would survive even if individual derivation steps were weakened.

## What comes next

This is Paper 1 of a 7-paper series. Each subsequent paper adds modules to the codebase and extends the derivation DAG:

| Paper | Title | Modules | New theorems |
|-------|-------|---------|-------------|
| **1** | **SPINE** (this repo) | `core.py` | **23** |
| 2 | STRUCTURE | `core.py` (extended) | ~10 |
| 3 | IRREVERSIBILITY | `supplements.py` | ~15 |
| 4 | CONSTRAINTS | `gauge.py`, `generations.py` | ~70 |
| 5 | QUANTUM | `majorana.py`, `supplements.py` | ~20 |
| 6 | DYNAMICS & GEOMETRY | `spacetime.py`, `gravity.py`, `cosmology.py` | ~40 |
| 7 | ACTION | `internalization.py`, `extensions.py` | ~30 |

By Paper 7, the DAG grows from 23 theorems to 312, and the framework makes 47 zero-parameter quantitative predictions — all from the same single axiom.

## Citation

If you use this code in academic work, please cite Paper 1:

```bibtex
@article{apf-paper1,
  title   = {The Structural Skeleton of Quantum Mechanics from Finite Enforcement Capacity},
  author  = {[Author]},
  year    = {2025},
  note    = {Code: https://github.com/[your-username]/apf-paper1}
}
```

## License

MIT. See [LICENSE](LICENSE).
