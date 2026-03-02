"""APF Paper 1 Theorem Bank — core module only.

This is the Paper 1 subset of the full APF theorem bank. It loads
only core.py (23 theorems) corresponding to the derivation chain
established in Paper 1: "The Structural Skeleton of Quantum Mechanics
from Finite Enforcement Capacity."

The full APF codebase (312 theorems across 16+ modules) will be
released incrementally as the paper series is published.

Usage:
    from apf.bank import run_all
    results = run_all()
"""

import time as _time


# ══════════════════════════════════════════════════════════════════════
# Global registry
# ══════════════════════════════════════════════════════════════════════

REGISTRY = {}
EXPECTED_THEOREM_COUNT = 23

_loaded = False
_MODULE_MAP = {}


def _load():
    """Lazy-load the core module into the registry."""
    global _loaded
    if _loaded:
        return
    from importlib import import_module

    try:
        mod = import_module('apf.core')
        before = set(REGISTRY.keys())
        mod.register(REGISTRY)
        after = set(REGISTRY.keys())
        _MODULE_MAP['core'] = sorted(after - before)
    except ImportError as e:
        import warnings
        warnings.warn(
            f"APF: Failed to load core module: {e}",
            RuntimeWarning,
            stacklevel=2,
        )
        _MODULE_MAP['core'] = []

    _loaded = True

    actual = len(REGISTRY)
    if actual != EXPECTED_THEOREM_COUNT:
        import warnings
        warnings.warn(
            f"APF: Expected {EXPECTED_THEOREM_COUNT} theorems, loaded {actual}.",
            RuntimeWarning,
            stacklevel=2,
        )


def run_all(verbose=True):
    """Execute all 23 Paper 1 theorem checks.

    Parameters
    ----------
    verbose : bool
        Print results to stdout.

    Returns
    -------
    dict
        {theorem_name: result_dict} for all checks.
    """
    _load()

    results = {}
    passed = failed = errors = 0
    t0 = _time.time()

    for name, check_fn in REGISTRY.items():
        try:
            r = check_fn()
            results[name] = r
            if r['passed']:
                passed += 1
                mark = 'PASS'
            else:
                failed += 1
                mark = 'FAIL'
            if verbose:
                ep = r.get('epistemic', '?')
                print(f"  [{ep}] {mark}  {name}")
                if r.get('key_result'):
                    print(f"         {r['key_result']}")
        except Exception as e:
            errors += 1
            results[name] = {'passed': False, 'error': str(e)}
            if verbose:
                print(f"  [?] ERR   {name}: {e}")

    elapsed = _time.time() - t0

    if verbose:
        print(f"\n{'=' * 60}")
        print(f"  Paper 1 (SPINE): {passed} passed, {failed} failed, "
              f"{errors} errors — {len(REGISTRY)} theorems in {elapsed:.2f}s")
        print(f"{'=' * 60}")

    return results


def list_theorems():
    """Return a sorted list of all registered theorem names."""
    _load()
    return sorted(REGISTRY.keys())


def get_check(name):
    """Return the check function for a given theorem name."""
    _load()
    return REGISTRY.get(name)
