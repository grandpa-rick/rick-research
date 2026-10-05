import sympy as sp, pickle
E1,E2,E3=sp.symbols('E1 E2 E3')
HE=[sp.sympify(s) for s in pickle.load(open('HE8.pkl','rb'))]
# H = phi(tilde H): E1->-E1, E3->-E3
for n,h in enumerate(HE):
    H=sp.expand(h.subs({E1:-E1,E3:-E3},simultaneous=True))
    p=sp.Poly(H,E1,E2,E3)
    cs=p.coeffs()
    neg=[(m,c) for m,c in zip(p.monoms(),cs) if c<0]
    print("n=%d  #monomials=%d  min coeff=%s  negatives=%d"%(n,len(cs),min(cs),len(neg)))
    if neg: print("   ",neg[:5])
print()
print("H_3 =",sp.factor(sp.expand(HE[3].subs({E1:-E1,E3:-E3},simultaneous=True))))
print("H_4 =",sp.expand(HE[4].subs({E1:-E1,E3:-E3},simultaneous=True)))
