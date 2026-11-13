import sys, itertools
from split import act_pi, act_pibar
def parse(s): return tuple(int(c) for c in s)
def run(N,src,tgt,maxlen):
    tgt={parse(t):c for t,c in tgt}; neg={k:-c for k,c in tgt.items()}
    start={parse(src):1}
    ops=[(b,i) for i in range(1,N) for b in (0,1)]
    fr=[((),start)]; seen=set()
    for L in range(maxlen):
        nf=[]
        for w,v in fr:
            for b,i in ops:
                u=(act_pibar if b else act_pi)(v,i)
                if not u: continue
                key=tuple(sorted(u.items()))
                if key in seen: continue
                seen.add(key); w2=w+(('pb' if b else 'p')+str(i),)
                if u==tgt or u==neg: print('FOUND',w2,'sign',1 if u==tgt else -1); return w2
                nf.append((w2,u))
        fr=nf; print('len',L+1,'states',len(fr),flush=True)
t25=[('12112',1),('12211',-1),('21112',-1),('22111',1)]
#run(5,'12112',t25,6)
t36='+1*232123 -1*232132 -1*232213 +1*232231 +1*233212 -1*233221 -1*322123 +1*322132 +1*322213 -1*322231 -1*332212 +1*332221'
run(6,'123223',[(x.split('*')[1],int(x.split('*')[0])) for x in t36.split()],int(sys.argv[1]))
