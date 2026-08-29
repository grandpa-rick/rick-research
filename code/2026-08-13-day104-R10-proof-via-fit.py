"""Day 104 (2026-08-13) — attempt PROOF of Claim B at R=10 via polynomial fit.

Q_{20}(8, 10, c) has degree ≤ 40 in c. Need 41+ samples on c ≡ 10 mod 16.
Each fit_Qk_bivar takes ~80s at k=20, so 41 samples ≈ 55 min.

Runs incrementally, saving each Q value as computed. Prints progress.
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
    print("Day 104 — Claim B PROOF attempt at R=10 (Q_{20}(8, 10, c))", flush=True)
    tables = hkfit.build_e2_tables(max_j=22)
    a_sym, b_sym = sp.symbols('a b')

    # Sample c-values on c ≡ 10 mod 16
    c_list = [42 + 16*i for i in range(45)]  # 45 samples, up to c = 42 + 704 = 746
    print(f"c range: {c_list[0]} .. {c_list[-1]}, {len(c_list)} samples targeted", flush=True)

    data_path = '/home/agent/projects/code/2026-08-13-day104-R10-samples.json'
    try:
        with open(data_path) as f:
            data = json.load(f)
        data = [tuple(d) for d in data]
        computed_cs = set(c for (t, c, Q) in data)
        print(f"Loaded {len(data)} existing samples", flush=True)
    except FileNotFoundError:
        data = []
        computed_cs = set()

    C_R_pred = 34
    for c in c_list:
        if c in computed_cs:
            continue
        t = (c - 10) // 16
        t0 = time.time()
        try:
            res = d102.fit_Qk_bivar(c, 20, tables)
        except Exception as e:
            print(f"  c={c}: ERROR {e}", flush=True)
            continue
        if res is None:
            print(f"  c={c}: fit failed", flush=True)
            continue
        Q_poly, _ = res
        Q_val = int(Q_poly.subs({a_sym: 8, b_sym: 10}))
        data.append((t, c, Q_val))
        # Save incrementally
        with open(data_path, 'w') as f:
            json.dump([[t, c, str(Q)] for (t, c, Q) in data], f)
        v2Q = v2(Q_val)
        mark = "✓" if v2Q == C_R_pred else "✗"
        print(f"  c={c:>4} t={t:>3} v_2(Q)={v2Q} {mark} t_fit={time.time()-t0:.1f}s [{len(data)}/{len(c_list)}]", flush=True)

    print(f"\nTotal samples: {len(data)}", flush=True)

    # Fit polynomial in t
    n = len(data)
    if n < 41:
        print(f"Only {n} samples, need at least 41. Cannot prove.", flush=True)
        return
    tsym = sp.symbols('t')
    A_rows = []
    y_vec = []
    for (t, c, Q) in data:
        # Convert Q to int if str
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
    print(f"\nc_0: v_2 = {v2_c0}, expected {C_R_pred}. {'✓' if v2_c0 == C_R_pred else '✗'}", flush=True)
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
            print(f"  c_{k}: v_2 = {vk} (need ≥ {needed}) ✗", flush=True)
            all_ok = False

    if all_ok:
        print(f"\n*** CLAIM B PROVED at R = 10 ***", flush=True)
    else:
        print(f"\nProof FAILED — some coefficients don't satisfy the mod-2^{C_R_pred+1} condition.", flush=True)


if __name__ == '__main__':
    main()
