"""Day 104 (2026-08-13) — Compute Q_{2R}(R-2, R, c) for various c and R.

Purpose: verify Rick's H3 hypothesis ε_R = ⌈log_2(R+2)⌉ structurally.

Plan:
  For R ∈ {6, 10}:
    For a few c ≡ R mod 16 with varied v_2(c-R):
      1. Fit Q_{2R}^{(c)}(a, b) via fit_Qk_bivar.
      2. Evaluate at (a, b) = (R-2, R).
      3. Report v_2(Q_{2R}(R-2, R, c)).
      4. Also compute v_2((R+2)_L), v_2((R+1)_L) — Kummer sanity check.

  KEY TEST: Does v_2(Q_{2R}(R-2, R, c)) = v_2(c - R) + const (const = 0 if H3)?
"""

import json
import time
from importlib import util
from math import comb

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


def s2(n):
    n = abs(int(n))
    v = 0
    while n:
        v += n & 1
        n >>= 1
    return v


def beta(c):
    return 2 * (c - 1) - s2(c - 1)


def delta_c2mod4(c):
    m = (c - 2) // 4
    return s2(m) + v2(m)


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def ceil_log2(n):
    if n <= 1:
        return 0
    k = 0
    p = 1
    while p < n:
        p *= 2
        k += 1
    return k


def poch_v2(base, length):
    if length <= 0:
        return 0
    top = base + length - 1
    bot = base - 1
    return (top - s2(top)) - (bot - s2(bot))


def main():
    print("=" * 78)
    print("Day 104 — Q_{2R}(R-2, R, c) structural probe (via fit_Qk_bivar)")
    print("=" * 78, flush=True)

    K_MAX_GLOBAL = 20
    t0 = time.time()
    tables = hkfit.build_e2_tables(max_j=K_MAX_GLOBAL + 2)
    print(f"build_e2_tables(max_j={K_MAX_GLOBAL + 2}): {time.time() - t0:.1f}s", flush=True)

    a_sym, b_sym = sp.symbols('a b')

    tests = [
        # (label, R, a_val, b_val, k, c_list)
        # R = 6, anchor (4, 6, 12): need Q_{12}^{(c)}(4, 6) at various c ≡ 6 mod 16
        ('R=6', 6, 4, 6, 12, [22, 38, 54, 70, 86, 102, 118, 134, 150, 166, 182, 198, 214, 230, 246, 262]),
        # R = 10, anchor (8, 10, 20): need Q_{20}^{(c)}(8, 10) at various c ≡ 10 mod 16
        ('R=10', 10, 8, 10, 20, [42, 74, 138, 154]),
    ]

    all_results = {}
    for (label, R, a, b, k, c_list) in tests:
        print(f"\n{'='*78}\n{label}: a={a}, b={b}, k={k}\n{'='*78}", flush=True)
        eps_R_H3 = ceil_log2(R + 2)
        print(f"H3 predicts ε_R = ⌈log_2({R+2})⌉ = {eps_R_H3}", flush=True)
        results = []
        for c in c_list:
            L = c - 1 - k
            if L < 0:
                print(f"  c={c}: L={L} < 0, skip")
                continue
            v2_cR = v2(c - R)
            t1 = time.time()
            try:
                r = d102.fit_Qk_bivar(c, k, tables)
            except Exception as e:
                print(f"  c={c}: fit ERROR {e}")
                continue
            if r is None:
                print(f"  c={c}: fit failed (t={time.time()-t1:.1f}s)")
                continue
            Q_poly, D_fit = r
            Q_val = int(Q_poly.subs({a_sym: a, b_sym: b}))
            t_c = time.time() - t1
            v2_Q = v2(Q_val) if Q_val != 0 else None
            v2_Rp1_L = poch_v2(R + 1, L)  # (a+3)_L = (R+1)_L
            v2_Rp2_L = poch_v2(R + 2, L)  # (b+2)_L = (R+2)_L
            h_val = rising_fact(a + 3, L) * rising_fact(b + 2, L) * Q_val
            v2_h = v2(h_val) if h_val != 0 else None
            u_c = beta(c) - delta_c2mod4(c)
            predicted_delta_H3 = max(0, v2_cR - eps_R_H3)
            predicted_v2h = u_c - predicted_delta_H3
            match = (v2_h == predicted_v2h) if v2_h is not None else False
            eff_offset = (v2_Q - v2_cR) if (v2_Q is not None and v2_cR is not None) else None
            row = {
                'c': c, 'v2_c_minus_R': v2_cR,
                'v2_Q': v2_Q, 'v2_Rp1_L': v2_Rp1_L, 'v2_Rp2_L': v2_Rp2_L,
                'v2_h': v2_h, 'u_c': u_c,
                'pred_delta_H3': predicted_delta_H3,
                'pred_v2h': predicted_v2h, 'match': match,
                'v2_Q_minus_v2_cR': eff_offset,
                't_c': round(t_c, 2),
                'D_fit': D_fit,
            }
            results.append(row)
            print(f"  c={c:>3} v_2(c-R)={v2_cR:>2} | v_2(Q)={v2_Q!s:>4} | v_2((R+1)_L)={v2_Rp1_L:>3} v_2((R+2)_L)={v2_Rp2_L:>3} | v_2(h)={v2_h!s:>4} u_c={u_c:>3} predδ_H3={predicted_delta_H3:>2} predv_2h={predicted_v2h:>3} MATCH={match} | v_2(Q)-v_2(c-R)={eff_offset} | t={t_c:.1f}s D={D_fit}", flush=True)
        all_results[label] = results

    outpath = '/home/agent/projects/code/2026-08-13-day104-Qk-anchor-value.json'
    with open(outpath, 'w') as f:
        json.dump({'note': 'Day 104 Q_{2R}(R-2, R, c) probe', 'results': all_results}, f, indent=2, default=str)
    print(f"\nSaved {outpath}")


if __name__ == '__main__':
    main()
