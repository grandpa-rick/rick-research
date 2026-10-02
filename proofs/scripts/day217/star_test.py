"""Test 3: s_lam * s_mu at t=1/s via e-star expansion: s_lam = sum_rho a_rho E_rho(1) (E_rho = E_{rho_1}...E_{rho_l})."""
import sys
sys.argv = [sys.argv[0], sys.argv[1], 'none']
exec(open('/home/agent/projects/proofs/scripts/day217/content_twist.py').read())
def Erho(rho, F, xs, V):
    for k in reversed(rho): F = Ek(k, F, xs, V)
    return F
def star(lam, mu):
    n = sum(lam); N = n+sum(mu)
    xn, Vn = setup(n); V_[n] = Vn
    P = list(parts(n))
    G = sp.Matrix(len(P), len(P), lambda i, j: 0)
    for i, rho in enumerate(P):
        d = to_schur(Erho(rho, sp.Poly(1, *xn, domain=DOM), xn, Vn), n)
        for j, nu in enumerate(P): G[i, j] = d.get(nu, 0)
    Gi = G.inv()   # s_nu = sum_rho Gi[nu,rho] E_rho(1)
    j = P.index(lam); coeffs = {rho: sp.factor(Gi[j, i]) for i, rho in enumerate(P) if Gi[j, i] != 0}
    log(f'  s_{lam} = sum a_rho E_rho(1): {coeffs}')
    xs, V = setup(N); V_[N] = V
    Fmu = schur(mu, xs, V); tot = sp.Poly(0, *xs, domain=DOM)
    for rho, a in coeffs.items(): tot += sp.Poly(a, *xs, domain=DOM)*Erho(rho, Fmu, xs, V)
    return to_schur(tot, N), N, xs
for lam, mu in [((2,), (1, 1)), ((1, 1), (2,)), ((2,), (2,)), ((2, 1), (1,)), ((2, 1), (2, 1))]:
    got, N, xs = star(lam, mu); pred = predicted(lam, mu, N, xs); bad = compare(got, pred)
    log(f's_{lam} * s_{mu} (N={N}): got={got}\n    pred={pred}  {"OK" if not bad else "MISMATCH "+str(bad)}')
