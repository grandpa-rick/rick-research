# Maximal (and other) parabolics, W^J-only: (d)-pairs, stuck pairs with gap>=2, rank sequences of (d)-intervals.
import sys, collections
src=open('q_cominuscule_scout.py').read().split('def boolean')[0]
exec(src)
def run(t,n,J,show=False):
    C=Cox(cartan(t,n)); lam,els=quotient(C,J)
    L=list(els); wr={m:els[m][0] for m in L}; wd={m:els[m][1] for m in L}; ln={m:els[m][2] for m in L}
    le=lambda a,b: C.le(wr[a],wr[b])
    up={a:[b for b in L if le(a,b)] for a in L}
    bad_d=0; stuck2=[]; rs=collections.Counter(); npairs=0
    for x in L:
        for y in up[x]:
            iv=[z for z in up[x] if le(z,y)]
            if any(C.le(C.apply_word(wd[z]+[j],C.rho),wr[y]) for z in iv for j in J): continue
            npairs+=1
            rk=tuple(sum(1 for z in iv if ln[z]==ln[x]+i) for i in range(ln[y]-ln[x]+1)); rs[rk]+=1
            DLy=[i for i in range(n) if wr[y][i]<0]
            if all(wr[x][i]<0 for i in DLy) and ln[y]-ln[x]>=2: stuck2.append((wd[x],wd[y]))
    print(t+str(n),'J=',J,'|W^J|',len(L),'(d)pairs',npairs,'stuck gap>=2:',len(stuck2),stuck2[:3]); 
    if show: print('   ranks:',dict(rs))
    return rs
import itertools
for t,n in [('A',4),('A',5),('B',4),('C',4),('D',4),('D',5),('F',4),('B',5),('C',5)]:
    for k in range(n):
        J=[i for i in range(n) if i!=k]
        run(t,n,J,show=True)
