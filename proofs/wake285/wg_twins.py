"""Exhaustive dominated-twin check (TW) on coxeter3 lcwgraphs output.
Twin: x!=z in cell, L(z) subset L(x), mu(y,z) >= mu(y,x) for all y in cell with L(y) not subset L(x).
Also reports candidate pairs (C2: L(z) nonempty, subset int L(x)) for the given simply-laced diagram."""
import re, sys
from collections import Counter
def parse(fn):
    cells = []; cur = None
    for line in open(fn):
        m = re.match(r"\s*(\d+)\s*:\s*(\d+):\{([\d,]*)\}:\{(.*)\}\s*$", line)
        if m:
            if int(m.group(2)) == 0: cur = []; cells.append(cur)
            D = frozenset(int(a) for a in m.group(3).split(',') if a)
            E = {int(a): int(b) for a, b in re.findall(r"\((\d+),(\d+)\)", m.group(4))}
            cur.append((D, E)); continue
        m = re.match(r"\s*(\d+):\{([\d,]*)\}:\{(.*)\}\s*$", line)
        if m:
            D = frozenset(int(a) for a in m.group(2).split(',') if a)
            E = {int(a): int(b) for a, b in re.findall(r"\((\d+),(\d+)\)", m.group(3))}
            assert int(m.group(1)) == len(cur); cur.append((D, E))
    return cells
def nbrs_of(typ, n):
    N = {i: set() for i in range(1, n+1)}
    E = [(1, 3), (2, 3)] + [(k, k+1) for k in range(3, n)] if typ == 'D' else [(k, k+1) for k in range(1, n)]
    for a, b in E: N[a].add(b); N[b].add(a)
    return N
def check(cells, N):
    twins = []; cand = 0; ncand_cells = 0; sym_bad = 0
    for ci, c in enumerate(cells):
        for i, (D, E) in enumerate(c):
            for j, m in E.items():
                if c[j][1].get(i) != m: sym_bad += 1
        hc = False
        for x, (Dx, Ex) in enumerate(c):
            intA = frozenset(s for s in Dx if N[s] <= Dx)
            for z, (Dz, Ez) in enumerate(c):
                if z == x or not Dz <= Dx: continue
                if Dz and Dz <= intA: cand += 1; hc = True
                ok = all(Ez.get(y, 0) >= Ex.get(y, 0) for y, (Dy, _) in enumerate(c)
                         if y not in (x, z) and not Dy <= Dx)
                # y = z itself: L(z) subset L(x), excluded automatically; y = x excluded
                if ok: twins.append((ci, x, z, sorted(Dx), sorted(Dz)))
        ncand_cells += hc
    return twins, cand, ncand_cells, sym_bad
if __name__ == '__main__':
    typ, n, fn = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    cells = parse(fn)
    print(fn, 'cells', len(cells), 'elements', sum(map(len, cells)))
    tw, cand, ncc, sb = check(cells, nbrs_of(typ, n))
    print('asymmetric mu entries', sb, '| candidate pairs', cand, 'in', ncc, 'cells | TWINS', len(tw))
    for t in tw[:10]: print('  twin', t)
