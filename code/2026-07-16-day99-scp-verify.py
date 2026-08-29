"""Day 99 G1 — verify SCP single-carrier proof formulas.

Closed forms derived structurally (via AMM + Q_k catalog at (0, 2)):

  v_2(h_0(0, 2, c=4m+2)) = 8m + 3 - s_2(m) - s_2(m+1)
  v_2(h_1(0, 2, c=4m+2)) = 8m + 1 - 2·s_2(m)
  v_2(h_2(0, 2, c=4m+2)) = v_2(Q_2) + 8m - 1 - 2·s_2(m)
  v_2(h_3(0, 2, c=4m+2)) = v_2(Q_3) + 8m - 2 - 2·s_2(m)
  v_2(h_4(0, 2, c=4m+2)) = 8m + 1 - 2·s_2(m) - v_2(m)   [Day 98]

where
  v_2(Q_2(0, 2, 4m+2)) = 3 + v_2(P_2(m)),  P_2(m) = 16m^3 + 8m^2 + m - 3
  v_2(Q_3(0, 2, 4m+2)) = 5 + v_2(m) + v_2(P_3(m)),  P_3(m) = 16m^3 - m - 9

C(4, k) prefactor v_2: (0, 2, 1, 2, 0) for k = 0..4.

Deltas: v_2(C(4,k) h_k) - v_2(h_4)
  Δ_0 = 1 + v_2(m) + v_2(m+1)
  Δ_1 = 2 + v_2(m)
  Δ_2 = v_2(Q_2) + v_2(m) - 1
       = 2 + v_2(m)  if m even (v_2(Q_2) = 3)
       ≥ 3           if m odd  (v_2(m)=0, v_2(Q_2) ≥ 4)
  Δ_3 = v_2(Q_3) + v_2(m) - 1
       = 4 + 2·v_2(m)  if m even (v_2(Q_3) = 5 + v_2(m))
       ≥ 5             if m odd  (v_2(m)=0, v_2(Q_3) ≥ 6)

All Δ_k > 0 for m ≥ 1, so k = 4 is unique minimizer.

This script verifies these formulas directly against the true h_k values.
"""
import json
from sympy import symbols, sympify, expand, factor
from math import comb

CATALOG_PATH = "/home/agent/projects/code/2026-07-11-Qk-catalog.json"


def v2(n):
    n = int(n)
    if n == 0:
        return None
    n = abs(n)
    v = 0
    while (n & 1) == 0:
        n >>= 1
        v += 1
    return v


def s2(n):
    n = int(n)
    v = 0
    while n:
        v += n & 1
        n >>= 1
    return v


def poch(a, L):
    """Pochhammer (a)_L = a * (a+1) * ... * (a + L - 1)."""
    p = 1
    for i in range(L):
        p *= (a + i)
    return p


def h_k(a, b, c, k):
    """Compute h_k^{(c)}(a, b) via three-variable factorisation."""
    L = c - 1 - k
    if L < 0:
        return 0
    return poch(a + 3, L) * poch(b + 2, L) * Q_at(k, a, b, c)


def load_catalog():
    with open(CATALOG_PATH) as f:
        cat = json.load(f)
    Q_sym = {}
    for k in range(6):
        Q_sym[k] = sympify(cat['Q_k_low_k'][str(k)])
    Q_sym[6] = sympify(cat['Q_k_extended']['6']['poly_expanded'])
    return Q_sym


A, B, C = symbols('a b c')
Q_SYM = load_catalog()


def Q_at(k, a_val, b_val, c_val):
    return int(Q_SYM[k].subs({A: a_val, B: b_val, C: c_val}))


def v2_h0_pred(m):
    return 8*m + 3 - s2(m) - s2(m+1)


def v2_h1_pred(m):
    return 8*m + 1 - 2*s2(m)


def v2_Q2_pred(m):
    return 3 + v2(16*m**3 + 8*m**2 + m - 3)


def v2_h2_pred(m):
    return v2_Q2_pred(m) + 8*m - 1 - 2*s2(m)


def v2_Q3_pred(m):
    return 5 + v2(m) + v2(16*m**3 - m - 9)


def v2_h3_pred(m):
    return v2_Q3_pred(m) + 8*m - 2 - 2*s2(m)


