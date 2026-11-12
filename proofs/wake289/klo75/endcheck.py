# cross-check the cyclic-generator End algorithm against brute-force commutant (all shapes, d<=45)
import sys; from indmodel import *
p=32003; CS={m:connected_shapes(m) for m in range(1,8)}
bad=0;tot=0
for n in range(2,int(sys.argv[1])+1):
  for comps in all_shapes(n,CS):
    cells=star(comps); B,act,s=build_module(cells); d=len(B)
    if d>45: continue
    E,F_of,_,_=end_algebra(B,act,s,p); G=dense(act,d)
    H=hom_space(G,G,d,d,p); tot+=1
    nd,loc=local_test(E,F_of,p)
    # brute local test: random element of H, distinct eigenvalues
    import sympy as sp, random
    rnd=random.Random(3); X=sum(rnd.randrange(p)*h for h in H)%p
    t=sp.symbols('t'); cp=sp.Poly(sp.Matrix(X.tolist()).charpoly(t).as_expr(),t,modulus=p)
    nd2=sp.quo(cp,sp.gcd(cp,cp.diff(t))).degree()
    if len(H)!=len(E) or nd!=nd2: bad+=1; print('MISMATCH',lam_mu(cells),len(H),len(E),nd,nd2)
print('checked',tot,'mismatches',bad)
