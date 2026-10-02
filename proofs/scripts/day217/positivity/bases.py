"""Convert Schur structure constants to e, h, b (=s^{n(mu)} e_mu) bases; positivity tests."""
import sys, pickle, itertools
from sympy import symbols, Matrix, expand, factor, Poly, cancel, Rational, together, fraction
from engine import parts, ssyt
s, t = symbols('s t')
MAXN = int(sys.argv[1])
g = pickle.load(open(f'g_schur_{MAXN}.pkl', 'rb'))
P = {n: list(parts(n)) for n in range(MAXN+1)}
def conj(l): return tuple(sum(1 for r in l if r > j) for j in range(l[0])) if l else ()
def kostka(nu, lam):
    N = len(lam); return sum(1 for v in ssyt(nu, N) if v == tuple(lam))
def nfun(l): return sum(i*r for i, r in enumerate(l))
# transition: B_lam = sum_nu M[lam][nu] s_nu
def trans(basis, n):
    M = Matrix(len(P[n]), len(P[n]), lambda i, j: 0)
    for i, lam in enumerate(P[n]):
        for j, nu in enumerate(P[n]):
            if basis == 'e': M[i, j] = kostka(conj(nu), lam)
            elif basis == 'h': M[i, j] = kostka(nu, lam)
            elif basis == 'b': M[i, j] = s**nfun(lam)*kostka(conj(nu), lam)
            elif basis == 'bt': M[i, j] = t**nfun(lam)*kostka(conj(nu), lam)
            elif basis == 'schur': M[i, j] = 1 if i == j else 0
    return M
def gs(lam, mu, nu): return g.get((lam, mu, nu), 0)
def structure(basis):
    TM = {n: trans(basis, n) for n in range(1, MAXN+1)}
    TI = {n: TM[n].inv() for n in TM}
    out = {}
    for a in range(1, MAXN):
        for b in range(1, MAXN-a+1):
            n = a+b
            for i, lam in enumerate(P[a]):
                for j, mu in enumerate(P[b]):
                    # product in schur
                    vec = [0]*len(P[n])
                    for x, al in enumerate(P[a]):
                        if TM[a][i, x] == 0: continue
                        for y, be in enumerate(P[b]):
                            if TM[b][j, y] == 0: continue
                            c = TM[a][i, x]*TM[b][j, y]
                            for z, nu in enumerate(P[n]): vec[z] += c*gs(al, be, nu)
                    res = Matrix([vec])*TI[n]
                    for z, nu in enumerate(P[n]):
                        v = factor(cancel(res[0, z]))
                        if v != 0: out[(lam, mu, nu)] = v
    return out
def poscheck(v):
    """returns (is_laurent, all_pos, all_neg_or_pos?)"""
    num, den = fraction(together(v))
    pd = Poly(den, s, t)
    if len(pd.terms()) != 1: return ('RATIONAL', None)
    pn = Poly(expand(num), s, t)
    cs = [c for _, c in pn.terms()]
    return ('laurent', all(c > 0 for c in cs) or all(c < 0 for c in cs))
if __name__ == '__main__':
    for basis in ['schur', 'e', 'h', 'b']:
        st = structure(basis)
        pickle.dump(st, open(f'g_{basis}_{MAXN}.pkl', 'wb'))
        nonlaur = [k for k, v in st.items() if poscheck(v)[0] != 'laurent']
        nonpos = [k for k, v in st.items() if poscheck(v)[0] == 'laurent' and not poscheck(v)[1]]
        print(f'== {basis}: {len(st)} nonzero consts; non-Laurent {len(nonlaur)}; non-sign-coherent {len(nonpos)}')
        for k in nonlaur[:3]: print('   nonLaurent', k, st[k])
        for k in nonpos[:5]: print('   nonpos', k, st[k])
