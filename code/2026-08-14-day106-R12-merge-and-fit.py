"""Day 106 merge-and-fit — combine main + supplement samples for R = 12 proof.

Loads the main samples JSON and the supplement JSON, combines them, drops any
sample with t = 0 (Pochhammer collapse at c = R = 12), and does the Vandermonde
solve for the degree-48 polynomial in t (49 samples needed at t = 1..49).

Then prints:
  - c_0 and its comparison to the predicted 12! * 13! * 24!
  - v_2(c_k) for each k, checking H5 (c_0 v_2 = 42) and Claim B (c_k v_2 >= 43 for k >= 1).
"""

import json
import time
import sys
from math import factorial
from sympy import Matrix
import sympy as sp


def v2(n):
    if n == 0: return None
    n = abs(int(n)); v = 0
    while (n & 1) == 0: n >>= 1; v += 1
    return v


def main():
    main_path = '/home/agent/projects/code/2026-08-14-day106-R12-proof-samples.json'
    supp_path = '/home/agent/projects/code/2026-08-14-day106-R12-supplement.json'

    with open(main_path) as f:
        main_data = json.load(f)
    with open(supp_path) as f:
        supp_data = json.load(f)

    combined = {}
    for (t, c, Q) in main_data + supp_data:
        combined[int(t)] = (int(t), int(c), int(Q))

    # Drop t = 0 (Pochhammer collapse at c = R = 12).
    if 0 in combined:
        print(f"Dropping t=0 sample (c={combined[0][1]}, Pochhammer collapse expected).", flush=True)
        del combined[0]

    ts = sorted(combined.keys())
    print(f"Combined samples: {len(ts)} points, t range = {ts[0]}..{ts[-1]}", flush=True)

    n_needed = 49  # degree-48 polynomial in t
    if len(ts) < n_needed:
        print(f"Only {len(ts)} samples, need {n_needed}. Aborting.", flush=True)
        sys.exit(1)

    # Take the first 49 samples (t = 1..49 if all present).
    ts = ts[:n_needed]
    data = [combined[t] for t in ts]
    n = len(data)

    # Vandermonde solve in t.
    A_rows = []
    y_vec = []
    for (t, c, Q) in data:
        A_rows.append([t**k for k in range(n)])
        y_vec.append(Q)
    A = Matrix(A_rows)
    y = Matrix(y_vec)

    print(f"Solving {n}x{n} Vandermonde system in t...", flush=True)
    t1 = time.time()
    sol = A.solve(y)
    print(f"Solve took {time.time()-t1:.1f}s", flush=True)

    C_R_pred = 42  # H5: C_12 = 4*12 - 3*s_2(12) = 48 - 6 = 42

    # c_0: constant term = Q at t = 0, formally. But polynomial in t here uses shift
    # c = 12 + 16*t; the "c_0" of the polynomial-in-t is Q evaluated at t = 0.
    c0 = int(sol[0])
    predicted = factorial(12) * factorial(13) * factorial(24)
    print(f"\nc_0 (polynomial-in-t constant term) = {c0}", flush=True)
    print(f"Predicted 12! * 13! * 24! = {predicted}", flush=True)
    print(f"c_0 == predicted? {'Y' if c0 == predicted else 'N'}", flush=True)

    print(f"\nv_2 of each c_k:", flush=True)
    all_ok = True
    v2_c0 = v2(c0)
    mark0 = "OK" if v2_c0 == C_R_pred else "XX"
    print(f"  c_0: v_2 = {v2_c0}, expected {C_R_pred}  [{mark0}]  (H5)", flush=True)
    if v2_c0 != C_R_pred:
        all_ok = False

    needed = C_R_pred + 1  # 43
    for k in range(1, n):
        coef = int(sol[k])
        if coef == 0:
            print(f"  c_{k}: 0 (trivially OK)", flush=True)
            continue
        vk = v2(coef)
        ok = vk >= needed
        mark = "OK" if ok else "XX"
        print(f"  c_{k}: v_2 = {vk} (need >= {needed})  [{mark}]", flush=True)
        if not ok:
            all_ok = False

    print("", flush=True)
    if all_ok:
        print(f"*** CLAIM B PROVED at R = 12 (H5 CONFIRMED: C_12 = 42) ***", flush=True)
    else:
        print(f"Proof FAILED - some coefficients don't satisfy the mod-2^{needed} condition.", flush=True)


if __name__ == '__main__':
    main()
