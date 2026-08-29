"""Day 104 (2026-08-13) — PROOF of Claim B at R=6 via polynomial fit.

Q_{12}(4, 6, c) has degree ≤ 24 in c. We compute 28 integer values on
c ≡ 6 mod 16, interpolate uniquely as poly in t (c = 6 + 16t), check
coefficients modulo 2^19.

RESULT: v_2(Q_{12}(4, 6, c)) = 18 EXACTLY for all c ≡ 6 mod 16.
"""

import time
import json
from importlib import util
from sympy import symbols, Matrix, Rational
import sympy as sp

spec = util.spec_from_file_location('hkfit', '/home/agent/projects/code/2026-07-10-hk-three-var-fit.py')
hkfit = util.module_from_spec(spec); spec.loader.exec_module(hkfit)
spec2 = util.spec_from_file_location('d102', '/home/agent/projects/code/2026-07-18-day102-anchor-810-1214-probe.py')
d102 = util.module_from_spec(spec2); spec2.loader.exec_module(d102)


def v2(n):
    if n == 0: return None
    n = abs(int(n)); v = 0
    while (n & 1) == 0: n >>= 1; v += 1
    return v


def main():
    print("Day 104 — Claim B PROOF at R=6")
    tables = hkfit.build_e2_tables(max_j=14)
    a_sym, b_sym = sp.symbols('a b')

    # Sample c-values on c ≡ 6 mod 16 (28 samples, > 25 = 2·12+1 needed for degree-24 poly)
    c_list = [22, 38, 54, 70, 86, 102, 118, 134, 150, 166, 182, 198, 214, 230, 246, 262,
              294, 310, 326, 342, 358, 374, 390, 406, 422, 438, 454, 470]

    data = []
    for c in c_list:
        t = (c - 6) // 16
        res = d102.fit_Qk_bivar(c, 12, tables)
        if res is None:
            continue
        Q_poly, _ = res
        Q_val = int(Q_poly.subs({a_sym: 4, b_sym: 6}))
        data.append((t, c, Q_val))

    n = len(data)
    print(f"Collected {n} samples")

    tsym = sp.symbols('t')
    A_rows = []
    y_vec = []
    for (t, c, Q) in data:
        A_rows.append([t**k for k in range(n)])
        y_vec.append(Q)
    A = Matrix(A_rows)
    y = Matrix(y_vec)
    sol = A.solve(y)

    print(f"\nCoefficients c_k of Q_{{12}}(4, 6, 6+16t):")
    all_ok = True
    C_R = 18  # H3 prediction
    v2_c0 = v2(sol[0])
    if v2_c0 != C_R:
        print(f"  c_0: v_2 = {v2_c0}, expected {C_R}. FAIL.")
        all_ok = False
    else:
        print(f"  c_0: v_2 = {C_R} exactly. ✓")
    for k in range(1, n):
        coef = int(sol[k])
        if coef == 0:
            print(f"  c_{k}: 0")
            continue
        vk = v2(coef)
        needed = C_R + 1
        ok = vk >= needed
        mark = "✓" if ok else "✗"
        print(f"  c_{k}: v_2 = {vk} (need ≥ {needed}) {mark}")
        if not ok:
            all_ok = False

    if all_ok:
        print("\n*** CLAIM B PROVED at R = 6 ***")
        print(f"v_2(Q_{{12}}(4, 6, c)) = {C_R} EXACTLY for all c ≡ 6 mod 16.")
    else:
        print("\nProof FAILED — see coefficients above.")


if __name__ == '__main__':
    main()
