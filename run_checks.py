#!/usr/bin/env python3
"""Run all Paper 1 theorem checks.

Executes the 23 machine-verifiable theorems from Paper 1 of the
Admissibility Physics Framework. Every theorem traces back to
Axiom A1 (finite enforcement capacity) through the derivation chain:

    A1 → L_ε* → L_nc → L_loc → L_irr → T1 → T2 → T3 → ...

Usage:
    python run_checks.py              # run all 23 checks
    python run_checks.py T2           # run a single check
    python run_checks.py --list       # list all theorem names
    python run_checks.py --deps T3    # show dependency chain for T3
"""

import sys
import os

# Ensure the package is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    from apf.bank import run_all, list_theorems, get_check

    args = sys.argv[1:]

    if not args:
        # Run everything
        print()
        print("  APF Paper 1 — Structural Skeleton (SPINE)")
        print("  " + "=" * 50)
        print("  23 theorems from A1 (finite enforcement capacity)")
        print()
        results = run_all(verbose=True)
        print()
        return

    if args[0] == '--list':
        print("\nPaper 1 theorems (23):\n")
        for name in list_theorems():
            print(f"  {name}")
        print()
        return

    if args[0] == '--deps' and len(args) > 1:
        name = args[1]
        fn = get_check(name)
        if fn is None:
            print(f"Unknown theorem: {name}")
            sys.exit(1)
        r = fn()
        deps = r.get('dependencies', [])
        print(f"\n{name} depends on: {', '.join(deps) if deps else '(none — this is the root)'}")
        print(f"Key result: {r.get('key_result', 'N/A')}\n")
        return

    # Run a single named check
    name = args[0]
    fn = get_check(name)
    if fn is None:
        print(f"Unknown theorem: {name}")
        print(f"Available: {', '.join(list_theorems())}")
        sys.exit(1)

    r = fn()
    status = 'PASS' if r['passed'] else 'FAIL'
    print(f"\n  {status}  {name}")
    print(f"  Key result: {r.get('key_result', 'N/A')}")
    print(f"  Dependencies: {', '.join(r.get('dependencies', []))}")
    print(f"  Epistemic: {r.get('epistemic', '?')}")
    print()


if __name__ == '__main__':
    main()
