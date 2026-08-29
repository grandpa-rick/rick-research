"""Refine the closed form for A_1 and check the boundary case j=1.

CLAIM (to prove):
  A_1(b, c, j) = (b+c-2)^{↓(j-2)} * P_j(b, c),   j >= 2,
  where P_j = (j/2)*[2b²c - b²j + 3b² + 2bc² - 4bcj + 8bc + bj - 3b - c²j + 5c² - cj - 3c].

CROSS-CHECK (j=1):
  A_1(b, c, 1) = b*c + b + 2c.
  If we FORMALLY extend the closed form: at j=1, (b+c-2)^{↓-1} would be 1/(b+c-1).
  P_1 = (1/2)[2b²c - b² + 3b² + 2bc² - 4bc + 8bc + b - 3b - c² + 5c² - c - 3c]
       = (1/2)[2b²c + 2b² + 2bc² + 4bc - 2b + 4c² - 4c]
       = b²c + b² + bc² + 2bc - b + 2c² - 2c
       = (b + c)(b + c - 1)(b + 2c - ?)  ? let's check
  P_1 / (b+c-1) = ?
"""

import sympy as sp
from sympy import symbols, factor, expand, Poly, cancel, simplify, Rational, Integer

b, c, j = symbols('b c j')

# Closed form for P_j
Pj_closed = (Rational(1, 2) * j * (
    2*b**2*c - b**2*j + 3*b**2
    + 2*b*c**2 - 4*b*c*j + 8*b*c + b*j - 3*b
    - c**2*j + 5*c**2 - c*j - 3*c
))
print("P_j =", expand(Pj_closed))
print("P_j factored (attempted):", factor(Pj_closed))

# Alternative: try expressing P_j in a nicer form.
# Group by powers of j:
Pj_by_j = Poly(Pj_closed, j)
for (deg,), cf in Pj_by_j.terms():
    print(f"  [j^{deg}]:  {factor(cf)}")

# Try to write in terms of falling factorials in j.
# j^2 - 3j = j(j-3),  j^2 + 3j = j(j+3), etc.

# Let's split: P_j = j*Q_j(b,c) where Q_j(b,c) - is inside the bracket / 2.
inner = 2 * Pj_closed / j
print(f"\n  P_j = j/2 * inner, where inner = {expand(inner)}")

# Regroup:
grouping = expand(inner)
# Try: inner = 2*(b^2*c + b*c^2) + 3*b^2 + 5*c^2 + 8*b*c - 3*b - 3*c - j*(b^2 + 4*b*c + c^2 - b + c)
inner_symbolic = 2*(b**2*c + b*c**2) + 3*b**2 + 5*c**2 + 8*b*c - 3*b - 3*c - j*(b**2 + 4*b*c + c**2 - b + c)
check = expand(inner - inner_symbolic)
print(f"  Check regroup: {check}")

# Great! So:
#   P_j = (j/2) * [ 2bc(b+c) + 3b² + 5c² + 8bc - 3b - 3c - j*(b² + 4bc + c² - b + c) ]
# Or:  P_j = (j/2) * [ 2bc(b+c) + (3b² + 8bc + 5c²) - (3b + 3c) - j*(b² + 4bc + c² - b + c) ]

# Note (3b² + 8bc + 5c²) = (3b + 5c)(b + c)?  3b*b + 3b*c + 5c*b + 5c*c = 3b² + 8bc + 5c². YES!
# So 3b² + 8bc + 5c² = (3b + 5c)(b + c).
# And 2bc(b+c) + (3b+5c)(b+c) - 3(b+c) = (b+c)(2bc + 3b + 5c - 3) ?
check2 = expand(2*b*c*(b+c) + (3*b + 5*c)*(b+c) - 3*(b+c) - (b + c)*(2*b*c + 3*b + 5*c - 3))
print(f"  Check regroup 2: {check2}")

# So the non-j part is (b+c)(2bc + 3b + 5c - 3).
# And the j part is - j * (b² + 4bc + c² - b + c). Can we factor that?
# b² + 4bc + c² - b + c = (b + c)² + 2bc - b + c ... hmm.
factor_j_part = factor(b**2 + 4*b*c + c**2 - b + c)
print(f"  Factor j part: b² + 4bc + c² - b + c = {factor_j_part}")

# Alternative regroup:
# P_j = (j/2) * [ (b+c)(2bc + 3b + 5c - 3) - j*(b² + 4bc + c² - b + c) ]

# Now, the KEY: A_1(b, c, j) = (b+c-2)^{↓(j-2)} * P_j(b, c, j) for j >= 2.
# Let's cross-check j = 1 separately.
# A_1(b, c, 1) should = b*c + b + 2c (from earlier).
# Formal: (b+c-2)^{↓-1} would be 1/(b+c-1).
# P_1 = (1/2)[2b²c - b² + 3b² + 2bc² - 4bc + 8bc + b - 3b - c² + 5c² - c - 3c]
#     = (1/2)[2b²c + 2b² + 2bc² + 4bc - 2b + 4c² - 4c]
#     = b²c + b² + bc² + 2bc - b + 2c² - 2c
P1 = Pj_closed.subs(j, 1)
print(f"\n  P_1(b,c) = {expand(P1)}")
print(f"  P_1 factored = {factor(P1)}")

# A_1(b,c,1) formal = P_1 / (b+c-1):
A1_j1_formal = cancel(P1 / (b + c - 1))
print(f"  A_1(b,c,1) formal (P_1 / (b+c-1)) = {A1_j1_formal}")
# actual
print(f"  Actual A_1(b,c,1) = b*c + b + 2c")
diff = expand(A1_j1_formal - (b*c + b + 2*c))
print(f"  Diff = {diff}")

# Wow, if the diff is 0, the closed form extends to j=1 in the formal sense.

# Cross-check the divisibility identity manually:
# (b+2)_{c-1-j} = product from i=0 to c-2-j of (b+2+i) = (b+2)(b+3)...(b+c-j)
# For j = 1: (b+2)_{c-2} = (b+2)(b+3)...(b+c-1).
# (b+c-2)^{↓(j-2)} for j = 1 is (b+c-2)^{↓-1} = 1/(b+c-1).
# So (b+2)_{c-2} * (b+c-2)^{↓-1} = (b+2)(b+3)...(b+c-1) / (b+c-1) = (b+2)(b+3)...(b+c-2) = (b+2)_{c-3}. OK!
# So the identity DOES extend formally to j=1: (b+c-1) cancels.
# But then A_1(b, c, 1) = (b+c-2)^{↓-1} * P_1 = P_1 / (b+c-1), which must be a polynomial.
# It IS iff P_1 is divisible by (b+c-1).
# Let's check:
q, r = sp.div(Poly(P1, b, c), Poly(b + c - 1, b, c))
print(f"\n  P_1 / (b+c-1): remainder = {r.as_expr()}")
if r.as_expr() == 0:
    print(f"    quotient = {q.as_expr()}")
    print(f"    quotient factored = {factor(q.as_expr())}")

# So (b+c-1) DOES divide P_1! (I'll expect r=0 based on the diff check above.)
# So A_1(b, c, 1) = P_1(b, c) / (b + c - 1), which is a polynomial.
