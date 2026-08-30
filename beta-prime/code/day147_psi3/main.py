import sys, time
from dwork_gen import *
N=int(sys.argv[1]) if len(sys.argv)>1 else 18
pts=[(-2,1),(0,0),(1,1),(2,-1),(0,1)]
variants=[('psi',PSI,'tau_after'),('naive',NAIVE,'tau_after'),
          ('E3only',E3ONLY,'tau_before'),('E3only',E3ONLY,'tau_after'),
          ('ident',IDENT,'tau_after')]
rows=[]
for (lname,lift,order) in variants:
    for (a,b) in pts:
        t=time.time()
        ok,first,minv,K,D=report(a,b,N,lift,lname,order,show=(a,b) in [(-2,1),(0,0)])
        mn=min([v for v in minv.values() if v is not None],default=None)
        rows.append((lname,order,a,b,a+b+1,ok,first,mn,round(time.time()-t,1)))
print("\n"+"="*100)
print(f"{'lift':8s} {'order':11s} {'(E1,E2)':10s} {'phi1':>5s} {'PASS':>6s} {'1st fail':>9s} {'min v3':>7s} {'sec':>6s}")
print("="*100)
for r in rows:
    print(f"{r[0]:8s} {r[1]:11s} ({r[2]},{r[3]})".ljust(32)+f"{r[4]:5d} {str(r[5]):>6s} {str(r[6]):>9s} {str(r[7]):>7s} {r[8]:>6}")
