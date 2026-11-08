"""Own parabolic (Deodhar, right W_J) KL computation on minimal coset reps W^J.
R^J recursion on a left descent s of tau (sigma,tau in W^J):
  s sigma<sigma:                 R^J(s sigma, s tau)
  s sigma>sigma, s sigma in W^J: (q-1)R^J(sigma,s tau)+q R^J(s sigma,s tau)
  s sigma not in W^J:            (q-1-u) R^J(sigma, s tau),  u in {-1,q}
Inversion: q^{l(tau)-l(sigma)} Pbar - P = sum_{sigma<g<=tau, g in W^J} R^J_{sigma,g} P^J_{g,tau}.
Claim to validate: with u=q, P^J_{sigma,tau} = P_{sigma w_J, tau w_J}."""
import sys
from kl import length, leq, padd, pmul, lswap, ldes, lower_covers
sys.setrecursionlimit(100000)

def blocks(J,n):
    # J: 0-indexed simple reflections (positions j,j+1); return list of position blocks
    bl=[];cur=[0]
    for p in range(1,n):
        if p-1 in J: cur.append(p)
        else: bl.append(cur); cur=[p]
    bl.append(cur); return bl
def minrep(w,J):
    w=list(w)
    for b in blocks(J,len(w)):
        vals=sorted(w[p] for p in b)
        for p,v in zip(b,vals): w[p]=v
    return tuple(w)
def maxrep(w,J):
    w=list(w)
    for b in blocks(J,len(w)):
        vals=sorted((w[p] for p in b),reverse=True)
        for p,v in zip(b,vals): w[p]=v
    return tuple(w)
def inWJ(w,J): return all(w[j]<w[j+1] for j in J)

class Parab:
    def __init__(self,J,u):
        self.J=list(J); self.u=u; self.memo={}
        self.c3=padd([-1,1],[0,-1]) if u=='q' else [0,1]   # q-1-u
    def R(self,s,t):
        if s==t: return [1]
        key=(s,t)
        if key in self.memo: return self.memo[key]
        ls,lt=length(s),length(t)
        if ls>=lt or not leq(s,t): self.memo[key]=[]; return []
        i=ldes(t)[0]; st=lswap(t,i); ss=lswap(s,i)
        if length(ss)<ls: res=self.R(ss,st)
        elif inWJ(ss,self.J): res=padd(pmul([-1,1],self.R(s,st)),pmul([0,1],self.R(ss,st)))
        else: res=pmul(self.c3,self.R(s,st))
        self.memo[key]=res; return res
    def interval(self,x,z):
        J=self.J
        if not leq(x,z): return []
        seen={z};fr=[z]
        while fr:
            nf=[]
            for w in fr:
                for c in lower_covers(w):
                    if c not in seen and inWJ(c,J) and leq(x,c): seen.add(c); nf.append(c)
            fr=nf
        return list(seen)
    def P(self,x,z,verbose=False):
        import time; t0=time.time()
        I=self.interval(x,z); L={w:length(w) for w in I}
        I.sort(key=lambda w:-L[w]); lz=L[z]
        if verbose: print('W^J interval size',len(I),flush=True)
        P={}
        for k,y in enumerate(I):
            if y==z: P[y]=[1]; continue
            ly=L[y]; rhs=[]
            for t in I[:k]:
                if L[t]>ly:
                    r=self.R(y,t)
                    if r: rhs=padd(rhs,pmul(r,P[t]))
            d=(lz-ly-1)//2
            p=[-(rhs[i] if i<len(rhs) else 0) for i in range(d+1)]
            while p and p[-1]==0: p.pop()
            Lg=lz-ly; chk=[0]*(Lg+1)
            for i,c in enumerate(p): chk[Lg-i]+=c; chk[i]-=c
            while chk and chk[-1]==0: chk.pop()
            if chk!=rhs: raise ValueError(('inconsistent',y,p,rhs))
            P[y]=p
            if verbose and k%200==0: print(k,len(self.memo),time.time()-t0,flush=True)
        return P,len(I)
