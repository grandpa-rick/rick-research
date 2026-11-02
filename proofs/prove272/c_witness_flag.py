# Flag-minor witness for Q60(c), type A_n.  g:[1..m]->distinct reals, theta(e_a-e_b)=g(a)-g(b), S={a<b: g(a)>g(b)}.
# b = Delta_{[1,p],J}|_N (flag minor, in every biperfect basis: BKK 1905.08460 Rem 2.10).
# Support of Delta(b): K with [1,p]<=K<=J (vanishing outside: zero-block); Phi: K* = argmin g(K).
# Check: (i) J = unique argmin over all p-subsets K<=J  => b in B_S
#        (ii) j+1 in J, j notin J  => eps_j(b)=1, e~_j b = Delta_{[1,p],J'}
#        (iii) competitor Kc <= J' with g(Kc)<g(J') and Delta_{Kc,J'}(n0)!=0 for explicit n0 (det computed)
import itertools
from fractions import Fraction
def det(M):
    M=[[Fraction(x) for x in r] for r in M]; d=Fraction(1); n=len(M)
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=0),None)
        if p is None: return 0
        if p!=c: M[c],M[p]=M[p],M[c]; d=-d
        d*=M[c][c]
        for r in range(c+1,n):
            f=M[r][c]/M[c][c]
            for k in range(c,n): M[r][k]-=f*M[c][k]
    return d
tot=ok=0
for m in range(3,8):
  for perm in itertools.permutations(range(m)):
    g={i+1:perm[i] for i in range(m)}
    for j in range(1,m):
      if g[j]<g[j+1]: continue
      F=[k for k in range(1,m+1) if k not in (j,j+1) and g[j+1]<g[k]<g[j]]
      if not F: continue
      tot+=1
      R=[k for k in F if k>j+1]
      if R:
        k=min(R); L=[r for r in range(j+2,k) if g[r]<g[j+1]]
        J=tuple(list(range(1,j))+[j+1]+L+[k]); Kc=tuple(list(range(1,j))+[j,j+1]+L); chain=[j+1]+L+[k]
      else:
        k=max(F); L=[r for r in range(k+1,j) if g[r]<g[j+1]]
        J=tuple(list(range(1,k))+L+[j+1]); Kc=tuple(list(range(1,k))+[k]+L); chain=[k]+L+[j]
      p=len(J); Jp=tuple(sorted([x for x in J if x!=j+1]+[j]))
      sub=[K for K in itertools.combinations(range(1,m+1),p) if all(a<=b for a,b in zip(K,J))]
      gs=lambda K:sum(g[x] for x in K)
      i_ok = min(sub,key=gs)==J and sorted(gs(K) for K in sub).count(gs(J))==1
      ii_ok = (j+1 in J) and (j not in J)
      n0=[[1 if a==b else 0 for b in range(m+1)] for a in range(m+1)]
      for a,b in zip(chain,chain[1:]): n0[a][b]=1
      dK=det([[n0[r][c] for c in Jp] for r in Kc])
      iii_ok = all(a<=b for a,b in zip(Kc,Jp)) and gs(Kc)<gs(Jp) and dK!=0
      ok+= i_ok and ii_ok and iii_ok
print("far (g,j) cases, n+1<=7:",tot," flag-minor witness valid:",ok)
