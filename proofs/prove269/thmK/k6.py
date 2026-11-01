import sys, collections
exec(open('q_cominuscule_scout.py').read().split('def boolean')[0])
def run(t,n,J):
    C=Cox(cartan(t,n)); lam,els=quotient(C,J)
    L=list(els); wr={m:els[m][0] for m in L}; wd={m:els[m][1] for m in L}; ln={m:els[m][2] for m in L}
    le=lambda a,b: C.le(wr[a],wr[b])
    for x in L:
        for y in L:
            if not le(x,y) or ln[y]-ln[x]<2: continue
            iv=[z for z in L if le(x,z) and le(z,y)]
            if any(C.le(C.apply_word(wd[z]+[j],C.rho),wr[y]) for z in iv for j in J): continue
            DLy=[i for i in range(n) if wr[y][i]<0]; DLx=[i for i in range(n) if wr[x][i]<0]
            if not all(i in DLx for i in DLy): continue
            rk=tuple(sum(1 for z in iv if ln[z]==ln[x]+i) for i in range(ln[y]-ln[x]+1))
            xsy=[s for s in DLy if C.le(wr[x],C.refl(s,wr[y]))]
            print('x',wd[x],'y',wd[y],'DLx',DLx,'DLy',DLy,'ranks',rk,'s in DLy with x<=sy:',xsy, 'lam_x',x,'lam_y',y)
run('F',4,[0,2,3])
