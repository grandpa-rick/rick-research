# Named-pair checks for Q58 at E6 node 4: doubly-stuck pairs, Thm K explicit pairs, commuting-cube pairs.
exec(open('q58_achain.py').read().split("if __name__")[0])
import itertools
S,pr,P,conf=run('E',6,(0,0,0,1,0,0))
L,ix,ln,upb,C=S['L'],S['ix'],S['ln'],S['upb'],S['C']; le=lambda a,b:(upb[a]>>b)&1
lam=L[0]
def wt(word):  # Bourbaki labels 1..6, element s_{w0} s_{w1} ... applied to lam
    return ix[C.apply_word([i-1 for i in word],lam)]
G={}
def A(x,y):
    if x not in G: G[x]=gcds(S,x)
    return sorted(G[x][y])
dset={(x,y) for x,y,_ in pr if x!=y}
ds=[]
for x,y in dset:
    D=[i for i in range(6) if L[y][i]<0]
    if all(L[x][i]<0 for i in D) and all(le(x,ix[C.refl(i,L[y])]) for i in D): ds.append((x,y))
print('doubly-stuck (d)-pairs by gap:',collections.Counter(ln[y]-ln[x] for x,y in ds))
d3=[p for p in ds if ln[p[1]]-ln[p[0]]==3]
print('gap-3 doubly stuck:',len(d3),' P values:',collections.Counter(P[p] for p in d3),' gcd-sets:',collections.Counter(tuple(A(*p)) for p in d3))
for xw,yw in [((6,2,4,5,1,3,2,4),(4,5,6,3,2,4,5,1,3,2,4)),((3,2,4,5,4,1,3,2,4),(5,6,4,3,2,4,5,4,1,3,2,4))]:
    x,y=wt(xw),wt(yw); print('ThmK pair ln',ln[x],ln[y],'(d)?',(x,y) in dset,'P=',P.get((x,y)),'gcds',A(x,y))
# commuting cubes: tau = s_a s_b s_c sig, a,b,c pairwise commuting, each step up
A6=cartan('E',6); cub=collections.Counter(); cubP=collections.Counter()
for x in range(len(L)):
    for T in itertools.combinations(range(6),3):
        if any(A6[i][j] for i in T for j in T if i!=j): continue
        if all(L[x][i]>0 for i in T):
            mu=L[x]
            for i in T: mu=C.refl(i,mu)
            y=ix[mu]; assert ln[y]==ln[x]+3
            cub[((x,y) in dset, max(A(x,y))>=2)]+=1; cubP[P.get((x,y))]+=1
print('gap-3 commuting cubes: ((d),A) ->',dict(cub),' P:',dict(cubP))
# A-true pairs: which gcds
print('gcd values among A-true (d)-pairs:',collections.Counter(max(A(x,y)) for x,y in dset if max(A(x,y))>=2))
