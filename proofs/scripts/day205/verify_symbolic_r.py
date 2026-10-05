"""Symbolic-in-r algebra: from Cor. G (a=1,2,3) plus e_1(tail) = e_1 - X_1 and
sigma_m(e_1 * f) = e_1 * sigma_m(f), derive (L1)-(L4) with r a SYMBOL.
e_n are treated as independent abstract symbols E(n) (sufficient: we only
need the derived expression to equal the claimed one identically)."""
import sympy as sp
t, r = sp.symbols('t r')
E = sp.Function('E')
e1, e2 = E(1), E(2)
br = lambda n: (1 - t**n)/(1 - t)          # [n]_t, valid for symbolic n
q = {0: 1, 1: (1-t)*e1, 2: (1-t)*e1**2 - (1-t**2)*e2}

def G(a, s):   # sigma_m[X_1^a e_s(tail)], Cor. G
    return ((-1)**a * t**(s+a) * E(s+a) + sum((-1)**(a-1-n) * q[n] * E(s+a-n) for n in range(a))) / (1-t)

L2 = G(2, r); L4 = G(3, r-1)
L1 = e1*G(1, r) - G(2, r)
L3 = e1*G(2, r-1) - G(3, r-1)
claims = {
 'L1': br(r+2)*E(r+2) + t*br(r)*E(r+1)*e1,
 'L2': -br(r+2)*E(r+2) + E(r+1)*e1,
 'L3': -br(r+2)*E(r+2) - t*br(r)*E(r+1)*e1 + (1+t)*E(r)*e2,
 'L4': br(r+2)*E(r+2) - E(r+1)*e1 - (1+t)*E(r)*e2 + E(r)*e1**2,
}
ok = True
for name, val in [('L1', L1), ('L2', L2), ('L3', L3), ('L4', L4)]:
    d = sp.simplify(sp.expand(sp.powsimp(sp.expand(val - claims[name]), force=True)))
    print(name, "symbolic-r difference:", d)
    ok &= (d == 0)
print("a=1 sanity: sigma[X_1 e_r(tail)] - [r+1]e_{r+1} =", sp.simplify(G(1, r) - br(r+1)*E(r+1)))
print("symbolic-in-r assembly:", "PASS" if ok else "FAIL")
