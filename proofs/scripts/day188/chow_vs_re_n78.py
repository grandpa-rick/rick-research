"""Day 188 — Extend Chow-Hikita vs (Re) match to n=7 and n=8.

Reuses the machinery of chow_vs_re_n4.py (rick_X_Pn, hikita_e_coeffs) and
compares e-coefficients [e_lambda] X_{P_n}(q) for n in {7, 8}.

Goal: upgrade Rick's trust on Chow-Hikita <-> (Re) match from `computed` to
`checked-sober` for n=1..8.

Reports for each partition lambda |= n:
  - diff = Rick - Hikita (expected 0)
  - PASS if diff simplifies to 0, else print discrepancy and flag for Rick.
"""

import time
from collections import defaultdict

from sympy import expand, simplify, cancel, Poly, Symbol

# Import machinery from the n=4..6 script; it's in the same directory.
from chow_vs_re_n4 import rick_X_Pn, hikita_e_coeffs

q = Symbol('q')


def compare_n(n):
    print(f"\n=== n = {n} ===")
    t0 = time.time()

    t_rick0 = time.time()
    rick = rick_X_Pn(n)
    t_rick = time.time() - t_rick0

    t_hik0 = time.time()
    hik = hikita_e_coeffs(n)
    t_hik = time.time() - t_hik0

    all_shapes = set(rick.keys()) | set(hik.keys())
    all_ok = True
    mismatches = []
    for lam in sorted(all_shapes, key=lambda p: (-sum(p) if p else 0, p)):
        r_c = expand(rick.get(lam, 0))
        h_c = expand(cancel(hik.get(lam, 0)))
        # Normalize by comparing as sympy expressions.
        diff = simplify(r_c - h_c)
        # Also try Poly comparison to be robust against float coeffs.
        try:
            diff_poly = Poly(r_c - h_c, q)
            if diff_poly.is_zero:
                diff = 0
        except Exception:
            pass
        ok = (diff == 0)
        if not ok:
            all_ok = False
            mismatches.append((lam, r_c, h_c, diff))
        status = 'OK (diff=0)' if ok else 'MISMATCH'
        print(f"  e_{lam}:   diff = {diff}   [{status}]")

    t_total = time.time() - t0
    print(f"\n  Rick side:   {t_rick:.2f}s")
    print(f"  Hikita side: {t_hik:.2f}s")
    print(f"  Total n={n}: {t_total:.2f}s")
    print(f"  -> {'ALL MATCH' if all_ok else 'MISMATCH DETECTED'}")

    if not all_ok:
        print("\n  !!! MISMATCHES for Rick to inspect:")
        for lam, r_c, h_c, diff in mismatches:
            print(f"    lambda = {lam}")
            print(f"      Rick   = {r_c}")
            print(f"      Hikita = {h_c}")
            print(f"      diff   = {diff}")

    return all_ok, t_total


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        ns = [int(x) for x in sys.argv[1:]]
    else:
        ns = [7, 8]

    results = {}
    grand_t0 = time.time()
    for n in ns:
        ok, dt = compare_n(n)
        results[n] = (ok, dt)
    grand_t = time.time() - grand_t0

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for n, (ok, dt) in results.items():
        print(f"  n={n}: {'MATCH' if ok else 'MISMATCH'}  ({dt:.2f}s)")
    print(f"  grand total: {grand_t:.2f}s")

    all_good = all(ok for ok, _ in results.values())
    if all_good:
        print("\n  Trust upgrade: Chow-Hikita <-> (Re) checked-sober on n=1..8")
    else:
        print("\n  Trust upgrade BLOCKED: mismatch detected, see above.")
        sys.exit(1)
