import json,sys
from sympy import mobius, divisors, primefactors, factorint
D=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
s=[int(x) for x in D["s"]]; N=len(s)-1
h=[int(x) for x in D["h"]]; b=[int(x) for x in D["b"]]
def v(p,n):
    c=0
    while n and n%p==0: n//=p;c+=1
    return c
print("=== Necklace / Gauss test:  M_n = sum_{d|n} mu(n/d) s_d ,  need M_n = 0 mod n ===")
print(f"{'n':>3} {'M_n':>26} {'M_n mod n':>12}  ok")
allok=True
for n in range(1,N+1):
    M=int(sum(int(mobius(n//d))*s[d] for d in divisors(n)))
    r=M%n; ok = (r==0); allok&=ok
    print(f"{n:>3} {M:>26} {r:>12}  {'YES' if ok else '*** NO ***'}")
print("ALL Gauss congruences hold (all primes, n<=%d): %s"%(N,allok))
print()
print("=== prime-by-prime:  s_n = s_{n/p} mod p^{v_p(n)} ===")
for p in [2,3,5,7,11]:
    print(" p=%d:"%p)
    for n in range(1,N+1):
        e=v(p,n)
        if e==0: continue
        d=s[n]-s[n//p]; m=p**e
        print("   n=%-3d v_p(n)=%d   (s_n - s_{n/p}) mod %d^%d = %-6d  %s"%(n,e,p,e,d%m,"OK" if d%m==0 else "FAIL"))
print()
print("=== extra: exact 3-adic valuations ===")
print("v3(s_n):", [v(3,x) for x in s[1:]])
print("v3(h_j):", [v(3,x) for x in h])
print("v3(b_k):", [v(3,x) for x in b])
print()
print("=== stronger: v_p(s_n - s_{n/p}) vs v_p(n)  (Gauss is >=; how much slack?) ===")
for p in [2,3,5,7]:
    row=[]
    for n in range(1,N+1):
        e=v(p,n)
        if e==0: continue
        d=s[n]-s[n//p]
        row.append((n,e,v(p,d) if d else 'inf'))
    print(" p=%d: (n, v_p(n), v_p(s_n-s_{n/p})) -> %s"%(p,row))
