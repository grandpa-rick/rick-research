"""K(tau F_P)/K(F_P)  =  Dwork defect of H = tau(F_P)/F_P   [order 'tau_before' = varsigma o tau]
   vs  tau(K)/K  literally                                  [order 'tau_after'  = tau o varsigma]
   These coincide iff tau and varsigma commute."""
import sys, time
from dwork_gen import *
N=int(sys.argv[1]) if len(sys.argv)>1 else 21
pts=[(-2,1),(0,0),(1,1),(2,-1),(0,1),(3,3),(-1,-1)]
variants=[('psi',PSI),('naive',NAIVE),('E3only',E3ONLY),('ident',IDENT)]
rows=[]
for order in ['tau_before','tau_after']:
    for (lname,lift) in variants:
        for (a,b) in pts:
            t=time.time()
            ok,first,minv,K,D=report(a,b,N,lift,lname,order,show=False)
            mn=min([v for v in minv.values() if v is not None],default=None)
            rows.append((lname,order,a,b,a+b+1,ok,first,mn,round(time.time()-t,1)))
print("="*104)
print(f"N={N}   'tau_before' = varsigma o tau = K(tau F_P)/K(F_P)  <-- the correct Dwork test for H")
print("="*104)
print(f"{'lift':8s} {'order':11s} {'(E1,E2)':12s} {'phi1':>5s} {'PASS':>6s} {'1stfail':>8s} {'minv3':>6s} {'sec':>6s}")
for r in rows:
    print(f"{r[0]:8s} {r[1]:11s} "+f"({r[2]},{r[3]})".ljust(12)+f"{r[4]:5d} {str(r[5]):>6s} {str(r[6]):>8s} {str(r[7]):>6s} {r[8]:>6}")
