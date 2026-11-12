"""Cap product with the fundamental class on toric Richardson varieties X_s (GLL 2609.30257).
H^{2i}(X_s) has basis F_u (u distinct subsequence of s, |u|=i-1; u=EPS for i=0),
H_{2j}(X_s) basis R_v.  [X_s] = R_s.  cap: F_u -> sum_v <F_u F_v, R_s> R_v.
M_i[u,v] = coeff of F_s in F_u F_v  ( = mult of P_u (x) P_v in Res^{H_d(0)}_{H_i(0)xH_{d-i}(0)} P_s ).
Report rank r_i vs b_i, b_{d-i}; also integral: gcd of maximal minors (via sympy smith form)."""
import itertools, sys
from functools import lru_cache
import sympy
EPS = None
def perm_with_des(u):  # u binary string of length a-1
    a = len(u)+1
    blocks=[[1]]
    for i,c in enumerate(u):
        if c=='1': blocks[-1].append(i+2)
        else: blocks.append([i+2])
    out=[]
    for b in blocks: out += b[::-1]
    # values within block decreasing: blocks are consecutive integers -> ok
    return out
def des(p): return ''.join('1' if p[i]>p[i+1] else '0' for i in range(len(p)-1))
@lru_cache(None)
def coeff(u,v,s):
    if u is EPS: return int(v==s)
    if v is EPS: return int(u==s)
    a,b=len(u)+1,len(v)+1
    if a+b!=len(s)+1: return 0
    sig=perm_with_des(u); tau=[x+a for x in perm_with_des(v)]
    n=a+b; cnt=0
    for pos in itertools.combinations(range(n),a):
        p=[0]*n; it1=iter(sig); it2=iter(tau); ps=set(pos)
        for k in range(n): p[k]=next(it1) if k in ps else next(it2)
        if des(p)==s: cnt+=1
    return cnt
def subseqs(s,L):
    return sorted({''.join(c) for c in itertools.combinations(s,L)})
def basis(s,i):
    return [EPS] if i==0 else subseqs(s,i-1)
def analyse(s):
    d=len(s)+1
    b=[len(basis(s,i)) for i in range(d+1)]
    ranks=[];dets=[]
    for i in range(d+1):
        U=basis(s,i); V=basis(s,d-i)
        M=sympy.Matrix(len(U),len(V),lambda x,y: coeff(U[x],V[y],s))
        r=M.rank(); ranks.append(r)
        if len(U)==len(V) and r==len(U): dets.append(abs(M.det()))
        else: dets.append(None)
    return b,ranks,dets
if __name__=='__main__':
    maxlen=int(sys.argv[1]) if len(sys.argv)>1 else 7
    tot=fail=0; nonpd=0
    for L in range(0,maxlen+1):
        for s in (''.join(t) for t in itertools.product('01',repeat=L)):
            b,r,dets=analyse(s); d=L+1
            mr=[min(b[i],b[d-i]) for i in range(d+1)]
            tot+=1
            ok = (r==mr)
            if not ok: fail+=1
            pal = b==b[::-1]
            if L<=4 or not ok or pal:
                print(s or "''", 'b=',b,'rank=',r,'maxrank' if ok else 'NOT-MAXRANK', 'palin' if pal else '', 'dets=',[x for x in dets if x is not None] if pal else '')
    print('total',tot,'not max rank',fail)
