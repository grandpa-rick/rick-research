import sympy as sp
u1,u2,u3,x = sp.symbols('u1 u2 u3 x')
E1,E2,E3 = sp.symbols('E1 E2 E3')
us=[u1,u2,u3]
coeffs = sp.Poly(sp.expand(sp.prod([x-u**3 for u in us])), x).all_coeffs()  # x^3 + c1 x^2 + ...
for i,name in [(1,'psi3(E1)'),(2,'psi3(E2)'),(3,'psi3(E3)')]:
    e = sp.expand(coeffs[i]*(-1)**i)
    p,r = sp.symmetrize(e, us, formal=False, symbols=[E1,E2,E3])
    print(name, "=", sp.expand(p), "   remainder:", sp.expand(r))
