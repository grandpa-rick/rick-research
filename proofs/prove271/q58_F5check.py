# F5 sanity: C_m, lam = omega_m (LG). Claim: along ANY saturated chain sig->tau the number of bond-1 steps equals
# (#minus signs of tau.omega_m) - (#minus signs of sig.omega_m)  [= # diagonal boxes of the skew], all other bonds 2;
# hence A(sig,tau) <=> skew diagonal-free <=> sign count unchanged.
exec(open('q58_achain.py').read().split("if __name__")[0])
for m in [2,3,4,5]:
    lam=tuple([0]*(m-1)+[1]); S=setup('C',m,lam); L,ln,up,upb,N=S['L'],S['ln'],S['up'],S['upb'],S['N']
    eps=lambda mu:[sum(mu[i] for i in range(k,m)) for k in range(m)]
    neg_=lambda a: sum(1 for c in eps(L[a]) if c<0)
    bad=0; npairs=0; nA=0
    for x in range(N):
        H={x:{0}}  # set of bond-1 counts along chains
        for v in sorted([u for u in range(N) if (upb[x]>>u)&1],key=lambda u:ln[u]):
            for w,p in up[v]:
                assert p in (1,2)
                H.setdefault(w,set()).update(h+(p==1) for h in H[v])
        G=gcds(S,x)
        for y in H:
            if y==x: continue
            npairs+=1
            if H[y]!={neg_(y)-neg_(x)}: bad+=1
            if (max(G[y])>=2)!=(neg_(y)==neg_(x)): bad+=1
            nA+=max(G[y])>=2
    print(f'C{m} omega_{m}: |W^J|={N} pairs={npairs} A-true={nA} failures={bad}')
