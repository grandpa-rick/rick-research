"""BFS over simultaneous left-star orbit of (y,z) (KL79 Thm 4.2: mu invariant). Look for F1-kill or gap-1 pair."""
from common import *
import sys
from collections import deque
def star(i,w):
    Lw=L(w)
    if len(Lw&{i,i+1})!=1: return None
    for y in (lmul(i,w),lmul(i+1,w)):
        Ly=L(y)
        if len(Ly&{i,i+1})==1 and (Ly&{i,i+1})!=(Lw&{i,i+1}): return y
def status(y,z):
    ly,lz=inv(y),inv(z)
    if (ly-lz)%2==0: return 'kill-parity',0
    lo,hi=(y,z) if ly<lz else (z,y)
    if not bruhat_le(lo,hi): return 'kill-incomparable',0
    for r in L(hi)-L(lo):
        if lmul(r,hi)!=lo: return 'kill-F1',0
    if abs(ly-lz)==1: return 'mu=1',1
    return 'open',abs(ly-lz)
def search(y,z,cap=200000):
    n=len(y); start=(tuple(y),tuple(z)); seen={start}; dq=deque([start]); best=None
    while dq:
        a,b=dq.popleft()
        st,g=status(list(a),list(b))
        if st!='open': return st,(a,b),len(seen)
        if best is None or g<best[0]: best=(g,(a,b))
        for i in range(1,n-1):
            a2=star(i,list(a))
            if a2 is None: continue
            b2=star(i,list(b))
            if b2 is None: continue
            nxt=(tuple(a2),tuple(b2))
            if nxt not in seen:
                seen.add(nxt); dq.append(nxt)
                if len(seen)>cap: return 'cap',best,len(seen)
    return 'exhausted',best,len(seen)
if __name__=='__main__':
    which=sys.argv[1] if len(sys.argv)>1 else '1'
    X,Z,lam=(PX,PZ,(4,4,3,3)) if which=='1' else (PX2,PZ2,(5,3,3,3))
    Q=[[1, 2, 3, 4], [5, 6, 7, 14], [8, 9, 10], [11, 12, 13]] if which=='1' else None
    if Q is None:
        t=syts(lam)[0]; Q=[[k+1 for k in range(14) if t[k]==r] for r in range(len(lam))]
    x=rsk_inv(X,Q); z=rsk_inv(Z,Q)
    for s,y in star_images(x):
        st,info,sz=search(y,z)
        print('s',s,'P(y)',rsk(y)[0],'->',st,'orbit-size',sz, (rsk(list(info[0]))[0],rsk(list(info[1]))[0],inv(info[0]),inv(info[1])) if st not in('cap','exhausted') else info[0])
