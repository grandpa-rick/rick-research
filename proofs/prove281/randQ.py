"""Cross-check: twin verdict of (Px,Pz) recomputed from scratch in random left cells (fresh y-set each time)."""
import sys,json,random; sys.path.insert(0,'.')
from common import *
from orbit2 import search12
random.seed(int(sys.argv[2])); n=15
C=json.load(open('certs15_%s.json'%sys.argv[1]))
T=None
for c in C:
    lam=tuple(c['lam'])
    if T is None: T=syts(lam)
    for trial in range(int(sys.argv[3])):
        t=random.choice(T); Q=[[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
        x=rsk_inv(c['Px'],Q); z=rsk_inv(c['Pz'],Q); A=L(x)
        ys=set(tuple(y) for s,y in star_images(x))
        for t2 in T:
            U=[[k+1 for k in range(n) if t2[k]==r] for r in range(len(lam))]
            if set(U and [i for i in range(1,n) if [r for r,R in enumerate(U) if i+1 in R][0]>[r for r,R in enumerate(U) if i in R][0]])>A:
                y=rsk_inv(U,Q)
                if search12(y,x)[0]=='mu=1': ys.add(tuple(y))
        vs=[search12(list(y),z)[0] for y in ys]
        v='TWIN' if all(a=='mu=1' for a in vs) else ('NO' if any(a.startswith('kill') for a in vs) else 'UND')
        print(c['A'],c['Pz'][0],'stored',c['verdict'],'randomQ',v,'agree',v==c['verdict'],flush=True)
