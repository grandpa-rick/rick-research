"""Task B/C: verify Psi_{3m} = (gamma + delta*sigma)^m (1) mod 3, and the
explicit word expansion, and the top-E3-degree coefficient."""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day146_prove')
from core import (build_Psi, pmul, padd, pscal, sigma, phi, ONE, E1, E2, E3,
                  const, ppow, E3deg)
from itertools import product as iproduct

def red3(P):
    return {m: c % 3 for m, c in P.items() if c % 3}

def eq(P, Q):
    return red3(P) == red3(Q)

# gamma = alpha*beta*E2, alpha = E2-E1+1, beta = E2+E1+1 ; delta = E1*E3
alpha = padd(E2, pscal(-1, E1), const(1))
beta  = padd(E2, E1, const(1))
gamma = pmul(pmul(alpha, beta), E2)
delta = pmul(E1, E3)

def op(x):                       # (gamma + delta*sigma)
    return red3(padd(pmul(gamma, x), pmul(delta, sigma(x))))

MMAX = 6
Psi = build_Psi(3*MMAX + 3)

print("=== check the mod-3 corollary recursion  Psi_{3m+3} = gamma Psi_3m + delta sigma(Psi_3m) ===")
cur = ONE
for m in range(MMAX+1):
    ok = eq(cur, Psi[3*m])
    print(f"  m={m:2d}  (gamma+delta sigma)^m(1) == Psi_{3*m} mod 3 ?  {ok}")
    if not ok:
        print("    LHS", red3(cur)); print("    RHS", red3(Psi[3*m]))
    cur = op(cur)

print()
print("=== also check Psi_{3m+1} = alpha Psi_3m,  Psi_{3m+2} = alpha beta Psi_3m mod 3 ===")
for m in range(MMAX+1):
    print(f"  m={m:2d}  +1:{eq(pmul(alpha,Psi[3*m]),Psi[3*m+1])}  "
          f"+2:{eq(pmul(pmul(alpha,beta),Psi[3*m]),Psi[3*m+2])}")

print()
print("=== closed-form WORD EXPANSION ===")
# term for r delta's with gaps g_0..g_r (sum = m-r):
#   prod_{l=0}^{r} sigma^l(gamma)^{g_l}  *  prod_{l=0}^{r-1} sigma^l(delta)
def sig_pow(P, l):
    for _ in range(l):
        P = red3(sigma(P))
    return red3(P)

SG = [sig_pow(gamma, l) for l in range(MMAX+2)]
SD = [sig_pow(delta, l) for l in range(MMAX+2)]

def compositions(n, parts):
    """all tuples of length `parts` of nonneg ints summing to n"""
    if parts == 1:
        yield (n,); return
    for first in range(n+1):
        for rest in compositions(n-first, parts-1):
            yield (first,) + rest

def word_formula(m):
    tot = {}
    for r in range(m+1):
        base = ONE
        for l in range(r):
            base = red3(pmul(base, SD[l]))
        for g in compositions(m-r, r+1):
            t = base
            for l in range(r+1):
                for _ in range(g[l]):
                    t = red3(pmul(t, SG[l]))
            tot = red3(padd(tot, t))
    return tot

for m in range(MMAX+1):
    print(f"  m={m:2d}  word formula == Psi_{3*m} mod 3 ?  {eq(word_formula(m), Psi[3*m])}")

print()
print("=== TASK C: top E3-degree coefficient of Psi_{3m} mod 3 ===")
def coeffE3(P, k):
    return {(a,b,0): c for (a,b,c), co in [] } # placeholder
def extract_E3(P, k):
    out = {}
    for (a,b,c), co in P.items():
        if c == k:
            out[(a,b,0)] = out.get((a,b,0),0) + co
    return red3(out)

def pstr(P):
    if not P: return "0"
    terms=[]
    for (a,b,c), co in sorted(P.items()):
        s=str(co)
        if a: s+=f"*E1^{a}"
        if b: s+=f"*E2^{b}"
        if c: s+=f"*E3^{c}"
        terms.append(s)
    return " + ".join(terms)

for m in range(MMAX+1):
    P = red3(Psi[3*m])
    d = E3deg(P)
    top = extract_E3(P, m)
    print(f"  m={m:2d}  deg_E3(Psi_{3*m} mod 3) = {d}  (bound {m});  [E3^{m}] = {pstr(top)}")
