"""Every left cell (all Q) of the four n=14 shapes: twin verdict via star orbit + F1 (Lemma S)."""
from common import *
from orbit import search
import sys
cases={'4433':((4,4,3,3),PX,PZ),'5333':((5,3,3,3),PX2,PZ2),
 '4442':((4,4,4,2),[[1,4,8,12],[2,5,9,13],[3,6,10,14],[7,11]],[[1,3,4,5],[2,7,8,9],[6,11,12,13],[10,14]]),
 '44411':((4,4,4,1,1),[[1,4,8,12],[2,5,9,13],[3,6,10,14],[7],[11]],[[1,3,4,5],[2,7,8,9],[6,11,12,13],[10],[14]])}
lam,X,Z=cases[sys.argv[1]]; from collections import Counter; C=Counter()
for t in syts(lam):
    Q=[[k+1 for k in range(14) if t[k]==r] for r in range(len(lam))]
    x=rsk_inv(X,Q); z=rsk_inv(Z,Q)
    C[tuple(search(y,z)[0] for s,y in star_images(x))]+=1
print(sys.argv[1],dict(C),flush=True)
