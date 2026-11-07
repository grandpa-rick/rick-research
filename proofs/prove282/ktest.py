"""Full-KL control of Prop K: same cell, Des T' subset Des T, |diff|>=2, corner c with rho_T(c)<rho_T'(c) => mu=0. Also evac mirror."""
import sys; sys.path.insert(0,'../prove281'); sys.path.insert(0,'.')
from klperm import full_kl,L,MU
from rskmod import rsk
from reduce import rb, corners
from corner import evac
n=int(sys.argv[1]); W,P,mu=full_kl(n)
cells={}
for w in W: cells.setdefault(rsk(w)[1],[]).append(w)
trig=bad=0
for C in cells.values():
    for x in C:
        for z in C:
            Lx,Lz=L(x),L(z)
            if not (Lz<Lx and len(Lx-Lz)>=2): continue
            T=[list(r) for r in rsk(x)[0]]; T2=[list(r) for r in rsk(z)[0]]
            hit=any(rb(A,c)[0]<rb(B,c)[0] for A,B in ((T,T2),(evac(T),evac(T2))) for c in corners(A))
            if hit:
                trig+=1
                if MU(mu,x,z): bad+=1
print('n',n,'Prop K triggered',trig,'violations',bad)
