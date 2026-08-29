"""Verify: A(T) B(T) satisfies the SHIFT-ODE

  (1 + E_1 T) F'(T) = (E_2 - E_1) F(T) - E_3 T (3 + E_1 T) F_tilde(T)

where F_tilde(T) = F(T)|_{E_2 -> E_2 - 2 E_1}.

Then, since F(T) = sum tops[b] T^b/b! satisfies the SAME shift-ODE
(derived from the top-weight recursion) with the same IC F(0) = 1,
uniqueness of the recursion forces F = A B.

Verify:
  (a) A B satisfies the shift-ODE (via A_tilde = A / (1 + E_1 T)^2).
  (b) tops[b+1] from shift-ODE matches tops[b+1] from direct computation.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t as tau, u1, u2, u3
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, top_weight_part,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import expand, Poly, Integer, Symbol, series, log, exp, factor, simplify, Rational, diff, symbols

Tsym = Symbol('Tsym')

# ---- Compute tops from direct Psi ----
tops_direct = {-2: Integer(0), -1: Integer(0)}
tops_direct[0] = Integer(1)
for b in range(1, 7):
    psi_u = Psi_direct(e2_u**b)
    psi_e = sym_to_ebasis_direct(psi_u)
    tops_direct[b] = top_weight_part(psi_e, b)

# ---- Compute tops via the closed form A B ----
# A(T) = sum (1/k!) prod_{r=1}^k (E_2 - r E_1) T^k
# B(T) = sum (E_3 M(T))^p / p! where M(T) = sum_{n>=2} (-1)^{n-1} (n^2-1)/n E_1^{n-2} T^n

def prod_falling(a, k):
    p = Integer(1)
    for r in range(1, k+1):
        p *= (a - r * E1)
    return p

def M_coeff(n):
    # M(T) = sum_{n>=2} (-1)^{n-1} (n^2-1)/n * E_1^{n-2} * T^n
    if n < 2:
        return Integer(0)
    return Integer((-1)**(n-1)) * Rational(n*n - 1, n) * E1**(n-2)

def A_coeff(k):
    return prod_falling(E2, k) / Integer(1)  # A_k^{(0)} = k! * A_k

def phi_from_AB(b):
    """phi_b = b! * [T^b] (A B) = sum_{k+l=b} C(b,k) * A_k^{(0)} * l! * B_l."""
    # Compute [T^b] of A B directly using power series.
    N = b + 1
    A_ser = sum(A_coeff(k) * Tsym**k / factorial(k) for k in range(N))
    E3_M = sum(E3 * M_coeff(n) * Tsym**n for n in range(2, N))
    B_ser = Integer(0)
    for p in range(0, N):
        B_ser += (E3_M ** p) / factorial(p)
    F_ser = expand(A_ser * B_ser)
    coeffs = Poly(F_ser, Tsym).as_dict()
    coeff_b = coeffs.get((b,), Integer(0))
    return expand(coeff_b * factorial(b))

def factorial(n):
    r = Integer(1)
    for i in range(2, n+1):
        r *= i
    return r

print("=== Verify tops[b] from closed form A * B matches tops from Psi ===")
for b in range(0, 6):
    phi = phi_from_AB(b)
    diff_val = expand(phi - tops_direct[b])
    print(f"  b={b}: {'OK' if diff_val == 0 else 'FAIL diff = ' + str(diff_val)}")

# ---- Verify: A*B satisfies the shift-ODE ----
print("\n=== Verify shift-ODE: (1+E_1 T) F' = (E_2-E_1) F - E_3 T (3+E_1 T) F_tilde ===")

# Since A_tilde = A * (1+E_1 T)^{-2} and B doesn't depend on E_2:
# F_tilde = A_tilde * B = A * B / (1+E_1 T)^2 = F / (1+E_1 T)^2.

# So the shift-ODE becomes:
#   (1+E_1 T) F' = (E_2 - E_1) F - E_3 T (3+E_1 T) * F/(1+E_1 T)^2
# Multiply both sides by (1+E_1 T)^2:
#   (1+E_1 T)^3 F' = (E_2 - E_1)(1+E_1 T)^2 F - E_3 T (3+E_1 T) F
# which is exactly the target ODE (1+E_1 T)^3 F' = [(E_2-E_1)(1+E_1 T)^2 - E_3 T(3+E_1 T)] F.

# Verify by expansion: for the closed form phi_b, does the shift-ODE hold at each T-order?
# (1+E_1 T) F' - (E_2-E_1) F + E_3 T (3+E_1 T) F_tilde = 0.
# Extract T^b coefficient (as EGF).

# LHS at T^b/b!:
#   (1+E_1 T) F' at T^b/b!:  phi[b+1] + E_1 * b * phi[b]
#   -(E_2-E_1) F at T^b/b!:  -(E_2-E_1) phi[b]
#   +E_3 T (3+E_1 T) F_tilde at T^b/b!:
#      3 E_3 * (b) * phi_tilde[b-1] + E_1 E_3 * b(b-1) * phi_tilde[b-2]
# Sum should be 0.

def sigma_top(P):
    return expand(P.subs(E2, E2 - 2*E1))

print("\nCheck shift-ODE at each b:")
for b in range(0, 6):
    phi_b = tops_direct[b]
    phi_bp1 = tops_direct[b+1] if b+1 in tops_direct else phi_from_AB(b+1)
    phi_tilde_bm1 = sigma_top(tops_direct[b-1]) if b >= 1 else Integer(0)
    phi_tilde_bm2 = sigma_top(tops_direct[b-2]) if b >= 2 else Integer(0)

    lhs = expand(
        phi_bp1 + E1 * b * phi_b
        - (E2 - E1) * phi_b
        + 3 * E3 * b * phi_tilde_bm1
        + E1 * E3 * b * (b-1) * phi_tilde_bm2
    )
    print(f"  b={b}: shift-ODE LHS = {lhs}  {'OK' if lhs == 0 else 'FAIL'}")
