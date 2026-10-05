"""Day 205 common: EXACT Day 198/204 Demazure-Lusztig convention, re-implemented with
Poly arithmetic for speed, and cross-checked against build_action (day198/p2Y_er.py).

Convention (day198 p2Y_er.build_action.Ti_apply):
    T_i F = t s_i F + (t-1)(-X_{i+1}) (F - s_i F)/(X_i - X_{i+1})
"""
import sympy as sp
from itertools import combinations

t = sp.symbols('t')

def Xs(m):
    return sp.symbols(f'X1:{m+1}')

def e(vars_, r):
    if r < 0 or r > len(vars_):
        return sp.Integer(0)
    if r == 0:
        return sp.Integer(1)
    return sp.Add(*[sp.Mul(*c) for c in combinations(vars_, r)])

def qint(n):
    return sp.Add(*[t**i for i in range(n)]) if n > 0 else sp.Integer(0)

def make_T(m):
    X = Xs(m)
    gens = list(X) + [t]
    def T(P, i):  # P: Poly in gens; i in 1..m-1
        a, b = X[i-1], X[i]
        sP = P.as_expr().xreplace({a: b, b: a})
        sP = sp.Poly(sP, *gens)
        diff = P - sP
        quot, rem = sp.div(diff, sp.Poly(a - b, *gens))
        assert rem.is_zero
        return sP * t + quot * sp.Poly((t - 1) * (-b), *gens)
    return T, gens

def sigma(F, m):
    """sigma_m F = sum_{k=0}^{m-1} T_k ... T_1 F  (T_1 applied first)."""
    T, gens = make_T(m)
    P = sp.Poly(sp.expand(F), *gens)
    total = P
    cur = P
    for k in range(1, m):
        cur = T(cur, k)          # cur = T_k T_{k-1} ... T_1 F
        total = total + cur
    return total.as_expr()
