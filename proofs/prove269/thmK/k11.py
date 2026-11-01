# (e): y in W_D x with D=D_L(y)  (x,y in W^J)  ==> (d) [x,y]_W subset W^J, P_{x,y}=1, [x,y] = W_D x.  All J.
import sys; sys.argv=['x']
exec(open('../prove269/thmK/k2.py').read().split('tests=')[0])
tests=[('A3',Agens(3)),('B3',Cgens(3)),('D4',Dgens(4)),('A4',Agens(4))]
for name,gens in tests:
    G=group(gens); N=G['N']; ln=G['ln']; r=G['r']; Pf=fullKL(G)
    tot=0; bad=0
    for k in range(r+1):
        for J in itertools.combinations(range(r),k):
            Wmin=[a for a in range(N) if all(ln[G['R'][a][j]]>ln[a] for j in J)]; Ws=set(Wmin)
            for x in Wmin:
                for y in Wmin:
                    if not le(G,x,y): continue
                    D=[i for i in range(r) if ln[G['L'][y][i]]<ln[y]]
                    orb={x}; fr=[x]
                    while fr:
                        nf=[]
                        for z in fr:
                            for i in D:
                                w=G['L'][z][i]
                                if w not in orb: orb.add(w); nf.append(w)
                        fr=nf
                    if y not in orb or any(ln[G["L"][x][i]]<ln[x] for i in D): continue
                    tot+=1
                    full={z for z in range(N) if le(G,x,z) and le(G,z,y)}
                    ok = full<=Ws and Pf[(x,y)]==(1,) and full==orb
                    bad+= not ok
    print(name,'(e)-pairs over all J',tot,'failures of (d)&P=1&[x,y]=W_D x:',bad)
