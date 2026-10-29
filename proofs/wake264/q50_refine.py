"""Q50 refinements + transfer matrix + negative controls (Wake 264)."""
import sys, itertools
from collections import defaultdict, Counter
import sympy as sp
from q50_count import strict_parts, triples, steps, S_of, lam_of

q = sp.symbols('q')

# ---- transfer matrix on bond-flow states (f1,f2) in {00,10,01}; per-site trajectory (n0,n1,n2) ----
def site_matrix(qq=1):
    st = [(0,0),(1,0),(0,1)]
    M = sp.zeros(3,3)
    for n in itertools.product((0,1), repeat=3):
        d1, d2 = n[1]-n[0], n[2]-n[1]
        inn = (int(d1==1), int(d2==1)); out = (int(d1==-1), int(d2==-1))
        if inn in st and out in st:
            M[st.index(inn), st.index(out)] += qq**(out[0]+out[1])
    return M, st

def tm_count(m, left, qq=1):
    M, st = site_matrix(qq)
    u = sp.Matrix([[left.get(s, 0) * (qq**(s[0]+s[1])) for s in st]])
    e = sp.Matrix([1,0,0])
    return sp.expand((u * M**m * e)[0])

if __name__ == "__main__":
    M_, st = site_matrix()
    print("site transfer matrix (rows=in-flow, cols=out-flow, states (f1,f2)):", st)
    sp.pprint(M_)
    print("eigenvals:", M_.eigenvals(), " M*e00 =", list(M_*sp.Matrix([1,0,0])))
    LEFT = {(0,0):1,(1,0):1}   # injection only at step 1
    for m in range(1, 8):
        V = triples(m)
        print(f"\n=== m={m}: total {sum(V.values())}, TM {tm_count(m, LEFT)}")
        # by |kappa|-|rho|
        byd = Counter()
        for (k, r), v in V.items():
            byd[sum(k)-sum(r)] += v
        poly = sp.expand(sum(c*q**d for d, c in byd.items()))
        print("  by |k|-|r|:", dict(sorted(byd.items())), " GF factor:", sp.factor(poly),
              " TM q-version:", sp.factor(tm_count(m, LEFT, q)))
        print("  signed sum (q=-1):", poly.subs(q, -1))
        if m <= 5:
            byr = defaultdict(int); byk = defaultdict(int)
            for (k, r), v in V.items():
                byr[r] += v; byk[k] += v
            print("  by rho (sum_k V):", {r: byr[r] for r in strict_parts(m)})
            print("  by kappa (sum_r V):", {k: byk[k] for k in strict_parts(m)})
    # negative controls
    print("\n=== negative controls ===")
    for m in range(1, 8):
        a = sum(triples(m, True, True).values())
        b = sum(triples(m, False, False).values())
        c = sum(triples(m, False, True).values())
        # drop antichain in step 1: lambda = any shifted shape between rho and kappa ... (kappa/lambda antichain no-diag)
        print(f"m={m}: inj both={a} ({tm_count(m,{(0,0):1,(1,0):1,(0,1):1})}), inj none={b}, inj step2 only={c}, 3^m={3**m}")
