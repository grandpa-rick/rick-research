"""
Lead 1 continued — N_1 ansatz.

MAJOR STRUCTURAL FIND at V=0:
    [T^b] N_1 |_{V=0} = (b² - 1)/b · (U+1)_(b-2)     for b >= 2.

Equivalently: [T^b] N_1 |_{V=0} = (b-1)(b+1)/b · Γ(U+b-1)/Γ(U+1).

At U=V=0: (U+1)_(b-2) → (b-2)!, so [T^b] N_1|_(0,0) = (b-1)(b+1)(b-2)!/b = (b+1)(b-1)!/b. MATCHES.

Now try to fit the full (U, V) form.
Symmetric ansatz candidates:
  (1) A(b)·(U+1)_(b-2)·(V+1)_(b-2)/(b-2)!
  (2) A(b)·(U+V+1)_(b-2)/(1)_(b-2)
  (3) A(b) · (something symmetric extending (U+1)_(b-2) at V=0)

Test each.
"""

from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, simplify, together)

U, V = symbols('U V')

# The data (from lead_bessel.py output)
coefs = {
    2: Rational(3, 2),
    3: 8*(U + V + 1)/3,
    4: (15*U**2 + 43*U*V + 45*U + 15*V**2 + 45*V + 30)/4,
    5: 2*(12*U**3 + 67*U**2*V + 72*U**2 + 67*U*V**2 + 202*U*V + 132*U + 12*V**3 + 72*V**2 + 132*V + 72)/5,
    6: (35*U**4 + 320*U**3*V + 350*U**3 + 624*U**2*V**2 + 1884*U**2*V + 1225*U**2 + 320*U*V**3 + 1884*U*V**2 + 3392*U*V + 1750*U + 35*V**4 + 350*V**3 + 1225*V**2 + 1750*V + 840)/6,
    7: 2*(24*U**5 + 325*U**4*V + 360*U**4 + 1039*U**3*V**2 + 3139*U**3*V + 2040*U**3 + 1039*U**2*V**3 + 6030*U**2*V**2 + 10734*U**2*V + 5400*U**2 + 325*U*V**4 + 3139*U*V**3 + 10734*U*V**2 + 14850*U*V + 6576*U + 24*V**5 + 360*V**4 + 2040*V**3 + 5400*V**2 + 6576*V + 2880)/7,
    8: (63*U**6 + 1183*U**5*V + 1323*U**5 + 5607*U**4*V**2 + 16947*U**4*V + 11025*U**4 + 9195*U**3*V**3 + 52799*U**3*V**2 + 93273*U**3*V + 46305*U**3 + 5607*U**2*V**4 + 52799*U**2*V**3 + 177357*U**2*V**2 + 240625*U**2*V + 102312*U**2 + 1183*U*V**5 + 16947*U*V**4 + 93273*U*V**3 + 240625*U*V**2 + 280728*U*V + 111132*U + 63*V**6 + 1323*V**5 + 11025*V**4 + 46305*V**3 + 102312*V**2 + 111132*V + 45360)/8,
}


def test_ansatz_1(b_max):
    """Ansatz (1): [T^b] N_1 = (b²-1)/(b(b-2)!) · (U+1)_(b-2) · (V+1)_(b-2)"""
    print("Ansatz (1): (b²-1)/(b(b-2)!) · (U+1)_(b-2) · (V+1)_(b-2)")
    for b in range(2, b_max + 1):
        if b == 2:
            pred = Rational(b*b - 1, b)  # 3/2 · 1 · 1 (empty products)
        else:
            pred = Rational(b*b - 1, b * factorial(b-2)) * rf(U+1, b-2) * rf(V+1, b-2)
        actual = coefs.get(b, Integer(0))
        diff = expand(actual - pred)
        print(f"  b={b}: diff = {diff}")


def test_ansatz_2(b_max):
    """Ansatz (2): [T^b] N_1 = (b²-1)/b · (U+V+1)_(b-2)/(b-2)! · normalization"""
    print("\nAnsatz (2): (b²-1)/b · (U+V+1)_(b-2)/(b-2)! ")
    for b in range(2, b_max + 1):
        if b == 2:
            pred = Rational(b*b - 1, b)
        else:
            pred = Rational(b*b - 1, b) * rf(U+V+1, b-2) / factorial(b-2)
        actual = coefs.get(b, Integer(0))
        diff = expand(actual - pred)
        print(f"  b={b}: diff = {diff}")


def test_ansatz_3(b_max):
    """Ansatz (3): Try summed form:
       [T^b] N_1 = (b²-1)/(b·(b-2)!·2) · [(U+1)_(b-2)(V+2)_(b-2) + (U+2)_(b-2)(V+1)_(b-2)] ?
    """
    print("\nAnsatz (3): symmetric mixed form")
    for b in range(2, b_max + 1):
        if b == 2:
            pred = Rational(b*b - 1, b)
        else:
            pred = Rational(b*b - 1, b*factorial(b-2)*2) * (
                rf(U+1, b-2) * rf(V+2, b-2) + rf(U+2, b-2) * rf(V+1, b-2)
            )
        actual = coefs.get(b, Integer(0))
        diff = expand(actual - pred)
        # simplify
        cf = factor(diff) if diff != 0 else 0
        print(f"  b={b}: diff = {cf}")


