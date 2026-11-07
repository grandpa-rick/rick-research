"""Connectivity of the right-star graph on left cells of shape lam (fixed P0): BFS w -> right stars; count distinct Q."""
import sys; sys.path.insert(0,'.')
from common import *
from orbit2 import rstar
from collections import deque
lam=tuple(int(c) for c in sys.argv[1]); n=sum(lam)
T=syts(lam); P0=[[k+1 for k in range(n) if T[0][k]==r] for r in range(len(lam))]
w0=tuple(rsk_inv(P0,P0)); seen={w0}; dq=deque([w0])
while dq:
    w=dq.popleft()
    for i in range(1,n-1):
        v=rstar(i,list(w))
        if v is not None and tuple(v) not in seen: seen.add(tuple(v)); dq.append(tuple(v))
Ps=set(str(rsk(list(w))[0]) for w in list(seen)[:2000])
print(lam,'f^lam',len(T),'reached',len(seen),'connected',len(seen)==len(T),'P constant on sample',len(Ps)==1,flush=True)
