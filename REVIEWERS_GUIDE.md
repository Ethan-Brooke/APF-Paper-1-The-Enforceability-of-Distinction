# Reviewers' Guide

### A physics-first walkthrough of the codebase for *The Enforceability of Distinction*

This document is written for the peer reviewers of Paper 1.  Its purpose is to map the logical architecture of the executable codebase to the claims in the manuscript, to make the structural assumptions maximally transparent, and to pre-empt the objections a skeptical reader should raise.

Every assertion in this guide can be verified without reading Python.  The [interactive derivation DAG](https://ethan-brooke.github.io/APF-Paper-1-The-Enforceability-of-Distinction/) provides a visual verification path; the code provides a machine-verified one.  This guide provides the third: a prose walkthrough of the mathematical logic.

---

## 1. The derivation in twelve steps

The codebase implements a single chain of reasoning from A1 to the quantum skeleton.  Here is that chain, written as a physicist would explain it to a colleague.  For each step: the theorem, what it depends on, the key mathematical move, and where to find it.

**Step 1 — A1: Finite Enforcement Capacity** (§2, `check_A1`)

The single axiom.  For any causally connected region $R$ and any state $\rho$ on $R$: the sum of enforcement costs over all simultaneously maintained distinctions is bounded by a finite, positive capacity $C(R)$.  Formally: $\sum_{d \in \mathcal{D}(\rho,R)} \varepsilon(d) \leq C(R) < \infty$, with $\varepsilon(d) \geq \varepsilon > 0$.

This is a constraint on what nature can do, not on what we can observe.  The code verifies consistency: any finite $C > 0$ works; the framework never requires a specific value.

**Step 2 — L<sub>ε*</sub>: Minimum Cost** (§4.1, `check_L_epsilon_star`)

*Depends on:* A1.

Every enforceable distinction has a minimum cost $\varepsilon^* > 0$.  The proof is by contrapositive: if $\varepsilon^* = 0$, then arbitrarily cheap distinctions exist, the number of simultaneously enforceable distinctions is unbounded, and A1 is violated.  Therefore $\varepsilon^* > 0$.

The code constructs the contradiction explicitly using exact rational arithmetic.

**Step 3 — M and NT: Multiplicity and Non-Degeneracy** (§2.2, `check_M`, `check_NT`)

*Depends on:* A1 (sub-clauses).

M: at least two distinguishable subsystems exist ($|\mathcal{D}| \geq 2$).  NT: their enforcement costs are not all equal ($\exists\, d_1, d_2 : \varepsilon(d_1) \neq \varepsilon(d_2)$).

These are the weakest possible non-triviality conditions.  Without M, A1 is satisfied trivially by a single point.  Without NT, all distinctions are clones and no internal structure arises.  Both are load-bearing assumptions at this layer; both are derived from the field content in Paper 4.  The M/NT self-consistency loop is explicitly identified as attack surface #4 in §9.2.

**Step 4 — L<sub>loc</sub>: Locality** (§4.2, `check_L_loc`)

*Depends on:* A1, L<sub>ε*</sub>, M, NT.

Enforcement must distribute over causally disconnected regions.  The proof constructs a concrete overflow witness: 6 distinctions with $\varepsilon = 2$ cost $19\frac{1}{2}$ at a single interface, exceeding $C = 10$.  But the same distinctions distribute across two interfaces at $8\frac{1}{4}$ each, both within budget.  Single-interface enforcement is inadmissible; therefore locality is forced.

This is the critical step that converts the capacity constraint into spatial structure.  The code verifies the overflow in exact arithmetic (no floating-point).

**Step 5 — L<sub>nc</sub>: Non-Closure** (§4.3, `check_L_nc`)

*Depends on:* A1, L<sub>loc</sub>.

The state space is not closed under composition.  Two individually admissible states can be jointly inadmissible: $E(\rho_1) \leq C$ and $E(\rho_2) \leq C$ but $E(\rho_1 \otimes \rho_2) > C$.  The state space is therefore not a simplex — classical probability theory fails.

This is the seed of quantum superposition.  The code constructs an explicit witness pair and verifies exact rational overflow.

**Step 6 — L<sub>Δ</sub>: Competition** (§4.4, `check_L_irr` superadditivity witness)

*Depends on:* A1, perturbation model.

Combined perturbations attacking jointly-enforced distinctions cost strictly more than the sum of individual defenses: $\Delta > 0$.  This is the assumption that separates the quantum case from the classical case.  A skeptic who rejects combined perturbations gets a classical knapsack theory — non-closure without noncommutativity.  The perturbation model is the precise assumption that selects quantum structure.  This is explicitly identified as attack surface #3 in §9.2.

**Step 7 — L<sub>irr</sub>: Irreversibility** (§4.5, `check_L_irr`)

*Depends on:* L<sub>nc</sub>, L<sub>Δ</sub>, L<sub>loc</sub>.

Cross-interface correlations, once created, cannot be locally undone.  The proof constructs a maximally entangled state and shows that the partial trace destroys the correlation information irreversibly — the original state cannot be recovered by operations on one interface alone.  This is the emergence of the arrow of time from finite capacity, not as an assumption.

**Step 8 — T1: The Bridge Theorem** (§5.1, `check_T1`)

*Depends on:* L<sub>Δ</sub>, NT, OR0 (Faithfulness).

The central theorem of the paper.  Enforcement operations are order-dependent: $E_A \circ E_B \neq E_B \circ E_A$ on the capacity functional $\Omega$.  The non-zero commutator is a direct consequence of superadditivity ($\Delta > 0$).  OR0 (Faithfulness) converts budget-level differences into state-level differences: distinct admissibility structures correspond to distinct states.

The code verifies non-commutativity using the Pauli witness ($\sigma_x, \sigma_z$) and computes the commutator norm.

**Step 9 — T2: Hilbert Space** (§5.2, `check_T2`, `check_L_T2_finite_gns`)

*Depends on:* T1, OR1–OR3, finite GNS construction.

The step from non-commuting enforcement maps to a Hilbert space representation.  This is the most technically involved step and uses four inputs:

- T1 gives non-commuting maps on $\Omega$
- OR1 (Convex Mixing) promotes them to an operator system
- OR2 (Self-Adjointness) ensures $A = A^\dagger$
- OR3 (Finite Generation) bounds the generator count by $\lfloor C/\varepsilon^* \rfloor$

The finite GNS construction (`check_L_T2_finite_gns`) then proves *constructively* — in a finite witness algebra $M_2(\mathbb{C})$ generated by $\sigma_x, \sigma_z$ — that a Hilbert space representation exists with $\dim(\mathcal{H}_{\text{GNS}}) = 4$.  Wedderburn–Artin then decomposes the algebra as $\bigoplus_k M_{n_k}(\mathbb{C})$.

No C*-completion, no Hahn–Banach, no Kadison representation theorem.  Pure finite linear algebra.

See §3 below for a detailed discussion of each OR condition.

**Step 10 — T3: Gauge Bundle** (§5.7, `check_T3`)

*Depends on:* T2, L<sub>loc</sub>.

Locality plus the operator algebra forces a gauge structure.  The automorphisms of the local algebras (the "relabelings" that preserve admissibility) form a compact group $G$.  This group has a principal-bundle structure $P \to M$ with a connection $\nabla$.  This is the skeleton of all gauge theories — from electromagnetism to the strong force — but at this stage the identity of $G$ is undetermined (that requires Paper 4).

**Step 11 — T<sub>Born</sub>, T<sub>CPTP</sub>, T<sub>⊗</sub>: Probability, dynamics, composition** (§5.3–5.6)

*Depends on:* T2, L<sub>nc</sub>, L<sub>loc</sub>.

Once the Hilbert space is established, three standard results follow:
- **T<sub>Born</sub>** (`check_T_Born`): Gleason's theorem for $\dim \geq 3$ forces $p = |\langle\psi|\varphi\rangle|^2$ as the unique probability rule.
- **T<sub>CPTP</sub>** (`check_T_CPTP`): Admissibility preservation forces completely positive trace-preserving maps as the unique dynamics.  Kraus decomposition $\Phi(\rho) = \sum K_i \rho K_i^\dagger$ is verified.
- **T<sub>⊗</sub>** (`check_T_tensor`): Independent interfaces force tensor-product composition $\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B$.  Entanglement is generic (witness: Bell state with $S = \ln 2$).

**Step 12 — T<sub>can</sub>: The Canonical Object** (§6, `check_T_canonical`)

*Depends on:* T2, T3, T<sub>S</sub>.

A1 forces a specific mathematical structure into existence: a sheaf of finite sets with a non-local cost functional $\Omega_{\text{inter}}$.  Sets compose (gluing axiom); costs do not (entanglement).  The separatedness and gluing axioms are verified constructively.  This is the mathematical type that the correlation space must have — a skeleton waiting for anatomy.

---

## 2. Pre-empting the 2×2 witness objection

A natural question: why do T1, L<sub>T2</sub>, and T0 all use $2 \times 2$ Pauli matrices?  Doesn't this smuggle quantum mechanics in through the back door?

No.  The Pauli matrices are used as an *existence proof*, not as a physical assumption.  The logical structure is:

1. T1 proves that enforcement operations *must* be non-commutative (from $\Delta > 0$ and OR0).
2. L<sub>T2</sub> then asks: given that non-commuting Hermitian operators exist, can we construct a Hilbert space representation *without* invoking infinite-dimensional functional analysis?
3. The answer is yes: take the *smallest* non-commutative algebra — $M_2(\mathbb{C})$ generated by $\sigma_x$ and $\sigma_z$ — and perform the GNS construction explicitly.  The result is a 4-dimensional Hilbert space, constructed in finite arithmetic.

The Pauli matrices are the minimal witness for non-commutativity, just as $\{0, 1\}$ is the minimal witness for a set with more than one element.  Using them proves that the GNS construction *works* in the finite case.  The specific physics (which gauge group, which particle content) enters only in Paper 4, where the capacity budget determines $G = SU(3) \times SU(2) \times U(1)$ and the representation content.

In `check_L_T2_finite_gns()`, the construction is fully explicit:
- State: $\omega(a) = \mathrm{Tr}(a)/2$
- Inner product: $\langle a, b \rangle = \omega(a^\dagger b)$
- Representation: $\pi(x)b = xb$ (left multiplication)
- Dimension: $\dim(\mathcal{H}_{\text{GNS}}) = 4$ (verified by rank computation)

No assumption of quantum mechanics is required to exhibit a non-commutative matrix algebra.

---

## 3. The structural assumptions: OR0–OR3

The passage from non-commuting enforcement maps (T1) to an operator algebra on Hilbert space (T2) requires four operational regularity conditions.  These are the structural assumptions of the framework — they play the same role as the axioms in GPT reconstruction programs (Hardy, CDP, Masanes–Müller).  We state each one, its physical content, where it enters the code, and how it compares to prior work.

### OR0 — Faithfulness

*Statement:* Distinct admissibility structures correspond to distinct states.  If two states produce different enforcement budgets, they are physically distinguishable.

*Physical content:* This is the condition that makes budget accounting meaningful.  Without it, the capacity functional $\Omega$ would not separate states, and the bridge theorem (T1) would have no force.

*Where in code:* `check_T1()` — used to convert budget-level order-dependence to state-level non-commutativity.

*Comparison:* Analogous to "no restriction" in GPT frameworks.  Weaker than local tomography (Masanes–Müller) or perfect distinguishability (CDP).

*Attack surface:* §9.2, item 2.

### OR1 — Convex Mixing

*Statement:* Probabilistic mixtures of enforcement strategies are themselves valid strategies.  If $E_1$ and $E_2$ are admissible, then $pE_1 + (1-p)E_2$ is admissible for $0 \leq p \leq 1$.

*Physical content:* This is the standard convexity assumption shared by *every* GPT reconstruction program.  It says that randomization is a valid physical operation.

*Where in code:* `check_T2()` — promotes the set of enforcement operations from a monoid to a convex operator system, enabling the algebraic structure needed for Wedderburn–Artin.

*Comparison:* Identical to the convexity axiom in Hardy (2001), CDP (2011), and Masanes–Müller (2011).  This is the most substantive of the four OR conditions.

*Attack surface:* §9.2, item 2.  A skeptic who rejects OR1 gets a non-convex theory that is not a GPT — but also not standard quantum mechanics.

### OR2 — Self-Adjointness

*Statement:* Every enforcement operation has a natural "reverse test": $A = A^\dagger$.

*Physical content:* Enforcement and measurement are two aspects of the same operation.  This is strictly weaker than Hardy's continuous reversibility and weaker than CDP's purification postulate.

*Where in code:* `check_T_Hermitian()` derives self-adjointness from L<sub>irr</sub> + L<sub>nc</sub>.  It enters T2 as a constraint on the algebra generators.

*Comparison:* Weaker than reversibility (Hardy), purification (CDP), or continuous deformation (Masanes–Müller).

### OR3 — Finite Generation

*Statement:* The number of independent algebra generators is bounded above by $\lfloor C / \varepsilon^* \rfloor$.

*Physical content:* This is not an independent assumption — it follows directly from L<sub>ε*</sub>.  If each generator corresponds to an enforceable distinction, and each distinction costs at least $\varepsilon^*$, then the generator count cannot exceed the capacity budget.

*Where in code:* `check_T2()` — used to ensure the algebra is finite-dimensional, enabling Wedderburn–Artin instead of requiring infinite-dimensional C*-theory.

*Comparison:* GPT programs that assume finite dimension directly (Hardy, CDP, Masanes–Müller) do not need this condition.  In the APF, finiteness is derived from the capacity bound.

### Summary

| | APF | Hardy (2001) | CDP (2011) | Masanes–Müller (2011) |
|---|---|---|---|---|
| Convexity | OR1 ✓ | ✓ | ✓ | ✓ |
| Faithfulness | OR0 ✓ | ✓ (implicit) | Perfect distinguishability | ✓ (implicit) |
| Reversibility | — | Continuous reversibility | Purification | Continuous reversibility |
| Local tomography | — | — | Local distinguishability | Local tomography |
| Finite dimension | OR3 (derived from A1) | State-counting rule | Assumed | Assumed |
| Composition | L<sub>loc</sub> (derived) | Subspace composition | Causality | — |

Notably absent from the APF: continuous reversibility, purification, local tomography, and subspace composition.  Present instead: the perturbation model (L<sub>Δ</sub>), which has no analog in GPT programs.

---

## 4. The five identifications

Five steps in the quantum skeleton invoke mappings between enforcement-theoretic concepts and standard mathematical structures that are not pure deductions from A1.  These are collected in §8.3 of the manuscript and are flagged as attack surface #5 in §9.2.

| Step | Identification | Physical motivation |
|------|---------------|-------------------|
| T<sub>Born</sub> | Budget conservation over outcomes ↔ Gleason frame function | Conservation of enforcement resources under measurement = frame function hypothesis |
| T<sub>CPTP</sub> | Total committed capacity ↔ operator trace | The enforcement budget of a state is its trace; budget preservation = trace preservation |
| T<sub>⊗</sub> | Linearity of enforcement in each subsystem ↔ bilinearity of composition | Independent interfaces contribute independently to the budget |
| T<sub>S</sub> | One distinction at minimum cost ↔ one qubit of compression | The natural unit of enforcement cost is the natural unit of information |
| T<sub>κ</sub> | One distinction spans at most two interfaces | Binary distinctions are the simplest non-trivial enforcement operations |

Each identification is physically motivated and consistent with A1, but none is a pure deduction from the axiom.  They represent the interface between the enforcement formalism and the mathematical formalism.  A reviewer who wishes to challenge any of them should examine the specific check function: the identification is always isolated in a clearly commented block.

---

## 5. What is not proved in Paper 1

For clarity, an explicit list of what this codebase does *not* claim to derive:

- The gauge group SU(3) × SU(2) × U(1) — Paper 4
- The 61-type field content — Paper 4
- Three generations of fermions — Paper 4
- Mass hierarchies and mixing matrices — Paper 4
- CP violation — Paper 4
- Spacetime dimension $d = 4$ — Paper 6
- Lorentzian signature — Paper 6
- The cosmological constant — Paper 6
- The 47 zero-parameter quantitative predictions — Papers 4–7

M and NT are load-bearing assumptions at this layer.  They are derived from the field content in Paper 4, creating a self-consistent loop (A1 → M/NT → field content → M/NT derived).  The DAG is acyclic; the logical structure is "assume, derive content, derive the assumption."

---

## 6. How to falsify: the six attack surfaces

These correspond to §9.2 of the manuscript.  For each, we identify what a reviewer can *do* — which code to modify and re-run to test the consequences.

| # | Attack surface | What to try in the code |
|---|---------------|------------------------|
| 1 | "Meaningful = robust" (§3) — L<sub>ε*</sub> rests on equating meaningfulness with perturbation-robustness | In `check_L_epsilon_star()`: weaken the perturbation criterion. If ε* = 0 is allowed, verify that the distinction count diverges |
| 2 | T1 and OR0 — Faithfulness converts budget differences to state differences | In `check_T1()`: remove the faithfulness check. Observe that non-commutativity no longer follows from order-dependence |
| 3 | L<sub>Δ</sub> and the perturbation model — superadditivity is the hinge | In `check_L_irr()` (witness): set Δ = 0. Observe that T1 fails: the theory becomes a classical knapsack model with additive costs |
| 4 | M/NT self-consistency — these are assumptions, not theorems, at this layer | In `check_M()`: set \|𝒟\| = 1. Verify that L<sub>loc</sub> is no longer forced (single interface suffices) |
| 5 | The five identifications (§8.3) — physically motivated but not derived from A1 | Examine the identified mapping in each check function. Each is isolated in a comment block |
| 6 | Red team: L<sub>nc</sub> necessity | `RT2_non_closure_necessity` in Appendix B: confirms Non-Closure is forced; only escapes are $C = \infty$ or $|\mathcal{D}| = 1$ |

---

## 7. Reading the code

If you choose to inspect the Python source directly, here is what to expect.

**`apf/core.py`** contains 23 functions, one per theorem.  Every function begins with a docstring that states the theorem in standard notation, lists its dependencies and manuscript section, and describes the mathematical content of the verification.  The function body constructs a witness using exact rational arithmetic (`Fraction`), verifies the stated inequality or algebraic property, and returns a structured result.

**`apf/apf_utils.py`** contains the infrastructure: exact matrix arithmetic, eigenvalue computation, trace, determinant, Kronecker product, and related operations.  All implemented using Python's `Fraction` type.  This file is infrastructure, not content — it plays the role of a linear algebra library, not a physics argument.

**`apf/bank.py`** is the registry that connects theorem names to check functions.  It provides `run_all()`, `get_check()`, and `list_theorems()`.

If you run `python run_checks.py`, every check function is called in dependency order and the results are printed.  Total execution time is under one second.

---

## 8. The scalar-to-matrix boundary

A natural concern: does the codebase smuggle quantum mechanics by using matrix multiplication (which is non-commutative by construction) to "derive" non-commutativity?

**The answer is no.  The derivation chain is strictly stratified.**

The first eleven theorems — A1, M, NT, L_epsilon*, L_loc, L_nc, L_Delta, L_irr, T0, T1 — use **only** finite sets, scalar costs, and exact rational arithmetic (`Fraction`).  No matrices.  No complex numbers.  No `_mm`, `_dag`, `_kron`, or any function from `apf_utils.py`'s linear algebra suite.

T1 (the Bridge Theorem) proves that enforcement operations are order-dependent using a purely scalar argument:

- The enforcement cost function E: 2^D -> Q is superadditive: E({s,c}) = 10 > E({s}) + E({c}) = 4 + 3 = 7.
- The marginal cost of enforcing c depends on what is already enforced: m(c | empty) = 3, but m(c | {s}) = 6.
- Similarly: m(s | empty) = 4, but m(s | {c}) = 7.
- These are different capacity profiles.  OR0 (Faithfulness) says distinct capacity profiles correspond to distinct physical states.
- Therefore enforce-s-then-c and enforce-c-then-s produce different intermediate states: the operations do not commute.

**Matrices first appear in T2**, where they are introduced as the *minimal representation* of the non-commutative structure T1 proved abstractly.  The Pauli matrices sigma_x, sigma_z generating M_2(C) are *consequences* of T1, not inputs to it.

If you wish to verify this stratification, search `check_T0` and `check_T1` for any call to `_mat`, `_mm`, `_dag`, `_kron`, `_tr`, `_eye`, or `_fnorm`.  You will find none.

---

## 9. Why the complex numbers?

Once T1 establishes non-commutativity from scalar capacity accounting, T2 must ask: what is the minimal algebraic structure that can represent non-commuting enforcement operations while preserving the capacity functional (trace)?

By **Frobenius' theorem** (1878), the only finite-dimensional associative division algebras over R are:

| Algebra | Commutative? | Self-dual? | Verdict |
|---------|-------------|-----------|---------|
| R | Yes | Yes | Cannot represent [E_A, E_B] != 0 |
| C | No (as a matrix ring) | Yes | **Forced** |
| H (quaternions) | No | No | Violates self-duality of capacity functional |

R is ruled out because it is commutative — it cannot host the non-commutative structure T1 proved.  H is ruled out because the capacity functional must be self-dual (the state space is its own dual under the trace inner product), which the quaternions violate.  Therefore C is the unique ground field.

This argument is well-established in the quantum foundations literature (see Barnum, Mueller, and Ududec, "Higher-order interference and single-system postulates characterizing quantum theory," *New J. Phys.* **16**, 123029, 2014).

The exact rational arithmetic in the pre-T2 code does not conflict with the complex numbers in the post-T2 code.  The rationals prove the *algebraic structure* (superadditivity, non-commutativity, non-closure).  The complex numbers are a property of the *representation* that structure forces.

---

*This guide accompanies the manuscript "The Enforceability of Distinction" submitted to Foundations of Physics, March 2026.*
