# braided ABS test: QSym_q = q-quasi-shuffle on compositions, braiding c(x(x)y)=q^{|x||y|} y(x)x
from fractions import Fraction as Fr
from itertools import product
from collections import defaultdict
import random, sys

def qqsh(a, b, q, sgn=1):
    """q-quasi-shuffle of compositions a,b: weight q^{sgn * sum over (b-letter strictly before a-letter) a_i b_j}"""
    # recursion on first letters
    memo = {}
    def rec(i, j):
        if (i, j) in memo: return memo[(i, j)]
        out = defaultdict(Fr)
        if i == len(a) and j == len(b):
            out[()] = Fr(1)
        else:
            if i < len(a):   # a-letter first: no new inversions
                for w, c in rec(i+1, j).items(): out[(a[i],)+w] += c
            if j < len(b):   # b-letter first: inverts with all remaining a letters
                wt = q ** (sgn * b[j] * sum(a[i:]))
                for w, c in rec(i, j+1).items(): out[(b[j],)+w] += c * wt
            if i < len(a) and j < len(b):  # merge: b[j] inverts with a[i+1:]
                wt = q ** (sgn * b[j] * sum(a[i+1:]))
                for w, c in rec(i+1, j+1).items(): out[(a[i]+b[j],)+w] += c * wt
        memo[(i, j)] = out
        return out
    return dict(rec(0, 0))

def mul(X, Y, q, sgn=1):
    out = defaultdict(Fr)
    for a, ca in X.items():
        for b, cb in Y.items():
            for w, c in qqsh(a, b, q, sgn).items(): out[w] += ca*cb*c
    return {k: v for k, v in out.items() if v != 0}

def comps(n):
    if n == 0: yield (); return
    for k in range(1, n+1):
        for r in comps(n-k): yield (k,)+r

def deconc(a):
    return [(a[:k], a[k:]) for k in range(len(a)+1)]

def tensmul(T1, T2, q, sgn_m=1, sgn_c=1):
    """braided product on Q(x)Q: (a(x)b)(c(x)d)=q^{|b||c|} ac (x) bd"""
    out = defaultdict(Fr)
    for (a, b), x in T1.items():
        for (c, d), y in T2.items():
            wt = q ** (sgn_c * sum(b) * sum(c))
            for u, cu in qqsh(a, c, q, sgn_m).items():
                for v, cv in qqsh(b, d, q, sgn_m).items():
                    out[(u, v)] += x*y*wt*cu*cv
    return {k: v for k, v in out.items() if v != 0}

def Delta(X):
    out = defaultdict(Fr)
    for a, c in X.items():
        for l, r in deconc(a): out[(l, r)] += c
    return dict(out)

def check_bialg(N, q, sgn_m=1, sgn_c=1):
    bad = 0; tot = 0
    for n1 in range(1, N):
        for n2 in range(1, N-n1+1):
            for a in comps(n1):
                for b in comps(n2):
                    lhs = Delta(mul({a: Fr(1)}, {b: Fr(1)}, q, sgn_m))
                    rhs = tensmul(Delta({a: Fr(1)}), Delta({b: Fr(1)}), q, sgn_m, sgn_c)
                    keys = set(lhs) | set(rhs)
                    tot += 1
                    if any(lhs.get(k, 0) != rhs.get(k, 0) for k in keys): bad += 1
    return bad, tot

def check_assoc(N, q):
    bad = tot = 0
    for n1 in range(1, N):
        for n2 in range(1, N-n1):
            for n3 in range(1, N-n1-n2+1):
                for a in comps(n1):
                    for b in comps(n2):
                        for c in comps(n3):
                            A, B, C = {a: Fr(1)}, {b: Fr(1)}, {c: Fr(1)}
                            tot += 1
                            if mul(mul(A, B, q), C, q) != mul(A, mul(B, C, q), q): bad += 1
    return bad, tot

def zetaQ(X):
    return sum((c for a, c in X.items() if len(a) <= 1), Fr(0))

if __name__ == "__main__":
    q = Fr(3, 7)
    print("assoc (deg<=6):", check_assoc(6, q))
    print("bialgebra q-mult, q-braid (deg<=6):", check_bialg(6, q))
    print("CONTROL q-mult, q^-1 braid:", check_bialg(5, q, 1, -1))
    print("CONTROL q^-1-mult, q braid:", check_bialg(5, q, -1, 1))
    print("q=1 classical:", check_bialg(5, Fr(1)))
    # zeta_Q multiplicative
    bad = 0
    for n1 in range(1, 5):
        for n2 in range(1, 5):
            for a in comps(n1):
                for b in comps(n2):
                    if zetaQ(mul({a: Fr(1)}, {b: Fr(1)}, q)) != zetaQ({a: 1})*zetaQ({b: 1}): bad += 1
    print("zetaQ multiplicative failures:", bad)
