from common import *
import sys
lam=(4,4,3,3); n=14; X,Z=(PX,PZ) if sys.argv[1:]!=['2'] else (PX2,PZ2)
if sys.argv[1:]==['2']: lam=(5,3,3,3)
best=None; hist={}
for t in syts(lam):
    Q=[[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
    x=rsk_inv(X,Q); z=rsk_inv(Z,Q)
    ys=star_images(x)
    gaps=tuple(sorted(inv(z)-inv(y) for s,y in ys))
    key=(max(gaps),sum(gaps))
    hist[gaps]=hist.get(gaps,0)+1
    if best is None or key<best[0]: best=(key,Q,gaps,inv(x),inv(z),[(s,str(rsk(y)[0])) for s,y in ys])
print('best',best)
for g,c in sorted(hist.items())[:15]: print(g,c)
