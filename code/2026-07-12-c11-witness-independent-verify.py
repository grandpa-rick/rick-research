"""Day 91 — Independent verification of h_6^{(11)}(1, 2) and H_11(1, 2, 6)
via the three-variable factorization h_k^{(c)}(a,b) = (a+3)_L (b+2)_L Q_k(a, b, c).

This does NOT use the Sym-side extraction pipeline (extract_h_k).
Instead, it uses the c-uniform Q_k polynomials from the catalog.

If the numbers match the witness in code/2026-07-12-c11-witness-hunt.py,
we have two independent derivations of h_k^{(11)}(1, 2) confirming the result.
"""
import json
from math import factorial
from sympy import symbols, sympify

CAT = "/home/agent/projects/code/2026-07-11-Qk-catalog.json"


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def pochhammer(x, n):
    """(x)_n = x (x+1) ... (x + n - 1). (x)_0 = 1."""
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def Cn(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def main():
    print("=" * 80)
    print("Independent verification of h_k^{(11)}(1, 2) via three-var factorization")
    print("=" * 80)
    with open(CAT) as f:
        cat = json.load(f)

    a_s, b_s, c_s = symbols('a b c')
    Q = {}
    for ks, s in cat["Q_k_low_k"].items():
        Q[int(ks)] = sympify(s)
    Q[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])

    c_val = 11
    a, b = 1, 2

    print()
    print(f"Evaluating h_k^{{(11)}}(1, 2) via")
    print(f"  h_k^{{(c)}}(a, b) = (a+3)_L * (b+2)_L * Q_k(a, b, c),  L = c - 1 - k")
    print()

    # From the witness-hunt output:
    hk_extracted = {
        0: 1077105223434240000,
        1: -701074405785600000,
        2: 429408073543680000,
        3: -241175389593600000,
        4: 118023848312832000,
        5: -44034425487360000,
        6: 5573710517760000,
    }

    print(f"{'k':>3s} {'L':>3s} {'(a+3)_L':>10s} {'(b+2)_L':>10s} {'Q_k(1,2,11)':>18s} {'h_k_computed':>22s} {'h_k_extracted':>22s}  match?")
    all_match = True
    for k in range(7):
        L = c_val - 1 - k
        A = pochhammer(a + 3, L)  # (a+3)_L
        B = pochhammer(b + 2, L)  # (b+2)_L
        Qval = int(Q[k].subs({a_s: a, b_s: b, c_s: c_val}))
        hk_comp = A * B * Qval
        hk_ext = hk_extracted[k]
        match = hk_comp == hk_ext
        if not match:
            all_match = False
        print(f"{k:>3d} {L:>3d} {A:>10d} {B:>10d} {Qval:>18d} {hk_comp:>22d} {hk_ext:>22d}  {'YES' if match else 'NO'}")

    print()
    if all_match:
        print("PERFECT MATCH — three-var factorization confirms extraction pipeline.")
    else:
        print("MISMATCH — check factorization or extraction.")

    # Recompute H_11(1, 2, 6) from summed h_k * C(6, k)
    H = sum(hk_extracted[k] * Cn(6, k) for k in range(7))
    print()
    print(f"H_11(1, 2, 6) = sum_{{j=0..6}} h_j(1, 2) * C(6, j)")
    print(f"             = {H}")
    print(f"v_2(H_11(1, 2, 6)) = {v2(abs(H))}")
    print(f"Registry / witness-hunt value: -3017710080000")
    print(f"Match: {H == -3017710080000}")


if __name__ == "__main__":
    main()
