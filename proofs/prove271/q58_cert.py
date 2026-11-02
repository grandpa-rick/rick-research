# Hand-checkable certificate: all saturated chains x->y for the Thm K pair, with bonds and reflecting roots.
exec(open('q58_achain.py').read().split("if __name__")[0])
S=setup('E',6,(0,0,0,1,0,0)); L,ix,ln,up,upb,C=S['L'],S['ix'],S['ln'],S['up'],S['upb'],S['C']
x=ix[C.apply_word([i-1 for i in (6,2,4,5,1,3,2,4)],L[0])]; y=ix[C.apply_word([i-1 for i in (4,5,6,3,2,4,5,1,3,2,4)],L[0])]
R=posroots(cartan('E',6))
def root_of(a,b):  # the positive root beta with s_beta L[a] = L[b]
    for bb,cc in R:
        p=sum(L[a][i]*cc[i] for i in range(6))
        if p>0:
            al=[tuple(cartan('E',6)[k][j] for k in range(6)) for j in range(6)]
            if tuple(L[a][k]-p*sum(bb[j]*al[j][k] for j in range(6)) for k in range(6))==L[b]: return bb,p
def chains(a):
    if a==y: return [[]]
    return [[(a,w,p)]+c for w,p in up[a] if (upb[w]>>y)&1 for c in chains(w)]
print('x =',L[x],'l=',ln[x],'  y =',L[y],'l=',ln[y])
for c in chains(x):
    print(' -> '.join(str(L[a]) for a,_,_ in c)+' -> '+str(L[y]))
    print('    bonds',[p for _,_,p in c],' roots',[''.join(map(str,root_of(a,w)[0])) for a,w,_ in c])
