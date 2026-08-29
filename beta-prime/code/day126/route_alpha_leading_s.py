"""
Test the sharper conjecture:
  For symmetric f, the top-τ part is a polynomial in (s, y). Its
  s-leading part (highest s-degree, keeping y-dependence) is preserved
  by Ψ.

Also test: does Ψ preserve the entire "τ-graded" structure?
"""

from sympy import symbols, expand, Poly, Integer, prod

u1, u2, u3 = symbols('u1 u2 u3')
tau, s, y = symbols('tau s y')

V = (u1 - u2) * (u1 - u3) * (u2 - u3)
e1 = u1 + u2 + u3
e2 = u1*u2 + u1*u3 + u2*u3
e3 = u1*u2*u3


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
    numer = expand(T_op(expand(f * V)))
    q, r = Poly(numer, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise ValueError("Division by V failed")
    return q.as_expr()


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


def top_tau(poly_in_u):
    red = substitute_and_reduce(poly_in_u)
    if red == 0:
        return (-1, Integer(0))
    p = Poly(red, tau)
    return (p.degree(), expand(p.LC()))


def s_leading(poly_in_sy):
    """Return the leading s-degree coefficient (a polynomial in y) of poly."""
    if poly_in_sy == 0:
        return (-1, Integer(0))
    # poly in (s, y): use Poly in s
    try:
        p = Poly(poly_in_sy, s)
    except Exception:
        return (0, expand(poly_in_sy))
    return (p.degree(), expand(p.LC()))


# ============================================================
# Sweep: many symmetric polynomials
# ============================================================

tests = []
for a1 in range(4):
    for a2 in range(6):
        for a3 in range(3):
            if 1 <= a1 + a2 + 2*a3 <= 6:
                name = f"e1^{a1} e2^{a2} e3^{a3}"
                tests.append((name, e1**a1 * e2**a2 * e3**a3, a1 + a2 + 2*a3))

print(f"Testing {len(tests)} e-monomials of weight ≤ 6")
print("=" * 90)
print(f"{'poly':<20} | {'weight':>6} | {'top-τ(f) s-lead':<20} | {'top-τ(Ψf) s-lead':<20} | eq?")
print("-" * 90)

all_match = True
for name, f, w in tests:
    df, tf = top_tau(f)
    Pf = Psi(f)
    dp, tp = top_tau(Pf)
    if df != dp:
        print(f"{name:<20} | {w:>6} | DEG-MISMATCH df={df} dp={dp}")
        all_match = False
        continue
    sd_f, sl_f = s_leading(tf)
    sd_p, sl_p = s_leading(tp)
    diff = expand(sl_f - sl_p)
    eq = (diff == 0) and (sd_f == sd_p)
    if not eq:
        all_match = False
    print(f"{name:<20} | {w:>6} | {str(sl_f)[:18]:<20} | {str(sl_p)[:18]:<20} | {'MATCH' if eq else 'DIFF: ' + str(diff)[:30]}")

print()
print(f"OVERALL: {'ALL MATCH' if all_match else 'SOME MISMATCH'}")
print()

# Also check: does the s-leading of top-τ(f) equal 1 for e-monomial f?
print("=" * 90)
print("Check: for e-monomial f = e1^a1 e2^a2 e3^a3, is s-leading of top-τ(f) always 1?")
print("=" * 90)
for name, f, w in tests[:20]:
    df, tf = top_tau(f)
    sd, sl = s_leading(tf)
    print(f"  {name}: top-τ = {tf}, s-lead ({sd}) = {sl}")
