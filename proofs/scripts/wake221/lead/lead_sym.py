"""Wake 221: symbolic-t Lead_{lam,mu}(t) via the Day 220 tight-merge-history formula (history_lead.py logic,
W closed form = Theorem W). Exact symbolic t via sympy fraction field QQ(t). Grade: computed."""
import sys, pickle
from itertools import combinations
from sympy import QQ, symbols, factor, Poly
t = symbols('t'); K = QQ.frac_field(t); T = K.gens[0]
def qi(m, x): return sum((x**i for i in range(m)), K(0))
def W(k, J):
    n = k+sum(J); r = K((-1)**len(J))*qi(n, T)/qi(k, T)
    for j in J: r *= qi(k, T**j)
    return r
def all_leads(lam):
    """returns dict mu -> (Lead(t), #histories) for all coarsenings mu (tight histories with any final state)."""
    states = {(): (K(1), 1)}
    for k in reversed(lam):
        new = {}
        for st, (w, c) in states.items():
            idx = range(len(st))
            for p in range(0, len(st)+1):
                for S in combinations(idx, p):
                    J = [st[i] for i in S]; rest = [st[i] for i in idx if i not in S]
                    ww = w*(W(k, J) if p else K(1))
                    key = tuple(sorted(rest+[k+sum(J)], reverse=True))
                    a, b = new.get(key, (K(0), 0)); new[key] = (a+ww, b+c)
        states = new
    return states
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in parts(n-k, k): yield (k,)+p
if __name__ == '__main__':
    nmax = int(sys.argv[1]); res = {}
    for n in range(1, nmax+1):
        for lam in parts(n):
            st = all_leads(lam)
            for mu, (L, c) in st.items():
                if mu == lam: continue
                e = K.to_sympy(L); res[(lam, mu)] = (e, c)
            L, c = st[(n,)] if (n,) in st else (K(0), 0)
            e = K.to_sympy(L)
            print(f'{lam} -> ({n},): #H={c} Lead(0)={e.subs(t,0)} Lead={factor(e)}', flush=True)
    pickle.dump(res, open(f'leads_n{nmax}.pkl', 'wb'))
    print('DONE')
