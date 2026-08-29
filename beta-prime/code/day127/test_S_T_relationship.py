"""Test: does S(T(P)) = S(P) for some class? For antisymmetric P?"""
from sympy import symbols, expand, S, Poly, factor
from itertools import permutations

s, y, t = symbols('s y t')
u1, u2, u3 = symbols('u1 u2 u3')

def reduce_y(P):
    P = expand(P)
    poly = Poly(P, y, s, t)
    result = S.Zero
    for monom, coef in poly.as_dict().items():
        yk, sm, tn = monom
        if yk == 0:
            f, g = 1, 0
        elif yk == 1:
            f, g = 0, 1
        else:
            f, g = 1, 0
            fk, gk = 0, 1
            for _ in range(yk - 1):
                fk_new = -t * gk
                gk_new = f + s * gk
                f, g = fk, gk
                fk, gk = fk_new, gk_new
            f, g = fk, gk
        result += coef * (s**sm) * (t**tn) * (f + g*y)
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

def sym_orbit(alpha):
    """Symmetric orbit: sum over all distinct permutations."""
    us = (u1, u2, u3)
    seen = set()
    result = S.Zero
    for perm in permutations(range(3)):
        key = tuple(alpha[p] for p in perm)
        if key in seen: continue
        seen.add(key)
        term = 1
        for i, p in enumerate(perm):
            term *= us[i]**alpha[p]
        result += term
    return expand(result)

V = antisym_orbit((2, 1, 0))
SV = reduce_y(apply_S(V))
STV = reduce_y(apply_T_then_S(V))
print(f"S(V) = {SV}")
print(f"S(T(V)) = {STV}")
print(f"S(V) - S(T(V)) = {expand(SV - STV)}\n")

# Test more antisym orbits
print("Antisymmetric orbit sums a_α: is S(T(a_α)) = S(a_α)?")
matches = 0
tests = 0
diffs_lower = 0
for A in range(6):
    for B in range(A):
        for C in range(B):
            alpha = (A, B, C)
            g = antisym_orbit(alpha)
            Sg = reduce_y(apply_S(g))
            STg = reduce_y(apply_T_then_S(g))
            diff = expand(STg - Sg)
            eq = (diff == 0)
            d_g = Poly(Sg, t).degree() if Sg != 0 else -1
            d_diff = Poly(diff, t).degree() if diff != 0 else -1
            tests += 1
            if eq:
                matches += 1
                mark = "EQUAL"
            else:
                if d_diff < d_g:
                    diffs_lower += 1
                    mark = f"drop τ-deg {d_g}->{d_diff}"
                else:
                    mark = f"SAME τ-deg {d_g}={d_diff}!"
            print(f"  α={alpha}: {mark}")

print(f"\n{matches}/{tests} exactly equal, {diffs_lower}/{tests} have diff of strictly lower τ-deg")

# Now test on fV for symmetric monomials
print("\n\nTest: for f = symmetric monomial, is S(T(fV)) = S(fV)? Or does diff have lower τ-deg?")
for a1, a2, a3 in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,2,0),(2,0,0),(0,3,0),(1,0,1),(0,1,1)]:
    e1 = u1 + u2 + u3
    e2 = u1*u2 + u1*u3 + u2*u3
    e3 = u1*u2*u3
    f = expand(e1**a1 * e2**a2 * e3**a3)
    fV = expand(f * V)
    S_fV = reduce_y(apply_S(fV))
    ST_fV = reduce_y(apply_T_then_S(fV))
    d_fV = Poly(S_fV, t).degree() if S_fV != 0 else -1
    d_ST = Poly(ST_fV, t).degree() if ST_fV != 0 else -1
    diff = expand(ST_fV - S_fV)
    d_diff = Poly(diff, t).degree() if diff != 0 else -1
    print(f"  f = e1^{a1}·e2^{a2}·e3^{a3}: τ-deg(fV)={d_fV}, τ-deg(T(fV))={d_ST}, τ-deg(diff)={d_diff}")
