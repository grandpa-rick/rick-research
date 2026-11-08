"""Optimised version of parab.py (same math, u=-1): comparable-only via bitsets, strip common left descents
without memo, bytes keys, and two-sided orbit reuse: P_{y w_J,z} constant on W_I y W_J (I=L(z))."""
import sys,time
from kl import length, leq, padd, pmul, lswap, ldes, lower_covers
from parab import inWJ, minrep, maxrep
sys.setrecursionlimit(100000)

def dmax(y,I,J):
    y=tuple(y); ch=True
    while ch:
        ch=False
        for i in I:
            s=lswap(y,i)
            if length(s)>length(y): y=s; ch=True
        y2=maxrep(y,J)
        if y2!=y: y=y2; ch=True
    return y

class Parab2:
    def __init__(self,J):
        self.J=set(J); self.memo={}
    def R(self,s,t,ls,lt):
        n=len(s)
        while True:
            if s==t: return [1]
            if ls>=lt: return []
            # find left descent of t; prefer one that is also a left descent of s (strip)
            it=[0]*(n+2); is_=[0]*(n+2)
            for k in range(n): it[t[k]]=k; is_[s[k]]=k
            dt=[a for a in range(1,n) if it[a]>it[a+1]]
            hit=-1
            for a in dt:
                if is_[a]>is_[a+1]: hit=a; break
            if hit<0: break
            s=lswap(s,hit-1); t=lswap(t,hit-1); ls-=1; lt-=1
        key=bytes(s)+bytes(t)
        r=self.memo.get(key)
        if r is not None: return r
        if not leq(s,t): res=[]
        else:
            a=dt[0]; st=lswap(t,a-1); ss=lswap(s,a-1)   # s*sigma > sigma here
            if inWJ(ss,self.J): res=padd(pmul([-1,1],self.R(s,st,ls,lt-1)),pmul([0,1],self.R(ss,st,ls+1,lt-1)))
            else: res=pmul([0,1],self.R(s,st,ls,lt-1))
        self.memo[key]=res; return res

def run(x,z,verbose=True):
    t0=time.time()
    I=ldes(z); J=[j for j in range(len(z)-1) if z[j]>z[j+1]]
    assert maxrep(x,J)==x or True
    xm,zm=minrep(x,J),minrep(z,J)
    Js=set(J)
    seen={zm};fr=[zm]
    while fr:
        nf=[]
        for w in fr:
            for c in lower_covers(w):
                if c not in seen and inWJ(c,Js) and leq(xm,c): seen.add(c); nf.append(c)
        fr=nf
    E=list(seen); L={w:length(w) for w in E}
    rep={w:minrep(dmax(w,I,J),J) for w in E}
    E.sort(key=lambda w:(-L[w], 0 if rep[w]==w else 1))
    idx={w:k for k,w in enumerate(E)}
    upc=[[] for _ in E]
    for k,w in enumerate(E):
        for c in lower_covers(w):
            if c in idx: upc[idx[c]].append(k)
    up=[0]*len(E)
    for k in range(len(E)):
        b=1<<k
        for c in upc[k]: b|=up[c]
        up[k]=b
    nreps=sum(1 for w in E if rep[w]==w)
    npairs=sum(bin(up[k]).count('1')-1 for k in range(len(E)) if rep[E[k]]==E[k])
    if verbose: print('W^J interval',len(E),'orbit reps',nreps,'comparable pairs from reps',npairs,time.time()-t0,flush=True)
    pa=Parab2(J); lz=L[zm]; P={}; done=0
    for k,y in enumerate(E):
        if y==zm: P[y]=[1]; continue
        r=rep[y]
        if r!=y and r in P: P[y]=P[r]; continue
        ly=L[y]; rhs=[]
        b=up[k]&~(1<<k)
        while b:
            low=b&-b; j=low.bit_length()-1; b^=low
            t=E[j]; rr=pa.R(y,t,ly,L[t])
            if rr: rhs=padd(rhs,pmul(rr,P[t]))
        d=(lz-ly-1)//2
        p=[-(rhs[i] if i<len(rhs) else 0) for i in range(d+1)]
        while p and p[-1]==0: p.pop()
        Lg=lz-ly; chk=[0]*(Lg+1)
        for i,c in enumerate(p): chk[Lg-i]+=c; chk[i]-=c
        while chk and chk[-1]==0: chk.pop()
        assert chk==rhs,(y,p,rhs)
        P[y]=p; done+=1
        if verbose and done%500==0: print(k,done,len(pa.memo),time.time()-t0,flush=True)
    return P[xm],len(E),nreps
