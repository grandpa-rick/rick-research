"""The b_k-relevant diagonal sits at B = 3k-1, where Lemma B is SHARP (v_3 = 1).
Compute D_k := (1/3)[E3^k] Psi_{3k-1}  mod 3   and  compare to  -E1^{k-1}.
Also print [E3^k]Psi_{3k}, [E3^k]Psi_{3k+1} mod 3 for context."""
import sys
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_Psi, E3deg

def extract(P,k,div=1):
    out={}
    for (a,b,c),co in P.items():
        if c==k:
            assert co % div == 0, (a,b,c,co,div)
            out[(a,b)] = out.get((a,b),0) + co//div
    return {m:v%3 for m,v in out.items() if v%3}

def pstr(P):
    if not P: return "0"
    t=[]
    for (a,b),co in sorted(P.items()):
        s=str(co)
        if a: s+=f"*E1^{a}"
        if b: s+=f"*E2^{b}"
        t.append(s)
    return " + ".join(t)

KMAX=7
Psi=build_Psi(3*KMAX+3)
print("k :  v3 min of [E3^k]Psi_{3k-1} ;  (1/3)[E3^k]Psi_{3k-1} mod 3 ;   -E1^(k-1) mod 3")
for k in range(1,KMAX+1):
    B=3*k-1
    coeff={m:c for m,c in Psi[B].items() if m[2]==k}
    if not coeff:
        print(f"k={k}: ZERO"); continue
    def v3(n):
        v=0
        while n%3==0: n//=3; v+=1
        return v
    vmin=min(v3(c) for c in coeff.values())
    D=extract(Psi[B],k,3)
    tgt={(k-1,0): 2%3} if k>=1 else {}
    print(f"k={k}:  v3min={vmin}   D_k = {pstr(D)}    match(-E1^{k-1})? {D==tgt}")
