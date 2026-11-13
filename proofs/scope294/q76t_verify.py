"""Independent re-check of Q76-T violations with prove281/klperm recursion restricted to lower ideal (computed)."""
import sys; sys.path.insert(0,'../prove281')
import klperm
from klperm import inv, lmul, L, bruhat_le
exec(open('cellinv.py').read().split("for n in range")[0].split("from collections")[1].split("\n",1)[1])
from itertools import permutations
def rsk_inv(Pt,Qt):
    P=[list(r) for r in Pt]; Q=[list(r) for r in Qt]; n=sum(map(len,P)); w=[0]*n
    for k in range(n,0,-1):
        r=next(i for i,row in enumerate(Q) if row and row[-1]==k); Q[r].pop(); a=P[r].pop()
        for i in range(r-1,-1,-1):
            row=P[i]; j=max(j for j,b in enumerate(row) if b<a); row[j],a=a,row[j]
        w[k-1]=a
        while P and not P[-1]: P.pop(); Q.pop()
    return tuple(w)
def kl_pair(x,y):
    n=len(y); W=sorted([w for w in permutations(range(1,n+1)) if bruhat_le(w,y)],key=inv)
    src=klperm.full_kl.__code__
    old=klperm.permutations; klperm.permutations=lambda r: W
    try: _,P,_=klperm.full_kl(n)
    finally: klperm.permutations=old
    return tuple(P[(x,y)]), inv(y)-inv(x)
P1=((1,3,6),(2,4,7),(5,)); P2=((1,2,3),(4,5,6),(7,))
for Q in [((1,3,6),(2,4,7),(5,)),((1,3,5),(2,4,6),(7,)),((1,3,5),(2,4,7),(6,)),((1,3,4),(2,5,7),(6,))]:
    x=rsk_inv(P1,Q); y=rsk_inv(P2,Q); assert rsk(x)==(P1,Q) and rsk(y)==(P2,Q)
    print(Q,x,y,"P,l(y)-l(x)=",kl_pair(x,y))
