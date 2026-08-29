"""Day 106 (2026-08-14) — PROOF of Claim B at R=12 via polynomial fit (H5 confirmation).

Q_{24}(10, 12, c) has degree ≤ 48 in c. Need 49+ samples on c ≡ 12 mod 16.
H5 predicts C_R = 4R − 3·s_2(R). For R=12: s_2(12)=2, so C_12 = 48 − 6 = 42.

Samples c = 12 + 16t for t = 0, 1, ..., 48 (49 samples). Runs incrementally,
saving each Q value as computed. Prints progress.
"""

import time
import json
import sys
from importlib import util
from sympy import Matrix
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
    print("Day 106 — Claim B PROOF attempt at R=12 (Q_{24}(10, 12, c))", flush=True)
    print("H5 prediction: C_12 = 4*12 - 3*s_2(12) = 48 - 6 = 42", flush=True)
    tables = hkfit.build_e2_tables(max_j=26)
    a_sym, b_sym = sp.symbols('a b')

    # Sample c-values on c ≡ 12 mod 16, starting at t=0 → c=12.
    c_list = [12 + 16*i for i in range(49)]  # 49 samples, c = 12 .. 12 + 16*48 = 780
    print(f"c range: {c_list[0]} .. {c_list[-1]}, {len(c_list)} samples targeted", flush=True)

    data_path = '/home/agent/projects/code/2026-08-14-day106-R12-proof-samples.json'
    try:
        with open(data_path) as f:
            data = json.load(f)
        data = [tuple(d) for d in data]
        computed_cs = set(c for (t, c, Q) in data)
        print(f"Loaded {len(data)} existing samples", flush=True)
    except FileNotFoundError:
        data = []
        computed_cs = set()

    C_R_pred = 42
    for c in c_list:
        if c in computed_cs:
            continue
        t = (c - 12) // 16
        t0 = time.time()
        try:
            res = d102.fit_Qk_bivar(c, 24, tables)
        except Exception as e:
            print(f"  c={c}: ERROR {e}", flush=True)
            continue
        if res is None:
            print(f"  c={c}: fit failed", flush=True)
            continue
        Q_poly, _ = res
        Q_val = int(Q_poly.subs({a_sym: 10, b_sym: 12}))
        data.append((t, c, Q_val))
        # Save incrementally
        with open(data_path, 'w') as f:
            json.dump([[t, c, str(Q)] for (t, c, Q) in data], f)
        v2Q = v2(Q_val)
        mark = "OK" if v2Q == C_R_pred else "XX"
        print(f"  c={c:>4} t={t:>3} v_2(Q)={v2Q} {mark} t_fit={time.time()-t0:.1f}s [{len(data)}/{len(c_list)}]", flush=True)

    print(f"\nTotal samples: {len(data)}", flush=True)

    # Fit polynomial in t
    n = len(data)
    if n < 49:
        print(f"Only {n} samples, need at least 49. Cannot prove.", flush=True)
        return
    tsym = sp.symbols('t')
    A_rows = []
    y_vec = []
    for (t, c, Q) in data:
        Qi = int(Q) if isinstance(Q, str) else Q
        A_rows.append([t**k for k in range(n)])
        y_vec.append(Qi)
    A = Matrix(A_rows)
    y = Matrix(y_vec)
    print(f"Solving {n}x{n} Vandermonde system...", flush=True)
    t1 = time.time()
    sol = A.solve(y)
    print(f"Solve took {time.time()-t1:.1f}s", flush=True)

    all_ok = True
    v2_c0 = v2(sol[0])
    print(f"\nc_0: v_2 = {v2_c0}, expected {C_R_pred}. {'OK' if v2_c0 == C_R_pred else 'XX'}", flush=True)
    if v2_c0 != C_R_pred:
        all_ok = False
    for k in range(1, n):
        coef = int(sol[k])
        if coef == 0:
            continue
        vk = v2(coef)
        needed = C_R_pred + 1
        ok = vk >= needed
        if not ok:
            print(f"  c_{k}: v_2 = {vk} (need >= {needed}) XX", flush=True)
            all_ok = False

    if all_ok:
        print(f"\n*** CLAIM B PROVED at R = 12 (H5 CONFIRMED: C_12 = 42) ***", flush=True)
    else:
        print(f"\nProof FAILED - some coefficients don't satisfy the mod-2^{C_R_pred+1} condition.", flush=True)


if __name__ == '__main__':
    main()
