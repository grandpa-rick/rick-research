"""Lemma I test in general Coxeter W: x~_L z, nonempty L(z) subset int L(x) (all Coxeter-graph nbrs of L(z) in L(x)), L(z)!=L(x) => mu(x,z)=0?"""
import sys; sys.path.insert(0,'../wake279')
from coxkl import coxeter_group, kl, left_cells
def M_from(edges,n):
    M=[[2]*n for _ in range(n)]
    for i in range(n): M[i][i]=1
    for a,b,m in edges: M[a][b]=M[b][a]=m
    return M
types={
 'A5':(5,[(0,1,3),(1,2,3),(2,3,3),(3,4,3)]),
 'D4':(4,[(0,1,3),(1,2,3),(1,3,3)]),
 'D5':(5,[(0,1,3),(1,2,3),(2,3,3),(2,4,3)]),
 'B4':(4,[(0,1,4),(1,2,3),(2,3,3)]),
 'H3':(3,[(0,1,5),(1,2,3)]),
 'F4':(4,[(0,1,3),(1,2,4),(2,3,3)]),
}
t=sys.argv[1]; n,E=types[t]; M=M_from(E,n)
nb={i:set() for i in range(n)}
for a,b,m in E: nb[a].add(b); nb[b].add(a)
G=coxeter_group(M); P,mu=kl(G); cells,D=left_cells(G,mu)
L=G['length']; cfg=0; viol=[]; par=0
for C in cells:
    for x in C:
        Lx=D[x]
        I={s for s in Lx if nb[s]<=Lx}
        for z in C:
            Lz=D[z]
            if Lz and Lz<=I and Lz!=Lx:
                cfg+=1; g=abs(int(L[z])-int(L[x]))
                if g%2: par+=1
                if mu[x,z]: viol.append((x,z,sorted(Lx),sorted(Lz),int(L[x]),int(L[z]),int(mu[x,z])))
print(t,'N',G['N'],'cells',len(cells),'interior configs',cfg,'odd-gap',par,'violations',len(viol)); print(viol[:10])
