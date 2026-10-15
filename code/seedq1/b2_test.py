# B2: symmetric form (a1,a1)=4,(a2,a2)=2,(a1,a2)=-2; a12=-1, a21=-2. Serre = kernel of Rosso map.
from lattice import *
q = Fr(3, 7); C = [[4, -2], [-2, 2]]; t = [Fr(2), Fr(-5, 3)]
def serre(Q, word_deg):
    from itertools import permutations
    ws = sorted(set(permutations(word_deg)))
    def rosso(w):
        P = Q.Psi(w, [Fr(1), Fr(1)])
        return {k: v for k, v in P.items() if all(sum(x) == 1 for x in k)}
    keys = sorted({k for w in ws for k in rosso(w)})
    M = sp.Matrix([[rosso(w).get(k, 0) for w in ws] for k in keys])
    ns = M.nullspace(); assert len(ns) == 1, len(ns)
    return {w: Fr(str(sp.nsimplify(c))) for w, c in zip(ws, ns[0])}
Q0 = QQ(C, [[0, 0], [0, 0]], q)
S1 = serre(Q0, (0, 0, 1)); S2 = serre(Q0, (1, 1, 1, 0))
print("S(2a1+a2):", S1); print("S(a1+3a2):", S2)
for d in range(-4, 5):
    Q = QQ(C, [[0, d], [0, 0]], q)   # antisym part phi12-phi21 = d
    print("phi12-phi21 =", d, " kills S1:", Q.PsiLin(S1, t) == {}, " kills S2:", Q.PsiLin(S2, t) == {})
