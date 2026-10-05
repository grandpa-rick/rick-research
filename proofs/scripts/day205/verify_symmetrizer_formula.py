"""Lemma S: for f = f(X_1; tail) symmetric in the tail,
   sigma_m f = sum_i f(X_i; X without X_i) * prod_{j != i} (X_i - t X_j)/(X_i - X_j).
Also checks the WRONG orientation (t X_i - X_j)/(X_i - X_j) fails, and the
partial-fraction identity used in the induction step."""
import random
import sympy as sp
from common import sigma, Xs, e, t

def lemmaS_rhs(fun, m):
    X = Xs(m)
    tot = 0
    for i in range(m):
        rest = [X[j] for j in range(m) if j != i]
        w = sp.Mul(*[(X[i] - t*X[j])/(X[i] - X[j]) for j in range(m) if j != i])
        tot += fun(X[i], rest) * w
    return tot

def lemmaS_wrong(fun, m):
    X = Xs(m)
    tot = 0
    for i in range(m):
        rest = [X[j] for j in range(m) if j != i]
        w = sp.Mul(*[(t*X[i] - X[j])/(X[i] - X[j]) for j in range(m) if j != i])
        tot += fun(X[i], rest) * w
    return tot

random.seed(7)
ok = True
for m in range(1, 6):
    tests = []
    for a in range(0, 4):
        for r in range(0, m):
            tests.append((f"X1^{a} e_{r}(tail)", lambda x, rest, a=a, r=r: x**a * e(rest, r)))
    tests.append(("X1^2 e_1(tail)^2 e_2(tail)+X1 p_3(tail)",
                  lambda x, rest: x**2*e(rest,1)**2*e(rest,2) + x*sum(y**3 for y in rest)))
    for name, fun in tests:
        X = Xs(m)
        F = fun(X[0], list(X[1:]))
        lhs = sigma(F, m)
        d = sp.cancel(sp.together(lemmaS_rhs(fun, m) - lhs))
        ok &= (d == 0)
        if d != 0:
            print("FAIL", m, name)
    print(f"m={m}: {len(tests)} tests, all pass so far = {ok}")
# wrong orientation should fail at m=2
X = Xs(2)
fun = lambda x, rest: x
print("wrong orientation differs at m=2 (expected True):",
      sp.cancel(lemmaS_wrong(fun, 2) - sigma(X[0], 2)) != 0)
# partial fractions identity used in the induction step
for m in range(2, 7):
    X = Xs(m)
    lhs = sp.Mul(*[(X[0] - t*X[j])/(X[0] - X[j]) for j in range(1, m)])
    rhs = 1 + sum((1-t)*X[i]/(X[0]-X[i]) * sp.Mul(*[(X[i]-t*X[j])/(X[i]-X[j]) for j in range(1, m) if j != i]) for i in range(1, m))
    pf = sp.cancel(lhs - rhs) == 0
    ok &= pf
    print(f"partial-fraction identity m={m}: {pf}")
print("Lemma S:", "PASS" if ok else "FAIL")
