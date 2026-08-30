from dwork_gen import *
N=12
print("### SANITY 1: lift = IDENT (no twist) at (-2,1)  -- must reproduce dwork.py failure at T^9")
report(-2,1,N,IDENT,'ident')
print("\n### SANITY 2: lift = E3ONLY (day146 fibrewise twist) at (-2,1), order tau_before")
report(-2,1,N,E3ONLY,'E3only','tau_before')
print("\n### SANITY 3: H = tau(F_P)/F_P integral at (-2,1)? (day146 Conjecture H)")
P=getP(N); F=series(P,N,IDENT,-2,1); Ft=series(P,N,TAUL,-2,1)
H=Smul(Ft,Sinv(F,N),N)
bad=[(n,i,c) for n,p in H.items() for i,c in enumerate(p) if c.denominator!=1]
print("   H integral:", "YES" if not bad else bad[:5])
print("   H_n for n<=6:", {n:[str(c) for c in H.get(n,[])] for n in range(7)})
