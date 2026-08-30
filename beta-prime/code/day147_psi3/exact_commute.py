"""Is there a Frobenius lift varsigma on Z[E1,E2,E3] with varsigma o tau = tau o varsigma EXACTLY?
The conditions are LINEAR in the unknown coefficients of f_i = varsigma(E_i):
   f1(tauE) = f1 + 3
   f2(tauE) = f2 + 2 f1 + 3
   f3(tauE) = f3 + f1 + f2 + 1
plus f_i == E_i^3 mod 3."""
import sympy as sp, itertools
E1,E2,E3=sp.symbols('E1 E2 E3')
TAU={E1:E1+3,E2:E2+2*E1+3,E3:E3+E1+E2+1}
def tsub(p): return sp.expand(p.subs(TAU,simultaneous=True))

def monos(W):  # weighted degree <= W, weights 1,2,3
    out=[]
    for k in range(W//3+1):
        for j in range((W-3*k)//2+1):
            for i in range(W-3*k-2*j+1):
                out.append(E1**i*E2**j*E3**k)
    return out

def solve_step(target, W, label):
    """find g (weighted deg <= W) with  g(tauE) - g = target ; return one solution or None"""
    ms=monos(W); cs=sp.symbols(f'c0:{len(ms)}')
    g=sum(c*m for c,m in zip(cs,ms))
    eq=sp.expand(tsub(g)-g-target)
    P=sp.Poly(eq,E1,E2,E3)
    sol=sp.solve(P.coeffs(),cs,dict=True)
    if not sol: 
        print(f"  {label}: NO SOLUTION with weighted deg <= {W}"); return None
    s=sol[0]
    gg=sp.expand(g.subs({c:s.get(c,0) for c in cs}))
    # zero out free params
    gg=sp.expand(gg.subs({c:0 for c in cs}))
    chk=sp.expand(tsub(gg)-gg-target)
    print(f"  {label}: SOLUTION found (deg<= {W}): {gg}    verify={chk==0}")
    return gg

print("f1 = E1^3 + 3 g1 :  need g1(tauE)-g1 = 1 - (( (E1+3)^3 - E1^3 ) - 3)/3")
t1=sp.expand((sp.Integer(3) - sp.expand((E1+3)**3-E1**3))/3)
print("   target1 =",t1)
for W in [3,6,9]:
    g1=solve_step(t1,W,f"g1 (W={W})")
    if g1 is not None: break
