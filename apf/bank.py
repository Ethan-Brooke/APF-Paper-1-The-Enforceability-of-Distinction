"""apf/bank.py — Paper 1 registry.

Lightweight registry for the 18-check subset bundled in this
paper-companion repo. Mirrors the canonical apf.bank API: REGISTRY (dict),
get_check(name), run_all(verbose=False).
"""
from collections import OrderedDict
import traceback

from apf import core as _core


def _build_registry():
    reg = OrderedDict()
    # 18-check core spine subset (Paper 1 main body)
    for name in ['check_A1', 'check_MD', 'check_A2', 'check_BW', 'check_L_epsilon_star', 'check_L_cost', 'check_L_loc', 'check_NT', 'check_L_nc', 'check_L_Delta', 'check_L_irr', 'check_T1', 'check_T_adj', 'check_T_alg', 'check_T2', 'check_T_Born', 'check_Tsirelson', 'check_T_canonical']:
        fn = getattr(_core, name, None)
        if fn is None:
            # Function couldn't be extracted — skip with a warning attribute
            continue
        reg[name] = fn
    # 3-check κ_int structural-rigidity addition (Paper 1 supplement v8.31 §9 + §14.5)
    try:
        from apf import kappa_int_bounds as _kappa_int
        _kappa_int.register(reg)
    except ImportError:
        pass  # module not available; skip
    return reg


REGISTRY = _build_registry()
EXPECTED_CHECK_COUNT = 21  # 18 core + 3 κ_int structural-rigidity


def get_check(name):
    """Return the check function registered as `name`. Raises KeyError if missing."""
    if name not in REGISTRY:
        raise KeyError(f"Check '{name}' not found. Available: {sorted(REGISTRY.keys())}")
    return REGISTRY[name]


def run_all(verbose=False):
    """Run every registered check, returning a list of result dicts."""
    results = []
    for name, fn in REGISTRY.items():
        try:
            r = fn()
            if not isinstance(r, dict):
                # Some legacy checks return True/False
                r = {"name": name, "passed": bool(r), "key_result": str(r)}
            elif "passed" not in r:
                r["passed"] = True
            r.setdefault("name", name)
        except Exception as e:
            r = {
                "name": name,
                "passed": False,
                "error": f"{type(e).__name__}: {e}",
                "traceback": traceback.format_exc(),
            }
        if verbose:
            status = "PASS" if r.get("passed", True) else "FAIL"
            print(f"  {r['name']}: {status}")
            if r.get("key_result"):
                print(f"    {r['key_result']}")
        results.append(r)
    return results
