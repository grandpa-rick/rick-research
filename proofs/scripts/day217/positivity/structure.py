"""Structure constants of Hikita star at generic (s,t), Schur basis, |lam|+|mu|<=MAXN."""
import sys, pickle
from sympy import symbols, Matrix, cancel, factor, Poly, together, fraction, zeros, eye
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
from engine import parts
s, t = symbols('s t')
K = QQ.frac_field(s, t)
MAXN = int(sys.argv[1])
mats = {kd:v for kd,v in pickle.load(open('Emats_6.pkl', 'rb')).items() if sum(kd)<=MAXN}
P = {n: list(parts(n)) for n in range(MAXN+1)}
def Emat(k, d):  # DomainMatrix rows = mu in P[d], cols = nu in P[d+k]
    M = mats[(k, d)]; rows = []
    for mu in P[d]:
        row = []
        for nu in P[d+k]:
            dd = M[mu].get(nu, {})
            row.append(K.convert(sum(c*s**a*t**b for (a, b), c in dd.items())))
        rows.append(row)
    return DomainMatrix(rows, (len(P[d]), len(P[d+k])), K)
EM = {kd: Emat(*kd) for kd in mats}
def Erho(rho, d):  # matrix of E_rho on Lambda^d (apply rho[-1] first)
    M = None; cur = d
    for k in reversed(rho):
        A = EM[(k, cur)]; M = A if M is None else M*A; cur += k
    return M
# L_lam operators
L = {}
for n in range(1, MAXN+1):
    G = DomainMatrix([[Erho(rho, 0)[0, j].element for j in range(len(P[n]))] for rho in P[n]], (len(P[n]), len(P[n])), K)
    Gi = G.inv()
    for i, lam in enumerate(P[n]):
        for d in range(0, MAXN-n+1):
            Lm = None
            for j, rho in enumerate(P[n]):
                a = Gi[i, j].element
                if a == K.zero: continue
                term = Erho(rho, d)*a
                Lm = term if Lm is None else Lm+term
            L[(lam, d)] = Lm
    print('L done n=', n, flush=True)
g = {}
for (lam, d), Lm in L.items():
    for i, mu in enumerate(P[d]):
        if d == 0: continue
        for j, nu in enumerate(P[sum(lam)+d]):
            v = Lm[i, j].element
            if v != K.zero: g[(lam, mu, nu)] = K.to_sympy(v)
pickle.dump(g, open(f'g_schur_{MAXN}.pkl', 'wb'))
print('entries', len(g))
