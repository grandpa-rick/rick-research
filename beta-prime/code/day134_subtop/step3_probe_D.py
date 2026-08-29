"""Compute D(tops[b]) for various b. Look for closed form.
Then compute G(T) via generating-function ansatz.

D(tops[0]) = 0
D(tops[1]) = 6
D(tops[2]) = 18(E2 - 3E1)
D(tops[3]) = ?
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct, e2_u,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import (Poly, Integer, expand, diff, symbols, Rational, factorial,
                    Symbol, factor, collect, simplify, Add)

T = Symbol('T')


def weight_part(P, w):
    P = expand(P)
    if P == 0:
        return Integer(0)
    p = Poly(P, E1, E2, E3)
    out = Integer(0)
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        if i + j + 2*k == w:
            out += coeff * E1**i * E2**j * E3**k
    return out


def sigma_top(P):
    return expand(P.subs(E2, E2 - 2*E1))


def D_op(P):
    P = expand(P)
    d1 = diff(P, E1)
    d2 = diff(P, E2)
    d3 = diff(P, E3)
    return expand(-3 * sigma_top(d1) + 3 * sigma_top(d2) + (E1 - E2) * sigma_top(d3))


# Compute tops[b]
NMAX = 8
tops = {0: Integer(1)}
sub1 = {0: Integer(0)}
for b in range(1, NMAX + 1):
    psi_u = Psi_direct(e2_u**b)
    psi_e = sym_to_ebasis_direct(psi_u)
    tops[b] = weight_part(psi_e, b)
    sub1[b] = weight_part(psi_e, b - 1)

print("=== D(tops[b]) for b = 0..NMAX ===")
Dtops = {}
for b in range(NMAX + 1):
    Dtops[b] = D_op(tops[b])
    print(f"  b={b}: D(tops[{b}]) = {Dtops[b]}")

# Guess: is D(tops[b]) = c(b) · (something involving tops[b-1])?
# For b=1: D = 6. tops[0] = 1. So c(1) = 6.
# For b=2: D = 18 E_2 - 54 E_1 = 18(E_2 - 3E_1). tops[1] = E_2 - E_1. Not a scalar multiple.

# Let me try: is D(tops[b]) = a·tops[b-1] + b·(E_2 - c E_1)·tops[b-2] + ... ?
# Or: is D(tops[b])/sub_1[b]? Same weight class...
# Both D(tops[b]) and sub_1[b] have weight b-1.

print("\n=== D(tops[b]) vs sub_1[b] (both weight b-1) ===")
for b in range(1, NMAX + 1):
    print(f"  b={b}: D(tops[{b}]) = {Dtops[b]}")
    print(f"        sub_1[{b}]    = {sub1[b]}")

# Try: sub_1[b] = alpha_b · D(tops[b]) + beta_b · (other)?
# Compute ratio sub_1[b]/D(tops[b]) for a specific coefficient (say pure-E1):
print("\n=== [E1^{b-1}] ratio sub_1/D(tops) ===")
for b in range(1, NMAX + 1):
    p_sub = Poly(sub1[b], E1, E2, E3)
    p_D = Poly(Dtops[b], E1, E2, E3)
    ce1_sub = p_sub.coeff_monomial((b-1, 0, 0))
    ce1_D = p_D.coeff_monomial((b-1, 0, 0))
    r = Rational(ce1_sub, ce1_D) if ce1_D != 0 else None
    print(f"  b={b}: sub_1[E1^{b-1}]={ce1_sub}, D(tops)[E1^{b-1}]={ce1_D}, ratio={r}")

# Look at F(T) generating function derivatives
F_series = sum(tops[b] * T**b / factorial(b) for b in range(NMAX + 1))
G_series = sum(sub1[b] * T**b / factorial(b) for b in range(NMAX + 1))

# Compute D(F) as series
DF_series = sum(Dtops[b] * T**b / factorial(b) for b in range(NMAX + 1))

# Is D(F) = c1 · T · F'(T) + c2 · F(T) + ... where c_i involve E1, E2, E3?
# D(F) has weight-(b-1) coeff at T^b/b!.
# F has weight-b coeff at T^b/b!.
# T · F'(T) has [T^b/b!] = b · tops[b], weight b. Not matching.

# Let's try: D(F) = 3 · ∂ F/∂E_2 - 3 · ∂F/∂E_1 (something like this, without the σ_top)
# We had D(F)/F̃ has L=log(1+E1 T) term. Let me just compute D(F)/F̃ symbolically to see structure.

print("\n=== D(F)/(F/(1+E1 T)^2) as series ===")
Ftilde = expand(F_series.subs(E2, E2 - 2*E1))
# D(F)/Ftilde
# Compute via Taylor
F_dict = Poly(F_series, T).as_dict()
Ft_dict = Poly(Ftilde, T).as_dict()
DF_dict = Poly(DF_series, T).as_dict()

def as_series_coeffs(poly_expr, N):
    p = Poly(poly_expr, T)
    d = {}
    for (deg,), c in p.terms():
        d[deg] = c
    return {k: d.get(k, Integer(0)) for k in range(N)}

Fs = as_series_coeffs(F_series, NMAX+1)
Fts = as_series_coeffs(Ftilde, NMAX+1)
DFs = as_series_coeffs(DF_series, NMAX+1)

# Compute DF / Ft as series: solve DF_k = sum_i Q_i Ft_{k-i}, Q_0 · Ft_0 = DF_0
# Ft_0 = F(0) = 1, so Q_k = DF_k − Σ_{i<k} Q_i Ft_{k-i}
Q = {}
for k in range(NMAX + 1):
    rhs = DFs[k] - sum(Q[i] * Fts[k-i] for i in range(k))
    Q[k] = expand(rhs)

print("D(F)/F̃ as power series in T:")
for k in range(NMAX + 1):
    if Q[k] != 0:
        # Factor if possible
        try:
            f = factor(Q[k])
            print(f"  T^{k}: {f}")
        except:
            print(f"  T^{k}: {Q[k]}")
