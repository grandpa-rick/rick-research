"""Parabolic heredity test for Q68 type-A dominated twins (Wake 284, 2026-11-08).
Inputs: census certificate files (candidate pairs + verdicts) for n=14,15,16.
Twins are tableau-level pairs (P_x,P_z) (Prop Q: verdict independent of Q).
L(w) = Des P(w), i in Des P iff i+1 lies in a strictly lower row than i.
Embedding (i): w -> w(1..n),n+1   (W_J, J={s_1..s_{n-1}}, omitted s_n, boundary s_{n-1})
Embedding (ii): w -> 1,w+1        (J={s_2..s_n}, omitted s_1, boundary s_2 = shifted s_1)
"""
import json, glob, itertools, collections, sys
D = '/home/agent/projects/proofs/'

def T(P): return tuple(tuple(r) for r in P)

def load(n):
    recs = {}
    pats = {14: ['wake282/certs14_*.json'], 15: ['prove281/certs15_*.json'],
            16: ['wake282/certs16_*.json']}[n]
    for p in pats:
        for f in sorted(glob.glob(D + p)):
            for r in json.load(open(f)):
                recs[(T(r['Px']), T(r['Pz']))] = r
    if n == 16:
        for r in json.load(open(D + 'prove283/certs16_6433_ext.json')):
            k = (T(r['Px']), T(r['Pz']))
            assert k in recs; recs[k] = r
        for k, r in recs.items():
            if r['verdict'] == 'UNDECIDED':
                assert tuple(r['lam']) == (5, 5, 3, 3), r['lam']
                r = dict(r); r['verdict'] = 'NO'; recs[k] = r   # prove282 verify_red: mu=0 => NO
    return recs

def rsk(w):
    P, Q = [], []
    for i, a in enumerate(w, 1):
        r = 0
        while True:
            if r == len(P): P.append([a]); Q.append([i]); break
            row = P[r]; j = next((j for j, b in enumerate(row) if b > a), None)
            if j is None: row.append(a); Q[r].append(i); break
            row[j], a = a, row[j]; r += 1
    return T(P), T(Q)

def des(P):
    pos = {v: r for r, row in enumerate(P) for v in row}
    return {i for i in range(1, len(pos)) if pos[i + 1] > pos[i]}

def emb1(w): return list(w) + [len(w) + 1]
def emb2(w): return [1] + [a + 1 for a in w]

def in_parabolic(P, k):
    """data (mu, nu) if (P,Q) in S_k x S_{N-k} for suitable Q, else None.
    x=u(+)v  <=>  row i of P = (row i of P(u)) ++ (row i of P(v)+k), large part a straight SYT."""
    small = [[a for a in row if a <= k] for row in P]
    large = [[a for a in row if a > k] for row in P]
    for row in P:  # small entries precede large ones automatically (rows increase)
        pass
    nu = [len(r) for r in large]
    if any(nu[i] < nu[i + 1] for i in range(len(nu) - 1)): return None
    for i in range(len(large) - 1):
        for j in range(len(large[i + 1])):
            if large[i][j] >= large[i + 1][j]: return None
    mu = tuple(len(r) for r in small)
    return (mu, tuple(nu))

def main():
    out = []
    pr = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))
    C = {n: load(n) for n in (14, 15, 16)}
    # convention check: A == Des Px, and x's RSK
    for n in C:
        for k, r in C[n].items():
            assert set(r['A']) == des(r['Px']), 'A != Des Px'
            assert rsk(r['x']) == (T(r['Px']), T(r['Q'])) and rsk(r['z']) == (T(r['Pz']), T(r['Q']))
            assert set(r['A']) >= des(r['Pz'])
    tw = {n: {k for k, r in C[n].items() if r['verdict'] == 'TWIN'} for n in C}
    pr('twin counts', {n: len(tw[n]) for n in tw}, 'candidate counts', {n: len(C[n]) for n in C})
    pr('\n## S_14 twins: L(x)=Des P_x, L(z)=Des P_z')
    for k in sorted(tw[14]):
        r = C[14][k]
        pr('lam', r['lam'], 'x', r['x'], 'z', r['z'], 'L(x)', sorted(des(k[0])), 'L(z)', sorted(des(k[1])))
    images = {16: set(), 15: set()}
    stats = collections.Counter(); conv_ce = []; conv_sup = []
    for n in (14, 15):
        for k in sorted(tw[n]):
            r = C[n][k]; Lx = des(k[0])
            for e, f, b in (('i', emb1, n - 1), ('ii', emb2, 1)):
                X, Z = f(r['x']), f(r['z'])
                (PX, QX), (PZ, QZ) = rsk(X), rsk(Z)
                assert QX == QZ
                assert des(PX) == ({i for i in Lx} if e == 'i' else {i + 1 for i in Lx})
                key = (PX, PZ); images[n + 1].add(key)
                cand = key in C[n + 1]
                v = C[n + 1][key]['verdict'] if cand else 'not-candidate'
                bd = b in Lx
                stats[(n, e, bd, v)] += 1
                row = (n, e, r['lam'], r['x'], r['z'], sorted(Lx), v)
                if bd and v == 'TWIN': pr('VIOLATION of boundary kill', row)
                if not bd:
                    (conv_sup if v == 'TWIN' else conv_ce).append(row)
    pr('\n## table: (n, embedding, boundary gen in L(x), verdict in S_{n+1}) : count')
    for kk in sorted(stats, key=str): pr(kk, stats[kk])
    pr('\nconverse supports', len(conv_sup), 'counterexamples', len(conv_ce))
    for row in conv_ce: pr('  CE', row)
    for row in conv_sup: pr('  SUP', row)
    pr('\n## S_{n+1} twins: embedded images vs parabolic membership')
    for N in (15, 16):
        n_img = len(tw[N] & images[N])
        pr(f'S_{N}: twins {len(tw[N])}, images of S_{N-1} twins {n_img}, images that are not twins {len(images[N]-tw[N])}')
        cnt = collections.Counter(); par_rows = []
        for key in sorted(tw[N]):
            ks = [k for k in range(1, N) if (a := in_parabolic(key[0], k)) is not None and a == in_parabolic(key[1], k)]
            maxpar = (N - 1 in ks) or (1 in ks)
            cnt[('maximal S_{N-1}' if maxpar else ('other proper parabolic' if ks else 'native (no proper std parabolic)'))] += 1
            if ks: par_rows.append((C[N][key]['lam'], ks, key in images[N]))
        pr(f'  S_{N} twins by parabolic membership: {dict(cnt)}')
        for row in par_rows: pr('   in parabolic: lam', row[0], 'k-splits', row[1], 'image of S_{N-1} twin', row[2])
    open(D + 'wake284/out_twin_heredity.txt', 'w').write('\n'.join(out) + '\n')

main()
