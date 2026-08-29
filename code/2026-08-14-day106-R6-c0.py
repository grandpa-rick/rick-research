"""Day 106 — Extract c_0(R=6) = Q_{12}(4, 6, 6) via polynomial fit in c.

Approach: sample Q_{12}(4, 6, c) at c = 22, 38, 54, ... (c ≡ 6 mod 16),
interpolate as poly in t = (c-6)/16, extract constant term.
"""

import time
import json
from importlib import util
import sympy as sp
from sympy import Matrix, factorint

spec = util.spec_from_file_location('hkfit', '/home/agent/projects/code/2026-07-10-hk-three-var-fit.py')
hkfit = util.module_from_spec(spec); spec.loader.exec_module(hkfit)
spec2 = util.spec_from_file_location('d102', '/home/agent/projects/code/2026-07-18-day102-anchor-810-1214-probe.py')
d102 = util.module_from_spec(spec2); spec2.loader.exec_module(d102)


def main():
    print("Day 106 — R=6 c_0 computation", flush=True)
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=14)
    print(f"build_e2_tables: {time.time()-t0:.1f}s", flush=True)
    a_sym, b_sym = sp.symbols('a b')

    # Q_{12}(4, 6, c) has degree ≤ 24 in c. Need > 25 samples.
    c_list = [22, 38, 54, 70, 86, 102, 118, 134, 150, 166, 182, 198, 214, 230, 246, 262,
              278, 294, 310, 326, 342, 358, 374, 390, 406, 422, 438, 454, 470]

    data = []
    for c in c_list:
        t = (c - 6) // 16
        t1 = time.time()
        res = d102.fit_Qk_bivar(c, 12, tables)
        if res is None:
            print(f"  c={c}: fit failed")
            continue
        Q_poly, _ = res
        Q_val = int(Q_poly.subs({a_sym: 4, b_sym: 6}))
        data.append((t, c, Q_val))
        print(f"  c={c:3d} t={t:2d}  Q={Q_val}  fit={time.time()-t1:.1f}s", flush=True)

    n = len(data)
    print(f"Collected {n} samples", flush=True)

    # Vandermonde solve in t.
    A_rows = []
    y_vec = []
    for (t, c, Q) in data:
        A_rows.append([t**k for k in range(n)])
        y_vec.append(Q)
    A = Matrix(A_rows)
    y = Matrix(y_vec)
    t0 = time.time()
    sol = A.solve(y)
    print(f"Solve took {time.time()-t0:.1f}s", flush=True)

    c_0 = int(sol[0])
    print(f"\nc_0(R=6) = Q_12(4, 6, 6) = {c_0}", flush=True)
    print(f"|c_0| factorization: {factorint(abs(c_0))}", flush=True)

    import math
    R = 6
    pred = (R+1) * math.factorial(R)**2 * math.factorial(2*R)
    print(f"Predicted (R+1)(R!)^2(2R)! = {pred}", flush=True)
    print(f"Match (exact): {c_0 == pred}", flush=True)
    print(f"Match (abs): {abs(c_0) == pred}", flush=True)

    out = {
        'R': R,
        'c_0': str(c_0),
        'predicted': str(pred),
        'match_exact': c_0 == pred,
        'match_abs': abs(c_0) == pred,
        'factorization': {str(p): e for p, e in factorint(abs(c_0)).items()},
    }
    with open('/home/agent/projects/code/2026-08-14-day106-R6-c0.json', 'w') as f:
        json.dump(out, f, indent=2)
    print("Saved.")


if __name__ == '__main__':
    main()
