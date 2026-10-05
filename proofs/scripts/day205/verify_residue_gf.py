"""Residue / generating-function closed form (Day 205, Prop. G).

For a >= 1, all m >= 1, as an identity of rational functions in z:
  E(z) * sum_i X_i^a/(1+z X_i) * prod_{j!=i} (X_i - tX_j)/(X_i - X_j)
    = (1/(1-t)) * [ (-1)^a z^{-a} E(tz) + sum_{n=0}^{a-1} (-1)^{a-1-n} q_n z^{n-a} E(z) ],
where E(z) = prod_j (1+z X_j) and q_n = sum_k (-t)^k e_k h_{n-k} (Hall-Littlewood q_n).
Coefficient of z^r gives (Cor. G):
  sigma_m[X_1^a e_r(tail)] = (1/(1-t)) [ (-1)^a t^{r+a} e_{r+a}
                                         + sum_{n=0}^{a-1} (-1)^{a-1-n} q_n e_{r+a-n} ].
Also checks the three intermediate residue facts:
  (i)  Res_{u=X_i} A(u) = (1-t) X_i prod_{j!=i} d(X_i,X_j),  A(u) = prod (u - tX_j)/(u - X_j)
  (ii) A(-1/z) = E(tz)/E(z)
  (iii) A(u) = sum_n q_n u^{-n} (checked to order 4)
"""
import sympy as sp
from common import Xs, e, t

z, u = sp.symbols('z u')

def h(vars_, n):
    if n < 0: return sp.Integer(0)
    if n == 0: return sp.Integer(1)
    from itertools import combinations_with_replacement
    return sp.Add(*[sp.Mul(*c) for c in combinations_with_replacement(vars_, n)])

def qn(vars_, n):
    return sp.expand(sum((-t)**k * e(vars_, k) * h(vars_, n-k) for k in range(n+1)))

ok = True
for m in range(1, 6):
    X = Xs(m)
    E = lambda w: sp.Mul(*[1 + w*x for x in X])
    A = sp.Mul(*[(u - t*x)/(u - x) for x in X])
    # (i)
    for i in range(m):
        res = sp.cancel(((u - X[i]) * A).subs(u, X[i]))
        want = (1-t)*X[i]*sp.Mul(*[(X[i]-t*X[j])/(X[i]-X[j]) for j in range(m) if j != i])
        ok &= sp.cancel(res - want) == 0
    # (ii)
    ok &= sp.cancel(A.subs(u, -1/z) - E(t*z)/E(z)) == 0
    # (iii)
    w = sp.symbols('w')
    ser = sp.series(A.subs(u, 1/w), w, 0, 5).removeO()
    for n in range(5):
        ok &= sp.expand(ser.coeff(w, n) - qn(X, n)) == 0
    # main GF identity, a = 1..4
    for a in range(1, 5):
        lhs = E(z) * sum(X[i]**a/(1+z*X[i]) * sp.Mul(*[(X[i]-t*X[j])/(X[i]-X[j]) for j in range(m) if j != i]) for i in range(m))
        rhs = ((-1)**a * z**(-a) * E(t*z) + sum((-1)**(a-1-n) * qn(X, n) * z**(n-a) for n in range(a)) * E(z)) / (1-t)
        good = sp.cancel(sp.together(lhs - rhs)) == 0
        ok &= good
        print(f"m={m}, a={a}: GF identity {good}", flush=True)

# Specializations a=1,2,3 as symmetric-function identities (general m via q_1, q_2):
e1, e2 = sp.symbols('e1 e2')
q1 = (1-t)*e1
q2 = (1-t)*e1**2 - (1-t**2)*e2
print("q_1, q_2 formulas:",
      all(sp.expand(qn(Xs(4), 1) - q1.subs({e1: e(Xs(4), 1)})) == 0 for _ in [0]),
      sp.expand(qn(Xs(4), 2) - q2.subs({e1: e(Xs(4), 1), e2: e(Xs(4), 2)})) == 0)
print("Prop G:", "PASS" if ok else "FAIL")
