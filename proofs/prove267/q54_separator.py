# Q54 separator (computed only). Fresh re-implementation, no reuse of prove266 code.
# Shapes: strict partitions with parts in {1..m} (= subsets of {1..m}), Schubert classes of LG(m,2m).
# Shifted diagram: row i (0-idx) of part p occupies columns i..i+p-1.
# Pair (rho, lam): D(rho) subset of D(lam) (rho = lam allowed). Skew S = D(lam)\D(rho).
# Poset on cells: (i,j) <= (k,l) iff i<=k and j<=l. Antichain: no two distinct comparable cells.
import itertools, sys
from collections import Counter
def shapes(m):
    return [tuple(sorted(c, reverse=True)) for k in range(m+1) for c in itertools.combinations(range(1, m+1), k)]
def diag(k):
    return frozenset((i, j) for i, p in enumerate(k) for j in range(i, i+p))
def comparable(x, y):
    return (x[0] <= y[0] and x[1] <= y[1]) or (y[0] <= x[0] and y[1] <= x[1])
def is_antichain(S):
    return all(not comparable(x, y) for x, y in itertools.combinations(S, 2))
def is_chain(S):
    return all(comparable(x, y) for x, y in itertools.combinations(S, 2))
def words(m):
    return [w for w in itertools.product((0, 1, 2), repeat=m)
            if not any({w[i], w[i+1]} == {1, 2} for i in range(m-1))]
M = int(sys.argv[1]) if len(sys.argv) > 1 else 7
for m in range(1, M+1):
    sh = [(k, diag(k)) for k in shapes(m)]
    tot = anti = chain = nonempty_chain = 0
    dist_size = Counter()
    for (r, Dr), (l, Dl) in itertools.product(sh, sh):
        if not Dr <= Dl: continue
        S = Dl - Dr; tot += 1
        if is_antichain(S): anti += 1; dist_size[len(S)] += 1
        if is_chain(S): chain += 1; nonempty_chain += bool(S)
    W = words(m)
    nz = Counter(sum(x != 0 for x in w) for w in W)
    twos = Counter(w.count(2) for w in W)
    print(f"m={m}: all pairs {tot}, antichain {anti}, chain {chain} (nonempty {nonempty_chain}), words {len(W)}")
    print(f"   antichain by |S|: {dict(sorted(dist_size.items()))}")
    print(f"   words by #nonzero: {dict(sorted(nz.items()))}")
    print(f"   words by #2s     : {dict(sorted(twos.items()))}")

# Candidate word statistic matching the antichain-size distribution: number of maximal runs of 2s.
def runs2(w):
    return sum(1 for i in range(len(w)) if w[i] == 2 and (i == 0 or w[i-1] != 2))
print("check: antichain |S| distribution vs words by #maximal runs of 2s")
for m in range(1, M+1):
    sh = [(k, diag(k)) for k in shapes(m)]
    d = Counter(len(Dl-Dr) for (r, Dr), (l, Dl) in itertools.product(sh, sh) if Dr <= Dl and is_antichain(Dl-Dr))
    e = Counter(runs2(w) for w in words(m))
    print(f"m={m}: {dict(sorted(d.items()))} | {dict(sorted(e.items()))} | match={d==e}")
