"""Task 2 addendum: mod-3 commutation is TRIVIAL for any Frobenius lift.
So compare at the delta-ring level: defect/3 mod 3."""
import sympy as sp
E1,E2,E3=sp.symbols('E1 E2 E3'); Ev=[E1,E2,E3]
psi  = [E1**3-3*E1*E2+3*E3, E2**3-3*E1*E2*E3+3*E3**2, E3**3]
naive= [E1**3, E2**3, E3**3]
tauA = {E1:E1, E2:E2, E3:E3+E1+E2+1}
tauB = {E1:E1+3, E2:E2+2*E1+3, E3:E3+E1+E2+1}
phi1 = E1+E2+1

def red(p,m):
    p=sp.expand(p)
    if p==0: return sp.Integer(0)
    P=sp.Poly(p,E1,E2,E3)
    return sp.expand(sum(sp.Integer(c%m)*sp.prod([g**k for g,k in zip((E1,E2,E3),mo)])
                         for mo,c in zip(P.monoms(),P.coeffs())))

for tname,tau in [('tau_A (brief)',tauA),('tau_B (day146 real, u->u+1)',tauB)]:
    for lname,lift in [('psi^3',psi),('naive E^3',naive)]:
        print(f"--- {tname} x {lname} ---")
        lm={E1:lift[0],E2:lift[1],E3:lift[2]}
        for i,n in enumerate(['E1','E2','E3']):
            a=sp.expand(lift[i].subs(tau,simultaneous=True))
            b=sp.expand(tau[Ev[i]].subs(lm,simultaneous=True))
            d=sp.expand(a-b)
            assert sp.expand(d/3)==sp.cancel(d/3)
            d3=sp.expand(d/3)
            r=red(d3,3)
            div = "n/a"
            if r!=0:
                q,rem=sp.div(sp.Poly(r,E1,E2,E3),sp.Poly(phi1,E1,E2,E3))
                div = f"rem mod phi1 = {red(rem.as_expr(),3)}"
            print(f"   {n}: (defect)/3 mod 3 = {r}    [{div}]")
        print()
