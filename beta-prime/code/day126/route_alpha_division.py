"""
Test whether:
  (i)  T preserves τ-deg on ARBITRARY polynomials (not just monomials).
  (ii) Division by V preserves τ-deg: if V | P (P antisymmetric) and P has
       τ-deg d, then P/V has τ-deg d - τ-deg(V).
  (iii) What is τ-deg(V)?
"""

from sympy import symbols, expand, Poly, Integer, prod

u1, u2, u3 = symbols('u1 u2 u3')
tau, s, y = symbols('tau s y')

V = (u1 - u2) * (u1 - u3) * (u2 - u3)


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


def substitute_and_reduce(poly):
    expr = expand(poly.subs([(u1, tau), (u2, y), (u3, s - y)]))
    while True:
        p = Poly(expr, y)
        if p.degree() < 2:
            break
        d = p.degree()
        lc = p.LC()
        replacement = lc * y**(d - 2) * (s * y - tau)
        expr = expand(expr - lc * y**d + replacement)
    return expand(expr)


def tau_degree(poly):
    reduced = substitute_and_reduce(poly)
    if reduced == 0:
        return -1
    return Poly(reduced, tau).degree()


# ============================================================
# What is τ-deg V?
# ============================================================

def compute_V_stuff():
    print("=" * 70)
    print("Analysis of V = (u1-u2)(u1-u3)(u2-u3)")
    print("=" * 70)
    Vred = substitute_and_reduce(V)
    print(f"  V reduced: {Vred}")
    print(f"  τ-deg V = {tau_degree(V)}")
    print()

    # V's total u-degree is 3. Under substitute+reduce, y-degree gets reduced.
    # u1-u2 = τ - y
    # u1-u3 = τ - (s-y) = τ - s + y
    # u2-u3 = y - (s-y) = 2y - s
    # Product: (τ-y)(τ-s+y)(2y-s)
    # Let's compute step by step
    from sympy import symbols
    tau_, s_, y_ = symbols('tau s y')
    A = tau_ - y_
    B = tau_ - s_ + y_
    C = 2*y_ - s_
    # A*B*C
    prod_ = expand(A*B*C)
    print(f"  V(τ, y, s-y) expanded: {prod_}")
    # Reduce y² to sy - τ iteratively
    while True:
        p = Poly(prod_, y_)
        if p.degree() < 2:
            break
        d = p.degree()
        lc = p.LC()
        prod_ = expand(prod_ - lc * y_**d + lc * y_**(d - 2) * (s_ * y_ - tau_))
    print(f"  V reduced (manual): {prod_}")
    print()


# ============================================================
# Does T preserve τ-deg on SUMS of monomials?
# ============================================================

def test_T_on_sums():
    print("=" * 70)
    print("Test: T preserves τ-deg on random polynomial sums?")
    print("=" * 70)
    # Try: sum of monomials at various weights
    tests = [
        u1 + u2,
        u1 + u3,
        u2 + u3,
        u1 - u2,      # antisym; τ-deg = 1
        u1 - u3,
        u2 - u3,
        u1**2 + u2**2,
        u1**2 - u2*u3,
        u1**2 * u2 + u1 * u2**2,
        (u1-u2)*(u1-u3),  # partial antisym
        V,  # fully antisym
        V * u1,
        V * (u1 + u2 + u3),
        V * u1 * u2,
    ]
    for f in tests:
        td_f = tau_degree(f)
        td_Tf = tau_degree(T_op(f))
        eq = "OK" if td_f == td_Tf else "FAIL"
        print(f"  f = {f}")
        print(f"     τ-deg f = {td_f}, τ-deg T(f) = {td_Tf}  [{eq}]")
    print()


# ============================================================
# Division by V: check that if we take P = T(f·V) for symmetric f,
# then τ-deg(P) = τ-deg(f) + τ-deg(V), and P/V has τ-deg(f).
# ============================================================

def test_division_by_V():
    print("=" * 70)
    print("Test: τ-deg(T(f·V)) = τ-deg(f) + τ-deg(V) = τ-deg(f) + 3")
    print("=" * 70)
    e1 = u1 + u2 + u3
    e2 = u1*u2 + u1*u3 + u2*u3
    e3 = u1*u2*u3
    tests = [
        ("1", Integer(1), 0),
        ("e1", e1, 1),
        ("e2", e2, 1),
        ("e3", e3, 2),
        ("e2²", e2**2, 2),
        ("e2³", e2**3, 3),
        ("e2⁴", e2**4, 4),
        ("e2⁵", e2**5, 5),
    ]
    td_V = tau_degree(V)
    print(f"  τ-deg V = {td_V}")
    for name, f, w in tests:
        td_f = tau_degree(f)
        fV = expand(f * V)
        td_fV = tau_degree(fV)
        TfV = T_op(fV)
        td_TfV = tau_degree(TfV)
        # Divide by V
        q, r = Poly(TfV, u1, u2, u3).div(Poly(V, u1, u2, u3))
        assert r.as_expr() == 0
        Psi_f = q.as_expr()
        td_Psi_f = tau_degree(Psi_f)
        print(f"  f={name}: τ-deg(f)={td_f}, τ-deg(f·V)={td_fV}, τ-deg(T(f·V))={td_TfV}, τ-deg(Ψf)={td_Psi_f}")
    print()


# ============================================================
# Test: τ-deg is subadditive under multiplication? (would prove
# τ-deg(P/V) >= τ-deg(P) - τ-deg(V) via a "flatness" argument.)
# ============================================================

def test_multiplicativity():
    print("=" * 70)
    print("Test: is τ-deg multiplicative?  τ-deg(A · B) = τ-deg(A) + τ-deg(B)?")
    print("=" * 70)
    tests = [
        (u1, u1),
        (u2, u3),
        (u1, u2 + u3),
        (V, u1**2),
        (V, u1*u2*u3),
        (V, u2*u3),
        (V, u2**2),  # u2² : τ-deg = 1;   V·u2² : ?
        ((u1-u2), (u1-u3)),
        ((u1-u2)*(u1-u3), (u2-u3)),
    ]
    for A, B in tests:
        tdA = tau_degree(A)
        tdB = tau_degree(B)
        tdAB = tau_degree(expand(A*B))
        eq = "OK" if tdAB == tdA + tdB else "STRICT<"
        print(f"  A={A}, B={B}: τ-deg A={tdA}, τ-deg B={tdB}, τ-deg A·B={tdAB}  [{eq}]")
    print()

    # Note: after reduction, y appears, so the ring is not a domain in the
    # naive sense — but degrees should still be additive if we treat the
    # substitution first, then reduce.
    #
    # BEFORE reduction: (τ, y, s) live in a poly ring, τ-deg is multiplicative.
    # AFTER reduction: y² = sy - τ, which HAS τ. Reducing y² could DECREASE τ-deg
    # only when the y² term's coefficient contains the leading τ. Otherwise,
    # y² → sy - τ ADDS τ at the same or higher degree.


if __name__ == "__main__":
    compute_V_stuff()
    test_T_on_sums()
    test_division_by_V()
    test_multiplicativity()
