"""Commutative shadows of G_s.
(A) Sym shadow: Sym/Ann_Sym(r_s), r_s = chi(R_s) ribbon Schur, Hall pairing. r^Sym_i = rank [<h_lam h_mu, R_s>]_{lam|-i, mu|-d-i},
    <h_nu,R_s> = [F_s] h_nu computed in QSym by shuffle products (independent of the ribbon-SSYT formula; cross-checked by SSYT count).
    Since Sym = Q[p_1,p_2,...] with p_k^perp = k d/dp_k, this is the weighted apolar algebra of r_s in the p-variables.
(B) polynomial shadow: standard apolar algebra of the form r_s(x_1..x_n), n=3,4,5 (catalecticant ranks)."""
import itertools, sys
from collections import Counter
from functools import lru_cache
import sympy
from controls import prod, alt, comp_of
from fastcap import rank
from predict import pred
def partitions(n,m=None):
    if m is None: m=n
    if n==0: yield (); return
    for k in range(min(n,m),0,-1):
        for p in partitions(n-k,k): yield (k,)+p
@lru_cache(None)
def h_in_F(nu):  # Counter over strings
    C=Counter({None:1}); tot=0
    for part in nu:
        newtot=tot+part; D=Counter()
        for u,c in C.items():
            for t,e in prod(u,'0'*(part-1),newtot).items(): D[t]+=c*e
        C=D; tot=newtot
    return C
def ssyt_ribbon_content(s,nu):  # independent: # fillings of ribbon s with content nu (bit0: weak incr, bit1: strict decr)
    n=len(s)+1; cnt=0
    letters=[i for i,m in enumerate(nu) for _ in range(m)]
    for w in set(itertools.permutations(letters)):
        if all((w[i]<=w[i+1]) if s[i]=='0' else (w[i]>w[i+1]) for i in range(n-1)): cnt+=1
    return cnt
def sym_hilb(s):
    d=len(s)+1; out=[]
    for i in range(d+1):
        M=[[h_in_F(tuple(sorted(l+m,reverse=True)))[s] for m in partitions(d-i)] for l in partitions(i)]
        out.append(rank(M))
    return out
def poly_hilb(s,n):
    xs=sympy.symbols('x1:%d'%(n+1)); d=len(s)+1
    alpha=comp_of(s); L=len(s)
    def h(k): return sum(sympy.prod(c) for c in itertools.combinations_with_replacement(xs,k)) if k>0 else 1
    cuts=[i for i,c in enumerate(s) if c=='1']
    F=0
    for r in range(len(cuts)+1):
        for keep in itertools.combinations(cuts,r):
            t=''.join('1' if (i in keep) else '0' for i in range(L))
            F+=(-1)**(len(cuts)-r)*sympy.prod([h(a) for a in comp_of(t)])
    F=sympy.Poly(sympy.expand(F),*xs)
    if F.is_zero: return 'zero'
    out=[]
    for i in range(d+1):
        rows=[]
        mons=list(itertools.combinations_with_replacement(range(n),i))
        for m in mons:
            G=F
            for v in m: G=G.diff(xs[v])
            rows.append(G)
        keys=sorted({k for G in rows for k in G.as_dict()})
        M=[[int(G.as_dict().get(k,0)) for k in keys] for G in rows]
        out.append(rank(M) if keys else 0)
    return out
if __name__=='__main__':
    # cross-check <h_nu,R_s> two ways
    bad=0
    for s in ['0101','01010','0110','1001']:
        for nu in partitions(len(s)+1): bad+= h_in_F(nu)[s]!=ssyt_ribbon_content(s,nu)
    print('h_nu pairing crosscheck mismatches',bad)
    Lmax=int(sys.argv[1])
    for L in range(1,Lmax+1):
        s=alt(L)
        print('L',L,s,'QSym G_s',pred(L),'| Sym shadow',sym_hilb(s),flush=True)
    for L in range(1,8):
        s=alt(L)
        print('L',L,s,'poly shadow n=3,4,5:',[poly_hilb(s,n) for n in (3,4,5)],flush=True)
    # nonalternating examples: QSym vs Sym
    from fastcap import ranks
    for s in ['0010','0110','00100','01001','001101','0100110']:
        print('nonalt',s,'QSym',ranks(s),'Sym',sym_hilb(s))
