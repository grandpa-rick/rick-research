"""Day 99 Phase 2 detail — look at (a, b) fixed at (0, 2) and various sweep patterns
for c ∈ {11, 13, 15}, to check the PROVE.md hypothesis that anchor is (0, (c-3)/4).

Also verify (1, 2) at c=11 is really the anchor.
"""
import json
from sympy import symbols, sympify
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


def rising(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= x + i
    return p


A, B, C = symbols('a b c')
with open(CATALOG_PATH) as f:
    cat = json.load(f)
Q_SYM = {}
for k in range(6):
    Q_SYM[k] = sympify(cat['Q_k_low_k'][str(k)])
Q_SYM[6] = sympify(cat['Q_k_extended']['6']['poly_expanded'])


def h_k(a_val, b_val, c_val, k):
    if k > 6:
        return None
    L = c_val - 1 - k
    if L < 0:
        return 0
    p1 = rising(a_val + 3, L)
    p2 = rising(b_val + 2, L)
    Qk = int(Q_SYM[k].subs({A: a_val, B: b_val, C: c_val}))
    return p1 * p2 * Qk


def H_c(a_val, b_val, c_val, j):
    total = 0
    for k in range(0, min(j, 6) + 1):
        hk = h_k(a_val, b_val, c_val, k)
        if hk is None:
            return None
        total += comb(j, k) * hk
    if j > 6:
        return None
    return total


def main():
    for c_val in [11, 13]:
        print(f"\n{'=' * 78}")
        print(f"c = {c_val}, β = {2*(c_val-1) - s2(c_val-1)}")
        print(f"{'=' * 78}")

        # PROVE.md hypothesis: anchor at (0, (c-3)/4) with k* = (c-3)/2 + 1
        b_hyp = (c_val - 3) // 4
        k_hyp = (c_val - 3) // 2 + 1
        print(f"\nPROVE.md hypothesis anchor: (a, b) = (0, {b_hyp}), k* = {k_hyp}")

        # H_c at (0, b_hyp) for all j ≤ 6
        print(f"\n  v_2(H_c(0, {b_hyp}, j)) for j = 0..6:")
        for j in range(0, min(k_hyp, 6) + 1):
            Hv = H_c(0, b_hyp, c_val, j)
            if Hv is None or Hv == 0:
                print(f"    j = {j}: N/A")
            else:
                print(f"    j = {j}: v_2 = {v2(Hv)}")

        # Also check (0, 2) — the day 98 anchor at c=11:
        print(f"\n  v_2(H_c(0, 2, j)) at c={c_val}:")
        for j in range(0, 7):
            Hv = H_c(0, 2, c_val, j)
            if Hv is None or Hv == 0:
                print(f"    j = {j}: N/A")
            else:
                print(f"    j = {j}: v_2 = {v2(Hv)}")

        # Check the ACTUAL anchor found
        actual_anchors = {11: (1, 2), 13: (7, 0)}
        if c_val in actual_anchors:
            a_a, b_a = actual_anchors[c_val]
            print(f"\n  ACTUAL anchor found in sweep: (a, b) = ({a_a}, {b_a})")
            print(f"  v_2(H_c({a_a}, {b_a}, j)) for j = 0..6:")
            for j in range(0, 7):
                Hv = H_c(a_a, b_a, c_val, j)
                if Hv is None or Hv == 0:
                    print(f"    j = {j}: N/A")
                else:
                    print(f"    j = {j}: v_2 = {v2(Hv)}")

        # Also try (a = 0, b = 2) exhaustively at c = 11 for k = 0..6
        # to see what the h_k are
        if c_val == 11:
            print(f"\n  h_k(0, 2, 11) breakdown, k = 0..6:")
            for k in range(7):
                hv = h_k(0, 2, c_val, k)
                print(f"    k = {k}: v_2 = {v2(hv) if hv != 0 else '0'}")

            print(f"\n  h_k(1, 2, 11) breakdown, k = 0..6:")
            for k in range(7):
                hv = h_k(1, 2, c_val, k)
                print(f"    k = {k}: v_2 = {v2(hv) if hv != 0 else '0'}")

            # C(6, k) breakdown for (1, 2, j=6):
            print(f"\n  For (a, b, j) = (1, 2, 6), v_2(C(6, k) h_k):")
            for k in range(7):
                hv = h_k(1, 2, c_val, k)
                if hv == 0:
                    print(f"    k = {k}: C=? h=0")
                else:
                    v = v2(comb(6, k) * hv)
                    print(f"    k = {k}: C(6,{k}) = {comb(6,k)}, v_2(C*h_k) = {v}")

        # Sweep to see if the ANCHOR (a, b) satisfies some clean pattern
        # More detailed a-sweep at b=2 for c=11
        if c_val == 11:
            print(f"\n  A-sweep at b=2, j=6, c=11 (a in [0, 31]):")
            for a in range(0, 32):
                Hv = H_c(a, 2, c_val, 6)
                if Hv is not None and Hv != 0:
                    v = v2(Hv)
                    print(f"    a = {a:>2}: v_2(H) = {v}")


if __name__ == '__main__':
    main()
