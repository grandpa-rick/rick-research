"""Task 1 & 2: Adams psi^3 on Sym_3 in E-coordinates; tau-commutation defects."""
import sympy as sp
from sympy.polys.polyfuncs import symmetrize

u1,u2,u3 = sp.symbols('u1 u2 u3')
E1,E2,E3 = sp.symbols('E1 E2 E3')
Ev = [E1,E2,E3]
e = [u1+u2+u3, u1*u2+u1*u3+u2*u3, u1*u2*u3]

def toE(expr):
    sym, rem, gens = symmetrize(sp.expand(expr), [u1,u2,u3], formal=True)
    assert sp.expand(rem)==0, ("not symmetric", rem)
    sub = {g[0]: Ev[i] for i,g in enumerate(gens)}
    out = sp.expand(sym.subs(sub, simultaneous=True))
    # verify
    assert sp.expand(out.subs({E1:e[0],E2:e[1],E3:e[2]}, simultaneous=True) - sp.expand(expr))==0
    return out

print("="*70); print("TASK 1: psi^3(E_i) = e_i(u^3) in terms of E"); print("="*70)
psi = []
for i,name in enumerate(['E1','E2','E3']):
    f = sp.expand(sp.together(e[i].subs({u1:u1**3,u2:u2**3,u3:u3**3}, simultaneous=True)))
    f = sp.expand(sp.prod([1]) * sp.expand(f))
    ex = toE(sp.expand(f))
    psi.append(ex)
    print(f"  psi^3({name}) = {ex}")
    d = sp.Poly(sp.expand(ex - Ev[i]**3), E1,E2,E3)
    nz = [(m,c) for m,c in zip(d.monoms(), d.coeffs()) if c % 3 != 0]
    print(f"     psi^3({name}) - {name}^3 = {sp.expand(ex-Ev[i]**3)}   ->  == 0 mod 3 ? {'YES' if not nz else nz}")

# also express psi^3(E1) as power sum p3
p3 = sp.expand(toE(u1**3+u2**3+u3**3))
print("  (check) p_3 in E =", p3, " equals psi^3(E1)?", sp.expand(p3-psi[0])==0)

print()
print("="*70); print("TASK 2: tau-commutation"); print("="*70)

# --- two candidate taus ---
# tau_A : the one stated in the task brief
tauA = {E1: E1, E2: E2, E3: E3 + (E2+E1+1)}
# tau_B : the one actually implemented in day146 verify_master.py / core.py  == u_i -> u_i+1
tauB = {E1: E1+3, E2: E2+2*E1+3, E3: E3+E2+E1+1}

# confirm tau_B is induced by u -> u+1
for i,name in enumerate(['E1','E2','E3']):
    lhs = toE(sp.expand(e[i].subs({u1:u1+1,u2:u2+1,u3:u3+1}, simultaneous=True)))
    print(f"  e_{i+1}(u+1) in E = {lhs}   ==  tau_B({name})? {sp.expand(lhs - tauB[Ev[i]])==0}")

def apply_map(expr, m):
    return sp.expand(expr.subs(m, simultaneous=True))

def defects(tau, lift, label):
    print(f"\n--- {label} ---")
    worst = []
    for i,name in enumerate(['E1','E2','E3']):
        # tau o lift  (E_i)  = tau( lift(E_i) )
        a = apply_map(lift[i], tau)
        # lift o tau (E_i) = lift applied to tau(E_i): substitute E_j -> lift[j]
        liftmap = {E1:lift[0], E2:lift[1], E3:lift[2]}
        b = apply_map(tau[Ev[i]], liftmap)
        d = sp.expand(a-b)
        dp = sp.Poly(d, E1,E2,E3) if d != 0 else None
        d3 = 0 if dp is None else sp.expand(sum(sp.Integer(c%3)*sp.prod([g**k for g,k in zip((E1,E2,E3),m)])
                                                for m,c in zip(dp.monoms(),dp.coeffs())))
        print(f"  {name}:  tau(lift) - lift(tau) = {d}")
        print(f"        mod 3: {d3}")
        worst.append(d3)
    return worst

naive = [E1**3, E2**3, E3**3]
defects(tauA, psi,   "tau_A (brief's tau: E3 -> E3+phi1 only)   with psi^3")
defects(tauA, naive, "tau_A                                      with naive E_i^3")
defects(tauB, psi,   "tau_B (day146 actual tau = u->u+1)         with psi^3")
dn = defects(tauB, naive, "tau_B                                      with naive E_i^3")

print()
print("  naive/tau_B defect mod 3 factored:")
for i,x in enumerate(dn):
    print(f"    E{i+1}: {sp.factor(x)}")
phi1 = E2+E1+1
print("  phi1 =", phi1)
for i,x in enumerate(dn):
    if x!=0:
        q,r = sp.div(sp.Poly(x,E1,E2,E3), sp.Poly(phi1,E1,E2,E3))
        print(f"    E{i+1}: divisible by phi1? rem={r.as_expr()}   quotient={q.as_expr()}")
