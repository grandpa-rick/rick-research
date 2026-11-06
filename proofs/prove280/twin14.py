"""For each (*)-violating (lam,A) at n=14: every pair (Px,Pz), Des Px = A, {} != Des Pz subset int A.
Decide twin via star-orbit + F1 (decisions certified by KL79 Thm 4.2; undecided reported)."""
from common import *
from orbit import search
n=14
cases=[((5,3,3,3),{2,3,4,6,7,8,10,11,12}),((4,4,3,3),{2,3,4,6,7,8,10,11,12}),
       ((4,4,4,2),{1,2,4,5,6,8,9,10,12,13}),((4,4,4,1,1),{1,2,4,5,6,8,9,10,12,13})]
intr=lambda A:{i for i in A if all(j in A for j in (i-1,i+1) if 1<=j<=n-1)}
def tab(t,lam): return [[k+1 for k in range(n) if t[k]==r] for r in range(len(lam))]
def des(T):
    row={v:r for r,R in enumerate(T) for v in R}; return {i for i in range(1,n) if row[i+1]>row[i]}
def mu01(a,b):
    st,_,_=search(list(a),list(b))
    return 1 if st=='mu=1' else 0 if st.startswith('kill') else None
for lam,A in cases:
    I=intr(A); Ts=[tab(t,lam) for t in syts(lam)]
    Q=Ts[0]
    Xs=[T for T in Ts if des(T)==A]; Zs=[T for T in Ts if des(T) and des(T)<=I]
    Ups=[T for T in Ts if des(T)>A]
    print(lam,'A',sorted(A),'int',sorted(I),'#Px',len(Xs),'#Pz',len(Zs),'#P with Des>A',len(Ups))
    for PXa in Xs:
        x=rsk_inv(PXa,Q)
        ys=[y for s,y in star_images(x)]
        und=False
        for U in Ups:
            y=rsk_inv(U,Q); m=mu01(y,x)
            if m is None: und=True
            elif m: ys.append(y)
        for PZa in Zs:
            z=rsk_inv(PZa,Q)
            vals=[mu01(y,z) for y in ys]
            verdict='TWIN' if all(v==1 for v in vals) and not und else ('no' if 0 in vals else 'UNDECIDED')
            print('   Px',PXa,'Pz',PZa,'Des Pz',sorted(des(PZa)),'#y',len(ys),'mu(y,z)',vals,verdict)
