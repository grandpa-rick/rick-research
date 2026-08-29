"""Day 91 — Test D2' at c = 12, 15, 17 via witness scans using the Q_k catalog.

At c=15 (odd), D2' predicts beta'(15) = 21.
At c=17 (odd, ~1 mod 8), D2' predicts beta'(17) = 23.
At c=12 (even), D2' predicts beta'(12) = 19.

Compute h_k^{(c)}(a, b) for k = 0..6 (catalog range) via three-var factorization
and find min v_2 over reasonable shell. If min < D2' prediction, D2' is falsified.
"""
import json
from math import factorial
from sympy import symbols, sympify

with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
    cat = json.load(f)
a_s, b_s, c_s = symbols('a b c')
Q = {}
for ks, s in cat["Q_k_low_k"].items():
    Q[int(ks)] = sympify(s)
Q[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])


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
    return factorial(n) // (factorial(k) * factorial(n - k)) if 0 <= k <= n else 0


def compute_hk(a, b, c, k):
    L = c - 1 - k
    A = pochhammer(a + 3, L)
    B = pochhammer(b + 2, L)
    Qval = int(Q[k].subs({a_s: a, b_s: b, c_s: c}))
    return A * B * Qval


def compute_H_c(a, b, j, c, kmax=6):
    """H_c(a, b, j) = sum_{k=0..min(j, kmax)} h_k^{(c)}(a, b) * C(j, k)."""
    total = 0
    for k in range(min(j, kmax) + 1):
        total += compute_hk(a, b, c, k) * Cn(j, k)
    return total


def scan_c(c_val, N=30, target=None, label=""):
    print(f"\n{'='*72}")
    print(f"c = {c_val}   {label}    D2' predicts beta'({c_val}) = {target}")
    print(f"{'='*72}")

    # Per-k min v_2
    print(f"\nPer-k min v_2(h_k^{{(c={c_val})}}) in [0, {N})^2, a+b~{c_val%2}:")
    min_v_per_k = {}
    for k in range(7):
        m = float('inf')
        ach = None
        for a in range(N):
            for b in range(N):
                if (a + b) % 2 != c_val % 2:
                    continue
                hk = compute_hk(a, b, c_val, k)
                if hk == 0:
                    continue
                v = v2(abs(hk))
                if v < m:
                    m = v
                    ach = (a, b)
        min_v_per_k[k] = (m, ach)
        print(f"  k={k}: min v_2 = {m}   at {ach}")

    # H_c scan for j up to 6
    print(f"\nMin v_2(H_{c_val}(a, b, j)) scan in [0, {N})^2 for j in [0, 6]:")
    global_min = float('inf')
    global_at = None
    for j in range(7):
        best_v = float('inf')
        best_ab = None
        for a in range(N):
            for b in range(N):
                if (a + b) % 2 != c_val % 2:
                    continue
                Hc = compute_H_c(a, b, j, c_val)
                if Hc == 0:
                    continue
                v = v2(abs(Hc))
                if v < best_v:
                    best_v = v
                    best_ab = (a, b)
        if best_v < global_min:
            global_min = best_v
            global_at = (best_ab, j)
        print(f"  j={j}: min v_2 = {best_v}   at {best_ab}")

    print(f"\n{'-'*72}")
    print(f"Global min v_2(H_{c_val}(a, b, j)) for j <= 6 = {global_min}")
    if target is not None:
        if global_min < target:
            print(f"  beta'({c_val}) <= {global_min} < {target}: D2' FALSIFIED at c={c_val}")
        elif global_min == target:
            print(f"  matches D2' prediction (upper bound of D2''s value)")
        else:
            print(f"  scan bound {global_min} > D2' target — need scan wider OR check j > 6")
    return global_min


def main():
    # c=12 (even). D2' predicts beta'(12)=19.
    scan_c(12, N=64, target=19, label="(even, ~4 mod 8)")

    # c=13 (odd, 5 mod 8). D2' predicts 18.
    scan_c(13, N=64, target=18, label="(odd, ~5 mod 8)")

    # c=15 (odd, 7 mod 8). D2' predicts 21.
    scan_c(15, N=64, target=21, label="(odd, ~7 mod 8)")

    # c=17 (odd, 1 mod 8). D2' predicts 23.
    scan_c(17, N=64, target=23, label="(odd, ~1 mod 8)")


if __name__ == "__main__":
    main()
