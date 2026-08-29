"""Corrected reduction library."""
from sympy import symbols, expand, S, Poly
from itertools import permutations

s, y, t = symbols('s y t')
u1, u2, u3 = symbols('u1 u2 u3')

def reduce_y(P):
    """Reduce mod y^2 - sy + t. Bug-fixed version."""
    P = expand(P)
    poly = Poly(P, y, s, t)
    result = S.Zero
    for monom, coef in poly.as_dict().items():
        yk, sm, tn = monom
        # Compute y^yk = f + g*y via recurrence
        # f_0=1, g_0=0; f_1=0, g_1=1; f_{k+1}=-t*g_k, g_{k+1}=f_k+s*g_k
        if yk == 0:
            f_val, g_val = S.One, S.Zero
        elif yk == 1:
            f_val, g_val = S.Zero, S.One
        else:
            f_prev, g_prev = S.Zero, S.One  # k=1
            for k in range(1, yk):
                f_new = -t * g_prev
                g_new = f_prev + s * g_prev
                f_prev, g_prev = f_new, g_new
            f_val, g_val = f_prev, g_prev
        result += coef * (s**sm) * (t**tn) * (f_val + g_val*y)
    return expand(result)

def falling(x, n):
    p = S.One
    for i in range(n):
        p *= (x - i)
    return expand(p)

def apply_S(P_u):
    return P_u.subs({u1: t, u2: y, u3: s - y})

def apply_T_then_S(P_u):
    P_u = expand(P_u)
    poly = Poly(P_u, u1, u2, u3)
    result = S.Zero
    for monom, coef in poly.as_dict().items():
        a, b, c = monom
        Tm = falling(t, a) * falling(y, b) * falling(s - y, c)
        result += coef * Tm
    return expand(result)

def antisym_orbit(alpha):
    us = (u1, u2, u3)
    result = S.Zero
    for perm in permutations(range(3)):
        sign = 1
        for i in range(3):
            for j in range(i+1, 3):
                if perm[i] > perm[j]:
                    sign *= -1
        term = 1
        for i, p in enumerate(perm):
            term *= us[i]**alpha[p]
        result += sign * term
    return expand(result)

def tau_deg(P):
    P = expand(P)
    if P == 0:
        return -1
    return Poly(P, t).degree()

def top_tau(P):
    d = tau_deg(P)
    if d < 0:
        return S.Zero
    return Poly(P, t).coeff_monomial(t**d)
