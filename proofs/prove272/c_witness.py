# Type A_n, g: [1..n+1] -> distinct reals (theta(e_a - e_b) = g(a)-g(b)).  S={a<b: g(a)>g(b)}.
# Phi(Delta_{I,J}) = (Delta_{I,K*}, Delta_{K*,J}), K* = argmin_{I<=K<=J} sum g(K). b in B_S iff K*=J.
# e_j Delta_{I,J} = Delta_{I,J-(j+1)+j} if j+1 in J, j notin J.
# Claim: far (exists k notin{j,j+1}, g(j+1)<g(k)<g(j)) => witness below lies in B_S, eps_j=1, e~ b notin B_S.
import itertools
def between(I,J,m):
    for K in itertools.combinations(range(1,m+1),len(I)):
        if all(i<=k<=jj for i,k,jj in zip(I,K,J)): yield K
def argmin(I,J,g,m):
    vals=sorted((sum(g[k] for k in K),K) for K in between(I,J,m))
    assert len(vals)==1 or vals[0][0]<vals[1][0]
    return vals[0][1]
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
        I=tuple(sorted([j,j+1]+L)); J=tuple(sorted([j+1]+L+[k]))
      else:
        k=max(F); L=[r for r in range(k+1,j) if g[r]<g[j+1]]
        I=tuple(sorted([k]+L)); J=tuple(sorted(L+[j+1]))
      Jp=tuple(sorted([x for x in J if x!=j+1]+[j]))
      good = (j+1 in J and j not in J and all(a<=b for a,b in zip(I,Jp))
              and argmin(I,J,g,m)==J and argmin(I,Jp,g,m)!=Jp)
      ok+=good
print("far (g,j) cases n+1<=7:",tot,"witness valid:",ok)
