"""Day 216 kill test for 'Theorem H is folklore (transport of structure)'.
Step 1: commutativity [E_a,E_b] on arbitrary e_mu inputs (not just on 1), exact at rational (s,t), via point evaluation.
Also stability of E_k matrix in number of variables m (m = n+k vs n+k+1)."""
import sys, itertools, random, math
sys.path.insert(0, '/home/agent/projects/scripts/day214')
from ds_pointeval import parts, esym, solve, nstat
from fractions import Fraction as Fr
rng = random.Random(216)
def evalF(F, x):  # F: dict nu -> coeff (e-basis)
    return sum(c*math.prod(esym(p, x) for p in nu) for nu, c in F.items())
def Ek_pt(k, Ffun, x, s, t):
    m = len(x); tot = Fr(0)
    for A in itertools.combinations(range(m), k):
        As = set(A); w = Fr(1)
        for i in A:
            w *= x[i]
            for j in range(m):
                if j not in As: w *= (x[i]-t*x[j])/(x[i]-x[j])
        y = tuple(s*x[i] if i in As else x[i] for i in range(m))
        tot += w*Ffun(y)
    return tot
def to_e(fun, n, m):
    P = list(parts(n)); N = len(P)
    pts = [tuple(Fr(rng.randint(-10**5, 10**5), rng.randint(1, 10**3)) for _ in range(m)) for _ in range(N+1)]
    M = [[math.prod(esym(p, x) for p in nu) for nu in P] for x in pts[:N]]
    c = solve(M, [fun(x) for x in pts[:N]])
    x = pts[N]; assert sum(ci*math.prod(esym(p, x) for p in nu) for ci, nu in zip(c, P)) == fun(x), 'not in span (m too small?)'
    return {nu: ci for nu, ci in zip(P, c) if ci != 0}
def apply_E(ks, F, n, s, t, m):
    """apply E_{ks[-1]} first ... E_{ks[0]} last, to F of degree n, in m variables; return e-dict."""
    G = F; d = n
    for k in reversed(ks):
        Gc = G; G = to_e(lambda x, Gc=Gc, k=k: Ek_pt(k, lambda y: evalF(Gc, y), x, s, t), d+k, m); d += k
    return G
if __name__ == '__main__':
    NMAX = int(sys.argv[1]); S, T = Fr(3, 7), Fr(-5, 11); out = open(sys.argv[2], 'w')
    def log(*a):
        print(*a, flush=True); print(*a, file=out, flush=True)
    log('S,T =', S, T)
    # stability
    for n in range(0, 3):
        for k in range(1, 3):
            for mu in parts(n):
                F = {mu: Fr(1)}
                A1 = apply_E([k], F, n, S, T, n+k); A2 = apply_E([k], F, n, S, T, n+k+1)
                log('stability m=n+k vs n+k+1', k, mu, A1 == A2)
    nz = 0
    for n in range(0, NMAX):
        for a in range(1, NMAX):
            for b in range(a+1, NMAX):
                if n+a+b > NMAX: continue
                for mu in parts(n):
                    F = {mu: Fr(1)}; m = n+a+b
                    AB = apply_E([a, b], F, n, S, T, m); BA = apply_E([b, a], F, n, S, T, m)
                    diff = {nu: AB.get(nu, 0)-BA.get(nu, 0) for nu in set(AB) | set(BA)}
                    diff = {nu: v for nu, v in diff.items() if v != 0}
                    if diff: nz += 1
                    log(f'[E{a},E{b}] e{mu}: commute={not diff}', '' if not diff else {str(k): str(v) for k, v in list(diff.items())[:4]})
    log('noncommuting cases:', nz)
