"""Route 1 careful: verify the recursion structure.

Empirical finding: tops[b+1] = (E2 - b*E1)*tops[b] + Y_b
where Y_b is a polynomial in (E1,E2,E3) of top-weight b+1, divisible by E3.

Let X_b = Y_b / E3  (weight b-1 polynomial in E1,E2,E3).
Study X_b.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, e1_u, e2_u, e3_u,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import expand, Poly, Integer, factor, simplify, diff, Rational, symbols

# Compute tops[b] for b=0..7 if possible.
tops = {}
for b in range(0, 7):
    print(f"Computing tops[{b}]...", flush=True)
    psi_u = Psi_direct(e2_u**b) if b > 0 else Psi_direct(Integer(1))
    psi_e = sym_to_ebasis_direct(psi_u)
    tops[b] = top_weight_part(psi_e, b)

# Verify the recursion structure.
print("\n=== Recursion check: tops[b+1] = (E2 - b*E1)*tops[b] + Y_b, Y_b div by E3 ===")
Y = {}
for b in range(0, 6):
    lhs = tops[b+1]
    guess = expand((E2 - b*E1) * tops[b])
    Yb = expand(lhs - guess)
    # Check divisibility by E3
    q, r = Poly(Yb, E3).div(Poly(E3, E3))
    if r.as_expr() != 0:
        print(f"  b={b}: Y_b = {Yb} NOT divisible by E3.")
    else:
        Y[b] = Yb
        X = q.as_expr()
        print(f"  b={b}: X_b = Y_b/E3 =")
        print(f"    {X}")
        print(f"    factored: {factor(X)}")


# Now: X_b should be a linear combination of top-weight tops[b-1], and possibly
# tops[b-2] · E1 etc. Let's see.
print("\n=== Try: X_b = f_b(E1, E2, E3) * tops[b-1] + ... ? ===")
# Actually maybe X_b involves derivatives of tops[b].
# Try: X_b = a*E1 * tops[b-1] + b*E2 * tops[b-1] + ... etc.
# tops[b-1] has weight b-1, same as X_b. So X_b/tops[b-1] should be weight 0, i.e. a constant.

for b in range(1, 6):
    if b not in Y:
        continue
    X = expand(Y[b] / E3)
    print(f"\nb={b}: X_b weight = {b-1}, tops[b-1] = {tops[b-1]}")
    if tops[b-1] != 0:
        q, r = Poly(X, E1, E2, E3).div(Poly(tops[b-1], E1, E2, E3))
        print(f"  X_b / tops[b-1]: q = {q.as_expr()}, r = {r.as_expr()}")


# Look for X_b as combination of tops[b-1], E1*tops[b-2], E2*tops[b-2], E3*tops[b-3],
# and products.
print("\n=== Try linear combinations of pieces built from lower tops ===")
# Explicit ansatz: X_b = alpha_b * tops[b-1] + [terms involving derivatives?]

# Actually the beauty of the recursion (E2 - b*E1) being the linear factor from A(T)
# suggests X_b might be simply E3 · (derivative-like) of tops[b].
# Recall A(T) = prod (E2 - r*E1), B(T) = exp(E3*M(T)).
# F = A * B.  Derivative: F' = A' * B + A * B' = A'/A * F + M' * E3 * F.
# So F' = [A'/A + E3 * M'(T)] * F.
# Coefficient of T^b/b!: (b+1)! * F_{b+1}/(b+1)! = ... derivative shifts by 1.
# Actually F(T) = sum tops[b] * T^b/b!. F'(T) = sum tops[b+1] * T^b/b!.
# So sum tops[b+1] T^b/b! = [A'/A + E3 M'(T)] sum tops[b] T^b/b!.
#
# What is A(T) = (1+E1*T)^{E2/E1 - 1}?  A'(T) = (E2/E1 - 1) * E1 * (1+E1*T)^{E2/E1-2}
#             = (E2 - E1) * (1+E1*T)^{E2/E1-2}.
# So A'/A = (E2 - E1) / (1 + E1*T).
# And M(T) = T/(E1*(1+E1 T)^2) - log(1+E1 T)/E1^2
#     M'(T) = [ (1+E1 T)^2 - T*2*(1+E1 T)*E1 ] / [E1 * (1+E1 T)^4]
#            - (1/E1^2) * E1 / (1+E1 T)
#           = [ (1+E1 T) - 2*E1*T ] / [E1 * (1+E1 T)^3]  -  1/[E1 (1+E1 T)]
#           = [ 1 - E1 T ] / [E1 * (1+E1 T)^3]  -  1/[E1 (1+E1 T)]
#     Common denom E1*(1+E1 T)^3:
#           = [ (1-E1 T) - (1+E1 T)^2 ] / [E1 * (1+E1 T)^3]
#           = [ 1 - E1 T - 1 - 2 E1 T - E1^2 T^2 ] / [E1 * (1+E1 T)^3]
#           = [ -3 E1 T - E1^2 T^2 ] / [E1 * (1+E1 T)^3]
#           = -T (3 + E1 T) / (1+E1 T)^3
# So E3 * M'(T) = -E3 T (3 + E1 T) / (1+E1 T)^3.
#
# The recursion at coefficient level:
#   tops[b+1] = [A'/A + E3 * M'(T)]_{via convolution} applied to tops[b]
# where [A'/A + E3 M'] is a POWER SERIES in T. So actually this gives
#   tops[b+1] = sum_{j=0}^{b} C(b, j) * [T^j coefficient of A'/A + E3 M'] * tops[b-j]
# where the coefficient is a polynomial in E1, E2, E3.
# T^0: A'/A|_{T=0} = E2 - E1.  So leading term: (E2 - E1) * tops[b].
# Hmm but empirical result was (E2 - b*E1). So there's a discrepancy!
# Wait: (E2 - E1) * tops[b] gives a b+1-weight polynomial. But my empirical
# observation was tops[b+1] = (E2 - b*E1) * tops[b] + E3 * X_b.
# For b=0: tops[1] = (E2 - 0*E1) * tops[0] = E2 * 1 = E2. But tops[1] = -E1 + E2.
# So my Poly division ordering was misleading.

# Let me redo the b=0 case:
# Poly(tops[1]).div(Poly(tops[0])). tops[0]=1, so quotient IS tops[1] = -E1 + E2.
# So q = -E1 + E2, not -0*E1 + E2 = E2.
# My "pattern (E2 - b*E1)" was for b=1,2,3,4:  -2E1 + E2, -3E1 + E2, -4E1 + E2, -5E1 + E2.
# So general formula might be: q_b = (E2 - (b+1)*E1)? Let me check b=0: -E1 + E2 = E2 - 1*E1. YES.
# So q_b = E2 - (b+1)*E1.  (matches for b=0,1,2,3,4).
# But the ODE gives (E2 - E1) as constant term of A'/A at T=0.

# Let me redo the recursion properly.
print("\n=== Refit: tops[b+1] = (E2 - (b+1)*E1)*tops[b] + E3 * X_b ===")
for b in range(0, 6):
    Yb = expand(tops[b+1] - (E2 - (b+1)*E1)*tops[b])
    q, r = Poly(Yb, E3).div(Poly(E3, E3))
    if r.as_expr() != 0:
        print(f"  b={b}: NOT div by E3, Y_b = {Yb}")
    else:
        Xb = q.as_expr()
        print(f"  b={b}: X_b = {Xb}")
        print(f"     factored: {factor(Xb)}")

# So the empirical recursion is:
#   tops[b+1] = (E2 - (b+1)*E1) tops[b] + E3 * X_b
#
# where X_b has weight b-1.  Let's look at X_b in terms of tops[b-1]:

print("\n=== X_b vs tops[b-1] ===")
Xs = {}
for b in range(0, 6):
    Yb = expand(tops[b+1] - (E2 - (b+1)*E1)*tops[b])
    q, r = Poly(Yb, E3).div(Poly(E3, E3))
    if r.as_expr() == 0:
        Xs[b] = q.as_expr()

for b in range(1, 6):
    if b not in Xs:
        continue
    Xb = Xs[b]
    T_prev = tops[b-1]
    print(f"\nb={b}: X_b = {Xb}")
    print(f"       tops[{b-1}] = {T_prev}")

# Let's see if X_b = c_b * tops[b-1] for some scalar c_b:
print("\n=== ratio X_b / tops[b-1] ===")
for b in range(1, 6):
    if b not in Xs:
        continue
    Xb = Xs[b]
    T_prev = tops[b-1]
    if T_prev != 0:
        try:
            q, r = Poly(Xb, E1, E2, E3).div(Poly(T_prev, E1, E2, E3))
            print(f"  b={b}: q = {q.as_expr()}, r = {r.as_expr()}")
        except Exception as e:
            print(f"  b={b}: {e}")

# Now go back to the theoretical ODE:
# F'(T) = [A'/A + E3 M'(T)] F(T)
# extract T^b/b! coeff on LHS: tops[b+1] / b!... wait EGF-diff shifts.
# F'(T) = sum tops[b] T^{b-1}/(b-1)! for b>=1
#       = sum_{k>=0} tops[k+1] T^k/k!.
# RHS: [A'/A + E3 M'] * F(T), a product of two EGFs (well, one is a power series
# and F is the EGF).
# Actually A'/A is not an EGF, it's just a formal power series in T.
# When we multiply a formal series G(T) = sum g_j T^j and an EGF F = sum f_k T^k/k!:
#   G * F = sum_n (sum_j g_j * f_{n-j} / (n-j)!) T^n
#         = sum_n T^n/n! * (sum_j g_j * n!/(n-j)! * f_{n-j})
#         = sum_n T^n/n! * (sum_j g_j * (n)_j (falling) * f_{n-j})
# So tops[b+1] = sum_{j=0}^{b} (b)_j * g_j * tops[b-j], where g_j = [T^j] (A'/A + E3 M').

from sympy import symbols, series, Symbol, log
Tsym = Symbol('Tsym')
# A'/A = (E2 - E1)/(1 + E1*T)
# Taylor: (E2 - E1) * sum_{j>=0} (-E1)^j T^j = sum_j (E2-E1)(-E1)^j T^j.
# g_j^{(A)} = (E2 - E1)*(-E1)^j.
# E3 M'(T) = -E3 * T * (3 + E1 T) / (1 + E1 T)^3.
# Compute Taylor:
E1s, E2s, E3s = E1, E2, E3
M_prime = -Tsym * (3 + E1s * Tsym) / (1 + E1s * Tsym)**3
Aprime_over_A = (E2s - E1s) / (1 + E1s * Tsym)

series_len = 8
ser = series(Aprime_over_A + E3s * M_prime, Tsym, 0, series_len).removeO()
ser_poly = Poly(expand(ser), Tsym)
gs = {j: ser_poly.coeff_monomial(Tsym**j) for j in range(series_len)}
print("\n=== Coefficients of A'/A + E3 M'(T) ===")
for j in range(series_len):
    print(f"  g_{j} = {gs[j]}")

# Now check: tops[b+1] = sum_{j=0}^b (b)_j * g_j * tops[b-j].
print("\n=== Check the ODE recursion tops[b+1] = sum_j (b)_j g_j tops[b-j] ===")
def falling(n, j):
    p = 1
    for i in range(j):
        p *= (n - i)
    return p

for b in range(0, 6):
    rhs = Integer(0)
    for j in range(0, b+1):
        rhs += falling(b, j) * gs[j] * tops[b-j]
    rhs = expand(rhs)
    lhs = tops[b+1]
    diff_expr = expand(lhs - rhs)
    print(f"  b={b}: LHS - RHS = {diff_expr}  {'OK' if diff_expr == 0 else 'FAIL'}")

# If this passes for b=0..5, we've verified the recursion is CONSISTENT with
# the ODE F' = [A'/A + E3 M'] F.
