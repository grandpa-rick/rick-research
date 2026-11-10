import itertools,sys,numpy as np
from ind import ind_module
from modp import P, nullspace_modp
from loewy import loewy
def comps_sets(m): return [frozenset(S) for r in range(m) for S in itertools.combinations(range(1,m),r)]
def comp(S,m):
    c=[];prev=0
    for s in sorted(S)+[m]: c.append(s-prev); prev=s
    return tuple(c)
proj=lambda c: len(set(c))==1 and (c[0]==1 or len(c)==1)
Nmax=int(sys.argv[1]); bad=0; cnt=0
for N in range(3,Nmax+1):
  for a in range(1,N):
    b=N-a
    for S1 in comps_sets(a):
      for S2 in comps_sets(b):
        I,J=comp(S1,a),comp(S2,b)
        D=set(S1)|{s+a for s in S2}
        reps,mats=ind_module([a,b],D); n=len(reps)
        G={i:np.array(A.tolist(),dtype=np.int64) for i,A in mats.items()}
        top=[];soc=[]
        for K in comps_sets(N):
            Hm=np.vstack([(G[i].T-(1 if i in K else 0)*np.eye(n,dtype=np.int64))%P for i in G])
            d=len(nullspace_modp(Hm))
            if d: top.append((comp(K,N),d))
            Sm=np.vstack([(G[i]-(1 if i in K else 0)*np.eye(n,dtype=np.int64))%P for i in G])
            d=len(nullspace_modp(Sm))
            if d: soc.append((comp(K,N),d))
        conc=I+J; near=I[:-1]+(I[-1]+J[0],)+J[1:]
        # descent convention: K = set where pi acts by 1; C_D with D=S1 u (S2+a): concatenation I.J has descent set D u {a}? check both
        Dc=comp(D|{a},N); Dn=comp(D,N)
        pred=sorted([(Dc,1),(Dn,1)])
        ok= sorted(top)==pred; cnt+=1; bad+= (not ok)
        r,s=loewy(mats,n) if n<=20 else ([],[])
        print(N,I,J,'dim',n,'top',top,'soc',soc,'topPred',ok,'LL',len(r)-1,flush=True)
print('cases',cnt,'top!=C_{D+a}+C_D:',bad)
