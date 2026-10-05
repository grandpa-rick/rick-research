import sys
sys.path.insert(0, '/home/agent/projects/scripts/day215')
from analyze import load, conj, parts, nstat, M01
def fmt(p):
    p = [int(x) for x in p]; terms = []
    for i, c in enumerate(p):
        if c == 0: continue
        m = '' if i == 0 else ('t' if i == 1 else f't^{i}')
        terms.append(str(c) if i == 0 else (m if c == 1 else f'{c}{m}'))
    return ' + '.join(terms)
N = int(sys.argv[1])
out = ['# Day 215: d_{λμ}(t) = [s^{n(μ)}] c_{λμ}(s,t), all μ ⊵ λ, n ≤ %d' % N, '',
       'Grade: COMPUTED (exact rational arithmetic; scripts/day215/d_table.py; n≤5 cross-checked against direct day214 engine at t=2, t=-2/7).', '',
       'Columns: λ, μ, d(t), d(1), M01 = #0-1 matrices rows λ cols μ\', deg d, n(μ\')−n(λ\').', '',
       'Observed formula (COMPUTED n≤%d): d_{λμ}(t) = t^{−n(λ\')} Σ_ν K_{ν\'λ} K̃_{ν μ\'}(t) = t^{−n(λ\')}⟨e_λ, H̃_{μ\'}(x;t)⟩,  K̃ = cocharge Kostka–Foulkes.' % N, '']
for n in range(1, N+1):
    try: D = load(n)
    except FileNotFoundError: break
    out += [f'## n = {n}', '', '| λ | μ | d(t) | d(1) | M01 | deg | n(μ\')−n(λ\') |', '|---|---|---|---|---|---|---|']
    for lam in parts(n):
        for mu in sorted(D[lam], key=nstat):
            p = D[lam][mu]
            out.append(f'| {lam} | {mu} | {fmt(p)} | {int(sum(p))} | {M01(list(lam), list(conj(mu)))} | {len(p)-1} | {nstat(conj(mu))-nstat(conj(lam))} |')
    out.append('')
open('/home/agent/projects/scripts/day215/d_table.md', 'w').write('\n'.join(out))
print('written')
