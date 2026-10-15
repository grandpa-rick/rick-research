# Psi: H -> QSym_q for (1) H = free braided algebra T(V) on primitive letters, (2) rank-1 k[F]
from qqsym import *
from itertools import product as iprod
import sympy as sp

def Psi_word(w, deg, zeta, q, sgn=1):
    n = len(w); out = defaultdict(Fr)
    if n == 0: return {(): Fr(1)}
    for l in range(1, n+1):
        for b in iprod(range(l), repeat=n):
            if len(set(b)) < l: continue
            wt = Fr(1)
            for i in range(n):
                for j in range(i+1, n):
                    if b[i] > b[j]: wt *= q ** (sgn*deg[w[i]]*deg[w[j]])
            al = [0]*l; co = Fr(1)
            for i in range(n): al[b[i]] += deg[w[i]]; co *= zeta[w[i]]
            out[tuple(al)] += wt*co
    return {k: v for k, v in out.items() if v != 0}

def lin_mul(X, Y, q, sgn=1): return mul(X, Y, q, sgn)

if __name__ == "__main__":
    q = Fr(3, 7)
    deg = {0: 1, 1: 2, 2: 1}; zeta = {0: Fr(2), 1: Fr(-5, 3), 2: Fr(7, 11)}
    random.seed(1)
    words = [tuple(random.choice([0, 1, 2]) for _ in range(random.randint(1, 3))) for _ in range(40)]
    for (Hs, Qs, lab) in [(1, 1, "MATCHED"), (1, -1, "CONTROL H braid q, QSym q^-1"), (-1, 1, "CONTROL H q^-1, QSym q")]:
        bad = tot = 0
        for u in words[:20]:
            for v in words[20:]:
                if len(u)+len(v) > 6: continue
                lhs = Psi_word(u+v, deg, zeta, q, Hs)
                rhs = mul(Psi_word(u, deg, zeta, q, Hs), Psi_word(v, deg, zeta, q, Hs), q, Qs)
                tot += 1; bad += (lhs != rhs)
        print(lab, "Psi(uv)=Psi(u)*Psi(v) failures:", bad, "/", tot)
    # coalgebra-map + zeta check
    u = (0, 1, 2, 0); P = Psi_word(u, deg, zeta, q)
    print("zetaQ(Psi(u)) == zeta(u):", zetaQ(P) == zeta[0]**2*zeta[1]*zeta[2])
    # rank 1 symbolic
    qs, t = sp.symbols('q t')
    def qint(n): return sum(qs**i for i in range(n))
    def qfac(n):
        r = sp.Integer(1)
        for i in range(1, n+1): r *= qint(i)
        return r
    def psiF(n): return {a: t**n/sp.prod([qfac(x) for x in a]) for a in comps(n)}
    def smul(X, Y, sgn=1):
        out = defaultdict(lambda: sp.Integer(0))
        for a, ca in X.items():
            for b, cb in Y.items():
                # symbolic weights: recompute qqsh with symbol
                for w, c in qqsh_sym(a, b, sgn).items(): out[w] += ca*cb*c
        return out
    def qqsh_sym(a, b, sgn):
        def rec(i, j):
            if i == len(a) and j == len(b): return {(): sp.Integer(1)}
            out = defaultdict(lambda: sp.Integer(0))
            if i < len(a):
                for w, c in rec(i+1, j).items(): out[(a[i],)+w] += c
            if j < len(b):
                for w, c in rec(i, j+1).items(): out[(b[j],)+w] += c*qs**(sgn*b[j]*sum(a[i:]))
            if i < len(a) and j < len(b):
                for w, c in rec(i+1, j+1).items(): out[(a[i]+b[j],)+w] += c*qs**(sgn*b[j]*sum(a[i+1:]))
            return out
        return rec(0, 0)
    def gbin(n, k): return sp.cancel(qfac(n)/(qfac(k)*qfac(n-k)))
    for sgn, lab in [(1, "MATCHED"), (-1, "CONTROL q^-1 QSym")]:
        res = []
        for a in range(1, 4):
            for b in range(1, 5-a):
                L = smul(psiF(a), psiF(b), sgn); R = psiF(a+b)
                ok = all(sp.simplify(L.get(k, 0) - gbin(a+b, a)*R[k]) == 0 for k in R) and set(L) <= set(R)
                res.append(((a, b), ok))
        print("rank1", lab, res)
    print("Psi(F^(3)) =", {k: sp.factor(v) for k, v in psiF(3).items()})
    print("Psi(F^(2)) at q=1:", {k: v.subs(qs, 1) for k, v in psiF(2).items()})
