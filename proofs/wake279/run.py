import numpy as np, sys, time
from coxkl import *
from cones import *

def Amat(n): return [[1 if i == j else (3 if abs(i - j) == 1 else 2) for j in range(n)] for i in range(n)]
CASES = {
    'A3': Amat(3),
    'I2(4)': [[1, 4], [4, 1]], 'I2(5)': [[1, 5], [5, 1]], 'I2(6)': [[1, 6], [6, 1]], 'I2(8)': [[1, 8], [8, 1]],
    'B3': [[1, 4, 2], [4, 1, 3], [2, 3, 1]],
    'H3': [[1, 5, 2], [5, 1, 3], [2, 3, 1]],
    'D4': [[1, 3, 2, 2], [3, 1, 3, 3], [2, 3, 1, 2], [2, 3, 2, 1]],
    'A4': Amat(4),
}
names = sys.argv[1].split(',')
LA = int(sys.argv[2]) if len(sys.argv) > 2 else 6
LB = int(sys.argv[3]) if len(sys.argv) > 3 else 6
maxdim = int(sys.argv[4]) if len(sys.argv) > 4 else 99
conv = sys.argv[5] if len(sys.argv) > 5 else 'Cp'
rng = np.random.default_rng(1)
for name in names:
    G = coxeter_group(CASES[name]); P, mu = kl(G); cells, D = left_cells(G, mu)
    catalog = []
    print(f'=== {name} conv={conv} |W|={G["N"]} cells={len(cells)}')
    for c in sorted(cells, key=lambda c: (len(c), min(G["length"][w] for w in c))):
        rep = min(c, key=lambda w: G['length'][w])
        rw = ''.join(str(s + 1) for s in G['word'][rep]) or 'e'
        A = cell_module(G, mu, D, c, conv); d = len(c)
        inv = min(a.min() for a in A) >= 0
        if all(np.allclose(a, 0) for a in A): print(f'{rw:>10} d={d} all 1+s = 0 (degenerate)'); continue
        chi, norm, dc, pieces, comm = decompose(G, A, rng)
        labs = []
        for ch in pieces:
            for k, c2 in enumerate(catalog):
                if np.allclose(c2, ch, atol=1e-5): break
            else:
                catalog.append(ch); k = len(catalog) - 1
            labs.append(f'{int(round(ch[0]))}_{k}')
        diag_comm = all(np.allclose(m, np.diag(np.diag(m)), atol=1e-8) for m in comm)
        lam, mult = perron_F(A)
        if d > maxdim:
            print(f'{rw:>10} d={d} irr={"+".join(sorted(labs))} <chi,chi>={norm} perronF^T mult={mult} inv={inv} SKIP'); continue
        t = time.time()
        reached, npf, S = testA(A, L=LA)
        resA = f'{len(reached)}/{d}'
        if d <= 12:
            surv = testB(A, eps=0.05, L=LB)
            resB = 'all pairs collapse' if not surv else f'{len(surv)} survivors e.g. {surv[:3]}'
        else:
            resB = 'skipped'
        print(f'{rw:>10} d={d} irr={"+".join(sorted(labs))} <chi,chi>={norm} commKLdiag={diag_comm} '
              f'perronF^T mult={mult} inv={inv} A:{resA} (unreached {[i for i in range(d) if i not in reached]}) B:{resB} [{time.time()-t:.1f}s]',
              flush=True)
    dims = [int(round(c[0])) for c in catalog]
    print(f'irreps seen: {len(catalog)} dims {dims} sum d^2={sum(x*x for x in dims)}')
