"""Day 104 — extend v_2(Q_{12}(4, 6, c)) test to more c values, including
high-v_2(c-6) cases (c-6 = 512, 1024) and c NOT ≡ 6 mod 16 for contrast."""

import json
import time
from importlib import util

import sympy as sp

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)

spec2 = util.spec_from_file_location(
    "d102", "/home/agent/projects/code/2026-07-18-day102-anchor-810-1214-probe.py"
)
d102 = util.module_from_spec(spec2)
spec2.loader.exec_module(d102)


def v2(n):
    if n == 0: return None
    n = abs(int(n)); v = 0
    while (n & 1) == 0: n >>= 1; v += 1
    return v


def main():
    print("Day 104 — Q_{12}(4, 6, c) extended residue check")
    tables = hkfit.build_e2_tables(max_j=14)
    a_sym, b_sym = sp.symbols('a b')

    # Test multiple c-residues mod 16 (all c ≡ 2 mod 4)
    # High-v_2(c-6) test: c = 6 + 512 = 518, c = 6 + 1024 = 1030
    test_cases = [
        # (c, expected residue mod 16, note)
        (518, 6, "high v_2(c-6)=9"),
        (1030, 6, "high v_2(c-6)=10"),
        # Off-residue: c ≡ 2 mod 16, c ≡ 10 mod 16, c ≡ 14 mod 16
        (34, 2, "off-residue c ≡ 2 mod 16"),
        (42, 10, "off-residue c ≡ 10 mod 16"),
        (46, 14, "off-residue c ≡ 14 mod 16"),
        # More c ≡ 6 mod 16
        (294, 6, "another c ≡ 6 mod 16"),
        (310, 6, "another c ≡ 6 mod 16"),
    ]

    for c, R_pred, note in test_cases:
        t1 = time.time()
        try:
            r = d102.fit_Qk_bivar(c, 12, tables)
        except Exception as e:
            print(f"  c={c}: ERROR {e}")
            continue
        if r is None:
            print(f"  c={c}: fit failed")
            continue
        Q_poly, D_fit = r
        Q_val = int(Q_poly.subs({a_sym: 4, b_sym: 6}))
        v2_Q = v2(Q_val)
        v2_cR = v2(c - 6)
        print(f"  c={c:>4} (c mod 16 = {c % 16}, {note})  v_2(Q_{{12}}(4,6,c)) = {v2_Q}   v_2(c-6) = {v2_cR}   t={time.time()-t1:.1f}s")


if __name__ == '__main__':
    main()
