import sys,time
from dwork_gen import *
N=int(sys.argv[1]) if len(sys.argv)>1 else 30
pts=[(-2,1),(1,1),(0,0)]
for (a,b) in pts:
    print("\n"+"#"*90)
    print(f"### base point (E1,E2)=({a},{b})  phi1={a+b+1}   N={N}")
    tabs={}
    for lname,lift in [('psi',PSI),('naive',NAIVE),('E3only',E3ONLY)]:
        t=time.time()
        ok,first,minv,K,D=report(a,b,N,lift,lname,'tau_before',show=False)
        tabs[lname]=(ok,first,minv,D)
        print(f"  lift={lname:7s} PASS={ok} first_fail={first} "
              f"min_v3={min([v for v in minv.values() if v is not None],default=None)}  ({time.time()-t:.1f}s)")
    print("  per-T-degree MINIMUM v3 of tau-Dwork-defect coefficients:")
    print("    n   " + "".join(f"{n:4d}" for n in range(1,N+1)))
    for lname in tabs:
        mv=tabs[lname][2]
        print(f"    {lname:6s}" + "".join(f"{(mv.get(n) if mv.get(n) is not None else '.'):>4}" for n in range(1,N+1)))
    # H integrality (equivalent statement)
    P=getP(N); F=series(P,N,IDENT,a,b); Ft=series(P,N,TAUL,a,b)
    H=Smul(Ft,Sinv(F,N),N)
    bad=[(n,i,str(c)) for n,p in H.items() for i,c in enumerate(p) if c.denominator!=1]
    print("  H = tau(F_P)/F_P integral (equivalent to the criterion):", "YES" if not bad else bad[:4])
