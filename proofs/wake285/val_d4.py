import sys, random
sys.path.insert(0,'/home/agent/projects/proofs/wake279')
from coxkl import coxeter_group, kl
from run_pol import pol
n=4
M=[[1 if i==j else 2 for j in range(n)] for i in range(n)]
for a,b in [(0,2),(1,2),(2,3)]: M[a][b]=M[b][a]=3   # coxeter3 D labeling: 1,2 fork at 3
G=coxeter_group(M); P,mu=kl(G)
def fmt(c):
    t=[]
    for k,v in enumerate(c):
        if v: t.append((str(v) if v!=1 or k==0 else '')+('q^%d'%k if k>1 else 'q' if k==1 else ''))
    return '+'.join(reversed(t))
w=lambda i:''.join(str(s+1) for s in G['word'][i])
random.seed(0)
pairs=[(x,y) for x in range(G['N']) for y in range(G['N']) if P[x,y].any()]
nontriv=[p for p in pairs if P[p[0],p[1]].sum()>1]
print(len(pairs),'comparable pairs,',len(nontriv),'nontrivial')
samp=random.sample(pairs,150)+random.sample(nontriv,min(150,len(nontriv)))
bad=0
for x,y in samp:
    r,_=pol('D',4,w(x),w(y))
    if r!=fmt(P[x,y]): bad+=1; print('MISMATCH',w(x),w(y),r,fmt(P[x,y]))
print('checked',len(samp),'mismatches',bad)
