"""Day 91 — Fast witness computation at c=13 using Q_k catalog (k=0..6).

Compute h_k^{(13)}(a, b) for k = 0..6 via three-var factorization at
Lucas-min-achieving (a, b). Then sum H_13(a, b, k=6) = sum h_j * C(6, j)
and check v_2. If v_2 < D2''s prediction of 18, D2' is (partially) falsified.

Since we don't have Q_k for k = 7..12, we cannot compute H_13(a, b, j) for
j > 6. But we CAN check that h_6^{(13)}(a, b) has v_2 achievable = 16,
which gives beta'(13) <= v_2(H_13(a, b, 6)) IF distinct-min is met with
carrier at k=6 (since h_j contributions for j > 6 would require k >= 7, but
we fix j=6 so they don't appear).

Wait, H_c(a, b, j) = sum_{k=0..j} h_k * C(j, k). So H_13(a, b, 6) only uses
h_0..h_6, all covered by Q_k catalog.
"""
import json
from math import factorial
from sympy import symbols, sympify, expand


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def pochhammer(x, n):
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def Cn(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def main():
    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
        cat = json.load(f)
    a_s, b_s, c_s = symbols('a b c')
    Q = {}
    for ks, s in cat["Q_k_low_k"].items():
        Q[int(ks)] = sympify(s)
    Q[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])

    c_val = 13

    # Find achievers of Delta_6^{(13)} = 8 (from earlier catalog).
    # Lucas-min for L=6: (a+2) & 6 = 0, (b+1) & 6 = 0.
    # Try small (a, b) with a+b odd, a mod 8 in {6, 7}, b mod 8 in {0, 7}.
    L = c_val - 1 - 6
    print(f"c={c_val}, k=6, L={L}, shell parity a+b={c_val%2}")
    print()

    for (a, b) in [(7, 0), (6, 7), (7, 8), (14, 7), (15, 0), (6, 15)]:
        if (a + 2) & L != 0:
            print(f"  ({a},{b}): a+2 & L != 0, skip")
            continue
        if (b + 1) & L != 0:
            print(f"  ({a},{b}): b+1 & L != 0, skip")
            continue
        if (a + b) % 2 != c_val % 2:
            print(f"  ({a},{b}): wrong parity, skip")
            continue

        # Compute h_k^{(13)}(a, b) for k = 0..6 via factorization
        summands = []
        total = 0
        for k in range(7):
            Lk = c_val - 1 - k
            A = pochhammer(a + 3, Lk)
            B = pochhammer(b + 2, Lk)
            Qval = int(Q[k].subs({a_s: a, b_s: b, c_s: c_val}))
            hk = A * B * Qval
            C = Cn(6, k)
            contrib = C * hk
            total += contrib
            summands.append((k, hk, C, contrib))
        v_H = v2(abs(total)) if total else float('inf')
        print(f"\n(a, b)=({a}, {b})   H_13(a, b, 6) = sum_{{j=0..6}} h_j C(6,j) = {total}")
        print(f"   v_2(H_13) = {v_H}")
        for k, hk, C, contrib in summands:
            marker = "  <-- CARRIER k=6" if k == 6 else ""
            print(f"    k={k}: h_k = {hk:>25d}   C(6,k)={C}   v_2(contrib) = {v2(abs(contrib)) if contrib else float('inf')}{marker}")

        # Distinct-min check
        carrier_v = v2(abs(summands[6][3])) if summands[6][3] else float('inf')
        others = [v2(abs(s[3])) if s[3] else float('inf') for i, s in enumerate(summands) if i != 6]
        ok = all(o > carrier_v for o in others)
        print(f"   Distinct-min at k=6? {ok}")
        if ok and v_H < 18:
            print(f"   *** beta'(13) <= {v_H} < 18: D2' FALSIFIED at c=13 ***")
        elif ok and v_H == 18:
            print(f"   *** MATCHES D2' prediction beta'(13)=18 ***")


if __name__ == "__main__":
    main()
