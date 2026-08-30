"""Decide: does ANY Frobenius lift on Z[E1,E2,E3] commute with tau exactly?
Step 1: solve f1(tauE) = f1 + 3  in weighted degree <= W, get affine solution space.
Step 2: ask whether some solution has integer coeffs and f1 == E1^3 mod 3."""
import sympy as sp
E1,E2,E3=sp.symbols('E1 E2 E3')
TAU={E1:E1+3,E2:E2+2*E1+3,E3:E3+E1+E2+1}
def tsub(p): return sp.expand(sp.sympify(p).subs(TAU,simultaneous=True))
def monos(W):
    out=[]
    for k in range(W//3+1):
        for j in range((W-3*k)//2+1):
            for i in range(W-3*k-2*j+1):
                out.append(E1**i*E2**j*E3**k)
    return out

for W in [3,6,9,12]:
    ms=monos(W); cs=list(sp.symbols(f'c0:{len(ms)}'))
    g=sum(c*m for c,m in zip(cs,ms))
    eq=sp.expand(tsub(g)-g-3)          # want f1(tau)-f1 = 3
    P=sp.Poly(eq,E1,E2,E3)
    sol=sp.solve(P.coeffs(),cs,dict=True)
    assert sol
    s=sol[0]
    gsol=sp.expand(g.subs(s))
    free=sorted([c for c in cs if c not in s], key=lambda z:str(z))
    # decompose: particular + span of free params
    part=sp.expand(gsol.subs({c:0 for c in free}))
    basis=[sp.expand(gsol.subs({c:(1 if c==f else 0) for c in free})-part) for f in free]
    print(f"W={W}: particular f1 = {part}")
    print(f"   invariant basis ({len(basis)}):", [sp.factor(b) for b in basis])
    # now: can  part + sum a_i basis_i  be integral and == E1^3 mod 3 ?
    a=list(sp.symbols(f'a0:{len(basis)}'))
    f=sp.expand(part+sum(ai*bi for ai,bi in zip(a,basis)))
    diff=sp.expand(f-E1**3)
    Pd=sp.Poly(diff,E1,E2,E3)
    print("   need every coeff of (f1 - E1^3) divisible by 3; coeffs:")
    for m,c in zip(Pd.monoms(),Pd.coeffs()):
        print("      ",m,"->",sp.nsimplify(c))
    print()
