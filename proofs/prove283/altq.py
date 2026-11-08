"""Alternative Qs for instances 0 and 1 (6,4,3,3): list distinct (x,z) with small l(z), for an independent mu check."""
import sys,json,random
sys.path.insert(0,'/home/agent/projects/proofs/prove283'); sys.path.insert(0,'/home/agent/projects/proofs/prove282')
from qsearch import hookwalk,swaps,score,rowsuper,colsuper
from rskmod import rsk
D=json.load(open('/home/agent/projects/proofs/prove282/open26.json'))
random.seed(7); seen={}
for k in (0,1):
    I=D[k]; Qs=[rowsuper(I['lam']),colsuper(I['lam'])]+[hookwalk(I['lam']) for _ in range(3000)]
    # one round of neighbours of the best ones
    sc=sorted(Qs,key=lambda Q:score(I,Q)[0])[:50]
    for Q in sc: Qs+=swaps(Q)
    for Q in Qs:
        lz,lx,x,z=score(I,Q)
        key=(tuple(x),tuple(z))
        if key not in seen: seen[key]=(k,lz,lx,Q)
L=sorted(seen.items(),key=lambda t:(t[1][1],t[1][1]-t[1][2]))
for (x,z),(k,lz,lx,Q) in L[:15]:
    assert [list(r) for r in rsk(list(x))[0]]==D[k]['Px'] and [list(r) for r in rsk(list(z))[0]]==D[k]['Pz']
    print(k,lz,lx,lz-lx,list(x),list(z))
