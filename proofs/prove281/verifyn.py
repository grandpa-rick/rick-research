"""Independent replay (no shared code) of certs15_*.json: own RSK, own left/right star (asserting D_L / D_R membership),
rank-matrix Bruhat, own endpoint checks (gap-1 comparable => mu=1; even gap, Bruhat-incomparable, or F1 => mu=0),
own enumeration of the y's Lemma A requires (s x in cell with L not in A; all SYT U with Des U > A)."""
import json,sys
from itertools import combinations
F=sys.argv[1]; D=json.load(open(F)); n=len(D[0]["x"])
def ln(w): return sum(w[i]>w[j] for i,j in combinations(range(n),2))
def ldes(w):
    p=[0]*(n+2)
    for k,a in enumerate(w): p[a]=k
    return {i for i in range(1,n) if p[i+1]<p[i]}
def sw(i,w): return [i+1 if a==i else (i if a==i+1 else a) for a in w]
def inverse(w):
    r=[0]*n
    for k,a in enumerate(w): r[a-1]=k+1
    return r
def leq(u,w):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if sum(1 for k in range(i) if u[k]>=j) > sum(1 for k in range(i) if w[k]>=j): return False
    return True
def ins(w):
    P=[];Q=[]
    for k,x in enumerate(w,1):
        r=0
        while True:
            if r==len(P): P.append([x]);Q.append([k]);break
            big=[y for y in P[r] if y>x]
            if not big: P[r].append(x);Q[r].append(k);break
            y=min(big); P[r][P[r].index(y)]=x; x=y; r+=1
    return P,Q
def lstar(i,w):
    A=ldes(w)&{i,i+1}; assert len(A)==1
    c=[y for y in (sw(i,w),sw(i+1,w)) if len(ldes(y)&{i,i+1})==1 and (ldes(y)&{i,i+1})!=A]
    assert len(c)==1; return c[0]
def rstar(i,w): return inverse(lstar(i,inverse(w)))
def endpoint(a,b):
    la,lb=ln(a),ln(b)
    if (la-lb)%2==0: return 0
    lo,hi=(a,b) if la<lb else (b,a)
    if not leq(lo,hi): return 0
    for r in ldes(hi)-ldes(lo):
        if sw(r,hi)!=lo: return 0
    if abs(la-lb)==1: return 1
    raise AssertionError('undecided endpoint')
def replay(y,z,path):
    a,b=list(y),list(z)
    for side,i in path:
        f=lstar if side=='L' else rstar
        a,b=f(i,a),f(i,b)
    return endpoint(a,b)
def syts(shape):
    res=[]
    def rec(T,k):
        if k>n: res.append([r[:] for r in T]); return
        for r in range(len(shape)):
            if len(T[r])<shape[r] and (r==0 or len(T[r-1])>len(T[r])):
                T[r].append(k); rec(T,k+1); T[r].pop()
    rec([[] for _ in shape],1); return res
def des(T):
    row={v:r for r,R in enumerate(T) for v in R}; return {i for i in range(1,n) if row[i+1]>row[i]}
def rsk_inv(P,Q):  # brute: find w by reverse bumping
    P=[r[:] for r in P]; Q=[r[:] for r in Q]; w=[0]*n
    for k in range(n,0,-1):
        r=next(i for i,row in enumerate(Q) if row and row[-1]==k); Q[r].pop(); x=P[r].pop()
        for i in range(r-1,-1,-1):
            row=P[i]; j=max(j for j,y in enumerate(row) if y<x); row[j],x=x,row[j]
        w[k-1]=x
    assert ins(w)==(P_ if False else ins(w))
    return w
cache={}
for c in D:
    x,z=c['x'],c['z']; Lx,Lz=ldes(x),ldes(z); Q=ins(x)[1]
    assert ins(x)[0]==c['Px'] and ins(z)==(c['Pz'],Q) and x!=z and Lz and Lz<=Lx and Lx==set(c['A'])
    shape=tuple(len(r) for r in Q)
    if shape not in cache: cache[shape]=syts(shape)
    need=[sw(s,x) for s in range(1,n) if ins(sw(s,x))[1]==Q and not ldes(sw(s,x))<=Lx]
    Us=[T for T in cache[shape] if des(T)>Lx]
    Uw=[]
    for T in Us:
        y=rsk_inv(T,Q); assert ins(y)==(T,Q)
        uc=[u for u in c['Ucerts'] if u['y']==y]; assert len(uc)==1
        m=replay(y,x,uc[0]['path'])
        if m==1: need.append(y)
    assert sorted(map(tuple,need))==sorted(tuple(k['y']) for k in c['certs']),'y-set mismatch'
    vals=[replay(k['y'],z,k['path']) for k in c['certs']]
    v='TWIN' if all(vals) else 'NO'
    assert v==c['verdict'],(v,c['verdict'])
    print(shape,sorted(Lx),'Pz Des',sorted(Lz),'#y',len(vals),'#U',len(Us),'mu(y,z)',vals,v,'OK')
