# Day 232 (b): symbolic check of the (C2) Bernstein derivation, from the 216c conventions (proof file 216b §9.0):
#   T_i F = t s_i F + (t-1) X_{i+1} (s_i F - F)/(X_i - X_{i+1});  pi F = F(X_2..X_m, s X_1);
#   Y_i = t^{m-i} T_{i-1}..T_1 pi T_{m-1}^{-1}..T_i^{-1},  T^{-1} := t^{-1} T - (1 - t^{-1})  (R4).
# twisted=True: Hikita/longversion pi f = x_1 f(x_2..x_m, s x_1) (paper's Y_i = 216c's Y^bullet).
# Tests on ALL monomials of degree <= 3, m = 3 and m = 4, symbolic s,t.
import sympy as sp, itertools, sys
s, t = sp.symbols('s t')
def setup(m, twisted=False):
    X = sp.symbols('X1:%d' % (m + 1))
    def T(i, F):  # 1-based i
        a, b = X[i - 1], X[i]
        sF = F.subs({a: b, b: a}, simultaneous=True)
        return sp.expand(t * sF + sp.cancel((t - 1) * b * (sF - F) / (a - b)))
    def Ti(i, F): return sp.expand(T(i, F) / t - (1 - 1 / t) * F)
    def pi(F): return sp.expand((X[0] if twisted else 1) * F.subs({X[j]: (X[j + 1] if j < m - 1 else s * X[0]) for j in range(m)}, simultaneous=True))
    def Yop(i, F):
        # word t^{m-i} T_{i-1}..T_1 pi T_{m-1}^{-1}..T_i^{-1}; rightmost factor T_i^{-1} acts first
        for k in range(i, m): F = Ti(k, F)
        F = pi(F)
        for k in range(1, i): F = T(k, F)
        return sp.expand(t ** (m - i) * F)
    return X, T, Ti, pi, Yop
def mons(X, d):
    out = []
    for deg in range(d + 1):
        for c in itertools.combinations_with_replacement(X, deg): out.append(sp.Mul(*c))
    return out
res = {}
def rec(name, val): res[name] = res.get(name, True) and val
for m, tw in ((3, False), (4, False), (3, True)):
    X, T, Ti, pi, Y = setup(m, tw)
    for F in mons(X, 3):
        z = lambda e: sp.simplify(e) == 0
        for i in range(1, m):
            rec('R4 quadratic (T-t)(T+1)=0', z(T(i, T(i, F)) - (t - 1) * T(i, F) - t * F))
            rec('R4 inverse T^{-1}T=1', z(Ti(i, T(i, F)) - F))
            rec('B2 T_iY_iT_i = tY_{i+1}', z(T(i, Y(i, T(i, F))) - t * Y(i + 1, F)))
            rec('(1) T_iY_i - Y_{i+1}T_i = -(t-1)Y_{i+1}', z(T(i, Y(i, F)) - Y(i + 1, T(i, F)) + (t - 1) * Y(i + 1, F)))
            rec('(2) T_iY_{i+1} - Y_iT_i = (t-1)Y_{i+1}', z(T(i, Y(i + 1, F)) - Y(i, T(i, F)) - (t - 1) * Y(i + 1, F)))
            rec('[T_i, Y_i+Y_{i+1}]=0', z(T(i, Y(i, F) + Y(i + 1, F)) - Y(i, T(i, F)) - Y(i + 1, T(i, F))))
            rec('[T_i, Y_iY_{i+1}]=0', z(T(i, Y(i, Y(i + 1, F))) - Y(i, Y(i + 1, T(i, F)))))
            for j in range(1, m + 1):
                if j in (i, i + 1): continue
                rec('far [T_i,Y_j]=0', z(T(i, Y(j, F)) - Y(j, T(i, F))))
            if i <= m - 2:
                rec('R3 pi T_i = T_{i+1} pi', z(pi(T(i, F)) - T(i + 1, pi(F))))
                rec('braid T_iT_{i+1}T_i', z(T(i, T(i + 1, T(i, F))) - T(i + 1, T(i, T(i + 1, F)))))
            for k in range(i + 2, m):
                rec('far T_iT_k=T_kT_i', z(T(i, T(k, F)) - T(k, T(i, F))))
        for i in range(1, m + 1):
            for j in range(i + 1, m + 1):
                rec('C1 Y_iY_j=Y_jY_i (import, checked)', z(Y(i, Y(j, F)) - Y(j, Y(i, F))))
        e = [lambda G: G, lambda G: sum(Y(i, G) for i in range(1, m + 1))]
        e2 = sum(Y(i, Y(j, F)) for i in range(1, m + 1) for j in range(i + 1, m + 1))
        for i in range(1, m):
            rec('[T_i, e_2(Y)]=0', z(T(i, e2) - sum(Y(a, Y(b, T(i, F))) for a in range(1, m + 1) for b in range(a + 1, m + 1))))
    print('m=%d twisted=%s done' % (m, tw), flush=True)
# negative control: B2 with t replaced by 1 on the right must fail
X, T, Ti, pi, Y = setup(3)
neg = any(sp.simplify(T(1, Y(1, T(1, F))) - Y(2, F)) != 0 for F in mons(X, 2))
for k, v in res.items(): print('%-45s %s' % (k, v))
print('negative control (T_1Y_1T_1 = Y_2, no t) fails as it should:', neg)
print('ALL:', all(res.values()))
