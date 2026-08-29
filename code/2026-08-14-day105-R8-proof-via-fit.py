"""Day 105 (2026-08-14) — attempt PROOF of Claim B at R=8 via polynomial fit.

Q_{16}(6, 8, c) has degree ≤ 32 in c. Need 33+ samples on c ≡ 8 mod 16.
Use 37 samples for a small margin.

Two-phase run:
  Phase 1: compute Q_{16}(6, 8, 24) alone -> v_2 gives the ANCHOR value C_8.
           Hard-code C_R_pred = C_8 and print it.
  Phase 2: full sweep + Vandermonde solve, verify
             * v_2(c_0) == C_8 exactly
             * v_2(c_k) >= C_8 + 1 for all k >= 1

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
    t_wall_start = time.time()
    print("Day 105 — Claim B PROOF attempt at R=8 (Q_{16}(6, 8, c))", flush=True)
    # k_max = 16, need max_j >= 18 to be safe (mirroring pattern from R=10 which used max_j=22)
    tables = hkfit.build_e2_tables(max_j=18)
    a_sym, b_sym = sp.symbols('a b')

    # Sample c-values on c ≡ 8 mod 16: c = 8 + 16*t, t >= 1 (need c-1-16 >= 0 so c >= 17)
    # t=1 -> c=24, t=2 -> c=40, ..., 37 samples up to t=37 -> c=8+16*37 = 600
    c_list = [24 + 16 * i for i in range(37)]  # 37 samples, c in {24, 40, ..., 600}
    print(f"c range: {c_list[0]} .. {c_list[-1]}, {len(c_list)} samples targeted", flush=True)

    data_path = '/home/agent/projects/code/2026-08-14-day105-R8-samples.json'
    try:
        with open(data_path) as f:
            data = json.load(f)
        data = [tuple(d) for d in data]
        computed_cs = set(c for (t, c, Q) in data)
        print(f"Loaded {len(data)} existing samples", flush=True)
    except FileNotFoundError:
        data = []
        computed_cs = set()

    # --- Phase 1: compute anchor at c=24 first, if not already present, to obtain C_R_pred ---
    C_R_pred = None
    anchor_c = 24
    anchor_val = None
    for (t, c, Q) in data:
        if c == anchor_c:
            anchor_val = int(Q) if isinstance(Q, str) else Q
            break

    if anchor_val is None:
        print(f"\n--- Phase 1: computing anchor Q_{{16}}(6, 8, {anchor_c}) ---", flush=True)
        t0 = time.time()
        res = d102.fit_Qk_bivar(anchor_c, 16, tables)
        if res is None:
            print(f"  ANCHOR fit failed at c={anchor_c}", flush=True)
            return
        Q_poly, _ = res
        anchor_val = int(Q_poly.subs({a_sym: 6, b_sym: 8}))
        t_anchor = (anchor_c - 8) // 16
        data.append((t_anchor, anchor_c, anchor_val))
        with open(data_path, 'w') as f:
            json.dump([[tt, cc, str(QQ)] for (tt, cc, QQ) in data], f)
        print(f"  Anchor computed in {time.time()-t0:.1f}s", flush=True)

    C_8 = v2(anchor_val)
    C_R_pred = C_8
    print(f"\n*** ANCHOR: v_2(Q_{{16}}(6, 8, 24)) = {C_8}  --> C_8 = {C_8} ***", flush=True)
    print(f"    (setting C_R_pred = {C_R_pred} for the full sweep)\n", flush=True)

    # --- Phase 2: full sweep ---
    for c in c_list:
        if c in computed_cs or c == anchor_c:
            continue
        t = (c - 8) // 16
        t0 = time.time()
        try:
            res = d102.fit_Qk_bivar(c, 16, tables)
        except Exception as e:
            print(f"  c={c}: ERROR {e}", flush=True)
            continue
        if res is None:
            print(f"  c={c}: fit failed", flush=True)
            continue
        Q_poly, _ = res
        Q_val = int(Q_poly.subs({a_sym: 6, b_sym: 8}))
        data.append((t, c, Q_val))
        with open(data_path, 'w') as f:
            json.dump([[tt, cc, str(QQ)] for (tt, cc, QQ) in data], f)
        v2Q = v2(Q_val)
        mark = "OK" if v2Q == C_R_pred else "XX"
        print(f"  c={c:>4} t={t:>3} v_2(Q)={v2Q} {mark} t_fit={time.time()-t0:.1f}s [{len(data)}/{len(c_list)}]", flush=True)

    print(f"\nTotal samples: {len(data)}", flush=True)

    # Fit polynomial in t
    # Sort data by t
    data_sorted = sorted([(int(t), int(c), int(Q) if isinstance(Q, str) else Q) for (t, c, Q) in data], key=lambda r: r[0])
    n = len(data_sorted)
    if n < 33:
        print(f"Only {n} samples, need at least 33. Cannot prove.", flush=True)
        return
    A_rows = []
    y_vec = []
    for (t, c, Q) in data_sorted:
        A_rows.append([t**k for k in range(n)])
        y_vec.append(Q)
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

    wall = time.time() - t_wall_start
    if all_ok:
        print(f"\n*** CLAIM B PROVED at R = 8 ***", flush=True)
        print(f"    v_2(Q_{{16}}(6, 8, c)) = {C_R_pred} EXACTLY for all c ≡ 8 mod 16.", flush=True)
    else:
        print(f"\nProof FAILED — some coefficients don't satisfy the mod-2^{C_R_pred+1} condition.", flush=True)

    print(f"\nTotal wall-clock: {wall:.1f}s ({wall/60:.2f} min)", flush=True)


if __name__ == '__main__':
    main()
