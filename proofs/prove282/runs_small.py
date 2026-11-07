"""Nested mu-edges y-z (same left cell, L(z) strict subset L(y)): test run-wise interior variants."""
import sys; sys.path.insert(0,'../prove281')
from klperm import full_kl,L,MU
from rskmod import rsk
n=int(sys.argv[1])
W,P,mu=full_kl(n)
def runs(A):
    A=sorted(A); R=[]
    for a in A:
        if R and R[-1][-1]==a-1: R[-1].append(a)
        else: R.append([a])
    return R
def run_interior(Rn,Ly):  # run's outer neighbours all in L(y) (or off-diagram)
    i,j=Rn[0],Rn[-1]
    return (i==1 or i-1 in Ly) and (j==n-1 or j+1 in Ly)
cells={}
for w in W: cells.setdefault(rsk(w)[1],[]).append(w)
from collections import Counter
c=Counter(); ex=[]
for C in cells.values():
    for y in C:
        for z in C:
            Ly,Lz=L(y),L(z)
            if not Lz or not Lz<Ly or not MU(mu,y,z): continue
            rs=runs(Lz); k=sum(run_interior(r,Ly) for r in rs)
            c[(len(rs),k)]+=1
            if k==len(rs) and len(ex)<5: ex.append((y,z,sorted(Ly),sorted(Lz)))
print(n,'(#runs of Lz, #runs interior in Ly):',dict(c)); print(ex)
