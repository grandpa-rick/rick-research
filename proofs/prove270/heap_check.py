# PROVE 270 check: Boolean Bruhat intervals in minuscule W^J <-> heap antichains of w0^J, labels multiply to y x^{-1}
import itertools, sys
def cartan(t,n):
    A=[[0]*n for _ in range(n)]
    for i in range(n): A[i][i]=2
    def e(i,j,a=-1,b=-1): A[i][j]=a; A[j][i]=b
    if t=='A':
        for i in range(n-1): e(i,i+1)
    if t=='B':  # alpha_n short: <a_{n-1}^v,a_n>=-1? use A[i][j]=<a_i^v,a_j>
        for i in range(n-2): e(i,i+1)
        A[n-2][n-1]=-1; A[n-1][n-2]=-2
    if t=='C':
        for i in range(n-2): e(i,i+1)
        A[n-2][n-1]=-2; A[n-1][n-2]=-1
    if t=='D':
        for i in range(n-2): e(i,i+1)
        e(n-3,n-1)
    if t=='E':  # Bourbaki: 1-3-4-5-6(-7-8), 2-4
        for i,j in [(0,2),(2,3),(3,4),(1,3)]+[(k,k+1) for k in range(4,n-1)]: e(i,j)
    return A
def refl(A,i,mu):
    n=len(A); m=mu[i]
    return tuple(mu[j]-m*A[i][j] for j in range(n))  # alpha_i = sum_j A[i][j] w_j
def run(t,n,lam_node,J_override=None,label=''):
    A=cartan(t,n); lam=tuple(1 if j==lam_node else 0 for j in range(n)) if isinstance(lam_node,int) else tuple(lam_node)
    # orbit BFS from lam (going up in length: apply s_i when <a_i^v,mu> >0)
    word={lam:()}; frontier=[lam]
    while frontier:
        nf=[]
        for mu in frontier:
            for i in range(n):
                if mu[i]>0:
                    nu=refl(A,i,mu)
                    if nu not in word: word[nu]=(i,)+word[mu]; nf.append(nu)
        frontier=nf
    els=list(word); L={m:len(word[m]) for m in els}
    def act(w,mu):
        for i in reversed(w): mu=refl(A,i,mu)
        return mu
    # Bruhat via subword property
    below={}
    for y in els:
        w=word[y]; S=set()
        for mask in range(1<<len(w)):
            S.add(act(tuple(w[k] for k in range(len(w)) if mask>>k&1),lam))
        below[y]=S
    le=lambda x,y: x in below[y]
    # heap of w0^J
    top=max(els,key=lambda m:L[m]); s=word[top]; l=len(s)
    comm=lambda a,b: A[a][b]==0 and a!=b
    rel=set((i,j) for i in range(l) for j in range(i+1,l) if not comm(s[i],s[j]))
    # transitive closure
    less=[[False]*l for _ in range(l)]
    for (i,j) in rel: less[i][j]=True
    for k in range(l):
        for i in range(l):
            if less[i][k]:
                for j in range(l):
                    if less[k][j]: less[i][j]=True
    # filters of P (up-closed)
    filters=[]
    def isfilter(F): return all(j in F for i in F for j in range(l) if less[i][j])
    # enumerate filters by BFS adding minimal-of-complement maximal elements
    seen={frozenset()}; fr=[frozenset()]
    while fr:
        nf=[]
        for F in fr:
            for i in range(l):
                if i not in F and all(j in F for j in range(l) if less[i][j]):
                    G=F|{i}
                    if G not in seen: seen.add(G); nf.append(G)
        fr=nf
    filters=list(seen)
    def elt(F):  # word = labels of F in increasing position order (a linear extension of F), product applied to lam
        return act(tuple(s[i] for i in sorted(F)),lam)
    Fof={}
    for F in filters:
        e=elt(F); Fof.setdefault(e,[]).append(F)
    bij = len(filters)==len(els) and all(len(v)==1 for v in Fof.values()) and set(Fof)==set(els) and all(len(list(Fof[e])[0])==L[e] for e in els)
    Fof={e:v[0] for e,v in Fof.items()}
    # weak order check: Bruhat == filter inclusion
    weak_eq = all(le(x,y)==(Fof[x]<=Fof[y]) for x in els for y in els) if bij else False
    nb=0; bad=0; nc=0
    for x in els:
        for y in els:
            if not le(x,y): continue
            I=[z for z in els if le(x,z) and le(z,y)]; r=L[y]-L[x]
            atoms=[z for z in I if L[z]==L[x]+1]
            sig={z:frozenset(a for a in atoms if le(a,z)) for z in I}
            boolean = len(atoms)==r and len(set(sig.values()))==len(I)==2**r and all(le(z,w)==(sig[z]<=sig[w]) for z in I for w in I)
            # (c) by direct search: distinct commuting letters u with u x = y, lengths adding
            cfound=False
            for k in [r]:
                for U in itertools.combinations(range(n),k):
                    if all(comm(a,b) for a,b in itertools.combinations(U,2)) and act(U,x)==y: cfound=True
            if boolean!=cfound: bad+=1
            if boolean:
                nb+=1
                if bij:
                    Q=Fof[y]-Fof[x]; labs=[s[i] for i in Q]
                    anti=all(not less[i][j] and not less[j][i] for i in Q for j in Q if i!=j)
                    ok=anti and len(set(labs))==len(labs) and all(comm(a,b) for a,b in itertools.combinations(labs,2)) and act(tuple(labs),x)==y
                    if not ok: bad+=1
    print(f"{label} {t}{n} lam={lam}: |W^J|={len(els)} filters={len(filters)} bij={bij} Bruhat==weak={weak_eq} Boolean pairs={nb} failures={bad}")
for args in [('E',6,0),('E',6,5),('D',5,4),('D',5,0),('D',6,5),('B',4,3),('B',3,2),('A',5,2),('A',4,1),('C',4,0)]:
    run(*args)
# negative control: A3, J={s2}  (lam = w2 is minuscule in A3! use non-minuscule: B3 node1 (J={s2,s3}, adjoint-ish), C3 node2, A3 J={s1,s3}? )
for args in [('A',3,(1,0,1)),('B',3,0),('C',3,1),('A',4,(0,1,1,0))]:
    run(*args,label='CONTROL')
