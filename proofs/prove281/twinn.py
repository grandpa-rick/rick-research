"""For each exact (*)-violating (lam,A) at n (from viol<n>.json): every pair (Px,Pz). Decide twin in the cell Q=Q0
via star-orbit + F1/parity/Bruhat kills (Lemma S). y's to check: star images s x with L(y)!<=A (mu(y,x)=1) plus
all y=(U,Q) with Des U > A and mu(y,x)!=0 (y<x case, decided by orbit search)."""
import sys,json; sys.path.insert(0,'.')
from common import *
from orbit import search
n=int(sys.argv[1]); V=json.load(open('viol%d.json'%n))
only=sys.argv[2] if len(sys.argv)>2 else None
def mu01(a,b):
    st,_,_=search(list(a),list(b))
    return 1 if st=='mu=1' else 0 if st.startswith('kill') else None
res=[]
for e in V:
    lam=tuple(e['lam']); A=set(e['A'])
    if only and ''.join(map(str,lam))!=only: continue
    if not e['X']: continue
    t=syts(lam)[0]; Q=[[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
    for PXa in e['X']:
        x=rsk_inv(PXa,Q); assert rsk(x)==(PXa,Q) and L(x)==A
        ys=[(s,y) for s,y in star_images(x)]
        und=False; up=[]
        for U in e['U']:
            y=rsk_inv(U,Q); m=mu01(y,x); up.append(m)
            if m is None: und=True
            elif m: ys.append(('U',y))
        for PZa in e['Z']:
            z=rsk_inv(PZa,Q)
            vals=[mu01(y,z) for s,y in ys]
            verdict='TWIN' if all(v==1 for v in vals) and not und else ('no' if 0 in vals else 'UNDECIDED')
            print(lam,'A',sorted(A),'Px',PXa,'Pz',PZa,'Des Pz',sorted(L(z)),'ys',[s for s,y in ys],'mu(U,x)',up,'mu(y,z)',vals,verdict,flush=True)
            res.append(dict(lam=lam,A=sorted(A),Px=PXa,Pz=PZa,Q=Q,ys=[s for s,y in ys],muUx=up,vals=vals,verdict=verdict))
json.dump(res,open('twin%d_%s.json'%(n,only or 'all'),'w'))
