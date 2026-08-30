import json
from sympy import mobius, divisors, Matrix, Rational, symbols
D=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
s=[int(x) for x in D["s"]]; h=[int(x) for x in D["h"]]; b=[int(x) for x in D["b"]]
N=len(s)-1
print("=== realizability (Dold / exactly-realizable): m_n = (1/n) sum_{d|n} mu(n/d)s_d must be a NONNEG INTEGER ===")
ok=True
for n in range(1,N+1):
    M=int(sum(int(mobius(n//d))*s[d] for d in divisors(n)))
    m=M//n
    good = (M%n==0 and m>=0); ok&=good
    print(f"  n={n:<3} m_n = {m:<22} {'ok' if good else '*** FAIL ***'}")
print("s_n is EXACTLY REALIZABLE on n<=%d: %s"%(N,ok))
print()
# ---- P-recursion search: sum_{i=0..r} p_i(n) u_{n+i} = 0, deg p_i <= d ----
def prec(seq, name, rmax=4, dmax=4, off=0):
    print("=== P-recursion search for %s (order<=%d, degree<=%d) ==="%(name,rmax,dmax))
    L=len(seq)
    found=[]
    for r in range(1,rmax+1):
        for d in range(0,dmax+1):
            nun=(r+1)*(d+1)
            rows=[]
            for n in range(0, L-r):
                rows.append([ (n+off)**e * seq[n+i] for i in range(r+1) for e in range(d+1)])
            if len(rows) < nun+1:   # need strictly more equations than unknowns
                continue
            A=Matrix(rows)
            ns=A.nullspace()
            if ns:
                found.append((r,d,len(rows),len(ns)))
                print("   HIT order=%d degree=%d  (%d eqns, %d unknowns, nullity %d)"%(r,d,len(rows),nun,len(ns)))
    if not found: print("   NONE (with strictly more equations than unknowns in every tested (r,d))")
    # report the largest (r,d) actually testable
    print()
prec(s[1:], "s_n (n>=1)", off=1)
prec(h, "h_j (j>=0)", off=0)
prec(b, "b_k (k>=1)", off=1)
