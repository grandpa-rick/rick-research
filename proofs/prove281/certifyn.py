"""Certificates for every exact candidate pair at n: for each needed mu, a two-sided star path to a decided endpoint."""
import sys,json; sys.path.insert(0,'.')
from common import *
from orbit2 import search12 as search2
n=int(sys.argv[1]); only=sys.argv[2]; V=json.load(open('viol%d.json'%n)); out=[]
for e in V:
    lam=tuple(e['lam']); A=set(e['A'])
    if ''.join(map(str,lam))!=only or not e['X']: continue
    t=syts(lam)[0]; Q=[[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
    for PXa in e['X']:
        x=rsk_inv(PXa,Q)
        Ucerts=[]; ys=[y for s,y in star_images(x)]
        for U in e['U']:
            y=rsk_inv(U,Q); st,p,_,_=search2(y,x); Ucerts.append(dict(y=y,verdict=st,path=p))
            if st=='mu=1': ys.append(y)
        for PZa in e['Z']:
            z=rsk_inv(PZa,Q); certs=[]
            for y in ys:
                st,p,_,_=search2(y,z); certs.append(dict(y=y,verdict=st,path=p))
            vs=[c['verdict'] for c in certs]
            verdict='TWIN' if all(v=='mu=1' for v in vs) and all(c['verdict']!='cap' and c['verdict']!='exhausted' for c in Ucerts) else ('NO' if any(v.startswith('kill') for v in vs) else 'UNDECIDED')
            print(lam,sorted(A),PXa,PZa,vs,[c['verdict'] for c in Ucerts],verdict,flush=True)
            out.append(dict(lam=lam,A=sorted(A),Q=Q,Px=PXa,Pz=PZa,x=x,z=z,Ucerts=Ucerts,certs=certs,verdict=verdict))
json.dump(out,open("certs%d_%s.json"%(n,only),"w"))
