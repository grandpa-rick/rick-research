import sys, fastA2, fastB
for a in sys.argv[1:]:
    n,N=map(int,a.split(','))
    dA,pA=fastA2.run(n,N); dB,pB=fastB.run(n,N)
    print('==',n,N,'dimA',dA,'dimB',dB,'defect',dB-dA)
    for D,b in pB.items():
        k=tuple(sorted(D)); x=pA.get(k,0)
        if b!=x: print('   D',k,'eA',x,'eB',b,'def',b-x)
    sys.stdout.flush()