def test_ansatz_convolution(b_max):
    """
    N_1 = Σ_(b>=2) [T^b] N_1 T^b.
    Note: since deg is b-2 in each of U, V, and (b²-1)/(b(b-2)!) is a nice scalar,
    maybe there's a natural generating function.

    Consider: G(T; U, V) := Σ_(b>=2) (b²-1)/(b(b-2)!) · Q_b(U, V) · T^b
    where Q_b(U, V) is a symmetric poly of degree b-2 in each of U, V, with
    Q_b(U, 0) = (U+1)_(b-2).

    Try Q_b = (U+1)_(b-2) · e^V + symmetric?  No, e^V is not polynomial.

    Alternative: does N_1 = some integrand of Bessel-like functions?
    """
    pass


def analyze_ratio_to_product(b_max):
    """Compute r_b := [T^b] N_1  /  [(U+1)_(b-2)(V+1)_(b-2)/(b-2)!] and see if simpler."""
    print("\nRatio: [T^b] N_1 / [(U+1)_(b-2)(V+1)_(b-2)/(b-2)!]:")
    for b in range(3, b_max + 1):
        c = coefs.get(b, Integer(0))
        denom = rf(U+1, b-2) * rf(V+1, b-2) / factorial(b-2)
        try:
            r = simplify(c / denom)
            print(f"  b={b}:  r = {r}")
            print(f"        factored: {factor(r)}")
        except Exception as e:
            print(f"  b={b}: err {e}")


def analyze_ratio_UV1(b_max):
    """Try dividing by (U+V+1)_(b-2)/(b-2)! to see the residual."""
    print("\nRatio: [T^b] N_1 · b / [(b²-1) · (U+V+1)_(b-2)/(b-2)!]:")
    for b in range(3, b_max + 1):
        c = coefs.get(b, Integer(0))
        denom = Rational(b*b - 1, b*factorial(b-2)) * rf(U+V+1, b-2)
        try:
            r = simplify(c / denom)
            print(f"  b={b}: r = {factor(r)}")
        except Exception as e:
            print(f"  b={b}: err {e}")


def try_two_term_ansatz(b_max):
    """[T^b] N_1 = A(b)·(U+1)_(b-2)(V+1)_(b-2)/(b-2)! + B(b)·other_symmetric_of_degree_b-2

    Note (U+1)_(b-2)(V+1)_(b-2) has degree b-2 in each — matches!
    But its symmetric-poly expansion needs another degree-(b-2, b-2) symmetric term.
    Two natural symmetric bases of degree (b-2, b-2):
      P1 = (U+1)_(b-2) (V+1)_(b-2)
      P2 = Σ (U+a)_(b-2) (V+b')_(b-2) ...

    Test: maybe c_b = alpha_b · P1 + beta_b · S_b where S_b is some elementary sym.
    """
    print("\nTry: [T^b] N_1 = α_b · (U+1)_(b-2)(V+1)_(b-2)/(b-2)! + β_b · [(U+1)_(b-2) + (V+1)_(b-2)]")
    # At V=0: (V+1)_(b-2) = (b-2)!. So P1|_{V=0} = (U+1)_(b-2)·(b-2)!, /(b-2)! = (U+1)_(b-2).
    # 2nd term at V=0: (U+1)_(b-2) + (b-2)!.
    # RHS at V=0: α_b (U+1)_(b-2) + β_b · [(U+1)_(b-2) + (b-2)!] = (α_b + β_b)(U+1)_(b-2) + β_b (b-2)!
    # Should equal (b²-1)/b · (U+1)_(b-2).
    # Match: α_b + β_b = (b²-1)/b, β_b (b-2)! = 0 → β_b = 0, α_b = (b²-1)/b.
    # But then RHS = (b²-1)/b · (U+1)_(b-2)(V+1)_(b-2)/(b-2)!, which is ansatz 1 — we know it fails.
    print("  This reduces to ansatz 1 at V=0. Since ansatz 1 already tested.")


def try_deriv_ansatz(b_max):
    """Try N_1 = Σ_b (b²-1)/b · Q_b(U, V) · T^b/(b-2)! where Q_b is a symmetric poly
    of degree b-2 in each of U, V with Q_b(U,0) = (U+1)_(b-2).

    Then Q_b(U, V) might have decomposition:
       Q_b(U, V) = (b-2)! · sum over partitions ...
    """
    print("\nCompute Q_b = [T^b] N_1 · b · (b-2)! / (b²-1) (should be sym poly with Q_b(U,0)=(U+1)_(b-2))")
    for b in range(2, b_max + 1):
        c = coefs.get(b, Integer(0))
        if b == 2:
            Q = c * b / (b*b - 1)
        else:
            Q = c * b * factorial(b - 2) / (b*b - 1)
        Q_simp = simplify(Q)
        print(f"\n  b={b}:  Q_b = {expand(Q_simp)}")
        # Check Q_b at V=0:
        Q_V0 = expand(Q_simp.subs(V, 0))
        Q_V0_pred = expand(rf(U+1, b-2)) if b > 2 else Integer(1)
        print(f"    Q_b|_(V=0) = {factor(Q_V0)}, predicted (U+1)_(b-2) = {factor(Q_V0_pred)}, match: {expand(Q_V0 - Q_V0_pred) == 0}")


if __name__ == '__main__':
    b_max = 8
    test_ansatz_1(b_max)
    test_ansatz_2(b_max)
    test_ansatz_3(b_max)
    analyze_ratio_to_product(b_max)
    analyze_ratio_UV1(b_max)
    try_two_term_ansatz(b_max)
    try_deriv_ansatz(b_max)
