# NEXT_STEPS — Push the v8.32 + v7.9 refreshed Paper 1 repo to GitHub

The repo at `Codebase/APF-Paper-1-The-Enforceability-of-Distinction/` has been refreshed end-to-end with the LATER foundation-alignment additions:

- Paper 1 supplement v8.31 → **v8.32** (coderefs added to new bank checks)
- Codebase v7.8 → **v7.9** (Phase 42: 4 new tier-4 [P_structural] checks)
  - `apf/foundation_inputs.py` (NEW MODULE)
    - `check_T_four_input_declaration` — canonical 4-input set (FD1+FD2+FD3+finite-physical-regime)
    - `check_T_PLEC_derived_from_spine` — A1/MD/A2/BW derived consequences
  - `apf/kappa_int_bounds.py` extended
    - `check_T_R1_R4_spine_derivable`
    - `check_T_minimum_distinction_floor_via_MD`
- EXPECTED_THEOREM_COUNT 467 → **471**; verify_all 484 → **488**; modules 27 → **28**
- Codebase folder renamed v7.8 → **v7.9**
- README.md + START_HERE.md updated with v7.9 / 471/488 counts
- START_HERE.md §0 60-second mental map **rewritten in proper foundation sequence**:
  admissibility space → 3 primitives + finite-regime → PLEC derived → eternalist →
  Sep/IJC → κ_int rigidity → R1-R4 spine-derived
- Papers 9 (Geometric Substrate) + 10 (Calculus of Finite Continuability) added to
  corpus tables with placeholders for upcoming repo creation
- MANIFEST.custom extended with new sentinel ids + foundation-module entries
- All edits wrapped in `<!-- CUSTOM:start id=... -->` sentinels for refresh preservation

## Push command

The Drive-synced directory already has a `.git/` from the earlier push. To push the new commit:

```powershell
cd "C:\Users\EthanBrooke\My Drive\__APF Library\Codebase\APF-Paper-1-The-Enforceability-of-Distinction"
git add -A
git commit -m "Refresh v8.31 → v8.32 + codebase v7.8 → v7.9 (Phase 42 foundation alignment)"
git push --force
```

Or use the pre-built zip at `outputs/APF-Paper-1-refresh-v8.32-with-git_2026-05-05.zip` (unzip outside Drive, push from there).

## What changed for AI agents reading START_HERE.md

The 60-second mental map (§0) now puts the foundation claims in the right order:

1. **Admissibility space** (the structural referent) — Paper 0 v6.0 + Paper 1 sup v8.32
2. **Three primitive commitments + one regime hypothesis** = 4 inputs (FD1, FD2, FD3, finite-physical-regime)
3. **PLEC's four features as derived consequences** (not primitives) — A1/MD/A2/BW via Paper 10 §3.5 reductions
4. **Eternalist commitment** — time is derived (Paper 3 + Paper 6); operational vocabulary is descriptive convention
5. **What this paper contributes** — Sep/IJC + noncommutative continuation + κ_int rigidity + R1-R4 spine-derivation
6. **Canonical state** — codebase v7.9, 471 bank-registered theorems, 488 verify_all checks, 28 modules

This sequence is the corpus-canonical framing as of LATER-9 + LATER-22 + LATER-23 (Phase 42).
