"""Day 211: DS at length 3 end-to-end via e_lam = e_{l3} * (e_{l1} * e_{l2}) [207b inner, (TC) outer, k = l3 = smallest part].
Checks: support in dominance up-set of lam; lead = s^{n(lam)}; off-diagonal vanish at s=1; support == FULL up-set (meta, not part of DS);
and the (MM) property used in the proof: every intermediate e_{l3}*(e_x e_y) term has max part >= x and min (3-padded) part <= l3."""
import sys; sys.path.insert(0, '/home/agent/projects/scripts/day210')
import sympy as sp, time, pickle
from multiprocessing import Pool
from tc_extract import coeffs, ek_er, s, t
from ds3 import dominates, nstat, parts3
def pad3(mu): return list(mu) + [0]*(3-len(mu))
def up3(lam):
    n = sum(lam); P = []
    def rec(r, mx, cur):
        if r == 0: P.append(tuple(cur)); return
        for p in range(min(r, mx), 0, -1): rec(r-p, p, cur+[p])
    rec(n, n, []); return [p for p in P if dominates(p, lam)]
def job(lam):
    t0 = time.time(); l1, l2, l3 = lam
    inner = ek_er(l2, l1); out = {}; MM = True
    for mu, c in inner.items():
        x, y = (pad3(mu)[0], pad3(mu)[1])
        G = ek_er(l3, x) if y == 0 else coeffs(l3, x, y)
        for nu, d in G.items():
            if not (max(nu) >= x and min(pad3(nu)) <= l3): MM = False
            out[nu] = out.get(nu, 0) + c*d
    out = {m: sp.factor(v) for m, v in out.items() if sp.cancel(v) != 0}
    supp = all(dominates(m, lam) for m in out)
    lead = sp.cancel(out.get(lam, 0) - s**nstat(lam)) == 0
    q1 = all(sp.cancel(v.subs(s, 1)) == 0 for m, v in out.items() if m != lam)
    full = set(out) == set(up3(lam))
    return lam, supp, lead, q1, full, MM, len(out), time.time()-t0, out
if __name__ == '__main__':
    NMAX = int(sys.argv[1]); lams = [l for n in range(3, NMAX+1) for l in parts3(n)]
    ok = True; store = {}
    with Pool(4) as P:
        for lam, supp, lead, q1, full, MM, ns, dt, out in P.imap(job, lams):
            store[lam] = out; ok &= supp and lead and q1 and MM
            print(lam, 'supp⊆up-set:', supp, ' lead=s^n(λ):', lead, ' offdiag|s=1=0:', q1, ' (MM):', MM, ' supp==full up-set:', full, f'#supp {ns} ({dt:.0f}s)', flush=True)
    pickle.dump(store, open(f'ds3_full_N{NMAX}.pkl', 'wb'))
    print('ALL DS OK' if ok else 'FAILURES')
