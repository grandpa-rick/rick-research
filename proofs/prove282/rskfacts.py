"""Exhaustive check n<=8 of textbook RSK facts used (recall-only premises): R1 P(w\\n)=P(w)\\n; R2 RSK(w^-1)=(Q,P);
R3 RSK(w0 w w0)=(evac P, evac Q); R5 Q(y\\n)=Q(z\\n) when Q(y)=Q(z) and n in same row of P(y),P(z)."""
import sys; sys.path.insert(0,'.')
from itertools import permutations
from rskmod import rsk
from corner import evac
ok={1:0,2:0,3:0,5:0}; tot=0
for n in range(2,9):
    byQ={}
    for w in permutations(range(1,n+1)):
        w=list(w); P,Q=rsk(w); tot+=1
        wd=[a for a in w if a!=n]; Pd,Qd=rsk(wd)
        Pm=tuple(tuple(v for v in R if v!=n) for R in P if tuple(R)!=(n,))
        ok[1]+= (Pd==Pm)
        wi=[0]*n
        for i,a in enumerate(w): wi[a-1]=i+1
        ok[2]+= (rsk(wi)==(Q,P))
        wc=[n+1-a for a in reversed(w)]
        Pe,Qe=rsk(wc); ok[3]+= ([list(r) for r in Pe]==evac(P) and [list(r) for r in Qe]==evac(Q))
        r=next(i for i,R in enumerate(P) if n in R)
        byQ.setdefault((Q,r),[]).append(Qd)
    for k,v in byQ.items(): ok[5]+= all(q==v[0] for q in v)
print('total perms',tot,'R1',ok[1],'R2',ok[2],'R3',ok[3],'R5 classes ok',ok[5],'of',None)
