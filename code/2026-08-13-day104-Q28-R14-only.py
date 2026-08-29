"""Day 104 (2026-08-13) — Just fit Q_{28} at (a, b) = (12, 14), c ≡ 14 mod 16.

Purpose: verify v_2(Q_{28}(12, 14, c)) = 47 as predicted by H3.

Skip the full v_2(H_c) — only need Q_{28} fit at one c value.
Try c=46, 78, 158 in that order.
"""

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
    if n == 0:
        return None
    n = abs(int(n))
    v = 0
    while (n & 1) == 0:
        n >>= 1
        v += 1
    return v


def main():
    print("=" * 78)
    print("Day 104 — Q_{28}(12, 14, c) direct fit (R=14 carrier-level check)")
    print("=" * 78, flush=True)
    print("H3 predicts v_2(Q_{28}(12, 14, c)) = 47 constant for c ≡ 14 mod 16", flush=True)

    K_MAX = 28
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=K_MAX + 2)
    print(f"build_e2_tables(max_j={K_MAX + 2}): {time.time() - t0:.1f}s", flush=True)

    a_sym, b_sym = sp.symbols('a b')

    for c in [46, 78, 158]:
        L = c - 1 - 28
        print(f"\n--- c={c}, R=14, k=28, L={L}, v_2(c-14)={v2(c-14)} ---", flush=True)
        if L < 0:
            print("  L<0, skip")
            continue
        t1 = time.time()
        try:
            r = d102.fit_Qk_bivar(c, 28, tables)
        except Exception as e:
            print(f"  fit ERROR: {e}")
            continue
        t_fit = time.time() - t1
        if r is None:
            print(f"  fit failed (t={t_fit:.1f}s)")
            continue
        Q_poly, D_fit = r
        Q_val = int(Q_poly.subs({a_sym: 12, b_sym: 14}))
        v2_Q = v2(Q_val) if Q_val != 0 else None
        print(f"  fit ok D={D_fit} in {t_fit:.1f}s", flush=True)
        print(f"  Q_{{28}}(12, 14, {c}) has v_2 = {v2_Q}   (H3 predicts 47)", flush=True)
        if v2_Q == 47:
            print("  ✓ MATCHES H3 carrier-level", flush=True)
        else:
            print(f"  ✗ MISMATCH — H3 predicts 47, got {v2_Q}", flush=True)
        # Save state as we go
        out = {'c': c, 'v2_Q': v2_Q, 'H3_pred': 47, 'match': v2_Q == 47, 't_fit_s': t_fit}
        with open(f'/home/agent/projects/code/2026-08-13-day104-Q28-R14-c{c}.json', 'w') as f:
            json.dump(out, f, indent=2)
        # Stop after first successful result — no need to run all
        break


if __name__ == '__main__':
    main()
