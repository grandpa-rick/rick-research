"""Day 98 PROVE — Structural derivation of D at anchor (0, 2) for c ≡ 2 mod 8.

Claim: For c = 8n + 2 (n ≥ 1), v_2(Q_4(0, 2, c)) = 5 CONSTANT, via:
    - c(c-1) has v_2 = 1
    - R_4(c) := c^6 - 15c^5 + 91c^4 - 357c^3 + 988c^2 - 1572c + 1152
      satisfies R_4(8n+2) ≡ 16 mod 32, so v_2 = 4.
    - Sum: 5.

Then v_2(h_4(0, 2, c)) = v_2((3)_{c-5}) + v_2((4)_{c-5}) + 5, and closed form
    v_2(h_4(0, 2, c)) = β(c) - (s_2(m) + v_2(m)), m = (c-2)/4.

D_anchor(c) = s_2(m) + v_2(m). Kummer identity gives s_2(m-1) = s_2(m) - 1 + v_2(m),
so s_2(m) + v_2(m) = 1 + s_2(m-1). This matches empirical D(c).
"""
import json
from sympy import symbols, sympify, expand, Poly, simplify


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


def beta(c):
    return 2 * (c - 1) - s2(c - 1)


# --------------------------------------------------------------------------
# STEP 1: Confirm v_2(Q_4(0, 2, c)) = 5 for c ≡ 2 mod 8 via modular reduction.
# --------------------------------------------------------------------------

def check_R4_mod32():
    """Symbolic: reduce R_4(8n + 2) mod 32."""
    c, n = symbols('c n', integer=True)
    R4 = c**6 - 15*c**5 + 91*c**4 - 357*c**3 + 988*c**2 - 1572*c + 1152
    R4_sub = R4.subs(c, 8*n + 2)
    R4_exp = expand(R4_sub)

    print("R_4(c) = c^6 - 15c^5 + 91c^4 - 357c^3 + 988c^2 - 1572c + 1152")
    print(f"R_4(8n + 2) expanded:")
    print(f"  {R4_exp}")

    # Compute each coefficient mod 32.
    poly = Poly(R4_exp, n)
    print(f"\nCoefficients (n-power → coefficient, and coefficient mod 32):")
    for deg, coef in enumerate(poly.all_coeffs()[::-1]):
        cm = coef % 32
        print(f"  n^{deg}: {coef}   (mod 32 = {cm})")

    # All coefficients mod 32:
    all_c = [int(coef) % 32 for coef in poly.all_coeffs()[::-1]]
    print(f"\nR_4(8n+2) mod 32: sum of {all_c[0]} + " +
          " + ".join(f"{c}·n^{d}" for d, c in enumerate(all_c) if d > 0))

    # If all coefficients except constant term are ≡ 0 mod 32, R_4(8n+2) ≡ constant mod 32.
    non_const_zero = all(c == 0 for c in all_c[1:])
    print(f"\nAll n-power coeffs (except constant) are ≡ 0 mod 32? {non_const_zero}")
    print(f"Constant term (n^0) mod 32 = {all_c[0]}")
    if all_c[0] == 16:
        print(f"\n**PROVED**: R_4(8n+2) ≡ 16 mod 32 for all integer n.")
        print(f"           Hence v_2(R_4(8n+2)) = 4 exactly.")
        return True
    return False


def check_v2_Q4_02():
    """Numeric check for c = 10, 18, ..., 130."""
    print("\n" + "=" * 78)
    print("Numeric verification: v_2(Q_4(0, 2, c)) for c ≡ 2 mod 8")
    print("=" * 78)
    for n in range(1, 17):
        c_val = 8 * n + 2
        # Q_4(0, 2, c) = c(c-1) · R_4(c)
        c1 = c_val
        c2 = c_val - 1
        R4_c = (c_val**6 - 15*c_val**5 + 91*c_val**4 - 357*c_val**3
                + 988*c_val**2 - 1572*c_val + 1152)
        Q4 = c1 * c2 * R4_c
        print(f"  n={n:>2}, c={c_val:>3}: v_2(c(c-1))={v2(c1*c2)}, "
              f"v_2(R_4(c))={v2(R4_c)}, v_2(Q_4(0,2,c))={v2(Q4)}")


# --------------------------------------------------------------------------
# STEP 2: Assemble v_2(h_4(0, 2, c)) closed form via AMM.
# --------------------------------------------------------------------------

