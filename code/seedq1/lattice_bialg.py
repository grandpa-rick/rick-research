from lattice import *
def comps2(n):  # compositions of lattice vector n in N^2 into nonzero parts
    if n == (0, 0): yield (); return
    for a in range(n[0]+1):
        for b in range(n[1]+1):
            if (a, b) == (0, 0): continue
            for r in comps2((n[0]-a, n[1]-b)): yield ((a, b),)+r
def Delta(X):
    out = defaultdict(Fr)
    for a, c in X.items():
        for k in range(len(a)+1): out[(a[:k], a[k:])] += c
    return out
def tens(Q, T1, T2, csgn=1):
    out = defaultdict(Fr)
    for (a, b), x in T1.items():
        for (c, d), y in T2.items():
            tb = tuple(map(sum, zip(*b))) if b else (0, 0); tc = tuple(map(sum, zip(*c))) if c else (0, 0)
            wt = Q.br(tb, tc) ** csgn
            for u, cu in Q.qqsh(a, c).items():
                for v, cv in Q.qqsh(b, d).items(): out[(u, v)] += x*y*wt*cu*cv
    return {k: v for k, v in out.items() if v != 0}
q = Fr(3, 7); C = [[2, -1], [-1, 2]]
for B in [[[1, -1], [0, 1]], [[0, 2], [-1, 3]]]:
    Q = QQ(C, B, q)
    for csgn in [1, -1]:
        bad = tot = 0; ba = 0
        degs = [(1, 0), (0, 1), (1, 1), (2, 0), (2, 1)]
        for d1 in degs:
            for d2 in degs:
                for a in comps2(d1):
                    for b in comps2(d2):
                        L = {k: v for k, v in Delta(Q.mul({a: Fr(1)}, {b: Fr(1)})).items() if v != 0}
                        R = tens(Q, Delta({a: Fr(1)}), Delta({b: Fr(1)}), csgn)
                        tot += 1; bad += L != R
                        for d3 in degs[:3]:
                            for c in comps2(d3):
                                A_, B_, C_ = {a: Fr(1)}, {b: Fr(1)}, {c: Fr(1)}
                                ba += Q.mul(Q.mul(A_, B_), C_) != Q.mul(A_, Q.mul(B_, C_))
        print("B=", B, "braid sign", csgn, "bialg failures", bad, "/", tot, " assoc failures", ba)
