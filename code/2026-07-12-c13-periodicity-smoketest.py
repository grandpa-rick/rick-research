"""Smoke test: run c=13 periodicity script logic at T=7 and T=10 to verify
correctness on small grids and estimate runtime scaling."""
import sys
import time
from importlib import util
import json

import numpy as np
from sympy import symbols, sympify

spec = util.spec_from_file_location(
    "c13per", "/home/agent/projects/code/2026-07-12-c13-periodicity.py"
)
c13per = util.module_from_spec(spec)
spec.loader.exec_module(c13per)

# Also load the extract pipeline directly for cross-checking against sympy poly
spec2 = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod2 = util.module_from_spec(spec2)
spec2.loader.exec_module(mod2)


def main():
    c_val = 13

    # Load Q catalog
    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
        cat = json.load(f)
    a_s, b_s, c_s = symbols('a b c')
    Q_cat = {}
    for ks, s in cat["Q_k_low_k"].items():
        Q_cat[int(ks)] = sympify(s)
    Q_cat[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])

    # Sanity check: compare eval_hk_via_catalog_mod2T against extract_h_k for
    # a few (a, b) points, k = 0..6, at T = 30 (large enough to cover exact
    # values for the small (a, b)).
    print("Sanity check: h_k catalog eval vs extract_h_k, at small (a, b)")
    T = 30
    size_test = 32  # small grid; a, b in [0, 32)
    tables = mod2.build_e2_tables(max_j=14)
    for k in range(7):
        P_mod = c13per.eval_hk_via_catalog_mod2T(
            Q_cat[k], a_s, b_s, c_s, c_val, k, T, size_test)
        mask = (1 << T) - 1
        for (av, bv) in [(13, 13), (14, 15), (20, 17)]:
            hks = mod2.extract_h_k(av, bv, c_val, 12, tables)
            if hks is None:
                continue
            true_val = hks[k]
            expected = true_val % (1 << T)
            got = int(P_mod[av, bv])
            match = "OK" if (got == expected) else f"MISMATCH (want {expected})"
            print(f"  k={k} (a,b)=({av},{bv}): got {got}, {match}", flush=True)

    # Run periodicity at T=10 for k=0..6 via catalog to estimate time
    for T_check in [10, 12, 13]:
        size = 1 << T_check
        a_vec = np.arange(size, dtype=np.int64)
        b_vec = np.arange(size, dtype=np.int64)
        parity_mask = ((a_vec[:, None] + b_vec[None, :]) & 1) == 1
        print(f"\n[periodicity T={T_check}, k=0..6 via Q-cat]", flush=True)
        total_t = 0
        for k in range(7):
            t0 = time.time()
            P_mod = c13per.eval_hk_via_catalog_mod2T(
                Q_cat[k], a_s, b_s, c_s, c_val, k, T_check, size)
            min_v2, n_zero, n_total = c13per.compute_min_v2_on_shell(
                P_mod, parity_mask, T_check)
            dt = time.time() - t0
            total_t += dt
            print(f"  k={k}: min v_2 = {min_v2}, {n_zero}/{n_total}, {dt:.2f}s", flush=True)
            del P_mod
        print(f"  total (k=0..6): {total_t:.1f}s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
