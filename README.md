# The Enforceability of Distinction

### Interactive Mathematical Appendix to Paper 1 of the Admissibility Physics Framework

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.18439200"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.18439200.svg" alt="DOI"></a>
  <a href="https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction/blob/main/APF_Reviewer_Walkthrough.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a>
</p>

<p align="center">
  <a href="https://ethan-brooke.github.io/APF-Paper-1-The-Enforceability-of-Distinction/">Interactive Derivation DAG</a> ·
  <a href="#theorem-mapping-table">Theorem Map</a> ·
  <a href="REVIEWERS_GUIDE.md">Reviewers' Guide</a> ·
  <a href="#citation">Citation</a>
</p>

---

## Why this codebase exists

Paper 1 derives the structural skeleton of quantum mechanics from a single axiom: enforcement capacity is finite and positive.  Twenty-three theorems are proved, each building on the last, from the axiom through four structural lemmas to Hilbert spaces, the Born rule, CPTP dynamics, tensor products, gauge symmetry, and entropy.

This repository is the executable proof.

Because A1 is a discrete, finite-capacity bound, the natural language of proof is **exact rational arithmetic**.  Every witness in this codebase uses Python's `Fraction` type — no floating-point approximation, no rounding, no numerical error.  When the code asserts that a composition of two admissible states overflows the capacity bound, the overflow is *exact*: the rational number $19\tfrac{1}{2}$ exceeds $10$, not $10.000001 > 9.999999$.  This is the most rigorous way to verify the absence of classical overflow without artifacts.

The codebase requires **Python 3.9+ and the standard library only** — no NumPy, no SciPy, no external dependencies of any kind.  This is a deliberate choice: the proofs should be inspectable and reproducible without installing anything, and they should run unchanged in twenty years.  Every matrix operation is implemented by hand in exact arithmetic.

Each theorem is a single function that constructs a mathematical witness and returns a structured result: the theorem's name, its logical dependencies, its epistemic status, and a summary of what was proved.  The entire codebase is a directed acyclic graph of such functions.  There is nothing else here.

## How to verify

Three paths, in order of increasing friction:

**1. Colab notebook — zero install, full transparency.** [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction/blob/main/APF_Reviewer_Walkthrough.ipynb) Every key theorem is derived inline with exact rational arithmetic you can inspect and modify. Run all cells — the full verification takes under 10 seconds.

**2. Browser — zero install.** Open the [Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-1-The-Enforceability-of-Distinction/). Explore the 23-theorem dependency graph. Hover any node for its mathematical statement, key result, shortest derivation chain to A1, and the number of distinct paths (structural redundancy). Click **Run Checks** to watch all 23 theorems verify in topological order.

**3. Local — no pip install.**
```bash
git clone https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction.git
cd APF-Paper-1-The-Enforceability-of-Distinction
python run_checks.py
```
Expected output:
```
  Paper 1 (SPINE): 23 passed, 0 failed, 0 errors — 23 theorems
```

**4. Individual inspection.**
```python
from apf.bank import get_check
r = get_check('T_Born')()
print(r['key_result'])
# → "Born rule is unique admissibility-invariant probability (Gleason, d>=3)"
```

For reviewers, a [dedicated guide](REVIEWERS_GUIDE.md) walks through the logical architecture, the structural assumptions, and the anticipated objections.

---

## Theorem mapping table

This table maps every result in the manuscript to its executable verification.  Column 4 describes the *mathematical content* of each check — what is constructed, what inequality is verified, what structure is exhibited.

