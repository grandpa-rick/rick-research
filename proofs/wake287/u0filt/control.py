"""Positive/negative controls for the search in u0filt.py, plus explicit identification of rho(U0)|_Y at (2,3)."""
import sympy as sp, u0filt, core
orig = core.U0_ops
def only(keys):
    def f(n, N):
        o = orig(n, N); return {k: v for k, v in o.items() if k in keys}
    return f
for keys in [('e0', 'k0', 'k1'), ('f0', 'k0', 'k1'), ('k0', 'k1')]:
    u0filt.U0_ops = only(keys)
    r = u0filt.run(2, 3, verbose=False)
    print('control gens', keys, '-> chains', r['chains_in_Y'])
u0filt.U0_ops = orig
# explicit: e0, f0 on Y vs the PROVE-287 maps f: u_{N-1} -> v_N, g: v_2 -> u_1
W, idx, d = core.setup(2, 3)
U = {k: u0filt.tosp(v) for k, v in orig(2, 3).items()}
def vec(w): v = sp.zeros(d, 1); v[idx[w]] = 1; return v
u = {p: vec(tuple(1 if q == p else 0 for q in range(3))) for p in range(3)}   # one letter 1 at position p
v = {p: vec(tuple(0 if q == p else 1 for q in range(3))) for p in range(3)}   # one letter 0 at position p
for name, g in [('f0', U['f0']), ('e0', U['e0'])]:
    for p in range(3):
        print(name, 'u_%d ->' % (p+1), [W[i] for i in range(d) if (g*u[p])[i]], [(g*u[p])[i] for i in range(d) if (g*u[p])[i]],
              ' v_%d ->' % (p+1), [W[i] for i in range(d) if (g*v[p])[i]], [(g*v[p])[i] for i in range(d) if (g*v[p])[i]])
