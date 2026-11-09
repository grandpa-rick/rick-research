import json, sympy as sp
cells=json.load(open('cells5.json'))
def orbit(A,v,maxn=60):
    orb=[v]; fr=[v]
    while fr and len(orb)<maxn:
        new=[]
        for u in fr:
            for a in A:
                w=a*u
                if all(x>=0 for x in w): continue
                m=max(abs(x) for x in w); w=w/m
                if any(w==o for o in orb): continue
                orb.append(w); new.append(w)
        fr=new
    return orb, not fr
t=sp.symbols('t',positive=True)
for name,c in [('5_1',cells[0]),('5_2',cells[3])]:
    A=[sp.Matrix(a) for a in c['A']]
    print('==',name,c['cell'])
    for i in range(5):
      for j in range(5):
        if i==j: continue
        v=sp.eye(5)[:,i]-sp.Rational(1,20)*sp.eye(5)[:,j]
        orb,fin=orbit(A,v)
        if fin: print(i,j,len(orb),[list(o) for o in orb])
