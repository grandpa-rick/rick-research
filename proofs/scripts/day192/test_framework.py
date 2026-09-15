"""Sanity-check the a=3 framework by regressing against known e_1 ⋆ e_r (Thm 3.12)
   and Day 191 e_2 ⋆ e_2 result."""

import sympy as sp
from hikita_star import compute_ea_star_er, print_expansion, q, t


def main():
    # Test 1: e_1 ⋆ e_2 (Thm 3.12): (1-q^{-1})[3]_t e_3 + q^{-1} e_1 e_2 = (1-q^{-1})[3]_t e_3 + q^{-1} e_{2,1}
    print("=" * 72)
    print("TEST 1: e_1 ⋆ e_2 at m=3 (Thm 3.12 check)")
    print("=" * 72)
    exp = compute_ea_star_er(1, 2, 3, verbose=False)
    print_expansion(exp, "e_1 ⋆ e_2 at m=3:")

    expected_e3 = (1 - q**(-1)) * (1 + t + t**2)
    expected_e21 = q**(-1)
    d3 = sp.simplify(exp[(3,)] - expected_e3)
    d21 = sp.simplify(exp[(2, 1)] - expected_e21)
    print(f"\n  diff e_(3,): {d3}")
    print(f"  diff e_(2,1): {d21}")
    assert d3 == 0 and d21 == 0, "Thm 3.12 check failed!"
    print("  Thm 3.12 check PASSED.")

    # Test 2: e_2 ⋆ e_2 at m=4 (Day 191 result)
    print("\n" + "=" * 72)
    print("TEST 2: e_2 ⋆ e_2 at m=4 (Day 191 check)")
    print("=" * 72)
    exp = compute_ea_star_er(2, 2, 4, verbose=False)
    print_expansion(exp, "e_2 ⋆ e_2 at m=4:")

    # Expected:
    exp_e4 = (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**2
    exp_e31 = (q - 1)*(t + 1)/q**2
    exp_e22 = 1/q**2
    d4 = sp.simplify(exp[(4,)] - exp_e4)
    d31 = sp.simplify(exp[(3, 1)] - exp_e31)
    d22 = sp.simplify(exp[(2, 2)] - exp_e22)
    print(f"\n  diff e_(4,): {d4}")
    print(f"  diff e_(3,1): {d31}")
    print(f"  diff e_(2,2): {d22}")
    assert d4 == 0 and d31 == 0 and d22 == 0, "Day 191 check failed!"
    print("  Day 191 check PASSED.")

    # Test 3: a=3 code correctness — sanity check via commutativity of ⋆
    # e_3 ⋆ e_1 should equal e_1 ⋆ e_3 by commutativity (Hikita Prop 3.9).
    # e_1 ⋆ e_3 = (1-q^{-1})[4]_t e_4 + q^{-1} e_1 e_3 = (1-q^{-1})[4]_t e_4 + q^{-1} e_{3,1}
    print("\n" + "=" * 72)
    print("TEST 3: e_3 ⋆ e_1 at m=4 (should equal e_1 ⋆ e_3 by commutativity)")
    print("=" * 72)
    exp = compute_ea_star_er(3, 1, 4, verbose=True)
    print_expansion(exp, "e_3 ⋆ e_1 at m=4:")

    expected_e4 = (1 - q**(-1)) * (1 + t + t**2 + t**3)
    expected_e31 = q**(-1)
    d4 = sp.simplify(exp[(4,)] - expected_e4)
    d31 = sp.simplify(exp[(3, 1)] - expected_e31)
    print(f"\n  diff e_(4,): {d4}")
    print(f"  diff e_(3,1): {d31}")
    zero_others = all(
        sp.simplify(exp.get(lam, 0)) == 0 for lam in [(2, 2), (2, 1, 1), (1, 1, 1, 1)]
    )
    print(f"  Other partitions all zero? {zero_others}")
    assert d4 == 0 and d31 == 0 and zero_others, "e_3 ⋆ e_1 commutativity check failed!"
    print("  Commutativity check PASSED.  a=3 framework is correct.")


if __name__ == "__main__":
    main()
