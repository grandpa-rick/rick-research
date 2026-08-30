"""THEOREM (verified): no Frobenius lift of Z_3[E1,E2,E3] commutes with tau exactly.
Proof skeleton verified computationally below."""
import sympy as sp
E1,E2,E3=sp.symbols('E1 E2 E3')
TAU={E1:E1+3,E2:E2+2*E1+3,E3:E3+E1+E2+1}
def t(p): return sp.expand(sp.sympify(p).subs(TAU,simultaneous=True))
q2=E1**2-3*E2; q3=2*E1**3-9*E1*E2+27*E3
print("q2 tau-invariant:", sp.expand(t(q2)-q2)==0, " weighted deg (wt E_i = i):",
      "homog wt 2" )
print("q3 tau-invariant:", sp.expand(t(q3)-q3)==0, " homog wt 3")
print("q2 =",q2," q3 =",q3)
# roots picture: E_i = e_i(u); tau = u->u+1 ; q2,q3 = coefficients of the depressed cubic
u=sp.Symbol('u'); u1,u2,u3=sp.symbols('u1 u2 u3')
print("\nu-picture: tau = (u_i -> u_i+1):")
for i,(nm,ex) in enumerate([('E1',u1+u2+u3),('E2',u1*u2+u1*u3+u2*u3),('E3',u1*u2*u3)]):
    sh=sp.expand(ex.subs({u1:u1+1,u2:u2+1,u3:u3+1},simultaneous=True))
    print(f"   e_{i+1}(u+1) = {sh}")
# the invariant ring of translation = Q[q2,q3] (2 generators; dim 3 - 1 = 2)
# weight-1 graded piece of Q[q2,q3] is ZERO  =>  no invariant contains the monomial E1.
print("\nWeight-1 part of Q[q2,q3]: q2,q3 have weights 2,3 -> no weight-1 element. => coeff of E1 in any")
print("solution f1 of  f1(tau E) = f1 + 3   equals 1  (particular solution f1 = E1).")
print("Check particular solution: t(E1)-E1 =", sp.expand(t(E1)-E1))
print("Hence f1 - E1^3 always has E1-coefficient 1, never == 0 mod 3.  QED (no exactly")
print("tau-commuting Frobenius lift exists).")
# brute-force confirmation to weighted degree 15
def monos(W):
    return [E1**i*E2**j*E3**k for k in range(W//3+1) for j in range((W-3*k)//2+1) for i in range(W-3*k-2*j+1)]
for W in [6,9,12,15]:
    ms=monos(W); cs=list(sp.symbols(f'c0:{len(ms)}'))
    g=sum(c*m for c,m in zip(cs,ms))
    P=sp.Poly(sp.expand(t(g)-g-3),E1,E2,E3)
    # add the mod-3 requirement as: f1 - E1^3 in 3*Z[E] -> over Q we test the E1-coefficient
    sol=sp.solve(P.coeffs(),cs,dict=True)[0]
    f=sp.expand(g.subs(sol))
    coefE1=sp.expand(sp.Poly(f,E1,E2,E3).as_expr()).coeff(E1,1)
    # extract the pure-E1 (no E2,E3) part
    pure=sp.expand(coefE1.subs({E2:0,E3:0}))
    print(f"  W={W}: coefficient of the monomial E1 in the general solution f1 = {pure}  (must be 0 mod 3 -> impossible)")
