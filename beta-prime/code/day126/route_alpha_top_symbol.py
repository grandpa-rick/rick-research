"""
Sharpen the argument: for each u-monomial m = u1^a u2^b u3^c, compute
  - S(u^α) reduced, and its top-τ coefficient
  - S([u]_α) reduced, and its top-τ coefficient
and verify they agree exactly (not just up to degree).

If they agree, then T (as a linear operator) has the same top-τ symbol as
the identity, and hence τ-degree is preserved on any polynomial (since
the top-τ contributions of each monomial are equal, no cancellation can
be introduced by T that wasn't already in the input).
"""

from sympy import symbols, expand, Poly, Integer, prod

u1, u2, u3 = symbols('u1 u2 u3')
tau, s, y = symbols('tau s y')


def falling(x, k):
    if k == 0:
        return Integer(1)
    return prod([x - i for i in range(k)])


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


def top_tau_part(poly_in_u):
    """Return (τ-deg, top-τ-part as polynomial in (y, s)).
    top-τ-part = coefficient of τ^d in S(poly), where d = τ-deg.
    """
    red = substitute_and_reduce(poly_in_u)
    if red == 0:
        return (-1, Integer(0))
    p = Poly(red, tau)
    d = p.degree()
    return (d, expand(p.LC()))


def falling_monomial(a, b, c):
    return falling(u1, a) * falling(u2, b) * falling(u3, c)


def ordinary_monomial(a, b, c):
    return u1**a * u2**b * u3**c


print("=" * 70)
print("Compare top-τ symbols of  u^α  vs  [u]_α  for α = (a, b, c)")
print("=" * 70)

fail = 0
matches = 0
diffs = []
for a in range(5):
    for b in range(5):
        for c in range(5):
            if a + b + c == 0:
                continue
            d1, top1 = top_tau_part(ordinary_monomial(a, b, c))
            d2, top2 = top_tau_part(falling_monomial(a, b, c))
            if d1 != d2:
                fail += 1
                print(f"  (a,b,c)=({a},{b},{c}): DEG MISMATCH: {d1} vs {d2}")
            elif expand(top1 - top2) != 0:
                fail += 1
                diffs.append(((a, b, c), d1, top1, top2))
            else:
                matches += 1

print(f"\n{matches} exact matches, {fail} mismatches out of {matches + fail} tests")
if diffs:
    print("\nDifferences (top-τ parts NOT equal, but degrees match):")
    for (abc, d, t1, t2) in diffs[:20]:
        print(f"  α = {abc}, τ-deg = {d}")
        print(f"    top-τ(u^α):   {t1}")
        print(f"    top-τ([u]_α): {t2}")
        print(f"    diff:         {expand(t1 - t2)}")

# If diffs is non-empty but shares degree, the top-τ symbols DIFFER, which
# means T is NOT identity on top-τ symbols. But τ-degree is still preserved.
# In that case, τ-deg preservation requires a different argument.
