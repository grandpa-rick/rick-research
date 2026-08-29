"""Try ansätze for G(T) := sum sub_1[b] T^b/b!."""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct, e2_u,
                                 E1, E2, E3, weight_of_e_monom)
from sympy import (Poly, Integer, expand, diff, symbols, Rational, factorial,
                    log, binomial, series, prod, simplify, factor, together,
                    cancel, Symbol, Function, collect)

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


def series_trunc(P, var, N):
    """Truncate polynomial P to degrees < N in var."""
    p = Poly(P, var)
    out = Integer(0)
    for (deg,), c in p.terms():
        if deg < N:
            out += c * var**deg
    return expand(out)


# Compute tops[b] and sub_1[b] via direct Psi
NMAX = 8
tops = {0: Integer(1)}
sub1 = {0: Integer(0)}
psi = {0: Integer(1)}

for b in range(1, NMAX + 1):
    psi_u = Psi_direct(e2_u**b)
    psi[b] = sym_to_ebasis_direct(psi_u)
    tops[b] = weight_part(psi[b], b)
    sub1[b] = weight_part(psi[b], b - 1)

F = sum(tops[b] * T**b / factorial(b) for b in range(NMAX + 1))
G = sum(sub1[b] * T**b / factorial(b) for b in range(NMAX + 1))

print("F(T) coefficients [T^b/b!]:")
for b in range(NMAX + 1):
    print(f"  b={b}: {tops[b]}")

print("\nG(T) coefficients [T^b/b!]:")
for b in range(NMAX + 1):
    print(f"  b={b}: {sub1[b]}")

# Try: is G(T) = (some polynomial in T with poly-in-E coefficients) * F(T) + (something)?
# Since G has sub-top weight, and F has top weight, the "multiplier" must LOWER weight by 1.

# Attempt 1: compute G(T)/F(T) as series in T up to order 8.
# Since F(0) = 1, F is invertible as power series.
print("\n=== G(T)/F(T) truncated to T^8 ===")
# Compute F_inv up to T^8
F_p = Poly(expand(F), T)
G_p = Poly(expand(G), T)

def poly_to_dict(P):
    p = Poly(P, T)
    d = {}
    for (deg,), c in p.terms():
        d[deg] = c
    return d

Fd = poly_to_dict(F)
Gd = poly_to_dict(G)
# Compute quotient G = Q * F, solve for Q up to T^8
Q = {}
NMAX_T = NMAX
for k in range(NMAX_T + 1):
    # [T^k] G = sum_{i+j=k} Q_i F_j
    rhs = Gd.get(k, Integer(0)) - sum(Q[i] * Fd.get(k - i, Integer(0)) for i in range(k))
    # F_0 = 1, so Q_k = rhs.
    Q[k] = expand(rhs)

print("G(T)/F(T) as series:")
for k in sorted(Q):
    if Q[k] != 0:
        print(f"  T^{k}: {Q[k]}")


# Attempt 2: (1 + E1 T) * G(T) / F(T)
print("\n=== (1 + E1 T) * G(T) / F(T) ===")
GF = expand((1 + E1 * T) * sum(Q[k] * T**k for k in Q))
GFp = poly_to_dict(GF)
for k in sorted(GFp):
    if GFp[k] != 0 and k <= NMAX:
        print(f"  T^{k}: {GFp[k]}")


# Attempt 3: Compute G(T) * (1 + E1 T)^2 / F(T)^2 or similar
print("\n=== G(T)^2 / F(T)... no, try G(T)/(T F(T)) since sub_1[0]=0 ===")
# G(T) = T + O(T^2), so G/T is a series.
if all(Gd.get(0, Integer(0)) == 0 for _ in [0]):
    # Divide by T
    G_over_T_d = {k-1: Gd[k] for k in Gd if k >= 1}
    print("G(T)/T coefficients (T^b for b = 0..):")
    for b in sorted(G_over_T_d):
        print(f"  T^{b}: {G_over_T_d[b]}")

    # Then (G/T) / F
    Q2 = {}
    for k in range(NMAX_T):
        rhs = G_over_T_d.get(k, Integer(0)) - sum(Q2[i] * Fd.get(k - i, Integer(0)) for i in range(k))
        Q2[k] = expand(rhs)
    print("\nG(T)/(T F(T)) as series:")
    for k in sorted(Q2):
        if Q2[k] != 0:
            print(f"  T^{k}: {Q2[k]}")


# Attempt 4: try G(T)*(1 + E1 T)/F(T) - some derivative combination
print("\n=== Direct comparison to derivatives ===")
# Compute T F'(T), T^2 F''(T), etc.
F_expr = expand(F)
Fprime = diff(F_expr, T)
Fpp = diff(Fprime, T)
print("[T^b/b!] T F'(T) is b*tops[b]. So T F'(T) has weight-preserving b tops[b].")
print("[T^b/b!] T^2 F''(T) is b(b-1) tops[b].")

# Try G vs c1 * T F' + c2 * T^2 F'' (with c_i involving E)
# But sub_1[b] doesn't have full weight b, so these don't match directly.
