# Independent verification of the E6 node-4 counterexample.
import sys, functools, itertools
exec(open('q_cominuscule_scout.py').read().split('def boolean')[0])
def setup(t,n):
    C=Cox(cartan(t,n))
    @functools.lru_cache(None)
    def R(u,w):
        if w==C.rho: return (1,) if u==C.rho else ()
        s=next(i for i in range(C.n) if w[i]<0); sw=C.refl(s,w); su=C.refl(s,u)
        if u[s]<0: return R(su,sw)
        return padd(pmul((-1,1),R(u,sw)), psc(R(su,sw),1))
    def below(word):  # all elements <= product(word) via subwords
        S=set()
        for mask in range(1<<len(word)):
            S.add(C.apply_word([word[i] for i in range(len(word)) if mask>>i&1],C.rho))
        return S
    def KL(xw,yw):
        x=C.apply_word(xw,C.rho); y=C.apply_word(yw,C.rho)
        assert C.length(x)==len(xw) and C.length(y)==len(yw)
        iv=[z for z in below(yw) if C.le(x,z)]
        iv.sort(key=C.length,reverse=True); P={}
        for z in iv:
            if z==y: P[z]=(1,); continue
            F=()
            for w in iv:
                if w!=z and C.le(z,w): F=padd(F,pmul(R(z,w),P[w]))
            d=C.length(y)-C.length(z); p=[-c for c in F[:(d-1)//2+1]]
            while p and p[-1]==0: p.pop()
            P[z]=tuple(p)
        return P[x], iv, C
    return KL
KLA=setup('A',3); print('A3 control P_{s2,s2s1s3s2} =',KLA([1],[1,0,2,1])[0], '(expect (1,1))')
print('A3 hexagon P_{s1,s2s3s2s1} =',KLA([0],[1,2,1,0])[0])
KL=setup('E',6)
J=[0,1,2,4,5]
for xw,yw in [([5,1,3,4,0,2,1,3],[3,4,5,2,1,3,4,0,2,1,3]),([2,1,3,4,3,0,2,1,3],[4,5,3,2,1,3,4,3,0,2,1,3])]:
    P,iv,C=KL(xw,yw)
    y=C.apply_word(yw,C.rho)
    rd=lambda z: [j for j in range(6) if C.le(C.apply_word([],C.rho),C.rho) and C.length(z)>0 and any(True for _ in [0]) and False]
    # right descents of z: z s_j < z  <=> length drops; compute via word of z
    def zword(z):
        w=[]
        while z!=C.rho:
            i=next(k for k in range(6) if z[k]<0); w.append(i); z=C.refl(i,z)
        return w
    rdes=[sorted(j for j in range(6) if C.length(C.apply_word(zword(z)+[j],C.rho))<C.length(z)) for z in iv]
    inWJ=all(set(r)<=set([3]) for r in rdes)
    ranks=[sum(1 for z in iv if C.length(z)==len(xw)+i) for i in range(len(yw)-len(xw)+1)]
    print('E6 x=',xw,'y=',yw,'|[x,y]_W| (subwords)=',len(iv),'ranks',ranks,'all in W^J:',inWJ,'P_{x,y}=',P)
