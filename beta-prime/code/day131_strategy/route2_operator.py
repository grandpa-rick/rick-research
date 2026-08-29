"""Route 2: Operator formula T(e_2^b · V) directly.

  T: monomial u_1^a u_2^b u_3^c |-> [u_1]_a [u_2]_b [u_3]_c  (falling factorials).
  Psi(f) = T(f V) / V,  V = (u1-u2)(u1-u3)(u2-u3).

Because T is a linear substitution on monomials, we can rewrite T(f V) in
terms of ordinary powers.  Study T(V), T(e_2 V), T(e_2^2 V), and look for
pattern that iterates cleanly.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (T_u, e1_u, e2_u, e3_u, V, Psi_direct,
                                 sym_to_ebasis_direct, E1, E2, E3)
from sympy import expand, Poly, Integer, factor, simplify, symbols, together

# First look at T(V):
TV = T_u(V)
print("T(V) =")
print(expand(TV))
print()
print("T(V) / V =")
q, r = Poly(TV, u1, u2, u3).div(Poly(V, u1, u2, u3))
print(f"quotient = {q.as_expr()}")
print(f"remainder = {r.as_expr()}")

print("\n--- T(e_2 V) ---")
TeV = T_u(expand(e2_u * V))
q1, r1 = Poly(TeV, u1, u2, u3).div(Poly(V, u1, u2, u3))
print(f"T(e_2 V) / V (should be symmetric = Psi(e_2)):")
print(f"  {q1.as_expr()}")
print(f"  remainder: {r1.as_expr()}  (should be 0)")

print("\n--- T(e_2^2 V) ---")
Te2V = T_u(expand(e2_u**2 * V))
q2, r2 = Poly(Te2V, u1, u2, u3).div(Poly(V, u1, u2, u3))
print(f"quotient (Psi(e_2^2)) = {sym_to_ebasis_direct(q2.as_expr())}")

# --- Key observation from Vandermonde/T interaction ---
# T is a "falling factorial substitution", which is the "Newton transform":
# it sends u^a to u(u-1)(u-2)...(u-a+1) = falling factorial (u)_a.
# Equivalently, T(u^a) = (u)_a = sum_k s(a,k) u^k  (signed Stirling 1st kind).
# Or, T applied to exp(x*u) gives exp(u * log(1+x)) in generating-function language.
# More usefully: T(u^a) = sum_k S1(a,k) u^k, i.e. T = "u -> (u)_a" is a
# TRIANGULAR change of basis in each u variable.
#
# Fact: T is the algebra homomorphism defined by T(u_i^n) = (u_i)_n, extended multiplicatively.
# So T(fg) = T(f)*T(g) is FALSE in general -- unless f, g are in disjoint variable sets.
# Actually T IS multiplicative because it's defined coordinate-wise on monomials:
# T(u_1^a u_2^b u_3^c) = (u_1)_a (u_2)_b (u_3)_c.  Hmm but T on u^2 = u(u-1) = u^2 - u,
# so T((u+v)^2)? Let me check.

from sympy import Rational
u = symbols('u')
# T(u^2) = u(u-1) = u^2 - u
# T((2u)^2) = T(4 u^2) = 4 (u^2 - u).
# But if T were "algebra hom" it should send 2u to something, then square.
# Actually T is INDUCED on the monomial basis. It's a linear map on polynomials.
# But is it multiplicative for polys in u alone?
# T(u^a * u^b) = T(u^{a+b}) = (u)_{a+b}. But T(u^a) T(u^b) = (u)_a (u)_b in general != (u)_{a+b}.
# So T is NOT multiplicative even in one variable.
# HOWEVER: for f in u_1, g in u_2, T(f g) = T(f) T(g) trivially since coordinate-wise.

# --- The multi-variable Vandermonde expansion ---
# V = det(u_i^{n-i}) = det(u_i^{2}, u_i^1, u_i^0) alternating sum.
# But we want to combine e_2^b · V and apply T.
# The KEY IDENTITY we need:  what is T(u_1^a u_2^b u_3^c · V)?
# Since T is defined on monomials, expand e_2^b V into monomials u_1^a u_2^b u_3^c
# and apply T to each.
# This is what the code does. Question: is there a CLOSED form?

# Alternative angle: T can be characterized by its action on exp(x*u_i):
#   T(sum x^a u^a / a!) = sum x^a (u)_a / a! = (1+x)^u  (since sum (u)_a x^a/a! = (1+x)^u)
# So T acts on generating functions by: sum_a f_a u^a / a! -> sum_a f_a (u)_a/a! -> in gen-fn,
# replace exp(xu) with (1+x)^u = exp(u log(1+x)).
# So if F(u; x) = sum f_a(u) x^a/a! and F(u; x) = phi(x)^u (for some scalar phi(x)),
# then T[F](u; x) := (1+phi(x)-1)^u ... hmm.
# Better: T(exp(x_1 u_1 + x_2 u_2 + x_3 u_3)) = exp(u_1 log(1+x_1)) * exp(u_2 log(1+x_2)) * exp(u_3 log(1+x_3))
# So T "replaces the exponential variables x_i with log(1+x_i)".
# In terms of formal power series: T[F(x_1,x_2,x_3)] = F(log(1+x_1), log(1+x_2), log(1+x_3)).

# So for Psi(f) = T(f V)/V, if we think of f V as a POLYNOMIAL and expand using
# monomials, we're evaluating (f V) at "log-substituted" points.

# --- Let's leverage the exp-generating-function form ---
# Consider Psi as a linear map on polynomials. We can characterize it by its
# generating-function image.
# f(u_1,u_2,u_3) has a generating expansion using dual "operator" variables.
# Actually let me try yet another angle: use the interpolation formula.

# --- Umbral: e_2^b · V decomposition ---
# V is antisymmetric.  e_2 is symmetric.  So e_2^b V is antisymmetric.
# Fact: T of an antisymmetric polynomial is antisymmetric?  T applies coordinate-wise,
# and permutation of coordinates commutes with T (each u_i is treated independently
# in the same way). So T commutes with S_3-action, hence T(antisymm) is antisymm.
# Therefore T(e_2^b V) is antisymmetric, hence divisible by V.

# --- e_2^b V in terms of "Schur-like" basis ---
# V has degree 3, e_2 has degree 2, so e_2^b V has degree 2b+3.
# Basis of antisymmetric polynomials of degree d in 3 vars: {V · h_lambda} for lambda partition.
# Actually antisymmetric polys are V · Sym.
# So e_2^b V = V * e_2^b (trivially), no help.

# --- Direct approach: Study T(V) first ---
# T(V) is antisymm.  T(V)/V = quotient.
# Compute: T(u_1^a u_2^b u_3^c) = (u_1)_a (u_2)_b (u_3)_c.
# V = sum_{sigma in S_3} sgn(sigma) u_{sigma(1)}^2 u_{sigma(2)}^1 u_{sigma(3)}^0
#   = sum_sigma sgn(sigma) prod_i u_{sigma(i)}^{3-i}
# Actually V has monomials u_1^2 u_2 - u_1^2 u_3 - u_1 u_2^2 + u_1 u_3^2 + u_2^2 u_3 - u_2 u_3^2.
# T(V) = sum sgn * (u_i)_{alpha_i} product.
# So T(V) = det[(u_i)_{n-j}]_{i,j=1..3}   where n=3, columns are (u_i)_2, (u_i)_1, (u_i)_0.
# So T(V) = det[(u_i)_2, u_i, 1] = "falling factorial Vandermonde"
# Well-known: this equals V! Actually,
#   det[(u_i)_{n-j}] = det[u_i^{n-j}] = V   because (u_i)_{n-j} = u_i^{n-j} + lower,
# and lower-degree monomials contribute to a lower-triangular perturbation of the
# Vandermonde matrix, which doesn't change the determinant.
# Let me verify:
print(f"\nT(V) = {expand(TV)}")
print(f"V    = {expand(V)}")
print(f"T(V) - V = {expand(TV - V)}")
