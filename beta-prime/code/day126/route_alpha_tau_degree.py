"""
Route α — τ-degree preservation under substitution u1 = τ, u2 = y, u3 = c
with y + c = s, y c = τ.

Substitution: u1 → τ, u2 → y, u3 → s - y, then reduce y² → s·y − τ.
Result is polynomial in (τ, s, y) with y-degree < 2.

We define:
    τ-deg(P) = degree in τ of the reduced polynomial substitute_and_reduce(P).

We check (Claim ★):
    τ-deg Ψ(P) = τ-deg P  for all symmetric P.

Steps:
  1. Verify (1,1,2)-weight = τ-deg on e-monomials (should follow from Day 118 note).
  2. Verify Ψ preserves τ-deg on many test polynomials.
  3. Additionally: test whether T (not divided by V) preserves τ-deg for
     non-symmetric polynomials, which would give a cleaner statement.
"""

import sys
from sympy import symbols, expand, Poly, Integer, Rational, prod, degree

u1, u2, u3 = symbols('u1 u2 u3')
tau, s, y = symbols('tau s y')

V = (u1 - u2) * (u1 - u3) * (u2 - u3)
e1_expr = u1 + u2 + u3
e2_expr = u1*u2 + u1*u3 + u2*u3
e3_expr = u1*u2*u3


def falling(x, k):
    if k == 0:
        return Integer(1)
    return prod([x - i for i in range(k)])


def T_op(poly):
    poly = expand(poly)
    if poly == 0:
        return Integer(0)
    p = Poly(poly, u1, u2, u3)
    result = Integer(0)
    for monom, coeff in p.as_dict().items():
        a, b, c = monom
        result += coeff * falling(u1, a) * falling(u2, b) * falling(u3, c)
    return expand(result)


