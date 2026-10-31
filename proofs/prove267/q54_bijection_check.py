# Pointwise check of the Q54 proof's lemmas + explicit bijection Phi (computed-level evidence for the written proof).
import itertools
def shapes(m): return [tuple(sorted(c,reverse=True)) for k in range(m+1) for c in itertools.combinations(range(1,m+1),k)]
def diag(k): return frozenset((i,j) for i,p in enumerate(k) for j in range(i,i+p))
def le(x,y): return x[0]<=y[0] and x[1]<=y[1]
def anti(S): return all(not(le(x,y) or le(y,x)) for x,y in itertools.combinations(S,2))
def maxl(D): return frozenset(s for s in D if not any(s!=t and le(s,t) for t in D))
def runs1(x): return sum(1 for i in range(len(x)) if x[i]==1 and (i==0 or x[i-1]==0))
def word(m,lam,S):
    # Phi: indicator word of lam; the run of consecutive parts whose bottom part k has its corner in S -> colour 2
    x=[1 if k in lam else 0 for k in range(1,m+1)]
    rows={p:i for i,p in enumerate(lam)}
    for k in range(1,m+1):
        if x[k-1] and (k==1 or not x[k-2]):           # k = bottom of a run (k-1 not a part)
            i=rows[k]; c=(i,i+k-1)                      # corner cell of row with part k
            if c in S:
                j=k
                while j<=m and x[j-1]: x[j-1]=2; j+=1
    return tuple(x)
def W(m): return {w for w in itertools.product((0,1,2),repeat=m) if not any({w[i],w[i+1]}=={1,2} for i in range(m-1))}
def r2(w): return sum(1 for i in range(len(w)) if w[i]==2 and (i==0 or w[i-1]!=2))
for m in range(1,9):
    sh=[(k,diag(k)) for k in shapes(m)]; Ds={d for _,d in sh}
    img=[]; ok=True
    for l,Dl in sh:
        mx=maxl(Dl)
        ok &= len(mx)==runs1([1 if k in l else 0 for k in range(1,m+1)])          # Lemma 2
        ok &= mx=={(i,i+p-1) for i,p in enumerate(l) if p-1 not in l}             # Lemma 2 explicit corners
        for r,Dr in sh:
            if Dr<=Dl and anti(Dl-Dr):
                S=Dl-Dr; ok &= S<=mx                                             # Lemma 1 (=>)
                w=word(m,l,S); img.append(w); ok &= (w in W(m)) and r2(w)==len(S)
        for k in range(len(mx)+1):                                               # Lemma 1 (<=)
            for S in itertools.combinations(mx,k): ok &= (Dl-frozenset(S)) in Ds
    print(m, ok, len(img), len(set(img))==len(img)==len(W(m)) and set(img)==W(m))
