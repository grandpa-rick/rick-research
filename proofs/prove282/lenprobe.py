import sys,json,random
sys.path.insert(0,'.')
from cfg import rsk_inv, bru
from count_int import syt
random.seed(282)
def ln(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
D=json.load(open('pfail.json'))
from collections import Counter
c=Counter(); shapes={}
for d in D[:40]:
    lam=tuple(d['lam'])
    if lam not in shapes: shapes[lam]=random.sample(syt(lam),300) if len(syt(lam))>300 else syt(lam)
    Px,Pz=d['Px'],d['Pz']; best=-99; inc=0
    for Q in shapes[lam]:
        Q=[list(r) for r in Q]
        x=rsk_inv(Px,Q); z=rsk_inv(Pz,Q); dl=ln(x)-ln(z); best=max(best,dl)
        if not bru(x,z): inc+=1
    c[(best>0, inc>0)]+=1
    print(lam, 'max l(x)-l(z)=',best,'incomparable cells',inc,'/',len(shapes[lam]),flush=True)
print(c)
