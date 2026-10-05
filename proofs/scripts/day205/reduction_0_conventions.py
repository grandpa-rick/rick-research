"""
Day 205, step 0: conventions.
 (a) The engine's T_i, T_i^{-1}, pi, Y_i agree EXACTLY with the Day 198 SymPy
     build_action (the code in which Sub-Lemma Z was checked) on random
     polynomials, m = 2..4.
 (b) Clio's form T_i f = t f + (t x_i - x_{i+1})/(x_i - x_{i+1}) (s_i f - f)
     agrees with the code's form (symbolic identity).
 (c) Hecke quadratic relation (T_i - t)(T_i + 1) = 0 and braid relations on
     random polynomials; T_i^{-1} T_i = id.
 (d) T_i F = t F for symmetric F; Y_i . 1 = X_i; e_1(Y) . 1 = e_1.
"""
import sys, random
import sympy as sp
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day198')
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day205')
from p2Y_er import build_action
from reduction_engine import *

q, t = sp.symbols('q t')
random.seed(205)
ok = True

def to_sympy(P, m):
    X = sp.symbols(f'X1:{m+1}')
    out = 0
    for e, c in P.items():
        cc = sum(v * t**te * q**(-Qe) for (te, Qe), v in c.items())
        out += cc * sp.prod([X[j]**e[j] for j in range(m)])
    return sp.expand(out)

def rand_poly(m, deg=3, nterms=5):
    P = {}
    for _ in range(nterms):
        e = [0] * m
        for _ in range(random.randint(0, deg)):
            e[random.randrange(m)] += 1
        p_add_term(P, tuple(e), c_int(random.randint(-3, 3)))
    return P

# (a)
for m in [2, 3, 4]:
    X, Ti, Tii, Pi, Ya = build_action(m)
    for trial in range(4):
        P = rand_poly(m)
        F = to_sympy(P, m)
        checks = []
        for i in range(1, m):
            checks.append((f"T_{i}", to_sympy(T(P, i), m), Ti(F, i)))
            checks.append((f"T_{i}^-1", to_sympy(Tinv(P, i), m), Tii(F, i)))
        checks.append(("pi", to_sympy(PI(P), m), Pi(F)))
        for i in range(1, m + 1):
            checks.append((f"Y_{i}", to_sympy(Y(P, i, m), m), Ya(F, i)))
        for name, a, b in checks:
            if sp.simplify(sp.expand(a - b)) != 0:
                ok = False
                print(f"  (a) MISMATCH m={m} {name}")
print("(a) engine == Day 198 build_action on random inputs, m=2,3,4:", ok)

# (b)
x1, x2, f1 = sp.symbols('x1 x2 f1')
F = sp.Function('F')
f, sf = F(x1, x2), F(x2, x1)
code = t * sf + (t - 1) * (-x2) * (f - sf) / (x1 - x2)
clio = t * f + (t * x1 - x2) / (x1 - x2) * (sf - f)
b_ok = sp.simplify(code - clio) == 0
ok &= b_ok
print("(b) code T_i == Clio's T_i (symbolic):", b_ok)

# (c)
c_ok = True
for m in [3, 4, 5]:
    for trial in range(3):
        P = rand_poly(m, deg=4, nterms=6)
        for i in range(1, m):
            TP = T(P, i)
            quad = p_add(p_add(T(TP, i), {e: c_shift(c, dt=1) for e, c in TP.items()}, -1),
                         p_add(TP, {e: c_shift(c, dt=1) for e, c in P.items()}, -1))
            # (T-t)(T+1) = T^2 + T - tT - t
            c_ok &= p_is_zero(quad)
            c_ok &= p_is_zero(p_add(Tinv(TP, i), P, -1))
            if i + 1 < m:
                lhs = T(T(T(P, i), i + 1), i)
                rhs = T(T(T(P, i + 1), i), i + 1)
                c_ok &= p_is_zero(p_add(lhs, rhs, -1))
            for j in range(i + 2, m):
                c_ok &= p_is_zero(p_add(T(T(P, i), j), T(T(P, j), i), -1))
ok &= c_ok
print("(c) quadratic, inverse, braid, far-commutation on random inputs m=3,4,5:", c_ok)

# (d)
d_ok = True
for m in [2, 3, 4, 5, 6]:
    one = {tuple([0] * m): dict(ONE)}
    for i in range(1, m + 1):
        d_ok &= p_is_zero(p_add(Y(one, i, m), var(m, i), -1))
    d_ok &= p_is_zero(p_add(e1Y(one, m), e_sym(m, 1), -1))
    for mu in [(1,), (2,), (2, 1), (3, 1)]:
        G = e_lam(m, mu)
        for i in range(1, m):
            d_ok &= p_is_zero(p_add(T(G, i), {e: c_shift(c, dt=1) for e, c in G.items()}, -1))
ok &= d_ok
print("(d) T_i F = tF (F symmetric), Y_i.1 = X_i, e_1(Y).1 = e_1, m=2..6:", d_ok)
# (e)
e_ok = True
for r in range(1, 8):
    for m in range(2, r + 4):
        er = e_sym(m, r)
        rhs = p_add(p_scale(e_sym(m, r + 1), c_mul(c_add(ONE, c_Q(1), sb=-1), tint(r + 1))),
                    p_scale(p_mul(e_sym(m, 1), er), c_Q(1)))
        e_ok &= p_is_zero(p_add(e1Y(er, m), rhs, -1))
        X1 = var(m, 1)
        a = sigma(p_mul(X1, e_tail(m, r)), m)
        b = sigma(p_mul(p_mul(X1, X1), e_tail(m, r - 1)), m)
        e_ok &= p_is_zero(p_add(a, p_scale(e_sym(m, r + 1), tint(r + 1)), -1))
        e_ok &= p_is_zero(p_add(b, p_add(p_mul(e_sym(m, 1), er), p_scale(e_sym(m, r + 1), tint(r + 1)), -1), -1))
ok &= e_ok
print("(e) Hikita Thm 3.12 reproduced by the code's e_1(Y), and via pi-split + Clio (5),(6):", e_ok)
print("STEP 0 OVERALL:", "PASSED" if ok else "FAILED")
