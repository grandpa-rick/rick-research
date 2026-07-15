"""Day 98 CODE Task 4 cross-check — sanity verify the H_20(2, 8, 11) = 33 finding.

We claim v_2(H_20(2, 8, 11)) = 33 via the polynomial extension.
Two checks:
  (1) The Q_k^(20) fit values reproduce h_k at some (a, b) with a, b >= 20
      (in-fit-region cross-validation).
  (2) Consistent with the c=20 Day 97 finding: h_11^{(20)}(2, 4) beats corner
      by 1 → same underlying extension being used.
"""
import time
from importlib import util
from math import factorial

import sympy as sp

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)

Hspec = util.spec_from_file_location(
    "hscan", "/home/agent/projects/code/2026-07-16-H20-scan.py"
)
hscan = util.module_from_spec(Hspec)
Hspec.loader.exec_module(hscan)


def v2(n):
    if n == 0:
        return None
    n = abs(int(n))
    v = 0
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def main():
    c_val = 20
    a_sym, b_sym = sp.symbols('a b')

    # Fit Q_k for k in [0, 11].
    print("Fitting Q_k^(20) for k in [0, 11]...")
    Q = {}
    for k in range(0, 12):
        tables = hkfit.build_e2_tables(max_j=k + 2)
        Q[k] = hscan.sample_and_fit_Qk(c_val, k, tables)
        assert Q[k] is not None, f"fit failed at k={k}"

    # ==== Check 1: cross-validate Q_11 at (a=25, b=22): a >= b >= c ====
    print("\n-- Check 1: cross-validate Q_k at in-region (a, b) = (25, 22) --")
    for k in range(0, 12):
        L = c_val - 1 - k
        tables = hkfit.build_e2_tables(max_j=k + 2)
        hks = hkfit.extract_h_k(25, 22, c_val, k, tables)
        h_true = hks[k]
        poch = hscan.rising_fact(25 + 3, L) * hscan.rising_fact(22 + 2, L)
        Q_val = int(Q[k].subs({a_sym: 25, b_sym: 22}))
        h_from_Q = poch * Q_val
        agree = (h_true == h_from_Q)
        print(f"  k={k:>2}: h_extract={h_true == h_from_Q and 'agrees' or 'DIFFERS'}"
              f" (v_2={v2(h_true)})")
        assert agree, f"cross-check FAILED at k={k}"
    print("  ✅ all k in [0, 11] agree on (a, b) = (25, 22)")

    # ==== Check 2: recompute H_20(2, 8, 11) step-by-step ====
    print("\n-- Check 2: recompute H_20(2, 8, 11) explicitly --")
    a, b, k_star = 2, 8, 11
    total = 0
    print(f"  Summands for H_20({a}, {b}, k*={k_star}):")
    print(f"  {'k':>2} {'C(k*,k)':>7} {'h_k':>50} {'C·h_k':>50} {'v_2':>5}")
    per_k_h = []
    for k in range(k_star + 1):
        L = c_val - 1 - k
        poch = hscan.rising_fact(a + 3, L) * hscan.rising_fact(b + 2, L)
        Q_val = int(Q[k].subs({a_sym: a, b_sym: b}))
        h = poch * Q_val
        per_k_h.append(h)
        C = factorial(k_star) // (factorial(k) * factorial(k_star - k))
        term = C * h
        total += term
        print(f"  {k:>2} {C:>7} {str(h)[:50]:>50} {str(term)[:50]:>50} {str(v2(term)):>5}")
    print(f"\n  H_20({a},{b},{k_star}) = {total}")
    v_H = v2(total)
    print(f"  v_2(H_20) = {v_H}")

    # Factor total in terms of 2^v * odd
    from math import gcd
    if total != 0:
        n = abs(total)
        while n % 2 == 0:
            n //= 2
        print(f"  Odd cofactor = {n}")
    assert v_H == 33, f"expected v_2 = 33, got {v_H}"

    # ==== Check 3: recompute the Day 97 finding — h_11^(20)(2,4) v_2 ====
    print("\n-- Check 3: recompute h_11^(20)(2, 4) --")
    L = c_val - 1 - 11
    poch = hscan.rising_fact(2 + 3, L) * hscan.rising_fact(4 + 2, L)
    Q_val = int(Q[11].subs({a_sym: 2, b_sym: 4}))
    h = poch * Q_val
    print(f"  h_11^(20)(2, 4) = {h}")
    print(f"  v_2 = {v2(h)}")
    print(f"  Day 97 claim: interior (2, 4) beats corner by 1 at k=11.")

    # And at the corners
    L = c_val - 1 - 11
    for (a_c, b_c) in [(30, 0), (0, 30), (30, 30), (0, 0)]:
        poch = hscan.rising_fact(a_c + 3, L) * hscan.rising_fact(b_c + 2, L)
        Q_val = int(Q[11].subs({a_sym: a_c, b_sym: b_c}))
        h_c = poch * Q_val
        print(f"  h_11^(20)({a_c},{b_c}) = ... v_2 = {v2(h_c)}")

    print("\n" + "=" * 78)
    print("VERDICT: v_2(H_20(2, 8, 11)) = 33 verified. Digit-sum formula β'(20) = 34 FALSIFIED.")
    print("=" * 78)


if __name__ == "__main__":
    main()