| Theorem | Manuscript | Code | What is mathematically verified |
|---------|-----------|------|-------------------------------|
| **A1** (Finite Enforcement Capacity) | §2 | `check_A1()` | Consistency: any finite C > 0 satisfies the axiom; max distinctions ⌊C/ε⌋ is finite for all test values |
| **M** (Multiplicity) | §2.2 | `check_M()` | \|𝒟\| ≥ 2 is satisfiable; constructive witness with heterogeneous costs; countermodel shows \|𝒟\| = 1 produces no physics |
| **NT** (Non-Degeneracy) | §2.2 | `check_NT()` | ε(d₁) ≠ ε(d₂) is satisfiable; identical costs collapse structure to trivial |
| **L<sub>ε*</sub>** (Minimum Cost) | §4.1 | `check_L_epsilon_star()` | Contrapositive: if ε* = 0 then \|𝒟\| = ∞, contradicting C < ∞. Constructive: ε* > 0 as Fraction |
| **L<sub>loc</sub>** (Locality) | §4.2 | `check_L_loc()` | Overflow witness: 6 distinctions with ε = 2 cost 19½ at a single interface (> C = 10), but distribute admissibly at 8¼ each (≤ 10). Locality is forced, not assumed |
| **L<sub>nc</sub>** (Non-Closure) | §4.3 | `check_L_nc()` | Two individually admissible states whose composition exceeds C. State space ≠ simplex. Exact rational overflow |
| **L<sub>Δ</sub>** (Competition) | §4.4 | `check_L_irr()` (witness) | Superadditivity: Δ > 0 strictly. Combined perturbation cost exceeds sum of individual costs |
| **L<sub>irr</sub>** (Irreversibility) | §4.5 | `check_L_irr()` | Cross-interface correlations increase committed capacity; partial-trace witness shows local reversal is impossible |
| **T0** (Axiom Witnesses) | §5 | `check_T0()` | Concrete non-commuting operators: σ_x, σ_z with Δ = 4; [A,B] ≠ 0 verified |
| **T1** (Bridge Theorem) | §5.1 | `check_T1()` | Order-dependence: E_A ∘ E_B ≠ E_B ∘ E_A on the capacity functional; enforces OR0 (Faithfulness) |
| **L<sub>T2</sub>** (Finite GNS) | §5.2 | `check_L_T2_finite_gns()` | Constructive GNS on M₂(ℂ): inner product ⟨a,b⟩ = ω(a†b) with ω = Tr(·)/2, representation π(x)b = xb, dim(H) = 4 |
| **T2** (Hilbert Space) | §5.2 | `check_T2()` | Non-closure + T1 + OR1–OR3 + finite GNS ⟹ C*-algebra on Hilbert space; Wedderburn–Artin decomposition ⊕ M_nk(ℂ) |
| **T<sub>Born</sub>** (Born Rule) | §5.3 | `check_T_Born()` | Gleason's theorem: frame function on H (dim ≥ 3) ⟹ unique probability p = \|⟨ψ\|φ⟩\|²; verified for d = 3 |
| **T<sub>Hermitian</sub>** (Self-Adjoint Observables) | §5.4 | `check_T_Hermitian()` | Irreversibility + non-closure ⟹ O = O†; self-adjointness forced, not postulated |
| **T<sub>CPTP</sub>** (CPTP Dynamics) | §5.5 | `check_T_CPTP()` | Admissibility preservation ⟹ completely positive trace-preserving maps; Kraus form Φ(ρ) = Σ K_i ρ K_i† verified |
| **T<sub>⊗</sub>** (Tensor Products) | §5.6 | `check_T_tensor()` | Independent interfaces ⟹ H_AB = H_A ⊗ H_B; entanglement generic (S = 0.6931 for Bell-state witness) |
| **T3** (Gauge Bundle) | §5.7 | `check_T3()` | Locality + operator algebra ⟹ interface automorphisms form compact group; principal bundle P → M with connection ∇ |
| **T<sub>S</sub>** (Entropy) | §5.8 | `check_T_entropy()` | S(ρ) = −Tr(ρ ln ρ) equals committed enforcement capacity; verified against exact von Neumann entropy |
| **T<sub>M</sub>** (Monogamy) | §5.9 | `check_T_M()` | Finite capacity + locality ⟹ disjoint interfaces enforce independently; seed of entanglement monogamy |
| **T<sub>ε</sub>** (Min Cost Parameter) | §5.10 | `check_T_epsilon()` | ε = min cost > 0 as well-defined parameter of any admissible system |
| **T<sub>κ</sub>** (Binary Multiplier) | §5.10 | `check_T_kappa()` | Binary distinction costs exactly 2ε: κ = 2. Derivation from ε + L_irr |
| **T<sub>η</sub>** (Correlation Bound) | §5.10 | `check_T_eta()` | η/ε ≤ 1: correlations never cost more than the distinctions they correlate |
| **T<sub>can</sub>** (Canonical Object) | §6 | `check_T_canonical()` | Sheaf of finite sets + non-local cost functional Ω_inter; separatedness + gluing axioms verified |
| **L<sub>cost</sub>** (Cost Uniqueness) | §6 | `check_L_cost()` | C(G) = dim(G)·ε is the unique cost assignment compatible with A1 |

All check functions reside in `apf/core.py`.  Every function listed above can be called independently and returns a structured result including its logical dependencies, epistemic status, and the mathematical content it verifies.

---

## The derivation chain

```
                              A1
                    (finite enforcement capacity)
                            │
                     ┌──────┴──────┐
                     M             NT
                (multiplicity)  (non-degeneracy)
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

Critical path: **A1 → L<sub>ε*</sub> → L<sub>loc</sub> → L<sub>nc</sub> → T1 → T2 → T3**

Many theorems have multiple derivation paths to A1.  This is structural redundancy — the results are over-determined and would survive even if individual derivation steps were weakened.  The [interactive DAG](https://ethan-brooke.github.io/APF-Paper-1-The-Enforceability-of-Distinction/) shows exact path counts for every node.

---

## Repository structure

```
├── README.md                 ← you are here
├── REVIEWERS_GUIDE.md        ← dedicated guide for peer reviewers
├── apf/
│   ├── core.py               ← the 23 theorem check functions
│   ├── apf_utils.py          ← exact arithmetic utilities (Fraction-based)
│   └── bank.py               ← registry and runner
├── docs/
│   └── index.html            ← interactive derivation DAG (GitHub Pages)
├── run_checks.py             ← convenience entry point
├── pyproject.toml            ← metadata (zero dependencies)
├── .zenodo.json              ← archival metadata
└── LICENSE                   ← MIT
```

The mathematical content lives in `apf/core.py`.  Everything else is infrastructure.  A [reviewers' guide](REVIEWERS_GUIDE.md) provides a physics-first walkthrough of the logical architecture.

---

## What this paper derives and what it does not

**Derived:** Hilbert spaces (T2), the Born rule (T<sub>Born</sub>), Hermitian observables (T<sub>Herm</sub>), CPTP dynamics (T<sub>CPTP</sub>), tensor products (T<sub>⊗</sub>), gauge symmetry skeleton (T3), von Neumann entropy (T<sub>S</sub>), and the canonical enforcement object (T<sub>can</sub>).  All from A1.

**Not derived here:** Specific gauge groups (SU(3) × SU(2) × U(1)), particle content (61 types, 3 generations), mass hierarchies, mixing matrices, CP violation, spacetime dimension (d = 4), cosmological parameters, and the 47 zero-parameter quantitative predictions.  These are the subjects of Papers 2–7.

---

## Citation

```bibtex
@software{apf-paper1,
  title   = {The Enforceability of Distinction: The Structural Skeleton of
             Quantum Mechanics from Finite Enforcement Capacity},
  author  = {Ethan Brooke},
  year    = {2025},
  doi     = {10.5281/zenodo.18439200},
  url     = {https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction}
}
```

## License

MIT.  See [LICENSE](LICENSE).
