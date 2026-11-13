# Is C'_u * C'_v (FQSym-type shuffle convolution, q=1) KL-positive in the C' basis of Q S_n?
import sys, itertools; sys.path.insert(0,'../prove281')
from klperm import full_kl, inv
N=int(sys.argv[1])
KL={n:full_kl(n) for n in range(1,N+1)}
def Cp(n,w):  # C'_w at q=1 as dict perm->int
    W,P,mu=KL[n]; return {x:sum(P[(x,w)]) for x in W if (x,w) in P}
def comp(a,b): return tuple(a[b[i]-1] for i in range(len(b)))  # (a∘b)(i)=a(b(i))
def toC(n,E):  # triangular solve in C' basis (top length first)
    W,P,mu=KL[n]; E=dict(E); out={}
    for w in sorted(W,key=inv,reverse=True):
        c=E.get(w,0)
        if c:
            out[w]=c
            for x,p in Cp(n,w).items(): E[x]=E.get(x,0)-c*p
    assert all(v==0 for v in E.values()); return out
for n in range(2,N+1):
  for a in range(1,n):
    b=n-a
    grass=[s for s in itertools.permutations(range(1,n+1)) if all(s[i]<s[i+1] for i in range(n-1) if i!=a-1)]
    for side in ("right","left"):
     for sgs,lab in ((grass,"G"),([tuple(sorted(range(1,n+1),key=lambda k:s[k-1])) for s in grass],"Ginv")):
      neg=0;tot=0;ex=None
      for u in KL[a][0]:
        for v in KL[b][0]:
          E={}
          for x,px in Cp(a,u).items():
            for y,py in Cp(b,v).items():
              xy=tuple(list(x)+[a+k for k in y])
              for s in sgs:
                w=comp(xy,s) if side=="right" else comp(s,xy)
                E[w]=E.get(w,0)+px*py
          C=toC(n,E); tot+=1
          if any(c<0 for c in C.values()): neg+=1; ex=ex or (u,v,{k:c for k,c in C.items() if c<0})
      print(n,(a,b),side,lab,"nonpositive",neg,"/",tot, ex if ex else "")
