"""Attempt: prove the recursion tops[b+1] = sum_j (b)_j g_j tops[b-j] structurally.

Idea:  Psi(e_2^{b+1}) = T(e_2^{b+1} V) / V.
        We want this in terms of Psi(e_2^b) = T(e_2^b V)/V and derivatives.

Key identity attempt: e_2 * (u_i^n) - relation? Consider the operator
  D := multiplication by e_2 in u-space.
And define the u-space operator "derivative"
  Delta_i := forward difference u_i^n -> u_i^n * n / u_i? etc.

Actually the cleanest identity: for a scalar function f(u_i), we have
   T(u_i * f(u_i)) = u_i * T(f(u_i)) - T(f(u_i)) shifted?
Let's check: T(u_i^{n+1}) = (u_i)_{n+1} = (u_i - n)(u_i)_n = u_i (u_i)_n - n (u_i)_n.
So T(u_i * u_i^n) = (u_i)_{n+1} = u_i * T(u_i^n) - n * T(u_i^n).
But T(u_i^n) = (u_i)_n and n * (u_i)_n = "difference"?  n (u_i)_n = u_i (u_i)_n - (u_i)_{n+1}?
Let's just verify:
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3, falling
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import expand, Poly, Integer, factor, simplify, symbols, Rational, diff

# Verify u_i * T(u_i^n) = T(u_i^{n+1}) + n T(u_i^n).
u = symbols('u')
for n in range(0, 5):
    lhs = expand(u * falling(u, n))
    rhs = expand(falling(u, n+1) + n * falling(u, n))
    print(f"n={n}: u*(u)_n = (u)_{n+1} + n*(u)_n? {'OK' if lhs == rhs else 'FAIL'}")

# So u_i T(f_i(u_i)) = T( (u_i - Delta_i) f_i(u_i)) where "Delta_i" is the shift operator?
# Or more usefully:
#   For a monomial u_i^n: u_i T(u_i^n) = T(u_i^{n+1}) + n T(u_i^n)
#   Multiplication by u_i in "T-space" is: T(u_i^{n+1}) = (u_i - n) T(u_i^n).
# So if we define an operator on generating functions:
#   sum_n a_n u_i^n / n!  under T is  sum_n a_n (u_i)_n / n!
#   multiplication by u_i in u_i-space shifts: T(u_i * f) = T((u_i) f)  where...
# This is the classical umbral calculus: "u_i acts as (u_i - Delta)".

# Now, e_2 = u_1 u_2 + u_1 u_3 + u_2 u_3.
# T(e_2 * f) for a monomial f = u_1^a u_2^b u_3^c :
#   e_2 * f = u_1^{a+1} u_2^{b+1} u_3^c + u_1^{a+1} u_2^b u_3^{c+1} + u_1^a u_2^{b+1} u_3^{c+1}
# T of each:  (u_1)_{a+1}(u_2)_{b+1}(u_3)_c + (u_1)_{a+1}(u_2)_b(u_3)_{c+1} + (u_1)_a(u_2)_{b+1}(u_3)_{c+1}
#
# Using u_i (u_i)_n = (u_i)_{n+1} + n (u_i)_n:
# so (u_i)_{a+1} = u_i (u_i)_a - a (u_i)_a.
# So T(u_1^{a+1} u_2^{b+1} u_3^c) = (u_1 (u_1)_a - a (u_1)_a) (u_2 (u_2)_b - b (u_2)_b) (u_3)_c
#                                 = u_1 u_2 (u_1)_a (u_2)_b (u_3)_c
#                                 - a u_2 (u_1)_a (u_2)_b (u_3)_c
#                                 - b u_1 (u_1)_a (u_2)_b (u_3)_c
#                                 + a b (u_1)_a (u_2)_b (u_3)_c
# Similarly for the other two terms.
# Summing over the 3 pair-choices:
# T(e_2 * u_1^a u_2^b u_3^c) = e_2 * T(u_1^a u_2^b u_3^c)
#                              - [a u_2 + b u_1 + a u_3 + c u_1 + b u_3 + c u_2] T(...)
#                              + [a b + a c + b c] T(...).
# Simplify middle bracket: (a+c) u_1 + (a+b?) wait let me recompute.
# Wait the three pair-choices:
#   (u_1, u_2): pairing on u_1, u_2:  -a u_2, -b u_1, +ab
#   (u_1, u_3): pairing on u_1, u_3:  -a u_3, -c u_1, +ac
#   (u_2, u_3): pairing on u_2, u_3:  -b u_3, -c u_2, +bc
# Sum of "linear in u" terms:
#   u_1 coeff: -b - c
#   u_2 coeff: -a - c
#   u_3 coeff: -a - b
# Constant: ab + ac + bc = e_2(a, b, c).
#
# So: T(e_2 * u_1^a u_2^b u_3^c) = [e_2(u) - (b+c) u_1 - (a+c) u_2 - (a+b) u_3 + e_2(a,b,c)]
#                                  * T(u_1^a u_2^b u_3^c)
# For a general polynomial f = sum c_{abc} u_1^a u_2^b u_3^c:
# T(e_2 f) is NOT (op on T(f)) because the (a,b,c)-dependent terms are exponent-dependent.

# HOWEVER, we can convert (a, b, c) exponents into DERIVATIVES:
#   a * u_1^a u_2^b u_3^c = u_1 d/du_1 (u_1^a u_2^b u_3^c).
# So a u_2, b u_1, etc appear as: b u_1 -> u_1 * (u_2 d/du_2) applied to monomial.
# Hmm this gets us:
# The identity becomes an operator identity on polynomials f:
#   T(e_2 * f) = [e_2 - (u_2 d/du_2 + u_3 d/du_3) u_1 - (u_1 d/du_1 + u_3 d/du_3) u_2
#                    - (u_1 d/du_1 + u_2 d/du_2) u_3] * T(f)
#                + e_2(u_1 d/du_1, u_2 d/du_2, u_3 d/du_3) T(f)
# CAREFUL WITH ORDERING OF u_i AND d/du_j.  Let me redo this.
# We had T(e_2 · u^{(a)}) = [e_2(u) - (b+c) u_1 - (a+c) u_2 - (a+b) u_3 + e_2(a,b,c)] T(u^{(a)})
# where u^{(a)} = u_1^a u_2^b u_3^c.
# For general f, this becomes:
#   T(e_2 f) = e_2(u) T(f)
#            - u_1 T((D_2 + D_3) f)
#            - u_2 T((D_1 + D_3) f)
#            - u_3 T((D_1 + D_2) f)
#            + T(e_2(D_1, D_2, D_3) f)
# where D_i = u_i d/du_i is the Euler operator on u_i.
# because (b+c) u_1^a u_2^b u_3^c = (D_2 + D_3) u_1^a u_2^b u_3^c.
#
# Now substitute f = e_2^b * V:
# T(e_2^{b+1} V) = e_2(u) T(e_2^b V) - u_1 T((D_2+D_3)(e_2^b V)) - ...  + T(e_2(D_1,D_2,D_3)(e_2^b V))
#
# Let's verify this identity for small cases:
D1 = lambda p: expand(u1 * diff(p, u1))
D2 = lambda p: expand(u2 * diff(p, u2))
D3 = lambda p: expand(u3 * diff(p, u3))

def apply_e2_D(p):
    """e_2(D1, D2, D3) applied to p."""
    return expand(D1(D2(p)) + D1(D3(p)) + D2(D3(p)))

def T_identity_check(f):
    lhs = T_u(expand(e2_u * f))
    rhs = (e2_u * T_u(f)
           - u1 * T_u(expand((D2(f) + D3(f))))
           - u2 * T_u(expand((D1(f) + D3(f))))
           - u3 * T_u(expand((D1(f) + D2(f))))
           + T_u(apply_e2_D(f)))
    return expand(lhs - rhs)

# Test on some polynomials.
test_polys = [Integer(1), u1, u1*u2, e2_u, V, e2_u*V, e2_u**2*V]
for f in test_polys:
    diff_val = T_identity_check(f)
    print(f"f = {f}: T-identity holds? {'YES' if diff_val == 0 else 'NO, diff = ' + str(diff_val)}")
