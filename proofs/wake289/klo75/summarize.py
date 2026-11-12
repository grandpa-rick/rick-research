import json, sys, glob
from collections import Counter, defaultdict
for f in sorted(glob.glob('out_n*.jsonl'), key=lambda x: int(x[5:-6])):
    L = [json.loads(l) for l in open(f)]; n = int(f[5:-6])
    tab = defaultdict(lambda: [0, 0, 0, 0])  # total, computed, indecomposable, skipped
    for r in L:
        t = tab[r['lab']]; t[0] += 1
        if r.get('skipped'): t[3] += 1; continue
        t[1] += 1; t[2] += (r['dimEndJ'] == 1)
    print(n, {k: tuple(v) for k, v in sorted(tab.items())})
    cj = [r for r in L if r['lab'] == 'CONJ']
    if cj:
        print('   CONJ dimEnd', sorted(Counter(r['dimEnd'] for r in cj).items()), ' dimEnd/J', Counter(r['dimEndJ'] for r in cj),
              ' topdim', sorted(Counter(sum(r['top'].values()) for r in cj).items()), ' srcW', Counter(r['srcW'] for r in cj))
    bad = [r for r in L if not r.get('skipped') and ((r['lab'] != 'RIBBON-PAIR') != (r['dimEndJ'] == 1))]
    for r in bad: print('   VIOLATION', r)
