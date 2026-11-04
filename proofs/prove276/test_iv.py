from q66 import *
tot=0;bad=0;badsw=0;cases=0;pairs=0
for n in (2,3,4):
    lams=[l for N in range(0,4) for l in partitions(N,n)]
    Bs={l:word_crystal_component(hw_word(l),n) for l in lams}
    for l1 in lams:
        for l2 in lams:
            B,Bp=Bs[l1],Bs[l2]
            # sanity: abstract tensor = concatenation word crystal
            T=tensor(B,Bp)
            for (x,y) in T.els:
                for i in range(1,n):
                    for op,D in (('e',T.e),('f',T.f)):
                        r=kash(x+y,i,op); s=D[(x,y),i]
                        assert (r is None and s is None) or (s is not None and s[0]+s[1]==r)
            A=quasify(T); Bq=qtensor(quasify(B),quasify(Bp)); Bs_=qtensor(quasify(B),quasify(Bp),swap=True)
            cases+=1; pairs+=len(T.els); bad+=same(A,Bq); badsw+=same(A,Bs_)
print("polynomial: tensor pairs",cases,"elements",pairs,"failures Q(BxB')=QB(x)''QB'",bad,"| swapped-kill control failures",badsw)
# non-polynomial: shift by det^c
res=Counter();first={}
for n in (2,3):
    lams=[l for N in range(0,3) for l in partitions(N,n)]
    for l1 in lams:
      for l2 in lams:
        for c1 in (-2,-1,0,1):
          for c2 in (-2,-1,0,1):
            B=shift(word_crystal_component(hw_word(l1),n),c1); Bp=shift(word_crystal_component(hw_word(l2),n),c2)
            b=same(quasify(tensor(B,Bp)),qtensor(quasify(B),quasify(Bp)))
            key=(n,min(c1,0)<0 or min(c2,0)<0)
            res[key,b>0]+=1
            if b and (n,l1,l2) not in first and len(first)<6: first[(n,l1,l2)]=(c1,c2,b)
print("shifted (key=(n, some factor non-polynomial), fails?) ->",dict(res))
print("sample failures:",first)
# minimal edge counterexample gl2: B(0,-1) (x) B(2,1)
B=shift(word_crystal_component((2,),2),-1)  # B(1,0)-1 = weights (0,-1),(-1,0) = B(0,-1)
Bp=shift(word_crystal_component((2,),2),1)  # B(2,1)
A=quasify(tensor(B,Bp));Q=qtensor(quasify(B),quasify(Bp))
for x in A.els:
    print(x,"wt",A.wt[x],"Q(BxB'): e,eps",A.e[x,1],A.eps[x,1]," QB(x)''QB': e,eps",Q.e[x,1],Q.eps[x,1])
