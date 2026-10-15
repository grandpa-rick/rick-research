from lattice import *
q = Fr(3, 7)
C = [[2, -1], [-1, 2]]
t = [Fr(2), Fr(-5, 3)]
random.seed(3)
words = [tuple(random.choice([0, 1]) for _ in range(random.randint(1, 3))) for _ in range(24)]
for B, lab in [([[0, 0], [0, 0]], "phi=0"), ([[1, -1], [0, 1]], "phi=Feigin-ish"), ([[0, 2], [-1, 0]], "phi=random")]:
    Q = QQ(C, B, q); bad = tot = 0
    for u in words[:12]:
        for v in words[12:]:
            if len(u)+len(v) > 5: continue
            tot += 1; bad += Q.Psi(u+v, t) != Q.mul(Q.Psi(u, t), Q.Psi(v, t))
    print(lab, "free-algebra Psi multiplicativity failures:", bad, "/", tot)
# Serre elements: kernel of Rosso map (Psi restricted to simple-letter words, t=1) in degree 2a1+a2
Q = QQ(C, [[0, 0], [0, 0]], q)
ws = [(0, 0, 1), (0, 1, 0), (1, 0, 0)]
def rosso(w):
    P = Q.Psi(w, [Fr(1), Fr(1)])
    return {k: v for k, v in P.items() if all(sum(x) == 1 for x in k)}
keys = sorted({k for w in ws for k in rosso(w)})
M = sp.Matrix([[rosso(w).get(k, 0) for w in ws] for k in keys])
ns = M.nullspace(); print("Serre kernel dim (2a1+a2):", len(ns), [sp.nsimplify(x) for x in ns[0]])
S = {w: Fr(str(sp.nsimplify(c))) for w, c in zip(ws, ns[0])}
S2 = {tuple(1-x for x in w): c for w, c in S.items()}  # swap roles -> degree a1+2a2 (by symmetry of C)
for B, lab in [([[0, 0], [0, 0]], "phi=0"), ([[1, -1], [0, 1]], "B12-B21=-1"), ([[1, 0], [-1, 1]], "B12-B21=+1"), ([[1, 2], [0, 1]], "B12-B21=2")]:
    Q2 = QQ(C, B, q)
    print(lab, "Psi(Serre_12) zero?", Q2.PsiLin(S, t) == {}, " Psi(Serre_21) zero?", Q2.PsiLin(S2, t) == {})
