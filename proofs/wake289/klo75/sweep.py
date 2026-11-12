# Sweep: all basic skew shapes |lambda/mu|=n. Categories: conn / dr (contains disconnected ribbon) / hyp (Conj 7.5 hypothesis).
import sys, json, time
from klo import *
CS = {m: connected_shapes(m) for m in range(1, 10)}
nlo, nhi = int(sys.argv[1]), int(sys.argv[2]); DRCAP = int(sys.argv[3]) if len(sys.argv) > 3 else 400
primes = [32003, 30011]
out = open(f'out_sweep_{nlo}_{nhi}.jsonl', 'w')
def star_gen(comps):  # generalized composition alpha_proj, then [alpha] list
    a = [tuple(r - l + 1 for l, r in c) for c in comps]
    res = [a[0]]
    for b in a[1:]:
        new = []
        for x in res: new += [x + b, x[:-1] + (x[-1] + b[0],) + b[1:]]
        res = new
    return a, sorted(res)
for n in range(nlo, nhi + 1):
    stats = {}
    t0 = time.time()
    for comps in all_shapes(n, CS):
        rib = [is_ribbon(c) for c in comps]
        cat = 'conn' if len(comps) == 1 else ('dr' if any(rib[j] and rib[j+1] for j in range(len(comps)-1)) else 'hyp')
        cells = star(comps); B, act, s = build_module(cells); d = len(B)
        st = stats.setdefault(cat, {'n': 0, 'indec': 0, 'dec': 0, 'skipped': 0, 'brick': 0, 'topok': 0})
        if cat == 'dr' and d > DRCAP: st['skipped'] += 1; continue
        check_relations(act, n)
        rec = {'n': n, 'cat': cat, 'shape': lam_mu(cells), 'ncomp': len(comps), 'ribbons': rib, 'd': d}
        res = []
        for p in (primes if cat == 'hyp' else primes[:1]):
            E, F_of, _, _ = end_algebra(B, act, s, p, seed=p)
            nd, loc = local_test(E, F_of, p, seed=p)
            res.append((len(E), nd, loc))
        assert all(r == res[0] for r in res), ('prime disagreement', rec, res)
        rec['dimEnd'], rec['nsummands'], rec['local'] = res[0]
        tp = top(B, act)
        rec['top'] = {str(comp_of(set(range(1, n)) - set(S), n)): m for S, m in tp.items()}
        ap, pred = star_gen(comps)
        rec['alpha_proj'] = [list(x) for x in ap]
        rec['top_matches_LemmaA5.4'] = sorted(rec['top']) == sorted(str(x) for x in pred) and all(m == 1 for m in tp.values())
        st['n'] += 1; st['indec' if rec['local'] else 'dec'] += 1; st['brick'] += (rec['dimEnd'] == 1); st['topok'] += rec['top_matches_LemmaA5.4']
        out.write(json.dumps(rec) + '\n'); out.flush()
        if cat == 'hyp' and not rec['local']: print('COUNTEREXAMPLE', rec, flush=True)
    print(n, json.dumps(stats), f'{time.time()-t0:.0f}s', flush=True)