def check_h4_02_formula():
    """For c = 4m+2 with m even, verify:
        v_2(h_4(0, 2, c)) = 8m + 1 - 2·s_2(m) - v_2(m).
    """
    print("\n" + "=" * 78)
    print("Numeric check: v_2(h_4(0, 2, c)) vs formula 8m + 1 - 2·s_2(m) - v_2(m)")
    print("=" * 78)
    all_match = True
    for n in range(1, 17):
        c_val = 8 * n + 2
        m = 2 * n
        # Direct: h_4(0, 2, c) = (3)_{c-5} * (4)_{c-5} * Q_4(0, 2, c)
        L = c_val - 5
        p1 = rising(3, L)
        p2 = rising(4, L)
        R4_c = (c_val**6 - 15*c_val**5 + 91*c_val**4 - 357*c_val**3
                + 988*c_val**2 - 1572*c_val + 1152)
        Q4 = c_val * (c_val - 1) * R4_c
        h4 = p1 * p2 * Q4
        v_actual = v2(h4)
        v_formula = 8*m + 1 - 2*s2(m) - v2(m)
        match = "✓" if v_actual == v_formula else "✗"
        print(f"  n={n:>2}, c={c_val:>3}, m={m:>2}: v_2(h_4)={v_actual}, "
              f"formula={v_formula} {match}")
        if v_actual != v_formula:
            all_match = False
    return all_match


def check_Danchor_formula():
    """For c ≡ 2 mod 8, verify D_anchor(c) = s_2(m) + v_2(m) = 1 + s_2(m-1)."""
    print("\n" + "=" * 78)
    print("Numeric check: D_anchor = s_2(m) + v_2(m) = 1 + s_2(m-1)")
    print("=" * 78)
    all_match = True
    for n in range(1, 17):
        c_val = 8 * n + 2
        m = 2 * n
        L = c_val - 5
        p1 = rising(3, L)
        p2 = rising(4, L)
        R4_c = (c_val**6 - 15*c_val**5 + 91*c_val**4 - 357*c_val**3
                + 988*c_val**2 - 1572*c_val + 1152)
        Q4 = c_val * (c_val - 1) * R4_c
        h4 = p1 * p2 * Q4
        v_h4 = v2(h4)
        D_ub = beta(c_val) - v_h4
        D_pred = 1 + s2(m - 1)
        D_form1 = s2(m) + v2(m)
        line = f"  n={n:>2}, c={c_val:>3}, m={m:>2}: D_anchor={D_ub}, "
        line += f"s_2(m)+v_2(m)={D_form1}, 1+s_2(m-1)={D_pred}"
        if D_ub == D_form1 == D_pred:
            line += "  ✓"
        else:
            line += "  ✗"
            all_match = False
        print(line)
    return all_match


def main():
    print("=" * 78)
    print("Day 98 PROVE — Structural derivation at anchor (0, 2), c ≡ 2 mod 8")
    print("=" * 78)

    print("\n### Step 1: R_4(8n+2) mod 32 modular reduction ###\n")
    ok1 = check_R4_mod32()
    check_v2_Q4_02()

    print("\n### Step 2: v_2(h_4(0, 2, c)) closed form ###")
    ok2 = check_h4_02_formula()

    print("\n### Step 3: D_anchor = s_2(m) + v_2(m) = 1 + s_2(m-1) ###")
    ok3 = check_Danchor_formula()

    print("\n" + "=" * 78)
    print(f"All three checks passed: {ok1 and ok2 and ok3}")
    print("=" * 78)

    # Also sanity check at c ≡ 6 mod 8 (m odd) — should NOT match D_pred formula
    # because that formula is for c ≡ 2 mod 8.
    print("\n\n### Sanity: c ≡ 6 mod 8 (m odd) ###")
    print("Expect: our (0, 2) anchor may or may not match D_pred, which is 1 + s_2(m-1)")
    print("        but m odd → 1 + s_2(m-1) is different arithmetic; formula may differ")
    for c_val in [6, 14, 22, 30, 38, 46, 54, 62, 70]:
        m = (c_val - 2) // 4
        if m < 1:
            continue
        L = c_val - 5
        if L < 0:
            continue
        p1 = rising(3, L)
        p2 = rising(4, L)
        R4_c = (c_val**6 - 15*c_val**5 + 91*c_val**4 - 357*c_val**3
                + 988*c_val**2 - 1572*c_val + 1152)
        Q4 = c_val * (c_val - 1) * R4_c
        h4 = p1 * p2 * Q4
        v_h4 = v2(h4)
        D_from_h4 = beta(c_val) - v_h4
        print(f"  c={c_val:>3}, m={m:>2}: v_2(h_4(0,2,{c_val}))={v_h4}, "
              f"β - h_4 = {D_from_h4}, s_2(m)+v_2(m) = {s2(m)+v2(m)}")


if __name__ == '__main__':
    main()
