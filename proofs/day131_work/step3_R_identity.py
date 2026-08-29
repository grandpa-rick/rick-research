"""Identify R := Q(e_2, V)/V and reduce piece_3 = N_b.

Q(e_2, V) := Sum_{a<b} [D_b(e_2) D_a(V) + D_a(e_2) D_b(V)]
           = 6 e_2 V - Sum_a D_a(e_2) D_a(V)

Since Q is antisymm, Q = R * V for a symmetric R. Compute R.

Then:
  e_2(D)(e_2^b V) = A_b * V
  where A_b = b(b-1)(e_2^b + e_1 e_3 e_2^{b-2}) + (b+2) e_2^b + b R e_2^{b-1}

So N_b = Psi(A_b).
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3, falling
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom, max_weight)
from sympy import expand, Poly, Integer, factor, simplify, symbols, Rational, diff

D1 = lambda p: expand(u1 * diff(p, u1))
D2 = lambda p: expand(u2 * diff(p, u2))
D3 = lambda p: expand(u3 * diff(p, u3))
E_op = lambda p: expand(D1(p) + D2(p) + D3(p))

def e2_D(p):
    return expand(D1(D2(p)) + D1(D3(p)) + D2(D3(p)))

def sigma(p):
    return expand(p.subs({u1: u1-1, u2: u2-1, u3: u3-1}, simultaneous=True))

def divV(x):
    x = expand(x)
    q, r = Poly(x, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise ValueError(f"Nonzero remainder: {r.as_expr()}")
    return q.as_expr()

# Compute Q(e_2, V) directly.
Q = expand(
    D2(e2_u) * D1(V) + D1(e2_u) * D2(V)
    + D3(e2_u) * D1(V) + D1(e2_u) * D3(V)
    + D3(e2_u) * D2(V) + D2(e2_u) * D3(V)
)

R = divV(Q)
print(f"R := Q/V = {R}")
print(f"R factored = {factor(R)}")

# Try to express R in E-basis:
R_E = sym_to_ebasis_direct(R)
print(f"R in E-basis: {R_E}")

# Now let's verify the decomposition of e_2(D)(e_2^b V) = A_b * V
print("\nVerify: e_2(D)(e_2^b V) / V = b(b-1)(e_2^b + e_1 e_3 e_2^{b-2}) + (b+2) e_2^b + b R e_2^{b-1}")
for b in range(0, 5):
    lhs = divV(e2_D(e2_u**b * V))
    if b == 0:
        rhs = 2 * Integer(1)  # b(b-1)=0, b=0
    elif b == 1:
        rhs = expand(1 * (e2_u + e3_u * e1_u * Integer(0)) * 0 + 3 * e2_u + 1 * R * Integer(1))  # b(b-1)=0
        # b=1: b(b-1) = 0, so A_1 = (1+2) e_2 + 1 * R * 1 = 3 e_2 + R
        rhs = expand(3 * e2_u + R)
    else:
        rhs = expand(b*(b-1) * (e2_u**b + e1_u * e3_u * e2_u**(b-2)) + (b+2) * e2_u**b + b * R * e2_u**(b-1))
    diff_val = expand(lhs - rhs)
    print(f"  b={b}: matches? {'YES' if diff_val == 0 else 'NO'}")
    if diff_val != 0:
        print(f"    diff = {diff_val}")

# Now N_b = Psi(A_b). Let's compute Psi(R e_2^{b-1}) — what is that?
# R involves E_1, E_2, E_3. Since Psi doesn't distribute over multiplication generally,
# we need to compute Psi(R * e_2^{b-1}) as one piece.

# Actually, we have identities:
#   Psi(e_1 * f) = (e_1 - 3) Psi(f) - Psi(E(f))
#   Psi(e_3 * f) = e_3 * sigma(Psi(f))
# For e_2 * f: use T-identity (that's the whole recursion).

# So if R is a polynomial in e_1, e_2, e_3, we may be able to reduce.
# From R_E, let's see if R is polynomial in E-vars (should be).

print(f"\nWeight of R = {max_weight(R_E)}")