def v2_h4_pred(m):
    return 8*m + 1 - 2*s2(m) - v2(m)


def main():
    print("=" * 78)
    print("Day 99 G1 verification: closed forms for v_2(h_k(0, 2, 4m+2)), k=0..4")
    print("=" * 78)
    print(f"{'m':>3} | {'c':>3} | {'k':>2} | {'v2(hk) actual':>14} | {'predicted':>10} | ok")
    print("-" * 78)
    fail = 0
    total = 0
    for m in range(1, 51):
        c = 4*m + 2
        for k, pred_fn in [(0, v2_h0_pred), (1, v2_h1_pred),
                           (2, v2_h2_pred), (3, v2_h3_pred),
                           (4, v2_h4_pred)]:
            actual = v2(h_k(0, 2, c, k))
            pred = pred_fn(m)
            ok = "OK" if actual == pred else "FAIL"
            if actual != pred:
                fail += 1
                print(f"{m:>3} | {c:>3} | {k:>2} | {str(actual):>14} | {pred:>10} | {ok}")
            total += 1
        # spot-report every 5 m
        if m in (1, 4, 7, 15, 32):
            print(f"--- m={m}, c={c}: h_0={v2(h_k(0,2,c,0))}, h_1={v2(h_k(0,2,c,1))},"
                  f" h_2={v2(h_k(0,2,c,2))}, h_3={v2(h_k(0,2,c,3))}, h_4={v2(h_k(0,2,c,4))}")
    print(f"\nTotal checks: {total}, Failures: {fail}")

    print("\n" + "=" * 78)
    print("Delta check: v_2(C(4,k) * h_k) - v_2(h_4) for k = 0, 1, 2, 3")
    print("=" * 78)
    print(f"{'m':>3} | {'c':>3} | {'D_0':>4} | {'D_1':>4} | {'D_2':>4} | {'D_3':>4}"
          f" | {'D0_pred':>7} | {'D1_pred':>7} | {'D2_pred':>7} | {'D3_pred':>7} | ok")
    print("-" * 100)
    fail2 = 0
    total2 = 0
    for m in range(1, 51):
        c = 4*m + 2
        v_h4 = v2(h_k(0, 2, c, 4))
        D = []
        Dpred = []
        for k in range(4):
            v_hk = v2(h_k(0, 2, c, k))
            D.append(v2(comb(4, k)) + v_hk - v_h4)
        # Predictions
        Dpred = [
            1 + v2(m) + v2(m+1),
            2 + v2(m),
            v2_Q2_pred(m) + v2(m) - 1,
            v2_Q3_pred(m) + v2(m) - 1,
        ]
        ok = all(D[k] == Dpred[k] for k in range(4)) and all(d > 0 for d in D)
        if not ok:
            fail2 += 1
            print(f"{m:>3} | {c:>3} | {D[0]:>4} | {D[1]:>4} | {D[2]:>4} | {D[3]:>4}"
                  f" | {Dpred[0]:>7} | {Dpred[1]:>7} | {Dpred[2]:>7} | {Dpred[3]:>7} | FAIL")
        total2 += 1
        if m <= 8 or m in (10, 15, 20, 32, 50):
            print(f"{m:>3} | {c:>3} | {D[0]:>4} | {D[1]:>4} | {D[2]:>4} | {D[3]:>4}"
                  f" | {Dpred[0]:>7} | {Dpred[1]:>7} | {Dpred[2]:>7} | {Dpred[3]:>7} | OK")
    print(f"\nTotal delta checks: {total2}, Failures: {fail2}")

    # Sanity check: all deltas > 0
    print("\n" + "=" * 78)
    print("min Δ_k over m = 1..50:")
    print("=" * 78)
    min_D = [None, None, None, None]
    for m in range(1, 51):
        c = 4*m + 2
        v_h4 = v2(h_k(0, 2, c, 4))
        for k in range(4):
            v_hk = v2(h_k(0, 2, c, k))
            D = v2(comb(4, k)) + v_hk - v_h4
            if min_D[k] is None or D < min_D[k]:
                min_D[k] = D
    for k in range(4):
        print(f"  min Δ_{k} = {min_D[k]}  ({'STRICT>0' if min_D[k] > 0 else 'FAIL'})")


if __name__ == '__main__':
    main()