def Psi(f):
    """f is symmetric in u1,u2,u3; returns a symmetric polynomial."""
    numer = expand(T_op(expand(f * V)))
    q, r = Poly(numer, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise ValueError(f"Division by V failed! remainder = {r.as_expr()}")
    return q.as_expr()


def substitute_and_reduce(poly):
    """Substitute u1 = τ, u2 = y, u3 = s - y, then reduce y^k for k ≥ 2 using
    y² = s·y − τ.  Returns a polynomial in (τ, s, y) with y-deg < 2.
    """
    expr = expand(poly.subs([(u1, tau), (u2, y), (u3, s - y)]))
    # Reduce y^k iteratively
    while True:
        p = Poly(expr, y)
        if p.degree() < 2:
            break
        # replace highest power of y using y² = s·y − τ
        d = p.degree()
        lc = p.LC()  # polynomial in tau, s
        # y^d = y^(d-2) * (s·y − τ)
        replacement = lc * y**(d - 2) * (s * y - tau)
        expr = expand(expr - lc * y**d + replacement)
    return expand(expr)


def tau_degree(poly):
    """τ-degree of a polynomial in u1, u2, u3 after substitution+reduction."""
    reduced = substitute_and_reduce(poly)
    if reduced == 0:
        return -1
    return Poly(reduced, tau).degree()


def weight_e(monomial_exps):
    """Weight of e_1^a1 e_2^a2 e_3^a3."""
    a1, a2, a3 = monomial_exps
    return a1 + a2 + 2 * a3


def e_monomial(a1, a2, a3):
    return e1_expr**a1 * e2_expr**a2 * e3_expr**a3


# ============================================================
# Step 1: Verify weight = τ-deg on e-monomials  (Day 118 result)
# ============================================================

def step1_weight_vs_tau_deg():
    print("=" * 70)
    print("STEP 1: Verify (1,1,2)-weight = τ-deg on e-monomials")
    print("=" * 70)
    monomials = []
    for W in range(0, 7):
        for a1 in range(W + 1):
            for a2 in range(W - a1 + 1):
                # a1 + a2 + 2*a3 = W  =>  a3 = (W - a1 - a2)/2
                rem = W - a1 - a2
                if rem >= 0 and rem % 2 == 0:
                    a3 = rem // 2
                    monomials.append((a1, a2, a3))
    passed = 0
    failed = 0
    for (a1, a2, a3) in monomials:
        f = e_monomial(a1, a2, a3)
        td = tau_degree(f)
        w = weight_e((a1, a2, a3))
        status = "OK" if td == w else "FAIL"
        if td == w:
            passed += 1
        else:
            failed += 1
            print(f"  e1^{a1} e2^{a2} e3^{a3}: w={w}, τ-deg={td}  [{status}]")
    print(f"  {passed} passed, {failed} failed out of {len(monomials)} monomials")
    print()
    return failed == 0


# ============================================================
# Step 2: Test Claim ★ : τ-deg Ψ(P) = τ-deg P for symmetric P
# ============================================================

def step2_claim_star():
    print("=" * 70)
    print("STEP 2: Claim ★ — τ-deg Ψ(P) = τ-deg P on symmetric polynomials")
    print("=" * 70)

    test_polys = []

    # simple e-monomials
    for (a1, a2, a3), name in [
        ((1, 0, 0), "e1"),
        ((0, 1, 0), "e2"),
        ((0, 0, 1), "e3"),
        ((2, 0, 0), "e1²"),
        ((1, 1, 0), "e1·e2"),
        ((1, 0, 1), "e1·e3"),
        ((0, 1, 1), "e2·e3"),
        ((0, 2, 0), "e2²"),
        ((0, 3, 0), "e2³"),
        ((1, 2, 0), "e1·e2²"),
        ((0, 2, 1), "e2²·e3"),
        ((0, 4, 0), "e2⁴"),
        ((0, 5, 0), "e2⁵"),
        ((0, 6, 0), "e2⁶"),
        ((0, 0, 2), "e3²"),
        ((2, 2, 0), "e1²·e2²"),
        ((0, 1, 2), "e2·e3²"),
        ((1, 1, 1), "e1·e2·e3"),
        ((3, 0, 0), "e1³"),
        ((2, 1, 0), "e1²·e2"),
        ((0, 3, 1), "e2³·e3"),
    ]:
        test_polys.append((name, e_monomial(a1, a2, a3), weight_e((a1, a2, a3))))

    # also sums (non-monomial symmetric)
    test_polys.append(("e1 + e2", e1_expr + e2_expr, 1))
    test_polys.append(("e1 + e3", e1_expr + e3_expr, 2))
    test_polys.append(("e2² + e3", e2_expr**2 + e3_expr, 2))
    test_polys.append(("e1·e2 + e3", e1_expr*e2_expr + e3_expr, 2))

    print(f"{'polynomial':<20}  {'τ-deg(P)':>10}  {'τ-deg Ψ(P)':>12}  status")
    print("-" * 70)
    passed = 0
    failed = 0
    failures = []
    for name, P, expected_w in test_polys:
        td_P = tau_degree(P)
        PsiP = Psi(P)
        td_PsiP = tau_degree(PsiP)
        # For sums, the τ-deg is max of τ-degs, which equals the weight if no
        # cancellation of the top piece
        equal = (td_P == td_PsiP)
        weight_check = (td_P == expected_w) if isinstance(expected_w, int) else True
        status = "OK" if equal else "FAIL"
        if equal:
            passed += 1
        else:
            failed += 1
            failures.append((name, td_P, td_PsiP))
        print(f"{name:<20}  {td_P:>10}  {td_PsiP:>12}  {status}"
              + (f" (expected w={expected_w})" if not weight_check else ""))
    print()
    print(f"Total: {passed} passed, {failed} failed out of {len(test_polys)}")
    if failures:
        print("FAILURES:", failures)
    print()
    return failed == 0


# ============================================================
# Step 3: Test if T alone preserves τ-deg on non-symmetric input
# ============================================================

def step3_T_alone():
    print("=" * 70)
    print("STEP 3: Does T preserve τ-deg on ARBITRARY (non-symmetric) monomials?")
    print("=" * 70)
    print("For each u-monomial u1^a u2^b u3^c, compare τ-deg of original vs. T(...)")
    print()
    passed = 0
    failed = 0
    fails = []
    for a in range(4):
        for b in range(4):
            for c in range(4):
                if a + b + c == 0:
                    continue
                mono = u1**a * u2**b * u3**c
                td_orig = tau_degree(mono)
                td_T = tau_degree(T_op(mono))
                if td_orig == td_T:
                    passed += 1
                else:
                    failed += 1
                    fails.append(((a, b, c), td_orig, td_T))
    print(f"Total: {passed} passed, {failed} failed out of {passed + failed}")
    if fails:
        print("First 10 failures:")
        for (exps, td1, td2) in fails[:10]:
            print(f"  u1^{exps[0]} u2^{exps[1]} u3^{exps[2]}: τ-deg orig={td1}, τ-deg T={td2}")
    print()
    return failed == 0


# ============================================================
# Step 4: Check τ-deg of Ψ(e_2^b) up to large b, and compare to b
# ============================================================

def step4_e2_powers():
    print("=" * 70)
    print("STEP 4: Ψ(e_2^b) for b = 1..8 — τ-deg check")
    print("=" * 70)
    for b in range(1, 9):
        f = e2_expr**b
        td_P = tau_degree(f)
        try:
            PsiP = Psi(f)
        except Exception as ex:
            print(f"  b={b}: Ψ failed: {ex}")
            continue
        td_PsiP = tau_degree(PsiP)
        status = "OK" if td_PsiP == b else ("FAIL" if td_PsiP > b else "STRICT<")
        print(f"  b={b}: τ-deg(e_2^b) = {td_P}, τ-deg Ψ(e_2^b) = {td_PsiP}  [{status}]")
    print()


# ============================================================
# Step 5: Look at leading tau-terms to understand structure
# ============================================================

def step5_leading_tau_analysis():
    print("=" * 70)
    print("STEP 5: Leading τ-coefficient analysis")
    print("=" * 70)
    print("For P = e_2^b:")
    for b in range(1, 6):
        f = e2_expr**b
        PsiP = Psi(f)
        red_P = substitute_and_reduce(f)
        red_PsiP = substitute_and_reduce(PsiP)
        p_P = Poly(red_P, tau)
        p_PsiP = Poly(red_PsiP, tau)
        lead_P = p_P.LC()
        lead_PsiP = p_PsiP.LC() if p_PsiP.degree() >= 0 else 0
        print(f"  b={b}:")
        print(f"     leading τ-coef of e_2^b (τ-deg {p_P.degree()}):        {expand(lead_P)}")
        print(f"     leading τ-coef of Ψ(e_2^b) (τ-deg {p_PsiP.degree()}):  {expand(lead_PsiP)}")
    print()


if __name__ == "__main__":
    ok1 = step1_weight_vs_tau_deg()
    ok2 = step2_claim_star()
    ok3 = step3_T_alone()
    step4_e2_powers()
    step5_leading_tau_analysis()

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Step 1 (weight = τ-deg on e-monomials):     {'PASS' if ok1 else 'FAIL'}")
    print(f"  Step 2 (Claim ★: Ψ preserves τ-deg):        {'PASS' if ok2 else 'FAIL'}")
    print(f"  Step 3 (T preserves τ-deg on non-sym):      {'PASS' if ok3 else 'FAIL'}")
