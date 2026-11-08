# structural features of the 206 parity-failing candidate pairs; tightness A==N[L(z)]; evacuation-mirror pairing in open26
import json,sys
sys.path.insert(0,'/home/agent/projects/proofs/prove282')
from rskmod import rsk
from collections import Counter
P=json.load(open('/home/agent/projects/proofs/prove282/pfail.json'))
O=json.load(open('/home/agent/projects/proofs/prove282/open26.json'))
T=lambda P: tuple(tuple(r) for r in P)
def des(Tb,n):
    row={v:r for r,R in enumerate(Tb) for v in R}; return frozenset(i for i in range(1,n) if row[i+1]>row[i])
def runs(S):
    S=sorted(S); out=[]
    for s in S:
        if out and out[-1][-1]==s-1: out[-1].append(s)
        else: out.append([s])
    return out
def N(L,n): return frozenset(j for s in L for j in (s-1,s,s+1) if 1<=j<=n-1)
def evac(Tb,n):
    # evac via RSK of reversed-complemented reading word: P(w0 w w0) = evac P(w)
    w=[v for R in reversed(Tb) for v in R]   # reading word, P(w)=Tb
    assert T(rsk(w)[0])==T(Tb)
    w2=[n+1-v for v in reversed(w)]
    return rsk(w2)[0]
okeys={(tuple(o['lam']),T(o['Px']),T(o['Pz'])):i for i,o in enumerate(O)}
def feat(d):
    n=d['n']; A=frozenset(d['A']); Lz=des(d['Pz'],n)
    return dict(tight=(A==N(Lz,n)), extra=len(A-N(Lz,n)), AminusLz=len(A-Lz), runsA=[len(r) for r in runs(A)], runsLz=[len(r) for r in runs(Lz)], allsingle=all(len(r)==1 for r in runs(Lz)))
c=Counter()
for d in P:
    k=(tuple(d['lam']),T(d['Px']),T(d['Pz']))
    st='OPEN' if k in okeys else 'KILL'
    f=feat(d); c[(st,f['tight'],f['allsingle'])]+=1
print('(status,tight,L(z) all singleton runs):',dict(c))
print()
for i,o in enumerate(O):
    n=16; f=feat(o)
    m=(tuple(o['lam']),T(evac(o['Px'],n)),T(evac(o['Pz'],n)))
    print(i,o['lam'],'tight',f['tight'],'extra',f['extra'],'|A-Lz|',f['AminusLz'],'runsA',f['runsA'],'runsLz',f['runsLz'],'Lz',sorted(des(o['Pz'],n)),'evac-mirror->',okeys.get(m,'not in open26' if m not in okeys else None))
