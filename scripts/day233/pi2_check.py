# Day 233: extended affine Hecke presentation check for T_1..T_{m-1}, pi (untwisted pi_0 and twisted pi = x_1 pi_0).
# Conventions copied verbatim from scripts/day232/c2_check.py (216c / longversion l.90-96):
#   T_i F = t s_i F + (t-1) X_{i+1}(s_i F - F)/(X_i - X_{i+1});  pi_0 F = F(X_2..X_m, s X_1);  pi = X_1 pi_0 (twisted)
#   Y_i = t^{m-i} T_{i-1}..T_1 pi T_{m-1}^{-1}..T_i^{-1},  T^{-1} := t^{-1}T - (1-t^{-1}).
# Presentation (GL_m extended affine Hecke, T_0 eliminated): (a) quadratic, (b) braid+far, (c) pi T_i pi^{-1}=T_{i+1} (i<=m-2),
# (d) pi^2 T_{m-1} pi^{-2} = T_1 [checked in the inverse-free form pi^2 T_{m-1} = T_1 pi^2], (e) pi invertible.
import sympy as sp, itertools
s, t = sp.symbols('s t')
def setup(m, twisted):
    X = sp.symbols('X1:%d' % (m + 1))
    def T(i, F):
        a, b = X[i - 1], X[i]
        sF = F.subs({a: b, b: a}, simultaneous=True)
        return sp.expand(t * sF + sp.cancel((t - 1) * b * (sF - F) / (a - b)))
    def Ti(i, F): return sp.expand(T(i, F) / t - (1 - 1 / t) * F)
    def pi(F): return sp.expand((X[0] if twisted else 1) * F.subs({X[j]: (X[j + 1] if j < m - 1 else s * X[0]) for j in range(m)}, simultaneous=True))
    def piinv(G):  # inverse on Laurent polys: z -> (z_m/s, z_1, ..., z_{m-1}), times s/z_m if twisted
        H = G.subs({X[0]: X[m - 1] / s, **{X[j]: X[j - 1] for j in range(1, m)}}, simultaneous=True)
        return sp.expand((s / X[m - 1] if twisted else 1) * H)
    def Y(i, F):
        for k in range(i, m): F = Ti(k, F)
        F = pi(F)
        for k in range(1, i): F = T(k, F)
        return sp.expand(t ** (m - i) * F)
    return X, T, Ti, pi, piinv, Y
def mons(X, d, lo=0):
    out = []
    for e in itertools.product(range(lo, d + 1), repeat=len(X)):
        if sum(abs(a) for a in e) <= d: out.append(sp.Mul(*[x ** a for x, a in zip(X, e)]))
    return out
z = lambda e: sp.simplify(e) == 0
ALL = True
for m in (3, 4):
    for tw in (False, True):
        X, T, Ti, pi, piinv, Y = setup(m, tw)
        res = {}
        def rec(k, v):
            res[k] = res.get(k, True) and v
        P = mons(X, 3)                 # polynomials, deg<=3
        L = mons(X, 3, lo=-1)          # Laurent monomials, exponents in [-1,3], sum|e|<=3
        for F in P:
            for i in range(1, m):
                rec('(a) (T_i-t)(T_i+1)=0', z(T(i, T(i, F)) - (t - 1) * T(i, F) - t * F))
                if i <= m - 2:
                    rec('(b) braid', z(T(i, T(i + 1, T(i, F))) - T(i + 1, T(i, T(i + 1, F)))))
                    rec('(c) pi T_i = T_{i+1} pi', z(pi(T(i, F)) - T(i + 1, pi(F))))
                for k in range(i + 2, m): rec('(b) far', z(T(i, T(k, F)) - T(k, T(i, F))))
            rec('(d) pi^2 T_{m-1} = T_1 pi^2', z(pi(pi(T(m - 1, F))) - T(1, pi(pi(F)))))
            # pi^m central (consequence of (c)+(d)); check vs T_1
            pm = lambda G: [G := pi(G) for _ in range(m)][-1]
            rec('pi^m T_1 = T_1 pi^m (consequence)', z(pm(T(1, F)) - T(1, pm(F))))
            # negative control: pi T_{m-1} = T_1 pi (wrong: T_0 not T_1) must FAIL somewhere
            res.setdefault('NEG pi T_{m-1} = T_1 pi holds everywhere (want False)', True)
            res['NEG pi T_{m-1} = T_1 pi holds everywhere (want False)'] &= z(pi(T(m - 1, F)) - T(1, pi(F)))
            for i in range(1, m + 1):
                for j in range(i + 1, m + 1):
                    rec('C1 Y_iY_j=Y_jY_i', z(Y(i, Y(j, F)) - Y(j, Y(i, F))))
        for F in L:  # Laurent: invertibility and the inverse forms of (c),(d)
            rec('(e) pi piinv = 1 = piinv pi (Laurent)', z(pi(piinv(F)) - F) and z(piinv(pi(F)) - F))
            for i in range(1, m - 1):
                rec('(c) Laurent pi T_i piinv = T_{i+1}', z(pi(T(i, piinv(F))) - T(i + 1, F)))
            rec('(d) Laurent pi^2 T_{m-1} pi^{-2} = T_1', z(pi(pi(T(m - 1, piinv(piinv(F))))) - T(1, F)))
            rec('(a) Laurent quadratic', all(z(T(i, T(i, F)) - (t - 1) * T(i, F) - t * F) for i in range(1, m)))
        # (e) on Pol: is pi surjective onto Pol? test whether piinv maps Pol into Pol
        surj = all(not (sp.fraction(sp.together(piinv(F)))[1].free_symbols & set(X)) for F in P)  # denominators in X only (1/s is a scalar)
        res['(e) pi^{-1}(Pol) subset Pol, i.e. pi bijective on Pol'] = surj
        print('=== m=%d twisted=%s  (#Pol mons=%d, #Laurent mons=%d)' % (m, tw, len(P), len(L)))
        for k, v in res.items():
            print('  %-58s %s' % (k, v))
            if not k.startswith('NEG') and not k.startswith('(e) pi^{-1}(Pol)'): ALL &= v
print('ALL relation checks (excluding NEG and the Pol-surjectivity probe):', ALL)
