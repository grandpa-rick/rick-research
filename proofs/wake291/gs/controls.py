"""Negative controls for P1a and commutative shadows.
Strings: binary length n-1, bit 1 = descent/cut (cap_rank.py convention).  X in NSym_d given as dict t->coeff in R basis.
r_i(X) = rank [ <F_u F_v, X> ]_{u in comp(i), v in comp(d-i)} = Hilbert function of QSym/Ann(X)."""
import itertools, random, sys
from collections import Counter
from functools import lru_cache
from cap_rank_import import perm_with_des, des
from fastcap import rank
def comps(n):  # all compositions of n as strings ; n=0 -> [None]
    return [None] if n==0 else [''.join(t) for t in itertools.product('01',repeat=n-1)]
@lru_cache(None)
def prod(u,v,n):  # F_u F_v as Counter over strings of length n-1
    if u is None: return Counter({v:1})
    if v is None: return Counter({u:1})
    a=len(u)+1; b=len(v)+1
    sig=perm_with_des(u); tau=[x+a for x in perm_with_des(v)]
    C=Counter()
    for pos in itertools.combinations(range(n),a):
        ps=set(pos); i1=iter(sig); i2=iter(tau)
        p=[next(i1) if k in ps else next(i2) for k in range(n)]
        C[des(p)]+=1
    return C
def hilb(X,d):
    out=[]
    for i in range(d+1):
        U=comps(i); V=comps(d-i)
        M=[[sum(c*X.get(t,0) for t,c in prod(u,v,d).items()) for v in V] for u in U]
        out.append(rank(M))
    return out
def ribbon_mult(A,B):  # product of two R-expansions (dicts string->coef), junction bit free
    C=Counter()
    for a,x in A.items():
        for b,y in B.items():
            for j in '01': C[a+j+b]+=x*y
    return dict(C)
def prodlist(parts):
    X=parts[0]
    for P in parts[1:]: X=ribbon_mult(X,P)
    return X
S=lambda n:{'0'*(n-1):1}
Lam=lambda n:{'1'*(n-1):1}
Psi=lambda n:{'1'*k+'0'*(n-1-k):(-1)**k for k in range(n)}
def alt(L): return ('01'*30)[:L]
def comp_of(s):
    parts=[1]
    for c in s:
        if c=='1': parts.append(1)
        else: parts[-1]+=1
    return parts
if __name__=='__main__':
    from predict import pred
    random.seed(1)
    Lmax=int(sys.argv[1]) if len(sys.argv)>1 else 9
    for L in range(1,Lmax+1):
        d=L+1; s=alt(L); alpha=comp_of(s)
        tests={
          'R_s (sanity)':{s:1},
          'S^alpha':prodlist([S(a) for a in alpha]),
          'Lambda^alpha':prodlist([Lam(a) for a in alpha]),
          'Psi^alpha':prodlist([Psi(a) for a in alpha]),
          'random int NSym_d':{t:random.randint(-5,5) for t in comps(d)},
          'R_s + R_(d) (perturb)':{s:1,'0'*L:1},
          'R_s + R_{s flipped last bit}':{s:1, s[:-1]+('1' if s[-1]=='0' else '0'):1},
        }
        print('L',L,'alpha',alpha,'P1a/even pred',pred(L),flush=True)
        for name,X in tests.items():
            h=hilb(X,d); print('   %-30s'%name,h,'MATCH' if h==pred(L) else 'differs',flush=True)
