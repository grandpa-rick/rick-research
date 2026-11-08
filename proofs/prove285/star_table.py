"""(*) check for every constructible character of D_n, n<=8 (= every left-cell character type)."""
from dchar import *
from itertools import combinations
import sys

def nbrs(n):
    N = {i: set() for i in range(1, n+1)}
    def e(a, b): N[a].add(b); N[b].add(a)
    for i in range(1, n-1): e(i, i+1)
    e(n-2, n)
    return N

def dist(n, v, subsets):
    f = {J: sum(a*b for a, b in zip(v, fvec(n, J))) for J in subsets}
    g = {}
    for A in subsets:
        t = sum((-1)**(len(K)-len(A)) * f[K] for K in subsets if A <= K)
        assert t >= 0, ('negative', n, v, A, t)
        if t: g[A] = t
    return g

def label(n, v):
    G = D(n)
    def p(x): return ''.join(map(str, x)) or '-'
    return '+'.join(f"{c if c>1 else ''}[{p(G.irr[i][0])}.{p(G.irr[i][1])}{'+-'[G.irr[i][2]<0] if G.irr[i][2] else ''}]" for i, c in enumerate(v) if c)

def main():
  out = []
  for n in range(4, int(sys.argv[1])+1):
      G = D(n); Nb = nbrs(n)
      subsets = [frozenset(J) for k in range(n+1) for J in combinations(range(1, n+1), k)]
      deg = [r[G.classes.index(((1,)*n, (), 0))] for r in G.table]
      viol = []
      for v in sorted(Con(n)):
          g = dist(n, v, subsets)
          dim = sum(a*b for a, b in zip(v, deg)); assert sum(g.values()) == dim
          occ = list(g)
          cand = []
          for A in occ:
              intA = frozenset(s for s in A if Nb[s] <= A)
              for B in occ:
                  if B and B <= intA and (B != A or g[A] >= 2): cand.append((sorted(A), sorted(B)))
          if cand: viol.append((label(n, v), dim, cand))
      line = f"D{n}: {len(Con(n))} constructible chars, (*)-violators: {len(viol)}"
      print(line, flush=True); out.append(line)
      for lab, dim, cand in viol:
          s = f"   {lab} dim={dim} #cand={len(cand)} e.g. {cand[:3]}"; print(s); out.append(s)
  open('out_star_table.txt', 'w').write('\n'.join(out) + '\n')

if __name__=='__main__': main()
