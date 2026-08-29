"""Day 106 — Extract c_0(R=12) = Q_{24}(10, 12, 12) via polynomial fit in t.

Sample Q_{24}(10, 12, c) at c = 28, 44, ... (c ≡ 12 mod 16, skip c=12 where fit fails),
interpolate as poly in t = (c-12)/16, extract value at t=0.

Q_{24}(10, 12, c) has degree ≤ 48 in c, so we need >= 49 samples.
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
    print("Day 106 — R=12 c_0 computation", flush=True)
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=26)
    print(f"build_e2_tables: {time.time()-t0:.1f}s", flush=True)
    a_sym, b_sym = sp.symbols('a b')

    # Q_{24}(10, 12, c) has degree ≤ 48 in c. Need 49+ samples.
    # Skip c=12 since L = c-1-k = -13 < 0.
    # Start c=28: t=1. Sample t=1..49 (49 samples).
    c_list = [28 + 16*i for i in range(49)]  # c = 28 .. 28 + 16*48 = 796

    data_path = '/home/agent/projects/code/2026-08-14-day106-R12-c0-samples.json'
    try:
        with open(data_path) as f:
            data = json.load(f)
        data = [(int(t), int(c), int(Q)) for (t, c, Q) in data]
        computed = set(c for (t, c, Q) in data)
        print(f"Loaded {len(data)} existing samples", flush=True)
    except FileNotFoundError:
        data = []
        computed = set()

    for c in c_list:
        if c in computed:
            continue
        t = (c - 12) // 16
        t1 = time.time()
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
        with open(data_path, 'w') as f:
            json.dump([[t, c, str(Q)] for (t, c, Q) in data], f)
        print(f"  c={c:4d} t={t:2d}  fit={time.time()-t1:.1f}s [{len(data)}/{len(c_list)}]", flush=True)

    n = len(data)
    print(f"Total samples: {n}", flush=True)
    if n < 49:
        print("Not enough samples")
        return

    # Sort by t
    data.sort(key=lambda x: x[0])

    # Vandermonde in t.
    A_rows = []
    y_vec = []
    for (t, c, Q) in data:
        A_rows.append([t**k for k in range(n)])
        y_vec.append(Q)
    A = Matrix(A_rows)
    y = Matrix(y_vec)
    t1 = time.time()
    sol = A.solve(y)
    print(f"Solve took {time.time()-t1:.1f}s", flush=True)

    c_0 = int(sol[0])
    print(f"\nc_0(R=12) = Q_24(10, 12, 12) = {c_0}", flush=True)

    import math
    R = 12
    pred = (R+1) * math.factorial(R)**2 * math.factorial(2*R)
    print(f"Predicted = {pred}", flush=True)
    print(f"Match exact: {c_0 == pred}", flush=True)
    print(f"Match |val|: {abs(c_0) == pred}", flush=True)
    print(f"|c_0| factorization: {factorint(abs(c_0))}", flush=True)
    print(f"pred factorization: {factorint(pred)}", flush=True)

    out = {
        'R': R,
        'c_0': str(c_0),
        'predicted': str(pred),
        'match_exact': c_0 == pred,
        'match_abs': abs(c_0) == pred,
        'factorization': {str(p): e for p, e in factorint(abs(c_0)).items()},
    }
    with open('/home/agent/projects/code/2026-08-14-day106-R12-c0.json', 'w') as f:
        json.dump(out, f, indent=2)
    print("Saved.")


if __name__ == '__main__':
    main()
