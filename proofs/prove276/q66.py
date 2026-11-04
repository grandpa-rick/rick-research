# PROVE 276: Q65/Q66. Abstract crystals, quasification (CMRR 2309.14898 Def 4.5), quasi-tensor (Theorem A, word order).
import itertools, sys
sys.path.insert(0,'../prove275')
from qc import kash, kstr, quasi, qstr, inv, INF
from collections import Counter

# ---- abstract crystal: dict el -> data; ops as dicts
class Cr:
    def __init__(s,els,n,wt,e,f,eps,phi):
        s.els=els;s.n=n;s.wt=wt;s.e=e;s.f=f;s.eps=eps;s.phi=phi
def word_crystal_component(hw,n):
    # crystal component (Kashiwara ops) of word hw over [n]
    seen={hw};st=[hw]
    while st:
        w=st.pop()
        for i in range(1,n):
            for op in 'ef':
                v=kash(w,i,op)
                if v is not None and v not in seen: seen.add(v);st.append(v)
    els=sorted(seen)
    wt={w:tuple(w.count(j) for j in range(1,n+1)) for w in els}
    e={(w,i):kash(w,i,'e') for w in els for i in range(1,n)}
    f={(w,i):kash(w,i,'f') for w in els for i in range(1,n)}
    eps={(w,i):kstr(w,i)[0] for w in els for i in range(1,n)}
    phi={(w,i):kstr(w,i)[1] for w in els for i in range(1,n)}
    return Cr(els,n,wt,e,f,eps,phi)
def shift(C,c):  # B (x) det^c : same graph, weights + c
    return Cr(C.els,C.n,{x:tuple(a+c for a in C.wt[x]) for x in C.els},C.e,C.f,C.eps,C.phi)
def tensor(B,Bp):  # signature rule, WORD order: x(x)y <-> word xy ; e acts on x iff eps_x > phi_y
    n=B.n;els=[(x,y) for x in B.els for y in Bp.els]
    wt={};e={};f={};eps={};phi={}
    for (x,y) in els:
        wt[(x,y)]=tuple(a+b for a,b in zip(B.wt[x],Bp.wt[y]))
        for i in range(1,n):
            ex,px,ey,py=B.eps[x,i],B.phi[x,i],Bp.eps[y,i],Bp.phi[y,i]
            m=min(ex,py)
            eps[(x,y),i]=ey+ex-m; phi[(x,y),i]=px+py-m
            if ex>py: t=B.e[x,i]; e[(x,y),i]=None if t is None else (t,y)
            else: t=Bp.e[y,i]; e[(x,y),i]=None if t is None else (x,t)
            if py>ex: t=Bp.f[y,i]; f[(x,y),i]=None if t is None else (x,t)
            else: t=B.f[x,i]; f[(x,y),i]=None if t is None else (t,y)
    return Cr(els,n,wt,e,f,eps,phi)
class QC:
    def __init__(s,els,n,wt,e,f,eps,phi): s.els=els;s.n=n;s.wt=wt;s.e=e;s.f=f;s.eps=eps;s.phi=phi
def quasify(C):  # CMRR Def 4.5
    n=C.n;e={};f={};eps={};phi={}
    for x in C.els:
        for i in range(1,n):
            alive = C.eps[x,i]==C.wt[x][i]   # wt_{i+1} is index i (0-based)
            eps[x,i]=C.eps[x,i] if alive else INF
            phi[x,i]=C.phi[x,i] if alive else INF
            e[x,i]=C.e[x,i] if alive else None
    for x in C.els:
        for i in range(1,n): f[x,i]=None
    for x in C.els:
        for i in range(1,n):
            if e[x,i] is not None: f[e[x,i],i]=x
    return QC(C.els,n,C.wt,e,f,eps,phi)
def qtensor(Q,Qp,swap=False):  # Theorem A, word order; swap=True is the NEGATIVE CONTROL (kill phi_x>0 & eps_y>0)
    n=Q.n;els=[(x,y) for x in Q.els for y in Qp.els];wt={};e={};f={};eps={};phi={}
    for (x,y) in els:
        wt[(x,y)]=tuple(a+b for a,b in zip(Q.wt[x],Qp.wt[y]))
        for i in range(1,n):
            ex,px,ey,py=Q.eps[x,i],Q.phi[x,i],Qp.eps[y,i],Qp.phi[y,i]
            kill = ex==INF or ey==INF or ((px>0 and ey>0) if swap else (ex>0 and py>0))
            if kill: eps[(x,y),i]=phi[(x,y),i]=INF; e[(x,y),i]=f[(x,y),i]=None; continue
            eps[(x,y),i]=ex+ey; phi[(x,y),i]=px+py
            if ex>0: e[(x,y),i]=(Q.e[x,i],y)
            elif ey>0: e[(x,y),i]=(x,Qp.e[y,i])
            else: e[(x,y),i]=None
            if py>0: f[(x,y),i]=(x,Qp.f[y,i])
            elif px>0: f[(x,y),i]=(Q.f[x,i],y)
            else: f[(x,y),i]=None
    return QC(els,n,wt,e,f,eps,phi)
def same(A,B):
    bad=0
    for x in A.els:
        if A.wt[x]!=B.wt[x]: bad+=1
        for i in range(1,A.n):
            if (A.e[x,i],A.f[x,i],A.eps[x,i],A.phi[x,i])!=(B.e[x,i],B.f[x,i],B.eps[x,i],B.phi[x,i]): bad+=1
    return bad
def hw_word(lam):  # row reading word of Yamanouchi tableau (rows bottom to top) -> highest weight lam
    w=[]
    for r in range(len(lam)-1,-1,-1): w+= [r+1]*lam[r]
    return tuple(w)
def partitions(N,maxparts):
    def rec(N,mx,k):
        if N==0: yield (); return
        if k==0: return
        for p in range(min(N,mx),0,-1):
            for r in rec(N-p,p,k-1): yield (p,)+r
    return list(rec(N,N,maxparts))
