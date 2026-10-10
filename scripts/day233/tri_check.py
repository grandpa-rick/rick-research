# Day 233: triangularity of the UNTWISTED Y_i on monomials x^lam (Pol_d, m=3 d<=3; m=4 d<=2), symbolic s,t.
# Same operator conventions as pi2_check.py / day232 c2_check.py.
import sympy as sp, itertools, sys
sys.path.insert(0, '.')
s, t = sp.symbols('s t')
def setup(m):
    X = sp.symbols('X1:%d' % (m + 1))
    def T(i, F):
        a, b = X[i - 1], X[i]
        sF = F.subs({a: b, b: a}, simultaneous=True)
        return sp.expand(t * sF + sp.cancel((t - 1) * b * (sF - F) / (a - b)))
    def Ti(i, F): return sp.expand(T(i, F) / t - (1 - 1 / t) * F)
    def pi(F): return sp.expand(F.subs({X[j]: (X[j + 1] if j < m - 1 else s * X[0]) for j in range(m)}, simultaneous=True))
    def Y(i, F):
        for k in range(i, m): F = Ti(k, F)
        F = pi(F)
        for k in range(1, i): F = T(k, F)
        return sp.expand(t ** (m - i) * F)
    return X, Y
def comps(m, d): return [c for c in itertools.product(range(d + 1), repeat=m) if sum(c) == d]
def dom_leq(a, b):  # partitions a <= b in dominance
    pa, pb = sorted(a, reverse=True), sorted(b, reverse=True); sa = sb = 0
    for x, y in zip(pa, pb):
        sa += x; sb += y
        if sa > sb: return False
    return True
def inv(c): return sum(1 for i in range(len(c)) for j in range(i + 1, len(c)) if c[i] < c[j])  # #ascents-pairs: 0 for decreasing
ok_all = True
for m, D in ((3, 3), (4, 2)):
    X, Y = setup(m)
    for d in range(D + 1):
        C = comps(m, d)
        mon = {c: sp.Mul(*[x ** e for x, e in zip(X, c)]) for c in C}
        edges = set(); diag = {}
        for lam in C:
            for i in range(1, m + 1):
                P = sp.Poly(Y(i, mon[lam]), *X)
                for mu, coeff in zip(P.monoms(), P.coeffs()):
                    coeff = sp.factor(coeff)
                    if tuple(mu) == lam: diag[(lam, i)] = coeff
                    else: edges.add((lam, tuple(mu)))
        # classify off-diagonal support mu of Y x^lam
        cls = {'mu+ < lam+ strictly (dominance)': 0, 'same orbit, inv(mu) < inv(lam) (mu more sorted-decreasing)': 0,
               'same orbit, inv(mu) > inv(lam)': 0, 'mu+ > lam+ or incomparable': 0}
        for lam, mu in edges:
            lp, mp = sorted(lam, reverse=True), sorted(mu, reverse=True)
            if lp == mp: cls['same orbit, inv(mu) < inv(lam) (mu more sorted-decreasing)' if inv(mu) < inv(lam) else 'same orbit, inv(mu) > inv(lam)'] += 1
            elif dom_leq(mu, lam): cls['mu+ < lam+ strictly (dominance)'] += 1
            else: cls['mu+ > lam+ or incomparable'] += 1
        # acyclicity of support graph => a common triangular total order exists
        G = {c: set() for c in C}
        for lam, mu in edges: G[lam].add(mu)
        seen, stack, cyc = {}, [], False
        def dfs(u):
            global cyc
            seen[u] = 1
            for v in G[u]:
                if seen.get(v) == 1: cyc = True
                elif v not in seen: dfs(v)
            seen[u] = 2
        for c in C:
            if c not in seen: dfs(c)
        print('=== m=%d d=%d: #comps=%d, #offdiag support pairs=%d, support graph acyclic=%s' % (m, d, len(C), len(edges), not cyc))
        for k, v in cls.items(): print('    %-62s %d' % (k, v))
        # diagonal entries
        joint = {}
        for lam in C:
            ys = [diag.get((lam, i), 0) for i in range(1, m + 1)]
            sexp = [sp.degree(y, s) if y != 0 else None for y in ys]
            texp = [sp.degree(y, t) if y != 0 else None for y in ys]
            pure = all(y != 0 and sp.simplify(y - s ** a * t ** b) == 0 for y, a, b in zip(ys, sexp, texp))
            joint[lam] = tuple(ys)
            # predicted b_i(lam) = #{j : lam_j > lam_i} + #{j < i : lam_j = lam_i}  (fitted on first run, then checked on all lam)
            b = [sum(1 for j in range(m) if lam[j] > lam[i]) + sum(1 for j in range(i) if lam[j] == lam[i]) for i in range(m)]
            print('    lam=%s  y=%s  s-exp=%s  t-exp=%s  pure=%s  s-exp==lam:%s  t-exp==b(lam):%s' % (
                lam, ys, sexp, texp, pure, list(sexp) == list(lam), list(texp) == b))
            ok_all &= pure and list(sexp) == list(lam) and list(texp) == b
        print('    simple joint spectrum on Pol_%d: %s' % (d, len(set(joint.values())) == len(C)))
        ok_all &= (not cyc) and len(set(joint.values())) == len(C) and cls['same orbit, inv(mu) < inv(lam) (mu more sorted-decreasing)'] == 0 and cls['mu+ > lam+ or incomparable'] == 0
print('ALL (acyclic support; only classes dominance-lower or same-orbit-more-inversions; diag = s^lam_i t^b_i(lam); simple joint spectrum):', ok_all)
