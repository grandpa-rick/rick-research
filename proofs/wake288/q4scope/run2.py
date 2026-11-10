import itertools,sys
from ind import ind_module
from loewy import loewy
def comps_sets(m): return [frozenset(S) for r in range(m) for S in itertools.combinations(range(1,m),r)]
def comp(S,m):
    c=[];prev=0
    for s in sorted(S)+[m]: c.append(s-prev); prev=s
    return tuple(c)
def inv(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
Nmax=int(sys.argv[1])
for N in range(3,Nmax+1):
  for a in range(1,N):
    b=N-a
    for S1 in comps_sets(a):
      for S2 in comps_sets(b):
        I,J=comp(S1,a),comp(S2,b)
        if len(set(I))==1 and I[0] in (1,a) and len(set(J))==1 and J[0] in(1,b): continue
        D=set(S1)|{s+a for s in S2}
        reps,mats=ind_module([a,b],D); n=len(reps)
        r,s=loewy(mats,n)
        rl=[r[k]-r[k+1] for k in range(len(r)-1)]; sl=[s[k+1]-s[k] for k in range(len(s)-1)][::-1]
        L=max(inv(w) for w in reps); lev=[sum(1 for w in reps if inv(w)==k) for k in range(L+1)]
        print(N,I,J,'dim',n,'rad layers',rl,'soc layers(top->bot)',sl,'rigid',rl==sl,'inv-levels',lev,flush=True)
