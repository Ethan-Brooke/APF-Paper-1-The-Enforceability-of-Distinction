# The Enforceability of Distinction: Quantum Structure from Finite Enforcement Capacity

### Interactive Mathematical Appendix to Paper 1 of the Admissibility Physics Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18439200.svg)](https://doi.org/10.5281/zenodo.18439200) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction/blob/main/APF_Reviewer_Walkthrough.ipynb)

[Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-1-The-Enforceability-of-Distinction/) · [Theorem Map](#theorem-mapping-table) · [Reviewers' Guide](REVIEWERS_GUIDE.md) · [The full APF corpus](#the-full-apf-corpus) · [Citation](#citation)

> **AI agents:** start with [`START_HERE.md`](START_HERE.md) — operational checklist that loads the framework context in 5–10 minutes. The corpus inventory and full file map are in [`ai_context/repo_map.json`](ai_context/repo_map.json).

---

## Why this codebase exists

Argument-first technical paper of the Admissibility Physics Framework. From PLEC's four constitutive features (A1, MD, A2, BW) on FD1's enforcement-interface triple (S_Γ, 𝒟(Γ), C(Γ)), the body delivers two formal endpoints: the Sep/IJC classification of finite tested interfaces, and a noncommutative continuation structure on the (IJC) branch (the bridge L_Δ → T1 → T_adj → L_blk → T_alg). The standard ascent from this noncommutative continuation algebra to a complex Hilbert representation, the Born rule, and Tsirelson-type bounds is previewed and deferred to the quantum-structure paper. Companion: standalone formal-foundation supplement (v8.8, concept DOI 10.5281/zenodo.19714957) carrying the Sep/IJC Representation Theorem as a finite-Boolean-feasibility biconditional.

This repository is the executable audit layer for the symbolic proofs in this paper.  Every theorem in the manuscript traces to a named `check_*` function that exercises the claim at concrete representative values; the symbolic proof itself lives in the manuscript and its Technical Supplement.  Numerical agreement at concrete values is a sanity check, not a proof — see Paper~0 v4.4 §`sec:codebase` for the canonical trust-control discipline.

The codebase is a faithful subset of the canonical APF codebase v24.3.249 (3,745 bank-registered theorems across 422 modules). Each theorem in the manuscript traces to a named `check_*` function in the bundled `apf/` package, which can be called independently and returns a structured result.

The codebase requires Python 3.8+ and NumPy / SciPy (some numerical lemmas use them; see `pyproject.toml`).

## How to verify

Three paths, in order of increasing friction:

**1. Colab notebook — zero install.** [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction/blob/main/APF_Reviewer_Walkthrough.ipynb) Every key theorem is derived inline, with annotated cells you can inspect and modify. Run all cells — the full verification takes under a minute.

**2. Browser — zero install.** Open the [Interactive Derivation DAG](https://ethan-brooke.github.io/APF-Paper-1-The-Enforceability-of-Distinction/). Explore the dependency graph. Hover any node for its mathematical statement, key result, and shortest derivation chain to A1. Click **Run Checks** to watch all theorems verify in topological order.

**3. Local execution.**

```bash
git clone https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction.git
cd APF-Paper-1-The-Enforceability-of-Distinction
pip install -e .
python run_checks.py
```

Expected output:

```
      Paper 1 (The Enforceability of Distinction): 18 passed, 0 failed, 18 total — verified in <minutes>
```

**4. Individual inspection.**

```python
from apf.bank import get_check
r = get_check('check_A1')()
print(r['key_result'])
```

For reviewers, a [dedicated guide](REVIEWERS_GUIDE.md) walks through the logical architecture, the structural assumptions, and the anticipated objections.

---

## Theorem mapping table

This table maps every result in the manuscript to its executable verification.

| Check | Type | Summary |
|-------|------|---------|
| `check_A1` | Other | A1: Finite Enforcement Capacity (THE AXIOM). |
| `check_MD` | Other |  |
| `check_A2` | Other |  |
| `check_BW` | Other |  |
| `check_L_epsilon_star` | Lemma | L_epsilon*: Minimum Enforceable Distinction. |
| `check_L_cost` | Lemma | L_cost: Cost Functional Uniqueness (v3.1). |
| `check_L_loc` | Lemma | L_loc: Locality from Admissibility Physics. |
| `check_NT` | Other | NT: Non-Degeneracy Postulate. |
| `check_L_nc` | Lemma | L_nc: Non-Closure from Admissibility Physics + Locality. |
| `check_L_Delta` | Lemma |  |
| `check_L_irr` | Lemma | L_irr: Irreversibility from Admissibility Physics. |
| `check_T1` | Theorem | T1: Non-Closure -> Measurement Obstruction. |
| `check_T_adj` | Theorem |  |
| `check_T_alg` | Theorem | T_alg: Enforcement algebra A = Alg{E_d} cannot be faithfully represented |
| `check_T2` | Theorem | T2: Non-Closure -> Operator Algebra on Hilbert Space. |
| `check_T_Born` | Theorem | T_Born: Born Rule from Admissibility Invariance. |
| `check_Tsirelson` | Theorem |  |
| `check_T_canonical` | Theorem | T_canonical: The Canonical Object (Theorem 9.16, Paper 13 Section 9). |

All check functions reside in `apf/core.py`. Every function listed above can be called independently and returns a structured result including its logical dependencies and the mathematical content it verifies.

---

## The derivation chain

```
  Level 0: A1 · MD · A2 · BW
  Level 1: L_epsilon_star · L_loc · L_nc
  Level 2: L_cost · L_Delta
  Level 3: NT · L_irr · T1
  Level 4: T_adj
  Level 5: T_alg
  Level 6: T2
  Level 7: T_Born · Tsirelson
  Level 8: T_canonical
```

The [interactive DAG](https://ethan-brooke.github.io/APF-Paper-1-The-Enforceability-of-Distinction/) shows the full graph with hover details and animated verification.

---

## Repository structure

```
├── README.md                              ← you are here
├── START_HERE.md                          ← AI operational checklist; read-first for AI agents
├── REVIEWERS_GUIDE.md                     ← physics-first walkthrough for peer reviewers
├── interactive_dag.html                   ← interactive D3.js derivation DAG (also served at docs/ via GitHub Pages)
├── repo_map.json                          ← machine-readable map of this repo (root copy of ai_context/repo_map.json)
├── theorems.json                          ← theorem catalog (root copy of ai_context/theorems.json)
├── derivation_graph.json                  ← theorem DAG as JSON (root copy of ai_context/derivation_graph.json)
├── ai_context/                            ← AI onboarding pack (corpus map, theorems, glossary, etc.)
│   ├── AGENTS.md                          ← authoritative entry point for AI agents
│   ├── FRAMEWORK_OVERVIEW.md              ← APF in 5 minutes
│   ├── GLOSSARY.md                        ← axioms, PLEC primitives, epistemic tags
│   ├── AUDIT_DISCIPLINE.md                ← engagement posture for critique/proposal
│   ├── OPEN_PROBLEMS.md                   ← catalog of open problems + verdicts
│   ├── repo_map.json                      ← machine-readable map of this repo
│   ├── theorems.json                      ← machine-readable theorem catalog
│   ├── derivation_graph.json              ← theorem DAG as JSON
│   └── wiki/                              ← bundled APF wiki (concepts, papers, codebase)
├── apf/
│   ├── core.py                            ← 18 theorem check functions
│   ├── apf_utils.py                       ← exact arithmetic + helpers
│   └── bank.py                            ← registry and runner
├── docs/
│   └── index.html                         ← interactive derivation DAG (GitHub Pages)
├── APF_Reviewer_Walkthrough.ipynb         ← Colab notebook
├── run_checks.py                          ← convenience entry point
├── pyproject.toml                         ← package metadata
├── zenodo.json                            ← archival metadata
├── Paper_1_Enforceability_of_Distinction_v5.2.tex                ← the paper
├── Paper_1_Enforceability_of_Distinction_Supplement_v8.31.tex                ← Technical Supplement

└── LICENSE                                ← MIT
```

---

## What this paper derives and what it does not

**Derived:** (see Theorem mapping table above)

**Not derived here:** Specific results outside this paper's scope live in companion papers — see the corpus table below for the full corpus (Papers 0-42).

---

## Citation

```bibtex
@software{apf-paper1,
  title   = {The Enforceability of Distinction: Quantum Structure from Finite Enforcement Capacity},
  author  = {Brooke, Ethan},
  year    = {2026},
  doi     = {10.5281/zenodo.18439200},
  url     = {https://github.com/Ethan-Brooke/APF-Paper-1-The-Enforceability-of-Distinction}
}
```

For the full citation lineage (concept-DOI vs version-DOI, related identifiers, bibtex for all corpus papers), see [`ai_context/CITING.md`](ai_context/CITING.md).

---

<!-- FOOTER:start -->
---

## About the APF series

The Admissibility Physics Framework is a constraint-first derivation of the Standard Model and cosmological structure from a single primitive — finite enforcement capacity. The corpus runs from the foundational papers through the gauge sector, the quantum formalism, Lorentzian spacetime and the Einstein field equations, the cosmological constant, the electroweak and dark sectors, and the lattice Yang-Mills program. Each paper's main text and Technical Supplement is deposited separately on Zenodo and collected in the **[admissibility_physics](https://zenodo.org/communities/admissibility_physics)** community. The engine repository is the machine-verifiable companion to all of it (v24.3.249 — 3,745 bank-registered theorems across 422 typed modules, 48 quantitative predictions).

| # | Title | Concept DOI |
|---|---|---|
| Engine | Admissibility Physics — Unified Theorem Bank & Verification Engine | [10.5281/zenodo.18529115](https://doi.org/10.5281/zenodo.18529115) |
| 0 | What Physics Permits: A Constraint-First Framework for Physics | [10.5281/zenodo.18439523](https://doi.org/10.5281/zenodo.18439523) |
| 1 | The Enforceability of Distinction | [10.5281/zenodo.18439200](https://doi.org/10.5281/zenodo.18439200) |
| 2 | Finite Admissibility and the Failure of Global Description | [10.5281/zenodo.18439274](https://doi.org/10.5281/zenodo.18439274) |
| 3 | Entropy, Time, and Accumulated Cost | [10.5281/zenodo.18439363](https://doi.org/10.5281/zenodo.18439363) |
| 4 | Admissibility Constraints and Structural Saturation | [10.5281/zenodo.18439397](https://doi.org/10.5281/zenodo.18439397) |
| 5 | Quantum Structure from Finite Enforceability | [10.5281/zenodo.18439433](https://doi.org/10.5281/zenodo.18439433) |
| 6 | Dynamics and Geometry as Optimal Admissible Reallocation | [10.5281/zenodo.18439445](https://doi.org/10.5281/zenodo.18439445) |
| 7 | A Minimal Quantum of Action from Finite Admissibility | [10.5281/zenodo.18439513](https://doi.org/10.5281/zenodo.18439513) |
| 8 | The Admissibility-Capacity Ledger | [10.5281/zenodo.19721384](https://doi.org/10.5281/zenodo.19721384) |
| 9 | The Geometric Substrate as Cost Structure of Comparison Continuations | [10.5281/zenodo.20041675](https://doi.org/10.5281/zenodo.20041675) |
| 10 | The Calculus of Finite Continuability | [10.5281/zenodo.20041680](https://doi.org/10.5281/zenodo.20041680) |
| 11 | Forced Universality from Capacity-Bounded Admissibility | [10.5281/zenodo.20684198](https://doi.org/10.5281/zenodo.20684198) |
| 13 | The Minimal Admissibility Core | [10.5281/zenodo.18361446](https://doi.org/10.5281/zenodo.18361446) |
| 16 | Markov Breakdown and the Hard Problems | [10.5281/zenodo.20684207](https://doi.org/10.5281/zenodo.20684207) |
| 18 | The Electroweak Sector as a Capacity Equilibrium | [10.5281/zenodo.20684209](https://doi.org/10.5281/zenodo.20684209) |
| 20 | The Enforcement Crystal | [10.5281/zenodo.18531732](https://doi.org/10.5281/zenodo.18531732) |
| 21 | APF Engine — Unified Theorem Bank and Verification Engine | [10.5281/zenodo.18529115](https://doi.org/10.5281/zenodo.18529115) |
| 24 | The Recruitment-Radius Extension — Foundations | [10.5281/zenodo.20684211](https://doi.org/10.5281/zenodo.20684211) |
| 28 | Absolute Mass Scales from Electroweak Capacity Saturation | [10.5281/zenodo.20684215](https://doi.org/10.5281/zenodo.20684215) |
| 29 | Plaquette Representation Dominance and Confinement | [10.5281/zenodo.20684218](https://doi.org/10.5281/zenodo.20684218) |
| 30 | A Tube Mechanism for the Lattice Mass Gap | [10.5281/zenodo.20684220](https://doi.org/10.5281/zenodo.20684220) |
| 31 | Osterwalder-Schrader Structure of Lattice Yang-Mills | [10.5281/zenodo.20684222](https://doi.org/10.5281/zenodo.20684222) |
| 33 | Trace-to-Scheme Export Architecture | [10.5281/zenodo.20684224](https://doi.org/10.5281/zenodo.20684224) |
| 35 | The Dark Sector as a Two-Role Capacity Decomposition | [10.5281/zenodo.20684228](https://doi.org/10.5281/zenodo.20684228) |
| 40 | Between Symmetry and the Void — The Thermodynamics of Finite Distinction | [10.5281/zenodo.20684235](https://doi.org/10.5281/zenodo.20684235) |
| 41 | The Horizon as a Continuation Ledger | [10.5281/zenodo.20684241](https://doi.org/10.5281/zenodo.20684241) |
| 42 | The Weak Mixing Angle Is Not Free | [10.5281/zenodo.20684245](https://doi.org/10.5281/zenodo.20684245) |

Concept DOIs always resolve to the latest version. Technical Supplements are deposited as linked records — `isSupplementTo` the main paper, `isDocumentedBy` the companion repository.

## Author

Ethan Brooke — Independent Researcher, San Anselmo, California, USA.

- ORCID: [0009-0001-2261-4682](https://orcid.org/0009-0001-2261-4682)
- LinkedIn: [linkedin.com/in/ethanbrooke](https://www.linkedin.com/in/ethanbrooke/)
- GitHub: [github.com/Ethan-Brooke](https://github.com/Ethan-Brooke)
- Contact: brooke.ethan@gmail.com

MIT — see [LICENSE](LICENSE).
<!-- FOOTER:end -->
