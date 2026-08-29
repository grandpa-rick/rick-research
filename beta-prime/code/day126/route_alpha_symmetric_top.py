"""
Understand the top-τ symbol carefully.

Observation from route_alpha_top_symbol.py:
  top-τ(u^α) ≠ top-τ([u]_α) in general, but they differ by CONSTANTS.

But wait — this was for individual monomials, and the differences were things
like ±3, ±1, ±6. If the top-τ symbols differ, then summing over sym-poly
COULD introduce cancellations.

Yet empirically, Ψ preserves τ-deg on symmetric P. Why? Let's examine:

  1. Compute top-τ(f · V) and top-τ(T(f · V)) for symmetric f.
  2. Check if they agree exactly (not just in degree) or differ.
  3. Also examine what happens under division by V.
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


# The top-τ symbol of V
print("=" * 70)
print("Top-τ symbol of V")
print("=" * 70)
d, top = top_tau(V)
print(f"  τ-deg V = {d}, top-τ part = {top}")
print(f"  T(V) = ?")
d2, top2 = top_tau(T_op(V))
print(f"  τ-deg T(V) = {d2}, top-τ part = {top2}")
print(f"  Diff of top-τ parts: {expand(top - top2)}")
print()

# Test on f·V for symmetric f
tests_f = [
    ("1", Integer(1)),
    ("e1", e1),
    ("e2", e2),
    ("e3", e3),
    ("e2²", e2**2),
    ("e2³", e2**3),
    ("e2⁴", e2**4),
    ("e2⁵", e2**5),
    ("e1*e2", e1*e2),
    ("e1*e3", e1*e3),
]

print("=" * 70)
print("For symmetric f: compare top-τ(f·V) vs top-τ(T(f·V))")
print("=" * 70)
for name, f in tests_f:
    fV = expand(f * V)
    TfV = T_op(fV)
    d1, top1 = top_tau(fV)
    d2, top2 = top_tau(TfV)
    diff = expand(top1 - top2)
    same_deg = "OK" if d1 == d2 else "DEG-MISMATCH"
    same_top = "MATCH" if diff == 0 else "DIFF"
    print(f"  f = {name:8s}: deg={d1} vs {d2} [{same_deg}], top diff = {diff}  [{same_top}]")
print()

# The key: EVEN IF top-τ(f·V) ≠ top-τ(T(f·V)), the τ-degree is the same
# because both are nonzero polynomials in (y, s).
# For (★), we need top-τ(T(f·V)) ≠ 0 AND divides V properly to give top-τ(Ψf).

# So the correct statement is:
#   top-τ(T(f·V)) ≠ 0  (given f is symmetric, degree bound tight)
#   top-τ(T(f·V)) / top-τ(V) = top-τ(Ψ f) after some interpretation
#   ... and top-τ(Ψ f) also ≠ 0.

# Test top-τ(Ψ f) directly
print("=" * 70)
print("Top-τ(Ψ f) directly:")
print("=" * 70)
for name, f in tests_f:
    Pf = Psi(f)
    df, tf = top_tau(f)
    dp, tp = top_tau(Pf)
    print(f"  f={name:8s}: τ-deg f = {df}, top = {tf}")
    print(f"                 τ-deg Ψf = {dp}, top = {tp}")
    print(f"                 diff Ψf-f (top-τ part): {expand(tf - tp)}")
print()

# ============================================================
# Observation: Are top-τ parts of Ψf and f always equal?
# If so, that's a STRONGER statement than τ-deg preservation.
# ============================================================
print("=" * 70)
print("Is top-τ(Ψ f) = top-τ(f) exactly, for symmetric f?")
print("=" * 70)
for name, f in tests_f:
    Pf = Psi(f)
    df, tf = top_tau(f)
    dp, tp = top_tau(Pf)
    diff = expand(tf - tp)
    print(f"  f={name:8s}: top-τ f = {tf};  top-τ Ψf = {tp};  diff = {diff}")
